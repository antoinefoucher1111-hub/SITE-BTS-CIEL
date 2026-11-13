"""<Ce que vérifie cette série, en une phrase.>
Usage : python harness_<nom>.py <app.py> <dossier_de_travail_hors_projet>
Jamais le vrai Supabase : aucun secret n'est chargé (stockage local dans le dossier de travail)."""
import os, sys
from streamlit.testing.v1 import AppTest

app, wd = sys.argv[1], sys.argv[2]
os.makedirs(wd, exist_ok=True)
os.chdir(wd)                      # le stockage local de test est créé ici, pas dans le projet
R = []


def check(nom, condition, detail=''):
    R.append((nom, bool(condition)))
    print(('OK   ' if condition else 'ECHEC') + ' ' + nom + (f'  -> {detail}' if detail else ''), flush=True)


def ouvrir(slug, theme='sombre'):
    at = AppTest.from_file(app, default_timeout=120)
    at.session_state['nav_slug'] = slug
    at.session_state['theme'] = theme
    at.run()
    return at


# ── Scénario 1 ─────────────────────────────────────────────
at = ouvrir('accueil')
check('accueil : aucune exception', not at.exception, [str(e.value)[:150] for e in at.exception])

# ── Scénario 2 : une action qui donne des XP ───────────────
# p0 = at.session_state['_profile'].get('points', 0) if '_profile' in at.session_state else 0
# next(b for b in at.button if (b.key or '') == '<clé>').click().run()
# p1 = at.session_state['_profile'].get('points', 0)
# check('+N XP ajoutés', p1 - p0 == N, p1 - p0)
# at.run()
# check('pas de double comptage', at.session_state['_profile'].get('points', 0) == p1)

# Ligne lue par lancer_tout.py : ne pas modifier son format.
print(f"RESUME {sum(1 for r in R if r[1])} réussis / {sum(1 for r in R if not r[1])} échoués")
