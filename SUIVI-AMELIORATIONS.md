# CIEL Studio : suivi des améliorations

Mis à jour le 12/11/2026. Version de travail : **v38** (dans `app-v30.py`, le nom attendu par l'appli). Rien n'est commité ni déployé.

Sauvegardes de chaque étape dans `sauvegardes/` : `app-v35-origine.py`, `app-v36-etape1.py`, `app-v36-avant-etape2.py`, `app-v37-avant-etape3.py`.

| Étape | Problèmes détectés | Corrigés | Restants | Tests exécutés | Réussis | Échoués |
|---|---|---|---|---|---|---|
| 1. HARDEN | – | 7 améliorations | – | 50 pages (session précédente) | 50 | 0 |
| 2. Contrastes et thèmes | 63 | 63 | 0 | 19 | 19 | 0 |
| Vérification de la v37 | – | – | – | 225 | 223 | 2 (défauts de la v35, traités à l'étape 3) |
| 3. ADAPT (téléphone) | 25 | 25 | 0 | 267 | 267 | 0 |

## Fichiers et sauvegardes

| Fichier | État |
|---|---|
| `app-v30.py` | v37 = v36 + corrections de l'étape 2 |
| `app-v36.py` | v36 de l'étape 1 (inchangé) |
| `docs/index.html`, `docs/sw.js` | Changements de l'étape 1 (`ciel-v3`). L'étape 2 n'a rien changé ici. |
| `.streamlit/config.toml` | Inchangé |
| `sauvegardes/` | `app-v35-origine.py`, `app-v36-etape1.py`, `app-v36-avant-etape2.py`, `index-v35.html`, `index-etape1.html`, `sw-v35.js`, `sw-etape1.js` |

La v35 d'origine est aussi conservée dans git (commit `ff79253`).

## Tableau de bord

| | Nombre |
|---|---|
| 1. Améliorations faites à l'étape 1 | **7** |
| 2. Problèmes confirmés à l'étape 2 | **63** |
| 3. Corrections faites à l'étape 2 | **63** |
| 4. Corrections restantes de l'étape 2 | **0** |
| 5. Tests de l'étape 2 | **19 réussis, 0 échoué** |
| (Tests de préparation, faits avant) | 6 réussis, 0 échoué |

Les 63 problèmes confirmés viennent de l'inventaire de départ (64), moins 3 points qui, une fois vérifiés, n'étaient pas des défauts (voir plus bas), plus 2 défauts trouvés en cours de route (F4 et F5).

## 1. Étape 1 (HARDEN) : 7 améliorations, d'après la session précédente

Ces améliorations n'ont pas été refaites ici.

1. Réponses de quiz pré-cochées corrigées (40)
2. Quiz qui démarrent sans réponse (46)
3. Réponse vide comptée comme fausse
4. Corrections qui plantaient sur une réponse vide, protégées (9)
5. Pastilles de réponse neutralisées
6. Contour de focus clavier bleu de 2 px
7. Préférence « réduire les animations » respectée

On ne sait pas si les 40 réponses pré-cochées font partie des 46 quiz : elles ne sont pas additionnées.

## 2 et 3. Étape 2 : problèmes et corrections

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

## 5. Tests de l'étape 2 (19 réussis, 0 échoué)

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

## À prévoir plus tard (hors étape 2)

- Il reste environ 25 couleurs `rgba(...)` écrites en dur, surtout des fonds teintés (par exemple ligne 1034 : `rgba(56,189,248,0.3)`). Elles n'étaient pas dans l'inventaire de l'étape 2.
- Les cartes ont une bordure gauche colorée de 5 à 6 px. Il faudra trancher sur ce choix de design lors d'une prochaine étape (mise en page et finitions).

## Environnement de test

- L'environnement isolé et la copie de l'appli sont hors du projet ; la configuration de lancement est `.claude/launch.json` (« ciel-local », port 8599).
- Sans les identifiants Supabase, l'appli utilise un stockage local de test, situé hors du projet.
