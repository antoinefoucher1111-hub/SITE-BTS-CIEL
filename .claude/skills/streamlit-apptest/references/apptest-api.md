# AppTest dans CIEL Studio

Module : `from streamlit.testing.v1 import AppTest`. Testé avec Streamlit 1.67.

## Ouvrir une page

```python
at = AppTest.from_file(app, default_timeout=120)   # 120 s : le fichier fait plus de 9 000 lignes
at.session_state['nav_slug'] = 'quiz'              # page à ouvrir
at.session_state['theme'] = 'clair'                # sombre | gris | clair
at.run()
```

Ancienne adresse : `at.query_params['p'] = 'planning'` avant `at.run()`.

Faux Supabase : `at.secrets['supabase'] = {'url': URL_LOCALE, 'key': 'cle-de-test'}` (voir `scripts/harness_comptes.py`). Sans cette ligne, l'appli utilise son stockage local de test, créé dans le dossier courant : d'où le `os.chdir(dossier_de_travail)` en tête de chaque série.

## Trouver un widget

Toujours par clé quand elle existe, sinon par libellé :

```python
at.text_input(key='v33_new_name').input('testciel')
next(b for b in at.button if 'Valider mes réponses' in (b.label or '')).click().run()
radios = [r for r in at.radio if (r.key or '').startswith('v31_gq_')]
r.set_value(r.options[0])
sb.set_value(choix).run()                          # selectbox
```

Après `input()` ou `set_value()`, l'action ne part qu'au prochain `.run()` (souvent celui du `click()`).

## Lire le résultat

| Élément | Accès |
|---|---|
| Exceptions Python de l'appli | `at.exception` (doit être vide) |
| Messages | `at.success`, `at.info`, `at.warning`, `at.error` (`.value`) |
| Texte et HTML | `at.markdown` (`.value`), `at.subheader`, `at.expander` (`.label`), `at.tabs` (`.label`) |
| Indicateurs | `at.metric` (`.label`, `.value`) |
| État | `at.session_state['_profile']`, `['current_user']`, `['nav_slug']`, `['_xp_dernier']` |

## Bonnes pratiques

- Une instance `AppTest` neuve par scénario indépendant : la session ne doit pas fuir d'un test à l'autre.
- Vérifier aussi l'absence de double comptage : relancer `at.run()` après une action qui donne des XP, puis contrôler que les points n'ont pas bougé.
- Mesurer les XP par différence (`p1 - p0`), jamais par valeur absolue.
- Imprimer `OK   nom` ou `ECHEC nom  -> détail`, puis terminer par `RESUME x réussis / y échoués`.
