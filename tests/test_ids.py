"""Identifiants de questions stables (v44, élément B1).

Le carnet d'erreurs et les statistiques des élèves sont rangés par identifiant de question.
Ces tests vérifient qu'aucun identifiant de la v43 n'a disparu, et qu'un « id » explicite l'emporte sur
l'identifiant calculé à partir du texte (pour pouvoir corriger une question sans casser ce lien).

L'appli est exécutée en mode isolé, dans un dossier temporaire, sans aucun secret (jamais Supabase).
"""
import json
import logging
import os
import runpy
import shutil

import pytest

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope='module')
def appli(tmp_path_factory):
    dossier = tmp_path_factory.mktemp('appli')
    shutil.copy2(os.path.join(RACINE, 'app-v30.py'), dossier / 'app-v30.py')
    shutil.copytree(os.path.join(RACINE, 'ciel'), dossier / 'ciel', ignore=shutil.ignore_patterns('__pycache__'))
    ancien = os.getcwd()
    os.chdir(dossier)
    logging.disable(logging.CRITICAL)
    try:
        yield runpy.run_path(str(dossier / 'app-v30.py'), run_name='__ciel_tests__')
    finally:
        logging.disable(logging.NOTSET)
        os.chdir(ancien)


def test_aucun_identifiant_v43_perdu(appli):
    attendu = json.load(open(os.path.join(RACINE, 'tests', 'ids_v43.json'), encoding='utf-8'))
    actuels = {q['id'] for q in appli['QUESTION_POOL']}
    manquants = sorted(set(attendu['ids']) - actuels)
    assert not manquants, f"{len(manquants)} identifiant(s) de la v43 ont disparu : {manquants[:5]}"


def test_identifiants_uniques(appli):
    ids = [q['id'] for q in appli['QUESTION_POOL']]
    assert len(ids) == len(set(ids))


def test_id_explicite_prioritaire(appli):
    banque = appli['GRAND_QUIZ_DATA']
    banque.append({'q': 'Question de test au texte corrigé', 'options': ['A', 'B'], 'rep': 'A', 'id': 'id-fige-test'})
    try:
        pool = appli['build_question_pool']()
        assert any(q['id'] == 'id-fige-test' for q in pool)
    finally:
        banque.pop()
