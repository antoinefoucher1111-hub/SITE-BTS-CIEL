# Ce qu'AppTest couvre et ce qu'il ne couvre pas

## Couvert

- Exécution du script Python de chaque page, dans chaque thème : exceptions, erreurs affichées.
- Logique : scores, XP, historique, carnet d'erreurs, comptes, connexion, préférences.
- Navigation : `nav_slug`, anciennes adresses `?p=`, pages regroupées.
- Textes produits par l'appli : messages, titres, libellés, contenu Markdown.
- Échanges avec le stockage, via le faux Supabase local.

## Non couvert : vérifier dans un navigateur

| Point | Pourquoi AppTest ne le voit pas | Comment vérifier |
|---|---|---|
| Contrastes, couleurs des 3 thèmes | Le CSS n'est pas appliqué | Navigateur sur l'appli locale, mesure WCAG du texte visible |
| Téléphone (375 px), débordements | Aucune mise en page | Fenêtre de 375 px, défilement horizontal de la page |
| Formules KaTeX | Rendues dans le navigateur | Chercher `.katex-error` dans la page |
| Minuteur de l'examen | `st.iframe` n'exécute pas son JavaScript | Ouvrir l'examen et voir le décompte |
| Boutons-liens, accordéons, survols | Purement CSS | Contrôle visuel |

Faux positifs connus côté navigateur : les éléments `.katex-mathml` (MathML pour lecteurs d'écran, rognés) et les grands tracés SVG de KaTeX dépassent la page sans être visibles. Une formule longue défile dans son propre cadre `.katex`.

## Jamais vérifiable ici

- Vrai Supabase sur l'appli en ligne : création de compte, connexion, XP, mot de passe oublié.
- Vrais téléphones iOS et Android.
- Version de Streamlit en production.

Ces points se notent dans « Vérifications manuelles restantes » du suivi, jamais comme testés.
