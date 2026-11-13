"""Sécurité de CIEL Studio : limite d'essais, échappement HTML, validation des sauvegardes importées.

Aucune dépendance à Streamlit : tout est testable avec pytest (voir tests/test_securite.py).
"""
import html
import re
import threading
import time

# ───────────────────────────── limite d'essais ─────────────────────────────


class LimiteurEssais:
    """Compte les échecs par clé (« login:<compte> », « secours:<compte> », « admin ») pour tout le serveur.

    Après `seuil` échecs, la clé est bloquée `attente` secondes ; chaque nouveau blocage double l'attente,
    sans dépasser `attente_max`. Une clé sans échec depuis `oubli` secondes repart de zéro.
    Une seule instance doit être partagée par toutes les sessions (st.cache_resource dans l'appli).
    """

    def __init__(self, seuil=5, attente=30, attente_max=300, oubli=3600, horloge=time.time, max_cles=5000):
        self.seuil, self.attente_base, self.attente_max, self.oubli = seuil, attente, attente_max, oubli
        self.horloge, self.max_cles = horloge, max_cles
        self._etat = {}                     # clé -> {'n': échecs, 'palier': blocages, 'jusqu': fin de blocage, 'dernier': date}
        self._verrou = threading.Lock()

    def _purger(self, maintenant):
        if len(self._etat) <= self.max_cles:
            return
        for cle in [c for c, e in self._etat.items() if maintenant - e['dernier'] > self.oubli and e['jusqu'] <= maintenant]:
            del self._etat[cle]

    def attente(self, cle):
        """Secondes à attendre avant un nouvel essai (0 si l'essai est permis)."""
        with self._verrou:
            e = self._etat.get(cle)
            if not e:
                return 0
            reste = e['jusqu'] - self.horloge()
            return int(reste) + 1 if reste > 0 else 0

    def echec(self, cle):
        """Enregistre un échec. Renvoie l'attente imposée (0 si pas encore bloqué)."""
        with self._verrou:
            maintenant = self.horloge()
            e = self._etat.get(cle)
            if not e or maintenant - e['dernier'] > self.oubli:
                e = {'n': 0, 'palier': 0, 'jusqu': 0.0, 'dernier': maintenant}
            e['n'] += 1
            e['dernier'] = maintenant
            attente = 0
            if e['n'] >= self.seuil:
                attente = min(self.attente_base * (2 ** e['palier']), self.attente_max)
                e['jusqu'] = maintenant + attente
                e['palier'] += 1
                e['n'] = 0
            self._etat[cle] = e
            self._purger(maintenant)
            return attente

    def succes(self, cle):
        """Un essai réussi efface l'historique de la clé."""
        with self._verrou:
            self._etat.pop(cle, None)


def message_attente(secondes):
    if secondes >= 120:
        return f"Trop d'essais. Réessaie dans {(secondes + 59) // 60} minutes."
    return f"Trop d'essais. Attends {secondes} secondes."


# ───────────────────────────── HTML ─────────────────────────────

def echapper(texte):
    """Texte sûr à insérer dans du HTML (st.markdown avec unsafe_allow_html=True)."""
    return html.escape(str(texte), quote=True)


# ───────────────────────────── mots de passe ─────────────────────────────

LONGUEUR_MIN_MDP = 8


def mot_de_passe_valide(mdp):
    """Règle des NOUVEAUX mots de passe (les mots de passe existants ne sont pas revérifiés)."""
    return isinstance(mdp, str) and len(mdp) >= LONGUEUR_MIN_MDP


# ───────────────────────────── import de sauvegarde ─────────────────────────────

TAILLE_MAX_SAUVEGARDE = 2 * 1024 * 1024          # octets
_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
_MAX_TEXTE, _MAX_LISTE, _MAX_PROFONDEUR = 500, 5000, 6

# Badges réellement attribués par l'appli (add_user_points) : seuls ceux-là sont repris d'une sauvegarde,
# avec leurs textes officiels. Garder cette liste alignée sur add_user_points si un badge y est ajouté.
BADGES_OFFICIELS = {
    'pts_100': {'id': 'pts_100', 'nom': 'Centurion CIEL', 'desc': 'Cap des 100 points XP franchi !', 'icon': '💯'},
    'pts_300': {'id': 'pts_300', 'nom': "Maître de l'Atelier", 'desc': 'Cap des 300 points XP franchi !', 'icon': '🏆'},
}

# Clés de profil acceptées dans une sauvegarde importée, avec leur type attendu.
CLES_SAUVEGARDE = {
    'role': str, 'created_at': str, 'last_login': str, 'level': str, 'notes': str, 'exam_date': str,
    'points': int, 'history': list, 'badges': list, 'days': list, 'fc_mastered': list,
    'domain_mastery': dict, 'completed_activities': dict, 'prefs': dict, 'srs': dict, 'vocab': dict,
    'errors': dict, 'qstats': dict, 'cstats': dict, 'activity': dict, 'e6_tasks': list, 'schema_version': int,
}


def _nettoyer(v, profondeur=0):
    """Ne garde que des valeurs JSON simples, de taille bornée. Renvoie None pour ce qui est rejeté."""
    if profondeur > _MAX_PROFONDEUR:
        return None
    if isinstance(v, bool) or v is None:
        return v
    if isinstance(v, (int, float)):
        return v if v == v and abs(v) < 1e12 else None          # rejette NaN et valeurs absurdes
    if isinstance(v, str):
        return v[:_MAX_TEXTE]
    if isinstance(v, list):
        out = [_nettoyer(x, profondeur + 1) for x in v[:_MAX_LISTE]]
        return [x for x in out if x is not None]
    if isinstance(v, dict):
        out = {}
        for k, x in list(v.items())[:_MAX_LISTE]:
            if isinstance(k, str):
                x = _nettoyer(x, profondeur + 1)
                if x is not None:
                    out[k[:_MAX_TEXTE]] = x
        return out
    return None


def _historique(liste):
    out = []
    for h in liste:
        if not isinstance(h, dict):
            continue
        try:
            total = int(h.get('total', 0))
            score = float(h.get('score', 0))
        except (TypeError, ValueError):
            continue
        if total <= 0 or not 0 <= score <= total:
            continue
        out.append({'date': str(h.get('date', ''))[:19], 'quiz': str(h.get('quiz', ''))[:120],
                    'score': int(score) if score == int(score) else score, 'total': total,
                    'details': _nettoyer(h['details']) if isinstance(h.get('details'), dict) else {}})
    return out


def _badges(liste):
    out, vus = [], set()
    for b in liste:
        if isinstance(b, dict) and b.get('id') in BADGES_OFFICIELS and b['id'] not in vus:
            vus.add(b['id'])
            date = str(b.get('date', ''))
            out.append({**BADGES_OFFICIELS[b['id']], 'date': date if _DATE.match(date) else ''})
    return out


def valider_sauvegarde(brut, taille_octets=None):
    """Vérifie un fichier de sauvegarde déjà décodé (json.load).

    Renvoie (True, profil_nettoyé) ou (False, message). Le profil nettoyé ne contient jamais de clé
    commençant par « _ » (mot de passe, code de secours…) ni de clé inconnue : l'appli y remet ensuite
    le pseudo, le mot de passe et le code de secours du compte connecté.
    La valeur de « points » est gardée telle quelle si c'est un entier positif (logique d'XP inchangée).
    """
    if taille_octets is not None and taille_octets > TAILLE_MAX_SAUVEGARDE:
        return False, "Ce fichier est trop gros pour être une sauvegarde CIEL Studio."
    prof = brut.get('user_profile') if isinstance(brut, dict) else None
    if not isinstance(prof, dict) or 'points' not in prof:
        return False, "Ce fichier n'est pas une sauvegarde CIEL Studio."
    try:
        points = int(prof['points'])
    except (TypeError, ValueError):
        return False, "Ce fichier contient des points illisibles."
    if points < 0 or points > 10 ** 9:
        return False, "Ce fichier contient des points impossibles."

    propre = {}
    for cle, typ in CLES_SAUVEGARDE.items():
        if cle not in prof:
            continue
        v = prof[cle]
        if typ is int:
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                continue
            v = int(v)
        elif not isinstance(v, typ):
            continue
        v = _nettoyer(v)
        if v is not None:
            propre[cle] = v
    propre['points'] = points
    if 'history' in propre:
        propre['history'] = _historique(prof['history'])
    if 'badges' in propre:
        propre['badges'] = _badges(prof['badges'])
    if 'exam_date' in propre and not _DATE.match(propre['exam_date']):
        del propre['exam_date']
    if 'days' in propre:
        propre['days'] = [j for j in propre['days'] if isinstance(j, str) and _DATE.match(j)]
    return True, propre
