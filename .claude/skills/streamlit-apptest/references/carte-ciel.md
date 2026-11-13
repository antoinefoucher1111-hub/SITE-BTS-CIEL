# Carte de CIEL Studio pour les tests

État de référence : v43 (`APP_VERSION = 'v43'`, tag Git `v43`). Les numéros de ligne changent : chercher par nom.

## Pages

La liste fait foi dans `app-v30.py`, entre `NAV = [` et `NAV_ITEMS =`. `harness_pages.py` la relit à chaque lancement : rien à mettre à jour à la main.

44 pages en v43 : accueil, seance, erreurs, examen, quiz, vocabulaire, flashcards, enonces, stats, classement, compte, reseaux, cyber, crypto, anssi, prog, systeme, encyclo, elec, fiches, datasheets, formulaire, suites, fonctions, anglais, cge, sandbox, wireshark, calculs, oscillo, kirchhoff, uml, annales, e5, tests-e6, livrables-e6, gantt, semaines, revision-totale, remediation, installer, methode, methodes, ressources.

Anciennes adresses (`NAV_ALIAS`) : maths-resume → formulaire, anglais-tech → datasheets, planning → semaines, pcap → wireshark, scores → stats, videos et liens → ressources.

## Thèmes

`st.session_state['theme']` : `sombre`, `gris`, `clair`. Le choix se fait avec la radio de clé `theme` et il est enregistré dans `profil['prefs']['theme']`.

## Session

| Clé | Contenu |
|---|---|
| `nav_slug` | page affichée |
| `current_user` | pseudo connecté, ou l'invité par défaut |
| `_profile` | profil : `points`, `history`, `errors`, `prefs`, etc. |
| `_xp_dernier` | gain réel du dernier appel à `add_user_points` |

## Préfixes de clés de widgets

| Préfixe | Où |
|---|---|
| `v31_gq_` | questions du grand quiz |
| `v31_ex_` | questions de l'examen (sauf `v31_ex_fmt`) |
| `v31_err_` | carnet d'erreurs |
| `v33_new_*`, `v33_login_*` | création de compte et connexion |
| `lab_*`, `btn_chk_*`, `sel_*_lab` | exercices de terminal |
| `home_*` | boutons de l'accueil |

L'appli compte 213 clés de widgets, sans doublon. Toute nouvelle clé doit rester unique.

## XP

- Grand quiz : +3 par bonne réponse. Examen blanc : +4 par bonne réponse. Exercices : 15 à 25 selon l'exercice (table `LABS` de `harness_labs.py`).
- `add_user_points` garde la logique d'origine. Une enveloppe enregistre le gain réel dans `_xp_dernier`, et `xp_txt(points, cle)` produit le texte affiché : « +N XP », « déjà gagnés » ou l'avertissement invité.
- Un même gain n'est accordé qu'une fois : au 2e essai, le message dit « déjà gagnés ».
- Ne pas modifier le système d'XP sans accord explicite.

## Stockage

- `get_store()` choisit `_SupabaseStore` si `st.secrets['supabase']` contient `url` et `key`, sinon `_LocalStore` (fichier `users_db_v2.json` dans le dossier courant).
- `_SupabaseStore` appelle `<url>/rest/v1/profiles` en REST (`requests`) : `GET ?id=eq.<uid>&select=data`, `POST` avec `Prefer: resolution=merge-duplicates`, `DELETE`, `select=lb:data->lb` pour le classement, `select=id` pour la liste.
- Mots de passe : `_hash_pwd` (PBKDF2-SHA256, 200 000 itérations, sel aléatoire) et `_check_pwd` (`hmac.compare_digest`).
