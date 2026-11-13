"""Accueil v41 : « Première fois ici ? » pour les nouveaux seulement, maîtrise réduite aux 3 plus faibles."""
import os, re, sys
from streamlit.testing.v1 import AppTest

app, wd = sys.argv[1], sys.argv[2]
os.makedirs(wd, exist_ok=True); os.chdir(wd)
R = []


def check(n, c, d=''):
    R.append((n, bool(c))); print(('OK   ' if c else 'ECHEC') + ' ' + n + (f'  -> {d}' if d else ''), flush=True)


def md(at):
    return '\n'.join(str(m.value) for m in at.markdown)


at = AppTest.from_file(app, default_timeout=120)
at.session_state['nav_slug'] = 'accueil'
at.run()
t = md(at)
check('nouvel utilisateur : « Première fois ici ? » affiché', 'Première fois ici' in t)
check('« J-xx » affiché une seule fois', len(re.findall(r'>J-\d+<|>Jour J<|>—<', t)) == 1, re.findall(r'>J-\d+<', t))
check('« Pour aller plus loin » : 3 boutons (examen, quiz, énoncés)',
      all(any(k in (b.key or '') for b in at.button) for k in ('home_examen', 'home_quiz', 'home_enonces')))
check('lien « Toutes mes matières dans Mes stats »', any((b.key or '') == 'home_stats' for b in at.button))
check('pas de ligne de maîtrise sans données', t.count("class='mastery-row'") == 0)

# Utilisateur qui a déjà révisé : un quiz complet (10 réponses)
at.session_state['nav_slug'] = 'quiz'
at.run()
for r in [r for r in at.radio if (r.key or '').startswith('v31_gq_')]:
    r.set_value(r.options[0])
next(b for b in at.button if 'Valider mes réponses' in (b.label or '')).click().run()
# 4 quiz de plus pour dépasser 5 réponses par matière dans plusieurs matières
for _ in range(4):
    next(b for b in at.button if 'Nouveau quiz' in (b.label or '')).click().run()
    for r in [r for r in at.radio if (r.key or '').startswith('v31_gq_')]:
        r.set_value(r.options[0])
    next(b for b in at.button if 'Valider mes réponses' in (b.label or '')).click().run()
at.session_state['nav_slug'] = 'accueil'
at.run()
t = md(at)
check('après des quiz : « Première fois ici ? » masqué', 'Première fois ici' not in t)
n = t.count("class='mastery-row'")
check('« À travailler en priorité » : 1 à 3 matières', 1 <= n <= 3, n)
check('accueil sans exception', not at.exception, [str(e.value)[:120] for e in at.exception])
print(f"RESUME {sum(1 for r in R if r[1])} réussis / {sum(1 for r in R if not r[1])} échoués")
