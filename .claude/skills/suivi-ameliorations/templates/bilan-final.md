# Bilan à présenter à l'utilisateur en fin d'étape

Phrase d'ouverture : ce qui est fait, le résultat des tests, et ce qui n'est pas fait (commit, push, déploiement).

## Pages et thèmes vérifiés
- <n pages × 3 thèmes à 1280 px : x réussis / y>
- <téléphone 375 px : x / y>

## Tests : X réussis, Y échoués
| Série | Résultat |
|---|---|
| <série> | <x/y> |

<Incidents dus aux tests eux-mêmes, s'il y en a, en une ligne chacun.>

## Problèmes trouvés et corrigés (N)
| # | Gravité | Problème | Correction |
|---|---|---|---|

<Observations non corrigées.>

## Vérifications à faire à la main (non faites ici)
- <point>

## Fichiers modifiés
- <fichier> : <résumé>

## Sauvegardes
- Avant les corrections : `sauvegardes/<fichier>`
- **Sauvegarde finale : `sauvegardes/<fichier>`**, SHA-256 `<empreinte complète>`

## État de Git
<Sortie résumée de etat_git.sh : branche, HEAD, avance sur main, main et origin/main, tags, fichiers modifiés, non suivis, ignorés.>

<Dernière ligne : « Rien n'a été commité, poussé, fusionné ni déployé. » ou l'état réel.>
