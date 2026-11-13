"""Sauvegarde app-v30.py dans sauvegardes/ avec son empreinte SHA-256, sans jamais écraser.

Usage :
    python sauvegarde.py <etiquette> [--fichier CHEMIN] [--version vNN]

Exemple : python sauvegarde.py avant-etape9  ->  sauvegardes/app-v43-avant-etape9.py
La version est lue dans APP_VERSION, sauf si --version est donné.
Pour le suivi : python sauvegarde.py --suivi  ->  sauvegardes/SUIVI-v43.md
"""
import argparse, hashlib, re, shutil, sys
from pathlib import Path

for _flux in (sys.stdout, sys.stderr):              # accents lisibles dans la console Windows
    try:
        _flux.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJET = Path(__file__).resolve().parents[4]     # .claude/skills/suivi-ameliorations/scripts -> racine
DOSSIER = PROJET / 'sauvegardes'


def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def version_de(app):
    m = re.search(r"^APP_VERSION\s*=\s*['\"](v\d+)['\"]", app.read_text(encoding='utf-8'), re.M)
    if not m:
        sys.exit(f'APP_VERSION introuvable dans {app}. Donner --version vNN.')
    return m.group(1)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('etiquette', nargs='?', help='ex. avant-etape9, polish-final')
    p.add_argument('--fichier', default=str(PROJET / 'app-v30.py'))
    p.add_argument('--version', default=None)
    p.add_argument('--suivi', action='store_true', help='sauvegarder SUIVI-AMELIORATIONS.md en SUIVI-vNN.md')
    a = p.parse_args()

    app = PROJET / 'app-v30.py'
    version = a.version or version_de(app)
    if a.suivi:
        source, cible = PROJET / 'SUIVI-AMELIORATIONS.md', DOSSIER / f'SUIVI-{version}.md'
    else:
        if not a.etiquette or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', a.etiquette):
            sys.exit("Étiquette requise, en minuscules, chiffres et tirets (ex. avant-etape9).")
        source, cible = Path(a.fichier).resolve(), DOSSIER / f'app-{version}-{a.etiquette}.py'

    if not source.is_file():
        sys.exit(f'Fichier introuvable : {source}')
    DOSSIER.mkdir(exist_ok=True)
    if cible.exists():
        if sha256(cible) == sha256(source):
            print(f'Déjà sauvegardé, identique : {cible.relative_to(PROJET)}\nSHA-256 {sha256(cible)}')
            return
        conseil = ('Donner une autre version avec --version, ou vérifier pourquoi le suivi a changé.' if a.suivi
                   else 'Choisir une autre étiquette.')
        sys.exit(f'Refusé : {cible.relative_to(PROJET)} existe déjà avec un contenu différent. {conseil}')

    shutil.copy2(source, cible)
    h1, h2 = sha256(source), sha256(cible)
    if h1 != h2:
        sys.exit(f'ERREUR : la copie diffère de la source ({h1} / {h2}).')
    print(f'Sauvegarde : {cible.relative_to(PROJET)}\nSource     : {source.name}\nSHA-256    : {h2}')


if __name__ == '__main__':
    main()
