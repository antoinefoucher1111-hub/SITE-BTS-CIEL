"""Non-régression : ouvre chaque page du menu dans chaque thème avec Streamlit AppTest.
Usage : python harness_pages.py <app.py> <dossier_de_travail> <sortie.json>
Le dossier de travail reçoit le stockage local de test (jamais Supabase : pas de secrets)."""
import json, os, re, sys, time, traceback
from streamlit.testing.v1 import AppTest

app, workdir, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(workdir, exist_ok=True)
os.chdir(workdir)
src = open(app, encoding='utf-8').read()
block = src[src.index('\nNAV = ['):src.index('NAV_ITEMS =')]
slugs = re.findall(r'\(\s*"([a-z0-9-]+)",\s*"', block)
themes = ['sombre', 'gris', 'clair']
res = []
for th in themes:
    for slug in slugs:
        t0 = time.time()
        r = {'theme': th, 'slug': slug}
        try:
            at = AppTest.from_file(app, default_timeout=120)
            at.session_state['nav_slug'] = slug
            at.session_state['theme'] = th
            at.run()
            r['exceptions'] = [str(e.value)[:300] for e in at.exception]
            r['errors'] = [str(e.value)[:200] for e in at.error]
            r['n_markdown'] = len(at.markdown)
            r['theme_after'] = at.session_state['theme'] if 'theme' in at.session_state else None
            r['slug_after'] = at.session_state['nav_slug'] if 'nav_slug' in at.session_state else None
        except Exception as e:
            r['crash'] = f'{type(e).__name__}: {str(e)[:300]}'
        r['sec'] = round(time.time() - t0, 1)
        res.append(r)
        print(th, slug, 'EXC' if r.get('exceptions') or r.get('crash') else 'ok', r['sec'], flush=True)
json.dump({'slugs': slugs, 'results': res}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('FIN', len(res))
