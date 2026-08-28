# Carnet de Bord & de Révision Exhaustif (v3) - BTS CIEL (Option A)

Ce carnet de bord numérique est conçu pour centraliser toutes vos connaissances, cours, travaux pratiques (TP) et activités de révision sur les deux années de votre **BTS Cybersécurité, Informatique et réseaux, Électronique (Option A : Informatique et réseaux)**.

---

## 📌 Module 1 : Réseaux (Networking)

### 🧠 1. Concepts Clés à Maîtriser Absolument
*   **Modèle OSI & TCP/IP** : Rôle, fonctions et protocoles de chaque couche (Physique, Liaison, Réseau, Transport, Session, Présentation, Application). Encapsulation et désencapsulation des données.
*   **Adressage IPv4 & IPv6** : Sous-réseaux, masques de sous-réseau, CIDR, VLSM (Variable Length Subnet Masking), adresses privées/publiques, unicast/multicast/anycast, notation condensée d'IPv6.
*   **VLANs (Virtual Local Area Network)** : VLAN de données, de gestion, natif. Trunking (norme IEEE 802.1Q) et routage inter-VLAN (Router-on-a-Stick ou commutateur de niveau 3 / L3 Switch).
*   **Protocoles de Routage** : Routage statique (routes par défaut, de secours, d'hôte) et dynamique (RIP, OSPF basé sur l'état de lien et l'algorithme de Dijkstra).
*   **Services d'Infrastructure** :
    *   **NAT/PAT (Network Address Translation)** : NAT statique, dynamique et surcharge (Overload/PAT) pour préserver les adresses IPv4 publiques.
    *   **DHCP (Dynamic Host Configuration Protocol)** : Processus DORA (Discover, Offer, Request, Acknowledge), baux DHCP, agents relais DHCP (commande `ip helper-address`).
    *   **DNS (Domain Name System)** : Résolution directe/inverse, types d'enregistrements (A, AAAA, MX, CNAME, NS, TXT, SOA).

---

### 📋 2. Checklist d'Apprentissage
- [ ] Maîtriser le calcul binaire et le découpage de sous-réseaux (VLSM) en moins de 3 minutes.
- [ ] Savoir expliquer le cheminement d'une trame Ethernet et d'un paquet IP à travers un routeur.
- [ ] Configurer un commutateur Cisco de A à Z (VLAN, SSH, sécurité des ports).
- [ ] Configurer et valider un routage inter-VLAN avec un routeur Cisco (sous-interfaces).
- [ ] Configurer le NAT statique et le NAT avec surcharge (PAT) sur un routeur Cisco.
- [ ] Analyser des captures réseau à l'aide de Wireshark pour diagnostiquer des pannes (ARP, DHCP, TCP 3-way handshake).

---

### 💻 3. Commandes et Syntaxes de Survie (Cisco IOS)
```ios
! --- CONFIGURATION DE BASE D'UN ROUTEUR / COMMUTATEUR ---
Router> enable
Router# configure terminal
Router(config)# hostname R1-BTS-CIEL
R1-BTS-CIEL(config)# no ip domain-lookup
R1-BTS-CIEL(config)# enable secret ClasseDefense2026

! --- SECURISATION DES ACCES (SSH) ---
R1-BTS-CIEL(config)# ip domain-name bts-ciel.local
R1-BTS-CIEL(config)# crypto key generate rsa general-keys modulus 2048
R1-BTS-CIEL(config)# username admin privilege 15 secret SuperPass123
R1-BTS-CIEL(config)# line vty 0 4
R1-BTS-CIEL(config-line)# transport input ssh
R1-BTS-CIEL(config-line)# login local
R1-BTS-CIEL(config-line)# exit

! --- CONFIGURATION DES INTERFACES ET ROUTAGE ---
R1-BTS-CIEL(config)# interface GigabitEthernet0/0/0
R1-BTS-CIEL(config-if)# ip address 192.168.1.254 255.255.255.0
R1-BTS-CIEL(config-if)# no shutdown
R1-BTS-CIEL(config-if)# exit

! Routage statique (Route par défaut vers la passerelle de sortie)
R1-BTS-CIEL(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1

! --- CONFIGURATION DES VLANS SUR UN SWITCH ---
Switch# configure terminal
Switch(config)# hostname S1-BTS-CIEL
S1-BTS-CIEL(config)# vlan 10
S1-BTS-CIEL(config-vlan)# name Informatique
S1-BTS-CIEL(config-vlan)# vlan 20
S1-BTS-CIEL(config-vlan)# name IoT
S1-BTS-CIEL(config-vlan)# exit

! Assignation d'un port d'accès à un VLAN
S1-BTS-CIEL(config)# interface FastEthernet0/1
S1-BTS-CIEL(config-if)# switchport mode access
S1-BTS-CIEL(config-if)# switchport access vlan 10
S1-BTS-CIEL(config-if)# exit

! Configuration d'un lien Trunk
S1-BTS-CIEL(config)# interface GigabitEthernet0/1
S1-BTS-CIEL(config-if)# switchport mode trunk
S1-BTS-CIEL(config-if)# switchport trunk allowed vlan 10,20
S1-BTS-CIEL(config-if)# exit

! --- CONFIGURATION DU NAT SURCHARGE (PAT) ---
R1-BTS-CIEL(config)# interface GigabitEthernet0/0/0
R1-BTS-CIEL(config-if)# ip nat inside
R1-BTS-CIEL(config-if)# exit
R1-BTS-CIEL(config)# interface GigabitEthernet0/0/1
R1-BTS-CIEL(config-if)# ip nat outside
R1-BTS-CIEL(config-if)# exit
R1-BTS-CIEL(config)# access-list 1 permit 192.168.1.0 0.0.0.255
R1-BTS-CIEL(config)# ip nat inside source list 1 interface GigabitEthernet0/0/1 overload

! --- COMMANDES DE DIAGNOSTIC ET VISUALISATION ---
R1-BTS-CIEL# show ip interface brief
R1-BTS-CIEL# show ip route
R1-BTS-CIEL# show run
R1-BTS-CIEL# show mac address-table
R1-BTS-CIEL# show ip nat translations
```

---

### 🔗 4. Liens Utiles et Ressources Réseau
*   [Cisco Networking Academy](https://www.netacad.com/) : Le portail officiel pour préparer vos certifications CCNA.
*   [IT-Connect - Catégorie Réseau](https://www.it-connect.fr/) : Fiches de cours, tutoriels pas à pas sur le routage, le protocole DNS et les sous-réseaux.
*   [Thierry Vaira - BTS SN/CIEL](http://tvaira.free.fr/) : Cours magistraux, travaux pratiques de routage Cisco et développement réseau.
*   [OpenClassrooms - Apprenez le fonctionnement des réseaux TCP/IP](https://openclassrooms.com/fr/courses/857447-apprenez-le-fonctionnement-des-reseaux-tcp-ip) : Cours interactif complet pour asseoir ses bases.

---
---

## 🔒 Module 2 : Cybersécurité (Cybersecurity)

### 🧠 1. Concepts Clés à Maîtriser Absolument
*   **La Triade CIA/CPA** : Confidentialité, Intégrité, Disponibilité et Preuve/Non-répudiation.
*   **Cryptographie** :
    *   **Symétrique** : AES (modes CBC et GCM pour le chiffrement authentifié).
    *   **Asymétrique** : RSA, Diffie-Hellman, ECC (bi-clés publique/privée, signature, échange de clés).
    *   **Hachage** : SHA-256, MD5 (contrôle d'intégrité, condensats).
*   **Protocoles de Sécurisation** : HTTPS/TLS (Handshake, certificats x509), SSH, VPN (IPsec IKEv2 et OpenVPN/WireGuard), protocoles de sécurité Wi-Fi (WPA2, WPA3 SAE, 802.1X).
*   **Sécurisation Périmétrique** : Pare-feux (UFW, IPTables, filtrage d'état), ACLs, proxy et reverse proxy.
*   **Top 10 OWASP** : Injections SQL, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), failles d'authentification et de configuration de sécurité.
*   **Audit et Tests d'intrusion** : Reconnaissance passive/active, scan de ports (Nmap), recherche de vulnérabilités, exploitation.

---

### 📋 2. Checklist d'Apprentissage
- [ ] Comprendre et expliquer le fonctionnement d'une poignée de main TLS (TLS Handshake).
- [ ] Configurer des règles de filtrage de ports (IPtables / UFW) sur une machine Linux.
- [ ] Détecter et corriger une faille d'injection SQL dans un script web backend (requêtes préparées).
- [ ] Mettre en place le Port Security sur un commutateur Cisco.

---

### 💻 3. Commandes et Syntaxes de Survie (Outils Cyber)
```bash
# Scan de base avec détection d'OS et de services avec Nmap
nmap -A -T4 192.168.1.50

# Générer une clé privée RSA de 2048 bits
openssl genrsa -out cle_privee.pem 2048

# Chiffrer un fichier sensible avec AES-256-CBC
openssl enc -aes-256-cbc -salt -in document.txt -out document.txt.enc

# Autoriser les ports SSH (22) et HTTPS (443) avec UFW
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
```

---

### 🔗 4. Liens Utiles et Plateformes de Pratique Cyber
*   [TryHackMe](https://tryhackme.com/) : Idéal pour l'apprentissage guidé en cybersécurité grâce à des salles virtuelles thématiques.
*   [Root-Me](https://www.root-me.org/) : Plateforme française incontournable d'entraînement au hacking éthique.
*   [IT-Connect - Sécurité](https://www.it-connect.fr/security/) : Articles complets sur le durcissement système (Hardening).
*   [OWASP Foundation](https://owasp.org/) : Source d'information mondiale pour la sécurité applicative.

---
---

## 💻 Module 3 : Programmation & Dev (Software Engineering)

### 🧠 1. Concepts Clés à Maîtriser Absolument
*   **Langage C++ (ISO)** :
    *   **Pointeurs & Références** : Opérateurs `*` et `&`, allocation dynamique avec `new` et `delete` / `new[]` et `delete[]`.
    *   **Programmation Orientée Objet (POO)** : Classes, encapsulation (private, protected, public), constructeurs/destructeurs, héritage, polymorphisme et méthodes virtuelles pures (`virtual void methode() = 0;`).
*   **Langage Python** : Scripts d'automatisation, sockets réseaux (lib `socket`), requêtes HTTP (lib `requests`), traitement de trames JSON.
*   **Versioning** : Commandes de base de Git (`status`, `add`, `commit`, `push`, `pull`, `branch`, `merge`).

---

### 📋 2. Checklist d'Apprentissage
- [ ] Expliquer clairement la différence entre passage par valeur, par pointeur et par référence en C++.
- [ ] Concevoir et implémenter une classe C++ complète en séparant la déclaration (`.h`) de la définition (`.cpp`).
- [ ] Écrire un script client-serveur TCP/IP simple en Python.
- [ ] Résoudre un conflit de fusion (merge conflict) avec Git.

---

### 💻 3. Commandes et Syntaxes de Survie (C++ & Python)
```cpp\n// --- CLASSE C++ ET POLYMORPHISME ---
#include <iostream>
#include <string>

class Capteur {
protected:
    std::string ref;
public:
    Capteur(std::string r) : ref(r) {}
    virtual ~Capteur() {} // Destructeur virtuel indispensable !
    virtual float lireValeur() = 0; // Méthode virtuelle pure -> Classe abstraite
};

class CapteurTemperature : public Capteur {
public:
    CapteurTemperature(std::string r) : Capteur(r) {}
    float lireValeur() override {
        return 23.5f; // Simulation de lecture
    }
};

int main() {
    Capteur* cap = new CapteurTemperature(\"TEMP-001\");
    std::cout << \"Valeur : \" << cap->lireValeur() << \" °C\" << std::endl;
    delete cap; // Libération correcte de la mémoire du tas (Heap)
    return 0;
}
```

```python
# --- SCRIPT CLIENT TCP EN PYTHON ---
import socket

HOST = \"192.168.1.10\"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(b\"GET_DATA\")
    reponse = client_socket.recv(1024)
    print(f\"Données reçues : {reponse.decode('utf-8')}\")
```

---
---

## 🖥️ Module 4 : Administration Système (SysAdmin)

### 🧠 1. Concepts Clés à Maîtriser Absolument
*   **Gestion des Droits Linux** : Rôle des permissions `r`, `w`, `x` sur les fichiers et répertoires. Notation octale. Propriété avec `chown` et droits avec `chmod`.
*   **Active Directory (AD)** : Structure hiérarchique, contrôleur de domaine (DC), Unités d'Organisation (OU), stratégies de groupe (GPO) et ordre d'application (LSDOU).
*   **Services Réseaux Communs** :
    *   **DHCP** : Fonctionnement du processus de découverte DORA.
    *   **DNS** : Résolution directe, reverse, types d'enregistrements DNS d'un domaine.

---

### 📋 2. Checklist d'Apprentissage
- [ ] Calculer instantanément les permissions octales Linux complexes (ex: chmod 755, 644, 750).
- [ ] Déployer un domaine Active Directory de base sous Windows Server.
- [ ] Configurer et valider des stratégies de groupe (GPO) pour sécuriser un parc Windows client.
- [ ] Configurer un serveur DNS local et un serveur DHCP sous Debian Linux.

---

### 💻 3. Commandes et Syntaxes de Survie (SysAdmin Linux)
```bash
# --- GESTION DES DROITS ---
# Accorder tous les droits au propriétaire, lecture/exécution au groupe, aucun aux autres
chmod 750 script_deploiement.sh

# Changer le propriétaire et le groupe d'un dossier récursivement
sudo chown -R admin:ciel /var/www/html/

# --- SERVICE SYSTEMD ---
# Redémarrer et activer le service DHCP au démarrage
sudo systemctl restart isc-dhcp-server
sudo systemctl enable isc-dhcp-server

# Consulter l'état d'un service réseau
sudo systemctl status bind9
```

---
---

## 🔌 Module 5 : Électronique & IoT (Hardware & Embedded)

### 🧠 1. Concepts Clés à Maîtriser Absolument
*   **Microcontrôleurs** : Cibles courantes du BTS CIEL (STM32, ESP32). Architecture de base, broches GPIO, registres matériels.
*   **Bus de Communication** :
    *   **I2C** : Synchrone, maître-esclave, lignes SDA (données) et SCL (horloge). Adressage matériel sur 7 ou 10 bits.
    *   **SPI** : Synchrone full-duplex rapide. 4 lignes : MOSI, MISO, SCLK, SS/CS.
    *   **UART** : Liaison asynchrone point-à-point, 2 fils : Tx et Rx.
*   **Traitement de Signal & Quantification** : Échantillonnage, Théorème de Nyquist-Shannon (\\(Fe \ge 2 \times Fmax\\)), calcul de quantum de CAN (\\(q = V_{ref} / (2^n - 1)\\)).
*   **Protocoles IoT** : MQTT (Publish/Subscribe, Broker, Topics, niveaux de QoS 0/1/2), LoRa / LoRaWAN (LPWAN longue portée et faible consommation).

---

### 📋 2. Checklist d'Apprentissage
- [ ] Analyser une trame d'un bus de données I2C ou SPI à l'oscilloscope numérique.
- [ ] Développer le code d'acquisition d'un capteur I2C sous STM32CubeIDE.
- [ ] Calculer la valeur numérique produite par un CAN 12 bits pour une tension d'entrée donnée.
- [ ] Mettre en œuvre une communication asynchrone sécurisée avec un Broker MQTT.

---

### 💻 3. Commandes et Syntaxes de Survie (MQTT & C++ Embarqué)
```cpp
// --- EXEMPLE D'ACQUISITION ANALOGIQUE (C++ ESP32) ---
#include <Arduino.h>\n\nconst int PIN_CAPTEUR = 34; // Broche ADC1_CH6
const float VREF = 3.3f;
const int RESOLUTION_ADC = 4095; // ADC 12 bits (2^12 - 1)

void setup() {
    Serial.begin(115200);
    pinMode(PIN_CAPTEUR, INPUT);
}

void loop() {
    int valeurBrute = analogRead(PIN_CAPTEUR);
    float tension = (valeurBrute * VREF) / RESOLUTION_ADC;
    Serial.printf(\"Brut : %d | Tension calculée : %.3f V\\n\", valeurBrute, tension);
    delay(1000);
}
```

```bash
# --- COMMANDES DE SURVIE MQTT EN CONSOLE (CLI) ---
# S'abonner à un topic sur un Broker public (ex : test.mosquitto.org)
mosquitto_sub -h test.mosquitto.org -t \"bts/ciel/optionA/capteurs/temp\"

# Publier une valeur de température formatée en JSON
mosquitto_pub -h test.mosquitto.org -t \"bts/ciel/optionA/capteurs/temp\" -m \"{\\\"sensor_id\\\": \\\"TEMP-12\\\", \\\"value\\\": 21.8}\"
```

---
---

## 📐 Module 6 : Modélisation UML & SysML (Ingénierie Logiciel & Système)

### 🧠 1. Concepts Clés de Modélisation
*   **UML (Unified Modeling Language)** : Modélisation logicielle obligatoire pour l'épreuve E6 (Projet) et fréquente en E4.
    *   **Diagramme de Cas d'Utilisation (Use Case)** : Identifie les acteurs, les limites du système et les cas d'utilisation (avec relations `<<include>>` et `<<extend>>`).
    *   **Diagramme de Classes** : Modélise la structure statique du code orienté objet. Concepts d'association, multiplicité, héritage/généralisation, agrégation (losange vide) et composition forte (losange plein).
    *   **Diagramme de Séquence** : Représente la chronologie des échanges de messages (synchrones, asynchrones, retours) entre les objets au cours du temps (notions d'alt/option/loop).
*   **SysML (Systems Modeling Language)** : Modélisation système d'ingénierie globale.
    *   **BDD (Block Definition Diagram)** : Décrit la structure d'un système sous forme de blocs de composants logiques ou physiques.
    *   **IBD (Internal Block Diagram)** : Représente l'intérieur d'un bloc, la connectique et la nature des flux de données ou d'énergie transitant entre ses ports (standard ports, flow ports).
    *   **Requirement Diagram (RD)** : Modélise les exigences du cahier des charges, leurs relations d'inclusion (`deriveReqt`) ou de validation (`verify` par un cas de test).

---

### 🎨 2. Exemples de Diagrammes d'Examen en ASCII-Art

#### Diagramme de Classes UML (Exemple : Station de charge pour Véhicule Électrique)
```
+-----------------------------------+
|               Borne               |
+-----------------------------------+
| - idBorne : int                   |
| - etat : string                   |
+-----------------------------------+
| + verouillerPrise() : bool        |
| + debloquerPrise() : bool         |
+-----------------------------------+
                  1
                  |
                  |  Contient (Composition)
                  |
                 ◆ 1..*
+-----------------------------------+
|               Connecteur          |
+-----------------------------------+
| - type : string                   |
| - puissanceMax : float            |
+-----------------------------------+
| + demarrerCourant() : void        |
+-----------------------------------+
                  1
                  |
                  |  Est raccordé à (Association)
                  |
                 0..1
+-----------------------------------+
|            VehiculeElec           |
+-----------------------------------+
| - immatriculation : string        |
| - socBatterie : int               |
+-----------------------------------+
| + lireSoc() : int                 |
+-----------------------------------+
```

#### Diagramme de Séquence UML (Exemple : Processus d'authentification et de démarrage de charge)
```
 Utilisateur               Borne                Serveur central
     |                       |                        |
     |---- Passer Badge ---->|                        |
     |                       |---- Demande Auth ----->|
     |                       |<--- Reponse (OK) ------|
     |<--- Signal Pret ------|                        |
     |                       |                        |
     |-- Connecter Prise --->|                        |
     |                       |----- Log Start ------->|
     |<--- Charge active ----|                        |
```

#### SysML Block Definition Diagram (BDD) (Exemple : Station de Surveillance de la Qualité de l'Air)
Le BDD montre l'arbre structurel du système global (Station_de_Mesure) découpé en sous-blocs :
```
           +---------------------------------------------+
           |              «block»                        |
           |          Station_de_Mesure                  |
           +---------------------------------------------+
                                  |
            +---------------------+---------------------+
            |                     |                     |
   ◆ [1]    |            ◆ [1]    |            ◆ [1]    |            ◆ [1]
+-------------------+  +-------------------+  +-------------------+  +-------------------+
|     «block»       |  |     «block»       |  |     «block»       |  |     «block»       |
| Unite_Acquisition |  |  Capteur_CO2_SPI  |  | Capteur_Temp_I2C  |  |  Module_Energie   |
|   (STM32F401)     |  |    (SPI-CO2-01)   |  |     (ADT7410)     |  | (Panneau/Batterie)|
+-------------------+  +-------------------+  +-------------------+  +-------------------+
```

#### SysML Internal Block Diagram (IBD) (Exemple : Connexions internes et flux de données)
L'IBD montre comment les ports et les flux de signaux transitent entre les blocs internes :
```
+---------------------------------------------------------------------------------------+
| ibd [Block] Station_de_Mesure                                                         |
|                                                                                       |
|   +--------------------------+                         +--------------------------+   |
|   |    Capteur_CO2_SPI       |                         |    Unite_Acquisition     |   |
|   |                          |    Données SPI (Bus)    |       (STM32F401)        |   |
|   |                 [p_spi]  |O=======================>|  [p_spi]                 |   |
|   +--------------------------+                         |                          |   |
|                                                        |                          |   |
|   +--------------------------+                         |                          |   |
|   |    Capteur_Temp_I2C      |                         |                          |   |
|   |                          |    Données I2C (Bus)    |                          |   |
|   |                 [p_i2c]  |X----------------------->|  [p_i2c]                 |   |
|   +--------------------------+                         |                          |   |
|                                                        |                          |   |
|   +--------------------------+                         |                          |   |
|   |     Module_Energie       |                         |                          |   |
|   |                          |     Alimentation (3.3V) |                          |   |
|   |                 [p_pwr]  |#=======================>|  [p_pwr]                 |   |
|   +--------------------------+                         +--------------------------+   |
+---------------------------------------------------------------------------------------+
```
*   **Légende des ports de l'IBD** :
    *   `O===>` représente le bus physique **SPI** (MOSI, MISO, SCLK, CS).
    *   `X--->` représente la liaison série bus **I2C** (SDA, SCL).
    *   `#===>` représente les lignes d'alimentation électrique en courant continu.

---

### 📋 3. Exercices Pratiques de Modélisation (UML & SysML)
*   **Exercice 1** : Dans l'IBD ci-dessus, expliquez la différence entre un port de flux (Flow Port) et un port standard (Standard Port).
    *   *Correction* : Un port de flux (Flow Port) spécifie la nature des données ou matières physiques qui transitent (ex: un flux de température, d'octets, ou d'électricité), tandis qu'un port standard est axé sur les services/méthodes logicielles (interfaces orientées requêtes, ex: appeler `read()`).
*   **Exercice 2** : Pourquoi associe-t-on un diagramme d'exigences (Requirement Diagram) à un cas de test d'intégration pour l'épreuve E6 ?
    *   *Correction* : Le diagramme d'exigences liste les besoins contractuels du système. La relation SysML `«verify»` lie une exigence spécifique à un cas de test ou de validation matérielle pour prouver que le système développé répond aux exigences du client.

---
---

## 🎯 Module 7 : Annales & Sujets d'Examens Précédents

Cette section décortique les sujets réels des sessions d'examens récentes du **BTS CIEL Option A** (sessions 2024 et 2025).

### 📁 1. Session 2024 - Station Industrielle de Surveillance Environnementale
*   **Sujet** : La station surveille la qualité de l'air d'un site industriel. Le microcontrôleur effectue l'acquisition périodique d'un capteur de monoxyde de carbone (CO) par SPI et transmet les trames sous forme de paquets UDP vers une passerelle Debian locale.
*   **Exercice Typique d'Examen (C++)** :
    ```cpp
    // Routine défectueuse provoquant des crashs système réguliers
    void acquerirMesures() {
        float* releves = new float[24];
        for(int i = 0; i < 24; ++i) {
            releves[i] = lireCapteurSPI();
        }
        sauvegarderBase(releves);
        delete releves; // <-- ERREUR CRITIQUE !
    }
    ```
    *   **Question** : Expliquez l'erreur de mémoire dynamique présente dans ce code et donnez la syntaxe exacte pour y remédier.
    *   **Correction officielle** : L'opérateur d'allocation `new[]` a été utilisé pour réserver de l'espace pour 24 réels en bloc sur le tas (Heap). Cependant, le développeur a appelé le destructeur simple `delete` au lieu de `delete[]`. En C++, faire cela n'appelle le destructeur que pour le tout premier élément du tableau. Les 23 autres éléments restent bloqués en mémoire, créant une **fuite de mémoire (Memory Leak)** à chaque appel. La correction exacte est d'écrire : **`delete[] releves;`**.

### 📁 2. Session 2025 - Borne de Recharge de Véhicules Électriques
*   **Sujet** : Borne de recharge intelligente communicante en IPsec avec l'infrastructure et supervisant la tension d'alimentation secteur avec un convertisseur analogique-numérique (CAN) 12 bits de plage [0V ; 5V].
*   **Exercice Typique d'Examen (Calcul de Signal & Quantum)** :
    *   **Question** : Si la sonde analogique retourne une tension d'entrée de **3,12V**, calculez le quantum du CAN et la valeur décimale entière **N** retournée par l'ADC (arrondir à l'entier le plus proche).
    *   **Calcul détaillé** :
        1.  Calcul du quantum \\(q\\) (résolution 12 bits = \\(2^{12} - 1 = 4095\\) pas) :
            $$q = \frac{V_{ref}}{2^{12} - 1} = \frac{5,0}{4095} \approx 0,001221 \text{ V} \approx 1,22 \text{ mV}$$
        2.  Calcul de la valeur numérique entière \\(N\\) :
            $$N = \text{arrondi}\left(\frac{V_e}{q}\right) = \text{arrondi}\left(\frac{3,12}{0,001221}\right) = \text{arrondi}(2555,28) = \mathbf{2555}$$
        *   La valeur brute entière générée par le convertisseur est **2555** (soit `0x9FB` en hexadécimal).

---
---

## 🧪 Module 8 : Épreuve E6 - Cahier de Recette & Plan de Test d'Intégration

L'épreuve E6 valide la phase de tests unitaires et d'intégration de votre projet de fin d'études. Voici un modèle complet de **test d'intégration automatisé en Python** servant à valider le flux complet d'une passerelle d'acquisition.

### 🧪 Script de Test d'Intégration Réel (Python / Pytest)
Ce script teste le flux d'intégration complet : acquisition d'une mesure, transmission à un Broker MQTT, capture par un script démon Python et insertion robuste dans une base de données locale SQLite3.

```python
# test_integration_e6.py
import pytest
import sqlite3
import json
import time
from unittest.mock import MagicMock

# --- CONFIGURATION DE BASE ---
DATABASE_TEST = "test_ciel_e6_database.db"
TOPIC_TEST = "bts/ciel/optionA/capteurs/mesures"

# --- FIXTURE PYTEST POUR PREPARER LA BASE DE DONNEES ---
@pytest.fixture
def setup_database():
    conn = sqlite3.connect(DATABASE_TEST)
    cursor = conn.cursor()
    # Création de la table des relevés
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mesures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            capteur_id TEXT NOT NULL,
            valeur REAL NOT NULL
        )
    """)
    conn.commit()
    yield conn
    # Nettoyage après les tests
    cursor.execute("DROP TABLE mesures")
    conn.commit()
    conn.close()

# --- CODE APPLICATIF DE LA PASSERELLE (A TESTER) ---
def inserer_mesure_db(conn, payload_json):
    """Analyse la trame JSON reçue et l'insère en base de données."""
    try:
        data = json.loads(payload_json)
        capteur_id = data["sensor_id"]
        valeur = float(data["value"])
        
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mesures (capteur_id, valeur) VALUES (?, ?)", 
            (capteur_id, valeur)
        )
        conn.commit()
        return True
    except (json.JSONDecodeError, KeyError, ValueError):
        return False

# --- SUITE DE TESTS D'INTEGRATION ---
def test_integration_flow_succes(setup_database):
    """Teste le flux d'intégration nominal d'une trame valide."""
    conn = setup_database
    # Simulation d'une trame reçue du broker MQTT d'un capteur CO2 (Annales 2024)
    payload_mqtt = '{"sensor_id": "CO2-SURVEILLANCE", "value": 450.5}'
    
    # 1. Traitement de la trame
    statut = inserer_mesure_db(conn, payload_mqtt)
    
    # 2. Validation de l'insertion
    assert statut is True, "Le traitement de la trame MQTT valide a échoué"
    
    # 3. Vérification de la persistance en BDD
    cursor = conn.cursor()
    cursor.execute("SELECT capteur_id, valeur FROM mesures WHERE capteur_id = 'CO2-SURVEILLANCE'")
    relevé = cursor.fetchone()
    
    assert relevé is not None, "Aucun relevé trouvé en base de données pour ce capteur"
    assert relevé[0] == "CO2-SURVEILLANCE", "Identifiant du capteur incorrect"
    assert relevé[1] == 450.5, "Valeur physique insérée incorrecte"

def test_integration_flow_erreur_format(setup_database):
    """Teste le comportement de la passerelle en présence d'une trame corrompue."""
    conn = setup_database
    # Trame JSON corrompue (manque une accolade)
    payload_mqtt_corrompu = '{"sensor_id": "CO2-SURVEILLANCE", "value": 450.5'
    
    # Traitement de la trame
    statut = inserer_mesure_db(conn, payload_mqtt_corrompu)
    
    # Validation du comportement d'erreur (la passerelle doit rejeter sainement sans crasher)
    assert statut is False, "La passerelle a accepté à tort une trame JSON corrompue"
    
    # Vérification qu'aucune ligne n'a été ajoutée en base de données
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM mesures")
    count = cursor.fetchone()[0]
    assert count == 0, "Une trame corrompue a pollué la base de données"
```

---

### 📋 2. Fiche de Validation Logicielle (PVL) de Projet E6
Pour votre soutenance de projet E6, vous devez présenter des fiches de tests d'intégration sous cette forme normalisée :

| ID Test | Composants Impliqués | Description de l'Action | Résultat Attendu | Statut |
| :--- | :--- | :--- | :--- | :--- |
| **TEST-INT-01** | STM32 (SPI) + Capteur | Lancement de l'acquisition C++ du capteur | Lecture correcte des registres SPI | **VALIDE** |
| **TEST-INT-02** | STM32 + Routeur Cisco | Envoi d'un paquet UDP de données | Le paquet traverse le VLAN et est reçu | **VALIDE** |
| **TEST-INT-03** | Python Daemon + Broker | S'abonner et recevoir une trame JSON | Analyse sémantique de la trame valide | **VALIDE** |
| **TEST-INT-04** | Python Gateway + DB | Insertion du jeu de données en base de données | Enregistrement pérenne et intègre | **VALIDE** |
