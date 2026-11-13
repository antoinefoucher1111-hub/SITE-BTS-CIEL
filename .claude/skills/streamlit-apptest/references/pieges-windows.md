# Pièges rencontrés sous Windows

## Encodage de la sortie

La console Windows écrit en cp1252 par défaut. Un emoji dans un libellé d'onglet (par exemple 📊) fait planter `print()` avec `UnicodeEncodeError: 'charmap' codec can't encode character`. Ce n'est pas l'appli qui échoue, c'est l'affichage du test.

Solution : `PYTHONIOENCODING=utf-8`. `lancer_tout.py` le règle pour chaque série. Pour lancer un harnais à la main :

```bash
PYTHONIOENCODING=utf-8 .venv/Scripts/python .claude/skills/streamlit-apptest/scripts/harness_alias.py app-v30.py <dossier_hors_projet>
```

## « missing ScriptRunContext »

Avertissement normal d'AppTest, répété des centaines de fois dans les journaux. À ignorer, et à filtrer à la lecture : `grep -v ScriptRunContext`.

## Fins de ligne et empreintes

Le dépôt a `core.autocrlf=true`. `app-v30.py` est stocké en LF dans Git.

- `git archive` écrit les fichiers en CRLF sous Windows : la copie obtenue n'a pas la même empreinte SHA-256. Pour tester les octets exacts d'un commit ou d'un tag : `git -c core.autocrlf=false archive <ref> | tar -x -C <dossier>`.
- Un fichier réécrit en LF alors que Git l'avait extrait en CRLF peut apparaître « modifié » avec un diff vide (cas de `docs/manifest.webmanifest`). Ce n'est pas un vrai changement.

## Durée

Avec `default_timeout=120`, une page met 2 à 5 s. La série `pages` (132 ouvertures) dure 10 à 15 minutes, et l'ensemble 15 à 25 minutes. Toujours en arrière-plan.

## Python

`python3` peut renvoyer vers le raccourci du Microsoft Store, qui n'est pas un vrai Python. Utiliser le Python de l'environnement virtuel (`.venv/Scripts/python`) ou `python`.
