# Format de SUIVI-AMELIORATIONS.md

Fichier en UTF-8, fins de ligne LF, en français. Ordre des parties :

## 1. Titre et en-tête d'état

```markdown
# CIEL Studio : suivi des améliorations

Mis à jour le JJ/MM/AAAA. Version stable : **vNN** (dans `app-v30.py`, le nom attendu par l'appli), <état Git en une phrase : commit, branche, tag>. **Rien n'est poussé sur GitHub, fusionné dans `main` ou déployé.** <ou l'état réel>

Sauvegardes de chaque étape dans `sauvegardes/` : <liste, avec l'empreinte abrégée des versions validées>.
```

L'état Git de l'en-tête doit correspondre à la sortie de `scripts/etat_git.sh` au moment de l'écriture.

## 2. Tableau récapitulatif

Sept colonnes, une ligne par étape, dans l'ordre :

```markdown
| Étape | Problèmes détectés | Corrigés | Restants | Tests exécutés | Réussis | Échoués |
|---|---|---|---|---|---|---|
| 8. POLISH FINAL (audit complet) | 5 | 5 | 0 | 466 | 466 | 0 |
```

- « Tests exécutés » = « Réussis » + « Échoués ». Les points non vérifiés n'y entrent pas.
- Une vérification sans correction s'écrit avec « – » dans les colonnes de problèmes.

## 3. Fichiers et sauvegardes

Tableau `| Fichier | État |` : `app-v30.py`, `app-v36.py`, `docs/…`, `.streamlit/config.toml`, `.gitignore`, `sauvegardes/` (liste complète, hors Git).

## 4. Une section par étape

Titre : `## Étape N : NOM (description courte), vNN`. Contenu dans cet ordre (voir `templates/section-etape.md`) :

1. Contexte : demande, sauvegarde faite avant.
2. Audit ou diagnostic : tableau des contrôles et résultats.
3. Problèmes trouvés et corrigés : tableau `# | Gravité | Problème | Cause | Correction`.
4. Tests : tableau `Test | Résultat`, avec le total dans le titre (« Tests de la vNN (X réussis, Y échoués) »).
5. Incidents de travail : erreurs de scripts ou de tests, et ce qui a été fait. Préciser quand c'est le test, et non l'appli, qui était en cause.
6. Observations non corrigées.
7. Vérifications manuelles restantes : ce qui n'a pas pu être testé ici.

## 5. Sections permanentes, en fin de fichier

- « Stabilisation … dans Git » : branches, commits, tags, état du distant.
- « Points laissés en attente ».
- « Environnement de test ».

## Conventions

- Empreintes : les 8 premiers caractères suffisent dans le texte (`7b3ce69b…`). L'empreinte complète figure au moins une fois pour la sauvegarde finale.
- Noms de fichiers, fonctions, clés et commandes entre accents graves.
- Gravités : Critique, Haute, Moyenne, Basse.
- Vocabulaire constant : « réussi » et « échoué », jamais « OK » ou « KO » dans le texte.
- Ne jamais supprimer l'historique d'une étape passée. On ajoute une correction datée.
