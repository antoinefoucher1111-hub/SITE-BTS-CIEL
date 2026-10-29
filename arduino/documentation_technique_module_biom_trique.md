# Projet BTS CIEL – Drink Manager

## Module d'Identification Biométrique (Capteur AS608)

Ce document décrit l'intégration et la configuration du module de contrôle d'accès biométrique. Ce sous-système repose sur une architecture combinant un microcontrôleur Arduino UNO et un capteur d'empreintes digitales optique, interfacés avec l'unité de supervision (Raspberry Pi 5).

### Sommaire

1. [Nomenclature Matérielle](#1-nomenclature-matérielle)
2. [Schéma de Raccordement](#2-schéma-de-raccordement)
3. [Procédure de Validation (Arduino)](#3-procédure-de-validation-arduino)
4. [Configuration de l'Unité de Supervision](#4-configuration-de-lunité-de-supervision)
5. [Arborescence du Dépôt](#5-arborescence-du-dépôt)
6. [Plan d'Action / Reste à Faire](#6-plan-daction--reste-à-faire)

---



### 1. Nomenclature Matérielle


| Composant                | Référence       | Fonction dans l'architecture                                                                 |
| ------------------------ | --------------- | -------------------------------------------------------------------------------------------- |
| **Microcontrôleur**      | Arduino UNO     | Traitement des signaux du capteur et gestion de la liaison série avec le Raspberry Pi.       |
| **Capteur Biométrique**  | AS608 (JM-101B) | Acquisition optique et stockage local des gabarits d'empreintes (DSP intégré).               |
| **Unité de Supervision** | Raspberry Pi 5  | Hébergement de l'application Drink Manager, gestion de la base de données et logique métier. |
| **Connectique**          | Câbles Dupont   | Bus de données UART et alimentation (5V/GND).                                                |


---



### 2. Schéma de Raccordement

Le capteur communique avec la carte Arduino via un bus de terrain (UART). *Statut : Montage réalisé et validé.*


| Broche Capteur (AS608)  | Câblage physique     | Broche Arduino UNO | Observations                            |
| ----------------------- | -------------------- | ------------------ | --------------------------------------- |
| **VCC (Rouge)**         | Alimentation         | **5V**             | Tolérance 5V confirmée pour le JM-101B. |
| **GND (Noir ou Vert)**  | Référence commune    | **GND**            |                                         |
| **TX (Jaune ou Blanc)** | Émission de données  | **D2**             | Configuré en *RX* via `SoftwareSerial`. |
| **RX (Vert ou Bleu)**   | Réception de données | **D3**             | Configuré en *TX* via `SoftwareSerial`. |


---



### 3. Procédure de Validation (Arduino)

La validation matérielle requiert l'enregistrement (enrôlement) et la vérification des empreintes via l'environnement de développement.

**Protocole :**

1. Intégrer la dépendance `Adafruit Fingerprint Sensor Library` via le gestionnaire de bibliothèques de l'IDE Arduino.
2. Déployer le programme d'enrôlement (`Fichier → Exemples → Adafruit Fingerprint Sensor Library → enroll`).
3. Interagir via le Moniteur Série (Baudrate : 9600) pour générer un nouvel identifiant (ID).
4. Déployer le programme de validation (`fingerprint`) pour certifier la reconnaissance du gabarit biométrique enregistré.

---



### 4. Configuration de l'Unité de Supervision

1. **Préparation de l'OS :** Image **Raspberry Pi OS (64-bit)** déployée via *Raspberry Pi Imager*.
2. **Paramètres d'amorçage :** Configuration *headless* (nom d'hôte, accès réseau sécurisé, service SSH activé).
3. **Connectivité :** Interface réseau Ethernet activée (adressage DHCP par défaut).

---



### 5. Arborescence du Dépôt

```text
docs/
└── biometrie/
    ├── README.md          # Présente documentation matérielle et logicielle
    └── cablage_AS608.jpg  # Représentation graphique du circuit matériel
```

---



### 6. Plan d'Action / Reste à Faire

- [ ] **Développement :** Pousser les codes sources définitifs (enrôlement et lecture) sur le dépôt Git. 
- [ ] **Documentation :** Spécifier le protocole de communication série (trames de données) entre l'Arduino et le Raspberry Pi.
- [ ] **Intégration Logicielle :** Développer le script (Python/Node.js) sur le Raspberry Pi permettant de lier l'ID de l'empreinte au profil utilisateur dans la base de données du Drink Manager.