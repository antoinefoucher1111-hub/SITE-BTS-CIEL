"""Lance les séries de tests AppTest de CIEL Studio sur une COPIE de l'appli, hors du projet.

Usage :
    python lancer_tout.py [--app CHEMIN] [--series pages,comptes,...] [--sortie DOSSIER]

- --app     : appli à tester (par défaut : app-v30.py à la racine du projet).
- --series  : séries à lancer, séparées par des virgules (par défaut : toutes).
- --sortie  : dossier des journaux et des données de test, hors du projet (par défaut : un dossier temporaire).

Le Python qui exécute ce script doit avoir Streamlit et les dépendances de l'appli.
Code de sortie : 0 si tout est réussi, 1 sinon.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

for _flux in (sys.stdout, sys.stderr):              # accents lisibles dans la console Windows
    try:
        _flux.reconfigure(encoding='utf-8')
    except Exception:
        pass

ICI = Path(__file__).resolve().parent
PROJET = ICI.parents[3]          # .claude/skills/streamlit-apptest/scripts -> racine du projet
SERIES = ['pages', 'comptes', 'examen', 'accueil', 'alias', 'clarify', 'labs', 'securite']


def lancer(nom, app, sortie):
    journal = sortie / f'log_{nom}.txt'
    args = [sys.executable, str(ICI / f'harness_{nom}.py'), str(app), str(sortie / f'travail_{nom}')]
    if nom == 'pages':
        args.append(str(sortie / 'res_pages.json'))
    env = {**os.environ, 'PYTHONIOENCODING': 'utf-8'}
    t0 = time.time()
    with open(journal, 'w', encoding='utf-8') as f:
        code = subprocess.run(args, stdout=f, stderr=subprocess.STDOUT, env=env, cwd=str(sortie)).returncode
    texte = journal.read_text(encoding='utf-8', errors='replace')
    if nom == 'pages':           # format propre à harness_pages : « thème slug ok|EXC durée », puis « FIN n »
        ok = len(re.findall(r'^\S+ \S+ ok ', texte, re.M))
        ko = len(re.findall(r'^\S+ \S+ EXC ', texte, re.M))
        fini = bool(re.search(r'^FIN \d+', texte, re.M))
    else:
        m = re.findall(r'^RESUME (\d+) réussis / (\d+) échoués', texte, re.M)
        if m:
            ok, ko = int(m[-1][0]), int(m[-1][1])
        else:
            ok, ko = len(re.findall(r'^OK ', texte, re.M)), len(re.findall(r'^ECHEC', texte, re.M))
        fini = bool(m)
    return {'serie': nom, 'reussis': ok, 'echoues': ko, 'termine': fini and code == 0,
            'code': code, 'duree_s': round(time.time() - t0), 'journal': str(journal)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--app', default=str(PROJET / 'app-v30.py'))
    p.add_argument('--series', default=','.join(SERIES))
    p.add_argument('--sortie', default=None)
    a = p.parse_args()

    series = [s.strip() for s in a.series.split(',') if s.strip()]
    inconnues = [s for s in series if s not in SERIES]
    if inconnues:
        sys.exit(f'Séries inconnues : {inconnues}. Disponibles : {SERIES}')

    sortie = Path(a.sortie or tempfile.mkdtemp(prefix='ciel-tests-')).resolve()
    if sortie == PROJET or PROJET in sortie.parents:
        sys.exit('Refusé : le dossier de sortie doit être hors du projet (les tests créent des données locales).')
    sortie.mkdir(parents=True, exist_ok=True)

    copie = sortie / 'app' / 'app-v30.py'   # on teste une copie, jamais le fichier du projet
    copie.parent.mkdir(exist_ok=True)
    shutil.copy2(a.app, copie)
    paquet = Path(a.app).resolve().parent / 'ciel'          # v44 : modules importés par l'appli
    if paquet.is_dir():
        shutil.copytree(paquet, copie.parent / 'ciel', dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('__pycache__'))

    print(f'Appli testée : {a.app}\nCopie : {copie}\nJournaux : {sortie}\nSéries : {", ".join(series)}\n', flush=True)
    # « pages » est la plus longue : elle tourne en parallèle des autres, lancées l'une après l'autre
    with ThreadPoolExecutor(max_workers=1) as ex:
        fut_pages = ex.submit(lancer, 'pages', copie, sortie) if 'pages' in series else None
        autres = [lancer(s, copie, sortie) for s in series if s != 'pages']
        resultats = ([fut_pages.result()] if fut_pages else []) + autres

    total_ok = total_ko = 0
    for r in resultats:
        etat = 'OK   ' if r['echoues'] == 0 and r['termine'] else 'ECHEC'
        note = '' if r['termine'] else '  (série interrompue : lire le journal)'
        print(f"{etat} {r['serie']:8} {r['reussis']:4} réussis / {r['echoues']} échoués  [{r['duree_s']} s]{note}")
        total_ok += r['reussis']
        total_ko += r['echoues']
    tout_bon = total_ko == 0 and all(r['termine'] for r in resultats)
    print(f'\nTOTAL {total_ok} réussis / {total_ko} échoués' + ('' if tout_bon else '  — voir les journaux'))
    print(f'Journaux : {sortie}')
    (sortie / 'resume.json').write_text(json.dumps(resultats, ensure_ascii=False, indent=1), encoding='utf-8')
    sys.exit(0 if tout_bon else 1)


if __name__ == '__main__':
    main()
