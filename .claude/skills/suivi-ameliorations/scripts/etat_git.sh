#!/usr/bin/env bash
# État Git de CIEL Studio, en LECTURE SEULE : aucune commande ne modifie le dépôt ni l'index.
# Usage : bash .claude/skills/suivi-ameliorations/scripts/etat_git.sh [--distant]
#   --distant : interroge aussi GitHub avec « git ls-remote » (lecture seule, demande le réseau).

export GIT_OPTIONAL_LOCKS=0          # empêche « git status » de réécrire l'index
cd "$(git rev-parse --show-toplevel)" || exit 1

echo "== Branche et HEAD"
echo "branche : $(git branch --show-current)"
echo "HEAD    : $(git log -1 --format='%h %s')"

echo; echo "== Branches locales"
git branch -vv

echo; echo "== Tags"
git tag -n1 | sed 's/^/  /'
for t in $(git tag); do echo "  $t -> $(git rev-parse --short "$t^{commit}")"; done

echo; echo "== Commits d'avance sur main"
git log --oneline main..HEAD

echo; echo "== main / origin/main (référence locale)"
echo "main        : $(git rev-parse --short main 2>/dev/null)"
echo "origin/main : $(git rev-parse --short origin/main 2>/dev/null)"

if [ "$1" = "--distant" ]; then
  echo; echo "== Distant (git ls-remote)"
  git ls-remote --heads --tags origin
fi

echo; echo "== Fichiers modifiés et non suivis"
git status --porcelain=v1 -uall
echo "ignorés : $(git status --porcelain=v1 --ignored -uall | grep -c '^!!')"

echo; echo "== Empreintes"
sha256sum app-v30.py SUIVI-AMELIORATIONS.md 2>/dev/null
grep -m1 -o "APP_VERSION = '[^']*'" app-v30.py
