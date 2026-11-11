# 🎓 Compagnon d'Apprentissage & Studio de Révision — BTS CIEL (Option A & B)

Bienvenue sur le dépôt officiel du **Compagnon d'Apprentissage et Studio de Révision BTS CIEL (Cybersécurité, Informatique et réseaux, Électronique)**.

Ce projet fournit un écosystème pédagogique local interactif pour préparer et réussir les trois épreuves majeures du diplôme :
- **E4 : Épreuve Technique Écrite** (Réseaux, Cybersécurité, C++, IoT, SysML & Mathématiques).
- **E5 : Activités Professionnelles & TP d'Atelier** (Configurations Cisco IOS, Linux Debian, Active Directory, pfSense, Wireshark, Oscilloscope).
- **E6 : Projet de Fin d'Études** (Cahier des charges AFNOR, Modélisation UML, Développement, PVL Pytest & Soutenance).

---

## 📑 Table des Matières

1. [✨ Fonctionnalités Principales](#-fonctionnalités-principales)
2. [🏗️ Structure du Dépôt](#️-structure-du-dépôt)
3. [🚀 Guide d'Installation & Lancement Local](#-guide-dinstallation--lancement-local)
4. [🗺️ Architecture des 7 Pôles d'Ingénierie (29 Onglets)](#️-architecture-des-7-pôles-dingénierie-29-onglets)
5. [🛠️ Dépannage & FAQ](#️-dépannage--faq)
6. [🌐 Crédits & Références](#-crédits--références)

---

## ✨ Fonctionnalités Principales

- 📖 **Encyclopédie de Cours Exhaustive** : Couverture intégrale des 6 grands piliers du référentiel (Réseaux, Cybersécurité, Dev C++/Python, Administration Système Linux/Active Directory, Électronique/IoT, Modélisation SysML/UML).
- 🛠️ **Guide Réussite Épreuve E5 (TP & Pratique)** : 8 fiches réflexes d'atelier couvrant les configurations Cisco IOS, Linux Debian, Active Directory, pfSense DMZ, Wireshark, Oscilloscope, Bus industriels et la grille de diagnostic.
- 📄 **Fiches Savoir N°1 à N°12 & Fiches Montage N°1-2** : Synthèses techniques illustrées (Pont en H BTS7960, Pull-Up/Down, PWM MLI, Interruptions AVR, Mémoire ATmega328P, Boucle 4-20 mA, Capteurs, Relais, Bauds/bps, XON/XOFF, Routage IP, C++ LED, Vérins, Relais 230V).
- 🛡️ **Ateliers Cybersécurité & Gouvernance** : Méthodologie EBIOS RM (5 Ateliers ANSSI), Analyse d'impact PIA / AIPD (RGPD Art. 35, 9 critères CNIL), PKI OpenSSL (X.509, SAN), Matrice des flux pfSense LAN/DMZ/WAN et ports Active Directory (53, 88, 389, 636, 445, 135).
- 🗂️ **105 Flashcards Actives avec Suivi de Progression** : Cartes mémoire réflexes avec notes/conseils de professeurs, liens vers les sections du cours, vidéos recommandées et suivi du taux de maîtrise.
- 📝 **Grand Quiz d'Examen (70 Questions)** : Générateur de questionnaires d'examen paramétrables (10 à 70 questions) avec pont de correction automatique renvoyant vers le cours en cas d'erreur.
- ⚡ **5 Sandboxes & Terminaux Pratiques** : Consoles interactives sans danger pour Cisco IOS, Linux Bash, C++ Debugger, Windows PowerShell Active Directory, et IoT (Modbus RTU/MQTT/Sockets Python).
- 📄 **Datasheets Constructeurs en Anglais** : Fiches de spécifications techniques pour ATmega328P, ESP32, STM32F4, MCP2515 CAN, MAX485, BTS7960, L298N, MAX6675, DHT22 avec quiz d'anglais technique.
- 🔍 **Captures Wireshark PCAP Commentées** : Décodage champ par champ du Handshake TCP 3-way, DHCP DORA, DNS, Modbus RTU, CAN 2.0A/B, TLS 1.3 et décodeur hexadécimal brut.
- 📁 **Ingénierie de Projet E6 (PVL & CdCf AFNOR)** : Modèles de Cahiers des Charges AFNOR, matrice de traçabilité des exigences SysML ReqIF, recettes automatisées Pytest et procès-verbaux FAT/SAT.
- 🛡️ **Guides de Durcissement ANSSI** : Hardening Linux Debian, Active Directory Tiering Model (T0/T1/T2, LAPS), Wi-Fi WPA3-Enterprise 802.1X EAP-TLS.
- 🇬🇧 **Anglais Technique & Oral BTS** : Lexique bilingue 100+ termes, textes de compréhension écrite et trame de soutenance orale en anglais.
- 📊 **Tableau de Bord & Gantt E6** : Suivi analytique des notes, radar de compétences, et générateur de diagrammes de Gantt exportables via Matplotlib.

---

## 🏗️ Structure du Dépôt

```text
.
├── app-v27.py                     # Application Web Streamlit Ultime (29 Onglets / 7 Pôles)
├── structure_notebook_ciel-v3.md  # Carnet de bord & Référentiel Markdown complet
├── TUTO_INSTALLATION.md           # Guide pas-à-pas d'installation Windows & Linux
├── scores_history_v3.json        # Persistance locale de l'historique des notes
├── e6_project.json               # Persistance locale du planning de projet E6 (Gantt)
├── README.md                      # Documentation officielle du dépôt (ce fichier)
└── requirements.txt              # Dépendances Python (streamlit, pandas, matplotlib, etc.)
```

---

## 🚀 Guide d'Installation & Lancement Local

### 1. Prérequis
- **Python 3.9 à 3.12** (`python --version` ou `python3 --version`).

### 2. Télécharger le Dépôt
Décompressez le projet dans un dossier dédié sur votre ordinateur.

### 3. Créer un Environnement Virtuel
- **Linux / macOS** :
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows** :
  ```powershell
  python -m venv venv
  .env\Scriptsctivate
  ```

### 4. Installer les Dépendances
```bash
pip install streamlit pandas matplotlib numpy requests
```

### 5. Lancer l'Application
```bash
streamlit run app-v27.py
```
👉 Accédez à l'application sur **`http://localhost:8501`**.

---

## 🗺️ Architecture des 7 Pôles d'Ingénierie (29 Onglets)

### 🏠 Pôle 1 : Vue d'Ensemble & Bilan
1. `🏠 Accueil & Dashboard`
2. `🗓️ Planning Révisions BTS Blanc (9-11 Déc)`
3. `📈 Analyse des Scores`
4. `📋 Planning de Projet E6 (Gantt)`

### 🎓 Pôle 2 : Préparation BTS Blanc (Examens)
5. `🗓️ Révision Semaine par Semaine (BTS Blanc)`
6. `🎯 Révision Totale BTS Blanc (9-11 Déc)`
7. `🎯 Annales BTS (2024 & 2025)`
8. `📝 Grand Quiz d'Examen`

### 📚 Pôle 3 : Cours, Fiches & TPs
9. `📚 Encyclopédie des Cours & TPs`
10. `🛠️ Fiches Réussite Épreuve E5 (TP & Pratique)`
11. `📄 Fiches Savoir & Fiches Montage`
12. `🛡️ TP Cybersécurité, Gouvernance & pfSense`

### 📐 Pôle 4 : Mathématiques & Physique
13. `📊 Mathématiques : Suites Arithmétiques & Géométriques`
14. `📈 Mathématiques : Fonctions, Exponentielle & Logarithme`
15. `⚡ Lab Kirchhoff, Ohm & Circuits`
16. `📺 Lab Oscilloscope & Mesures Physiques`

### 🧪 Pôle 5 : Laboratoires, Calculs & Sandboxes
17. `🧮 Laboratoire de Calculs (Subnetting & Élec)`
18. `📐 Laboratoire UML & SysML`
19. `🔍 Lab Décodeur Wireshark`
20. `💻 Sandboxes & Terminaux Pratiques`
21. `🧪 Qualification & Tests E6`

### 📄 Pôle 6 : Documentation & Ressources Métier
22. `📄 Datasheets & Fiches Techniques (Composants)`
23. `🔍 Captures de Trames & Analyses Wireshark PCAP`
24. `📁 Modèles de Livrables & PVL Épreuve E6`
25. `🛡️ Guides de Durcissement (Hardening) ANSSI`
26. `🇬🇧 Vocabulaire & Anglais Technique BTS`

### 🗂️ Pôle 7 : Flashcards & Ressources
27. `🗂️ Flashcards Actives`
28. `📹 Vidéos de Cours`
29. `🌐 Répertoire des Liens`

---

## 🛠️ Dépannage & FAQ

### ❓ Formules mathématiques
Toutes les expressions mathématiques sont auditées sous forme de chaînes brutes Python (`r"..."`). Si KaTeX ne se rafraîchit pas, faites `F5` ou relancez l'application.

### ❓ Commande non reconnue
Vérifiez l'activation de l'environnement virtuel (`venv`) avant d'exécuter `streamlit run app-v27.py`.

### ❓ Port déjà utilisé
`streamlit run app-v27.py --server.port 8502`

---

## 🌐 Crédits & Références
- **Thierry Vaira** — La référence des cours et TPs d'informatique et réseaux.
- **IT-Connect** — Tutoriels d'administration système et réseau.
- **ANSSI** — Guides officiels de durcissement et méthode EBIOS RM.
- **CNIL** — Méthodologie PIA / AIPD et conformité RGPD.
- **Cisco Networking Academy** — Support de référence Réseaux & Cybersécurité.

---

<p align="center"><b>Excellentes révisions et pleine réussite au BTS CIEL ! 🎓⚡</b></p>
