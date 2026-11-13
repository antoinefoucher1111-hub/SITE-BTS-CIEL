"""Examen blanc complet en invité (stockage en mémoire de session). Usage : python harness_examen.py <app.py> <dossier>"""
import os, re, sys
from streamlit.testing.v1 import AppTest

app, wd = sys.argv[1], sys.argv[2]
os.makedirs(wd, exist_ok=True); os.chdir(wd)
R = []


def check(n, c, d=''):
    R.append((n, bool(c))); print(('OK   ' if c else 'ECHEC') + ' ' + n + (f'  -> {d}' if d else ''), flush=True)


for th in ['sombre', 'gris', 'clair']:
    at = AppTest.from_file(app, default_timeout=120)
    at.session_state['nav_slug'] = 'examen'; at.session_state['theme'] = th
    at.run()
    next(b for b in at.button if "Démarrer" in (b.label or '')).click().run()
    check(f'[{th}] examen démarré sans exception', not at.exception and 'v31_exam' in at.session_state)
    radios = [r for r in at.radio if (r.key or '').startswith('v31_ex_') and r.key != 'v31_ex_fmt']
    n = len(radios)
    check(f'[{th}] questions sans réponse cochée', n > 0 and all(r.value is None for r in radios), n)
    for r in radios[: n // 2]:
        r.set_value(r.options[0])
    p0 = at.session_state['_profile'].get('points', 0) if '_profile' in at.session_state else 0
    next(b for b in at.button if 'Rendre ma copie' in (b.label or '')).click().run()
    check(f'[{th}] copie rendue sans exception', not at.exception, [str(e.value)[:120] for e in at.exception])
    notes = [str(mt.value) for mt in at.metric if mt.label == 'Note']
    check(f'[{th}] note sur 20 affichée', notes and notes[0].endswith('/ 20'), notes)
    d = at.session_state['_profile']
    h = d.get('history', [])
    check(f'[{th}] passage enregistré dans l\'historique', h and h[-1]['quiz'].startswith('Examen blanc') and h[-1]['total'] == n, h[-1] if h else None)
    sc = h[-1]['score'] if h else -1
    check(f'[{th}] XP : +4 par bonne réponse', d.get('points', 0) - p0 == 4 * sc, (p0, d.get('points'), sc))
    check(f'[{th}] carnet : erreurs ajoutées', len(d.get('errors', {})) == n - sc, (len(d.get('errors', {})), n, sc))
    at.run()
    check(f'[{th}] pas de double comptage', d.get('points', 0) - p0 == 4 * sc)

print(f"RESUME {sum(1 for r in R if r[1])} réussis / {sum(1 for r in R if not r[1])} échoués")
