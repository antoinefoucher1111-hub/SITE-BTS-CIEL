---
name: streamlit-apptest
description: Tester CIEL Studio (app-v30.py) avec streamlit.testing.v1.AppTest — 44 pages × 3 thèmes, comptes avec un faux Supabase local, examen blanc, accueil, anciennes adresses ?p=, messages d'XP et 26 exercices de terminal. À utiliser avant tout commit qui modifie app-v30.py, après une correction de bug, ou quand on demande « lance les tests », « non-régression », « vérifie que rien n'est cassé ».
---

# streamlit-apptest : tests automatiques de CIEL Studio

Ce Skill contient les 7 séries de tests qui ont validé les versions v36 à v43 (284 vérifications sur une copie propre du tag `v43`), ainsi que la méthode pour s'en servir.

## Règles absolues

1. **Jamais le vrai Supabase.** Les tests ne chargent aucun secret. `harness_comptes.py` lance son propre faux serveur `/rest/v1/profiles` sur `127.0.0.1`. Aucune autre série ne parle au réseau.
2. **Tester une copie, hors du projet.** `scripts/lancer_tout.py` copie `app-v30.py` dans un dossier temporaire et y place les données de test. Ne jamais créer `users_db_v2.json` ni `e6_tasks_v7.json` dans le projet.
3. **Ne jamais modifier l'appli pour faire passer un test.** Si un test échoue, chercher d'abord qui a tort, l'appli ou le test, puis le dire clairement.
4. **Chiffres exacts uniquement.** Un compte rendu donne les nombres lus dans les journaux. Ce qui n'a pas été lancé est dit « non testé ».

## Prérequis

- Un Python avec Streamlit et les dépendances de l'appli. Par exemple, à la racine du projet (`.venv/` est ignoré par Git) :
  ```bash
  python -m venv .venv
  .venv/Scripts/python -m pip install -r requirements.txt
  ```
- Sous Windows, la sortie doit être en UTF-8. `lancer_tout.py` règle `PYTHONIOENCODING=utf-8` pour chaque série ; sinon un emoji dans un libellé fait planter l'affichage du test (voir `references/pieges-windows.md`).

## Méthode

1. **Syntaxe** : `python -c "import ast;ast.parse(open('app-v30.py',encoding='utf-8').read())"`
2. **Série ciblée**, choisie avec le tableau ci-dessous :
   ```bash
   .venv/Scripts/python .claude/skills/streamlit-apptest/scripts/lancer_tout.py --series comptes
   ```
3. **Non-régression complète** avant tout commit (15 à 25 minutes, à lancer en arrière-plan) :
   ```bash
   .venv/Scripts/python .claude/skills/streamlit-apptest/scripts/lancer_tout.py
   ```
4. **Compte rendu** : le résumé de `lancer_tout.py` (réussis et échoués par série), le dossier des journaux, et la liste de ce qui n'a pas été testé.

## Quelle série pour quelle modification

| Modification | Séries |
|---|---|
| N'importe quelle page, CSS dans un `st.markdown`, menu | `pages` (44 × 3 thèmes) |
| Comptes, mots de passe, stockage, `_SupabaseStore`, profil, thème enregistré | `comptes` |
| Examen blanc, minuteur, barème | `examen` |
| Accueil, « Première fois ici ? », maîtrise | `accueil` |
| `NAV`, `NAV_ALIAS`, pages regroupées, adresses `?p=` | `alias` |
| Messages de résultat et d'XP, `xp_txt`, historique vide | `clarify` |
| Exercices de terminal (`render_extended_lab`, ateliers Cyber A/B/C) | `labs` |
| Connexion, limite d'essais, code admin, import de sauvegarde, planning E6, `ciel/securite.py` | `securite` + `python -m pytest tests` |
| `add_user_points`, système d'XP | `comptes`, `examen`, `clarify`, `labs` |
| Avant un commit, un tag ou une fusion | toutes |

Résultats de référence (v44, étape 0) : pages 132, comptes 32, examen 24, accueil 8, alias 28, clarify 8, labs 52, securite 19. Soit 303 réussis, 0 échoué. Tests unitaires (`python -m pytest tests`, outil listé dans `requirements-dev.txt`) : 20 réussis.

Depuis la v44, l'appli importe le paquet `ciel/` : `lancer_tout.py` le copie à côté de la copie testée. Pour lancer un harnais à la main, copier aussi `ciel/` à côté de l'appli.

## Ce qu'AppTest ne voit pas

AppTest exécute le script Python sans rien afficher dans un navigateur. Passer au navigateur (plugin Playwright ou navigateur intégré, appli lancée en local) pour :

- les contrastes et couleurs des 3 thèmes ;
- l'affichage à 375 px et les débordements ;
- les formules KaTeX ;
- le minuteur de l'examen dans `st.iframe` ;
- le CSS en général.

Ne jamais écrire « testé » pour ces points sans vérification dans le navigateur. Détail : `references/limites.md`.

## Références

- `references/apptest-api.md` : utilisation d'AppTest dans ce projet.
- `references/carte-ciel.md` : pages, thèmes, clés de session et de widgets, XP.
- `references/limites.md` : couverture d'AppTest et vérifications manuelles.
- `references/pieges-windows.md` : encodage, avertissements, fins de ligne.
- `templates/nouveau_harnais.py` : squelette d'une nouvelle série.

## Ajouter une série

Copier `templates/nouveau_harnais.py` vers `scripts/harness_<nom>.py`. Garder `check()` et la ligne finale `RESUME x réussis / y échoués`, que lit `lancer_tout.py`. Puis ajouter `<nom>` à la liste `SERIES` de `lancer_tout.py`.
