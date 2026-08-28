# 🎓 Compagnon d'Apprentissage & de Révision — BTS CIEL (Option A)

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![BTS CIEL](https://img.shields.io/badge/BTS-CIEL%20Option%20A-success.svg)](https://eduscol.education.fr/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Bienvenue sur le dépôt officiel du **Compagnon d'Apprentissage et de Révision BTS CIEL (Option A : Cybersécurité, Informatique et réseaux, Électronique)**.

Ce projet fournit un environnement complet pour préparer et réussir les deux années du BTS ainsi que les épreuves d'examen (**E4, E5 et E6**) :
1. Un **carnet de bord numérique exhaustif en Markdown** (`structure_notebook_ciel-v3.md`).
2. Une **plateforme interactive locale en Python / Streamlit** (`app-v8.py`) intégrant cours, calculatrices dynamiques, simulateurs de commandes, annales d'examens et gestionnaire de projet E6.

---

## 📑 Table des Matières

- [✨ Fonctionnalités Principales](#-fonctionnalités-principales)
- [🏗️ Structure du Projet](#️-structure-du-projet)
- [🚀 Guide d'Installation et Lancement Local (Localhost)](#-guide-dinstallation-et-lancement-local-localhost)
  - [1. Prérequis](#1-prérequis)
  - [2. Cloner le Dépôt](#2-cloner-le-dépôt)
  - [3. Créer un Environnement Virtuel (Recommandé)](#3-créer-un-environnement-virtuel-recommandé)
  - [4. Installer les Dépendances](#4-installer-les-dépendances)
  - [5. Lancer l'Application](#5-lancer-lapplication)
- [🖥️ Visite Guidée de l'Application Web](#️-visite-guidée-de-lapplication-web)
  - [📚 1. Encyclopédie des Cours](#-1-encyclopédie-des-cours)
  - [📐 2. Laboratoire SysML & UML](#-2-laboratoire-sysml--uml)
  - [🎯 3. Annales Officielles BTS (2024 & 2025)](#-3-annales-officielles-bts-2024--2025)
  - [🧮 4. Générateurs & Calculatrices Dynamiques](#-4-générateurs--calculatrices-dynamiques)
  - [🔍 5. Lab Décodeur Wireshark](#-5-lab-décodeur-wireshark)
  - [⚡ 6. Sandboxes & Terminaux de Commandes](#-6-sandboxes--terminaux-de-commandes)
  - [🧪 7. Simulateur de Tests d'Intégration (Épreuve E6)](#-7-simulateur-de-tests-dintégration-épreuve-e6)
  - [📝 8. Grand Quiz d'Examen & Pont de Correction Actif](#-8-grand-quiz-dexamen--pont-de-correction-actif)
  - [📈 9. Dashboard Analytique & Suivi des Scores](#-9-dashboard-analytique--suivi-des-scores)
  - [📋 10. Gestion de Projet E6 & Diagramme de Gantt](#-10-gestion-de-projet-e6--diagramme-de-gantt)
  - [📹 11. Vidéothéconomie & Liens Utiles](#-11-vidéothéconomie--liens-utiles)
- [🛠️ Dépannage (FAQ / Troubleshooting)](#️-dépannage-faq--troubleshooting)
- [🌐 Références & Remerciements](#-références--remerciements)

---

## ✨ Fonctionnalités Principales

- 📖 **Cours Complets & Structurés** couvrant les 5 grands modules du référentiel BTS CIEL : Réseaux, Cybersécurité, Programmation/Dev (C++/Python), SysAdmin (Linux/AD), et Électronique/IoT.
- 📐 **Modélisation Système & Logicielle** : Diagrammes SysML (BDD, IBD) et UML (Classes, Séquence, Cas d'utilisation) avec exercices interactifs.
- 🧮 **Entraînement Mathématique Infini** : Moteurs de calcul aléatoires pour le découpage de sous-réseaux (VLSM) et la conversion analogique-numérique (CAN/ADC).
- 🔍 **Analyse Réseau Réelle** : Décodeur d'en-têtes hexadécimaux bruts (Wireshark) pour extraire IP, TTL, IHL et protocoles.
- ⚡ **Émulateurs de Commandes** : Terminaux interactifs simulant Cisco IOS (`config-if`), Linux Bash (`chmod` octal) et débuggeur de mémoire C++ (`new[]`/`delete[]`).
- 🎯 **Annales d'Examens Décortiquées** : Questions et corrigés détaillés issus des sessions officielles 2024 et 2025.
- 🧪 **Plan de Validation Logicielle (PVL) E6** : Scripts de tests d'intégration avec `pytest` et éditeur d'assertions.
- 🔄 **Pont Pédagogique Intelligent** : En cas d'erreur dans un quiz, l'application extrait et affiche instantanément le chapitre de cours concerné.
- 📊 **Tableau de Bord Analytique** : Graphiques d'évolution des notes, radar de compétences et plan d'action personnalisé hebdomadaire.
- 📅 **Gestionnaire de Projet E6** : Suivi des tâches en équipe avec génération automatique de planning de Gantt exportable pour la soutenance.

---

## 🏗️ Structure du Projet

```text
.
├── app-v8.py                    # Application Web Streamlit (Version Ultime)
├── structure_notebook_ciel-v3.md # Carnet de bord Markdown complet pour la prise de notes
├── scores_history_v3.json       # Fichier local d'historique des scores et statistiques
├── e6_project.json              # Fichier local de persistance des tâches du projet E6
├── README.md                    # Documentation complète du projet (ce fichier)
└── requirements.txt             # Dépendances Python requises
```

---

## 🚀 Guide d'Installation et Lancement Local (Localhost)

### 1. Prérequis

Assurez-vous que les outils suivants sont installés sur votre ordinateur :
- **Python 3.9 ou supérieur** : Téléchargeable sur [python.org](https://www.python.org/downloads/).
- **Git** (optionnel mais recommandé) : [git-scm.com](https://git-scm.com/).

Vérifiez votre installation dans un terminal :
```bash
python --version
# ou
python3 --version
```

---

### 2. Cloner le Dépôt

Ouvrez votre terminal ou invite de commande et clonez ce dépôt :
```bash
git clone https://github.com/votre-compte/bts-ciel-revision-hub.git
cd bts-ciel-revision-hub
```

---

### 3. Créer un Environnement Virtuel (Recommandé)

Il est vivement conseillé de travailler dans un environnement virtuel dédié :

* **Sous Linux / macOS** :
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

* **Sous Windows (PowerShell / CMD)** :
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

---

### 4. Installer les Dépendances

Installez les bibliothèques requises via `pip` :

```bash
pip install streamlit pandas matplotlib requests
```

*(Ou si un fichier `requirements.txt` est présent : `pip install -r requirements.txt`)*

---

### 5. Lancer l'Application

Démarrez le serveur local Streamlit :

```bash
streamlit run app-v8.py
```

Le terminal affichera les informations suivantes :
```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

👉 Votre navigateur web par défaut s'ouvrira automatiquement à l'adresse **`http://localhost:8501`**.

---

## 🖥️ Visite Guidée de l'Application Web

### 📚 1. Encyclopédie des Cours
Regroupe l'intégralité du programme officiel avec moteur de recherche instantané :
* **Réseaux & Télécoms** : Modèle OSI (7 couches), adressage IPv4/IPv6, encapsulation 802.1Q, routage statique/dynamique, DHCP (DORA), DNS, NAT/PAT.
* **Cybersécurité** : Triade CIA/CPA, AES/RSA/SHA-256, Top 10 OWASP (Injections SQL & XSS avec code corrigé), filtrage UFW et Port Security.
* **Programmation / Dev** : Pointeurs et références, allocation sur la Pile vs le Tas, POO en C++ (héritage, méthodes virtuelles pures), sockets TCP en Python.
* **Administration Système** : Droits octaux Linux (`chmod 750`), droits spéciaux (SUID/SGID/Sticky bit), Active Directory (OU, GPO, ordre LSDOU).
* **Électronique & IoT** : Shannon, quantum de CAN ($q = V_{ref} / (2^n - 1)$), bus I2C, SPI, UART, bus CAN, protocoles MQTT (QoS 0/1/2) et LoRaWAN.
* *Bonus* : Chaque chapitre contient un **mini-quiz d'auto-évaluation immédiat**.

---

### 📐 2. Laboratoire SysML & UML
Un atelier complet pour préparer l'épreuve E4 et le dossier E6 :
* **Diagrammes SysML** : Visualisation en ASCII-Art d'un *Block Definition Diagram (BDD)* et d'un *Internal Block Diagram (IBD)* modélisant une station de surveillance de l'air.
* **Diagrammes UML** : Modélisation d'une borne de recharge VE (Classes avec relations de composition et héritage, diagrammes de séquence avec messages synchrones/asynchrones).
* **Exercices d'analyse** : Décodage de flux physiques et d'architecture logicielle avec validation immédiate.

---

### 🎯 3. Annales Officielles BTS (2024 & 2025)
* **Session 2024 (Station de Surveillance de l'Air)** : Calcul de sous-réseaux $/28$, allocation dynamique de tableaux en C++ et correction de fuite mémoire via `delete[]`.
* **Session 2025 (Borne de Recharge de Véhicules Électriques)** : Droits d'accès Linux pour sauvegardes automatisées, calcul de la valeur numérique brute $N$ d'un CAN 12 bits sous $5,0\text{ V}$.
* **Quiz Annales Spécifique** : Questions d'examen chronométrées pour tester vos automatismes.

---

### 🧮 4. Générateurs & Calculatrices Dynamiques
* **Subnetting IPv4 Infini** : Génération aléatoire d'adresses IP de classes B et C avec validation du CIDR, du masque décimal pointé et du nombre d'hôtes utiles.
* **Calculs Électroniques & CAN** : Générateur de convertisseurs (10, 12, 16 bits) avec démonstration mathématique étape par étape du quantum $q$ et de la valeur de sortie $N$.

---

### 🔍 5. Lab Décodeur Wireshark
* Analyse d'un dump hexadécimal réel de 20 octets correspondant à un en-tête IPv4.
* Décodage des champs : Version IP, IHL (mots de 32 bits), TTL décimal, protocole encapsulé (TCP/UDP/ICMP), et adresses IP source/destination décimales pointées.

---

### ⚡ 6. Sandboxes & Terminaux de Commandes
* **Cisco IOS Terminal** : Assignation d'un port d'accès au VLAN 10 (`switchport access vlan 10`).
* **Linux Bash Console** : Calcul et saisie du masque octal `chmod 750 script.sh` pour sécuriser un script sensible.
* **C++ Memory Debugger** : Détection et correction d'une fuite de mémoire sur un tableau alloué sur le tas (`delete[] tab;`).

---

### 🧪 7. Simulateur de Tests d'Intégration (Épreuve E6)
* Script Python de validation logicielle avec `pytest` et `sqlite3` simulant la réception d'une trame JSON de télémétrie.
* Émulateur d'assertions où vous devez écrire les conditions de test (`assert code == 200`, `assert statut is True`).

---

### 📝 8. Grand Quiz d'Examen & Pont de Correction Actif
* 12 questions techniques de synthèse réparties sur l'ensemble du programme.
* **Pont Pédagogique Actif** : Dès qu'une réponse est erronée, l'application extrait automatiquement la fiche de cours complète de l'Encyclopédie et l'affiche directement sous la question.

---

### 📈 9. Dashboard Analytique & Suivi des Scores
* **Courbe d'Évolution** : Graphique temporel suivant l'évolution de vos notes.
* **Radar des Compétences** : Taux d'acquisition par domaine (Réseaux, Cyber, Prog, SysAdmin, Élec/IoT, Modélisation).
* **Recommandations Sur-Mesure** : Plan d'action rédigé par un professeur expert ciblant votre matière la plus fragile de la semaine.

---

### 📋 10. Gestion de Projet E6 & Diagramme de Gantt
* Gestionnaire dynamique de tâches de projet (Nom, Dates de début/fin, Avancement %, Responsable).
* **Génération automatique d'un planning de Gantt professionnel** (via Matplotlib) exportable sous forme d'image pour votre diaporama ou dossier de soutenance.

---

### 📹 11. Vidéothéconomie & Liens Utiles
* Lecteurs YouTube intégrés pour suivre vos professeurs préférés directement dans l'application :
  - **Julien Code** : C++ et bases du BTS CIEL.
  - **Stéphane Michelet** : Traitement du signal, Shannon, PWM/MLI.
  - **IT-Connect & Cocadmin** : VLANs Cisco, Active Directory, Windows Server & Linux.
* Répertoire complet des plateformes d'entraînement : Thierry Vaira, NetAcad, TryHackMe, Root-Me, OpenClassrooms, GitHub.

---

## 🛠️ Dépannage (FAQ / Troubleshooting)

### ❓ La commande `streamlit run` n'est pas reconnue
* Assurez-vous d'avoir bien activé votre environnement virtuel (`source venv/bin/activate` ou `.\venv\Scripts\activate`).
* Vous pouvez aussi lancer l'application avec :
  ```bash
  python -m streamlit run app-v8.py
  ```

### ❓ Le port 8501 est déjà utilisé
Si une autre instance est en cours d'exécution, lancez l'application sur un autre port :
```bash
streamlit run app-v8.py --server.port 8502
```

### ❓ Comment réinitialiser mes statistiques ou les tâches du projet E6 ?
Dans l'application :
* Rendez-vous dans **📈 Analyse des Scores** et cliquez sur **"Réinitialiser mon historique d'études"**.
* Rendez-vous dans **📋 Suivi de Projet E6** et cliquez sur **"Réinitialiser le projet d'origine"**.

---

## 🌐 Références & Remerciements

Ce projet s'appuie sur les ressources incontournables de la communauté BTS CIEL / SN-IR :
- **Thierry Vaira** (*tvaira.free.fr*) — La référence absolue des cours et TP d'informatique et réseaux.
- **IT-Connect** (*it-connect.fr*) — Articles et tutoriels système & réseau francophones.
- **Cisco Networking Academy** (*netacad.com*) — Cours de référence CCNA & CyberOps.
- **Julien Code**, **Stéphane Michelet**, **Cocadmin** — Pour leurs contenus vidéo pédagogiques de grande qualité.

---

<p align="center">
  <b>Bonnes révisions et pleine réussite à vos épreuves de BTS CIEL ! 🎓🚀</b>
</p>
