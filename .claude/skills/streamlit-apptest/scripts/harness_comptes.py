"""Comptes + Supabase SIMULÉ (serveur local en mémoire, jamais le vrai Supabase).
Usage : python harness_comptes.py <app.py> <dossier_de_travail>"""
import json, os, re, sys, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from streamlit.testing.v1 import AppTest

app, workdir = sys.argv[1], sys.argv[2]
os.makedirs(workdir, exist_ok=True)
os.chdir(workdir)

DB, CALLS = {}, []


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body=None):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        if body is not None:
            self.wfile.write(json.dumps(body).encode())

    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        CALLS.append(('GET', q.get('select', [''])[0], self.headers.get('apikey')))
        sel = q.get('select', [''])[0]
        if 'id' in q:
            uid = q['id'][0].replace('eq.', '')
            return self._send(200, [{'data': DB[uid]}] if uid in DB else [])
        if sel.startswith('lb:'):
            return self._send(200, [{'lb': v.get('lb')} for v in DB.values()])
        if sel == 'id':
            return self._send(200, [{'id': k} for k in DB])
        return self._send(200, [])

    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0)); body = json.loads(self.rfile.read(n))
        CALLS.append(('POST', body['id'], self.headers.get('apikey')))
        DB[body['id']] = body['data']
        self._send(201)

    def do_DELETE(self):
        q = parse_qs(urlparse(self.path).query); uid = q['id'][0].replace('eq.', '')
        CALLS.append(('DELETE', uid, self.headers.get('apikey')))
        DB.pop(uid, None)
        self._send(204)


srv = ThreadingHTTPServer(('127.0.0.1', 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{srv.server_address[1]}'
R = []


def check(name, cond, detail=''):
    R.append((name, bool(cond), str(detail)[:200]))
    print(('OK   ' if cond else 'ECHEC') + ' ' + name + ('  -> ' + str(detail)[:200] if detail else ''), flush=True)


def new_at(slug):
    at = AppTest.from_file(app, default_timeout=120)
    at.secrets['supabase'] = {'url': URL, 'key': 'cle-de-test'}
    at.session_state['nav_slug'] = slug
    return at


def goto(at, slug):
    at.session_state['nav_slug'] = slug
    at.run()
    check(f'page {slug} sans exception', not at.exception, [str(e.value)[:150] for e in at.exception])


def btn(at, label):
    for b in at.button:
        if label in (b.label or ''):
            return b
    raise KeyError(label)


def text(at):
    return '\n'.join(str(m.value) for m in at.markdown)


PSEUDO, PWD = 'testciel', 'motdepasse1'

# 1. Création de compte
A = new_at('compte'); A.run()
check('page compte (invité) sans exception', not A.exception)
A.text_input(key='v33_new_name').input(PSEUDO)
A.text_input(key='v33_new_pwd').input(PWD)
A.text_input(key='v33_new_pwd2').input(PWD)
btn(A, 'Créer mon compte').click().run()
check('création : pas d\'exception', not A.exception, [str(e.value)[:150] for e in A.exception])
check('création : utilisateur connecté', A.session_state['current_user'] == PSEUDO, A.session_state['current_user'])
check('création : profil écrit dans Supabase simulé', len(DB) == 1, list(DB))
uid = next(iter(DB), None)
check('création : mot de passe non stocké en clair', PWD not in json.dumps(DB.get(uid, {})))
check('création : appels avec la clé configurée', all(c[2] == 'cle-de-test' for c in CALLS))

# 2. Quiz (réponses : 1re option partout), score -> XP, historique, carnet d'erreurs
pts0 = DB[uid].get('points', 0); hist0 = len(DB[uid].get('history', [])); err0 = len(DB[uid].get('errors', {}))
goto(A, 'quiz')
radios = [r for r in A.radio if (r.key or '').startswith('v31_gq_')]
check('quiz : 10 questions sans réponse cochée', len(radios) == 10 and all(r.value is None for r in radios), [r.value for r in radios])
for r in radios:
    r.set_value(r.options[0])
btn(A, 'Valider mes réponses').click().run()
m = re.search(r'(\d+) / 10 — soit', text(A))
check('quiz : score affiché', m, text(A)[:120])
score = int(m.group(1)) if m else -1
d = DB[uid]
check('XP : +3 points par bonne réponse', d.get('points', 0) - pts0 == 3 * score, (pts0, d.get('points'), score))
check('stats : historique +1 passage', len(d.get('history', [])) - hist0 == 1, len(d.get('history', [])))
check('stats : score enregistré', d['history'][-1].get('score') == score and d['history'][-1].get('total') == 10, d['history'][-1])
check('carnet : une entrée par erreur', len(d.get('errors', {})) - err0 == 10 - score, (len(d.get('errors', {})), score))
# relancer la page ne doit pas recompter
A.run()
check('XP : pas de double comptage au rechargement', DB[uid].get('points', 0) - pts0 == 3 * score, DB[uid].get('points'))

# 3. Préférence de thème enregistrée
A.radio(key='theme').set_value('clair').run()
check('thème : choix enregistré dans le profil', (DB[uid].get('prefs') or {}).get('theme') == 'clair', DB[uid].get('prefs'))

# 4. Nouvelle session : mauvais mot de passe, puis bon
B = new_at('compte'); B.run()
B.text_input(key='v33_login_name').input(PSEUDO)
B.text_input(key='v33_login_pwd').input('mauvais-mdp')
btn(B, 'Se connecter').click().run()
check('connexion : mauvais mot de passe refusé', B.session_state['current_user'] != PSEUDO and len(B.error) > 0, [e.value for e in B.error])
B.text_input(key='v33_login_name').input(PSEUDO)
B.text_input(key='v33_login_pwd').input(PWD)
btn(B, 'Se connecter').click().run()
check('connexion : bon mot de passe accepté', B.session_state['current_user'] == PSEUDO, B.session_state['current_user'])
B.run()
check('connexion : thème du profil rechargé (clair)', B.session_state['theme'] == 'clair', B.session_state['theme'])
pd = B.session_state['_profile']
check('connexion : XP rechargée', pd.get('points') == DB[uid].get('points'), (pd.get('points'), DB[uid].get('points')))
check('connexion : historique rechargé', len(pd.get('history', [])) == len(DB[uid].get('history', [])))
check('connexion : carnet rechargé', len(pd.get('errors', {})) == len(DB[uid].get('errors', {})))

# 5. Pages qui lisent ces données
for slug in ['accueil', 'stats', 'erreurs', 'scores', 'classement', 'compte', 'seance']:
    goto(B, slug)
goto(B, 'erreurs')
check('carnet : page affiche les questions ratées', (10 - score == 0) or len([r for r in B.radio if (r.key or '').startswith('v31_err_')]) > 0,
      len(B.radio))
goto(B, 'stats')
check('stats : page renseignée (pas le message invité)', 'mode invité' not in text(B))

ok = sum(1 for r in R if r[1]); ko = [r for r in R if not r[1]]
print(f'\nRESUME {ok} réussis / {len(ko)} échoués')
print('Appels Supabase simulé :', {k: sum(1 for c in CALLS if c[0] == k) for k in ('GET', 'POST', 'DELETE')})
json.dump({'checks': R, 'calls': len(CALLS)}, open(os.path.join(workdir, 'comptes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
srv.shutdown()
