"""Étape 7 : messages d'XP exacts, couleurs selon le score, historique vide, erreurs lisibles."""
import os, sys
from streamlit.testing.v1 import AppTest

app, wd = sys.argv[1], sys.argv[2]
os.makedirs(wd, exist_ok=True); os.chdir(wd)
R = []


def check(n, c, d=''):
    R.append((n, bool(c))); print(('OK   ' if c else 'ECHEC') + ' ' + n + (f'  -> {d}' if d else ''), flush=True)


def msgs(at):
    return [('succès', str(m.value)) for m in at.success] + [('info', str(m.value)) for m in at.info] + \
           [('alerte', str(m.value)) for m in at.warning] + [('erreur', str(m.value)) for m in at.error]


at = AppTest.from_file(app, default_timeout=120)
at.session_state['nav_slug'] = 'reseaux'
at.run()
b = next(b for b in at.button if 'Valider mes 10 réponses' in (b.label or ''))
b.click().run()
m = [t for k, t in msgs(at) if 'Résultat' in t]
check('quiz de cours : message « Résultat : x/10 »', m, m)
check('1er essai en invité : « +N XP » et avertissement invité', m and '+0 XP' in m[0] and 'invité' in m[0], m)
check('0/10 : plus affiché en vert (succès)', not any('Résultat' in t for t in [str(s.value) for s in at.success]))
check('plus de « enregistrés sur votre profil »', not any('enregistrés sur votre profil' in t for _, t in msgs(at)))
b = next(b for b in at.button if 'Valider mes 10 réponses' in (b.label or ''))
b.click().run()
m = [t for k, t in msgs(at) if 'Résultat' in t]
check('2e essai : « déjà gagnés lors d\'une tentative précédente »', m and 'déjà gagnés' in m[0], m)
check('aucune exception', not at.exception, [str(e.value)[:150] for e in at.exception])

at = AppTest.from_file(app, default_timeout=120)
at.session_state['nav_slug'] = 'stats'
at.run()
t = '\n'.join(str(i.value) for i in at.info)
check('Mes stats (historique vide) : nouveau message et bouton Grand quiz',
      'Aucun résultat enregistré' in t and any((x.key or '') == 'hist_vide_quiz' for x in at.button), t[:120])
check('plus de renvoi vers « Programme Semaine par Semaine »', 'Programme Semaine par Semaine' not in t)

print(f"RESUME {sum(1 for r in R if r[1])} réussis / {sum(1 for r in R if not r[1])} échoués")
