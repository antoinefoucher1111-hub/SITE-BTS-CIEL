"""Anciennes adresses (?p=...) et contenus regroupés. Usage : python harness_alias.py <app.py> <dossier>"""
import os, sys
from streamlit.testing.v1 import AppTest

app, wd = sys.argv[1], sys.argv[2]
os.makedirs(wd, exist_ok=True); os.chdir(wd)
R = []


def check(n, c, d=''):
    R.append((n, bool(c))); print(('OK   ' if c else 'ECHEC') + ' ' + n + (f'  -> {d}' if d else ''), flush=True)


def txt(at):
    return '\n'.join(str(m.value) for m in at.markdown) + '\n'.join(str(e.label) for e in at.expander) + \
        '\n'.join(str(t.label) for t in at.tabs) + '\n'.join(str(s.value) for s in at.subheader)


ALIAS = {'maths-resume': ('formulaire', 'Résumé express'), 'anglais-tech': ('datasheets', "Glossaire de l'anglais technique"),
         'planning': ('semaines', "Vue d'ensemble du planning"), 'pcap': ('wireshark', 'Captures commentées'),
         'scores': ('stats', 'Historique, radar et badges'), 'videos': ('ressources', 'Vidéos de cours'),
         'liens': ('ressources', 'Liens utiles')}
for old, (new, marque) in ALIAS.items():
    # 1. adresse ?p=ancienne
    at = AppTest.from_file(app, default_timeout=120)
    at.query_params['p'] = old
    at.run()
    check(f'?p={old} -> {new}', not at.exception and at.session_state['nav_slug'] == new, at.session_state['nav_slug'] if 'nav_slug' in at.session_state else None)
    check(f'?p={old} : contenu regroupé présent ({marque})', marque in txt(at))
    # 2. ancienne page restée en mémoire de session
    at2 = AppTest.from_file(app, default_timeout=120)
    at2.session_state['nav_slug'] = old
    at2.run()
    check(f'session nav_slug={old} -> {new}', not at2.exception and at2.session_state['nav_slug'] == new)

# Contenus regroupés : on retrouve les deux parties
for slug, attendus in {'wireshark': ['Décodeur de trame', 'Captures commentées', 'Décryptage des champs du paquet', 'Handshake'],
                       'ressources': ['Vidéos de cours', 'Liens utiles', 'Leçons Vidéo', 'Cours Magistraux & Fiches'],
                       'stats': ['Mes stats', 'Historique, radar et badges', 'Radar de Compétences'],
                       'formulaire': ['Résumé express', 'Suites arithmétiques & géométriques'],
                       'datasheets': ["Glossaire de l'anglais technique", 'Throughput'],
                       'semaines': ["Vue d'ensemble du planning", 'Semaine 1']}.items():
    at = AppTest.from_file(app, default_timeout=120)
    at.session_state['nav_slug'] = slug
    at.run()
    t = txt(at)
    manque = [a for a in attendus if a not in t]
    check(f'page {slug} : toutes les parties présentes', not at.exception and not manque, manque)
    if slug == 'stats':
        noms = [tb.label for tb in at.tabs]
        check('stats : onglet « Gestion du compte » retiré (il renvoyait vers Mon compte)', not any('Gestion du Compte' in n for n in noms), noms)

print(f"RESUME {sum(1 for r in R if r[1])} réussis / {sum(1 for r in R if not r[1])} échoués")
