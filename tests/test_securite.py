"""Tests unitaires de ciel/securite.py (sans Streamlit). Lancer : python -m pytest tests"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ciel.securite import (BADGES_OFFICIELS, LONGUEUR_MIN_MDP, TAILLE_MAX_SAUVEGARDE, LimiteurEssais, echapper,
                           message_attente, mot_de_passe_valide, valider_sauvegarde)


class Horloge:
    def __init__(self):
        self.t = 1000.0

    def __call__(self):
        return self.t


# ── limite d'essais ──────────────────────────────────────────

def test_bloque_apres_5_echecs():
    h = Horloge()
    lim = LimiteurEssais(horloge=h)
    for _ in range(4):
        assert lim.echec('login:a') == 0
    assert lim.attente('login:a') == 0
    assert lim.echec('login:a') == 30
    assert lim.attente('login:a') == 31 or lim.attente('login:a') == 30


def test_attente_double_et_plafonne():
    h = Horloge()
    lim = LimiteurEssais(horloge=h)
    attentes = []
    for _ in range(6):
        for _ in range(5):
            a = lim.echec('admin')
        attentes.append(a)
        h.t += a + 1
    assert attentes == [30, 60, 120, 240, 300, 300]


def test_cles_independantes():
    lim = LimiteurEssais(horloge=Horloge())
    for _ in range(5):
        lim.echec('login:a')
    assert lim.attente('login:a') > 0
    assert lim.attente('login:b') == 0


def test_succes_efface():
    lim = LimiteurEssais(horloge=Horloge())
    for _ in range(4):
        lim.echec('login:a')
    lim.succes('login:a')
    assert lim.echec('login:a') == 0          # le compteur est reparti de zéro


def test_oubli_apres_une_heure():
    h = Horloge()
    lim = LimiteurEssais(horloge=h)
    for _ in range(5):
        lim.echec('login:a')                  # palier 1 atteint
    h.t += 4000
    for _ in range(4):
        assert lim.echec('login:a') == 0
    assert lim.echec('login:a') == 30         # repart au premier palier


def test_purge_bornee():
    h = Horloge()
    lim = LimiteurEssais(horloge=h, max_cles=10)
    for i in range(30):
        lim.echec(f'login:{i}')
    h.t += 4000
    lim.echec('login:nouveau')
    assert len(lim._etat) <= 11


def test_message_attente():
    assert '30 secondes' in message_attente(30)
    assert '5 minutes' in message_attente(300)


# ── HTML et mots de passe ────────────────────────────────────

def test_echapper():
    assert echapper("<img src=x onerror=alert(1)>") == "&lt;img src=x onerror=alert(1)&gt;"
    assert echapper("L'élève & \"moi\"") == "L&#x27;élève &amp; &quot;moi&quot;"
    assert echapper(12) == "12"


def test_mot_de_passe():
    assert LONGUEUR_MIN_MDP == 8
    assert not mot_de_passe_valide('1234567')
    assert mot_de_passe_valide('12345678')
    assert not mot_de_passe_valide(None)


# ── import de sauvegarde ─────────────────────────────────────

def _sauvegarde(**prof):
    base = {'points': 120, 'history': [], 'badges': []}
    base.update(prof)
    return {'user_profile': base}


def test_refuse_fichier_etranger():
    assert valider_sauvegarde([1, 2])[0] is False
    assert valider_sauvegarde({'autre': 1})[0] is False
    assert valider_sauvegarde({'user_profile': {'history': []}})[0] is False


def test_refuse_fichier_trop_gros():
    ok, msg = valider_sauvegarde(_sauvegarde(), taille_octets=TAILLE_MAX_SAUVEGARDE + 1)
    assert not ok and 'trop gros' in msg


def test_points_gardes_tels_quels():
    ok, p = valider_sauvegarde(_sauvegarde(points=4567))
    assert ok and p['points'] == 4567
    assert valider_sauvegarde(_sauvegarde(points='abc'))[0] is False
    assert valider_sauvegarde(_sauvegarde(points=-5))[0] is False


def test_retire_secrets_et_cles_inconnues():
    ok, p = valider_sauvegarde(_sauvegarde(_pwd='x', _recovery='y', _admin_ok=True, inconnu=1, username='autre', public=True))
    assert ok
    assert not any(k.startswith('_') for k in p)
    for k in ('inconnu', 'username', 'public'):
        assert k not in p


def test_badges_reconstruits_depuis_la_liste_officielle():
    piege = {'id': 'pts_100', 'nom': '<script>x</script>', 'desc': '<b>', 'icon': '<img>', 'date': '<i>'}
    ok, p = valider_sauvegarde(_sauvegarde(badges=[piege, {'id': 'faux', 'nom': 'x'}, piege]))
    assert ok and len(p['badges']) == 1
    b = p['badges'][0]
    assert b['nom'] == BADGES_OFFICIELS['pts_100']['nom'] and b['date'] == ''


def test_historique_normalise():
    hist = [{'date': '2026-11-01 10:00', 'quiz': 'Q' * 500, 'score': 7, 'total': 10, 'details': {'a': 1}},
            {'date': 'x', 'quiz': 'mauvais', 'score': 12, 'total': 10},
            {'quiz': 'sans total', 'score': 1},
            'pas un dict']
    ok, p = valider_sauvegarde(_sauvegarde(history=hist))
    assert ok and len(p['history']) == 1
    assert len(p['history'][0]['quiz']) == 120 and p['history'][0]['score'] == 7


def test_dates_et_types():
    ok, p = valider_sauvegarde(_sauvegarde(exam_date='<b>demain</b>', days=['2026-11-01', '<i>', 3],
                                           srs='pas un dict', notes='x' * 2000))
    assert ok
    assert 'exam_date' not in p and p['days'] == ['2026-11-01']
    assert 'srs' not in p and len(p['notes']) == 500
    ok, p = valider_sauvegarde(_sauvegarde(exam_date='2026-12-09'))
    assert p['exam_date'] == '2026-12-09'


def test_valeurs_imbriquees_bornees():
    profond = {'a': {'b': {'c': {'d': {'e': {'f': {'g': {'h': 1}}}}}}}}
    ok, p = valider_sauvegarde(_sauvegarde(errors=profond, qstats={'m': [1, float('nan'), 2]}))
    assert ok
    assert p['qstats'] == {'m': [1, 2]}
