---
name: suivi-ameliorations
description: Tenir à jour SUIVI-AMELIORATIONS.md et produire les bilans d'étape de CIEL Studio — sauvegardes de app-v30.py avec empreinte SHA-256, compteurs de tests fidèles aux journaux, problèmes trouvés et corrigés, vérifications manuelles restantes, état Git exact. À utiliser à la fin d'une étape d'amélioration, après une correction, avant ou après un commit, ou quand on demande « mets à jour le suivi », « fais le bilan », « sauvegarde la version ».
---

# suivi-ameliorations : journal des améliorations de CIEL Studio

`SUIVI-AMELIORATIONS.md`, à la racine du projet, est la mémoire du projet : chaque version, ce qui a changé, comment c'est testé, ce qui reste à vérifier. Ce Skill garde ce fichier fiable.

## Règles absolues

1. **Rien sans preuve.** Un test est « réussi » seulement si son journal le montre. Sinon il est « non testé » ou « à vérifier à la main ». Ne jamais arrondir ni estimer un compteur.
2. **Trois états distincts** : réussi, échoué, non vérifié. Un échec reste écrit, avec sa cause, même s'il est corrigé ensuite.
3. **Sauvegarde avant toute modification** de `app-v30.py`, avec `scripts/sauvegarde.py`. Elle refuse d'écraser un fichier existant.
4. **Dates absolues** (13/11/2026), jamais « hier » ni « aujourd'hui ».
5. **Git en lecture seule.** `scripts/etat_git.sh` ne modifie rien. Aucun commit, push, fusion ni déploiement sans demande explicite de l'utilisateur.
6. **Nom du fichier de l'appli** : toujours `app-v30.py`. La version vit dans `APP_VERSION`.
7. Un **nouveau document** (README, guide, spécification) relève de `doc-coauthoring`, pas de ce Skill.

## Méthode

### Avant une étape
1. Sauvegarder : `python .claude/skills/suivi-ameliorations/scripts/sauvegarde.py avant-etape9`. Le script lit la version dans `APP_VERSION`.
2. Noter l'empreinte affichée.

### Après les corrections et les tests
1. Relever les compteurs dans les journaux de `streamlit-apptest` (résumé de `lancer_tout.py`) et des contrôles faits dans le navigateur.
2. Sauvegarder la version finale : `sauvegarde.py <etiquette>` (par exemple `polish-final`).
3. Mettre à jour `SUIVI-AMELIORATIONS.md` selon `references/format-suivi.md` :
   - en-tête : date, version, état Git ;
   - ligne du tableau récapitulatif (`templates/ligne-recap.md`) ;
   - section de l'étape (`templates/section-etape.md`) ;
   - liste des sauvegardes.
4. Copier le suivi dans `sauvegardes/SUIVI-vNN.md` (même version que l'appli).
5. Relever l'état Git : `bash .claude/skills/suivi-ameliorations/scripts/etat_git.sh`.
6. Présenter le bilan avec `templates/bilan-final.md`.

## Fichiers

- `references/format-suivi.md` : structure exacte du suivi et conventions.
- `templates/ligne-recap.md`, `templates/section-etape.md`, `templates/bilan-final.md`.
- `scripts/sauvegarde.py` : copie datée et empreinte SHA-256, sans écrasement.
- `scripts/etat_git.sh` : branches, commits d'avance, statut, tags, distant, en lecture seule.
