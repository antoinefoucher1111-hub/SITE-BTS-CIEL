"""Sécurité (v44, étape 0) : limite d'essais partagée entre sessions, anciens profils, mots de passe,
échappement des données de profil, planning E6 propre à chaque élève.
Usage : python harness_securite.py <app.py> <dossier_de_travail_hors_projet>
Stockage local de test uniquement (aucun secret Supabase n'est chargé)."""
import json, os, sys
from streamlit.testing.v1 import AppTest

app, wd = sys.argv[1], sys.argv[2]
os.makedirs(wd, exist_ok=True)
os.chdir(wd)
if os.path.exists('users_db_v2.json'):
    os.remove('users_db_v2.json')
R = []
CODE_ADMIN = 'code-admin-de-test-1234'


def check(nom, condition, detail=''):
    R.append((nom, bool(condition)))
    print(('OK   ' if condition else 'ECHEC') + ' ' + nom + (f'  -> {detail}' if detail else ''), flush=True)


def ouvrir(slug='compte'):
    at = AppTest.from_file(app, default_timeout=120)
    at.secrets['admin'] = {'code': CODE_ADMIN}
    at.session_state['nav_slug'] = slug
    at.run()
    return at


def btn(at, label):
    return next(b for b in at.button if label in (b.label or ''))


def messages(at):
    return [str(m.value) for m in list(at.error) + list(at.success) + list(at.warning) + list(at.info)]


def creer(at, nom, mdp):
    at.text_input(key='v33_new_name').input(nom)
    at.text_input(key='v33_new_pwd').input(mdp)
    at.text_input(key='v33_new_pwd2').input(mdp)
    btn(at, 'Créer mon compte').click().run()


def connecter(at, nom, mdp):
    at.text_input(key='v33_login_name').input(nom)
    at.text_input(key='v33_login_pwd').input(mdp)
    btn(at, 'Se connecter').click().run()


def db():
    return json.load(open('users_db_v2.json', encoding='utf-8'))


# 1. Mots de passe : 8 caractères pour un nouveau compte
A = ouvrir()
creer(A, 'eleve.court', '1234567')
check('mot de passe de 7 caractères refusé', A.session_state['current_user'] != 'eleve.court' and any('8 caractères' in m for m in messages(A)), messages(A)[-1:])
A = ouvrir()
creer(A, 'eleve1', 'bonmotdepasse')
check('mot de passe de 13 caractères accepté', A.session_state['current_user'] == 'eleve1')
check('aucune exception', not A.exception, [str(e.value)[:120] for e in A.exception])

# 2. Limite d'essais : survit à une nouvelle session, propre à chaque compte
B = ouvrir()
for i in range(5):
    connecter(B, 'eleve1', f'faux{i}')
check('5 échecs : session bloquée', any("Trop d'essais" in m for m in messages(B)) or B.session_state['_login_fail'] == 0, messages(B)[-1:])
C = ouvrir()                                        # nouvelle session = page rechargée
connecter(C, 'eleve1', 'bonmotdepasse')
check('nouvelle session : toujours bloquée, même avec le bon mot de passe',
      C.session_state['current_user'] != 'eleve1' and any("Trop d'essais" in m for m in messages(C)), messages(C)[-1:])
A2 = ouvrir()
creer(A2, 'eleve2', 'autremotdepasse')
D = ouvrir()
connecter(D, 'eleve2', 'autremotdepasse')
check('un autre compte n\'est pas bloqué', D.session_state['current_user'] == 'eleve2', messages(D)[-1:])

# 3. Code administrateur : compteur commun à toutes les sessions
for i in range(5):
    E = ouvrir()
    E.text_input(key='v35_admin_code').input(f'faux-code-{i}')
    btn(E, 'Déverrouiller').click().run()
F = ouvrir()
F.text_input(key='v35_admin_code').input(CODE_ADMIN)
btn(F, 'Déverrouiller').click().run()
check('code admin : bloqué après 5 échecs répartis sur 5 sessions', not F.session_state['_admin_ok'] if '_admin_ok' in F.session_state else True,
      messages(F)[-1:])
check('code admin : message d\'attente affiché', any("Trop d'essais" in m for m in messages(F)), messages(F)[-1:])

# 4. Ancien profil sans mot de passe : plus récupérable par création de compte
base = db()
base['ancien'] = {'username': 'ancien', 'points': 1234, 'history': [], 'role': 'Candidat Option A'}
json.dump(base, open('users_db_v2.json', 'w', encoding='utf-8'), ensure_ascii=False)
G = ouvrir()
creer(G, 'ancien', 'motdepasse-du-tiers')
apres = db()['ancien']
check('ancien profil : création refusée', G.session_state['current_user'] != 'ancien' and not apres.get('_pwd'), messages(G)[-1:])
check('ancien profil : message vers l\'administrateur', any('administrateur' in m for m in messages(G)), messages(G)[-1:])
check('ancien profil : données intactes', apres.get('points') == 1234)

# 5. Échappement des données de profil affichées en HTML (profil modifié directement dans le stockage de test)
base = db()
p = base['eleve2']
p['created_at'] = '<i>piege-date</i>'
p['badges'] = [{'id': 'pts_100', 'nom': '<b>piege-nom</b>', 'desc': '<u>piege-desc</u>', 'icon': '<s>x</s>', 'date': '<em>d</em>'}]
p['history'] = [{'date': '2026-11-01 10:00', 'quiz': '<script>piege-quiz</script>', 'score': 5, 'total': 10, 'details': {}},
                {'date': '2026-11-02 10:00', 'quiz': 'Examen blanc normal', 'score': 7, 'total': 10, 'details': {}}]
json.dump(base, open('users_db_v2.json', 'w', encoding='utf-8'), ensure_ascii=False)
H = ouvrir()
connecter(H, 'eleve2', 'autremotdepasse')
H.session_state['nav_slug'] = 'compte'             # après connexion, l'appli renvoie vers l'accueil
H.run()
html_compte = '\n'.join(str(m.value) for m in H.markdown)
check('Mon compte : date de création échappée (affichée sur 10 caractères)',
      '&lt;i&gt;piege' in html_compte and '<i>piege' not in html_compte)
H.session_state['nav_slug'] = 'stats'
H.run()
html_stats = '\n'.join(str(m.value) for m in H.markdown)
bruts = [t for t in ('<b>piege', '<u>piege', '<script>piege', '<s>x', '<em>d') if t in html_stats]
check('Mes stats : aucune balise piégée brute', not bruts, bruts)
check('Mes stats : l\'historique piégé est bien affiché, échappé', '&lt;script&gt;piege-quiz' in html_stats)
check('pages compte et stats sans exception', not H.exception, [str(e.value)[:120] for e in H.exception])

# 6. Planning E6 : propre à chaque élève, plus de fichier commun
I = ouvrir()
connecter(I, 'eleve2', 'autremotdepasse')
I.session_state['nav_slug'] = 'gantt'
I.run()
n0 = len(I.session_state['_profile'].get('e6_tasks') or [])
next(t for t in I.text_input if 'Nom de la tâche' in (t.label or '')).input('Tâche privée de eleve2')
btn(I, 'Ajouter au planning').click().run()
taches2 = db()['eleve2'].get('e6_tasks') or []
check('Gantt : tâche enregistrée dans le profil de l\'élève', any(t.get('nom') == 'Tâche privée de eleve2' for t in taches2), len(taches2))
check('Gantt : aucun fichier commun créé sur le serveur', not os.path.exists('e6_tasks_v7.json'))
J = ouvrir('gantt')                                  # invité
taches_invite = (J.session_state['_profile'].get('e6_tasks') if '_profile' in J.session_state else None) or []
check('Gantt : un autre visiteur ne voit pas la tâche', not any(t.get('nom') == 'Tâche privée de eleve2' for t in taches_invite))
check('Gantt : pages sans exception', not I.exception and not J.exception, [str(e.value)[:120] for e in list(I.exception) + list(J.exception)])

print(f"RESUME {sum(1 for r in R if r[1])} réussis / {sum(1 for r in R if not r[1])} échoués")
