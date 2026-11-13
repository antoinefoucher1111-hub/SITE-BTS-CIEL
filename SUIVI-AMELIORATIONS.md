# CIEL Studio : suivi des améliorations

Mis à jour le 13/11/2026. Version de travail : **v43** (dans `app-v30.py`, le nom attendu par l'appli). La v38 est commitée sur la branche locale `v38-contrastes-mobile`. Les v39 à v43 (étapes 4 à 8) ne sont pas encore commitées. Rien n'est fusionné dans `main`, poussé ou déployé.

Sauvegardes de chaque étape dans `sauvegardes/` : `app-v35-origine.py`, `app-v36-etape1.py`, `app-v36-avant-etape2.py`, `app-v37-avant-etape3.py`, `app-v38-avant-etape4.py`, `app-v39-polish.py` (v39 validée, empreinte SHA-256 `cf0ef305…0514c`), `app-v40-distill.py` (v40, empreinte `8605e916…`), `app-v40-avant-etape6.py`, `app-v41-typeset-layout.py` (v41, empreinte `f6fcb563…`), `app-v41-avant-etape7.py`, `app-v42-clarify.py` (v42, empreinte `e5f2f1a9…`), `app-v42-avant-etape8.py`, `app-v43-polish-final.py` (v43 finale, empreinte `7b3ce69b…18471`).

| Étape | Problèmes détectés | Corrigés | Restants | Tests exécutés | Réussis | Échoués |
|---|---|---|---|---|---|---|
| 1. HARDEN | – | 7 améliorations | – | 50 pages (session précédente) | 50 | 0 |
| 2. Contrastes et thèmes | 63 | 63 | 0 | 19 | 19 | 0 |
| Vérification de la v37 | – | – | – | 225 | 223 | 2 (défauts de la v35, traités à l'étape 3) |
| 3. ADAPT (téléphone) | 25 | 25 | 0 | 267 | 267 | 0 |
| 4. POLISH (harmonisation) | 146 | 146 | 0 | 421 | 421 | 0 |
| 5. DISTILL (menu et navigation) | 11 | 11 | 0 | 268 | 268 | 0 |
| 6. TYPESET + LAYOUT | 15 | 15 | 0 | 259 | 259 | 0 |
| 7. CLARIFY (textes et libellés) | 22 | 22 | 0 | 286 | 286 | 0 |
| 8. POLISH FINAL (audit complet) | 5 | 5 | 0 | 466 | 466 | 0 |

## Fichiers et sauvegardes

| Fichier | État |
|---|---|
| `app-v30.py` | v43 = v36 + corrections des étapes 2 à 8 |
| `app-v36.py` | v36 de l'étape 1 (inchangé) |
| `docs/index.html`, `docs/sw.js` | Changements de l'étape 1 (`ciel-v3`). L'étape 2 n'a rien changé ici. |
| `.streamlit/config.toml` | Inchangé |
| `sauvegardes/` (sur ce poste, hors git) | `app-v35-origine.py`, `app-v36-etape1.py`, `app-v36-avant-etape2.py`, `app-v37-avant-etape3.py`, `app-v38-avant-etape4.py`, `app-v39-polish.py`, `SUIVI-v39.md`, `app-v40-distill.py`, `SUIVI-v40.md`, `app-v40-avant-etape6.py`, `app-v41-typeset-layout.py`, `SUIVI-v41.md`, `app-v41-avant-etape7.py`, `app-v42-clarify.py`, `SUIVI-v42.md`, `app-v42-avant-etape8.py`, `app-v43-polish-final.py`, `SUIVI-v43.md`, `index-v35.html`, `index-etape1.html`, `sw-v35.js`, `sw-etape1.js` |

La v35 d'origine est aussi conservée dans git (commit `ff79253`).

## Tableau de bord de l'étape 2

| | Nombre |
|---|---|
| 1. Améliorations faites à l'étape 1 | **7** |
| 2. Problèmes confirmés à l'étape 2 | **63** |
| 3. Corrections faites à l'étape 2 | **63** |
| 4. Corrections restantes de l'étape 2 | **0** |
| 5. Tests de l'étape 2 | **19 réussis, 0 échoué** |
| (Tests de préparation, faits avant) | 6 réussis, 0 échoué |

Les 63 problèmes confirmés viennent de l'inventaire de départ (64), moins 3 points qui, une fois vérifiés, n'étaient pas des défauts (voir plus bas), plus 2 défauts trouvés en cours de route (F4 et F5).

## Étape 1 (HARDEN) : 7 améliorations, d'après la session précédente

Ces améliorations n'ont pas été refaites ici.

1. Réponses de quiz pré-cochées corrigées (40)
2. Quiz qui démarrent sans réponse (46)
3. Réponse vide comptée comme fausse
4. Corrections qui plantaient sur une réponse vide, protégées (9)
5. Pastilles de réponse neutralisées
6. Contour de focus clavier bleu de 2 px
7. Préférence « réduire les animations » respectée

On ne sait pas si les 40 réponses pré-cochées font partie des 46 quiz : elles ne sont pas additionnées.

## Étape 2 : problèmes et corrections

### A. Couleurs du thème sous 4,5:1 : 10 problèmes, 10 corrigés

Chaque ratio est mesuré sur le fond le moins favorable du thème. Les teintes d'origine sont conservées.

| # | Thème | Variable | Avant | Après |
|---|---|---|---|---|
| A1 | sombre | `--faint` | #5c5c63 (2,80) | #7d7d84 (4,54) |
| A2 | gris | `--faint` | #76767f (3,00) | #95959c (4,54) |
| A3 | clair | `--faint` | #8b8b94 (2,91) | #6b6b72 (4,56) |
| A4 | sombre | `--blue` | #3d6bff (4,19) | #4974ff (4,61) |
| A5 | gris | `--blue` | #3d6bff (3,05) | #7092ff (4,66) |
| A6 | gris | `--red` | #ff453a (3,96) | #ff645b (4,65) |
| A7 | gris | `--violet` | #bf5af2 (3,83) | #c973f4 (4,66) |
| A8 | clair | `--red` | #e0352b (3,84) | #cc281e (4,66) |
| A9 | clair | `--green` | #1a8d43 (3,67) | #177a3a (4,67) |
| A10 | clair | `--warn` | #a16207 (4,25) | #995d07 (4,62) |

Ajustement lié à A3 : dans le thème clair, `--muted` passe de #62626b à #585860 (6,08:1). Ce n'est pas une correction de plus : cela garde deux niveaux de gris distincts maintenant que `--faint` est plus foncé.

### B. Étiquettes d'étapes : 9 problèmes, 9 corrigés

Les 9 étiquettes de l'accueil utilisent maintenant les variables du thème au lieu de couleurs écrites en dur :

- Étape 1 → `var(--red)`
- Étape 2 → `var(--blue)`
- Étape 3 → `var(--warn)`. Avant, c'était un jaune à 1,4:1, illisible en clair ; c'est maintenant un ambre lisible.
- Les 6 étiquettes grises → `var(--muted)`.

### C. Bordures de cartes et encadrés : 33 problèmes, 33 corrigés

28 cartes et 5 autres bordures (badge, lignes de tableau, encadrés) utilisent maintenant `var(--green)`, `var(--red)`, `var(--warn)`, `var(--blue)`, `var(--violet)`, `var(--line)` ou `var(--line-strong)`.

### D. Graphiques : 6 problèmes, 6 corrigés

Les graphiques prennent leurs couleurs dans le thème grâce à une nouvelle fonction `theme_color()`.

- D1 : courbe de progression. Le fond est transparent et les couleurs viennent du thème.
- D2 : radar des matières. Même chose.
- D3 : charge et décharge RC. Le titre est maintenant lisible en sombre et en gris.
- D5 : Gantt. Le titre et les barres viennent du thème.
- D6 : dégradé SVG de la courbe de l'accueil, maintenant en variables.
- D7 : barre de mémorisation et sa légende, maintenant en variables.

### E. Minuteur de l'examen blanc : 1 problème, 1 corrigé

Le minuteur est affiché dans un cadre isolé (iframe), où les variables du thème n'existent pas : ses couleurs `var(--warn)` et `var(--surface)` n'avaient aucun effet. Il reçoit maintenant les vraies couleurs du thème, et passe au rouge du thème dans la dernière minute.

### F. Thème clair : 4 problèmes, 4 corrigés

Cause commune à F1, F4 et F5 : depuis Streamlit 1.50 environ, les champs ne portent plus l'attribut `data-baseweb` que visait le CSS.

- F1 : la recherche du menu est maintenant claire, et la liste ouverte aussi.
- F3 : le bouton du menu sur téléphone a une icône de la couleur du texte, une zone tactile de 44 × 44 px et une pastille visible.
- F4 (trouvé à la vérification) : toutes les listes déroulantes de la zone principale.
- F5 (trouvé pendant les tests) : les champs de date et d'heure, qui étaient noirs en clair.

### Vérifiés et retirés du décompte (ce n'étaient pas des défauts)

- A11 : `--yellow` du thème clair. Cette couleur ne sert que de fond (avec du texte noir) ou de bordure, jamais de couleur de texte.
- D4 : l'oscilloscope. Son écran sombre est voulu ; ses libellés clairs sont lisibles dans les trois thèmes.
- F2 : les ronds des choix. Ils étaient déjà corrects, grâce à l'étape 1.

## Étape 2 : tests (19 réussis, 0 échoué)

Les tests ont été faits en local, avec Streamlit 1.67, en invité, sans Supabase.

| # | Test | Résultat |
|---|---|---|
| 1 | Syntaxe Python de `app-v30.py` | Réussi |
| 2 | Script de correction : chacun des 31 remplacements a trouvé exactement le nombre d'emplacements attendu | Réussi |
| 3 | L'appli démarre en v37, sans erreur côté serveur | Réussi |
| 4 | Sombre, accueil : contraste de 154 textes | Réussi (seul le « C » du logo est à 3,41:1, et les logos sont exemptés) |
| 5 | Clair, accueil : 154 textes, aucun échec ; « Étape 3 » lisible | Réussi |
| 6 | Clair : recherche du menu et liste ouverte (texte #0b0b0d sur blanc) | Réussi |
| 7 | Clair : champs de date après la correction F5 | Réussi |
| 8 | Clair, page Gantt : 99 textes | Réussi (le « 0 » du curseur est un faux positif, il est affiché sur fond blanc) |
| 9 | Téléphone, clair : bouton du menu visible, 44 × 44 px, il ouvre le menu | Réussi |
| 10 | Gris, Grand quiz : 139 textes, aucun échec | Réussi |
| 11 | Gris, correction du quiz : 178 textes, aucun échec | Réussi |
| 12 | Non-régression de l'étape 1 : quiz validé sans réponse = 0/10, sans plantage | Réussi |
| 13 | D1 : courbe de notes en gris et en clair | Réussi |
| 14 | D2 : radar en clair, et bordures de cartes en variables | Réussi |
| 15 | D3 : graphique RC en clair et en sombre (titre lisible) | Réussi |
| 16 | E1 : minuteur avec les vraies couleurs ; page d'examen, 246 textes, aucun échec | Réussi |
| 17 | D7 : barre de mémorisation en variables | Réussi |
| 18 | D6 : un dégradé SVG en `style="stop-color:var(...)"` prend bien les couleurs du thème | Réussi |
| 19 | Journal du serveur : aucune erreur de l'appli | Réussi |

### Ce qui n'a pas été testé

- La vraie connexion Supabase et les comptes réels : volontairement pas touchés. Le code de stockage n'a pas été modifié.
- La non-régression complète sur les 50 pages : elle n'a pas été relancée. Seules les pages testées ci-dessus l'ont été.
- Le minuteur dans les thèmes clair et gris : vérifié seulement en sombre. Le mécanisme est le même.
- La courbe SVG de l'accueil (D6) avec de vrais résultats d'examen : le principe est validé, mais pas l'affichage réel.
- La version en ligne de Streamlit : `requirements.txt` demande `>=1.35`. Avec une version plus ancienne, les anciennes règles `data-baseweb` restent en place, donc rien ne casse.

## Vérification complémentaire de la v37 (12/11, sans modifier le code)

Aucune ligne de l'appli n'a été modifiée pendant cette vérification.

### Bilan

| | Nombre |
|---|---|
| Tests réellement exécutés | **225** |
| Tests réussis | **223** |
| Tests échoués | **2** (tous deux présents depuis la v35 : ce ne sont pas des régressions de la v37) |
| Tests impossibles à effectuer | **3** |

### 1. Non-régression des 50 pages : 150 exécutés, 150 réussis

- Méthode : chaque page du menu est ouverte dans chaque thème, avec l'outil de test de Streamlit (AppTest 1.67), sur la v37 et sur la v36 de référence.
- 0 exception, 0 message d'erreur, et la page et le thème demandés sont bien conservés.
- Comparaison avec la v36 : même nombre de blocs affichés sur les 150 combinaisons page × thème, et aucun message d'erreur nouveau.

### 2. Minuteur de l'examen blanc : 6 exécutés, 6 réussis

Le contrôle s'est fait dans le navigateur.

| Thème | Texte | Fond | Résultat |
|---|---|---|---|
| sombre | #ffcc33 | #0b0b0d | Réussi |
| gris | #ffcc33 | #242428 | Réussi |
| clair | #995d07 | #ffffff | Réussi |

- Changement de thème pendant l'examen : le décompte continue normalement. Réussi.
- Dernière minute (forcée à 30 s) : texte et bordure passent au rouge du thème (#cc281e en clair). Réussi.
- Fin du temps : le message « Temps écoulé — valide ta copie » s'affiche. Réussi.

### 3. Comptes et Supabase : 33 exécutés, 33 réussis

- **Code :** la comparaison fonction par fonction entre la v35 d'origine et la v37 montre que les fonctions de stockage, de connexion et de calcul sont identiques. Seuls des affichages ont changé. Toutes les différences entre v36 et v37 sont des couleurs ou du CSS.
- **Supabase simulé :** un faux serveur Supabase local, en mémoire, reproduit l'API REST. Le vrai Supabase n'a jamais été contacté. 32 contrôles :
  - création de compte, avec un mot de passe non stocké en clair ;
  - clé envoyée à chaque appel ;
  - mauvais mot de passe refusé, bon mot de passe accepté ;
  - XP, historique, carnet d'erreurs et thème choisi rechargés dans une nouvelle session ;
  - pages accueil, stats, carnet, historique, classement, compte et séance sans exception, avec un compte connecté.
- Appels envoyés au faux serveur : 4 lectures, 6 écritures, 0 suppression.

### 4. Quiz, statistiques, XP, carnet d'erreurs : 24 exécutés, 24 réussis

Ces 24 contrôles portent sur l'examen blanc complet (40 questions), dans les 3 thèmes. Le Grand quiz est couvert par le point 3.

- L'examen démarre sans réponse cochée, la copie est rendue sans exception, et la note sur 20 s'affiche.
- Le passage est enregistré dans l'historique.
- XP : +4 par bonne réponse, sans double comptage quand on recharge la page.
- Carnet d'erreurs : une entrée par réponse fausse ou vide.
- Grand quiz (point 3) : +3 XP par bonne réponse, sans double comptage, avec historique et carnet justes.

Au premier passage, 3 contrôles avaient échoué à cause de mon test : il cherchait la note dans le texte, alors qu'elle s'affiche dans un indicateur. Après correction du test, ils passent. Ce n'était pas un défaut de l'appli.

### 5. Téléphone (375 × 812) : 9 exécutés, 7 réussis, 2 échoués

| Test | Résultat |
|---|---|
| Pas de débordement horizontal : quiz, examen, stats, séance | 4 réussis |
| Pas de débordement horizontal : **accueil** | **Échoué** : l'élément décoratif `.glow` du haut (520 px de large) permet de faire glisser la page de 73 px. **Présent depuis la v35.** |
| Fermer le menu, cocher une réponse au toucher, valider un quiz | 3 réussis |
| Taille des choix de réponse au toucher (24 px minimum) | **Échoué** : 23 px de haut. C'est la taille par défaut de Streamlit, **présente avant la v37**. |

Observation, qui ne compte pas comme un test : le menu s'ouvre tout seul à chaque chargement sur téléphone et cache la page. Cela vient du réglage `initial_sidebar_state='expanded'`, présent depuis la v35.

### 6. Journaux : 3 exécutés, 3 réussis

- Serveur de l'appli : aucune erreur de l'appli. Il n'y a que des coupures de connexion Windows (`WinError 10054`), dues aux rechargements de page.
- Console du navigateur : aucune erreur.
- Journaux des 150 ouvertures de pages : v37 et v36 identiques. Une seule alerte (police DejaVu Sans graisse 600), déjà présente en v36.

**Risque signalé, qui n'est pas une nouvelle erreur :** Streamlit 1.67 affiche « `st.components.v1.html` will be removed after 2026-06-01. Please replace with `st.iframe` ». Le minuteur de l'examen blanc (ligne 3717) utilise cette fonction depuis la v31. Comme `requirements.txt` demande `streamlit>=1.35`, une future mise à jour de Streamlit en ligne pourrait faire planter la page d'examen.

### Impossibles à effectuer (3)

- **Vrai Supabase et vrais comptes :** il n'y a pas d'identifiants sur ce poste, et vous avez demandé de ne pas toucher aux données. Ce point est remplacé par le faux Supabase et par la comparaison du code. Après un futur déploiement, il faudra vérifier avec votre propre compte (connexion, stats, carnet).
- **Vrai téléphone (iOS ou Android) :** seule l'émulation 375 × 812 du navigateur a été utilisée.
- **Version de Streamlit en ligne :** elle est inconnue depuis ce poste, donc impossible de dire si l'avertissement ci-dessus s'applique déjà en ligne.

### Non exécutés (pas demandés, à noter)

- Mot de passe oublié avec code de secours.
- Espace administrateur.
- Suppression de compte.

### Verdict

**Feu vert pour l'étape 3 :** aucune régression de la v37. Trois points sont à traiter, de préférence au début de l'étape 3 :

1. Remplacer `st.components.v1.html` par `st.iframe` pour le minuteur, ou figer la version de Streamlit. C'est le point le plus urgent.
2. Supprimer le débordement de `.glow` sur l'accueil en téléphone.
3. Agrandir les zones de toucher des choix de réponse, et revoir l'ouverture automatique du menu sur téléphone.

## Étape 3 : ADAPT (téléphone et écrans tactiles), v38

Sauvegarde faite avant : `sauvegardes/app-v37-avant-etape3.py`.

Méthode : un inventaire automatique en largeur téléphone (375 px) sur les 50 pages, avant les corrections puis après. Pour chaque page, il mesure :

- un débordement horizontal ;
- les zones de toucher de moins de 44 px ;
- les textes de moins de 12 px ;
- l'état du menu au chargement.

### Problèmes détectés : 25, tous corrigés

| # | Problème | Correction |
|---|---|---|
| A1 | Le minuteur utilise `st.components.v1.html`, que Streamlit annonce comme retirée | `st.iframe` si la fonction existe, l'ancienne fonction sinon (pour les versions plus anciennes de Streamlit) |
| B1 | Le menu s'ouvre tout seul sur téléphone et cache la page | `initial_sidebar_state='auto'` : ouvert sur ordinateur, fermé sur téléphone |
| C1 à C7 | Débordement horizontal sur 7 pages : accueil (halo `.glow`), formulaire, suites, fonctions, livrables E6, semaines, remédiation | Halo limité à la largeur de l'écran. Tableaux et formules larges défilent dans leur propre cadre. Formules dans une phrase : défilement sur téléphone. |
| D1 à D10 | Zones de toucher sous 44 px, par type de contrôle : choix de réponse (23 px), cases à cocher, onglets, boutons (dont validations de formulaires et boutons-liens), titres d'accordéons, champs texte, champs nombre et leurs boutons +/−, listes déroulantes, listes à choix multiples, œil « afficher le mot de passe » (32 × 16 px) | Hauteur minimale de 44 px **seulement au doigt ou sur petit écran**. Les choix de réponse prennent toute la largeur : 298 × 46 px au lieu de 35 × 23 px. |
| E1 à E5 | Textes sous 12 px (hors formules) : titres de section, étiquettes d'étapes, en-têtes de tableaux, badges, code dans les légendes | 12 px minimum sur téléphone |
| F1 | Barre du haut transparente : le contenu passait sous le bouton du menu en défilant (trouvé pendant les tests) | Barre opaque sur téléphone |

Résultat de l'inventaire mobile, avant et après :

| Mesure | v37 | v38 |
|---|---|---|
| Pages qui débordent | 7 | 0 |
| Textes sous 12 px (hors formules) | au moins 29 (comptage détaillé fait sur 18 pages) | 0 (sur les 50 pages) |
| Pages où le menu est ouvert au chargement (sans préférence enregistrée) | toutes (réglage `expanded`) | 0 |
| Choix de réponse sous 44 px | 311 | 0 |
| Onglets sous 44 px | 127 | 0 |

### Volontairement non traités (exemptions)

- Les liens dans le texte : la règle WCAG 2.5.8 exempte les liens dans une phrase.
- Les outils internes de Streamlit : barre d'outils au survol, flèches de défilement des onglets.
- Les champs natifs cachés : date, curseur.
- La petite flèche « Open » d'une liste déroulante : tout le champ de 44 px ouvre déjà la liste.
- Les indices et exposants des formules, qui sont petits par convention typographique.

### Sur ordinateur (souris), rien ne change

Les tailles compactes sont conservées : choix de réponse de 23 px, boutons de 40 px. La barre du haut reste transparente et le menu reste ouvert par défaut.

### Tests de l'étape 3 : 267 exécutés, 267 réussis, 0 échoué

| Test | Résultat |
|---|---|
| Syntaxe Python | 1 réussi |
| Inventaire téléphone final, 50 pages (débordement, toucher, textes, menu, barre du haut) | 50 réussis |
| Non-régression : 50 pages × 3 thèmes, structure identique à la v37 | 150 réussis |
| Comptes, faux Supabase : création, connexion, XP, historique, carnet, thème | 32 réussis |
| Examen blanc complet dans les 3 thèmes, avec le minuteur en `st.iframe` | 24 réussis |
| Minuteur dans le navigateur (décompte, couleurs) et avertissement de dépréciation absent des journaux | 2 réussis |
| Menu fermé au chargement sur téléphone et ouvert sur ordinateur (sans préférence enregistrée) | 1 réussi |
| Ordinateur à la souris : version compacte inchangée | 1 réussi |
| Contrôles à l'œil sur téléphone : accueil, quiz, tableau du formulaire, page compte | 4 réussis |
| Journaux du serveur et console du navigateur sans erreur de l'appli | 2 réussis |

Pendant le travail, 3 contrôles ont d'abord échoué, puis ont été corrigés et repassés :

- la règle de la barre du haut était battue par une règle plus ancienne et plus précise ;
- une formule de la page « semaines » débordait encore ;
- l'œil du mot de passe et la liste à choix multiples restaient trop petits.

Ils sont comptés dans les résultats finaux.

Comparaison du code : entre v37 et v38, une seule fonction Python change (`render_page_examen_blanc`, pour le minuteur). Le reste est du CSS. Le stockage, les comptes et les calculs sont intacts.

À savoir : Streamlit retient dans le navigateur si l'utilisateur a fermé le menu (`stSidebarCollapsed`). Ce choix personnel l'emporte ensuite sur le réglage par défaut.

### Impossibles à tester ici

- **Vrais téléphones (iOS Safari, Android Chrome) :** seule l'émulation Chromium a été utilisée, en 375 × 812.
- **Tablettes et téléphones en paysage :** les règles « au doigt » reposent sur `(pointer: coarse)`, que l'émulation de ce navigateur ne simule pas. Sur un vrai appareil tactile, elles s'appliqueront quelle que soit la largeur.
- **Vrai Supabase :** il n'y a pas d'identifiants sur ce poste, et vous avez demandé de ne pas toucher aux données.

## Étape 4 : POLISH (harmonisation des anciennes pages), v39

Sauvegarde faite avant : `sauvegardes/app-v38-avant-etape4.py`.

Choix validés :
- titre de page identique à l'intitulé du menu, sans emoji ;
- ancien titre conservé en accroche sous le titre ;
- emojis gardés dans les onglets, sous-titres et accordéons ;
- cartes avec une bordure fine.

### Problèmes détectés et corrigés : 146 sur 146

| Chantier | Détectés | Corrigés | Correction |
|---|---|---|---|
| P1 Titres de page | 42 | 42 | Fonction commune `page_header(titre, accroche)`. Le titre reprend l'intitulé du menu, sans emoji. L'ancien titre devient l'accroche (38 pages) ; elle est omise quand elle ne faisait que répéter le titre (Carnet d'erreurs, Examen blanc, Décodeur Wireshark, Programmation, Grand quiz, Réseaux). |
| P2 Ancien en-tête de la page Historique & badges | 1 | 1 | En-tête commun. L'étiquette « ESPACE PERSONNEL CERTIFIANT » au-dessus du titre est supprimée. Le total d'XP passe dans une case de statistique standard. |
| P3 Paragraphes atténués en style en ligne | 62 | 62 | Une seule classe `texte-attenue` |
| P4 Hiérarchie des titres inversée (un `####` à 24 px dépassait un `st.subheader` à 20,8 px) | 1 | 1 | Échelle commune : h3 20,8 px > h4 17,6 px > titre de carte 16,8 px |
| P5 Bordures épaisses des cartes (4 à 6 px) | 28 | 28 | Supprimées. Les cartes gardent leur bordure fine de 1 px, leur titre coloré et leur fond teinté. |
| P6 Couleurs `rgba` écrites en dur | 10 | 10 | `color-mix()` sur les variables du thème. **Cela solde le point « à prévoir » de l'étape 2.** |
| Trouvé pendant les tests : formules `$…$` affichées en brut dans du HTML | 2 | 2 | Accroche de « Fonctions » et introduction « charge RC » écrites en texte normal |

Sans objet :
- **P7 Badges :** déjà homogènes grâce au CSS commun. Le seul badge à style en ligne est traité en P6, et l'étiquette en capitales en P2.
- **P8 Séparateurs :** déjà homogènes (25,6 px au-dessus et au-dessous, mesuré).

Rétabli pendant le travail : la règle de suppression des bordures avait aussi touché les bordures gauches de 3 px des messages Streamlit (succès, erreur, info, avertissement). Elles sont hors du périmètre validé, donc remises à l'identique.

Non modifiés, comme convenu :
- les emojis des onglets, sous-titres et accordéons (environ 350) ;
- le contenu des cours ;
- la police et la mise en page générale ;
- le stockage, les comptes et le calcul des XP.

Entre v38 et v39, seules des fonctions d'affichage ont changé, plus l'ajout de `page_header`.

### Tests de l'étape 4 : 421 exécutés, 421 réussis, 0 échoué

| Test | Résultat |
|---|---|
| Syntaxe Python, et script de transformation où chaque remplacement a trouvé le nombre attendu | 2 réussis |
| Non-régression, 50 pages × 3 thèmes (avant les 3 retouches finales) | 150 réussis. Seule différence avec la v38 : la page Historique a un bloc de plus, ce qui est attendu (en-tête en deux blocs). |
| Non-régression sur la version finale, 50 pages × 3 thèmes | 150 réussis |
| Comptes, faux Supabase | 32 réussis |
| Examen blanc complet, 3 thèmes | 24 réussis |
| Inventaire téléphone, 50 pages (débordement, toucher, textes, menu) | 50 réussis. Au premier passage, un bouton du Gantt avait été mesuré pendant l'affichage ; il fait bien 44 px au second contrôle. |
| Contraste : Remédiation en sombre, gris et clair (90 textes chacun), CGE en sombre et en clair (43 textes chacun) | 5 réussis, 0 texte sous le seuil |
| Hiérarchie des titres mesurée (page Cybersécurité) | 1 réussi |
| Contrôles à l'œil : E5, Historique, CGE, Remédiation, Fonctions | 5 réussis |
| Recherche de formules `$…$` restées dans des titres, accroches ou introductions en HTML | 1 réussi (aucune) |
| Journaux : aucune erreur de l'appli | 1 réussi |

### À noter pour la suite

- Ces pages contiennent encore environ 350 emojis dans les onglets, sous-titres et accordéons, laissés volontairement. Leur retrait serait une refonte de contenu à décider à part.
- Le contraste n'a été mesuré que sur 2 pages modifiées représentatives (cartes teintées et badges). Les couleurs viennent toutes des variables vérifiées à l'étape 2.

## Étape 5 : DISTILL (menu et navigation), v40

Version de départ : v39, sauvegardée dans `sauvegardes/app-v39-polish.py`. Choix validé : « A + fusions sûres ».

### Avant et après

| | v39 | v40 |
|---|---|---|
| Groupes dans le menu | 12 | 7 (Accueil, Réviser, Mon espace, Cours, Labo pratique, Épreuves & BTS blanc, Guide & ressources) |
| Pages dans le menu | 50 | 44 |
| Hauteur du menu sur ordinateur (sections fermées) | 1 653 px | 1 425 px |
| « Mon espace » | sous 8 sections repliées | 3ᵉ groupe, visible dès le premier écran |

### Problèmes détectés et corrigés : 11 sur 11

| # | Problème | Correction |
|---|---|---|
| F1 | « Décodeur Wireshark » et « Captures de trames », deux pages pour le même outil | Une page « Wireshark » à 2 onglets |
| F2 | « Planning des révisions » (8 lignes), qui résume le programme semaine par semaine | Dépliant en tête de « BTS blanc : programme et planning » |
| F3 | « Anglais technique » : sa liste de composants était déjà dans « Datasheets » | Son glossaire est ajouté à « Datasheets & anglais technique » |
| F4 | « Résumé suites & décibels », qui double Suites, Fonctions et Formulaire | Dépliant en bas du « Formulaire complet » (contenu conservé) |
| F5 | « Vidéos de cours » et « Liens utiles », deux mini-pages | Une page « Ressources » (« Vidéos & liens utiles ») à 2 onglets |
| F6 | « Historique & badges » doublait « Mes stats » | Placé sous « Mes stats » |
| M1 | 12 groupes dans le menu | 7 groupes. Les 4 sections de cours sont réunies dans « Cours », avec des sous-titres Informatique, Électronique, Maths, Anglais & CGE. |
| M2 | « Mon espace » et « Guide » sous 8 sections repliées | « Mon espace » remonte en 3ᵉ position |
| M3, M4 | Intitulés trop longs : « Cybersécurité : EBIOS, PKI, pfSense, VPN » et « Terminaux (Cisco, Linux, AD…) » | « Cybersécurité : EBIOS, PKI, VPN » et « Terminaux de pratique » |
| M5 | L'onglet « Gestion du compte » de l'Historique renvoyait seulement vers « Mon compte » | Masqué sous « Mes stats ». « Mon compte » reste dans le menu. |

Les titres de page suivent les nouveaux intitulés, selon la règle de l'étape 4. Les 3 pages BTS blanc prennent le préfixe « BTS blanc : », pour se distinguer des épreuves E4, E5 et E6 dans le groupe commun.

**Anciennes adresses conservées.** `?p=maths-resume`, `anglais-tech`, `planning`, `pcap`, `scores`, `videos` et `liens` mènent à la page qui contient désormais leur contenu. C'est vrai aussi pour une session déjà ouverte qui avait gardé l'ancienne page en mémoire.

**Volontairement non fusionnés :**
- Les 5 pages de cours (réseaux, OWASP, programmation, système, électronique) : elles seules ont les mini-évaluations de 10 questions qui rapportent des XP, avec leurs clés d'activité, et les fiches réflexes.
- « Trouver ta méthode » et « Méthodes par matière ».

**Aucun contenu supprimé.** Les clés d'XP et les statistiques ne changent pas. Entre v39 et v40, 5 fonctions changent : `nav_current`, `nav_go`, `render_sidebar_menu`, `render_page_analyse_scores` (paramètre `embarque`) et `render_extended_lab` (titre renommé). Le stockage et les comptes sont intacts.

### Tests de l'étape 5 : 268 exécutés, 268 réussis, 0 échoué

| Test | Résultat |
|---|---|
| Syntaxe Python | 1 réussi |
| Cohérence menu et routeur : 44 pages, toutes avec leur branche, aucune branche orpheline | 1 réussi |
| Anciennes adresses (7 × lien `?p=`, 7 × session ouverte, 7 × contenu regroupé présent) et pages fusionnées complètes (6), onglet compte masqué (1) | 28 réussis |
| Non-régression, 44 pages × 3 thèmes, sur le fichier final | 132 réussis |
| Comptes, faux Supabase | 32 réussis |
| Examen blanc complet, 3 thèmes | 24 réussis |
| Inventaire téléphone, 44 pages (débordement, toucher, textes, menu fermé) | 44 réussis |
| Menu à l'écran sur ordinateur (7 groupes, « Mon espace » au premier écran) | 1 réussi |
| Groupe « Cours » ouvert sur ses sous-titres, et fil d'Ariane | 1 réussi |
| `?p=scores` à l'écran, menant à « Mes stats » avec l'historique | 1 réussi |
| Page « Wireshark » à 2 onglets, à l'écran | 1 réussi |
| Menu ouvert sur téléphone | 1 réussi |
| Journaux du serveur et console du navigateur sans erreur de l'appli | 1 réussi |

Incidents de travail, corrigés avant ces tests :
- une indentation fausse dans l'Historique (erreur de syntaxe détectée tout de suite) ;
- un script de test qui plantait en affichant un emoji dans la console Windows (problème du test, pas de l'appli).

### Non testé

- Vrais téléphones, et vrai Supabase (mêmes limites qu'aux étapes précédentes).
- Ouvrir une ancienne adresse ne sélectionne pas automatiquement le bon onglet. Par exemple, `?p=pcap` ouvre « Wireshark » sur l'onglet « Décodeur » ; il faut cliquer sur « Captures commentées ».

## Étape 6 : TYPESET + LAYOUT (typographie et mise en page), v41

Sauvegarde faite avant : `sauvegardes/app-v40-avant-etape6.py`. Choix validé pour l'accueil : version compacte.

La police Inter est gardée. Le détecteur d'Impeccable la signale comme « trop répandue », mais c'est l'identité de l'appli, et le périmètre portait sur l'harmonisation, pas sur un changement d'identité.

### Avant et après (mesuré à l'écran sur 12 pages représentatives)

| Mesure | v40 | v41 |
|---|---|---|
| Tailles de texte différentes à l'écran | 19 (dont 14 entre 11,5 et 18,4 px) | **8 rôles** : 12, 14, 16, 18, 20, 24, 41,6 et 73,6 px |
| Tailles différentes dans le code | 29 | 8 jetons (`--fs-xs` … `--fs-display`), plus 2 tailles d'icônes |
| Graisses | 6 (400, 500, 600, 700, 800, 900) | 4, plus le 900 réservé à « Salut. » et au logo |
| Interlettrage | 14 valeurs | 3 rôles (affichage, titre, capitales) |
| Interlignage | 7 valeurs | 4 rôles, plus 1,8 gardé dans 3 listes de contenu |
| Largeur de lecture (caractères par ligne, au plus) | 82 à 99 sur 6 pages | 71 au plus ; de 36 à 71 selon les pages |
| Espace au-dessus et au-dessous des titres | 8–12 px au-dessus, 16 px au-dessous (inversé) | 32 px au-dessus, 8 px au-dessous |
| Accueil sur ordinateur | 1 896 px | 1 319 px (−30 %) |
| Accueil sur téléphone | 3 242 px (4 écrans), première action à 837 px | 2 294 px pour un nouvel utilisateur, environ 1 670 px ensuite ; première action à 613 px (dans le premier écran) |

### Problèmes détectés et corrigés : 15 sur 15

| # | Problème | Correction |
|---|---|---|
| T1 | 19 tailles à l'écran, 29 dans le code | 8 rôles en variables, et 66 tailles écrites en dur passées sur ces rôles |
| T2 | Titres de cartes à 16,8 px, presque comme le texte ; deux tailles de h3 et deux de h4 | h2 24 > h3 20 > h4 et titre de carte 18 > texte 16 |
| T3 | 6 graisses | 500 → 400 (5 cas) ; titre de page 900 → 800 |
| T4 | 14 interlettrages, 7 interlignages | Jetons `--ls-*` et `--lh-*` |
| T5 | Espacement des titres inversé | 32 px au-dessus, 8 px au-dessous, aucune marge pour le premier élément d'un bloc ; `text-wrap: balance` sur les titres et `pretty` sur les paragraphes |
| L1 | Lignes de 82 à 99 caractères | Prose limitée à `58ch`, soit environ 70 caractères réels avec Inter. Tableaux, code et graphiques gardent toute la largeur. |
| L2 | 24 marges intérieures, 17 marges extérieures, 9 arrondis | Échelle d'espacement de base 4 px (`--sp-1` … `--sp-8`) et 3 arrondis (8, 12, 14 px) pour les cadres |
| L3 | 5 compositions de cartes différentes | Cartes, formulaires et bannière : marge intérieure de 20 px, arrondi de 14 px ; cases de statistiques : 16 px et 12 px |
| L4 | Boutons de l'accueil posés sous les cartes | La colonne entière devient la carte, bouton compris (CSS seulement) |
| A1 | Accueil de 4 écrans sur téléphone, première action hors du premier écran | Bandeau compact ; 3 chiffres clés sur téléphone (les 2 autres sont dans les cartes et dans Mes stats) |
| A2 | « J-27 » affiché deux fois | Une seule fois, dans les chiffres clés |
| A3 | « Première fois ici ? » montré à tout le monde | Montré seulement à un nouvel utilisateur : aucune flashcard, aucun mot, aucune statistique de quiz, aucun historique, aucun jour de révision. Calculé sur les données, **rien n'est enregistré**. Les 3 guides restent dans le menu. |
| A4 | « Pour aller plus loin » : 3 grandes cartes qui répètent le menu | Une ligne de 3 boutons |
| A5 | Maîtrise par matière (7 lignes) qui doublait Mes stats | « À travailler en priorité » : les 3 matières les plus faibles, et un lien vers « Toutes mes matières dans Mes stats » |
| A6 | Bandeau d'accueil trop haut | Marges réduites (24 px sur ordinateur, 8 px sur téléphone) |

Incidents de travail, corrigés avant les tests finaux :
- Une règle de l'étape 4 maintenait les titres `<h4>` des cartes à 16 px ; elle est alignée sur 18 px.
- La première limite de largeur (`70ch`) donnait encore environ 84 caractères par ligne, car l'unité `ch` correspond à la largeur du « 0 », plus large que la lettre moyenne. Elle est réglée à `58ch`.

Contrepartie : les pages très longues s'allongent un peu, à cause des lignes plus courtes et de l'espace ajouté au-dessus des titres (« semaines » passe de 5 063 à 6 049 px sur ordinateur).

**Inchangés :** les comptes, Supabase, le stockage et les XP. Seules des fonctions d'affichage changent : l'accueil, et les tailles de texte écrites en dur dans quelques pages.

### Tests de l'étape 6 : 259 exécutés, 259 réussis, 0 échoué

| Test | Résultat |
|---|---|
| Syntaxe Python | 1 réussi |
| Mesure typographique finale : 12 pages, tailles toutes dans l'échelle, 71 caractères par ligne au plus | 12 réussis |
| Accueil : « Première fois ici ? » pour un nouvel utilisateur puis masqué après des quiz, J-xx unique, 3 boutons, lien vers Mes stats, 1 à 3 matières en priorité, aucune exception | 8 réussis |
| Non-régression, 44 pages × 3 thèmes, sur le fichier final | 132 réussis. Seul l'accueil a moins de blocs qu'en v40, ce qui est attendu. |
| Comptes, faux Supabase | 32 réussis |
| Examen blanc complet, 3 thèmes | 24 réussis |
| Inventaire téléphone, 44 pages | 44 réussis |
| Contraste de l'accueil en sombre, clair et gris (123 textes chacun) | 3 réussis |
| Accueil à l'écran sur ordinateur et sur téléphone | 2 réussis |
| Journaux du serveur sans erreur de l'appli | 1 réussi |

Note sur le contraste en gris : une première mesure, prise pendant la transition de couleur juste après le changement de thème, signalait 30 textes du menu à 2,5:1. Une fois l'affichage stabilisé, il n'en reste aucun ; c'est un artefact de mesure.

### Non testé

- Vrais téléphones, et vrai Supabase.
- Le contraste n'a été mesuré que sur l'accueil (dont les cartes ont changé). Les couleurs des autres pages ne changent pas à cette étape.

## Étape 7 : CLARIFY (textes, libellés, messages), v42

Sauvegarde faite avant : `sauvegardes/app-v41-avant-etape7.py` (identique à la v41 validée). Choix validé : toutes les reformulations proposées (priorités 1 à 5), y compris celles qui changent le sens.

Audit : 1 079 textes d'interface lus (144 boutons, 245 messages, 141 onglets, 103 accordéons, 192 champs, titres, légendes et exemples). Fichiers modifiés : `app-v30.py` et ce suivi.

### Problèmes détectés et corrigés : 22 sur 22

| # | Problème | Correction | Ampleur |
|---|---|---|---|
| 1.1 | Un invité lisait « XP enregistrés sur votre profil » | Le message dit le gain réel ; en invité, il précise « (en invité, ils disparaissent quand tu fermes la page) ». Quatre introductions qui promettaient « sur votre profil » sont reformulées. | 5 quiz de cours + 4 introductions |
| 1.2 | Un 0/10 s'affichait en vert | Vert à partir de 7/10, neutre de 5 à 6, orange en dessous | 5 quiz de cours |
| 1.3 | Erreurs techniques montrées brutes | Phrase claire avec la marche à suivre ; le détail technique passe dans une petite ligne en dessous | 3 messages |
| 1.4 | Renvois vers des pages qui n'existent plus | Chemins de cours des flashcards mis aux noms actuels du menu ; message de l'historique vide réécrit | 105 chemins + 1 message |
| 1.5 | « Certifiant » et « officiel » collés à du contenu écrit pour l'appli | Retirés là où c'était inexact. Gardés quand c'est vrai : programme, barème, coefficient, BO, annales, thèmes de culture générale. | 15 « certifiant » et 17 « officiel » retirés |
| 1.6 | (trouvé pendant le travail) « +X XP » affiché à chaque tentative, alors que les XP ne sont gagnés qu'une fois par activité | « pas de nouveaux XP : déjà gagnés lors d'une tentative précédente » | 32 messages de résultat + 26 exercices |
| 2.1 | Tutoiement et vouvoiement mélangés | Tutoiement pour toute l'interface (consignes, messages, libellés, introductions) | 60 textes |
| 2.2 | « +X points » au lieu de « XP » | « XP » partout | 11 messages |
| 2.3 | Plusieurs noms pour la même chose | Lexique : **quiz**, **examen blanc**, **exercice** | 13 libellés |
| 2.4 | Verbes des boutons disparates | **Vérifier** (exercice), **Valider mes réponses** (quiz), **Rendre ma copie** (examen) | 7 boutons |
| 2.5 | « Révision du jour » contre « Séance du jour » | « Séance du jour » partout | 1 accroche |
| 2.6 | Anglais et jargon : Check, Roadmap, Hardening, Technical Grammar Focus, Master hub, hub | Remplacés par du français | 9 libellés |
| 3.1 | Majuscule à chaque mot | Majuscule de phrase. Noms propres et sigles protégés, citations « » respectées. | 290 libellés |
| 3.2 | Emojis décoratifs en tête des boutons | Retirés ; ✅ ❌ 🤔 gardés (auto-évaluation) ; ⬅️ ➡️ deviennent ← → | 23 boutons |
| 3.3 | Boutons vagues (« Valider », « Ouvrir → », « Voir → », « Installer → ») | « Valider mes réponses », « Ouvrir le carnet → », « Voir les méthodes → », « Voir comment l'installer → » | 7 boutons |
| 3.4 | 5 formats de résultat et un ton gonflé | Un format unique : « **Résultat : 7/10 (70 %)** · +21 XP », puis un conseil | 32 messages |
| 3.5 | « 70% » sans espace | « 70 % » avec espace insécable, uniquement dans le texte affiché (jamais dans le CSS ni dans le code d'exemple) | 22 |
| 4.1 | « en bas du menu de gauche » : faux sur téléphone | La consigne précise le bouton du menu en haut à gauche sur téléphone | 1 |
| 4.2 | Classement non chargé : aucune marche à suivre | « Réessaie dans un instant : tes résultats ne sont pas perdus. » | 1 |
| 4.3 | Historique vide : vouvoiement et page périmée | Nouveau message et bouton « Faire un Grand quiz → » | 1 |
| 5.1 | Code mort (`render_today_panel`, jamais appelée, avec un texte périmé) | Supprimé | 48 lignes |
| 5.2 | Accroches qui répétaient le titre | Réécrites ou retirées | 6 accroches |

**Ce qui ne change pas :**
- Le **système d'XP est intact** : la fonction d'origine est identique. Une petite enveloppe note seulement le gain réel pour que le message dise vrai. Les 49 appels d'XP et leurs clés d'activité sont identiques à la v41.
- Les fonctions d'enregistrement des scores et des réponses, de connexion, de création de compte et de stockage sont identiques.
- Les quiz et les examens fonctionnent comme avant ; seuls les textes affichés changent.
- Les clés de widgets sont identiques, sauf les 2 qui appartenaient à la fonction morte supprimée.

**Gardés volontairement :**
- 8 « vous » : citations d'examen, sujet de culture générale, contenus de cours et de quiz, et un vrai pluriel.
- Le nom « Quiz Certifiant … » enregistré dans l'historique des élèves : c'est une donnée de progression, à ne pas toucher.
- Les emojis des onglets et des sous-titres.

### Tests de l'étape 7 : 286 exécutés, 286 réussis, 0 échoué (sur le fichier final)

| Test | Résultat |
|---|---|
| Syntaxe Python | 1 réussi |
| Non-régression, 44 pages × 3 thèmes (dont l'absence de doublons de boutons renommés) | 132 réussis |
| Comptes, faux Supabase | 32 réussis |
| Examen blanc complet, 3 thèmes | 24 réussis |
| Accueil (Première fois, J-xx, boutons, maîtrise) | 8 réussis |
| Anciennes adresses et pages regroupées | 28 réussis |
| Messages d'XP et de résultat : invité au 1er essai, « déjà gagnés » au 2e essai, couleur selon le score, historique vide, plus de page périmée | 8 réussis |
| Inventaire téléphone, 44 pages | 44 réussis |
| Intégrité du code : clés de widgets, fonctions XP, scores et comptes identiques, 49 appels d'XP identiques | 3 réussis |
| Plus aucun ancien nom de page dans les chemins de cours | 1 réussi |
| Les espaces avant % ne touchent ni le CSS ni le code d'exemple | 1 réussi |
| Contrôles à l'écran : Cybersécurité, Terminaux, accueil | 3 réussis |
| Journaux sans erreur de l'appli | 1 réussi |

### Incidents de travail, tous corrigés avant les tests finaux

- Les scripts des lots 1 et 2 se sont arrêtés sur une forme de texte imprévue, **avant d'écrire** dans le fichier ; ils ont été corrigés puis relancés.
- Lot 3 : les positions données par l'analyseur Python sont en octets. La première passe n'a donc traité que 32 libellés sur 290. Le fichier a été restauré à l'état d'après le lot 2, puis la correction a été relancée.
- Une espace avant % était tombée dans un commentaire de code C++ montré aux élèves ; elle est annulée.
- Après le premier contrôle à l'écran : 1 accroche jargon et 11 consignes au vouvoiement oubliées ont été corrigées. Les tests ont été relancés sur le fichier final.
- Trois tests automatiques étaient à adapter, sans que l'appli soit en cause :
  - le chemin de cours d'une flashcard ne s'affiche qu'après avoir retourné la carte ; la vérification se fait donc dans les données ;
  - deux libellés attendus par les tests avaient été renommés.

### Points non vérifiés

- Les 26 messages d'exercices de terminal en situation réelle : leur logique est la même que celle des quiz, qui est testée, mais je n'ai pas saisi les commandes justes pour réussir chaque exercice.
- Vrais téléphones et vrai Supabase (mêmes limites qu'avant).
- Observation, sans modification : le système d'XP enregistre aussi une activité ratée à 0 point. Refaire ce quiz ensuite ne rapporte donc plus rien. C'est le comportement d'origine ; il est désormais affiché honnêtement, mais pas changé, comme demandé.

## Étape 8 : POLISH FINAL (audit complet puis 5 corrections), v43

Audit complet de la v42 d'abord, sans modifier le code. Les 5 corrections ci-dessous ont ensuite été appliquées après accord (« Oui, les 5 »). Sauvegarde avant les corrections : `sauvegardes/app-v42-avant-etape8.py`. Sauvegarde finale : `sauvegardes/app-v43-polish-final.py` (SHA-256 `7b3ce69bc9d74ecff98dbdc62dbc5e27b002403ad8ef739fa08b276cd3218471`).

### Audit de la v42 (avant correction)

| Contrôle | Résultat |
|---|---|
| Contrastes WCAG, 44 pages × 3 thèmes, à 1280 px | 121 réussis, 11 échoués (4 causes : D2, D3, D4 et un clignotement passager) |
| Débordements à 1280 px, 44 × 3 | 132 réussis |
| Non-régression : pages, comptes (faux Supabase), examen, accueil, anciennes adresses, messages | 132 + 32 + 24 + 8 + 28 + 8, tous réussis |
| 26 exercices de terminal, testés pour la première fois | 49 réussis, 3 échoués (exercice Trunk + 1 erreur du test lui-même) |
| Flashcards : 105 liens vers les cours, 8 cartes retournées | Tous valides |
| Minuteur de l'examen (`st.iframe`) | Décompte correct |
| Intégrité : fonctions de stockage, comptes, scores et sessions identiques à la v35 ; 49 appels d'XP identiques ; 213 clés de widgets sans doublon | Réussi. Seule `render_today_panel`, du code mort, avait été retirée. |
| Journaux du serveur et console du navigateur | Aucune erreur de l'appli |

### Problèmes trouvés et corrigés (5)

| # | Gravité | Problème | Cause | Correction |
|---|---|---|---|---|
| D1 | Haute | Exercice Cisco Atelier 2 (Trunk) : la bonne réponse `switchport trunk allowed vlan 10,20,40` était refusée. Défaut présent depuis la v35. | La réponse était comparée sans espaces à un texte attendu qui en contenait, donc jamais égal. | Texte attendu écrit sans espaces : `allowedvlan10,20,40` |
| D2 | Moyenne | Thème clair : la barre de titre d'un accordéon ouvert devenait noire, avec un titre invisible. | Fond sombre imposé par Streamlit sur `summary`. | CSS : fond transparent, `--surface-2` au survol |
| D3 | Moyenne | Texte des boutons-liens (« Regarder sur YouTube ») illisible dans les 3 thèmes. Défaut présent depuis la v35. | La couleur des paragraphes s'appliquait au texte du bouton. | CSS : `--bg` sur les boutons principaux, `--text` sur les secondaires |
| D4 | Moyenne | 14 formules affichées en erreur (`\text`, `\times`, `\alpha`, `\rightarrow`). Défaut présent depuis la v35. | Barres obliques simples dans des chaînes Python ordinaires, lues comme `\t`, `\a` ou `\r`. | 13 barres obliques doublées et la formule `Nb\_termes` des suites corrigée. Le texte affiché est inchangé. |
| D5 | Basse | Environ 20 consignes d'exercices encore au vouvoiement | Oubli de l'étape 7 | 26 verbes passés au tutoiement sur 25 lignes (Passez → Passe, Créez → Crée…) |

Aucune donnée Supabase, aucun calcul d'XP, aucun compte, aucun quiz ni examen n'a été modifié. La police Inter, les 3 thèmes et les 44 pages sont conservés. L'écart avec la v42 est de 43 lignes, toutes identifiées.

### Tests de la v43 (466 réussis, 0 échoué)

| Test | Résultat |
|---|---|
| 26 exercices de terminal : réussite, « +N XP » affiché, XP ajoutés une seule fois, « déjà gagnés » au 2e essai | 52 réussis |
| Exercice Trunk : `10,20,40` et `10, 20, 40` acceptés ; `10,20` et `10,20,30` refusés | 4 réussis |
| Non-régression, 44 pages × 3 thèmes | 132 réussis |
| Comptes, faux Supabase | 32 réussis |
| Examen blanc complet, 3 thèmes | 24 réussis |
| Accueil | 8 réussis |
| Anciennes adresses et pages regroupées | 28 réussis |
| Messages d'XP et de résultat | 8 réussis |
| Contrastes (17 626 textes mesurés), formules et débordements à 1280 px, 44 pages × 3 thèmes | 132 réussis |
| Téléphone (375 px) : aucun défilement horizontal, 44 pages | 44 réussis (seuls dépassent les éléments rognés ou défilants de KaTeX, ce qui est normal) |
| Intégrité du code par rapport à la v42 : 117 fonctions, seule `render_extended_lab` modifiée (D1, D5) ; appels d'XP, 213 clés, `st.iframe` et Supabase inchangés | 1 réussi |
| Journaux du serveur : aucune erreur de l'appli (seulement des fermetures de connexion Windows dues aux iframes de test) | 1 réussi |

### Observation non corrigée

- Thème clair : juste après un changement de thème, l'élément actif du menu garde 2 à 3 secondes le fond de l'ancien thème. C'est une transition passagère, pas un état stable ; elle n'a pas été corrigée. Elle n'est pas réapparue lors du balayage complet de la v43.

### Vérifications manuelles restantes (non faites ici, à ne pas considérer comme testées)

- Les 26 exercices ont été validés par des tests automatiques (AppTest), pas tapés à la main dans le navigateur.
- Vrai téléphone (iOS/Android) : seule la largeur de 375 px a été simulée.
- Vrai Supabase sur l'appli déployée : création de compte, connexion, enregistrement des XP, mot de passe oublié.
- Version de Streamlit en production (les tests utilisent la 1.67).
- Bouton « Regarder la leçon sur YouTube » des flashcards après retournement d'une carte : D3 a été vérifié sur la page Ressources, mais pas sur ce bouton-là.

## Points laissés en attente à l'étape 2 : soldés à l'étape 4

- Couleurs `rgba(...)` écrites en dur : remplacées par des variables du thème (étape 4, P6). Il n'en reste que dans la définition des thèmes, où elles sont voulues.
- Bordures gauches colorées de 5 à 6 px sur les cartes : supprimées (étape 4, P5).

## Environnement de test

- L'environnement isolé et la copie de l'appli sont hors du projet ; la configuration de lancement est `.claude/launch.json` (« ciel-local », port 8599).
- Sans les identifiants Supabase, l'appli utilise un stockage local de test, situé hors du projet.
