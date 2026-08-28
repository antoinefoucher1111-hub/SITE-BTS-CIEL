import streamlit as st
import random
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# --- CONFIGURATION STREAMLIT ---
st.set_page_config(
    page_title="BTS CIEL Pro Studio - Excellence Numérique",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuration Matplotlib Headless
import matplotlib
matplotlib.use('Agg')

# --- STYLE CSS MODERNE & IMMERSIF (UI/UX PRO) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    code, pre {
        font-family: 'Fira Code', monospace !important;
    }
    
    /* Header & Hero */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #1e293b 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 16px !important;
        padding: 30px 40px !important;
        margin-bottom: 25px !important;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3) !important;
        color: #ffffff !important;
    }
    .hero-title {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #1d4ed8, #4338ca, #0369a1) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 8px !important;
    }
    .hero-container .hero-title {
        background: linear-gradient(90deg, #93c5fd, #c4b5fd, #7dd3fc) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    .hero-subtitle {
        font-size: 1.1rem !important;
        color: #cbd5e1 !important;
        font-weight: 400 !important;
    }
    
    /* Badges & Tags */
    .badge {
        display: inline-block !important;
        padding: 4px 10px !important;
        border-radius: 9999px !important;
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        margin-right: 6px !important;
        margin-top: 4px !important;
    }
    .badge-blue { background-color: #1e3a8a !important; color: #dbeafe !important; border: 1px solid #3b82f6 !important; }
    .badge-emerald { background-color: #064e3b !important; color: #d1fae5 !important; border: 1px solid #10b981 !important; }
    .badge-purple { background-color: #3b0764 !important; color: #f3e8ff !important; border: 1px solid #a855f7 !important; }
    .badge-amber { background-color: #451a03 !important; color: #fef3c7 !important; border: 1px solid #f59e0b !important; }
    .badge-rose { background-color: #4c0519 !important; color: #ffe4e6 !important; border: 1px solid #f43f5e !important; }
    
    /* Cards - FIXED CONTRAST TO PREVENT WHITE TEXT ON WHITE BG */
    .ciel-card {
        background: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 14px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 4px 10px -1px rgba(0, 0, 0, 0.08) !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    .ciel-card:hover {
        box-shadow: 0 10px 20px -3px rgba(0, 0, 0, 0.12) !important;
    }
    .ciel-card p, .ciel-card li, .ciel-card ul, .ciel-card span, .ciel-card div, .ciel-card b, .ciel-card i {
        color: #1e293b !important;
    }
    .ciel-card h3 {
        color: #1e3a8a !important;
        font-weight: 700 !important;
    }
    .ciel-card h4 {
        color: #065f46 !important;
        font-weight: 700 !important;
    }
    
    .dark-card {
        background: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 14px !important;
        padding: 22px !important;
        color: #f8fafc !important;
        margin-bottom: 20px !important;
    }
    .dark-card p, .dark-card li, .dark-card span, .dark-card b {
        color: #e2e8f0 !important;
    }
    
    /* Flashcard UI */
    .flashcard-box-modern {
        background: #ffffff !important;
        border: 2px solid #cbd5e1 !important;
        border-radius: 16px !important;
        padding: 35px 25px !important;
        text-align: center !important;
        min-height: 220px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.08) !important;
        margin: 15px 0 !important;
        color: #0f172a !important;
    }
    .flashcard-q-text {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        color: #0f172a !important;
        line-height: 1.5 !important;
    }
    .flashcard-a-box {
        background: #f0fdf4 !important;
        border: 1px solid #86efac !important;
        border-radius: 12px !important;
        padding: 20px !important;
        margin-top: 20px !important;
        color: #14532d !important;
        font-size: 1.05rem !important;
        text-align: left !important;
        line-height: 1.6 !important;
    }
    .flashcard-a-box p, .flashcard-a-box span, .flashcard-a-box div, .flashcard-a-box b {
        color: #14532d !important;
    }
    
    /* Terminals & Consoles */
    .terminal-header {
        background: #0f172a !important;
        color: #38bdf8 !important;
        padding: 10px 16px !important;
        border-top-left-radius: 10px !important;
        border-top-right-radius: 10px !important;
        font-family: 'Fira Code', monospace !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        border: 1px solid #334155 !important;
        border-bottom: none !important;
    }
    .terminal-body {
        background: #020617 !important;
        color: #f8fafc !important;
        padding: 18px !important;
        border-bottom-left-radius: 10px !important;
        border-bottom-right-radius: 10px !important;
        font-family: 'Fira Code', monospace !important;
        border: 1px solid #334155 !important;
        border-top: none !important;
        margin-bottom: 16px !important;
        font-size: 0.9rem !important;
        line-height: 1.6 !important;
    }
    .terminal-dot {
        width: 10px !important;
        height: 10px !important;
        border-radius: 50% !important;
        display: inline-block !important;
    }
    .dot-red { background: #ef4444 !important; }
    .dot-yellow { background: #f59e0b !important; }
    .dot-green { background: #10b981 !important; }
    
    /* Metrics block */
    .stat-box {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        padding: 18px 12px !important;
        text-align: center !important;
        color: #0f172a !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
    }
    .stat-number {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #1d4ed8 !important;
    }
    .stat-label {
        font-size: 0.85rem !important;
        color: #334155 !important;
        font-weight: 600 !important;
        margin-top: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- BASE DE DONNÉES ENCYCLOPÉDIQUE ÉTENDUE ---
COURS_BASE = {
    "📶 Réseaux & Télécoms": {
        "1. Modèle OSI vs TCP/IP & Encapsulation": """### 🌐 Architecture des Protocoles en Réseau
Le **modèle OSI (Open Systems Interconnection)** découpe la communication en 7 couches standardisées :
* **7. Application (PDU: Donnée)** : Protocoles applicatifs de haut niveau (HTTP, HTTPS, DNS, DHCP, SSH, MQTT, SNMP, SMTP).
* **6. Présentation** : Formatage des données, chiffrement (TLS/SSL) et compression (ASCII, UTF-8, JPEG).
* **5. Session** : Gestion et synchronisation des sessions d'échanges (NetBIOS, RPC, Sockets).
* **4. Transport (PDU: Segment / Datagramme)** : Communication de bout en bout et contrôle de flux. **TCP** (orienté connexion, fiable avec accusé de réception ACK et fenêtre glissante) vs **UDP** (sans connexion, rapide, sans garantie d'arrivée, idéal streaming/VoIP/DNS).
* **3. Réseau (PDU: Paquet)** : Routage logique et adressage mondial (IPv4, IPv6, ICMP, IPsec, protocoles OSPF/BGP). Equipement : **Routeur**.
* **2. Liaison de données (PDU: Trame)** : Adressage physique (adresses MAC 48 bits), détection d'erreurs (FCS/CRC32), protocoles Ethernet (802.3), Wi-Fi (802.11). Equipement : **Commutateur (Switch)**.
* **1. Physique (PDU: Bit)** : Transmission des signaux électriques, optiques ou électromagnétiques (RJ45, fibre optique, radio).

**Modèle TCP/IP (4 couches)** : Application, Transport, Internet, Accès Réseau.""",

        "2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)": """### 🧮 Méthodologie du Calcul de Masque & Subnetting
Une adresse **IPv4** fait 32 bits (4 octets). Elle est scindée en **Partie Réseau (NetID)** et **Partie Hôte (HostID)** via le masque de sous-réseau.

#### Règles Fondamentales :
* **Nombre total d'adresses dans un bloc** = $2^{(32 - \\text{CIDR})}$
* **Nombre d'adresses d'hôtes utilisables** = $2^{(32 - \\text{CIDR})} - 2$ (on soustrait l'adresse Réseau où tous les bits d'hôte sont à 0, et l'adresse de Broadcast où tous les bits d'hôte sont à 1).
* **Calcul d'adresse Réseau** = Opération logique `ET (AND)` bit-à-bit entre l'IP et le Masque.
* **Calcul du Broadcast** = Adresse Réseau + $(2^{(32 - \\text{CIDR})} - 1)$.

#### Table Rapide des Masques Fréquents :
* `/24` $\\rightarrow$ `255.255.255.0` (256 adresses, 254 hôtes)
* `/25` $\\rightarrow$ `255.255.255.128` (128 adresses, 126 hôtes)
* `/26` $\\rightarrow$ `255.255.255.192` (64 adresses, 62 hôtes)
* `/27` $\\rightarrow$ `255.255.255.224` (32 adresses, 30 hôtes)
* `/28` $\\rightarrow$ `255.255.255.240` (16 adresses, 14 hôtes)
* `/29` $\\rightarrow$ `255.255.255.248` (8 adresses, 6 hôtes)
* `/30` $\\rightarrow$ `255.255.255.252` (4 adresses, 2 hôtes - Liens point-à-point)

#### Notions IPv6 (128 bits) :
* Notation en 8 groupes de 4 caractères hexadécimaux séparés par des `:`.
* Règle de compression : omission des zéros en tête (`0db8` $\\rightarrow$ `db8`) et remplacement d'une suite continue de groupes de zéros par `::` (une seule fois par adresse).""",

        "3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN": """### 🔀 Segmentation & Routage Virtuel
Un **VLAN (Virtual LAN)** isole logiquement les domaines de diffusion au sein d'un même commutateur physique.

#### Modes de Ports Switch :
* **Port Access** : Appartient à un seul VLAN. Les trames y circulent détaguées (standard Ethernet 802.3).
* **Port Trunk** : Fait transiter plusieurs VLANs simultanément entre switchs ou vers un routeur. Utilise la norme **IEEE 802.1Q** qui insère un tag de **4 octets** dans l'en-tête Ethernet (incluant le VID sur 12 bits, soit 4096 VLANs possibles).

#### Routage Inter-VLAN (Router-on-a-Stick) :
Sur le routeur, une seule interface physique (ex: `g0/0/0`) est découpée en sous-interfaces logiques (`g0/0/0.10`, `g0/0/0.20`) avec la commande `encapsulation dot1Q <ID>`.""",

        "4. Services d'Infrastructure : DHCP, DNS, NAT/PAT": """### ⚙️ Services Réseaux Indispensables
* **DHCP (Dynamic Host Configuration Protocol)** : Attribution dynamique de configuration IP. Processus **DORA** :
  1. `Discover` (Client $\\rightarrow$ 255.255.255.255 en UDP 67/68)
  2. `Offer` (Serveur $\\rightarrow$ Client)
  3. `Request` (Client $\\rightarrow$ Serveur)
  4. `Acknowledge` (Serveur valide le bail IP)
* **DNS (Domain Name System)** : Résolution de noms d'hôtes. Types d'enregistrements : `A` (IPv4), `AAAA` (IPv6), `CNAME` (Alias), `MX` (Serveur mail), `PTR` (Résolution inverse).
* **NAT / PAT (Port Address Translation)** : Translation d'adresses privées (RFC 1918) vers une adresse publique unique en multiplexant les numéros de ports source TCP/UDP."""
    },
    "🔒 Cybersécurité": {
        "1. Cryptographie : Symétrique, Asymétrique & Hachage": """### 🛡️ Les Fondements Cryptographiques
La sécurité repose sur la triade **CIA** (Confidentialité, Intégrité, Disponibilité) + Authenticité et Non-répudiation.

* **Chiffrement Symétrique** : Même clé secrète pour chiffrer et déchiffrer. Rapide, adapté aux flux volumineux. Standard : **AES-128 / AES-256** (modes CBC, GCM avec authentification intégrée).
* **Chiffrement Asymétrique** : Paire de clés mathématiquement liées (Clé Publique distribuable, Clé Privée secrète). Algorithmes : **RSA (2048/4096 bits)**, **ECC (Courbes Elliptiques)**. Utilisé pour l'échange de clés de session et les signatures numériques.
* **Fonctions de Hachage** : Condensat à sens unique de taille fixe. Vérifie l'intégrité stricte. Algorithmes : **SHA-256**, **SHA-3** (MD5 et SHA-1 sont aujourd'hui vulnérables aux collisions).
* **Certificats X.509 & PKI** : Une Autorité de Certification (CA) signe la clé publique d'un serveur pour attester de son identité.""",

        "2. Top 10 OWASP & Sécurité Applicative": """### 🚨 Vulnérabilités Web et Remédiations
* **Injections SQL** : L'attaquant injecte du code SQL non filtré pour manipuler la BDD.
  * *Exemple vulnérable* : `query = "SELECT * FROM users WHERE user='" + input + "'"`
  * *Remédiation absolue* : Utiliser exclusivement des **requêtes préparées (paramétrées)** via PDO en PHP ou `cursor.execute("SELECT * FROM users WHERE user=%s", (input,))` en Python.
* **Cross-Site Scripting (XSS)** : Injection de scripts JavaScript malveillants exécutés par les navigateurs clients.
  * *Remédiation* : Échappement des caractères HTML (`htmlspecialchars()`), CSP (Content Security Policy).
* **CSRF (Cross-Site Request Forgery)** : Forcer un utilisateur authentifié à exécuter des actions non désirées. *Remédiation* : Jetons (tokens) anti-CSRF aléatoires et synchronisés.""",

        "3. Pare-feux, VPN & Sécurisation Système": """### 🧱 Défense Périmétrique et Durcissement
* **Pare-feu Stateful** : Analyse l'état des connexions (table d'états TCP). Sous Linux : `iptables` / `nftables` ou `ufw`.
* **VPN (Virtual Private Network)** :
  * **IPsec** : Opère en couche 3. Protocoles `AH` (Intégrité/Authentification) et `ESP` (Chiffrement + Intégrité). Modes : Transport (hôte à hôte) ou Tunnel (site à site).
  * **OpenVPN / WireGuard** : VPN applicatif et niveau kernel moderne utilisant TLS/chiffrement moderne.
* **Port Security Cisco** : Limite le nombre d'adresses MAC autorisées par port de switch pour contrer le MAC Flooding (`switchport port-security maximum 1`, `switchport port-security violation shutdown`)."""
    },
    "💻 Programmation / Dev": {
        "1. Langage C++ : Mémoire, Pointeurs & POO": """### ⚡ Maîtrise Bas Niveau & Orientée Objet en C++
Le C++ est au cœur du BTS CIEL pour la programmation système et microcontrôleurs embarqués.

#### Gestion de la Mémoire :
* **Pile (Stack)** : Gestion automatique, rapide, portée limitée au bloc `{}`.
* **Tas (Heap)** : Allocation manuelle dynamique avec `new` / `new[]`. Doit obligatoirement être libérée avec `delete` / `delete[]` pour éviter les **fuites de mémoire (Memory Leaks)**.
* **Pointeurs & Références** :
  * `int x = 42; int* p = &x;` $\\rightarrow$ `p` contient l'adresse, `*p` accède à la valeur.
  * `void modifier(int& ref)` $\\rightarrow$ passage par référence (sans copie mémoire).

#### Programmation Orientée Objet (POO) :
* **Encapsulation** : Données membres `private` accessibles via `getters`/`setters` `public`.
* **Héritage** : `class CapteurTemperature : public Capteur`.
* **Polymorphisme & Classes Abstraites** : Méthode déclarée `virtual void mesurer() = 0;` (méthode virtuelle pure). La classe devient abstraite et impose l'implémentation dans les classes dérivées.""",

        "2. Python Réseau, Systèmes & Sockets": """### 🐍 Automatisation & Sockets Réseau en Python
Python est l'outil privilégié pour les scripts de passerelle, de traitement de données IoT et d'administration système.

#### Client TCP Sockets :
```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.1.50', 8080))
    s.sendall(b'GET_TELEMETRY\\n')
    data = s.recv(1024)
    print('Reçu:', data.decode('utf-8'))
```

#### Manipulation de données JSON :
```python
import json
payload = {'capteur_id': 'TEMP_01', 'valeur': 23.4, 'unite': 'C'}
json_str = json.dumps(payload)
```"""
    },
    "🖥️ Administration Système": {
        "1. Droits Linux & Commandes Système": """### 🐧 Administration GNU/Linux
* **Droits Octaux (`chmod`)** :
  * `r` (Lecture) = 4, `w` (Écriture) = 2, `x` (Exécution) = 1.
  * `chmod 750 script.sh` : Propriétaire = `rwx` (7), Groupe = `r-x` (5), Autres = `---` (0).
* **Droits Spéciaux** : SUID (`4000`), SGID (`2000`), Sticky Bit (`1000` ex: `/tmp`).
* **Services Systemd** : `systemctl start|stop|restart|status|enable service_name`.
* **Supervision des logs** : `journalctl -u service_name -f` ou `tail -f /var/log/syslog`.""",

        "2. Active Directory, Domaines & GPO": """### 🏢 Gestion de Parc sous Windows Server
* **Active Directory Domain Services (AD DS)** : Annuaire d'objets (Utilisateurs, Groupes, Ordinateurs).
* **Unités d'Organisation (OU)** : Conteneurs logiques pour organiser le domaine.
* **GPO (Group Policy Object)** : Politiques de configuration et de durcissement centralisées.
* **Ordre d'application des GPO (LSDOU)** : **L**ocal $\\rightarrow$ **S**ite $\\rightarrow$ **D**omaine $\\rightarrow$ **O**U (la dernière stratégie appliquée prévaut sauf configuration 'Enforced')."""
    },
    "🔌 Électronique & IoT": {
        "1. Échantillonnage, CAN/CNA & Théorème de Shannon": """### 📡 Numérisation & Traitement du Signal
* **Théorème de Nyquist-Shannon** : La fréquence d'échantillonnage $Fe$ doit respecter $Fe \\ge 2 \\times F_{max}$ pour éviter tout **repliement de spectre (Aliasing)**. On place un filtre passe-bas anti-repliement avant le CAN.
* **Convertisseur Analogique-Numérique (CAN / ADC)** :
  * Résolution : $n$ bits $\\rightarrow 2^n$ niveaux de quantification (de $0$ à $2^n - 1$).
  * **Quantum ($q$)** : Plus petite variation de tension détectable :
    $$q = \\frac{V_{ref}}{2^n - 1} \\approx \\frac{V_{ref}}{2^n}$$
  * **Valeur numérique entière ($N$)** pour une tension d'entrée $V_e$ :
    $$N = \\text{arrondi}\\left(\\frac{V_e}{q}\\right) = \\text{arrondi}\\left(\\frac{V_e \\times (2^n - 1)}{V_{ref}}\\right)$$""",

        "2. Bus Série Matériels : I2C, SPI, UART & CAN Bus": """### 🔌 Liaisons de Données Embarquées
* **I2C** : 2 lignes bidirectionnelles (`SDA` Données, `SCL` Horloge). Maître-Esclave, adresses matérielles 7 bits sur bus avec résistances de Pull-up.
* **SPI** : 4 lignes full-duplex rapide (`MOSI`, `MISO`, `SCLK`, `SS/CS`). Sélection d'esclave active à l'état bas.
* **UART** : Liaison asynchrone point-à-point (2 fils `Tx`, `Rx`). Nécessite le même débit en bauds (ex: 115200 bauds, 8N1).
* **Bus CAN** : Bus différentiel robuste (`CAN_H`, `CAN_L`), résistant aux parasites industriels et automobiles. Résistances de terminaison de 120 $\\Omega$ à chaque extrémité.""",

        "3. Protocoles Connectés : MQTT & LoRaWAN": """### ☁️ Protocoles IoT & Télémesure
* **MQTT (Message Queuing Telemetry Transport)** : Architecture Publish/Subscribe autour d'un courtier (**Broker**). Messages légers publiés sur des thèmes (**Topics** ex: `site/batA/temp`). Niveaux de QoS :
  * `QoS 0` : Délivré au plus une fois (sans confirmation).
  * `QoS 1` : Délivré au moins une fois (avec accusé PUBACK).
  * `QoS 2` : Délivré exactement une fois (four-way handshake).
* **LoRaWAN** : Réseau LPWAN longue portée (plusieurs kilomètres) à très faible consommation d'énergie sur fréquences sans licence (868 MHz en Europe)."""
    },
    "📐 Modélisation UML & SysML": {
        "1. Diagrammes UML Essentiels (Classes, Séquence, Use Case)": """### 📐 Ingénierie Logicielle UML
* **Diagramme de Classes** : Modèle statique. Multiplicités (`1`, `0..1`, `1..*`, `*`).
  * **Agrégation (Losange blanc $\\diamond$)** : Relation 'fait partie de' faible. L'élément peut exister sans le conteneur.
  * **Composition (Losange noir $\\blacklozenge$)** : Relation d'appartenance forte. La destruction du conteneur détruit ses composants.
  * **Généralisation/Héritage (Flèche à triangle vide $\\rightarrow$)** : Spécialisation de classe.
* **Diagramme de Séquence** : Chronologie des échanges d'objets au cours du temps. Flèche pleine pour appel synchrone, flèche ouverte pour asynchrone, pointillé pour retour.""",

        "2. Diagrammes SysML (BDD, IBD, Exigences)": """### 🏗️ Modélisation Système SysML
* **BDD (Block Definition Diagram)** : Découpage structurel global du système en blocs matériels et logiciels.
* **IBD (Internal Block Diagram)** : Vue interne des flux de données (`flow ports`), d'énergie et de signaux circulant entre les ports des sous-blocs.
* **Diagramme d'Exigences (Requirement Diagram)** : Définition des critères du cahier des charges avec stéréotypes `<<deriveReqt>>`, `<<satisfy>>` (par un bloc) et `<<verify>>` (par un cas de test)."""
    }
}

# MINI-QUIZ D'AUTO-ÉVALUATION PAR COURS
MINI_QUIZ_COURS = {
    "1. Modèle OSI vs TCP/IP & Encapsulation": {
        "q": "À quelle couche du modèle OSI opère le protocole UDP ?",
        "options": ["Couche 2 (Liaison)", "Couche 3 (Réseau)", "Couche 4 (Transport)", "Couche 7 (Application)"],
        "rep": "Couche 4 (Transport)",
        "expl": "UDP est un protocole de couche Transport (couche 4), tout comme TCP."
    },
    "2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)": {
        "q": "Combien d'adresses d'hôtes utilisables offre un sous-réseau avec un masque /27 ?",
        "options": ["14", "30", "62", "126"],
        "rep": "30",
        "expl": "Pour /27, il reste 32 - 27 = 5 bits pour les hôtes. Soit 2^5 - 2 = 32 - 2 = 30 hôtes utilisables."
    },
    "3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN": {
        "q": "Quelle est la taille en octets du tag inséré par la norme IEEE 802.1Q dans la trame Ethernet ?",
        "options": ["2 octets", "4 octets", "8 octets", "16 octets"],
        "rep": "4 octets",
        "expl": "Le tag 802.1Q inséré dans la trame fait exactement 4 octets (32 bits), dont 12 bits dédiés au VLAN ID."
    },
    "1. Cryptographie : Symétrique, Asymétrique & Hachage": {
        "q": "Quel algorithme parmi les suivants est un algorithme de chiffrement asymétrique ?",
        "options": ["AES-256", "RSA", "SHA-256", "DES"],
        "rep": "RSA",
        "expl": "RSA est un algorithme asymétrique à clé publique/clé privée. AES et DES sont symétriques, SHA-256 est une fonction de hachage."
    },
    "2. Top 10 OWASP & Sécurité Applicative": {
        "q": "Quelle est la méthode la plus robuste pour neutraliser les failles d'injection SQL ?",
        "options": ["Utiliser des expressions régulières de filtrage", "Utiliser des requêtes préparées (paramétrées)", "Chiffrer la base de données en AES", "Désactiver le port MySQL 3306"],
        "rep": "Utiliser des requêtes préparées (paramétrées)",
        "expl": "Les requêtes préparées séparent strictement le code SQL des données utilisateurs saisies, rendant l'injection impossible."
    },
    "1. Langage C++ : Mémoire, Pointeurs & POO": {
        "q": "Quel opérateur C++ doit obligatoirement être utilisé pour libérer un tableau alloué avec 'new float[50]' ?",
        "options": ["delete", "free()", "delete[]", "clear()"],
        "rep": "delete[]",
        "expl": "En C++, toute allocation de tableau dynamique avec 'new[]' requiert impérativement 'delete[]' pour détruire tous les éléments."
    },
    "1. Échantillonnage, CAN/CNA & Théorème de Shannon": {
        "q": "Si un signal audio possède une fréquence maximale de 20 kHz, quelle doit être la fréquence minimale d'échantillonnage (Fe) selon Shannon ?",
        "options": ["10 kHz", "20 kHz", "40 kHz", "80 kHz"],
        "rep": "40 kHz",
        "expl": "Selon le théorème de Nyquist-Shannon, Fe >= 2 * Fmax. Pour 20 kHz, Fe doit être au moins de 40 kHz (ex: 44.1 kHz sur les CD Audio)."
    }
}

# --- FLASHCARDS ACTIVES ÉTENDUES ---
FLASHCARDS_DATA = [
    {"module": "Réseaux", "q": "Quelle est la différence fondamentale entre un commutateur (Switch) et un routeur ?", "a": "Un commutateur opère en Couche 2 (Liaison) et aiguille les trames via les adresses MAC au sein d'un LAN. Un routeur opère en Couche 3 (Réseau) et achemine les paquets entre différents réseaux via les adresses IP."},
    {"module": "Réseaux", "q": "Qu'est-ce que l'encapsulation 802.1Q (Trunking) ?", "a": "C'est un mécanisme normalisé qui insère une étiquette (tag) de 4 octets dans l'en-tête Ethernet pour faire transiter plusieurs VLANs sur un même lien physique."},
    {"module": "Réseaux", "q": "Quelles sont les 4 étapes du protocole DHCP ?", "a": "DORA : Discover (découverte par diffusion), Offer (proposition d'IP par le serveur), Request (demande formelle du client), Acknowledge (validation du bail IP)."},
    {"module": "Cybersécurité", "q": "Quelle est la différence entre chiffrement symétrique et asymétrique ?", "a": "Symétrique : même clé secrète partagée pour chiffrer et déchiffrer (rapide, ex: AES). Asymétrique : paire de clés publique/privée (résout le partage de clé, signature, ex: RSA)."},
    {"module": "Cybersécurité", "q": "Comment fonctionne une attaque XSS (Cross-Site Scripting) ?", "a": "Elle consiste à injecter du code client malveillant (souvent JavaScript) dans une page web pour qu'il soit exécuté par les navigateurs des autres utilisateurs."},
    {"module": "Programmation / Dev", "q": "Qu'est-ce qu'une méthode virtuelle pure en C++ ?", "a": "Une méthode déclarée avec '= 0' (ex: virtual void f() = 0;). Elle rend la classe abstraite et force les classes dérivées à l'implémenter pour pouvoir être instanciées."},
    {"module": "Programmation / Dev", "q": "Pourquoi ne doit-on jamais utiliser delete au lieu de delete[] pour un tableau ?", "a": "Parce que 'delete' simple ne libère que le premier élément du tableau sur le tas et n'appelle pas les destructeurs des éléments suivants, créant une fuite mémoire critique."},
    {"module": "Administration Système", "q": "Que signifie la commande 'chmod 750 fichier.sh' ?", "a": "Propriétaire = 7 (rwx), Groupe = 5 (r-x : lecture et exécution), Autres = 0 (aucun droit)."},
    {"module": "Administration Système", "q": "Quel est l'ordre d'application des stratégies de groupe (GPO) dans Active Directory ?", "a": "Ordre LSDOU : Local -> Site -> Domaine -> Unité d'Organisation (OU). La dernière GPO appliquée a la priorité la plus forte."},
    {"module": "Électronique / IoT", "q": "Quelle est la formule du quantum (q) pour un CAN n bits de plage [0 ; Vref] ?", "a": "q = Vref / (2^n - 1). C'est la plus petite variation de tension analogique mesurable par le convertisseur."},
    {"module": "Électronique / IoT", "q": "Quelles sont les deux lignes utilisées par le bus I2C ?", "a": "SDA (Serial Data Line pour les données bidirectionnelles) et SCL (Serial Clock Line pour le signal d'horloge de synchronisation)."},
    {"module": "Modélisation UML/SysML", "q": "Quelle est la différence entre composition et agrégation en diagramme de classes ?", "a": "L'agrégation (losange vide) est une association faible (le composant survit sans le conteneur). La composition (losange plein) est une relation forte d'appartenance (la destruction du conteneur détruit le composant)."}
]

# --- QUESTIONS DU GRAND QUIZ D'EXAMEN (10 QUESTIONS TYPES) ---
GRAND_QUIZ_DATA = [
    {
        "q": "Q1 : Vous disposez du réseau 192.168.10.0/24. Vous devez créer 4 sous-réseaux de taille égale. Quel sera le nouveau masque ?",
        "options": ["255.255.255.128 (/25)", "255.255.255.192 (/26)", "255.255.255.224 (/27)", "255.255.255.240 (/28)"],
        "rep": "255.255.255.192 (/26)",
        "mod": "📶 Réseaux & Télécoms",
        "chap": "2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)",
        "expl": "Pour faire 4 sous-réseaux (2^2), il faut emprunter 2 bits au masque /24, ce qui donne un masque /26, soit 255.255.255.192."
    },
    {
        "q": "Q2 : Quelle commande Cisco IOS permet d'activer le trunking 802.1Q pour le VLAN 20 sur une sous-interface de routeur g0/0.20 ?",
        "options": ["switchport access vlan 20", "encapsulation dot1Q 20", "trunk allowed vlan 20", "ip route vlan 20"],
        "rep": "encapsulation dot1Q 20",
        "mod": "📶 Réseaux & Télécoms",
        "chap": "3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN",
        "expl": "Sur une sous-interface de routeur, l'encapsulation se configure avec 'encapsulation dot1Q <VLAN_ID>'."
    },
    {
        "q": "Q3 : En C++, comment appelle-t-on une classe possédant au moins une fonction membre déclarée virtuelle pure (= 0) ?",
        "options": ["Une classe scellée (final)", "Une classe générique", "Une classe de base abstraite", "Une interface statique"],
        "rep": "Une classe de base abstraite",
        "mod": "💻 Programmation / Dev",
        "chap": "1. Langage C++ : Mémoire, Pointeurs & POO",
        "expl": "Une classe avec une méthode virtuelle pure est une classe abstraite. Elle ne peut être instanciée directement."
    },
    {
        "q": "Q4 : Quel est l'effet de la commande Linux 'chmod 754 backup.sh' ?",
        "options": ["User: rwx, Group: r-x, Others: r--", "User: rwx, Group: rw-, Others: r-x", "User: r-x, Group: rwx, Others: ---", "User: rw-, Group: r--, Others: r--"],
        "rep": "User: rwx, Group: r-x, Others: r--",
        "mod": "🖥️ Administration Système",
        "chap": "1. Droits Linux & Commandes Système",
        "expl": "7 = 4+2+1 (rwx), 5 = 4+1 (r-x), 4 = 4 (r--)."
    },
    {
        "q": "Q5 : Un convertisseur CAN 10 bits alimenté en 0-5V reçoit une tension de 2,5V. Quelle est la valeur entière brute N générée ?",
        "options": ["256", "512", "1024", "128"],
        "rep": "512",
        "mod": "🔌 Électronique & IoT",
        "chap": "1. Échantillonnage, CAN/CNA & Théorème de Shannon",
        "expl": "Un CAN 10 bits génère des valeurs de 0 à 1023. Pour la demi-tension 2,5V, la valeur numérique vaut 512."
    },
    {
        "q": "Q6 : Quel protocole de sécurisation réseau fournit une authentification et un chiffrement au niveau de la Couche 3 (Réseau) ?",
        "options": ["TLS 1.3", "IPsec", "HTTPS", "WPA3"],
        "rep": "IPsec",
        "mod": "🔒 Cybersécurité",
        "chap": "3. Pare-feux, VPN & Sécurisation Système",
        "expl": "IPsec opère au niveau de la couche Réseau (Couche 3 du modèle OSI)."
    },
    {
        "q": "Q7 : Quel composant Active Directory applique de façon centralisée des stratégies de sécurité sur les postes d'un domaine ?",
        "options": ["GPO (Group Policy Object)", "Enregistrement DNS MX", "Base SAM locale", "Protocole SMB"],
        "rep": "GPO (Group Policy Object)",
        "mod": "🖥️ Administration Système",
        "chap": "2. Active Directory, Domaines & GPO",
        "expl": "Les GPO permettent d'administrer et de sécuriser de façon centralisée les environnements utilisateurs et postes."
    },
    {
        "q": "Q8 : Quel protocole IoT repose sur une architecture Publish/Subscribe avec un Broker central ?",
        "options": ["HTTP REST", "MQTT", "CoAP", "Modbus RTU"],
        "rep": "MQTT",
        "mod": "🔌 Électronique & IoT",
        "chap": "3. Protocoles Connectés : MQTT & LoRaWAN",
        "expl": "MQTT est un protocole de télémétrie léger fondé sur le modèle Publish/Subscribe et un courtier (Broker)."
    },
    {
        "q": "Q9 : Quelle relation UML est symbolisée par un losange plein (noir) du côté de la classe conteneur ?",
        "options": ["Héritage / Généralisation", "Agrégation", "Composition", "Dépendance"],
        "rep": "Composition",
        "mod": "📐 Modélisation UML & SysML",
        "chap": "1. Diagrammes UML Essentiels (Classes, Séquence, Use Case)",
        "expl": "La composition (losange noir) traduit une relation d'appartenance forte avec cycle de vie lié."
    },
    {
        "q": "Q10 : En SysML, quel diagramme permet de modéliser les flux internes (matière, énergie, données) entre les ports des blocs ?",
        "options": ["BDD (Block Definition Diagram)", "IBD (Internal Block Diagram)", "Requirement Diagram", "Use Case Diagram"],
        "rep": "IBD (Internal Block Diagram)",
        "mod": "📐 Modélisation UML & SysML",
        "chap": "2. Diagrammes SysML (BDD, IBD, Exigences)",
        "expl": "L'IBD (Internal Block Diagram) représente l'agencement interne et les flux reliant les ports d'un bloc."
    }
]

# --- INITIALISATION FICHIER SCORES ---
SCORES_FILE = "scores_history_v7.json"

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    today = datetime.now()
    default_hist = [
        {"date": (today - timedelta(days=21)).strftime("%Y-%m-%d %H:%M"), "score": 5, "total": 10, "details": {"Réseaux": 1, "Cybersécurité": 1, "Prog": 1, "SysAdmin": 1, "Elec": 1, "UML": 0}},
        {"date": (today - timedelta(days=14)).strftime("%Y-%m-%d %H:%M"), "score": 7, "total": 10, "details": {"Réseaux": 2, "Cybersécurité": 1, "Prog": 2, "SysAdmin": 1, "Elec": 1, "UML": 0}},
        {"date": (today - timedelta(days=7)).strftime("%Y-%m-%d %H:%M"), "score": 8, "total": 10, "details": {"Réseaux": 2, "Cybersécurité": 2, "Prog": 1, "SysAdmin": 1, "Elec": 1, "UML": 1}},
        {"date": (today - timedelta(days=2)).strftime("%Y-%m-%d %H:%M"), "score": 9, "total": 10, "details": {"Réseaux": 2, "Cybersécurité": 2, "Prog": 2, "SysAdmin": 1, "Elec": 1, "UML": 1}}
    ]
    with open(SCORES_FILE, 'w') as f:
        json.dump(default_hist, f)
    return default_hist

def save_score(score, total, details):
    history = load_scores()
    history.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "score": score,
        "total": total,
        "details": details
    })
    with open(SCORES_FILE, 'w') as f:
        json.dump(history, f)

# --- NAVIGATION SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/graduation-cap.png", width=75)
    st.markdown("### **BTS CIEL - Studio Pro**")
    st.caption("Cybersécurité, Informatique & Réseaux, Électronique")
    
    page = st.radio(
        "Navigation :",
        [
            "🏠 Accueil & Dashboard",
            "📚 Encyclopédie des Cours",
            "🧮 Laboratoire de Calculs (Subnetting & Élec)",
            "📐 Laboratoire UML & SysML",
            "🧪 Qualification & Tests E6",
            "🎯 Annales BTS (2024 & 2025)",
            "🗂️ Flashcards Actives",
            "🔍 Lab Décodeur Wireshark",
            "⚡ Sandboxes de Commandes",
            "📝 Grand Quiz d'Examen",
            "📈 Analyse des Scores",
            "📋 Planning de Projet E6 (Gantt)",
            "📹 Vidéos de Cours",
            "🌐 Répertoire des Liens"
        ]
    )
    st.markdown("---")
    st.success("⚡ **Statut** : Mode Entraînement Actif")

# --- 1. PAGE ACCUEIL ---
if page == "🏠 Accueil & Dashboard":
    st.markdown("""
    <div class='hero-container'>
        <div class='hero-title'>⚡ BTS CIEL - Studio d'Apprentissage v7</div>
        <div class='hero-subtitle'>Plateforme d'élite pour la réussite des épreuves E4, E5 et E6 du BTS Cybersécurité, Informatique et réseaux, Électronique</div>
        <div style='margin-top: 15px;'>
            <span class='badge badge-blue'>Option A : Informatique & Réseaux</span>
            <span class='badge badge-emerald'>Simulateur d'Examens</span>
            <span class='badge badge-purple'>UML & SysML Pro</span>
            <span class='badge badge-amber'>Conforme Annales 2024-2026</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='stat-box'><div class='stat-number'>6</div><div class='stat-label'>Modules d'Ingénierie</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stat-box'><div class='stat-number'>15+</div><div class='stat-label'>Chapitres de Cours Détaillés</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='stat-box'><div class='stat-number'>4</div><div class='stat-label'>Sandboxes Interactives</div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='stat-box'><div class='stat-number'>100%</div><div class='stat-label'>Génération Locale & Corrigée</div></div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div class='ciel-card'>
            <h3 style='color: #1e3a8a !important; margin-top:0; font-size: 1.3rem;'>🎯 Comment vous entraîner avec efficacité ?</h3>
            <p style='color: #1e293b !important; font-size: 1rem;'>Ce studio complet a été architecturé pour simuler fidèlement les exigences des épreuves nationales :</p>
            <ul style='color: #1e293b !important; line-height: 1.7;'>
                <li><b style='color: #0f172a !important;'>📚 Encyclopédie Enrichie</b> : Révisez les fiches de cours complètes et validez votre compréhension avec les <i style='color: #2563eb;'>Mini-Quiz intégrés</i> à la fin de chaque chapitre.</li>
                <li><b style='color: #0f172a !important;'>🧮 Lab de Calculs Dynamique</b> : Entraînez-vous à l'infini sur le découpage de masques <i style='color: #2563eb;'>VLSM IPv4</i>, le calcul de quantum <i style='color: #2563eb;'>CAN 10/12/16 bits</i> et les fréquences d'échantillonnage de <i style='color: #2563eb;'>Shannon</i>.</li>
                <li><b style='color: #0f172a !important;'>📐 Modélisation SysML & UML</b> : Décryptez des diagrammes réels (BDD, IBD, Séquence, Classes) et apprenez à traduire des modèles en code C++.</li>
                <li><b style='color: #0f172a !important;'>🧪 Qualification E6</b> : Rédigez et exécutez des tests d'intégration automatisés pour valider vos livrables de projet de fin d'études.</li>
                <li><b style='color: #0f172a !important;'>⚡ Sandboxes de Commandes</b> : Tapez directement vos lignes de configuration sous <i style='color: #2563eb;'>Cisco IOS</i>, vos commandes de droits <i style='color: #2563eb;'>Linux</i> et débugguez des fuites mémoire <i style='color: #2563eb;'>C++</i>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='ciel-card' style='border-left: 6px solid #10b981 !important;'>
            <h4 style='color: #065f46 !important; margin-top:0; font-size: 1.15rem;'>📋 Épreuves Couvertes :</h4>
            <p style='color: #1e293b !important; margin-bottom: 12px;'><b style='color: #0f172a !important;'>• E4 : Épreuve Technique Écrite</b><br>
            <span style='color: #475569 !important;'>Réseaux, Sécurité, C++, IoT & SysML</span></p>
            <p style='color: #1e293b !important; margin-bottom: 12px;'><b style='color: #0f172a !important;'>• E5 : Activités Professionnelles & TP</b><br>
            <span style='color: #475569 !important;'>Configurations Cisco, Linux, Wireshark</span></p>
            <p style='color: #1e293b !important; margin-bottom: 0;'><b style='color: #0f172a !important;'>• E6 : Projet de Fin d'Études</b><br>
            <span style='color: #475569 !important;'>Cahier des charges, UML, Dev, PVL & Gantt</span></p>
        </div>
        """, unsafe_allow_html=True)

# --- 2. PAGE ENCYCLOPÉDIE DES COURS ---
elif page == "📚 Encyclopédie des Cours":
    st.markdown("<div class='hero-title'>📚 Encyclopédie des Cours & Mini-Tests</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Cours théoriques exhaustifs, formules d'ingénierie et mini-évaluations interactives</p>", unsafe_allow_html=True)
    
    col_sel1, col_sel2 = st.columns([1, 1])
    with col_sel1:
        domaine = st.selectbox("Sélectionnez le Domaine d'Ingénierie :", list(COURS_BASE.keys()))
    with col_sel2:
        search_query = st.text_input("🔍 Rechercher un concept dans ce domaine :", placeholder="ex: Shannon, 802.1Q, pointeur, GPO...")
        
    chapitres = COURS_BASE[domaine]
    
    for chap_titre, chap_contenu in chapitres.items():
        if search_query.lower() in chap_titre.lower() or search_query.lower() in chap_contenu.lower():
            with st.expander(f"📖 {chap_titre}", expanded=True):
                st.markdown(chap_contenu)
                
                if chap_titre in MINI_QUIZ_COURS:
                    st.markdown("---")
                    mq = MINI_QUIZ_COURS[chap_titre]
                    st.markdown(f"**⚡ Mini-Test de Validation :** *{mq['q']}*")
                    choix_mq = st.radio("Votre réponse :", mq["options"], key=f"mq_{chap_titre}")
                    if st.button("Valider la réponse", key=f"btn_mq_{chap_titre}"):
                        if choix_mq == mq["rep"]:
                            st.success(f"🎉 **Exact !** {mq['expl']}")
                        else:
                            st.error(f"❌ **Incorrect.** Réponse attendue : **{mq['rep']}**.\n\n*Explication : {mq['expl']}*")

# --- 3. PAGE LABORATOIRE DE CALCULS ---
elif page == "🧮 Laboratoire de Calculs (Subnetting & Élec)":
    st.markdown("<div class='hero-title'>🧮 Laboratoire de Calculs Dynamiques</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Générateur infini d'exercices de calculs pour l'épreuve écrite E4</p>", unsafe_allow_html=True)
    
    tab_calc1, tab_calc2 = st.tabs(["🌐 Calculs de Sous-Réseaux (Subnetting IPv4)", "⚡ Calculs Électronique & CAN (Quantum)"])
    
    with tab_calc1:
        st.subheader("Générateur Infini de Découpage IPv4")
        if "subnet_ip" not in st.session_state:
            t_class = random.choice(["B", "C"])
            if t_class == "C":
                st.session_state.subnet_ip = f"192.168.{random.randint(1, 200)}.0"
                st.session_state.subnet_cidr = 24
                st.session_state.subnet_subnets = random.choice([2, 4, 8])
            else:
                st.session_state.subnet_ip = f"172.{random.randint(16, 31)}.{random.randint(1, 200)}.0"
                st.session_state.subnet_cidr = 16
                st.session_state.subnet_subnets = random.choice([4, 8, 16])
                
            bits_n = 0
            while (2**bits_n) < st.session_state.subnet_subnets:
                bits_n += 1
            new_c = st.session_state.subnet_cidr + bits_n
            st.session_state.sol_c = new_c
            st.session_state.sol_hosts = (2**(32 - new_c)) - 2
            
        ip_c = st.session_state.subnet_ip
        cidr_c = st.session_state.subnet_cidr
        subs_c = st.session_state.subnet_subnets
        
        st.info(f"📋 **Énoncé** : Soit l'adresse réseau **{ip_c}/{cidr_c}**. Découpez ce bloc en **{subs_c} sous-réseaux** de dimensions égales.")
        
        c_ans1, c_ans2 = st.columns(2)
        with c_ans1:
            u_cidr = st.number_input("Nouveau préfixe CIDR (ex: 26) :", min_value=1, max_value=32, value=24, key="u_cidr_in")
        with c_ans2:
            u_hosts = st.number_input("Nombre d'hôtes utiles par sous-réseau :", min_value=1, value=254, key="u_hosts_in")
            
        if st.button("Vérifier mes calculs Réseau", type="primary"):
            c_ok = (u_cidr == st.session_state.sol_c)
            h_ok = (u_hosts == st.session_state.sol_hosts)
            if c_ok and h_ok:
                st.balloons()
                st.success(f"🏆 **Parfait !** Nouveau masque : `/{st.session_state.sol_c}` | Hôtes utiles : `{st.session_state.sol_hosts}`.")
            else:
                if not c_ok:
                    st.error(f"❌ **Erreur CIDR** : Pour créer {subs_c} sous-réseaux, il faut emprunter {st.session_state.sol_c - cidr_c} bits. Le nouveau CIDR est `/{st.session_state.sol_c}`.")
                if not h_ok:
                    st.error(f"❌ **Erreur Hôtes** : Avec un `/{st.session_state.sol_c}`, la taille totale du bloc est de {2**(32-st.session_state.sol_c)} adresses. Moins 2 adresses réservées = {st.session_state.sol_hosts} hôtes utiles.")
                    
        if st.button("Générer un autre exercice Réseau"):
            for k in ["subnet_ip", "subnet_cidr", "subnet_subnets", "sol_c", "sol_hosts"]:
                if k in st.session_state: del st.session_state[k]
            st.rerun()
            
    with tab_calc2:
        st.subheader("Générateur de Calculs de Quantum & CAN (ADC)")
        if "adc_bits" not in st.session_state:
            st.session_state.adc_bits = random.choice([10, 12, 16])
            st.session_state.adc_vref = random.choice([3.3, 5.0])
            st.session_state.adc_ve = round(random.uniform(0.5, st.session_state.adc_vref - 0.2), 2)
            
            n_levels = (2**st.session_state.adc_bits) - 1
            q_val = st.session_state.adc_vref / n_levels
            st.session_state.adc_sol_n = round(st.session_state.adc_ve / q_val)
            st.session_state.adc_sol_q_mv = q_val * 1000.0
            
        bits = st.session_state.adc_bits
        vref = st.session_state.adc_vref
        ve = st.session_state.adc_ve
        
        st.info(f"📋 **Énoncé** : Un convertisseur analogique-numérique possède une résolution de **{bits} bits** et une tension de référence **Vref = {vref} V**. On applique en entrée une tension analogique **Ve = {ve} V**.")
        
        u_n = st.number_input("Entrez la valeur numérique entière N générée en sortie du CAN :", min_value=0, value=0, key="u_n_adc")
        
        if st.button("Vérifier le calcul CAN", type="primary"):
            if abs(u_n - st.session_state.adc_sol_n) <= 1:
                st.balloons()
                st.success(f"🏆 **Calcul exact !** N = **{st.session_state.adc_sol_n}** (Quantum q ≈ {st.session_state.adc_sol_q_mv:.3f} mV).")
            else:
                st.error(f"❌ **Valeur incorrecte.** N calculé = **{st.session_state.adc_sol_n}**.")
                st.markdown(f"""
                **Démonstration du calcul :**
                1. Quantum : $$q = \\frac{{V_{{ref}}}}{{2^n - 1}} = \\frac{{{vref}}}{{2^{{{bits}}} - 1}} = \\frac{{{vref}}}{{{(2**bits)-1}}} \\approx {st.session_state.adc_sol_q_mv/1000.0:.6f} \\text{{ V}}$$
                2. Valeur entière : $$N = \\text{{arrondi}}\\left(\\frac{{V_e}}{{q}}\\right) = \\text{{arrondi}}\\left(\\frac{{{ve}}}{{{st.session_state.adc_sol_q_mv/1000.0:.6f}}}\\right) = {st.session_state.adc_sol_n}$$
                """)
                
        if st.button("Générer un autre exercice CAN"):
            for k in ["adc_bits", "adc_vref", "adc_ve", "adc_sol_n", "adc_sol_q_mv"]:
                if k in st.session_state: del st.session_state[k]
            st.rerun()

# --- 4. PAGE LABORATOIRE UML & SYSML ---
elif page == "📐 Laboratoire UML & SysML":
    st.markdown("<div class='hero-title'>📐 Laboratoire Interactif UML & SysML</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Modélisation système d'ingénierie et cas pratiques d'examen</p>", unsafe_allow_html=True)
    
    tab_uml1, tab_uml2 = st.tabs(["🏗️ Modélisation SysML (BDD & IBD)", "📐 Modélisation UML (Classes & Séquence)"])
    
    with tab_uml1:
        st.subheader("Exemple Complet SysML : Station de Surveillance de la Qualité de l'Air")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown("#### Block Definition Diagram (BDD)")
            st.code("""
+-------------------------------------------------------------+
|             bdd [Système] StationSurveillance               |
+-------------------------------------------------------------+
|                                                             |
|   +-----------------------------------------------------+   |
|   |                       Station                       |   |
|   +-----------------------------------------------------+   |
|   | parts:                                              |   |
|   |  - cibleAcquisition : MicrocontroleurSTM32 [1]      |   |
|   |  - capteurCO2 : CapteurSondeNDIR [1]                |   |
|   |  - moduleCom : TransmetteurLoRa [1]                 |   |
|   |  - alimentation : BlocBatterieRegulee [1]           |   |
|   +-----------------------------------------------------+   |
|                              |                              |
|                  +-----------+-----------+                  |
|                  |                       |                  |
|                 1◆                      1◆                  |
|   +--------------------------+  +-----------------------+   |
|   |  MicrocontroleurSTM32    |  |    CapteurSondeNDIR   |   |
|   +--------------------------+  +-----------------------+   |
|   | - frequence : 84 MHz     |  | - plagePPM : 0..5000  |   |
|   | - memFlash : 512 Ko      |  | - interface : SPI     |   |
|   +--------------------------+  +-----------------------+   |
+-------------------------------------------------------------+
            """, language="text")
        with col_s2:
            st.markdown("#### Internal Block Diagram (IBD)")
            st.code("""
+-----------------------------------------------------------------+
|             ibd [Block] StationSurveillance                     |
+-----------------------------------------------------------------+
|                                                                 |
|  +--------------------+                   +------------------+  |
|  |  capteurCO2:       |                   |  cibleAcquis:    |  |
|  |  CapteurSondeNDIR  |                   |  STM32           |  |
|  |                    |                   |                  |  |
|  |           [p_spi]  |=== Bus SPI (4 fils) ===[p_spi]       |  |
|  |                    |   (MOSI, MISO,    |                  |  |
|  |                    |    SCLK, CS)      |                  |  |
|  |                    |                   |          [p_uart]|  |
|  +--------------------+                   +-------------||---+  |
|                                                         ||      |
|                                                Liaison Série TX |
|                                                         ||      |
|  +--------------------+                                 ||      |
|  |  moduleCom:        |                                 ||      |
|  |  TransmetteurLoRa  |                                 ||      |
|  |                    |                                 ||      |
|  |           [p_uart] |=================================++      |
|  +--------------------+                                         |
+-----------------------------------------------------------------+
            """, language="text")
            
        st.markdown("#### ✍️ Exercice d'Analyse SysML :")
        q_sysml = st.radio(
            "En observant l'IBD ci-dessus, quel bus physique assure le transfert des mesures brutes entre le capteur de CO2 et le microcontrôleur ?",
            ["Liaison série asynchrone UART", "Bus synchrone 4 fils SPI", "Bus I2C sur 2 fils", "Bus CAN différentiel"],
            key="q_sysml_radio"
        )
        if st.button("Valider l'analyse SysML"):
            if q_sysml == "Bus synchrone 4 fils SPI":
                st.success("✅ **Exact !** Le port `[p_spi]` relie le capteur au microcontrôleur via le bus SPI (MOSI, MISO, SCLK, CS).")
            else:
                st.error("❌ **Erreur.** Le diagramme indique explicitement un bus SPI à 4 fils.")
                
    with tab_uml2:
        st.subheader("Modélisation Logicielle UML")
        st.code("""
+------------------------------------+
|             Capteur                |
+------------------------------------+
| # refCapteur : string              |
| # tensionAlim : float              |
+------------------------------------+
| + Capteur(r : string)              |
| + virtual ~Capteur()               |
| + virtual lireConcentration() = 0  |  <--- Méthode virtuelle pure
+------------------------------------+
                  ^
                  |  Héritage (Généralisation)
                  |
+------------------------------------+
|           CapteurCO2SPI            |
+------------------------------------+
| - pinChipSelect : int              |
| - frequenceHorlogeHz : int         |
+------------------------------------+
| + CapteurCO2SPI(r:string, cs:int)  |
| + lireConcentration() : float      |  <--- Implémentation concrète
+------------------------------------+
        """, language="text")

# --- 5. PAGE TESTS D'INTÉGRATION E6 ---
elif page == "🧪 Qualification & Tests E6":
    st.markdown("<div class='hero-title'>🧪 Qualification Logicielle & Tests E6</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Méthodologie du Plan de Validation Logicielle (PVL) et assertions de tests automatisés</p>", unsafe_allow_html=True)
    
    st.write("""
    Dans l'épreuve **E6**, vous devez prouver la conformité de vos développements avec le cahier des charges initial au moyen d'un **Plan de Validation Logicielle (PVL)** rigoureux.
    """)
    
    st.markdown("### 💻 Exemple de Script de Test d'Intégration Réseau & BDD (Python / PyTest) :")
    st.code("""
import pytest
import json

def valider_payload_telemesure(payload_json_str):
    try:
        data = json.loads(payload_json_str)
        if "device_id" not in data or "co2_ppm" not in data:
            return False, "Champs obligatoires manquants"
        if not (0 <= data["co2_ppm"] <= 5000):
            return False, "Valeur CO2 hors plage valide [0-5000]"
        return True, "Payload conforme"
    except Exception as e:
        return False, str(e)

# --- CAS DE TEST D'INTÉGRATION ---
def test_integration_payload_nominal():
    payload_test = '{"device_id": "STATION_AIR_01", "co2_ppm": 420.5, "temp": 21.4}'
    valide, msg = valider_payload_telemesure(payload_test)
    assert valide is True
    assert msg == "Payload conforme"

def test_integration_payload_anomalie():
    payload_anormal = '{"device_id": "STATION_AIR_01", "co2_ppm": 99999.0}'
    valide, msg = valider_payload_telemesure(payload_anormal)
    assert valide is False
    assert "hors plage" in msg
    """, language="python")
    
    st.markdown("### ✍️ Testez vos réflexes d'Assurance Qualité :")
    st.write("Complétez l'assertion Python pour valider qu'un code de retour HTTP reçu d'un serveur Web vaut bien **200 (OK)** :")
    user_assert = st.text_input("Saisissez votre ligne d'assertion :", placeholder="assert reponse.status_code == 200", key="qa_assert")
    if st.button("Exécuter le Test d'Intégration"):
        if user_assert.strip().replace(" ", "") == "assertreponse.status_code==200":
            st.success("✅ **Test Validé !** L'assertion vérifie avec exactitude le code statut HTTP nominal.")
        else:
            st.info("💡 **Syntaxe attendue** : `assert reponse.status_code == 200`")

# --- 6. PAGE ANNALES BTS (2024 & 2025) ---
elif page == "🎯 Annales BTS (2024 & 2025)":
    st.markdown("<div class='hero-title'>🎯 Quiz & Cas Réels Annales BTS CIEL</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Questions d'examens officielles des sessions 2024 et 2025 décortiquées</p>", unsafe_allow_html=True)
    
    choix_a = st.selectbox("Sélectionnez l'Annale à étudier :", ["Session 2024 (Station de Surveillance de l'Air)", "Session 2025 (Borne de Recharge VE)"])
    
    if "2024" in choix_a:
        st.markdown("### 📕 Session 2024 : Station de Surveillance de la Qualité de l'Air")
        st.markdown("""
        **Mise en situation** : Une passerelle d'acquisition collecte les données de capteurs environnementaux et les publie sur un serveur sécurisé.
        """)
        
        q1_24 = st.radio(
            "1. Pour isoler les équipements d'acquisition sur un switch Cisco, on crée le sous-réseau 192.168.100.0/28. Combien d'adresses d'hôtes utilisables ce sous-réseau offre-t-il ?",
            ["14 hôtes", "16 hôtes", "30 hôtes", "6 hôtes"],
            key="q1_24_k"
        )
        if st.button("Valider la Q1 (2024)"):
            if q1_24 == "14 hôtes":
                st.success("✅ **Exact !** 32 - 28 = 4 bits d'hôte. 2^4 - 2 = 14 adresses utilisables.")
            else:
                st.error("❌ **Incorrect.** 2^(32-28) - 2 = 16 - 2 = 14 hôtes.")
                
        st.markdown("---")
        st.write("2. **Question de Code C++** : Quelle instruction permet de libérer le tableau alloué par `float* t = new float[100];` ?")
        c_24 = st.text_input("Instruction C++ :", placeholder="delete[] t;", key="c_24_in")
        if st.button("Valider la Q2 (2024)"):
            if c_24.strip().replace(" ", "") == "delete[]t;":
                st.success("✅ **Code conforme aux critères officiels d'examen !**")
            else:
                st.error("❌ **Erreur.** La commande exacte est `delete[] t;`.")
                
    else:
        st.markdown("### 📕 Session 2025 : Borne de Recharge de Véhicules Électriques")
        st.markdown("""
        **Mise en situation** : Une borne intelligente supervise la recharge de véhicules via une interface Linux connectée en réseau et surveille la tension secteur.
        """)
        q1_25 = st.radio(
            "1. Quel droit octal minimal doit-on attribuer à un script d'administration système pour qu'il soit exécutable par le propriétaire et le groupe sans être accessible aux autres utilisateurs ?",
            ["chmod 777", "chmod 750", "chmod 640", "chmod 700"],
            key="q1_25_k"
        )
        if st.button("Valider la Q1 (2025)"):
            if q1_25 == "chmod 750":
                st.success("✅ **Exact !** 7 (rwx) pour User, 5 (r-x) pour Group, 0 (aucun droit) pour Others.")
            else:
                st.error("❌ **Incorrect.** La réponse attendue est `chmod 750`.")

# --- 7. PAGE FLASHCARDS ACTIVES ---
elif page == "🗂️ Flashcards Actives":
    st.markdown("<div class='hero-title'>🗂️ Flashcards Actives</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Stimulez votre mémoire active en rédigeant votre réponse avant de vérifier la solution</p>", unsafe_allow_html=True)
    
    mods = ["Tous"] + list(set([f["module"] for f in FLASHCARDS_DATA]))
    sel_m = st.selectbox("Filtrer par module :", mods)
    f_list = FLASHCARDS_DATA if sel_m == "Tous" else [f for f in FLASHCARDS_DATA if f["module"] == sel_m]
    
    if "fc_idx" not in st.session_state: st.session_state.fc_idx = 0
    if st.session_state.fc_idx >= len(f_list): st.session_state.fc_idx = 0
    
    cur_fc = f_list[st.session_state.fc_idx]
    
    st.markdown(f"**Module :** `{cur_fc['module']}` | **Carte** `{st.session_state.fc_idx + 1} / {len(f_list)}`")
    
    st.markdown(f"""
    <div class='flashcard-box-modern'>
        <div class='flashcard-q-text'>{cur_fc['q']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    user_fc_ans = st.text_area("Rédigez votre réponse ici :", key=f"fc_txt_{st.session_state.fc_idx}")
    
    col_fc1, col_fc2, col_fc3 = st.columns(3)
    with col_fc1:
        if st.button("⬅️ Précédente", use_container_width=True):
            st.session_state.fc_idx = (st.session_state.fc_idx - 1) % len(f_list)
            st.rerun()
    with col_fc2:
        rev = st.checkbox("👁️ Afficher la correction", key=f"rev_{st.session_state.fc_idx}")
    with col_fc3:
        if st.button("Suivante ➡️", use_container_width=True):
            st.session_state.fc_idx = (st.session_state.fc_idx + 1) % len(f_list)
            st.rerun()
            
    if rev:
        st.markdown(f"""
        <div class='flashcard-a-box'>
            <b>💡 Réponse de l'expert :</b><br>
            {cur_fc['a']}
        </div>
        """, unsafe_allow_html=True)

# --- 8. PAGE LAB DÉCODEUR WIRESHARK ---
elif page == "🔍 Lab Décodeur Wireshark":
    st.markdown("<div class='hero-title'>🔍 Lab Décodeur Wireshark</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Apprenez à décoder les octets hexadécimaux bruts d'une capture réseau</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='terminal-header'>
        <span class='terminal-dot dot-red'></span>
        <span class='terminal-dot dot-yellow'></span>
        <span class='terminal-dot dot-green'></span>
        &nbsp; capture_reseau_brute_ipv4.hex (20 Octets En-tête IP)
    </div>
    <div class='terminal-body'>
    Octet n° : 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19<br>
    Données  : <b>45 00 00 3C 1C 2D 40 00 40 06 A8 B2 C0 A8 0A 05 C0 A8 0A 01</b>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Décryptage des champs du paquet :")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        ans_ver = st.selectbox("Version IP (Premier nibble '4') :", ["IPv4 (4)", "IPv6 (6)"])
        ans_ihl = st.number_input("Longueur de l'en-tête (IHL) en mots de 32 bits (Deuxième nibble '5') :", min_value=0, max_value=15, value=0)
        ans_ttl = st.number_input("TTL décimal (Octet 8 : hex '40') :", min_value=0, max_value=255, value=0)
    with col_w2:
        ans_proto = st.selectbox("Protocole encapsulé (Octet 9 : hex '06') :", ["ICMP (1)", "TCP (6)", "UDP (17)"])
        ans_src = st.text_input("IP Source décodée (Octets 12-15 : 'C0 A8 0A 05') :", placeholder="ex: 192.168.10.5")
        ans_dst = st.text_input("IP Destination décodée (Octets 16-19 : 'C0 A8 0A 01') :", placeholder="ex: 192.168.10.1")
        
    if st.button("Valider l'analyse de trame", type="primary"):
        ok = (ans_ver == "IPv4 (4)" and ans_ihl == 5 and ans_ttl == 64 and ans_proto == "TCP (6)" and ans_src.strip() == "192.168.10.5" and ans_dst.strip() == "192.168.10.1")
        if ok:
            st.balloons()
            st.success("🏆 **Décodage parfait ! Vous maîtrisez l'anatomie de l'en-tête IPv4.**")
        else:
            st.error("❌ **Certains champs sont incorrects.**")
            st.info("💡 **Aide** : C0 = 192, A8 = 168, 0A = 10, 05 = 5 $\\rightarrow$ `192.168.10.5` | TTL 0x40 = 64 en décimal.")

# --- 9. PAGE SANDBOXES DE COMMANDES ---
elif page == "⚡ Sandboxes de Commandes":
    st.markdown("<div class='hero-title'>⚡ Sandboxes & Terminaux Pratiques</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Exercez-vous à la saisie de commandes réelles d'examen sans danger</p>", unsafe_allow_html=True)
    
    t1, t2, t3 = st.tabs(["📶 Cisco IOS Switch Terminal", "🖥️ Linux Bash Permission Console", "💻 C++ Memory Debugger"])
    
    with t1:
        st.markdown("**Scénario** : Configurez le port `FastEthernet0/5` en mode accès sur le **VLAN 30**.")
        st.markdown("<div class='terminal-header'>Switch-BTS-CIEL(config-if)#</div>", unsafe_allow_html=True)
        c_cisco = st.text_input("Commande Cisco :", placeholder="switchport access vlan 30", key="sb_cisco")
        if st.button("Exécuter sur l'IOS"):
            if c_cisco.strip().lower() == "switchport access vlan 30":
                st.success("✅ **Commande validée !** Le port est correctement assigné au VLAN 30.")
            else:
                st.error("❌ Commande rejetée par l'interpréteur Cisco IOS.")
                st.info("💡 Commande normalisée : `switchport access vlan 30`")
                
    with t2:
        st.markdown("**Scénario** : Sécurisez le fichier `deploy.sh` : Propriétaire = Tous droits (rwx), Groupe = Lecture/Exécution (rx), Autres = Aucun.")
        st.markdown("<div class='terminal-header'>root@debian-srv:~#</div>", unsafe_allow_html=True)
        c_bash = st.text_input("Commande Bash :", placeholder="chmod 750 deploy.sh", key="sb_bash")
        if st.button("Exécuter le chmod"):
            if c_bash.strip() in ["chmod 750 deploy.sh", "chmod 750 ./deploy.sh"]:
                st.success("✅ **Permissions appliquées avec succès !** (Masque octal 750).")
            else:
                st.error("❌ Permissions incorrectes.")
                st.info("💡 Commande attendue : `chmod 750 deploy.sh`")
                
    with t3:
        st.markdown("**Scénario** : Corrigez la fuite de mémoire dans ce code C++ :")
        st.code("""
int* buffer = new int[256];
// ... utilisation du buffer ...
delete buffer; // <-- FUITE MÉMOIRE !
        """, language="cpp")
        c_cpp = st.text_input("Ligne corrigée :", placeholder="delete[] buffer;", key="sb_cpp")
        if st.button("Vérifier la correction C++"):
            if c_cpp.strip().replace(" ", "") == "delete[]buffer;":
                st.success("✅ **Fuite mémoire colmatée avec succès !**")
            else:
                st.error("❌ Erreur de syntaxe.")
                st.info("💡 Syntaxe correcte : `delete[] buffer;`")

# --- 10. PAGE GRAND QUIZ D'EXAMEN ---
elif page == "📝 Grand Quiz d'Examen":
    st.markdown("<div class='hero-title'>📝 Grand Quiz d'Examen de Synthèse</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Évaluez votre niveau global sur 10 questions de synthèse représentatives</p>", unsafe_allow_html=True)
    
    scores = {}
    for i, ex in enumerate(GRAND_QUIZ_DATA):
        st.markdown(f"### {ex['q']}")
        chx = st.radio(f"Sélectionnez votre réponse :", ex['options'], key=f"gq_{i}")
        scores[i] = (chx, ex['rep'], ex['expl'], ex['mod'], ex['chap'])
        st.markdown("---")
        
    if st.button("Soumettre mon Examen de Synthèse", type="primary", use_container_width=True):
        total_ok = 0
        wrong = []
        details = {"Réseaux": 0, "Cybersécurité": 0, "Prog": 0, "SysAdmin": 0, "Elec": 0, "UML": 0}
        
        for i, (chx, rep, expl, m_ref, c_ref) in scores.items():
            k_mod = "Réseaux"
            if "Cyber" in m_ref: k_mod = "Cybersécurité"
            elif "Prog" in m_ref: k_mod = "Prog"
            elif "SysAdmin" in m_ref: k_mod = "SysAdmin"
            elif "Élec" in m_ref: k_mod = "Elec"
            elif "Modélisation" in m_ref: k_mod = "UML"
            
            if chx == rep:
                total_ok += 1
                details[k_mod] += 1
            else:
                wrong.append({"num": i+1, "mod": m_ref, "chap": c_ref, "chx": chx, "rep": rep, "expl": expl})
                
        save_score(total_ok, len(GRAND_QUIZ_DATA), details)
        
        st.markdown("## 📊 Votre Bilan d'Examen")
        pct = total_ok / len(GRAND_QUIZ_DATA)
        st.progress(pct)
        
        if total_ok >= 8:
            st.success(f"🏆 **Excellente performance ! Score : {total_ok} / {len(GRAND_QUIZ_DATA)}**. Vos connaissances sont solides !")
        elif total_ok >= 5:
            st.info(f"👍 **Résultat honorable ! Score : {total_ok} / {len(GRAND_QUIZ_DATA)}**. Continuez à travailler vos points faibles.")
        else:
            st.warning(f"⚠️ **Score : {total_ok} / {len(GRAND_QUIZ_DATA)}**. Révisez les cours ciblés ci-dessous.")
            
        if wrong:
            st.markdown("---")
            st.markdown("### 🔄 Pont de Correction Automatique")
            for w in wrong:
                st.error(f"**Question {w['num']} ({w['mod']} - {w['chap']})**")
                st.write(f"Votre choix : *{w['chx']}* | Bonne réponse : **{w['rep']}**")
                st.info(f"💡 *Explication : {w['expl']}*")
                try:
                    c_txt = COURS_BASE[w['mod']][w['chap']]
                    with st.expander(f"📖 Fiche de Révision : {w['chap']}", expanded=True):
                        st.markdown(c_txt)
                except:
                    pass

# --- 11. PAGE ANALYSE DES SCORES ---
elif page == "📈 Analyse des Scores":
    st.markdown("<div class='hero-title'>📈 Tableau de Bord & Analyse des Scores</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Suivez votre progression dans le temps et vos compétences par domaine</p>", unsafe_allow_html=True)
    
    hist = load_scores()
    if hist:
        df = pd.DataFrame(hist)
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.metric("Tentatives totales", len(df))
        with c2: st.metric("Moyenne générale", f"{(df['score']/df['total']).mean()*100:.1f} %")
        with c3: st.metric("Meilleur score", f"{df['score'].max()} / 10")
        with c4: st.metric("Dernier score", f"{df['score'].iloc[-1]} / 10")
        
        st.markdown("### 📈 Évolution des Notes au Fil des Jours")
        df_plot = df[["date", "score"]].copy().set_index("date")
        st.line_chart(df_plot)
        
        totals = {"Réseaux": 0, "Cybersécurité": 0, "Prog": 0, "SysAdmin": 0, "Elec": 0, "UML": 0}
        for h in hist:
            for k, v in h.get("details", {}).items():
                if k in totals: totals[k] += v
                
        max_pts = len(hist) * 2
        rates = {k: (v / max_pts)*100 if max_pts > 0 else 0 for k, v in totals.items()}
        
        df_b = pd.DataFrame({"Compétence": list(rates.keys()), "Taux d'Acquisition (%)": list(rates.values())}).set_index("Compétence")
        st.markdown("### 📊 Taux de Maîtrise par Compétence")
        st.bar_chart(df_b)
        
        weak = min(rates, key=rates.get)
        st.markdown(f"### 🎓 Conseil Pédagogique : Priorité **{weak}**")
        st.info(f"Votre compétence nécessitant le plus de consolidation est **{weak}** ({rates[weak]:.1f}%). Révisez les chapitres dédiés dans l'Encyclopédie et pratiquez les flashcards associées !")
        
        if st.button("Réinitialiser l'historique"):
            if os.path.exists(SCORES_FILE): os.remove(SCORES_FILE)
            st.rerun()

# --- 12. PAGE PLANNING DE PROJET E6 (GANTT) ---
elif page == "📋 Planning de Projet E6 (Gantt)":
    st.markdown("<div class='hero-title'>📋 Planning de Projet E6 & Diagramme de Gantt</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Gérez vos jalons de projet et générez votre planning pour votre soutenance finale</p>", unsafe_allow_html=True)
    
    PROJ_FILE = "e6_tasks_v7.json"
    if os.path.exists(PROJ_FILE):
        try:
            with open(PROJ_FILE, "r") as f: t_data = json.load(f)
        except: t_data = []
    else:
        td = datetime.now().date()
        t_data = [
            {"nom": "1. Cahier des charges & CdCf", "debut": (td - timedelta(days=25)).strftime("%Y-%m-%d"), "fin": (td - timedelta(days=15)).strftime("%Y-%m-%d"), "avancement": 100, "resp": "Équipe"},
            {"nom": "2. Modélisation SysML & UML", "debut": (td - timedelta(days=15)).strftime("%Y-%m-%d"), "fin": (td - timedelta(days=5)).strftime("%Y-%m-%d"), "avancement": 100, "resp": "Étudiant A"},
            {"nom": "3. Développement C++ & Pilotes SPI", "debut": (td - timedelta(days=5)).strftime("%Y-%m-%d"), "fin": (td + timedelta(days=10)).strftime("%Y-%m-%d"), "avancement": 60, "resp": "Étudiant A"},
            {"nom": "4. Passerelle Python & Base de Données", "debut": (td).strftime("%Y-%m-%d"), "fin": (td + timedelta(days=15)).strftime("%Y-%m-%d"), "avancement": 30, "resp": "Étudiant B"},
            {"nom": "5. Sécurisation TLS & Durcissement Linux", "debut": (td + timedelta(days=10)).strftime("%Y-%m-%d"), "fin": (td + timedelta(days=22)).strftime("%Y-%m-%d"), "avancement": 0, "resp": "Étudiant B"},
            {"nom": "6. Plan de Validation Logicielle (PVL)", "debut": (td + timedelta(days=20)).strftime("%Y-%m-%d"), "fin": (td + timedelta(days=30)).strftime("%Y-%m-%d"), "avancement": 0, "resp": "Équipe"}
        ]
        with open(PROJ_FILE, "w") as f: json.dump(t_data, f)
        
    c_g1, c_g2 = st.columns([1, 2])
    with c_g1:
        st.subheader("Ajouter une tâche de projet :")
        with st.form("f_t"):
            t_nom = st.text_input("Nom de la tâche :", "7. Dossier d'examen et soutenance")
            t_deb = st.date_input("Date de début :", datetime.now().date())
            t_fin = st.date_input("Date de fin :", datetime.now().date() + timedelta(days=12))
            t_pct = st.slider("Avancement (%) :", 0, 100, 0)
            t_r = st.text_input("Responsable :", "Mon Nom")
            if st.form_submit_button("Ajouter au planning"):
                t_data.append({"nom": t_nom, "debut": t_deb.strftime("%Y-%m-%d"), "fin": t_fin.strftime("%Y-%m-%d"), "avancement": t_pct, "resp": t_r})
                with open(PROJ_FILE, "w") as f: json.dump(t_data, f)
                st.rerun()
    with c_g2:
        st.subheader("Planning de Gantt Dynamique")
        if t_data:
            fig, ax = plt.subplots(figsize=(9, 4.5))
            y_pos = []
            y_labels = []
            for i, tk in enumerate(reversed(t_data)):
                s_d = datetime.strptime(tk["debut"], "%Y-%m-%d")
                e_d = datetime.strptime(tk["fin"], "%Y-%m-%d")
                dur = (e_d - s_d).days
                pct_v = tk["avancement"]
                ax.barh(i, dur, left=s_d, color="#e2e8f0", edgecolor="#94a3b8", height=0.5)
                bar_c = "#10b981" if pct_v == 100 else "#3b82f6"
                ax.barh(i, dur * (pct_v / 100.0), left=s_d, color=bar_c, height=0.5)
                y_pos.append(i)
                y_labels.append(f"{tk['nom']}\\n({tk['resp']} - {pct_v}%)")
            ax.set_yticks(y_pos)
            ax.set_yticklabels(y_labels, fontsize=8)
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
            plt.title("Planning de Gantt du Projet E6", fontsize=12, fontweight="bold", color="#1e3a8a")
            plt.grid(axis='x', linestyle='--', alpha=0.5)
            plt.tight_layout()
            g_path = "/workspace/scratch/gantt_chart_v7.png"
            plt.savefig(g_path, dpi=150)
            plt.close()
            st.image(g_path)

# --- 13. PAGE VIDÉOS DE COURS ---
elif page == "📹 Vidéos de Cours":
    st.markdown("<div class='hero-title'>📹 Vidéothèque Pédagogique</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Vidéos de cours recommandées par les professeurs de BTS CIEL</p>", unsafe_allow_html=True)
    
    VIDEOS_LIST = {
        "Julien Code (C++ & Programmation BTS)": [
            {"titre": "Débutez en C++ - Les bases du langage", "id": "6m8gS-iXmXQ"},
            {"titre": "Comprendre les pointeurs en C++", "id": "S1yR7_7bWRE"}
        ],
        "IT-Connect & Cocadmin (Réseaux & Active Directory)": [
            {"titre": "Comprendre et configurer un VLAN", "id": "06Y6qYg9_C0"},
            {"titre": "Active Directory de A à Z - Tutoriel Complet", "id": "rQ_1n8Y0o-0"}
        ],
        "Stéphane Michelet (Physique & Signal)": [
            {"titre": "Traitement du Signal : Échantillonnage & Shannon", "id": "3Z8oE-pCq00"},
            {"titre": "La Modulation de Largeur d'Impulsion (PWM/MLI)", "id": "4jS0qUfE_y4"}
        ]
    }
    
    canal = st.selectbox("Sélectionnez une thématique vidéo :", list(VIDEOS_LIST.keys()))
    for v in VIDEOS_LIST[canal]:
        col_v1, col_v2 = st.columns([1, 1])
        with col_v1:
            st.subheader(v["titre"])
            st.markdown(f"[Ouvrir directement sur YouTube ↗️](https://www.youtube.com/watch?v={v['id']})")
        with col_v2:
            st.video(f"https://www.youtube.com/watch?v={v['id']}")
        st.markdown("---")

# --- 14. PAGE RÉPERTOIRE DES LIENS ---
elif page == "🌐 Répertoire des Liens":
    st.markdown("<div class='hero-title'>🌐 Répertoire des Ressources Essentielles</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Les sites de référence incontournables pour réussir votre BTS CIEL</p>", unsafe_allow_html=True)
    
    LIENS = {
        "Cours Magistraux & Fiches": [
            ("Le site de Thierry Vaira", "http://tvaira.free.fr/", "La bible de référence du BTS informatique et réseaux."),
            ("Cours BTS CIEL", "https://coursbtsciel.fr/", "Fiches synthétiques de cours et résumés."),
            ("IT-Connect", "https://www.it-connect.fr/", "Tutoriels professionnels SysAdmin, Linux et Réseaux.")
        ],
        "MOOCs & Formations": [
            ("Cisco Networking Academy", "https://www.netacad.com/", "Cours officiels de préparation aux certifications Cisco."),
            ("OpenClassrooms - Réseaux TCP/IP", "https://openclassrooms.com/fr/courses/857447-apprenez-le-fonctionnement-des-reseaux-tcp-ip", "Fondations des réseaux."),
            ("OpenClassrooms - Programmation C++", "https://openclassrooms.com/fr/courses/1894236-programmez-avec-le-langage-c", "Maîtrise de la POO en C++.")
        ],
        "Entraînement Pratique & Cyber": [
            ("Root-Me", "https://www.root-me.org/", "Plateforme d'entraînement au hacking éthique."),
            ("TryHackMe", "https://tryhackme.com/", "Salles guidées de cybersécurité."),
            ("France-IOI", "http://france-ioi.org/", "Entraînement algorithmique.")
        ]
    }
    
    for cat, items in LIENS.items():
        st.markdown(f"### 📂 {cat}")
        for nom, url, desc in items:
            col_l1, col_l2 = st.columns([1, 3])
            with col_l1:
                st.markdown(f"**[{nom}]({url})**")
            with col_l2:
                st.write(desc)
        st.markdown("---")
