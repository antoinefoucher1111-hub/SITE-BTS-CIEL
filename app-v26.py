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
st.markdown(r"""
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
r""", unsafe_allow_html=True)

# --- BASE DE DONNÉES ENCYCLOPÉDIQUE ÉTENDUE ---
COURS_BASE = {
    '📶 Réseaux & Télécoms': {
        '1. Modèle OSI vs TCP/IP & Encapsulation': r"""### 🌐 Architecture des Protocoles en Réseau
Le **modèle OSI (Open Systems Interconnection)** découpe la communication en 7 couches standardisées :
* **7. Application (PDU: Donnée)** : Protocoles applicatifs de haut niveau (HTTP, HTTPS, DNS, DHCP, SSH, MQTT, SNMP, SMTP).
* **6. Présentation** : Formatage des données, chiffrement (TLS/SSL) et compression (ASCII, UTF-8, JPEG).
* **5. Session** : Gestion et synchronisation des sessions d'échanges (NetBIOS, RPC, Sockets).
* **4. Transport (PDU: Segment / Datagramme)** : Communication de bout en bout et contrôle de flux. **TCP** (orienté connexion, fiable avec accusé de réception ACK et fenêtre glissante) vs **UDP** (sans connexion, rapide, sans garantie d'arrivée, idéal streaming/VoIP/DNS).
* **3. Réseau (PDU: Paquet)** : Routage logique et adressage mondial (IPv4, IPv6, ICMP, IPsec, protocoles OSPF/BGP). Equipement : **Routeur**.
* **2. Liaison de données (PDU: Trame)** : Adressage physique (adresses MAC 48 bits), détection d'erreurs (FCS/CRC32), protocoles Ethernet (802.3), Wi-Fi (802.11). Equipement : **Commutateur (Switch)**.
* **1. Physique (PDU: Bit)** : Transmission des signaux électriques, optiques ou électromagnétiques (RJ45, fibre optique, radio).

**Modèle TCP/IP (4 couches)** : Application, Transport, Internet, Accès Réseau.r""",

        '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)': r"""### 🧮 Méthodologie du Calcul de Masque & Subnetting
Une adresse **IPv4** fait 32 bits (4 octets). Elle est scindée en **Partie Réseau (NetID)** et **Partie Hôte (HostID)** via le masque de sous-réseau.

#### Règles Fondamentales :
* **Nombre total d'adresses dans un bloc** = $2^{(32 - \text{CIDR})}$
* **Nombre d'adresses d'hôtes utilisables** = $2^{(32 - \text{CIDR})} - 2$ (on soustrait l'adresse Réseau où tous les bits d'hôte sont à 0, et l'adresse de Broadcast où tous les bits d'hôte sont à 1).
* **Calcul d'adresse Réseau** = Opération logique `ET (AND)` bit-à-bit entre l'IP et le Masque.
* **Calcul du Broadcast** = Adresse Réseau + $(2^{(32 - \text{CIDR})} - 1)$.

#### Table Rapide des Masques Fréquents :
* `/24` $\rightarrow$ `255.255.255.0` (256 adresses, 254 hôtes)
* `/25` $\rightarrow$ `255.255.255.128` (128 adresses, 126 hôtes)
* `/26` $\rightarrow$ `255.255.255.192` (64 adresses, 62 hôtes)
* `/27` $\rightarrow$ `255.255.255.224` (32 adresses, 30 hôtes)
* `/28` $\rightarrow$ `255.255.255.240` (16 adresses, 14 hôtes)
* `/29` $\rightarrow$ `255.255.255.248` (8 adresses, 6 hôtes)
* `/30` $\rightarrow$ `255.255.255.252` (4 adresses, 2 hôtes - Liens point-à-point)

#### Notions IPv6 (128 bits) :
* Notation en 8 groupes de 4 caractères hexadécimaux séparés par des `:`.
* Règle de compression : omission des zéros en tête (`0db8` $\rightarrow$ `db8`) et remplacement d'une suite continue de groupes de zéros par `::` (une seule fois par adresse).r""",

        '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN': r"""### 🔀 Segmentation & Routage Virtuel
Un **VLAN (Virtual LAN)** isole logiquement les domaines de diffusion au sein d'un même commutateur physique.

#### Modes de Ports Switch :
* **Port Access** : Appartient à un seul VLAN. Les trames y circulent détaguées (standard Ethernet 802.3).
* **Port Trunk** : Fait transiter plusieurs VLANs simultanément entre switchs ou vers un routeur. Utilise la norme **IEEE 802.1Q** qui insère un tag de **4 octets** dans l'en-tête Ethernet (incluant le VID sur 12 bits, soit 4096 VLANs possibles).

#### Routage Inter-VLAN (Router-on-a-Stick) :
Sur le routeur, une seule interface physique (ex: `g0/0/0`) est découpée en sous-interfaces logiques (`g0/0/0.10`, `g0/0/0.20`) avec la commande `encapsulation dot1Q <ID>`.r""",

        "4. Services d'Infrastructure : DHCP, DNS, NAT/PAT": r"""### ⚙️ Services Réseaux Indispensables
* **DHCP (Dynamic Host Configuration Protocol)** : Attribution dynamique de configuration IP. Processus **DORA** :
  1. `Discover` (Client $\rightarrow$ 255.255.255.255 en UDP 67/68)
  2. `Offer` (Serveur $\rightarrow$ Client)
  3. `Request` (Client $\rightarrow$ Serveur)
  4. `Acknowledge` (Serveur valide le bail IP)
* **DNS (Domain Name System)** : Résolution de noms d'hôtes. Types d'enregistrements : `A` (IPv4), `AAAA` (IPv6), `CNAME` (Alias), `MX` (Serveur mail), `PTR` (Résolution inverse).
* **NAT / PAT (Port Address Translation)** : Translation d'adresses privées (RFC 1918) vers une adresse publique unique en multiplexant les numéros de ports source TCP/UDP.r""",

        '5. Protocoles Industriels & Bus de terrain (Modbus, Profibus)': r"""### 🏭 Protocoles Industriels & Bus de terrain (Modbus, Profibus)
Dans l'option A du BTS CIEL, l'étude des réseaux industriels est incontournable. Le protocole **Modbus RTU** (communiquant généralement sur une liaison physique **RS-485**) est un modèle de communication de type maître-esclave.

#### Caractéristiques de Modbus RTU :
* **Format des trames** : Composé de l'Adresse de l'esclave (1 octet), du Code Fonction (1 octet), des Données (variable) et du contrôle d'erreur CRC-16 (2 octets).
* **Fonctions de lecture/écriture de registres de base** :
  * `01` : Read Coils (Sorties binaires)
  * `02` : Read Discrete Inputs (Entrées binaires)
  * `03` : Read Holding Registers (Sorties analogiques en lecture/écriture, de taille 16 bits par registre)
  * `04` : Read Input Registers (Entrées analogiques en lecture seule)
  * `05` : Write Single Coil (Écriture d'une seule sortie binaire)
  * `06` : Write Single Register (Écriture d'un seul registre analogique 16 bits)r""",

        '6. Transmission optique (Fibres optiques Monomodes & Multimodes)': r"""### ⚡ Transmission optique (Fibres optiques Monomodes & Multimodes)
La fibre optique utilise le principe de réflexion totale interne pour propager des impulsions lumineuses.

#### Fibre Monomode (Single-mode) :
* **Structure** : Cœur extrêmement étroit (environ 9 micromètres), gaine de 125 micromètres.
* **Propagation** : Un seul chemin rectiligne de la lumière (un seul mode).
* **Source** : Diode Laser de forte puissance.
* **Performance** : Absence quasi-totale de dispersion modale, portée kilométrique très longue distance, idéale pour les réseaux d'interconnexion WAN.

#### Fibre Multimode (Multi-mode) :
* **Structure** : Cœur plus large (50 ou 62,5 micromètres).
* **Propagation** : Plusieurs modes de propagation par rebonds (dispersion modale importante provoquant un étalement des impulsions dans le temps).
* **Source** : LED ou VCSEL.
* **Performance** : Portée réduite (courte distance comme les LANs d'entreprises ou Data Centers).r""",

    },
    '🔒 Cybersécurité': {
        '1. Cryptographie : Symétrique, Asymétrique & Hachage': r"""### 🛡️ Les Fondements Cryptographiques
La sécurité repose sur la triade **CIA** (Confidentialité, Intégrité, Disponibilité) + Authenticité et Non-répudiation.

* **Chiffrement Symétrique** : Même clé secrète pour chiffrer et déchiffrer. Rapide, adapté aux flux volumineux. Standard : **AES-128 / AES-256** (modes CBC, GCM avec authentification intégrée).
* **Chiffrement Asymétrique** : Paire de clés mathématiquement liées (Clé Publique distribuable, Clé Privée secrète). Algorithmes : **RSA (2048/4096 bits)**, **ECC (Courbes Elliptiques)**. Utilisé pour l'échange de clés de session et les signatures numériques.
* **Fonctions de Hachage** : Condensat à sens unique de taille fixe. Vérifie l'intégrité stricte. Algorithmes : **SHA-256**, **SHA-3** (MD5 et SHA-1 sont aujourd'hui vulnérables aux collisions).
* **Certificats X.509 & PKI** : Une Autorité de Certification (CA) signe la clé publique d'un serveur pour attester de son identité.r""",

        '2. Top 10 OWASP & Sécurité Applicative': r"""### 🚨 Vulnérabilités Web et Remédiations
* **Injections SQL** : L'attaquant injecte du code SQL non filtré pour manipuler la BDD.
  * *Exemple vulnérable* : `query = "SELECT * FROM users WHERE user='" + input + "'"`
  * *Remédiation absolue* : Utiliser exclusivement des **requêtes préparées (paramétrées)** via PDO en PHP ou `cursor.execute("SELECT * FROM users WHERE user=%s", (input,))` en Python.
* **Cross-Site Scripting (XSS)** : Injection de scripts JavaScript malveillants exécutés par les navigateurs clients.
  * *Remédiation* : Échappement des caractères HTML (`htmlspecialchars()`), CSP (Content Security Policy).
* **CSRF (Cross-Site Request Forgery)** : Forcer un utilisateur authentifié à exécuter des actions non désirées. *Remédiation* : Jetons (tokens) anti-CSRF aléatoires et synchronisés.r""",

        '3. Pare-feux, VPN & Sécurisation Système': r"""### 🧱 Défense Périmétrique et Durcissement
* **Pare-feu Stateful** : Analyse l'état des connexions (table d'états TCP). Sous Linux : `iptables` / `nftables` ou `ufw`.
* **VPN (Virtual Private Network)** :
  * **IPsec** : Opère en couche 3. Protocoles `AH` (Intégrité/Authentification) et `ESP` (Chiffrement + Intégrité). Modes : Transport (hôte à hôte) ou Tunnel (site à site).
  * **OpenVPN / WireGuard** : VPN applicatif et niveau kernel moderne utilisant TLS/chiffrement moderne.
* **Port Security Cisco** : Limite le nombre d'adresses MAC autorisées par port de switch pour contrer le MAC Flooding (`switchport port-security maximum 1`, `switchport port-security violation shutdown`).r""",

        '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)': r"""### 🛡️ Protocoles Sécurisés : Chiffrement & Authentification
* **VPN (Virtual Private Network)** : Crée un tunnel sécurisé à travers un réseau non sécurisé (Internet).
  * **IPsec** : Opère en couche 3 (Réseau) pour chiffrer l'intégralité du trafic IP d'un site à un autre (VPN Site-à-Site).
  * **OpenVPN / WireGuard** : Utilise le protocole SSL/TLS ou des mécanismes cryptographiques modernes (Noise protocol) de couche Transport pour les connexions clients d'accès à distance.
* **HTTPS** : Sécurisation du protocole HTTP par l'utilisation d'une couche TLS. Lors du **TLS Handshake** (poignée de main TLS), le client et le serveur s'accordent sur les algorithmes (Cipher Suite), s'authentifient via des certificats X.509 et génèrent une clé symétrique de session temporaire.
* **MQTTS** : Variante sécurisée de MQTT qui utilise TLS (Port par défaut 8883) pour chiffrer les flux d'objets connectés et authentifier les clients de manière robuste.r""",

    },
    '💻 Programmation / Dev': {
        '1. Langage C++ : Mémoire, Pointeurs & POO': r"""### ⚡ Maîtrise Bas Niveau & Orientée Objet en C++
Le C++ est au cœur du BTS CIEL pour la programmation système et microcontrôleurs embarqués.

#### Gestion de la Mémoire :
* **Pile (Stack)** : Gestion automatique, rapide, portée limitée au bloc `{}`.
* **Tas (Heap)** : Allocation manuelle dynamique avec `new` / `new[]`. Doit obligatoirement être libérée avec `delete` / `delete[]` pour éviter les **fuites de mémoire (Memory Leaks)**.
* **Pointeurs & Références** :
  * `int x = 42; int* p = &x;` $\rightarrow$ `p` contient l'adresse, `*p` accède à la valeur.
  * `void modifier(int& ref)` $\rightarrow$ passage par référence (sans copie mémoire).

#### Programmation Orientée Objet (POO) :
* **Encapsulation** : Données membres `private` accessibles via `getters`/`setters` `public`.
* **Héritage** : `class CapteurTemperature : public Capteur`.
* **Polymorphisme & Classes Abstraites** : Méthode déclarée `virtual void mesurer() = 0;` (méthode virtuelle pure). La classe devient abstraite et impose l'implémentation dans les classes dérivées.r""",

        '2. Python Réseau, Systèmes & Sockets': r"""### 🐍 Automatisation & Sockets Réseau en Python
Python est l'outil privilégié pour les scripts de passerelle, de traitement de données IoT et d'administration système.

#### Client TCP Sockets :
```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.1.50', 8080))
    s.sendall(b'GET_TELEMETRY\n')
    data = s.recv(1024)
    print('Reçu:', data.decode('utf-8'))
```

#### Manipulation de données JSON :
```python
import json
payload = {'capteur_id': 'TEMP_01', 'valeur': 23.4, 'unite': 'C'}
json_str = json.dumps(payload)
```r""",

        '3. Structures de données avancées & Unions en Langage C': r"""### 🏗️ Structures de données avancées & Unions en Langage C
* **Structures (`struct`)** : Regroupement de plusieurs variables de types différents. En mémoire, chaque variable possède sa propre adresse, et la taille globale est au minimum égale à la somme des membres, plus d'éventuels octets de bourrage (padding) insérés par le compilateur pour l'alignement mémoire.
* **Unions (`union`)** : Regroupement de membres de types différents partageant la **même zone mémoire**. À tout moment, un seul membre peut être stocké dans l'union. L'occupation mémoire totale d'une union est égale à la taille de son membre le plus volumineux.
* **Exemple d'union** :
  ```cpp
  union Paquet {
      char brut[4];
      float valeur; // Partage le même espace de 4 octets
  };
  ```r""",

    },
    '🖥️ Administration Système': {
        '1. Droits Linux & Commandes Système': r"""### 🐧 Administration GNU/Linux
* **Droits Octaux (`chmod`)** :
  * `r` (Lecture) = 4, `w` (Écriture) = 2, `x` (Exécution) = 1.
  * `chmod 750 script.sh` : Propriétaire = `rwx` (7), Groupe = `r-x` (5), Autres = `---` (0).
* **Droits Spéciaux** : SUID (`4000`), SGID (`2000`), Sticky Bit (`1000` ex: `/tmp`).
* **Services Systemd** : `systemctl start|stop|restart|status|enable service_name`.
* **Supervision des logs** : `journalctl -u service_name -f` ou `tail -f /var/log/syslog`.r""",

        '2. Active Directory, Domaines & GPO': r"""### 🏢 Gestion de Parc sous Windows Server
* **Active Directory Domain Services (AD DS)** : Annuaire d'objets (Utilisateurs, Groupes, Ordinateurs).
* **Unités d'Organisation (OU)** : Conteneurs logiques pour organiser le domaine.
* **GPO (Group Policy Object)** : Politiques de configuration et de durcissement centralisées.
* **Ordre d'application des GPO (LSDOU)** : **L**ocal $\rightarrow$ **S**ite $\rightarrow$ **D**omaine $\rightarrow$ **O**U (la dernière stratégie appliquée prévaut sauf configuration 'Enforced').r""",

        '3. Virtualisation & Environnements Serveurs (Debian, VMware)': r"""### 🖥️ Virtualisation & Environnements Serveurs (Debian, VMware)
La virtualisation permet de faire fonctionner plusieurs machines virtuelles (VM) sur un unique serveur physique (Hyperviseur).

#### Hyperviseurs de Type 1 (Bare Metal) :
* Opèrent directement sur le matériel physique du serveur, sans système d'exploitation hôte préalable.
* Offrent des performances optimales et une isolation stricte des ressources.
* Exemples : **VMware ESXi**, Microsoft Hyper-V Server, Proxmox VE (KVM).

#### Hyperviseurs de Type 2 (Hosted) :
* S'exécutent comme des applications au-dessus d'un système d'exploitation hôte existant (Windows, Linux, macOS).
* Exemples : **VMware Workstation**, Oracle VM VirtualBox.

#### Serveur Linux Debian :
* Système d'exploitation stable par excellence pour héberger des serveurs d'infrastructure (DNS Bind9, DHCP isc-dhcp-server, Apache, etc.).r""",

    },
    '🔌 Électronique & IoT': {
        '1. Échantillonnage, CAN/CNA & Théorème de Shannon': r"""### 📡 Numérisation & Traitement du Signal
* **Théorème de Nyquist-Shannon** : La fréquence d'échantillonnage $Fe$ doit respecter $Fe \ge 2 \times F_{max}$ pour éviter tout **repliement de spectre (Aliasing)**. On place un filtre passe-bas anti-repliement avant le CAN.
* **Convertisseur Analogique-Numérique (CAN / ADC)** :
  * Résolution : $n$ bits $\rightarrow 2^n$ niveaux de quantification (de $0$ à $2^n - 1$).
  * **Quantum ($q$)** : Plus petite variation de tension détectable :
    $$q = \frac{V_{ref}}{2^n - 1} \approx \frac{V_{ref}}{2^n}$$
  * **Valeur numérique entière ($N$)** pour une tension d'entrée $V_e$ :
    $$N = \text{arrondi}\left(\frac{V_e}{q}\right) = \text{arrondi}\left(\frac{V_e \times (2^n - 1)}{V_{ref}}\right)$$r""",

        '2. Bus Série Matériels : I2C, SPI, UART & CAN Bus': r"""### 🔌 Liaisons de Données Embarquées
* **I2C** : 2 lignes bidirectionnelles (`SDA` Données, `SCL` Horloge). Maître-Esclave, adresses matérielles 7 bits sur bus avec résistances de Pull-up.
* **SPI** : 4 lignes full-duplex rapide (`MOSI`, `MISO`, `SCLK`, `SS/CS`). Sélection d'esclave active à l'état bas.
* **UART** : Liaison asynchrone point-à-point (2 fils `Tx`, `Rx`). Nécessite le même débit en bauds (ex: 115200 bauds, 8N1).
* **Bus CAN** : Bus différentiel robuste (`CAN_H`, `CAN_L`), résistant aux parasites industriels et automobiles. Résistances de terminaison de 120 $\Omega$ à chaque extrémité.r""",

        '3. Protocoles Connectés : MQTT & LoRaWAN': r"""### ☁️ Protocoles IoT & Télémesure
* **MQTT (Message Queuing Telemetry Transport)** : Architecture Publish/Subscribe autour d'un courtier (**Broker**). Messages légers publiés sur des thèmes (**Topics** ex: `site/batA/temp`). Niveaux de QoS :
  * `QoS 0` : Délivré au plus une fois (sans confirmation).
  * `QoS 1` : Délivré au moins une fois (avec accusé PUBACK).
  * `QoS 2` : Délivré exactement une fois (four-way handshake).
* **LoRaWAN** : Réseau LPWAN longue portée (plusieurs kilomètres) à très faible consommation d'énergie sur fréquences sans licence (868 MHz en Europe).r""",

        "4. Lois Fondamentales d'Électricité & Composants Passifs": r"""### 🔌 Lois Fondamentales d'Électricité & Composants Passifs
* **Loi d'Ohm** : $U = R \times I$ (la tension en Volts est égale à la résistance en Ohms multipliée par l'intensité en Ampères).
* **Loi de Joule (Puissance)** : $P = U \times I = R \times I^2 = \frac{U^2}{R}$ (la puissance dissipée par effet Joule est exprimée en Watts).
* **Lois de Kirchhoff** :
  * **Loi des Nœuds** : La somme des intensités des courants entrant dans un nœud est égale à la somme des intensités sortant du même nœud.
  * **Loi des Mailles** : La somme algébrique des tensions le long d'une maille fermée est nulle.
* **Condensateur** : Stocke des charges électriques.
  * **Relation Charge-Tension** : $Q = C \times U$ (la charge en Coulombs est proportionnelle à la capacité en Farads).
  * **Énergie emmagasinée** : $E_c = \frac{1}{2} C \times U^2$ (l'énergie stockée s'exprime en Joules).r""",

    },
    '📐 Modélisation UML & SysML': {
        '1. Diagrammes UML Essentiels (Classes, Séquence, Use Case)': r"""### 📐 Ingénierie Logicielle UML
* **Diagramme de Classes** : Modèle statique. Multiplicités (`1`, `0..1`, `1..*`, `*`).
  * **Agrégation (Losange blanc $\diamond$)** : Relation 'fait partie de' faible. L'élément peut exister sans le conteneur.
  * **Composition (Losange noir $\blacklozenge$)** : Relation d'appartenance forte. La destruction du conteneur détruit ses composants.
  * **Généralisation/Héritage (Flèche à triangle vide $\rightarrow$)** : Spécialisation de classe.
* **Diagramme de Séquence** : Chronologie des échanges d'objets au cours du temps. Flèche pleine pour appel synchrone, flèche ouverte pour asynchrone, pointillé pour retour.r""",

        '2. Diagrammes SysML (BDD, IBD, Exigences)': r"""### 🏗️ Modélisation Système SysML
* **BDD (Block Definition Diagram)** : Découpage structurel global du système en blocs matériels et logiciels.
* **IBD (Internal Block Diagram)** : Vue interne des flux de données (`flow ports`), d'énergie et de signaux circulant entre les ports des sous-blocs.
* **Diagramme d'Exigences (Requirement Diagram)** : Définition des critères du cahier des charges avec stéréotypes `<<deriveReqt>>`, `<<satisfy>>` (par un bloc) et `<<verify>>` (par un cas de test).r""",

    },
}

# MINI-QUIZ D'AUTO-ÉVALUATION PAR COURS
MINI_QUIZ_COURS = {   '1. Cryptographie : Symétrique, Asymétrique & Hachage': {   'expl': 'RSA '
                                                                        'est '
                                                                        'un '
                                                                        'algorithme '
                                                                        'asymétrique '
                                                                        'à clé '
                                                                        'publique/clé '
                                                                        'privée. '
                                                                        'AES '
                                                                        'et '
                                                                        'DES '
                                                                        'sont '
                                                                        'symétriques, '
                                                                        'SHA-256 '
                                                                        'est '
                                                                        'une '
                                                                        'fonction '
                                                                        'de '
                                                                        'hachage.',
                                                                'options': [   'AES-256',
                                                                               'RSA',
                                                                               'SHA-256',
                                                                               'DES'],
                                                                'q': 'Quel '
                                                                     'algorithme '
                                                                     'parmi '
                                                                     'les '
                                                                     'suivants '
                                                                     'est un '
                                                                     'algorithme '
                                                                     'de '
                                                                     'chiffrement '
                                                                     'asymétrique '
                                                                     '?',
                                                                'rep': 'RSA'},
    '1. Langage C++ : Mémoire, Pointeurs & POO': {   'expl': 'En C++, toute '
                                                             'allocation de '
                                                             'tableau '
                                                             'dynamique avec '
                                                             "'new[]' requiert "
                                                             'impérativement '
                                                             "'delete[]' pour "
                                                             'détruire tous '
                                                             'les éléments.',
                                                     'options': [   'delete',
                                                                    'free()',
                                                                    'delete[]',
                                                                    'clear()'],
                                                     'q': 'Quel opérateur C++ '
                                                          'doit '
                                                          'obligatoirement '
                                                          'être utilisé pour '
                                                          'libérer un tableau '
                                                          "alloué avec 'new "
                                                          "float[50]' ?",
                                                     'rep': 'delete[]'},
    '1. Modèle OSI vs TCP/IP & Encapsulation': {   'expl': 'UDP est un '
                                                           'protocole de '
                                                           'couche Transport '
                                                           '(couche 4), tout '
                                                           'comme TCP.',
                                                   'options': [   'Couche 2 '
                                                                  '(Liaison)',
                                                                  'Couche 3 '
                                                                  '(Réseau)',
                                                                  'Couche 4 '
                                                                  '(Transport)',
                                                                  'Couche 7 '
                                                                  '(Application)'],
                                                   'q': 'À quelle couche du '
                                                        'modèle OSI opère le '
                                                        'protocole UDP ?',
                                                   'rep': 'Couche 4 '
                                                          '(Transport)'},
    '1. Échantillonnage, CAN/CNA & Théorème de Shannon': {   'expl': 'Selon le '
                                                                     'théorème '
                                                                     'de '
                                                                     'Nyquist-Shannon, '
                                                                     'Fe >= 2 '
                                                                     '* Fmax. '
                                                                     'Pour 20 '
                                                                     'kHz, Fe '
                                                                     'doit '
                                                                     'être au '
                                                                     'moins de '
                                                                     '40 kHz '
                                                                     '(ex: '
                                                                     '44.1 kHz '
                                                                     'sur les '
                                                                     'CD '
                                                                     'Audio).',
                                                             'options': [   '10 '
                                                                            'kHz',
                                                                            '20 '
                                                                            'kHz',
                                                                            '40 '
                                                                            'kHz',
                                                                            '80 '
                                                                            'kHz'],
                                                             'q': 'Si un '
                                                                  'signal '
                                                                  'audio '
                                                                  'possède une '
                                                                  'fréquence '
                                                                  'maximale de '
                                                                  '20 kHz, '
                                                                  'quelle doit '
                                                                  'être la '
                                                                  'fréquence '
                                                                  'minimale '
                                                                  "d'échantillonnage "
                                                                  '(Fe) selon '
                                                                  'Shannon ?',
                                                             'rep': '40 kHz'},
    '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)': {   'expl': 'Pour '
                                                                           '/27, '
                                                                           'il '
                                                                           'reste '
                                                                           '32 '
                                                                           '- '
                                                                           '27 '
                                                                           '= '
                                                                           '5 '
                                                                           'bits '
                                                                           'pour '
                                                                           'les '
                                                                           'hôtes. '
                                                                           'Soit '
                                                                           '2^5 '
                                                                           '- '
                                                                           '2 '
                                                                           '= '
                                                                           '32 '
                                                                           '- '
                                                                           '2 '
                                                                           '= '
                                                                           '30 '
                                                                           'hôtes '
                                                                           'utilisables.',
                                                                   'options': [   '14',
                                                                                  '30',
                                                                                  '62',
                                                                                  '126'],
                                                                   'q': 'Combien '
                                                                        "d'adresses "
                                                                        "d'hôtes "
                                                                        'utilisables '
                                                                        'offre '
                                                                        'un '
                                                                        'sous-réseau '
                                                                        'avec '
                                                                        'un '
                                                                        'masque '
                                                                        '/27 ?',
                                                                   'rep': '30'},
    '2. Top 10 OWASP & Sécurité Applicative': {   'expl': 'Les requêtes '
                                                          'préparées séparent '
                                                          'strictement le code '
                                                          'SQL des données '
                                                          'utilisateurs '
                                                          'saisies, rendant '
                                                          "l'injection "
                                                          'impossible.',
                                                  'options': [   'Utiliser des '
                                                                 'expressions '
                                                                 'régulières '
                                                                 'de filtrage',
                                                                 'Utiliser des '
                                                                 'requêtes '
                                                                 'préparées '
                                                                 '(paramétrées)',
                                                                 'Chiffrer la '
                                                                 'base de '
                                                                 'données en '
                                                                 'AES',
                                                                 'Désactiver '
                                                                 'le port '
                                                                 'MySQL 3306'],
                                                  'q': 'Quelle est la méthode '
                                                       'la plus robuste pour '
                                                       'neutraliser les '
                                                       "failles d'injection "
                                                       'SQL ?',
                                                  'rep': 'Utiliser des '
                                                         'requêtes préparées '
                                                         '(paramétrées)'},
    '3. Structures de données avancées & Unions en Langage C': {   'expl': 'Une '
                                                                           'union '
                                                                           'fait '
                                                                           'la '
                                                                           'taille '
                                                                           'de '
                                                                           'son '
                                                                           'membre '
                                                                           'le '
                                                                           'plus '
                                                                           'grand, '
                                                                           'car '
                                                                           'tous '
                                                                           'ses '
                                                                           'membres '
                                                                           'partagent '
                                                                           'la '
                                                                           'même '
                                                                           'adresse '
                                                                           'de '
                                                                           'départ. '
                                                                           'Donc '
                                                                           'ici, '
                                                                           '4 '
                                                                           'octets.',
                                                                   'options': [   '1 '
                                                                                  'octet',
                                                                                  '4 '
                                                                                  'octets',
                                                                                  '5 '
                                                                                  'octets',
                                                                                  '8 '
                                                                                  'octets'],
                                                                   'q': 'En C, '
                                                                        'si '
                                                                        'une '
                                                                        'union '
                                                                        'regroupe '
                                                                        'un '
                                                                        'char '
                                                                        '(1 '
                                                                        'octet) '
                                                                        'et un '
                                                                        'int '
                                                                        '(4 '
                                                                        'octets), '
                                                                        'quelle '
                                                                        'est '
                                                                        'sa '
                                                                        'taille '
                                                                        'totale '
                                                                        'en '
                                                                        'mémoire '
                                                                        '?',
                                                                   'rep': '4 '
                                                                          'octets'},
    '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN': {   'expl': 'Le tag '
                                                                       '802.1Q '
                                                                       'inséré '
                                                                       'dans '
                                                                       'la '
                                                                       'trame '
                                                                       'fait '
                                                                       'exactement '
                                                                       '4 '
                                                                       'octets '
                                                                       '(32 '
                                                                       'bits), '
                                                                       'dont '
                                                                       '12 '
                                                                       'bits '
                                                                       'dédiés '
                                                                       'au '
                                                                       'VLAN '
                                                                       'ID.',
                                                               'options': [   '2 '
                                                                              'octets',
                                                                              '4 '
                                                                              'octets',
                                                                              '8 '
                                                                              'octets',
                                                                              '16 '
                                                                              'octets'],
                                                               'q': 'Quelle '
                                                                    'est la '
                                                                    'taille en '
                                                                    'octets du '
                                                                    'tag '
                                                                    'inséré '
                                                                    'par la '
                                                                    'norme '
                                                                    'IEEE '
                                                                    '802.1Q '
                                                                    'dans la '
                                                                    'trame '
                                                                    'Ethernet '
                                                                    '?',
                                                               'rep': '4 '
                                                                      'octets'},
    '3. Virtualisation & Environnements Serveurs (Debian, VMware)': {   'expl': 'Les '
                                                                                'hyperviseurs '
                                                                                'installés '
                                                                                'directement '
                                                                                'sur '
                                                                                'le '
                                                                                'matériel '
                                                                                '(Bare '
                                                                                'Metal) '
                                                                                'sont '
                                                                                'classifiés '
                                                                                'comme '
                                                                                'Type '
                                                                                '1 '
                                                                                '(ex: '
                                                                                'VMware '
                                                                                'ESXi, '
                                                                                'Hyper-V).',
                                                                        'options': [   'Hyperviseur '
                                                                                       'de '
                                                                                       'Type '
                                                                                       '1',
                                                                                       'Hyperviseur '
                                                                                       'de '
                                                                                       'Type '
                                                                                       '2',
                                                                                       'Système '
                                                                                       "d'exploitation "
                                                                                       'hébergé',
                                                                                       'Container '
                                                                                       'de '
                                                                                       'type '
                                                                                       'Docker'],
                                                                        'q': 'Comment '
                                                                             'classifie-t-on '
                                                                             'un '
                                                                             'hyperviseur '
                                                                             'comme '
                                                                             'VMware '
                                                                             'ESXi '
                                                                             'qui '
                                                                             "s'exécute "
                                                                             'directement '
                                                                             'sur '
                                                                             'le '
                                                                             'matériel '
                                                                             'physique '
                                                                             '(Bare '
                                                                             'Metal) '
                                                                             '?',
                                                                        'rep': 'Hyperviseur '
                                                                               'de '
                                                                               'Type '
                                                                               '1'},
    "4. Lois Fondamentales d'Électricité & Composants Passifs": {   'expl': "L'énergie "
                                                                            'est '
                                                                            'E '
                                                                            '= '
                                                                            '0.5 '
                                                                            '* '
                                                                            'C '
                                                                            '* '
                                                                            'U^2 '
                                                                            '= '
                                                                            '0.5 '
                                                                            '* '
                                                                            '(10e-6) '
                                                                            '* '
                                                                            '(10^2) '
                                                                            '= '
                                                                            '0.5 '
                                                                            '* '
                                                                            '10e-6 '
                                                                            '* '
                                                                            '100 '
                                                                            '= '
                                                                            '0.0005 '
                                                                            'Joules, '
                                                                            'soit '
                                                                            '0,5 '
                                                                            'mJ.',
                                                                    'options': [   '0,5 '
                                                                                   'mJ',
                                                                                   '5 '
                                                                                   'mJ',
                                                                                   '50 '
                                                                                   'mJ',
                                                                                   '100 '
                                                                                   'mJ'],
                                                                    'q': 'Si '
                                                                         'un '
                                                                         'condensateur '
                                                                         'de '
                                                                         '10 '
                                                                         'µF '
                                                                         'est '
                                                                         'chargé '
                                                                         'sous '
                                                                         'une '
                                                                         'tension '
                                                                         'de '
                                                                         '10 '
                                                                         'V, '
                                                                         'quelle '
                                                                         'énergie '
                                                                         'électrique '
                                                                         'a-t-il '
                                                                         'emmagasinée '
                                                                         '?',
                                                                    'rep': '0,5 '
                                                                           'mJ'},
    '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)': {   'expl': 'IPsec '
                                                                      'opère '
                                                                      'en '
                                                                      'Couche '
                                                                      '3 '
                                                                      '(Réseau) '
                                                                      'du '
                                                                      'modèle '
                                                                      'OSI '
                                                                      'pour '
                                                                      'chiffrer '
                                                                      'et '
                                                                      'authentifier '
                                                                      "l'intégralité "
                                                                      'des '
                                                                      'paquets '
                                                                      'IP '
                                                                      'circulant '
                                                                      'dans le '
                                                                      'tunnel.',
                                                              'options': [   'Couche '
                                                                             '2 '
                                                                             '(Liaison)',
                                                                             'Couche '
                                                                             '3 '
                                                                             '(Réseau)',
                                                                             'Couche '
                                                                             '4 '
                                                                             '(Transport)',
                                                                             'Couche '
                                                                             '7 '
                                                                             '(Application)'],
                                                              'q': 'À quel '
                                                                   'niveau du '
                                                                   'modèle OSI '
                                                                   'opère la '
                                                                   'suite de '
                                                                   'protocoles '
                                                                   'sécurisés '
                                                                   'IPsec pour '
                                                                   'configurer '
                                                                   'un tunnel '
                                                                   'VPN ?',
                                                              'rep': 'Couche 3 '
                                                                     '(Réseau)'},
    '5. Protocoles Industriels & Bus de terrain (Modbus, Profibus)': {   'expl': 'Modbus '
                                                                                 'RTU '
                                                                                 'ajoute '
                                                                                 '2 '
                                                                                 'octets '
                                                                                 'à '
                                                                                 'la '
                                                                                 'fin '
                                                                                 'de '
                                                                                 'la '
                                                                                 'trame '
                                                                                 'pour '
                                                                                 'y '
                                                                                 'stocker '
                                                                                 'un '
                                                                                 'condensat '
                                                                                 'de '
                                                                                 'contrôle '
                                                                                 "d'intégrité "
                                                                                 'CRC-16.',
                                                                         'options': [   'Le '
                                                                                        'checksum '
                                                                                        'de '
                                                                                        'parité '
                                                                                        'simple',
                                                                                        'Un '
                                                                                        'hash '
                                                                                        'SHA-256',
                                                                                        'Le '
                                                                                        'contrôle '
                                                                                        "d'erreur "
                                                                                        'CRC-16 '
                                                                                        '(Cyclic '
                                                                                        'Redundancy '
                                                                                        'Check)',
                                                                                        'Un '
                                                                                        'encapsulage '
                                                                                        'TLS'],
                                                                         'q': 'Dans '
                                                                              'une '
                                                                              'trame '
                                                                              'Modbus '
                                                                              'RTU, '
                                                                              'quel '
                                                                              'élément '
                                                                              'assure '
                                                                              'le '
                                                                              'contrôle '
                                                                              "d'intégrité "
                                                                              'de '
                                                                              'la '
                                                                              'trame '
                                                                              '?',
                                                                         'rep': 'Le '
                                                                                'contrôle '
                                                                                "d'erreur "
                                                                                'CRC-16 '
                                                                                '(Cyclic '
                                                                                'Redundancy '
                                                                                'Check)'},
    '6. Transmission optique (Fibres optiques Monomodes & Multimodes)': {   'expl': 'La '
                                                                                    'fibre '
                                                                                    'monomode '
                                                                                    'ne '
                                                                                    'transmet '
                                                                                    "qu'un "
                                                                                    'seul '
                                                                                    'rayon '
                                                                                    '(mode '
                                                                                    'de '
                                                                                    'propagation), '
                                                                                    'ce '
                                                                                    'qui '
                                                                                    'élimine '
                                                                                    'quasi-totalement '
                                                                                    'la '
                                                                                    'dispersion '
                                                                                    'modale '
                                                                                    'temporelle.',
                                                                            'options': [   'Fibre '
                                                                                           'Multimode '
                                                                                           'à '
                                                                                           'saut '
                                                                                           "d'indice",
                                                                                           'Fibre '
                                                                                           'Multimode '
                                                                                           'à '
                                                                                           'gradient '
                                                                                           "d'indice",
                                                                                           'Fibre '
                                                                                           'Monomode '
                                                                                           '(Single-mode)',
                                                                                           'Câble '
                                                                                           'paire '
                                                                                           'torsadée '
                                                                                           'blindée '
                                                                                           'STP'],
                                                                            'q': 'Quelle '
                                                                                 'fibre '
                                                                                 'optique '
                                                                                 'présente '
                                                                                 'la '
                                                                                 'plus '
                                                                                 'faible '
                                                                                 'dispersion '
                                                                                 'modale, '
                                                                                 'permettant '
                                                                                 'ainsi '
                                                                                 'la '
                                                                                 'plus '
                                                                                 'longue '
                                                                                 'distance '
                                                                                 'de '
                                                                                 'transmission '
                                                                                 '?',
                                                                            'rep': 'Fibre '
                                                                                   'Monomode '
                                                                                   '(Single-mode)'}}

# --- FLASHCARDS ACTIVES ÉTENDUES ---
FLASHCARDS_DATA = [
    {
        "id": 1,
        "module": "📶 Réseaux & Télécoms",
        "chap": "1. Modèle OSI vs TCP/IP",
        "q": "Quelles sont les 7 couches du modèle OSI et leurs PDU respectifs ?",
        "a": "7. Application (Donnée), 6. Présentation (Donnée), 5. Session (Donnée), 4. Transport (Segment TCP / Datagramme UDP), 3. Réseau (Paquet IP), 2. Liaison (Trame Ethernet/MAC), 1. Physique (Bit/Signal).",
        "note": "💡 **Conseil Examen** : Mnémonique de haut en bas : Après Plusieurs Semaines Tout Revient Logiquement Propre. Ne confondez jamais Trame (C2) et Paquet (C3) !",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 1. Modèle OSI vs TCP/IP",
        "v_id": "33UJvS_z8R8",
        "v_title": "Comprendre le Modèle OSI en 10 minutes"
    },
    {
        "id": 2,
        "module": "📶 Réseaux & Télécoms",
        "chap": "1. Modèle OSI vs TCP/IP",
        "q": "Quel est le processus de connexion à 3 voies (3-way handshake) du protocole TCP ?",
        "a": "1. Client -> Serveur : SYN (séquence x). 2. Serveur -> Client : SYN-ACK (séquence y, ack x+1). 3. Client -> Serveur : ACK (ack y+1). La connexion TCP est établie.",
        "note": "💡 **Conseil Examen** : La retransmission d'un segment manquant s'effectue soit par le temporisateur RTO, soit par 3 DupACKs consécutifs.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 1. Modèle OSI vs TCP/IP",
        "v_id": "0j3_T7sN8J4",
        "v_title": "Fonctionnement détaillé de TCP & Handshake"
    },
    {
        "id": 3,
        "module": "📶 Réseaux & Télécoms",
        "chap": "2. Adressage IPv4/IPv6 & VLSM",
        "q": "Quelle est la formule du nombre d'hôtes utiles dans un sous-réseau IPv4 de CIDR donné ?",
        "a": "N_hôtes = 2^(32 - CIDR) - 2. On soustrait l'adresse Réseau (bits hôtes à 0) et l'adresse de Broadcast (bits hôtes à 1).",
        "note": "💡 **Conseil Examen** : Pour un masque /28, 32-28 = 4 bits. 2^4 - 2 = 14 hôtes utilisables. Soustrayez toujours 2 !",
        "cours_ref": "🧮 Laboratoire de Calculs -> Subnetting VLSM IPv4",
        "v_id": "42S-A-9PqM0",
        "v_title": "Masterclass Subnetting VLSM IPv4"
    },
    {
        "id": 4,
        "module": "📶 Réseaux & Télécoms",
        "chap": "2. Adressage IPv4/IPv6 & VLSM",
        "q": "Quel protocole remplace le protocole ARP en IPv6 pour découvrir les adresses MAC des voisins ?",
        "a": "Le protocole NDP (Neighbor Discovery Protocol), s'appuyant sur des messages ICMPv6 Neighbor Solicitation (NS) et Neighbor Advertisement (NA).",
        "note": "💡 **Conseil Examen** : En IPv6, le broadcast n'existe plus ! Il est entièrement remplacé par le Multicast (ex: ff02::1 pour tous les nœuds).",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 2. Adressage IPv4/IPv6",
        "v_id": "72sn_0M4T4g",
        "v_title": "IPv6, SLAAC et NDP expliqués simplement"
    },
    {
        "id": 5,
        "module": "📶 Réseaux & Télécoms",
        "chap": "3. Commutation & VLANs",
        "q": "Comment un commutateur (Switch) remplit-il sa table de commutation (table MAC / CAM) ?",
        "a": "Par apprentissage passif (Learning) : à la réception d'une trame, il lit l'adresse MAC source et l'associe au port d'entrée. Pour commuter, il consulte la MAC destination.",
        "note": "💡 **Conseil Examen** : Si la MAC destination est inconnue, le switch effectue un inondage (Flooding) sur tous les ports du VLAN sauf le port récepteur.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Commutation & VLANs",
        "v_id": "06Y6qYg9_C0",
        "v_title": "Commutation Ethernet & Table CAM"
    },
    {
        "id": 6,
        "module": "📶 Réseaux & Télécoms",
        "chap": "3. Commutation & VLANs",
        "q": "Quelle est la taille exacte et le rôle du tag inséré par la norme IEEE 802.1Q ?",
        "a": "Le tag mesure 4 octets (32 bits), dont 12 bits sont dédiés au VID (VLAN ID), permettant de faire transiter jusqu'à 4094 VLANs sur une liaison Trunk.",
        "note": "💡 **Conseil Examen** : Le VLAN Natif (VLAN 1 par défaut) voyage non étiqueté sur le Trunk. Il doit être identique aux deux extrémités du lien.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Commutation & VLANs",
        "v_id": "0j3_T7sN8J4",
        "v_title": "Tout savoir sur le Trunking 802.1Q"
    },
    {
        "id": 7,
        "module": "📶 Réseaux & Télécoms",
        "chap": "4. Routage Inter-VLAN",
        "q": "Quelle est la séquence de commandes Cisco IOS pour configurer Router-on-a-Stick sur le VLAN 20 ?",
        "a": "interface GigabitEthernet0/0.20 -> encapsulation dot1Q 20 -> ip address 192.168.20.254 255.255.255.0.",
        "note": "💡 **Conseil Examen** : Pensez à activer l'interface physique parente avec no shutdown sous interface g0/0 !",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 4. Routage Inter-VLAN",
        "v_id": "LqT5y7aZJ4k",
        "v_title": "Configuration Router-on-a-Stick Cisco"
    },
    {
        "id": 8,
        "module": "📶 Réseaux & Télécoms",
        "chap": "3. Commutation & Spanning Tree",
        "q": "Quel est le rôle principal du protocole Spanning Tree (STP 802.1D / RSTP 802.1w) ?",
        "a": "Éviter les boucles logiques de Niveau 2 (tempêtes de broadcast) en bloquant les ports redondants pour former une topologie en arbre sans boucle.",
        "note": "💡 **Conseil Examen** : Le Root Bridge est élu selon le Bridge ID (Priority + MAC) le plus faible. RSTP converge en moins de 2 secondes.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Commutation & Spanning Tree",
        "v_id": "i8D4W6U4z_E",
        "v_title": "Spanning Tree & RSTP 802.1w"
    },
    {
        "id": 9,
        "module": "📶 Réseaux & Télécoms",
        "chap": "5. Services Infrastructure",
        "q": "Quels sont les 4 messages du processus DHCP DORA ?",
        "a": "1. Discover (Broadcast client UDP 67). 2. Offer (Proposition serveur UDP 68). 3. Request (Demande client). 4. Acknowledge (Validation du bail par le serveur).",
        "note": "💡 **Conseil Examen** : Pour relayer DHCP à travers un routeur, configurez ip helper-address <IP_Serveur_DHCP> sur l'interface du sous-réseau client.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 5. Services Infrastructure",
        "v_id": "72sn_0M4T4g",
        "v_title": "Services DHCP & Relai DHCP"
    },
    {
        "id": 10,
        "module": "📶 Réseaux & Télécoms",
        "chap": "5. Services Infrastructure",
        "q": "À quoi servent les enregistrements DNS de type A, AAAA, CNAME, MX et PTR ?",
        "a": "A : Nom -> IPv4. AAAA : Nom -> IPv6. CNAME : Alias. MX : Serveur Mail. PTR : Résolution inverse (IP -> Nom FQDN).",
        "note": "💡 **Conseil Examen** : L'enregistrement PTR se situe dans la zone de recherche inverse (ex: 1.168.192.in-addr.arpa).",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 5. Services Infrastructure",
        "v_id": "72sn_0M4T4g",
        "v_title": "Architecture du DNS & Enregistrements"
    },
    {
        "id": 11,
        "module": "📶 Réseaux & Télécoms",
        "chap": "5. Services Infrastructure",
        "q": "Quelle est la différence entre NAT Statique et PAT (Overload) ?",
        "a": "NAT Statique : traduction 1-à-1 fixe d'IP privée vers publique. PAT (Port Address Translation) : multiple IP privées sur 1 IP publique grâce aux ports TCP/UDP.",
        "note": "💡 **Conseil Examen** : La commande Cisco PAT est ip nat inside source list <ACL> interface <WAN> overload.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 5. Services Infrastructure",
        "v_id": "LqT5y7aZJ4k",
        "v_title": "Comprendre le NAT/PAT & Port Forwarding"
    },
    {
        "id": 12,
        "module": "📶 Réseaux & Télécoms",
        "chap": "6. Routage Dynamique OSPF",
        "q": "Sur quelle métrique et quel algorithme repose le protocole de routage OSPF ?",
        "a": "Algorithme d'État de Lien (Dijkstra / Shortest Path First) avec métrique basée sur le Coût de Bande Passante (Coût = 10^8 / Débit bps).",
        "note": "💡 **Conseil Examen** : Toutes les zones OSPF (Areas) doivent obligatoirement se raccorder à l'Area 0 (Backbone Area).",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 6. Routage Dynamique",
        "v_id": "3k1-zK7u1G0",
        "v_title": "Routage OSPF & Aires OSPF"
    },
    {
        "id": 13,
        "module": "📶 Réseaux & Télécoms",
        "chap": "7. Transmissions Optiques",
        "q": "Quelles sont les caractéristiques comparées des fibres Monomode (SMF) et Multimode (MMF) ?",
        "a": "Monomode (SMF) : cœur 9 µm, émetteur Laser (1310/1550 nm), très longue portée, pas de dispersion modale. Multimode (MMF) : cœur 50/62.5 µm, émetteur LED (850/1300 nm), portée < 500m.",
        "note": "💡 **Conseil Examen** : L'angle limite de réflexion totale interne suit sin(i_lim) = n2/n1 (avec n1 cœur > n2 gaine).",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 7. Transmissions Optiques",
        "v_id": "3Z8oE-pCq00",
        "v_title": "Fibre Optique : Monomode vs Multimode"
    },
    {
        "id": 14,
        "module": "📶 Réseaux & Télécoms",
        "chap": "7. Théorie de l'Information",
        "q": "Quelle est la formule de la capacité maximale binaire d'un canal bruité (Shannon-Hartley) ?",
        "a": "C = B * log2(1 + S/N) en bps, avec B la bande passante (Hz) et S/N le rapport signal sur bruit en puissance linéaire.",
        "note": "💡 **Conseil Examen** : Si le rapport S/N est donné en dB, convertissez-le d'abord en linéaire : S/N = 10^(SNR_dB / 10).",
        "cours_ref": "📊 Mathématiques Appliquées -> Calculs de Décibels",
        "v_id": "3Z8oE-pCq00",
        "v_title": "Capacité de Shannon & Rapport Signal/Bruit"
    },
    {
        "id": 15,
        "module": "📶 Réseaux & Télécoms",
        "chap": "7. Théorie de l'Information",
        "q": "Quelle est la relation entre Débit binaire D (bps) et Rapidité de modulation R (Bauds) ?",
        "a": "D = R * log2(M) = R * n, où n est le nombre de bits transmis par symbole (valence M = 2^n).",
        "note": "💡 **Conseil Examen** : Pour une modulation 16-QAM (M = 16), n = log2(16) = 4 bits/symbole. Un débit de 2400 Bauds donne 9600 bps.",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°9 Bauds vs bps",
        "v_id": "3Z8oE-pCq00",
        "v_title": "Bauds vs Bits par seconde et Valences"
    },
    {
        "id": 16,
        "module": "📶 Réseaux & Télécoms",
        "chap": "8. Wireshark & Analyse",
        "q": "Quels filtres Wireshark isolent le trafic HTTP, DNS, IP source 192.168.1.10 et TCP 80 ?",
        "a": "http, dns, ip.src == 192.168.1.10, tcp.port == 80. Combinaisons avec && ou and.",
        "note": "💡 **Conseil Examen** : Ne confondez pas Filtre de Capture (host 10.0.0.1) et Filtre d'Affichage (ip.addr == 10.0.0.1).",
        "cours_ref": "🔍 Lab Décodeur Wireshark",
        "v_id": "TkCSr30UojM",
        "v_title": "Maîtriser les filtres Wireshark"
    },
    {
        "id": 17,
        "module": "📶 Réseaux & Télécoms",
        "chap": "3. Sécurité Switchs Cisco",
        "q": "Quels sont les 3 modes de violation pour Cisco Port Security ?",
        "a": "1. protect : jette sans alerte. 2. restrict : jette + alerte SNMP + incrémente compteur. 3. shutdown : désactive le port (err-disabled).",
        "note": "💡 **Conseil Examen** : Pour réactiver un port en err-disabled : faites shutdown puis no shutdown sous l'interface.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Sécurité des Commutateurs",
        "v_id": "0j3_T7sN8J4",
        "v_title": "Sécuriser les ports avec Port Security"
    },
    {
        "id": 18,
        "module": "📶 Réseaux & Télécoms",
        "chap": "2. En-tête IPv4",
        "q": "Quel est le rôle des champs TTL et Protocol dans l'en-tête IPv4 ?",
        "a": "TTL : décrémenté de 1 par chaque routeur (évite les boucles). Protocol : indique le protocole encapsulé (6 = TCP, 17 = UDP, 1 = ICMP).",
        "note": "💡 **Conseil Examen** : En valeur hexadécimale Wireshark : 0x06 = TCP, 0x11 = UDP, 0x01 = ICMP.",
        "cours_ref": "📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 2. En-tête IP",
        "v_id": "TkCSr30UojM",
        "v_title": "Décodage d'en-tête IP sous Wireshark"
    },
    {
        "id": 19,
        "module": "🔒 Cybersécurité",
        "chap": "1. Méthode EBIOS RM",
        "q": "Quels sont les 5 Ateliers de la méthode EBIOS RM de l'ANSSI ?",
        "a": "1. Cadrage & Socle de sécurité. 2. Sources de Risques (SR). 3. Scénarios Stratégiques. 4. Scénarios Opérationnels (Kill Chain). 5. Traitement des Risques (PACS).",
        "note": "💡 **Conseil Examen** : Retenez les critères d'impact DICP : Disponibilité, Intégrité, Confidentialité, Preuve/Traçabilité.",
        "cours_ref": "🛡️ TP Cybersécurité -> Ateliers EBIOS RM ANSSI",
        "v_id": "J8n0j3x9K2A",
        "v_title": "Méthode EBIOS RM ANSSI en 5 Ateliers"
    },
    {
        "id": 20,
        "module": "🔒 Cybersécurité",
        "chap": "2. Analyse PIA / AIPD",
        "q": "Quand une Analyse d'Impact relative à la Protection des Données (AIPD/PIA) est-elle obligatoire ?",
        "a": "Conformément à l'Art. 35 du RGPD, dès qu'un traitement est susceptible d'engendrer un risque élevé pour la vie privée, notamment lorsqu'il remplit au moins 2 critères sur 9 de la grille CNIL.",
        "note": "💡 **Conseil Examen** : Exemples de critères CNIL : profilage, données sensibles/biométriques, personnes vulnérables (salariés/mineurs), grande échelle.",
        "cours_ref": "🛡️ TP Cybersécurité -> Atelier PIA / AIPD RGPD",
        "v_id": "5k9m2-8a9X0",
        "v_title": "Réaliser une AIPD / PIA RGPD"
    },
    {
        "id": 21,
        "module": "🔒 Cybersécurité",
        "chap": "3. Cryptographie",
        "q": "Quelle est la différence fondamentale entre le chiffrement symétrique et asymétrique ?",
        "a": "Symétrique : une seule clé secrète partagée pour chiffrer/déchiffrer (rapide, ex: AES-256). Asymétrique : clé publique pour chiffrer, clé privée pour déchiffrer (résout le partage de clé, ex: RSA-2048).",
        "note": "💡 **Conseil Examen** : En pratique, on utilise un chiffrement hybride : RSA pour échanger une clé de session AES, puis AES pour les données.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 1. Cryptographie",
        "v_id": "0iY2m-J4z-0",
        "v_title": "Chiffrement Symétrique vs Asymétrique"
    },
    {
        "id": 22,
        "module": "🔒 Cybersécurité",
        "chap": "3. Cryptographie",
        "q": "Qu'est-ce qu'une fonction de hachage irréversible et à quoi sert une empreinte SHA-256 ?",
        "a": "Une fonction mathématique à sens unique qui transforme un message de taille quelconque en une empreinte de taille fixe (256 bits). Utilisée pour vérifier l'Intégrité.",
        "note": "💡 **Conseil Examen** : Une fonction de hachage est irréversible (impossible de retrouver le message d'origine) et déterministe.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 1. Cryptographie",
        "v_id": "0iY2m-J4z-0",
        "v_title": "Hachage SHA-256 & Intégrité"
    },
    {
        "id": 23,
        "module": "🔒 Cybersécurité",
        "chap": "4. PKI & Certificats X.509",
        "q": "Pourquoi la CA Racine (Root CA) d'une PKI doit-elle être conservée hors ligne (offline) ?",
        "a": "Pour empêcher toute compromission à distance. Si la clé privée de la Root CA est compromise, toute la chaîne de confiance s'effondre.",
        "note": "💡 **Conseil Examen** : Ce sont les CA Intermédiaires (Issuing CAs) en ligne qui émettent les certificats clients et serveurs.",
        "cours_ref": "🛡️ TP Cybersécurité -> PKI & Certificats X.509",
        "v_id": "0iY2m-J4z-0",
        "v_title": "Architecture PKI & Autorités de Certification"
    },
    {
        "id": 24,
        "module": "🔒 Cybersécurité",
        "chap": "4. PKI & Certificats X.509",
        "q": "Quelle extension d'un certificat X.509 permet de déclarer plusieurs noms de domaine / IPs ?",
        "a": "L'extension SAN (Subject Alternative Name).",
        "note": "💡 **Conseil Examen** : Sans l'extension SAN, les navigateurs modernes rejettent le certificat TLS même si le Common Name (CN) est correct.",
        "cours_ref": "🛡️ TP Cybersécurité -> PKI & Certificats X.509",
        "v_id": "0iY2m-J4z-0",
        "v_title": "Certificats TLS X.509 & Extension SAN"
    },
    {
        "id": 25,
        "module": "🔒 Cybersécurité",
        "chap": "4. PKI & Certificats X.509",
        "q": "Quelles sont les commandes OpenSSL pour générer une clé privée RSA et une demande CSR ?",
        "a": "Clé : openssl genrsa -out server.key 2048. Demande CSR : openssl req -new -key server.key -out server.csr.",
        "note": "💡 **Conseil Examen** : Pour inspecter le contenu binaire d'un certificat : openssl x509 -in server.crt -text -noout.",
        "cours_ref": "🛡️ TP Cybersécurité -> PKI & Certificats X.509",
        "v_id": "0iY2m-J4z-0",
        "v_title": "Tutoriel Commandes OpenSSL"
    },
    {
        "id": 26,
        "module": "🔒 Cybersécurité",
        "chap": "5. Architecture DMZ & pfSense",
        "q": "Quelle est la règle d'isolation réseau fondamentale entre la DMZ et le LAN ?",
        "a": "Interdiction stricte d'initiation de connexion depuis la DMZ vers le LAN. Seul le LAN ou le WAN peuvent initier une connexion vers la DMZ.",
        "note": "💡 **Conseil Examen** : Si un serveur Web en DMZ est compromis par un pirate, celui-ci ne doit pas pouvoir attaquer le LAN interne.",
        "cours_ref": "🛡️ TP Cybersécurité -> Pare-Feu pfSense & DMZ",
        "v_id": "L2k3j4X5m-0",
        "v_title": "Architecture DMZ & Configuration pfSense"
    },
    {
        "id": 27,
        "module": "🔒 Cybersécurité",
        "chap": "5. Architecture DMZ & pfSense",
        "q": "Quels sont les ports TCP/UDP indispensables à autoriser pour le fonctionnement d'Active Directory ?",
        "a": "DNS : 53 (TCP/UDP), Kerberos : 88 (TCP/UDP), LDAP : 389 (TCP/UDP), LDAPS : 636 (TCP), SMB : 445 (TCP), RPC : 135 (TCP).",
        "note": "💡 **Conseil Examen** : Kerberos gère l'authentification (port 88) tandis que LDAP gère les requêtes d'annuaire (port 389/636).",
        "cours_ref": "🛡️ TP Cybersécurité -> Matrice des Flux AD",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Ports & Flux Active Directory"
    },
    {
        "id": 28,
        "module": "🔒 Cybersécurité",
        "chap": "6. Top 10 OWASP",
        "q": "Quelle technique prémunit définitivement une application web contre les injections SQL ?",
        "a": "L'utilisation de requêtes préparées (paramétrées / Prepared Statements) qui séparent strictly le code SQL des données utilisateurs.",
        "note": "💡 **Conseil Examen** : Le simple filtrage d'expressions régulières ou l'échappement manuel de caractères ne suffit pas face aux contournements OWASP.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 3. Top 10 OWASP",
        "v_id": "0k3j4X5m-0",
        "v_title": "Injections SQL & Requêtes Préparées"
    },
    {
        "id": 29,
        "module": "🔒 Cybersécurité",
        "chap": "6. Top 10 OWASP",
        "q": "Quelle est la différence entre une faille XSS Stored et XSS Reflected ?",
        "a": "XSS Stored : le script malveillant est stocké en BDD et exécuté pour tous les visiteurs. XSS Reflected : le script est réfléchi immédiatement dans l'URL.",
        "note": "💡 **Conseil Examen** : La parade contre le XSS est l'échappement systématique des caractères HTML (&lt;, &gt;, quotes) et l'en-tête CSP (Content Security Policy).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 3. Top 10 OWASP",
        "v_id": "0k3j4X5m-0",
        "v_title": "OWASP XSS & Sécurisation Web"
    },
    {
        "id": 30,
        "module": "🔒 Cybersécurité",
        "chap": "6. Top 10 OWASP",
        "q": "En quoi consiste une attaque CSRF (Cross-Site Request Forgery) et comment la contrecarrer ?",
        "a": "Attaque qui piège un utilisateur authentifié pour exécuter des actions non voulues à son insu. Parade : utiliser un Jetons Anti-CSRF imprédictible.",
        "note": "💡 **Conseil Examen** : Le jeton anti-CSRF est un token unique généré par session et vérifié lors de chaque soumission de formulaire POST.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 3. Top 10 OWASP",
        "v_id": "0k3j4X5m-0",
        "v_title": "Faille CSRF & Protection par Tokens"
    },
    {
        "id": 31,
        "module": "🔒 Cybersécurité",
        "chap": "5. Pare-feu & Filtrage",
        "q": "Quelle est la politique de filtrage recommandée par défaut sur un pare-feu réseau ?",
        "a": "Politique Deny All (Tout refuser par défaut) et n'autoriser explicitement que les flux strictement nécessaires (Whitelisting).",
        "note": "💡 **Conseil Examen** : La dernière règle d'un pare-feu (règle 999) est toujours Deny Any Any.",
        "cours_ref": "🛡️ TP Cybersécurité -> Pare-Feu pfSense",
        "v_id": "L2k3j4X5m-0",
        "v_title": "Filtrage Réseau & Politiques Pare-Feu"
    },
    {
        "id": 32,
        "module": "🔒 Cybersécurité",
        "chap": "7. Tunnels VPN",
        "q": "Quelle est la différence entre un VPN IPsec (Couche 3) et un VPN TLS / OpenVPN (Couche 4) ?",
        "a": "IPsec (Couche 3) : chiffrement au niveau paquet IP (site-à-site), transparent pour les applications. TLS (Couche 4) : VPN client-à-site via port TCP 443.",
        "note": "💡 **Conseil Examen** : IPsec utilise le protocole ESP (IP 50) pour le chiffrement/authentification et IKE (UDP 500) pour la négociation de clés.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 4. Tunnels VPN",
        "v_id": "L2k3j4X5m-0",
        "v_title": "Tunnels VPN IPsec vs TLS"
    },
    {
        "id": 33,
        "module": "🔒 Cybersécurité",
        "chap": "8. Sécurité IoT",
        "q": "Sur quel port et quel protocole repose la version sécurisée de MQTT (MQTTS) ?",
        "a": "MQTTS s'appuie sur MQTT encapsulé dans une couche TLS/SSL, fonctionnant par défaut sur le port TCP 8883 (au lieu du port 1883 en clair).",
        "note": "💡 **Conseil Examen** : MQTTS garantit la confidentialité des messages de télémétrie capteurs et l'authentification du Broker par certificat X.509.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 5. Sécurité IoT",
        "v_id": "0iY2m-J4z-0",
        "v_title": "Protocole MQTTS & Sécurisation IoT"
    },
    {
        "id": 34,
        "module": "🔒 Cybersécurité",
        "chap": "9. Attaques Réseau",
        "q": "Comment fonctionne une attaque SYN Flood et comment la neutraliser ?",
        "a": "Le pirate envoie une masse de paquets TCP SYN sans répondre au SYN-ACK, saturant la table de connexions du serveur. Parade : activer les SYN Cookies.",
        "note": "💡 **Conseil Examen** : La technologie SYN Cookies permet au serveur d'encode l'état de la connexion dans le numéro de séquence sans allouer de mémoire.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 6. Attaques Réseau",
        "v_id": "0k3j4X5m-0",
        "v_title": "Attaques DoS/DDoS & SYN Flood"
    },
    {
        "id": 35,
        "module": "🔒 Cybersécurité",
        "chap": "10. Sécurité Wi-Fi",
        "q": "Quel est le rôle d'un serveur RADIUS dans une architecture Wi-Fi 802.1X / WPA3-Enterprise ?",
        "a": "Le serveur RADIUS agit comme serveur d'authentification centralisé : il vérifie les identifiants/certificats des utilisateurs auprès de l'annuaire (AD/LDAP).",
        "note": "💡 **Conseil Examen** : En WPA2/WPA3-Personal, la clé est partagée (PSK). En WPA-Enterprise, chaque utilisateur a son propre compte d'accès.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 7. Sécurité Wi-Fi",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Wi-Fi 802.1X & Serveur RADIUS"
    },
    {
        "id": 36,
        "module": "🔒 Cybersécurité",
        "chap": "11. Exploitation de vulnérabilité",
        "q": "Qu'est-ce qu'une attaque par Dépassement de Tampon (Buffer Overflow) ?",
        "a": "Écriture de données au-delà de la mémoire allouée à un tableau, écrasant l'adresse de retour dans la Pile pour exécuter du code malveillant (Shellcode).",
        "note": "💡 **Conseil Examen** : Parades : fonctions C sûres (strncpy au lieu de strcpy) et protections compilateur (ASLR, NX Bit / DEP, Stack Canaries).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 8. Développement Sécurisé",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Buffer Overflow & Protections Mémoire"
    },
    {
        "id": 37,
        "module": "💻 Programmation / Dev",
        "chap": "1. Gestion Mémoire C++",
        "q": "Quelle est la différence entre la mémoire Pile (Stack) et la mémoire Tas (Heap) ?",
        "a": "Pile (Stack) : automatique, rapide, taille limitée, portée locale. Tas (Heap) : dynamique, allouée avec new/delete, gérée par le développeur, risque de fuites.",
        "note": "💡 **Conseil Examen** : Toute allocation avec new doit être libérée avec delete. Tout new[] doit être libéré avec delete[].",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++",
        "v_id": "S1yR7_7bWRE",
        "v_title": "Mémoire C++ : Pile vs Tas"
    },
    {
        "id": 38,
        "module": "💻 Programmation / Dev",
        "chap": "1. Gestion Mémoire C++",
        "q": "Pourquoi est-il obligatoire d'utiliser delete[] pour un tableau alloué dynamiquement ?",
        "a": "L'opérateur delete[] appelle le destructeur pour chaque élément du tableau avant de restituer la mémoire. delete seul ne détruit que le premier élément.",
        "note": "💡 **Conseil Examen** : L'oubli des crochets [] lors de la libération d'un tableau dynamique provoque une fuite de mémoire (Memory Leak).",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++",
        "v_id": "S1yR7_7bWRE",
        "v_title": "Allocation Dynamique delete[] C++"
    },
    {
        "id": 39,
        "module": "💻 Programmation / Dev",
        "chap": "1. Gestion Mémoire C++",
        "q": "Quelle est la différence entre un pointeur (*) et une référence (&) en C++ ?",
        "a": "Un pointeur est une variable qui contient une adresse mémoire (peut être NULL et réassignable). Une référence est un alias fixe d'une variable existante (non NULL).",
        "note": "💡 **Conseil Examen** : Préférez le passage de grands objets par référence constante (const MaClasse& obj) pour éviter les copies coûteuses en mémoire.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++",
        "v_id": "S1yR7_7bWRE",
        "v_title": "Pointeurs et Références en C++"
    },
    {
        "id": 40,
        "module": "💻 Programmation / Dev",
        "chap": "1. Smart Pointers C++11",
        "q": "Quelle est la différence entre std::unique_ptr et std::shared_ptr en C++11 ?",
        "a": "std::unique_ptr : propriété exclusive d'une ressource (non copiable, libération auto). std::shared_ptr : propriété partagée avec compteur de références.",
        "note": "💡 **Conseil Examen** : Les Smart Pointers gèrent automatiquement le cycle de vie de la mémoire (RAII) et éliminent les fuites mémoire.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++",
        "v_id": "S1yR7_7bWRE",
        "v_title": "Smart Pointers C++11"
    },
    {
        "id": 41,
        "module": "💻 Programmation / Dev",
        "chap": "2. Langage C",
        "q": "Quelle est la différence d'occupation mémoire entre une struct et une union en C ?",
        "a": "struct : chaque membre possède son propre espace mémoire (somme des tailles). union : tous les membres partagent la même adresse (taille du plus grand).",
        "note": "💡 **Conseil Examen** : L'union est idéale pour décoder des trames réseau brutes (ex: lire un float 32 bits sous forme de 4 octets char[4]).",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°12 C/C++",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Structures et Unions en Langage C"
    },
    {
        "id": 42,
        "module": "💻 Programmation / Dev",
        "chap": "3. POO C++",
        "q": "À quoi servent les niveaux d'accès private, protected et public en POO C++ ?",
        "a": "private : accessible uniquement dans la classe. protected : accessible dans la classe et ses classes dérivées. public : accessible partout.",
        "note": "💡 **Conseil Examen** : C'est le principe d'Encapsulation : masquez les attributs en private et fournissez des accesseurs public (getters/setters).",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Encapsulation & Niveaux d'Accès POO"
    },
    {
        "id": 43,
        "module": "💻 Programmation / Dev",
        "chap": "3. POO C++",
        "q": "Comment s'écrit l'héritage public d'une classe Fille depuis une classe Mere en C++ ?",
        "a": "class Fille : public Mere { public: Fille(); };",
        "note": "💡 **Conseil Examen** : L'héritage public préserve les droits public et protected de la classe mère dans la classe fille.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Héritage POO C++"
    },
    {
        "id": 44,
        "module": "💻 Programmation / Dev",
        "chap": "3. POO C++",
        "q": "Qu'est-ce qu'une méthode virtuelle pure en C++ et quel est son impact ?",
        "a": "Une méthode déclarée avec virtual void f() = 0;. Elle n'a pas d'implémentation dans la classe mère et rend la classe Abstraite (non instanciable).",
        "note": "💡 **Conseil Examen** : Une classe fille doit obligatoirement redéfinir toutes les méthodes virtuelles pures de la classe mère pour pouvoir être instanciée.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Classes Abstraites & Méthodes Virtuelles Pures"
    },
    {
        "id": 45,
        "module": "💻 Programmation / Dev",
        "chap": "3. POO C++",
        "q": "Pourquoi le destructeur d'une classe mère polymorphe doit-il obligatoirement être virtual ?",
        "a": "Pour garantir que lors de la suppression d'un objet via un pointeur de classe mère (delete ptr), le destructeur de la classe fille soit correctement exécuté.",
        "note": "💡 **Conseil Examen** : Si le destructeur n'est pas virtuel, seul le destructeur de la classe mère est appelé, provoquant une fuite de la mémoire de la fille.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Destructeurs Virtuels en C++"
    },
    {
        "id": 46,
        "module": "💻 Programmation / Dev",
        "chap": "4. Multithreading C++11",
        "q": "Comment instancier et exécuter un thread en parallèle en C++11 avec std::thread ?",
        "a": "std::thread t(maFonction, arg1); t.join(); (ou t.detach();).",
        "note": "💡 **Conseil Examen** : N'oubliez jamais d'appeler t.join() pour attendre la fin du thread avant la destruction de l'objet std::thread.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 3. Multithreading C++",
        "v_id": "5m9k3j4X5m0",
        "v_title": "Multithreading C++11 avec std::thread"
    },
    {
        "id": 47,
        "module": "💻 Programmation / Dev",
        "chap": "4. Multithreading C++11",
        "q": "Comment protéger une variable partagée contre les Race Conditions avec std::mutex ?",
        "a": "En utilisant un verrou RAII std::lock_guard<std::mutex> lock(mon_mutex); au début de la section critique.",
        "note": "💡 **Conseil Examen** : lock_guard verrouille le mutex au constructeur et le libère automatiquement au destructeur (fin de portée/scope).",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 3. Multithreading C++",
        "v_id": "5m9k3j4X5m0",
        "v_title": "Exclusion Mutuelle std::mutex & RAII"
    },
    {
        "id": 48,
        "module": "💻 Programmation / Dev",
        "chap": "5. Sockets Python TCP",
        "q": "Quelles sont les 5 méthodes sockets exécutées côté serveur TCP en Python ?",
        "a": "1. socket.socket() -> 2. bind((ip, port)) -> 3. listen(backlog) -> 4. accept() -> 5. recv(buffer) / sendall(data).",
        "note": "💡 **Conseil Examen** : La méthode accept() est bloquante et renvoie un tuple (conn_socket, (client_ip, client_port)).",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 4. Sockets Python",
        "v_id": "6m9k3j4X5m0",
        "v_title": "Programmation Sockets TCP en Python"
    },
    {
        "id": 49,
        "module": "💻 Programmation / Dev",
        "chap": "5. Sockets Python UDP",
        "q": "Quelles sont les méthodes sockets utilisées pour envoyer et recevoir des datagrammes UDP en Python ?",
        "a": "sendto(data, (ip, port)) pour envoyer, et recvfrom(buffer_size) pour recevoir (renvoie data et l'adresse de l'expéditeur).",
        "note": "💡 **Conseil Examen** : UDP étant sans connexion, il n'y a ni connect(), ni listen(), ni accept() !",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 4. Sockets Python",
        "v_id": "6m9k3j4X5m0",
        "v_title": "Sockets UDP Python sendto recvfrom"
    },
    {
        "id": 50,
        "module": "💻 Programmation / Dev",
        "chap": "5. Encodage & JSON",
        "q": "Comment convertir une chaîne de caractères en octets pour l'envoyer sur une socket en Python ?",
        "a": "En utilisant la méthode .encode('utf-8') (et .decode('utf-8') à la réception). Pour le JSON : json.dumps(dict) et json.loads(str).",
        "note": "💡 **Conseil Examen** : Les sockets transmettent des octets (bytes) et non des chaînes de caractères brutes (str).",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 4. Sockets Python",
        "v_id": "6m9k3j4X5m0",
        "v_title": "Encodage UTF-8 & Formats JSON Python"
    },
    {
        "id": 51,
        "module": "💻 Programmation / Dev",
        "chap": "6. Versioning Git",
        "q": "Quelles sont les commandes Git pour ajouter, valider et envoyer des modifications localement et à distance ?",
        "a": "git add . -> git commit -m msg -> git push origin main.",
        "note": "💡 **Conseil Examen** : git status permet de vérifier l'état de l'index et des fichiers modifiés à tout moment.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 5. Versioning Git",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Commandes Git Essentielles"
    },
    {
        "id": 52,
        "module": "💻 Programmation / Dev",
        "chap": "3. Surcharge & Override C++11",
        "q": "À quoi sert le mot-clé override placé en fin de déclaration de méthode en C++11 ?",
        "a": "Il indique au compilateur que la méthode redéfinit explicitement une méthode virtuelle de la classe mère, générant une erreur en cas de signature incorrecte.",
        "note": "💡 **Conseil Examen** : override évite les bogues subtils liés aux fautes de frappe dans le nom ou les arguments d'une méthode virtuelle.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Surcharge & Mot-clé override C++11"
    },
    {
        "id": 53,
        "module": "💻 Programmation / Dev",
        "chap": "2. Directives Préprocesseur C",
        "q": "À quoi servent les directives #ifndef, #define, #endif (Include Guards) dans un fichier d'en-tête .h ?",
        "a": "À éviter les inclusions multiples d'un même fichier d'en-tête lors de la compilation, prévenant les erreurs de re-déclaration.",
        "note": "💡 **Conseil Examen** : Alternative moderne : la directive préprocesseur #pragma once en tête de fichier .h.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 1. Compilateur C/C++",
        "v_id": "6m8gS-iXmXQ",
        "v_title": "Include Guards & Préprocesseur C"
    },
    {
        "id": 54,
        "module": "💻 Programmation / Dev",
        "chap": "1. Pointeurs & Références",
        "q": "Que fait l'opérateur & placé devant une variable existante en C++ ?",
        "a": "Il renvoie l'adresse mémoire de la variable (ex: int* p = &x;).",
        "note": "💡 **Conseil Examen** : Ne confondez pas l'opérateur adresse & en expression et la déclaration de référence int& ref = x;.",
        "cours_ref": "📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++",
        "v_id": "S1yR7_7bWRE",
        "v_title": "Opérateurs Pointeur et Adresse C++"
    },
    {
        "id": 55,
        "module": "🖥️ Administration Système",
        "chap": "1. Permissions Linux",
        "q": "Que signifie le masque octal 750 sur un fichier ou dossier Linux ?",
        "a": "Owner (Utilisateur) = 7 (rwx), Group (Groupe) = 5 (r-x), Others (Autres) = 0 (---).",
        "note": "💡 **Conseil Examen** : Valeurs des droits : Read r = 4, Write w = 2, Execute x = 1. 7 = 4+2+1, 5 = 4+1, 0 = 0.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "Permissions Linux chmod Octal"
    },
    {
        "id": 56,
        "module": "🖥️ Administration Système",
        "chap": "1. Permissions Linux",
        "q": "Que signifie le droit spécial SUID (4000) sur un fichier exécutable Linux ?",
        "a": "L'exécutable est lancé avec les privilèges du propriétaire du fichier (ex: root) et non de l'utilisateur qui le lance (ex: /usr/bin/passwd).",
        "note": "💡 **Conseil Examen** : En notation symbolique, le SUID apparaît sous la forme d'un s à la place du x utilisateur (ex: -rwsr-xr-x).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "Droits Spéciaux Linux : SUID, SGID, Sticky"
    },
    {
        "id": 57,
        "module": "🖥️ Administration Système",
        "chap": "1. Permissions Linux",
        "q": "À quoi sert le droit spécial SGID (2000) appliqué sur un répertoire Linux ?",
        "a": "Tous les nouveaux fichiers et dossiers créés à l'intérieur héritent automatiquement du groupe du répertoire parent.",
        "note": "💡 **Conseil Examen** : Le SGID est idéal pour configurer des dossiers de travail partagés entre plusieurs membres d'un même groupe.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "Droit SGID & Dossiers Partagés Linux"
    },
    {
        "id": 58,
        "module": "🖥️ Administration Système",
        "chap": "1. Permissions Linux",
        "q": "À quoi sert le droit spécial Sticky Bit (1000) sur un répertoire comme /tmp ?",
        "a": "Il empêche les utilisateurs de supprimer ou renommer les fichiers dont ils ne sont pas les propriétaires.",
        "note": "💡 **Conseil Examen** : En notation symbolique, le Sticky Bit s'affiche t à la place du x des autres (ex: drwxrwxrwt /tmp).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "Sticky Bit & Répertoire /tmp"
    },
    {
        "id": 59,
        "module": "🖥️ Administration Système",
        "chap": "1. Permissions Linux",
        "q": "Quelles commandes Linux permettent de lire et d'attribuer une ACL POSIX personnalisée à l'utilisateur alice ?",
        "a": "Lecture : getfacl fichier. Modification : setfacl -m u:alice:rwx fichier.",
        "note": "💡 **Conseil Examen** : L'option -m signifie modify. Pour supprimer les ACLs : setfacl -b fichier.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "ACLs Linux getfacl setfacl"
    },
    {
        "id": 60,
        "module": "🖥️ Administration Système",
        "chap": "2. Services Linux systemd",
        "q": "Quelles commandes systemctl permettent de vérifier l'état, redémarrer et activer un service au démarrage ?",
        "a": "État : systemctl status service. Redémarrer : systemctl restart service. Activer au boot : systemctl enable service.",
        "note": "💡 **Conseil Examen** : Ne confondez pas systemctl start (lance immédiatement) et systemctl enable (programme le lancement au boot).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. Services Linux systemd",
        "v_id": "2n3j4X5m-0",
        "v_title": "Gestion des Services systemd systemctl"
    },
    {
        "id": 61,
        "module": "🖥️ Administration Système",
        "chap": "2. Outils de Recherche Linux",
        "q": "Comment chercher tous les fichiers .log modifiés depuis 7 jours et contenant le mot Failed ?",
        "a": "find /var/log -name \"*.log\" -mtime -7 -exec grep -H \"Failed\" {} +.",
        "note": "💡 **Conseil Examen** : La commande grep -rnI \"motif\" /chemin cherche récursivement en ignorant les fichiers binaires.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. CLI Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "Recherche Linux find & grep"
    },
    {
        "id": 62,
        "module": "🖥️ Administration Système",
        "chap": "2. Scripting Bash",
        "q": "Que contiennent les variables spéciales 0, 0,  et -bash dans un script Bash ?",
        "a": "0 : code de retour de la dernière commande (0 = succès). 0 : nombre d'arguments.  : tous les arguments. -bash : nom du script.",
        "note": "💡 **Conseil Examen** : Testez toujours si [ 0 -eq 0 ] après une commande critique (ex: ping, rsync, compilation) pour gérer les erreurs.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. Scripting Bash",
        "v_id": "2n3j4X5m-0",
        "v_title": "Variables Spéciales Bash 0 0"
    },
    {
        "id": 63,
        "module": "🖥️ Administration Système",
        "chap": "2. Redirections Linux",
        "q": "Quelle est la différence entre les opérateurs de redirection >, >> et 2>&1 en Bash ?",
        "a": "> : écrase le fichier cible avec stdout. >> : ajoute à la fin du fichierTarget. 2>&1 : redirige stderr (canal 2) vers stdout (canal 1).",
        "note": "💡 **Conseil Examen** : Pour masquer totalement les messages d'erreur d'une commande : commande 2> /dev/null.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. CLI Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "Redirections & Pipes Linux"
    },
    {
        "id": 64,
        "module": "🖥️ Administration Système",
        "chap": "3. Active Directory",
        "q": "Quels sont les composants hiérarchiques d'un annuaire Active Directory (ADDS) ?",
        "a": "Forêt (limite de sécurité) -> Domaine -> Unités d'Organisation (OU - conteneurs pour appliquer des GPO) -> Objets (Utilisateurs, Groupes, PC).",
        "note": "💡 **Conseil Examen** : Les GPO ne s'appliquent directement qu'aux Unités d'Organisation (OU), pas aux groupes de sécurité !",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Architecture Active Directory Forêt Domaine OU"
    },
    {
        "id": 65,
        "module": "🖥️ Administration Système",
        "chap": "3. Active Directory GPO",
        "q": "Quel est l'ordre d'application des stratégies de groupe (GPO) dans Active Directory ?",
        "a": "Ordre LSDOU : 1. Local -> 2. Site -> 3. Domaine -> 4. Unité d'Organisation (OU).",
        "note": "💡 **Conseil Examen** : La règle la plus spécifique (OU) s'applique en dernier et prévaut sur les règles parentes (Domaine/Site).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory GPO",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Ordre d'Application des GPO LSDOU"
    },
    {
        "id": 66,
        "module": "🖥️ Administration Système",
        "chap": "3. Active Directory FSMO",
        "q": "Quel est le rôle FSMO chargé de la synchronisation de l'heure et de la réinitialisation des mots de passe ?",
        "a": "Le rôle FSMO PDC Emulator (Primary Domain Controller Emulator).",
        "note": "💡 **Conseil Examen** : Il existe 5 rôles FSMO dans un domaine AD (Schema Master, Domain Naming, PDC Emulator, RID Master, Infrastructure Master).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory FSMO",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Rôles FSMO Active Directory"
    },
    {
        "id": 67,
        "module": "🖥️ Administration Système",
        "chap": "3. Active Directory Services",
        "q": "Quels sont les rôles serveurs nécessaires au fonctionnement d'un domaine Active Directory ?",
        "a": "ADDS (Active Directory Domain Services) et DNS (Domain Name System). Optionnellement DHCP.",
        "note": "💡 **Conseil Examen** : Sans un DNS fonctionnel résolvant les enregistrements SRV (_ldap._tcp.dc._msdcs), les clients ne peuvent pas rejoindre le domaine.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory Services",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Services ADDS & DNS"
    },
    {
        "id": 68,
        "module": "🖥️ Administration Système",
        "chap": "3. Active Directory Kerberos",
        "q": "Comment fonctionne l'authentification Kerberos dans un domaine Active Directory ?",
        "a": "Le client s'authentifie auprès du KDC (Key Distribution Center - port 88) qui lui délivre un TGT (Ticket Granting Ticket) puis des tickets de service.",
        "note": "💡 **Conseil Examen** : Kerberos requiert une synchronisation temporelle stricte entre les ordinateurs (écart max de 5 minutes par défaut).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory Kerberos",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Authentification Kerberos Active Directory"
    },
    {
        "id": 69,
        "module": "🖥️ Administration Système",
        "chap": "3. PowerShell Active Directory",
        "q": "Quelle est la commande PowerShell pour créer un compte utilisateur dans l'OU Ingénieurs ?",
        "a": "New-ADUser -Name \"Alice Martin\" -SamAccountName \"amartin\" -UserPrincipalName \"amartin@ciel.local\" -Path \"OU=Ingenieurs,DC=ciel,DC=local\" -Enabled .",
        "note": "💡 **Conseil Examen** : N'oubliez pas le commutateur -Enabled , sinon le compte créé reste désactivé.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. PowerShell AD",
        "v_id": "8m9k3j4X5m0",
        "v_title": "PowerShell New-ADUser"
    },
    {
        "id": 70,
        "module": "🖥️ Administration Système",
        "chap": "3. PowerShell Réseau",
        "q": "Quelle commande PowerShell remplace telnet pour tester l'ouverture du port LDAPS 636 sur le serveur AD ?",
        "a": "Test-NetConnection -ComputerName \"dc1.ciel.local\" -Port 636.",
        "note": "💡 **Conseil Examen** : L'alias court est tnc dc1.ciel.local -p 636. Il renvoie TcpTestSucceeded : True.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. PowerShell Réseau",
        "v_id": "8m9k3j4X5m0",
        "v_title": "PowerShell Test-NetConnection"
    },
    {
        "id": 71,
        "module": "🖥️ Administration Système",
        "chap": "4. Virtualisation",
        "q": "Quelle est la différence entre un hyperviseur de Type 1 (Bare-Metal) et de Type 2 (Hébergé) ?",
        "a": "Type 1 : s'installe directement sur le matériel (ex: VMware ESXi, Proxmox). Type 2 : s'installe au-dessus d'un OS hôte (ex: VMware Workstation, VirtualBox).",
        "note": "💡 **Conseil Examen** : Les hyperviseurs Type 1 offrent de bien meilleures performances et sont utilisés en production industrielle.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 4. Virtualisation",
        "v_id": "rQ_1n8Y0o-0",
        "v_title": "Virtualisation Type 1 vs Type 2"
    },
    {
        "id": 72,
        "module": "🖥️ Administration Système",
        "chap": "1. Privilèges Linux Sudo",
        "q": "Quel fichier de configuration sécurisé régit les droits d'élévation de privilèges sudo et quelle commande l'édite ?",
        "a": "Le fichier /etc/sudoers, édité exclusivement avec la commande sécurisée visudo.",
        "note": "💡 **Conseil Examen** : visudo vérifie la syntaxe avant de sauvegarder, évitant de bloquer l'accès root sur le système.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Privilèges Linux",
        "v_id": "2n3j4X5m-0",
        "v_title": "Fichier sudoers & Commande visudo"
    },
    {
        "id": 73,
        "module": "🔌 Électronique & IoT",
        "chap": "1. Lois d'Électricité",
        "q": "Quelles sont les formules de la Loi d'Ohm, de la conductance G et de la Puissance Joule P ?",
        "a": "Loi d'Ohm : U = R * I. Conductance : G = 1/R (Siemens S) => I = G * U. Puissance Joule : P = U * I = R * I^2 = U^2 / R.",
        "note": "💡 **Conseil Examen** : En convention récepteur, la tension U et le courant I sont orientés en sens opposés.",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°1 Physique CIEL",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Lois d'Ohm, Conductance & Puissance Joule"
    },
    {
        "id": 74,
        "module": "🔌 Électronique & IoT",
        "chap": "1. Lois de Kirchhoff",
        "q": "Énoncez la Loi des Nœuds et la Loi des Mailles de Kirchhoff.",
        "a": "Loi des Nœuds : la somme des intensités entrantes est égale à la somme des intensités sortantes (sum I_in = sum I_out). Loi des Mailles : la somme algébrique des tensions le long d'une maille fermée est nulle (sum U = 0).",
        "note": "💡 **Conseil Examen** : Pour appliquer la loi des mailles, choisissez arbitrairement un sens de parcours et comptez positivement les tensions fléchées dans le sens du parcours.",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°1 Physique CIEL",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Lois de Kirchhoff Nœuds et Mailles"
    },
    {
        "id": 75,
        "module": "🔌 Électronique & IoT",
        "chap": "1. Pont Diviseur",
        "q": "Quelle est la formule de la tension de sortie U2 d'un pont diviseur de tension formé de R1 et R2 ?",
        "a": "U2 = E * (R2 / (R1 + R2)).",
        "note": "💡 **Conseil Examen** : Formule d'isolation de R2 si U2 et E sont connus : R2 = (U2 * R1) / (E - U2).",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°1 Physique CIEL",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Pont Diviseur de Tension"
    },
    {
        "id": 76,
        "module": "🔌 Électronique & IoT",
        "chap": "2. Pont en H",
        "q": "Quel est le rôle du pont en H (ex: BTS7960 43A) et quelle règle de sécurité est critique ?",
        "a": "Permet d'inverser le sens de rotation d'un moteur CC bipolaire. Règle critique : interdiction de fermer simultanément les interrupteurs d'une même branche (Shooting Through / court-circuit direct).",
        "note": "💡 **Conseil Examen** : Le pilotage PWM s'effectue sur les broches R_PWM / L_PWM avec les broches R_EN / L_EN à l'état HAUT (5V).",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°1 Le Pont en H",
        "v_id": "8m9k3j4X5m0",
        "v_title": "Pont en H BTS7960 & Moteur CC"
    },
    {
        "id": 77,
        "module": "🔌 Électronique & IoT",
        "chap": "3. Pull-Up / Pull-Down",
        "q": "Pourquoi utilise-t-on des résistances de Pull-Up ou Pull-Down (10 kΩ) sur les entrées numériques CMOS ?",
        "a": "Pour fixer un potentiel logique stable (HIGH ou LOW) au repos et éviter la haute impédance (état flottant / effet antenne aux parasites).",
        "note": "💡 **Conseil Examen** : Sur Arduino ATmega328P, activez la résistance de tirage interne avec pinMode(pin, INPUT_PULLUP) (niveau repos = HIGH).",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°2 Pull-Up Pull-Down",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Résistances Pull-Up & Pull-Down"
    },
    {
        "id": 78,
        "module": "🔌 Électronique & IoT",
        "chap": "4. PWM / MLI",
        "q": "Quelle est la formule du rapport cyclique alpha et de la tension moyenne V_moy d'une PWM ?",
        "a": "Rapport cyclique : alpha = t_haut / T (entre 0 et 1). Tension moyenne : V_moy = alpha * V_max = V_max * (valeur_8bits / 255).",
        "note": "💡 **Conseil Examen** : Pour analogWrite(pin, 127) sous 5V : alpha ~ 50% => V_moy = 2.5 V.",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°3 La PWM",
        "v_id": "4jS0qUfE_y4",
        "v_title": "Signal PWM MLI & Rapport Cyclique"
    },
    {
        "id": 79,
        "module": "🔌 Électronique & IoT",
        "chap": "5. Interruptions AVR",
        "q": "Comment fonctionne une interruption matérielle (ISR) et quel mot-clé qualifie une variable modifiée dans une ISR ?",
        "a": "L'ISR interrompt le programme principal, sauvegarde le contexte, s'exécute rapidement, puis reprend le programme. La variable partagée doit être déclarée volatile.",
        "note": "💡 **Conseil Examen** : Ne faites JAMAIS d'appels à delay() ou d'impressions Serial.print() à l'intérieur d'une routine d'interruption ISR !",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°4 Interruptions",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Interruptions Matérielles & Mot-clé Volatile"
    },
    {
        "id": 80,
        "module": "🔌 Électronique & IoT",
        "chap": "6. Mémoire Microcontrôleur",
        "q": "Quelles sont les 3 zones mémoires du microcontrôleur ATmega328P et leurs capacités ?",
        "a": "1. Flash (32 Ko) : code programme non-volatile. 2. SRAM (2 Ko) : variables volatiles (Pile + Tas). 3. EEPROM (1 Ko) : données permanentes non-volatiles.",
        "note": "💡 **Conseil Examen** : Pour stocker des chaînes constantes en Flash et économiser la SRAM limitée (2 Ko), utilisez la macro PROGMEM / F().",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°5 Mémoire UNO R3",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Mémoire Flash SRAM EEPROM ATmega328P"
    },
    {
        "id": 81,
        "module": "🔌 Électronique & IoT",
        "chap": "7. Capteur 4-20 mA",
        "q": "Pourquoi la boucle de courant 4-20 mA industrielle est-elle dite à sécurité Live Zero ?",
        "a": "Car un courant I = 0 mA signale immédiatement une rupture de câble ou une panne d'alimentation, contrairement au 0-20 mA où 0 mA peut être une mesure valide.",
        "note": "💡 **Conseil Examen** : Pour lire un 4-20 mA sur une entrée CAN 0-5V, insérez une résistance de précision de 250 Ω en série (U = 250 * I => 1V à 5V).",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°6 Signal 4-20 mA",
        "v_id": "9m9k3j4X5m0",
        "v_title": "Boucle de Courant 4-20 mA Industrielle"
    },
    {
        "id": 82,
        "module": "🔌 Électronique & IoT",
        "chap": "8. CAN / ADC Quantum",
        "q": "Quelle est la formule du quantum q et de la valeur numérique N restituée par un CAN n bits ?",
        "a": "Quantum : q = V_ref / (2^n - 1). Valeur entière N = arrondi(V_entrée / q).",
        "note": "💡 **Conseil Examen** : Pour un CAN 12 bits (2^12 - 1 = 4095) sous V_ref = 5.0 V : q = 5.0 / 4095 ~ 1.221 mV par LSB.",
        "cours_ref": "🧮 Laboratoire de Calculs -> Quantum CAN 10/12/16 bits",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Convertisseur Analogique Numérique CAN ADC"
    },
    {
        "id": 83,
        "module": "🔌 Électronique & IoT",
        "chap": "9. Capteurs & Métrologie",
        "q": "Quelle est la différence entre Justesse et Fidélité d'un capteur de mesure ?",
        "a": "Justesse : absence d'erreur systématique (moyenne des mesures centrée sur la valeur vraie). Fidélité : répétabilité des mesures (faible dispersion / écart-type).",
        "note": "💡 **Conseil Examen** : Précision globale = Justesse + Fidélité. La sensibilité est la pente d S / d E de la caractéristique de transfert.",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°7 Métrologie Capteurs",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Métrologie Capteurs Justesse Fidélité"
    },
    {
        "id": 84,
        "module": "🔌 Électronique & IoT",
        "chap": "10. Relais & Commande",
        "q": "Quelle composant est obligatoire en anti-parallèle sur la bobine d'un relais électromécanique ?",
        "a": "Une Diode de Roue Libre (ex: 1N4007) pour évacuer la surtension d'auto-induction (e = -L di/dt) lors de l'ouverture du transistor de commande.",
        "note": "💡 **Conseil Examen** : Un relais statique (SSR) utilise un optocoupleur et un Triac/MOSFET, offrant une commutation silencieuse sans usure mécanique.",
        "cours_ref": "📄 Fiches Savoir -> Fiche Savoir N°8 Relais",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Relais & Diode de Roue Libre"
    },
    {
        "id": 85,
        "module": "🔌 Électronique & IoT",
        "chap": "11. Bus I2C",
        "q": "Quelles sont les 2 lignes du bus I2C et comment est géré l'adressage des esclaves ?",
        "a": "SDA (Serial Data) et SCL (Serial Clock), bidirectionnelles à drain ouvert avec résistances de Pull-Up. L'adressage s'effectue sur 7 bits (128 adresses).",
        "note": "💡 **Conseil Examen** : Chaque trame I2C débute par une condition START (SDA descend quand SCL est HAUT) et se termine par STOP.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔌 Électronique -> Bus I2C",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Bus I2C SDA SCL"
    },
    {
        "id": 86,
        "module": "🔌 Électronique & IoT",
        "chap": "12. Bus SPI",
        "q": "Quelles sont les 4 lignes du bus SPI et quel est son mode de fonctionnement ?",
        "a": "MOSI (Master Out Slave In), MISO (Master In Slave Out), SCLK (Horloge), CS/SS (Chip Select). Bus synchrone Full-Duplex très rapide.",
        "note": "💡 **Conseil Examen** : La ligne CS/SS est active au niveau BAS (0V). Il faut autant de lignes CS séparées que d'esclaves SPI connectés au maître.",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔌 Électronique -> Bus SPI",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Bus SPI MOSI MISO SCLK CS"
    },
    {
        "id": 87,
        "module": "🔌 Électronique & IoT",
        "chap": "13. Bus CAN",
        "q": "Comment fonctionne la signalisation différentielle et l'arbitrage non destructif CSMA/CR du Bus CAN ?",
        "a": "Bus 2 fils CAN_H et CAN_L avec terminaisons 120 Ω. Bit dominant (0) : V_diff = 2V. Bit récessif (1) : V_diff = 0V. Le bit dominant (0) écrase le récessif (1).",
        "note": "💡 **Conseil Examen** : Lors de l'arbitrage d'identifiants, l'ID de valeur numérique la plus faible possède la priorité absolue (ex: 0x001 prioritaire sur 0x01A).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔌 Électronique -> Bus CAN",
        "v_id": "10m9k3j4X5m0",
        "v_title": "Bus CAN Differential CSMA/CR"
    },
    {
        "id": 88,
        "module": "🔌 Électronique & IoT",
        "chap": "14. Modbus RTU / RS-485",
        "q": "Quels sont les rôles des Code Fonction 03 et 16 dans le protocole Modbus RTU sur RS-485 ?",
        "a": "Code Fonction 03 (0x03) : Lecture de mots de registres (Read Holding Registers). Code Fonction 16 (0x10) : Écriture de mots multiples (Write Multiple Registers).",
        "note": "💡 **Conseil Examen** : Les trames Modbus RTU se terminent par un contrôle d'erreur de 2 octets CRC-16 (Cyclic Redundancy Check).",
        "cours_ref": "📚 Encyclopédie des Cours -> 🔌 Électronique -> Modbus RTU",
        "v_id": "11m9k3j4X5m0",
        "v_title": "Modbus RTU RS-485"
    },
    {
        "id": 89,
        "module": "🔌 Électronique & IoT",
        "chap": "1. Circuits RC",
        "q": "Quelle est la formule de la constante de temps tau d'un circuit RC et de la tension de charge u_C(t) ?",
        "a": "Tau = R * C (secondes). Charge : u_C(t) = E * (1 - e^(-t/tau)). Décharge : u_C(t) = E * e^(-t/tau).",
        "note": "💡 **Conseil Examen** : À t = tau, la charge atteint 63.2% de E. À t = 5*tau, la charge est considérée comme totale (99.3% de E).",
        "cours_ref": "📊 Mathématiques Appliquées -> Fonctions, Exponentielle & Logarithme",
        "v_id": "13m9k3j4X5m0",
        "v_title": "Circuit RC Constante de Temps Tau"
    },
    {
        "id": 90,
        "module": "🔌 Électronique & IoT",
        "chap": "1. Mesures Oscilloscope",
        "q": "Comment calculer la tension efficace V_eff et la fréquence f d'un signal sinusoïdal sur oscilloscope ?",
        "a": "V_eff = V_max / sqrt(2) ~ 0.707 * V_max. Fréquence : f = 1 / T (Hz), où T est la période mesurée sur l'axe horizontal en ms/div.",
        "note": "💡 **Conseil Examen** : N'oubliez pas que V_max = V_pp / 2 (tension crête-à-crête mesurée du bas au haut de la sinusoïde).",
        "cours_ref": "📺 Lab Oscilloscope & Mesures Physiques",
        "v_id": "7m9k3j4X5m0",
        "v_title": "Mesures Oscilloscope Vpp Veff Fréquence"
    },
    {
        "id": 91,
        "module": "📐 Modélisation UML & SysML",
        "chap": "1. Suites Arithmétiques",
        "q": "Quelles sont les formules de récurrence, explicite et de somme des termes d'une suite arithmétique ?",
        "a": "Récurrence : u_(n+1) = u_n + r. Explicite : u_n = u_0 + n * r. Somme : S_N = N * ((u_premier + u_dernier) / 2).",
        "note": "💡 **Conseil Examen** : La somme de n premiers termes de u_0 à u_(n-1) comporte exactement n termes.",
        "cours_ref": "📊 Mathématiques Appliquées -> Suites Arithmétiques",
        "v_id": "12m9k3j4X5m0",
        "v_title": "Suites Arithmétiques Formules & Somme"
    },
    {
        "id": 92,
        "module": "📐 Modélisation UML & SysML",
        "chap": "1. Suites Géométriques",
        "q": "Quelles sont les formules de récurrence, explicite et de somme des termes d'une suite géométrique ?",
        "a": "Récurrence : u_(n+1) = u_n * q. Explicite : u_n = u_0 * q^n. Somme : S_N = u_premier * ((1 - q^N) / (1 - q)) (si q != 1).",
        "note": "💡 **Conseil Examen** : Une atténuation de 15% de puissance optique correspond à une raison q = 1 - 0.15 = 0.85.",
        "cours_ref": "📊 Mathématiques Appliquées -> Suites Géométriques",
        "v_id": "12m9k3j4X5m0",
        "v_title": "Suites Géométriques Atténuation & Somme"
    },
    {
        "id": 93,
        "module": "📐 Modélisation UML & SysML",
        "chap": "1. Limites de Suites",
        "q": "Quel est le comportement à l'infini d'une suite géométrique u_n = u_0 * q^n pour u_0 > 0 ?",
        "a": "Si q > 1 : lim u_n = +infini (divergence). Si 0 < q < 1 : lim u_n = 0 (convergence vers 0 / signal éteint). Si q = 1 : constante.",
        "note": "💡 **Conseil Examen** : Si 0 < q < 1, le signal s'atténue progressivement jusqu'à devenir indétectable.",
        "cours_ref": "📊 Mathématiques Appliquées -> Limites de Suites",
        "v_id": "12m9k3j4X5m0",
        "v_title": "Limites de Suites Géométriques"
    },
    {
        "id": 94,
        "module": "📐 Modélisation UML & SysML",
        "chap": "1. Étude de Variations",
        "q": "Quelle est la méthode pour étudier le sens de variation d'une suite u_n = f(n) via la dérivée ?",
        "a": "1. Poser f(x) sur [0, +infini[. 2. Calculer f'(x). 3. Étudier le signe de f'(x). 4. Si f'(x) > 0, f est croissante donc la suite (u_n) est croissante.",
        "note": "💡 **Conseil Examen** : Le dénominateur d'une dérivée de quotient (u/v)' = (u'v - uv') / v^2 est un carré toujours strictly positif.",
        "cours_ref": "📊 Mathématiques Appliquées -> Méthode de la Dérivée",
        "v_id": "12m9k3j4X5m0",
        "v_title": "Méthode de la Dérivée u_n = f(n)"
    },
    {
        "id": 95,
        "module": "📐 Modélisation UML & SysML",
        "chap": "2. Fonctions Exp & Ln",
        "q": "Quelles sont les dérivées et propriétés algébriques remarquables des fonctions e^x et ln(x) ?",
        "a": "(e^x)' = e^x, (e^(u(x)))' = u'(x) e^(u(x)). (ln(x))' = 1/x, (ln(u(x)))' = u'(x)/u(x). ln(a * b) = ln(a) + ln(b), ln(1/a) = -ln(a).",
        "note": "💡 **Conseil Examen** : La fonction e^x est strictement positive pour tout x réel (e^x > 0). ln(x) n'est définie que pour x > 0.",
        "cours_ref": "📊 Mathématiques Appliquées -> Fonctions Exp & Ln",
        "v_id": "13m9k3j4X5m0",
        "v_title": "Fonctions Exponentielle & Logarithme Népérien"
    },
    {
        "id": 96,
        "module": "📐 Modélisation UML & SysML",
        "chap": "2. Calcul de Décibels",
        "q": "Quelles sont les formules du gain/atténuation en Décibels pour la Puissance P et la Tension V ?",
        "a": "Puissance : A_dB = 10 * log10(P2 / P1). Tension : A_v_dB = 20 * log10(V2 / V1).",
        "note": "💡 **Conseil Examen** : Une division par 2 de la puissance correspond à une atténuation de -3 dB (10 * log10(0.5) ~ -3.01 dB).",
        "cours_ref": "📊 Mathématiques Appliquées -> Calculs de Décibels",
        "v_id": "13m9k3j4X5m0",
        "v_title": "Calculs de Gain & Atténuation en Décibels"
    },
    {
        "id": 97,
        "module": "📐 Modélisation UML & SysML",
        "chap": "3. SysML BDD",
        "q": "Quel est le rôle du diagramme SysML BDD (Block Definition Diagram) ?",
        "a": "Il représente la structure globale du système, la hiérarchie des blocs, leurs compositions (black diamond) et leurs propriétés.",
        "note": "💡 **Conseil Examen** : La composition forte (losange noir) signifie que la destruction du bloc parent entraîne la destruction des sous-blocs.",
        "cours_ref": "📐 Laboratoire UML & SysML -> Diagrammes SysML",
        "v_id": "14m9k3j4X5m0",
        "v_title": "Diagramme SysML BDD Structure Globale"
    },
    {
        "id": 98,
        "module": "📐 Modélisation UML & SysML",
        "chap": "3. SysML IBD",
        "q": "À quoi sert le diagramme SysML IBD (Internal Block Diagram) et que représentent ses Flow Ports ?",
        "a": "Il décrit l'assemblage interne d'un bloc, les liaisons entre sous-composants via des ports d'interfaçage physiques ou de flux de données (Flow Ports).",
        "note": "💡 **Conseil Examen** : Les flèches sur les Flow Ports indiquent la direction des flux de données (in, out, inout).",
        "cours_ref": "📐 Laboratoire UML & SysML -> Diagrammes SysML",
        "v_id": "14m9k3j4X5m0",
        "v_title": "Diagramme SysML IBD Flow Ports"
    },
    {
        "id": 99,
        "module": "📐 Modélisation UML & SysML",
        "chap": "3. SysML Requirement",
        "q": "Quelles sont les deux relations clés dans un diagramme SysML Requirement Diagram ?",
        "a": "deriveReqt (une exigence dérive d'une autre) et verify (un cas de test ou sous-système vérifie qu'une exigence est satisfaite).",
        "note": "💡 **Conseil Examen** : Chaque exigence possède un identifiant unique (Id) et un texte de critère de satisfaction.",
        "cours_ref": "📐 Laboratoire UML & SysML -> Diagrammes SysML",
        "v_id": "14m9k3j4X5m0",
        "v_title": "Requirement Diagram & Traçabilité"
    },
    {
        "id": 100,
        "module": "📐 Modélisation UML & SysML",
        "chap": "4. UML Diagramme de Classes",
        "q": "Quelle est la différence entre une Agrégation (losange blanc) et une Composition (losange noir) en UML ?",
        "a": "Agrégation (losange blanc) : relation faible, l'élément contenu peut exister indépendamment. Composition (losange noir) : relation forte, cycle de vie lié.",
        "note": "💡 **Conseil Examen** : La multiplicité 1..* indique un-à-plusieurs, 0..1 indique optionnel.",
        "cours_ref": "📐 Laboratoire UML & SysML -> Diagrammes UML",
        "v_id": "15m9k3j4X5m0",
        "v_title": "Diagramme de Classes UML Associations"
    },
    {
        "id": 101,
        "module": "📐 Modélisation UML & SysML",
        "chap": "4. UML Diagramme de Séquence",
        "q": "Que représentent les fragments alt et loop dans un diagramme de séquence UML ?",
        "a": "alt : bloc conditionnel (alternative Si / Sinon). loop : boucle d'itération répétitive (Tant que / Pour).",
        "note": "💡 **Conseil Examen** : Les lignes verticales représentent la ligne de vie des objets. Les flèches pleines sont synchrones, flèches ouvertes asynchrones.",
        "cours_ref": "📐 Laboratoire UML & SysML -> Diagrammes UML",
        "v_id": "15m9k3j4X5m0",
        "v_title": "Diagramme de Séquence UML Fragments"
    },
    {
        "id": 102,
        "module": "📐 Modélisation UML & SysML",
        "chap": "4. UML États-Transitions",
        "q": "Quels sont les éléments constituants d'une transition dans un diagramme d'États-Transitions UML ?",
        "a": "Événement déclencheur [ Condition de garde ] / Action exécutée (ex: boutonAppuye [ tension > 3.3V ] / allumerLED()).",
        "note": "💡 **Conseil Examen** : La condition de garde [ ] est une condition booléenne qui doit être VRAIE pour que la transition franchisse l'état.",
        "cours_ref": "📐 Laboratoire UML & SysML -> Diagrammes UML",
        "v_id": "15m9k3j4X5m0",
        "v_title": "Diagramme d'États-Transitions UML"
    },
    {
        "id": 103,
        "module": "📐 Modélisation UML & SysML",
        "chap": "5. Qualification E6 & PVL",
        "q": "Qu'est-ce qu'un Plan de Validation Logicielle (PVL) pour l'épreuve du Projet E6 ?",
        "a": "Un document formalisant la matrice de traçabilité des exigences, décrivant la procédure de test, le résultat attendu et le statut (PASS / FAIL).",
        "note": "💡 **Conseil Examen** : Chaque test du PVL doit être directement associé à une exigence du Cahier des Charges Fonctionnel (CdCf).",
        "cours_ref": "🧪 Qualification & Tests E6",
        "v_id": "16m9k3j4X5m0",
        "v_title": "Plan de Validation Logicielle PVL E6"
    },
    {
        "id": 104,
        "module": "📐 Modélisation UML & SysML",
        "chap": "5. Tests Automated Pytest",
        "q": "Comment rédiger une fonction de test automatisée sous Python avec le framework pytest ?",
        "a": "def test_calcul_quantum(): assert calcul_quantum(5.0, 12) == pytest.approx(0.001221, rel=1e-3)",
        "note": "💡 **Conseil Examen** : Les fonctions de test doivent impérativement commencer par le mot-clé test_ pour être détectées par pytest.",
        "cours_ref": "🧪 Qualification & Tests E6 -> Framework Pytest",
        "v_id": "16m9k3j4X5m0",
        "v_title": "Tests Unitaires & Automatisés Pytest"
    },
    {
        "id": 105,
        "module": "📐 Modélisation UML & SysML",
        "chap": "5. Gestion de Projet Gantt",
        "q": "Qu'est-ce que le Chemin Critique dans le suivi de projet E6 (Diagramme de Gantt) ?",
        "a": "La séquence de tâches sans aucune marge. Tout retard sur une tâche du chemin critique décale la date de fin globale du projet.",
        "note": "💡 **Conseil Examen** : Identifiez les tâches jalons (Milestones) de durée nulle marquant la fin des phases clés (ex: Validation du PVL).",
        "cours_ref": "📋 Planning de Projet E6 (Gantt)",
        "v_id": "16m9k3j4X5m0",
        "v_title": "Diagramme de Gantt & Chemin Critique E6"
    }
]

GRAND_QUIZ_DATA = [   {   'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)',
        'expl': 'Pour faire 4 sous-réseaux (2^2), il faut emprunter 2 bits au '
                'masque /24, ce qui donne un masque /26, soit 255.255.255.192.',
        'mod': '📶 Réseaux & Télécoms',
        'options': [   '255.255.255.128 (/25)',
                       '255.255.255.192 (/26)',
                       '255.255.255.224 (/27)',
                       '255.255.255.240 (/28)'],
        'q': 'Q1 : Vous disposez du réseau 192.168.10.0/24. Vous devez créer 4 '
             'sous-réseaux de taille égale. Quel sera le nouveau masque ?',
        'rep': '255.255.255.192 (/26)'},
    {   'chap': '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN',
        'expl': 'Sur une sous-interface de routeur (ex: g0/0.10), on configure '
                "l'encapsulation de type trunking à l'aide de la commande "
                "'encapsulation dot1Q 10' où 10 est l'ID du VLAN.",
        'mod': '📶 Réseaux & Télécoms',
        'options': [   'switchport access vlan 10',
                       'encapsulation dot1Q 10',
                       'trunk allowed vlan 10',
                       'ip route vlan 10'],
        'q': "Q2 : Quelle commande Cisco IOS permet d'activer le routage "
             'inter-VLAN sur une sous-interface de routeur en spécifiant '
             "l'encapsulation 802.1Q pour le VLAN 10 ?",
        'rep': 'encapsulation dot1Q 10'},
    {   'chap': '1. Langage C++ : Mémoire, Pointeurs & POO',
        'expl': 'Une classe comportant au moins une méthode virtuelle pure '
                '(déclarée avec = 0) est appelée classe de base abstraite. '
                'Elle ne peut pas être instanciée.',
        'mod': '💻 Programmation / Dev',
        'options': [   'Une classe scellée (sealed)',
                       'Une interface statique',
                       'Une classe de base abstraite',
                       'Une classe dérivée'],
        'q': 'Q3 : En C++, si une classe B hérite publiquement de la classe A, '
             'et que la classe A possède au moins une méthode virtuelle pure, '
             'comment qualifie-t-on la classe A ?',
        'rep': 'Une classe de base abstraite'},
    {   'chap': '1. Permissions GNU/Linux & Services système',
        'expl': "'u+x' signifie User + eXecution (droit d'exécution pour le "
                "propriétaire). 'g-w' signifie Group - Write (retrait du droit "
                "d'écriture pour le groupe).",
        'mod': '🖥️ Administration Système',
        'options': [   "Ajoute le droit d'exécution au propriétaire et retire "
                       "le droit d'écriture au groupe",
                       "Ajoute l'écriture pour l'utilisateur et retire "
                       "l'exécution pour le groupe",
                       'Donne tous les droits au propriétaire et supprime les '
                       'droits du groupe',
                       'Rend le fichier exécutable par tout le monde'],
        'q': "Q4 : Quel est l'effet de la commande Linux 'chmod u+x,g-w "
             "script.sh' ?",
        'rep': "Ajoute le droit d'exécution au propriétaire et retire le droit "
               "d'écriture au groupe"},
    {   'chap': '1. Échantillonnage, CAN/CNA & Théorème de Shannon',
        'expl': 'q = 5 / (2^12 - 1) = 5 / 4095 = 0.001221 V. N = arrondi(3.12 '
                '/ 0.001221) = 2555. (Sujet officiel BTS CIEL 2025).',
        'mod': '🔌 Électronique & IoT',
        'options': ['2048', '2555', '2560', '3120'],
        'q': 'Q5 : Un convertisseur analogique-numérique (CAN) possède une '
             "résolution de 12 bits et une plage d'entrée de 0 à 5V. Quelle "
             'est la valeur numérique entière générée pour une tension de '
             '3.12V ?',
        'rep': '2555'},
    {   'chap': '1. Modèle OSI vs TCP/IP & Encapsulation',
        'expl': 'IPsec opère au niveau de la couche Réseau (couche 3) pour '
                "chiffrer et encapsuler l'intégralité du trafic entre deux "
                'passerelles réseau.',
        'mod': '📶 Réseaux & Télécoms',
        'options': ['TLS/SSL', 'IPsec', 'HTTPS', 'WPA3'],
        'q': 'Q6 : Quel protocole de sécurisation réseau fournit une '
             'authentification et un chiffrement robustes au niveau de la '
             'couche réseau (Couche 3 du modèle OSI) ?',
        'rep': 'IPsec'},
    {   'chap': '2. Services Active Directory & GPO (Windows Server)',
        'expl': "Les stratégies de groupe (GPO) permettent d'appliquer de "
                'façon centralisée des configurations de sécurité et des '
                'environnements aux postes de travail.',
        'mod': '🖥️ Administration Système',
        'options': [   'Enregistrements DNS',
                       'Base SAM locale',
                       'GPO (Group Policy Object)',
                       'Serveur DHCP'],
        'q': "Q7 : Quel composant Active Directory gère l'application "
             'centralisée de stratégies de groupe sur les ordinateurs du '
             'domaine ?',
        'rep': 'GPO (Group Policy Object)'},
    {   'chap': '2. Protocoles IoT (MQTT & LoRaWAN)',
        'expl': 'LoRaWAN est conçu pour transmettre de petits volumes de '
                "données sur des distances kilométriques à partir d'objets "
                'alimentés sur piles.',
        'mod': '🔌 Électronique & IoT',
        'options': ['Wi-Fi 6', 'LoRaWAN', 'WebSockets', 'HTTP REST'],
        'q': 'Q8 : Quel protocole IoT est particulièrement optimisé pour la '
             'communication longue portée (LPWAN) avec une consommation '
             'ultra-faible ?',
        'rep': 'LoRaWAN'},
    {   'chap': '2. Scripting & Automatisation en Python (Réseaux)',
        'expl': 'La commande \'git commit -m "message"\' crée un point de '
                'sauvegarde local de vos modifications indexées dans '
                "l'historique du dépôt.",
        'mod': '💻 Programmation / Dev',
        'options': ['git push', 'git save', 'git commit', 'git checkout'],
        'q': "Q9 : Dans Git, quelle commande permet d'enregistrer localement "
             'vos modifications indexées en y associant un message explicatif '
             '?',
        'rep': 'git commit'},
    {   'chap': '2. Diagrammes SysML (BDD, IBD, Exigences)',
        'expl': "L'IBD (Internal Block Diagram) représente l'agencement "
                "interne et les flux de matière, d'énergie ou de données "
                "reliant les ports d'un bloc.",
        'mod': '📐 Modélisation UML & SysML',
        'options': [   'BDD (Block Definition Diagram)',
                       'IBD (Internal Block Diagram)',
                       'Requirement Diagram',
                       'Use Case Diagram'],
        'q': 'Q10 : En SysML, quel diagramme permet de modéliser les flux '
             'internes (matière, énergie, données) entre les ports des blocs ?',
        'rep': 'IBD (Internal Block Diagram)'},
    {   'chap': '5. Modulations & Transmissions de Signaux (FSK, ASK, PSK, '
                'QAM)',
        'expl': 'Une modulation 16-QAM code n = log2(16) = 4 bits par symbole. '
                'Le débit binaire est D = R * n. Donc R = D / n = 9600 / 4 = '
                '2400 Bauds.',
        'mod': '📶 Réseaux & Télécoms',
        'options': ['2400 Bauds', '4800 Bauds', '9600 Bauds', '19200 Bauds'],
        'q': 'Q11 : Quelle est la rapidité de modulation minimale (en Bauds) '
             'pour transmettre un débit binaire de 9600 bps avec une '
             'modulation 16-QAM ?',
        'rep': '2400 Bauds'},
    {   'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)',
        'expl': "Le protocole NDP (Neighbor Discovery Protocol) s'appuie sur "
                "ICMPv6 pour réaliser la découverte d'adresse physique (ARP en "
                "IPv4), la détection d'adresses dupliquées, et la découverte "
                'de routeurs (SLAAC).',
        'mod': '📶 Réseaux & Télécoms',
        'options': [   'ICMPv4',
                       'NDP (Neighbor Discovery Protocol)',
                       'DHCPv6',
                       'SNDP'],
        'q': "Q12 : Quel protocole de l'architecture IPv6 prend en charge la "
             "découverte des voisins et l'auto-configuration SLAAC, remplaçant "
             'le protocole ARP ?',
        'rep': 'NDP (Neighbor Discovery Protocol)'},
    {   'chap': '3. Durcissement & Filtrage : Pare-feux (Linux) & Port '
                'Security',
        'expl': "Le mode 'protect' rejette silencieusement le trafic suspect "
                "sans bloquer l'interface et sans incrémenter le compteur de "
                "violation, à l'inverse du mode 'restrict' qui l'incrémente.",
        'mod': '🔒 Cybersécurité',
        'options': [   'switchport port-security violation shutdown',
                       'switchport port-security violation restrict',
                       'switchport port-security violation protect',
                       'switchport port-security violation disable'],
        'q': 'Q13 : Dans un commutateur Cisco, comment configure-t-on le Port '
             'Security pour rejeter silencieusement le trafic suspect en cas '
             "d'intrusion, sans désactiver l'interface ?",
        'rep': 'switchport port-security violation protect'},
    {   'chap': '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)',
        'expl': "La poignée de main TLS commence par le 'Client Hello' "
                "(propositions d'algorithmes), suivi du 'Server Hello' (choix "
                "d'algorithme), de l'envoi des certificats par le serveur, de "
                "l'échange de clés (Key Exchange) et de la validation finale "
                "('Finished').",
        'mod': '🔒 Cybersécurité',
        'options': [   'Client Hello -> Server Hello -> Exchange Certificates '
                       '-> Key Exchange -> Finished',
                       'Server Hello -> Client Hello -> Exchange Certificates '
                       '-> Finished',
                       'Exchange Certificates -> Client Hello -> Server Hello '
                       '-> Finished',
                       'Client Hello -> Exchange Certificates -> finished'],
        'q': "Q14 : Quel est l'ordre des messages échangés lors de la poignée "
             "de main TLS (TLS Handshake) au début d'une connexion HTTPS ?",
        'rep': 'Client Hello -> Server Hello -> Exchange Certificates -> Key '
               'Exchange -> Finished'},
    {   'chap': '3. Threads, Mutex & Sockets Multi-Client (C++11)',
        'expl': 'std::lock_guard utilise le principe RAII. Si une fonction '
                'lève une exception ou se termine prématurément par un '
                "'return', le destructeur de std::lock_guard est invoqué et le "
                'mutex est libéré, évitant un interblocage permanent '
                '(Deadlock).',
        'mod': '💻 Programmation / Dev',
        'options': [   'Il permet de verrouiller plusieurs mutex simultanément '
                       'de manière statique',
                       'Il garantit le déverrouillage automatique en fin de '
                       'bloc, même si une exception est levée',
                       "Il est plus rapide à l'exécution de 50%",
                       'Il supprime automatiquement les conditions de '
                       'concurrence'],
        'q': "Q15 : En C++, quel est le principal avantage de l'utilisation de "
             "'std::lock_guard' par rapport à l'appel direct de '.lock()' et "
             "'.unlock()' sur un mutex ?",
        'rep': 'Il garantit le déverrouillage automatique en fin de bloc, même '
               'si une exception est levée'},
    {   'chap': '2. Scripting & Automatisation en Python (Réseaux)',
        'expl': "La méthode 'accept()' est bloquante. Dès qu'un client se "
                'connecte, elle renvoie une nouvelle socket dédiée à la '
                "communication avec ce client, ainsi qu'un tuple contenant son "
                'adresse IP et son port.',
        'mod': '💻 Programmation / Dev',
        'options': ['bind()', 'listen()', 'connect()', 'accept()'],
        'q': "Q16 : Quelle méthode de la bibliothèque 'socket' en Python "
             "bloque l'exécution du serveur et attend la connexion d'un client "
             'distant ?',
        'rep': 'accept()'},
    {   'chap': '3. Gestion Avancée Linux & Sécurisation (ACLs, SUID/SGID, '
                'umask)',
        'expl': "La commande 'umask 002' soustrait le bit d'écriture aux "
                "Autres (Others) lors de la création d'un fichier (666 - 002 = "
                "664) ou d'un dossier (777 - 002 = 775).",
        'mod': '🖥️ Administration Système',
        'options': [   'chmod 775',
                       'umask 002',
                       'setfacl -m umask:002',
                       'chown 002'],
        'q': 'Q17 : Sous Linux, comment définit-on un umask égal à 002 pour '
             "s'assurer que les nouveaux répertoires de projet soient créés "
             'par défaut avec les droits 775 (rwxrwxr-x) ?',
        'rep': 'umask 002'},
    {   'chap': '4. Bus Réseau Industriel CAN (Controller Area Network)',
        'expl': "Le bus CAN utilise le protocole CSMA/CR. Lorsqu'un bit "
                "dominant (0) est émis en même temps qu'un bit récessif (1), "
                "l'état dominant (0) l'emporte physiquement sur la ligne. Le "
                'nœud émettant le bit récessif détecte cette différence et '
                "s'arrête instantanément de transmettre.",
        'mod': '🔌 Électronique & IoT',
        'options': [   'Le protocole CSMA/CD basé sur la détection de '
                       'collision physique',
                       "L'identifiant de la trame et la priorité des bits "
                       'dominants (0) sur les bits récessifs (1)',
                       "Un jeton d'émission circulant d'un contrôleur à "
                       "l'autre",
                       "Le signal d'horloge commun SCL"],
        'q': 'Q18 : Sur le bus réseau de communication CAN, quel élément '
             "garantit l'arbitrage non destructif et instantané lorsque deux "
             'nœuds transmettent au même moment ?',
        'rep': "L'identifiant de la trame et la priorité des bits dominants "
               '(0) sur les bits récessifs (1)'},
    {   'chap': '1. Modélisation Logicielle UML (Classes, Séquence, Cas '
                "d'Utilisation)",
        'expl': "En diagramme de classes UML, l'agrégation se dessine avec un "
                "losange vide ◇ à l'extrémité du contenant, tandis que la "
                'composition se dessine avec un losange plein ◆.',
        'mod': '📐 Modélisation UML & SysML',
        'options': [   'Agrégation = Losange vide ◇ | Composition = Losange '
                       'plein ◆',
                       'Agrégation = Losange plein ◆ | Composition = Losange '
                       'vide ◇',
                       'Agrégation = Flèche simple -> | Composition = Flèche '
                       'double =>',
                       'Agrégation = Ligne pointillée | Composition = Ligne '
                       'continue'],
        'q': 'Q19 : En UML, comment représente-t-on graphiquement une relation '
             "d'agrégation simple par rapport à une relation de composition ?",
        'rep': 'Agrégation = Losange vide ◇ | Composition = Losange plein ◆'},
    {   'chap': "3. Diagramme d'États-Transitions UML",
        'expl': 'Le diagramme de machine à états (State Machine) modélise le '
                "cycle de vie réactif d'un objet, en décrivant ses états, ses "
                "transitions et ses actions d'états (entry, do, exit).",
        'mod': '📐 Modélisation UML & SysML',
        'options': [   'Le diagramme de séquence',
                       "Le diagramme de cas d'utilisation",
                       'Le diagramme de machine à états',
                       "Le diagramme d'activité"],
        'q': "Q20 : Quel diagramme d'États-Transitions UML permet de modéliser "
             "le comportement réactif d'un objet en définissant des actions à "
             "l'entrée et à la sortie d'un état ?",
        'rep': 'Le diagramme de machine à états'},
    {   'chap': '1. Modèle OSI vs TCP/IP & Encapsulation',
        'expl': 'OSPF (Open Shortest Path First) est un protocole de routage '
                'dynamique interne à état de lien (Link-State) qui utilise '
                "l'algorithme de Dijkstra pour calculer le chemin le plus "
                'court.',
        'mod': '📶 Réseaux & Télécoms',
        'options': ['RIP', 'BGP', 'OSPF', 'EIGRP'],
        'q': 'Q21 : Quel est le protocole de routage dynamique interne de type '
             "'État de lien' le plus utilisé, fonctionnant avec le découpage "
             'de zones (Areas) ?',
        'rep': 'OSPF'},
    {   'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)',
        'expl': 'Pour /28, la taille de sous-réseau est de 16 IP. Les '
                'sous-réseaux commencent à 172.16.50.0, .16, .32, .48, etc. '
                "L'IP .40 est dans le sous-réseau .32. L'adresse réseau est "
                ".32, et la première IP d'hôte utilisable est .33.",
        'mod': '📶 Réseaux & Télécoms',
        'options': [   '172.16.50.32',
                       '172.16.50.33',
                       '172.16.50.41',
                       '172.16.50.1'],
        'q': 'Q22 : En adressage IPv4, quelle est la première adresse IP '
             "d'hôte utilisable pour le sous-réseau contenant l'hôte "
             '172.16.50.40/28 ?',
        'rep': '172.16.50.33'},
    {   'chap': '1. Cryptographie : Symétrique, Asymétrique & Hachage',
        'expl': "L'autorité de certification est un tiers de confiance qui "
                "valide l'identité du possesseur du certificat en le signant "
                "avec sa propre clé privée, permettant l'utilisation de HTTPS "
                'en toute confiance.',
        'mod': '🔒 Cybersécurité',
        'options': [   'Chiffrer les requêtes de base de données à la volée',
                       'Générer et signer numériquement des certificats X.509 '
                       'pour lier une clé publique à une identité',
                       'Bloquer les attaques par déni de service distribué '
                       '(DDoS)',
                       'Détecter les intrusions physiques sur les commutateurs '
                       'Cisco'],
        'q': "Q23 : En cybersécurité, quelle est la principale fonction d'une "
             'autorité de certification (CA) ?',
        'rep': 'Générer et signer numériquement des certificats X.509 pour '
               'lier une clé publique à une identité'},
    {   'chap': '3. Gestion Avancée Linux & Sécurisation (ACLs, SUID/SGID, '
                'umask)',
        'expl': "La commande 'getfacl' permet d'afficher les permissions "
                'étendues (ACLs) configurées sur un fichier ou un répertoire '
                'Linux.',
        'mod': '🖥️ Administration Système',
        'options': ['ls -la', 'getfacl', 'setfacl -l', 'acl-list'],
        'q': 'Q24 : Quelle commande Linux permet de lister de manière '
             "détaillée les listes de contrôle d'accès (ACL) configurées sur "
             'un dossier spécifique ?',
        'rep': 'getfacl'},
    {   'chap': '1. Langage C++ : Mémoire, Pointeurs & POO',
        'expl': 'RAII est le paradigme fondamental en C++. Les classes '
                'encapsulent la gestion des ressources dans leur constructeur '
                'et leur destructeur (comme std::lock_guard ou '
                'std::unique_ptr), rendant la gestion de ressources '
                'automatique et sûre.',
        'mod': '💻 Programmation / Dev',
        'options': [   "L'héritage virtuel",
                       'Le patron de conception (design pattern)',
                       'Le RAII (Resource Acquisition Is Initialization)',
                       'Le polymorphisme dynamique'],
        'q': "Q25 : En C++, comment s'appelle le mécanisme qui permet de "
             "s'assurer qu'une ressource (comme de la mémoire ou un verrou) "
             "est acquise lors de l'instanciation d'un objet et libérée "
             'automatiquement lors de sa destruction ?',
        'rep': 'Le RAII (Resource Acquisition Is Initialization)'},
    {   'chap': '2. Protocoles IoT (MQTT & LoRaWAN)',
        'expl': 'MQTT est le standard de fait en IoT industriel pour '
                'transmettre de manière asynchrone des télémétries à un Broker '
                'via un modèle Publish/Subscribe.',
        'mod': '🔌 Électronique & IoT',
        'options': ['HTTP REST', 'FTP', 'MQTT', 'SNMP'],
        'q': "Q26 : Dans un projet d'examen E6, quel protocole est typiquement "
             'utilisé pour transmettre de manière fiable et périodique des '
             'mesures de capteurs IoT à travers une passerelle via des Topics '
             '?',
        'rep': 'MQTT'},
    {   'chap': '3. Bus de Communication Série (I2C, SPI, UART)',
        'expl': "C'est toujours le maître qui prend l'initiative de la "
                "communication et génère le signal d'horloge de "
                'synchronisation SCL.',
        'mod': '🔌 Électronique & IoT',
        'options': [   'Le circuit de tirage (Pull-up)',
                       'Le composant maître (Master)',
                       "N'importe quel esclave actif",
                       'Le courtier réseau'],
        'q': 'Q27 : Sur un bus de communication I2C, quel est le composant '
             "responsable de générer l'horloge SCL servant de cadencement ?",
        'rep': 'Le composant maître (Master)'},
    {   'chap': '2. Diagrammes SysML (BDD, IBD, Exigences)',
        'expl': "Le BDD (Block Definition Diagram) permet d'avoir une vision "
                'globale statique de la structure du système, équivalent SysML '
                'du diagramme de classes UML.',
        'mod': '📐 Modélisation UML & SysML',
        'options': [   "Le diagramme d'exigences (RD)",
                       'Le diagramme de définition de bloc (BDD)',
                       "Le diagramme de cas d'utilisation (UCD)",
                       'Le diagramme de séquence (SD)'],
        'q': 'Q28 : Quel diagramme SysML modélise le découpage hiérarchique et '
             'les relations structurelles globales (physiques ou logiques) '
             "entre les blocs d'un système ?",
        'rep': 'Le diagramme de définition de bloc (BDD)'},
    {   'chap': '3. Threads, Mutex & Sockets Multi-Client (C++11)',
        'expl': "std::thread est l'objet natif en C++11 pour créer et démarrer "
                "un nouveau thread d'exécution parallèle au sein d'un "
                'processus.',
        'mod': '💻 Programmation / Dev',
        'options': [   'std::thread',
                       'std::mutex',
                       'std::fork',
                       'std::async_task'],
        'q': "Q29 : En C++11, quelle classe permet d'instancier et de démarrer "
             "l'exécution parallèle d'une fonction dans un fil d'exécution "
             'séparé ?',
        'rep': 'std::thread'},
    {   'chap': '2. Services Active Directory & GPO (Windows Server)',
        'expl': "Active Directory s'appuie obligatoirement sur un serveur DNS "
                '(souvent hébergé directement sur le DC) pour stocker les '
                'enregistrements de service de domaine (SRV).',
        'mod': '🖥️ Administration Système',
        'options': [   'Le service WINS',
                       'Le service DNS',
                       'Le service DHCP',
                       'Le service IIS'],
        'q': 'Q30 : Dans Active Directory, quel service réseau indispensable '
             "s'occupe de traduire les requêtes de résolution de noms de "
             'domaine des contrôleurs de domaine (DC) ?',
        'rep': 'Le service DNS'},
    {   'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)',
        'expl': "Un /28 offre 16 adresses IP au total. Moins l'adresse réseau "
                "et l'adresse de broadcast, il reste 14 adresses d'hôtes "
                "utilisables. C'est le dimensionnement exact.",
        'mod': '📶 Réseaux & Télécoms',
        'options': ['/26', '/27', '/28', '/29'],
        'q': "Q31 : Dans le sujet d'examen officiel BTS CIEL 2024, quel masque "
             'de sous-réseau CIDR est préconisé pour un réseau de 14 hôtes '
             'utiles au maximum ?',
        'rep': '/28'},
    {   'chap': '2. Top 10 OWASP & Sécurité Applicative',
        'expl': "Le CSRF consiste à usurper l'identité d'un utilisateur "
                'connecté en transmettant des requêtes malveillantes à son '
                "insu via son propre navigateur vers un site qu'il a déjà "
                'authentifié.',
        'mod': '🔒 Cybersécurité',
        'options': [   'CSRF (Cross-Site Request Forgery)',
                       'Injection SQL',
                       'XSS (Cross-Site Scripting)',
                       'Broken Authentication'],
        'q': 'Q32 : Quelle vulnérabilité web critique (Top 10 OWASP) permet à '
             "un attaquant de forcer le navigateur d'une victime authentifiée "
             'à exécuter des actions non souhaitées sur un site tiers ?',
        'rep': 'CSRF (Cross-Site Request Forgery)'},
    {   'chap': '3. Gestion Avancée Linux & Sécurisation (ACLs, SUID/SGID, '
                'umask)',
        'expl': "L'ajout du SUID s'effectue via 'chmod u+s' (ou au format "
                'octal chmod 4755, où le 4 active le SUID).',
        'mod': '🖥️ Administration Système',
        'options': [   'chmod u+s <programme>',
                       'chmod 777 <programme>',
                       'chmod +x <programme>',
                       'chown root <programme>'],
        'q': "Q33 : Quelle commande Linux permet d'accorder le droit "
             "d'exécution temporaire avec les privilèges de son propriétaire "
             '(SUID) à un programme exécutable ?',
        'rep': 'chmod u+s <programme>'},
    {   'chap': '1. Échantillonnage, CAN/CNA & Théorème de Shannon',
        'expl': 'La fréquence maximale du signal est Fmax = 12 kHz. Selon '
                'Shannon, Fe >= 2 * Fmax = 2 * 12 kHz = 24 kHz.',
        'mod': '🔌 Électronique & IoT',
        'options': ['12 kHz', '24 kHz', '24.2 kHz', '48 kHz'],
        'q': "Q34 : Quelle est la fréquence d'échantillonnage minimale requise "
             'pour numériser un signal analogique dont la bande passante '
             "s'étend de 100 Hz à 12 kHz sans subir de repliement de spectre ?",
        'rep': '24 kHz'},
    {   'chap': '1. Modélisation Logicielle UML (Classes, Séquence, Cas '
                "d'Utilisation)",
        'expl': 'Le diagramme de séquence est un diagramme dynamique temporel '
                'décrivant la chronologie des échanges de messages entre '
                'lignes de vie.',
        'mod': '📐 Modélisation UML & SysML',
        'options': [   'Diagramme de classes',
                       "Diagramme de cas d'utilisation",
                       'Diagramme de séquence',
                       "Diagramme d'activité"],
        'q': "Q35 : En UML, comment s'appelle le diagramme comportemental "
             "décrivant l'enchaînement chronologique des interactions entre "
             "acteurs et objets à l'aide de lignes de vie ?",
        'rep': 'Diagramme de séquence'},
    {   'chap': '1. Modélisation Logicielle UML (Classes, Séquence, Cas '
                "d'Utilisation)",
        'expl': 'Les tests de non-régression consistent à rejouer le plan de '
                "test suite à des modifications pour s'assurer que les "
                "fonctionnalités stables antérieures n'ont pas subi "
                "d'altérations.",
        'mod': '📐 Modélisation UML & SysML',
        'options': [   'Les tests unitaires',
                       "Les tests d'intégration",
                       'Les tests de régression (ou non-régression)',
                       'Les tests de boîte blanche'],
        'q': "Q36 : Dans un projet d'examen E6, quelle section du Plan de "
             "Validation Logicielle (PVL) s'assure que les modifications "
             "apportées à un module n'ont pas introduit d'effets de bord "
             'négatifs sur les modules existants ?',
        'rep': 'Les tests de régression (ou non-régression)'},
    {   'chap': '4. Bus Réseau Industriel CAN (Controller Area Network)',
        'expl': "À l'état récessif (bit 1), les fils CAN_H et CAN_L sont tous "
                "deux maintenus à une tension moyenne d'environ 2.5V, la "
                'tension différentielle mesurée est nulle ($V_{diff} = 0\t'
                '\text{V}$).',
        'mod': '🔌 Électronique & IoT',
        'options': [   'CAN_H = 3.5V et CAN_L = 1.5V (Vdiff = 2.0V)',
                       'CAN_H = 2.5V et CAN_L = 2.5V (Vdiff = 0V)',
                       'CAN_H = 5.0V et CAN_L = 0V (Vdiff = 5.0V)',
                       'CAN_H = 0V et CAN_L = 5.0V'],
        'q': 'Q37 : Sur un bus différentiel CAN, quel état physique des '
             'tensions sur les fils correspond à un bit récessif (Logique 1) ?',
        'rep': 'CAN_H = 2.5V et CAN_L = 2.5V (Vdiff = 0V)'},
    {   'chap': '1. Permissions GNU/Linux & Services système',
        'expl': "En Bash Linux, la variable '$?' contient le statut de sortie "
                'de la dernière commande. Un code de 0 indique un succès, et '
                'un code supérieur à 0 indique une erreur.',
        'mod': '🖥️ Administration Système',
        'options': ['$?', '$#', '$$', '$*'],
        'q': "Q38 : Dans un script d'administration Linux, quelle variable "
             "spéciale renvoie le code de retour d'erreur de la dernière "
             'commande exécutée en console ?',
        'rep': '$?'},
    {   'chap': '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)',
        'expl': 'HTTPS est le protocole de navigation Web sécurisé. Il '
                "encapsule le protocole HTTP classique au sein d'une session "
                'de chiffrement TLS de couche Transport/Application.',
        'mod': '🔒 Cybersécurité',
        'options': ["HTTPS (s'appuyant sur TLS)", 'IPsec', 'WPA3', 'SSHv2'],
        'q': 'Q39 : Quel protocole sécurisé opère au niveau de la couche '
             'Application (Port TCP 443) pour négocier des connexions Web '
             'chiffrées ?',
        'rep': "HTTPS (s'appuyant sur TLS)"},
    {   'chap': '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN',
        'expl': 'Par convention sous la norme IEEE 802.1Q, les trames '
                'appartenant au VLAN natif (souvent le VLAN 1 par défaut) '
                'traversent les liens Trunk sans recevoir de tag '
                "d'identification.",
        'mod': '📶 Réseaux & Télécoms',
        'options': [   'Elle est taguée obligatoirement avec un VLAN ID égal à '
                       '1',
                       'Elle circule de manière non taguée',
                       "Elle est chiffrée avec l'algorithme AES",
                       'Elle est rejetée silencieusement'],
        'q': "Q40 : Sur un lien d'interconnexion Trunk entre deux "
             'commutateurs, comment circule une trame Ethernet appartenant au '
             'VLAN natif ?',
        'rep': 'Elle circule de manière non taguée'},
    {   'chap': '5. Protocoles Industriels & Bus de terrain (Modbus, Profibus)',
        'expl': 'Le code de fonction standard 03 (Read Holding Registers) '
                "permet de lire les registres d'écriture/lecture analogiques "
                'de 16 bits (Holding Registers). Le code 04 permet de lire les '
                "registres d'entrée en lecture seule (Input Registers).",
        'mod': '📶 Réseaux & Télécoms',
        'options': [   '01 (Read Coils)',
                       '02 (Read Discrete Inputs)',
                       '03 (Read Holding Registers)',
                       '04 (Read Input Registers)'],
        'q': "Q41 : Dans le cadre de l'interfaçage de réseaux industriels avec "
             'le protocole Modbus RTU (série RS-485), quel code de fonction '
             '(Function Code) standard permet de lire la valeur de registres '
             'de sortie analogiques (Holding Registers) ?',
        'rep': '03 (Read Holding Registers)'},
    {   'chap': "4. Services d'Infrastructure : DHCP, DNS, NAT/PAT",
        'expl': "L'émission de la requête ARP (ARP Request) s'effectue par "
                'diffusion générale (Broadcast) à destination de toutes les '
                'machines du domaine de diffusion locale (adresse MAC '
                'destination FF:FF:FF:FF:FF:FF). La réponse (ARP Reply) est '
                'ensuite renvoyée en Unicast.',
        'mod': '📶 Réseaux & Télécoms',
        'options': [   'Unicast (adresse MAC du routeur)',
                       'Multicast (adresse MAC IPv6)',
                       'Broadcast (adresse MAC FF:FF:FF:FF:FF:FF)',
                       'Anycast (adresse MAC dynamique)'],
        'q': "Q42 : Lors de la résolution d'adresse physique via le protocole "
             'ARP (Address Resolution Protocol), quel type de trame Ethernet '
             'est émise par une machine pour interroger le réseau, et quelle '
             "est l'adresse MAC de destination de cette trame ?",
        'rep': 'Broadcast (adresse MAC FF:FF:FF:FF:FF:FF)'},
    {   'chap': "4. Lois Fondamentales d'Électricité & Composants Passifs",
        'expl': "L'énergie emmagasinée dans un condensateur se calcule par la "
                'formule E = (1/2) * C * U^2. Donc, E = 0,5 * (220 * 10^-6 F) '
                '* (10 V)^2 = 0,5 * 0,00022 * 100 = 0,011 J = 11 mJ.',
        'mod': '🔌 Électronique & IoT',
        'options': ['1,1 mJ', '11 mJ', '22 mJ', '110 mJ'],
        'q': 'Q43 : Un condensateur de capacité C = 220 µF est raccordé dans '
             "un circuit électrique continu sous une tension d'alimentation "
             "stable U = 10 V. Quelle est l'énergie électrostatique E "
             'emmagasinée par ce condensateur ?',
        'rep': '11 mJ'},
    {   'chap': "4. Lois Fondamentales d'Électricité & Composants Passifs",
        'expl': 'Pour deux résistances en parallèle, la résistance équivalente '
                "s'obtient par la formule : Req = (R1 * R2) / (R1 + R2) = (100 "
                '* 300) / (100 + 300) = 30000 / 400 = 75 Ω.',
        'mod': '🔌 Électronique & IoT',
        'options': ['75 Ω', '200 Ω', '400 Ω', '300 Ω'],
        'q': 'Q44 : Deux résistances ohmiques R1 = 100 Ω et R2 = 300 Ω sont '
             'branchées en parallèle dans un circuit de filtrage. Quelle est '
             'la valeur de la résistance équivalente Req de cette association '
             '?',
        'rep': '75 Ω'},
    {   'chap': '6. Transmission optique (Fibres optiques Monomodes & '
                'Multimodes)',
        'expl': 'La fibre Monomode possède un cœur très étroit (9 µm) par '
                'rapport à la Multimode (50 µm ou 62,5 µm). Elle limite la '
                'propagation à un faisceau rectiligne unique (mode axial), ce '
                'qui annule la dispersion modale temporelle et permet de très '
                'hauts débits sur de très longues distances sans répéteur.',
        'mod': '📶 Réseaux & Télécoms',
        'options': [   'La fibre Monomode a un diamètre de cœur très fin (≈ 9 '
                       "µm) et ne transmet qu'un seul mode de propagation "
                       'laser, réduisant presque à zéro la dispersion modale.',
                       'La fibre Monomode utilise une source lumineuse LED de '
                       "faible coût et souffre d'une forte atténuation sur de "
                       'courtes distances.',
                       'La fibre Multimode est réservée exclusivement aux '
                       'liaisons océaniques intercontinentales de très longue '
                       'distance.',
                       'La fibre Monomode utilise un cœur de grand diamètre (≈ '
                       "50 µm ou 62,5 µm) permettant d'injecter plusieurs "
                       "longueurs d'ondes à la fois."],
        'q': "Q45 : Dans l'épreuve de transmission optique, quelle "
             'caractéristique distingue fondamentalement une fibre optique '
             "Monomode (Single-mode) d'une fibre optique Multimode "
             '(Multi-mode) ?',
        'rep': 'La fibre Monomode a un diamètre de cœur très fin (≈ 9 µm) et '
               "ne transmet qu'un seul mode de propagation laser, réduisant "
               'presque à zéro la dispersion modale.'},
    {   'chap': '3. Structures de données avancées & Unions en Langage C',
        'expl': 'Contrairement à une structure (struct) qui additionne la '
                'taille de ses membres (plus alignement), une union partage le '
                'même espace mémoire pour tous ses membres. Sa taille totale '
                'correspond donc à la taille de son plus grand membre, qui est '
                'ici le float (4 octets).',
        'mod': '💻 Programmation / Dev',
        'options': ['1 octet', '4 octets', '7 octets', '8 octets'],
        'q': "Q46 : En programmation système C/C++ pour l'embarqué, si un "
             "programme définit un type 'union' contenant un 'char' (1 octet), "
             "un 'short' (2 octets) et un 'float' (4 octets), quelle sera "
             "l'occupation mémoire en octets d'une instance de cette union ?",
        'rep': '4 octets'},
    {   'chap': '2. Active Directory, Domaines & GPO',
        'expl': "L'enregistrement PTR (Pointer Record) est utilisé dans la "
                'zone de recherche inverse (Reverse Lookup Zone) pour associer '
                'une adresse IP à un nom DNS, indispensable pour certains '
                'services de sécurité et de filtrage anti-spam.',
        'mod': '🖥️ Administration Système',
        'options': [   'Enregistrement A',
                       'Enregistrement CNAME',
                       'Enregistrement PTR',
                       'Enregistrement NS'],
        'q': "Q47 : Dans la configuration de zones d'un serveur de noms de "
             "domaine (DNS), quel type d'enregistrement (Resource Record) doit "
             'obligatoirement être créé pour assurer la résolution inverse '
             '(traduire une adresse IP publique ou privée en nom de domaine '
             'complet FQDN) ?',
        'rep': 'Enregistrement PTR'},
    {   'chap': '1. Droits Linux & Commandes Système',
        'expl': "Le SUID (Set User ID) permet d'exécuter un fichier binaire "
                'avec les droits de son propriétaire (généralement root). Il '
                "est représenté par la lettre 's' à la place du droit "
                "d'exécution du propriétaire (ex: rwsr-xr-x) et vaut 4 au "
                'premier chiffre en octal (ex: chmod 4755).',
        'mod': '🖥️ Administration Système',
        'options': [   'Le SUID (Set User ID, valeur numérique 4000)',
                       'Le SGID (Set Group ID, valeur numérique 2000)',
                       'Le Sticky Bit (valeur numérique 1000)',
                       "L'ACL d'accès spécifique"],
        'q': 'Q48 : Sous GNU/Linux, quelle permission spéciale permet à un '
             "utilisateur d'exécuter un fichier binaire avec les privilèges "
             "d'accès du propriétaire du fichier (par exemple, pour permettre "
             'à un simple utilisateur de changer son mot de passe avec '
             "l'exécutable '/usr/bin/passwd') ?",
        'rep': 'Le SUID (Set User ID, valeur numérique 4000)'},
    {   'chap': "4. Lois Fondamentales d'Électricité & Composants Passifs",
        'expl': "D'après la formule du pont diviseur de tension, la tension "
                "aux bornes de R2 s'exprime par : U_R2 = E * [R2 / (R1 + R2)] "
                '= 12 V * [400 / (800 + 400)] = 12 V * [400 / 1200] = 12 V * '
                '(1/3) = 4 V.',
        'mod': '🔌 Électronique & IoT',
        'options': ['4 V', '6 V', '8 V', '12 V'],
        'q': 'Q49 : Dans un montage électrique continu alimenté par un '
             'générateur de tension E = 12 V, un pont diviseur de tension est '
             'constitué de deux résistances en série R1 = 800 Ω et R2 = 400 Ω. '
             'Quelle est la tension de sortie U_R2 mesurée aux bornes de la '
             'résistance R2 ?',
        'rep': '4 V'},
    {   'chap': '2. Active Directory, Domaines & GPO',
        'expl': "Une Unité d'Organisation (OU) est un conteneur logique. On ne "
                'peut pas y attribuer directement des droits de partage de '
                "fichiers (ce n'est pas un groupe de sécurité), mais elle "
                "permet d'organiser les comptes utilisateurs/ordinateurs pour "
                "y lier des GPO ou déléguer le contrôle d'administration (ex: "
                'réinitialiser un mot de passe).',
        'mod': '🖥️ Administration Système',
        'options': [   'Organiser logiquement les objets du domaine pour '
                       'appliquer des stratégies de groupe (GPO) et déléguer '
                       "des tâches d'administration.",
                       'Créer des principaux de sécurité sur lesquels on peut '
                       "attribuer directement des droits d'accès aux partages "
                       'de fichiers.',
                       "Établir des relations d'approbation d'accès sécurisées "
                       "(Trust Relationships) avec d'autres forêts de "
                       'serveurs.',
                       'Augmenter le niveau fonctionnel global de la forêt AD '
                       "sans modifier l'infrastructure physique."],
        'q': "Q50 : Dans la structuration hiérarchique d'un annuaire Active "
             'Directory sous Windows Server, quel est le principal intérêt de '
             "la création d'Unités d'Organisation (OU) ?",
        'rep': 'Organiser logiquement les objets du domaine pour appliquer des '
               'stratégies de groupe (GPO) et déléguer des tâches '
               "d'administration."},
{
    "q": "Q41 : En transmission par fibre optique, quelle est la caractéristique majeure d'une fibre Monomode (SMF) par rapport à une fibre Multimode (MMF) ?",
    "options": [
        "Un cœur large de 50 µm et l'utilisation de LED sur courte distance",
        "Un cœur très étroit (~9 µm), l'absence de dispersion modale et des portées de plusieurs dizaines de kilomètres",
        "Une forte dispersion modale limitant la portée à 300 mètres",
        "L'utilisation exclusive de connecteurs ST"
    ],
    "rep": "Un cœur très étroit (~9 µm), l'absence de dispersion modale et des portées de plusieurs dizaines de kilomètres",
    "mod": "📶 Réseaux & Télécoms",
    "chap": "6. Transmissions Optiques & Fibre Optique (Monomode vs Multimode)",
    "expl": "La fibre Monomode (SMF) possède un cœur très fin (~9 µm) dans lequel ne se propage qu'un seul mode lumineux (Laser). Sans dispersion modale, elle permet d'atteindre des distances de 40 à 100 km."
},
{
    "q": "Q42 : Dans le protocole Modbus RTU, quel code fonction (Function Code) permet de lire des registres de lecture/écriture 16 bits (Holding Registers) ?",
    "options": [
        "Code 01",
        "Code 03",
        "Code 06",
        "Code 16 (0x10)"
    ],
    "rep": "Code 03",
    "mod": "📶 Réseaux & Télécoms",
    "chap": "7. Protocoles Industriels : Modbus RTU & Bus RS485",
    "expl": "Le code fonction Modbus 03 (Read Holding Registers) permet au maître de lire le contenu de registres de configuration ou de données 16 bits."
},
{
    "q": "Q43 : Conformément au RGPD et aux directives CNIL, quand la réalisation d'une Analyse d'Impact relative à la Protection des Données (AIPD / PIA) est-elle légalement obligatoire ?",
    "options": [
        "Uniquement pour les entreprises de plus de 500 salariés",
        "Dès lors que le traitement répond à au moins 2 des 9 critères de risque de la grille CNIL/CEPD",
        "Uniquement en cas de traitement de coordonnées bancaires",
        "Elle est toujours facultative"
    ],
    "rep": "Dès lors que le traitement répond à au moins 2 des 9 critères de risque de la grille CNIL/CEPD",
    "mod": "🔒 Cybersécurité",
    "chap": "6. Analyse d'Impact sur la Vie Privée PIA / AIPD (RGPD & CNIL)",
    "expl": "L'AIPD devient légalement obligatoire si un traitement de données personnelles accumule au moins 2 critères parmi les 9 définis par les autorités européennes (profilage, données sensibles, grande échelle, personnes vulnérables, etc.)."
},
{
    "q": "Q44 : Dans une architecture de pare-feu pfSense, pourquoi est-il strictement interdit d'autoriser le flux d'initiation de connexion depuis la DMZ vers le réseau interne LAN ?",
    "options": [
        "Parce que pfSense ne sait pas router les paquets entre DMZ et LAN",
        "Pour éviter qu'un attaquant compromettant un serveur public en DMZ ne puisse pivoter vers le réseau interne de l'entreprise",
        "Parce que les requêtes DNS ne fonctionnent que du LAN vers la DMZ",
        "Pour économiser la bande passante de l'interface WAN"
    ],
    "rep": "Pour éviter qu'un attaquant compromettant un serveur public en DMZ ne puisse pivoter vers le réseau interne de l'entreprise",
    "mod": "🔒 Cybersécurité",
    "chap": "8. Matrice des Flux & Architecture Pare-Feu pfSense (LAN/DMZ/WAN/AD)",
    "expl": "La DMZ héberge des serveurs exposés à Internet. En interdisant l'initiation de connexions de la DMZ vers le LAN, on empêche un pirate d'utiliser le serveur compromis comme rebond vers les machines internes."
},
{
    "q": "Q45 : En langage C, quelle est la particularité fondamentale de la mémoire d'une 'union' par rapport à une 'struct' ?",
    "options": [
        "Une union est allouée dynamiquement sur le tas alors qu'une struct est sur la pile",
        "Tous les membres d'une union partagent le même espace mémoire, et sa taille vaut celle de son plus grand membre",
        "Une union ne peut pas contenir de variables entières",
        "Une struct utilise systématiquement moins de mémoire qu'une union"
    ],
    "rep": "Tous les membres d'une union partagent le même espace mémoire, et sa taille vaut celle de son plus grand membre",
    "mod": "💻 Programmation / Dev",
    "chap": "2. Langage C : Structures struct & Unions union",
    "expl": "Dans une union, les membres chevauchent la même adresse mémoire. Écrire dans un membre écrase la valeur des autres. C'est idéal pour convertir un float 32 bits en 4 octets."
},
{
    "q": "Q46 : En C++11 multithread, quel composant doit être utilisé pour protéger une variable partagée dans une section critique contre les conditions de concurrence (Race Conditions) ?",
    "options": [
        "std::vector",
        "std::mutex avec std::lock_guard",
        "std::thread::sleep_for",
        "std::atomic_bool uniquement"
    ],
    "rep": "std::mutex avec std::lock_guard",
    "mod": "💻 Programmation / Dev",
    "chap": "4. Programmation Concurrente C++11 : Threads, Mutex & Section Critique",
    "expl": "Un mutex verrouille l'accès à la section critique. Le wrapper std::lock_guard applique le principe RAII : il verrouille le mutex à l'instanciation et le libère automatiquement à la sortie du bloc."
},
{
    "q": "Q47 : Dans la technologie IoT LoRaWAN, quelle classe d'équipements offre la plus faible consommation énergétique en n'ouvrant des fenêtres de réception qu'immédiatement après une émission ?",
    "options": [
        "Classe A",
        "Classe B",
        "Classe C",
        "Classe D"
    ],
    "rep": "Classe A",
    "mod": "🔌 Électronique & IoT",
    "chap": "5. Protocoles Connectés : MQTT & LoRaWAN",
    "expl": "Les équipements LoRaWAN de Classe A restent en veille quasi-permanente. Ils n'ouvrent deux courtes fenêtres de réception qu'après avoir émis un message, offrant une autonomie de batterie maximale."
},
{
    "q": "Q48 : Dans une architecture PKI, quel est le rôle principal d'une Autorité de Certification Intermédiaire (Issuing CA) ?",
    "options": [
        "Signer le certificat de la CA Racine",
        "Délivrer et signer les certificats X.509 opérationnels des serveurs et utilisateurs tout en gardant la CA Racine hors ligne",
        "Stocker les clés privées de tous les utilisateurs Internet",
        "Remplacer le serveur DNS"
    ],
    "rep": "Délivrer et signer les certificats X.509 opérationnels des serveurs et utilisateurs tout en gardant la CA Racine hors ligne",
    "mod": "🔒 Cybersécurité",
    "chap": "7. PKI & Gestion des Certificats Numériques X.509",
    "expl": "Pour protéger la CA Racine (Root CA) maintenue hors ligne dans un coffre-fort, la CA Intermédiaire prend en charge la délivrance quotidienne des certificats."
},
{
    "q": "Q49 : En communication Modbus RTU sur liaison RS485, comment la fin d'une trame est-elle détectée par les automates récepteurs ?",
    "options": [
        "Par un caractère de saut de ligne ASCII \\r\\n",
        "Par un silence sur le bus supérieur ou égal à 3,5 temps caractères",
        "Par un octet d'en-tête specifique 0x7E",
        "Par une impulsion sur une ligne physique séparée"
    ],
    "rep": "Par un silence sur le bus supérieur ou égal à 3,5 temps caractères",
    "mod": "📶 Réseaux & Télécoms",
    "chap": "7. Protocoles Industriels : Modbus RTU & Bus RS485",
    "expl": "Modbus RTU utilise un délimiteur temporel : un intervalle de silence de 3.5 caractères marque la fin d'une trame et le début de la suivante."
},
{
    "q": "Q50 : Quel est l'intérêt principal des extensions SAN (Subject Alternative Name) dans un certificat TLS X.509 ?",
    "options": [
        "Compresser la taille du certificat",
        "Autoriser plusieurs noms de domaine (FQDN) et adresses IP sous un seul et même certificat",
        "Chiffrer la clé privée sur le disque",
        "Désactiver TLS 1.3"
    ],
    "rep": "Autoriser plusieurs noms de domaine (FQDN) et adresses IP sous un seul et même certificat",
    "mod": "🔒 Cybersécurité",
    "chap": "7. PKI & Gestion des Certificats Numériques X.509",
    "expl": "L'extension SAN permet de lister l'ensemble des noms d'hôtes (ex: www.ciel.fr, mail.ciel.fr, IP) valides pour le certificat."
}
,
    {
        "q": "Q61 : Selon la loi de Shannon-Hartley, quelle est la capacité maximale C d'un canal de bande passante B = 1 MHz ayant un rapport signal/bruit S/N = 15 (linéaire) ?",
        "options": ["1 Mbps", "4 Mbps", "15 Mbps", "16 Mbps"],
        "rep": "4 Mbps",
        "mod": "📶 Réseaux & Télécoms",
        "chap": "5. Modulations & Transmissions de Signaux (FSK, ASK, PSK, QAM)",
        "expl": "C = B * log2(1 + S/N) = 1 MHz * log2(1 + 15) = 1 MHz * log2(16) = 1 MHz * 4 = 4 Mbps."
    },
    {
        "q": "Q62 : Quel protocole de prévention des boucles de commutation (Spanning Tree) offre une convergence rapide en quelques millisecondes sous la norme IEEE 802.1w ?",
        "options": ["STP (802.1D)", "RSTP (802.1w)", "PVST+", "MSTP (802.1s)"],
        "rep": "RSTP (802.1w)",
        "mod": "📶 Réseaux & Télécoms",
        "chap": "3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN",
        "expl": "Rapid Spanning Tree Protocol (RSTP - 802.1w) offre une réadaptation quasi-instantanée de la topologie réseau."
    },
    {
        "q": "Q63 : En C++11, quel pointeur intelligent (Smart Pointer) doit être utilisé pour garantir qu'un objet dynamique ne possède qu'un seul et unique propriétaire ?",
        "options": ["std::shared_ptr", "std::unique_ptr", "std::weak_ptr", "std::auto_ptr"],
        "rep": "std::unique_ptr",
        "mod": "💻 Programmation / Dev",
        "chap": "1. Langage C++ : Mémoire, Pointeurs & POO",
        "expl": "std::unique_ptr exécute la gestion de propriété exclusive sans surcoût de compteur de références."
    },
    {
        "q": "Q64 : Quelle commande Linux permet de rechercher toutes les lignes contenant le mot 'ERROR' dans tous les fichiers .log du dossier /var/log de manière récursive ?",
        "options": ["find /var/log -name 'ERROR'", "grep -r 'ERROR' /var/log/*.log", "cat /var/log | grep 'ERROR'", "locate 'ERROR' /var/log"],
        "rep": "grep -r 'ERROR' /var/log/*.log",
        "mod": "🖥️ Administration Système",
        "chap": "1. Droits Linux & Commandes Système",
        "expl": "L'option -r de grep effectue une recherche récursive dans tous les fichiers correspondant au motif."
    },
    {
        "q": "Q65 : Quelle est la fréquence de coupure fc d'un filtre RC passe-bas constitué d'une résistance R = 1 kΩ et d'un condensateur C = 159 nF ?",
        "options": ["100 Hz", "1 kHz", "10 kHz", "100 kHz"],
        "rep": "1 kHz",
        "mod": "🔌 Électronique & IoT",
        "chap": "1. Échantillonnage, CAN/CNA & Théorème de Shannon",
        "expl": "fc = 1 / (2 * pi * R * C) = 1 / (2 * 3.14159 * 1000 * 159e-9) ≈ 1000 Hz = 1 kHz."
    },
    {
        "q": "Q66 : En mathématiques, quelle est la dérivée f'(x) de la fonction f(x) = ln(3x^2 + 1) sur R ?",
        "options": ["f'(x) = 1 / (3x^2 + 1)", "f'(x) = 6x / (3x^2 + 1)", "f'(x) = 6x * (3x^2 + 1)", "f'(x) = 3 / x"],
        "rep": "f'(x) = 6x / (3x^2 + 1)",
        "mod": "📈 Mathématiques",
        "chap": "Fonctions, Exponentielle & Logarithme",
        "expl": "Pour f(x) = ln(u(x)), la dérivée est u'(x) / u(x). Avec u(x) = 3x^2 + 1, u'(x) = 6x. Donc f'(x) = 6x / (3x^2 + 1)."
    },
    {
        "q": "Q67 : Dans le protocole d'authentification Wi-Fi 802.1X / Enterprise, quel serveur est chargé de vérifier les identifiants et certificats des utilisateurs ?",
        "options": ["Serveur DHCP", "Serveur RADIUS", "Serveur DNS", "Serveur NTP"],
        "rep": "Serveur RADIUS",
        "mod": "🔒 Cybersécurité",
        "chap": "4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)",
        "expl": "Le serveur RADIUS centralise la gestion de l'authentification AAA (Authentication, Authorization, Accounting) en 802.1X."
    },
    {
        "q": "Q68 : Sur un réseau de communication Modbus RTU sur liaison série RS-485, quel est le nombre maximal théorique d'esclaves adressables sans répéteur ?",
        "options": ["16 esclaves", "32 esclaves", "127 esclaves", "247 esclaves"],
        "rep": "247 esclaves",
        "mod": "🔌 Électronique & IoT",
        "chap": "2. Bus Série Matériels : I2C, SPI, UART & CAN Bus",
        "expl": "La plage d'adresses esclaves Modbus s'étend de 1 à 247 (l'adresse 0 étant réservée à la diffusion / broadcast)."
    },
    {
        "q": "Q69 : En SysML, quel diagramme permet de définir la hiérarchie des exigences du cahier des charges et leurs relations de traçabilité (deriveReqt, verify) ?",
        "options": ["BDD (Block Definition Diagram)", "IBD (Internal Block Diagram)", "Requirement Diagram", "Use Case Diagram"],
        "rep": "Requirement Diagram",
        "mod": "📐 Modélisation UML & SysML",
        "chap": "2. Diagrammes SysML (BDD, IBD, Exigences)",
        "expl": "Le Requirement Diagram modélise les exigences fonctionnelles et non-fonctionnelles et leur traçabilité."
    },
    {
        "q": "Q70 : En C++, quel mot-clé permet d'indiquer qu'une méthode d'une classe dérivée est destinée à redéfinir une méthode virtuelle de sa classe mère ?",
        "options": ["virtual", "override", "overload", "static"],
        "rep": "override",
        "mod": "💻 Programmation / Dev",
        "chap": "1. Langage C++ : Mémoire, Pointeurs & POO",
        "expl": "Le spécificateur 'override' (C++11) garantit au compilateur que la méthode redéfinit exactement une méthode virtuelle de la classe de base."
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

# --- NAVIGATION SIDEBAR INTELLIGENTE & STRUCTURÉE ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/graduation-cap.png", width=75)
    st.markdown("### **BTS CIEL - Studio Pro**")
    st.caption("Cybersécurité, Informatique & Réseaux, Électronique")
    
    nav_mode = st.radio(
        "🎯 Mode de Navigation :",
        ["📁 Par Catégories (Structuré)", "📋 Liste Complète (23 Pages)"],
        index=0
    )
    
    CATEGORIES = {
        "🏠 Vue d'Ensemble & Bilan": [
            "🏠 Accueil & Dashboard",
            "🗓️ Planning Révisions BTS Blanc (9-11 Déc)",
            "📈 Analyse des Scores",
            "📋 Planning de Projet E6 (Gantt)"
        ],
        "🎓 Préparation BTS Blanc (Examens)": [
            "🗓️ Révision Semaine par Semaine (BTS Blanc)",
            "🎯 Révision Totale BTS Blanc (9-11 Déc)",
            "🎯 Annales BTS (2024 & 2025)",
            "📝 Grand Quiz d'Examen"
        ],
        "📚 Cours, Fiches & TPs": [
            "📚 Encyclopédie des Cours & TPs",
            "🛠️ Fiches Réussite Épreuve E5 (TP & Pratique)",
            "📄 Fiches Savoir & Fiches Montage",
            "🛡️ TP Cybersécurité, Gouvernance & pfSense",
            "🛡️ Guides de Durcissement (Hardening) ANSSI"
        ],
        "📐 Mathématiques & Physique": [
            "📊 Mathématiques : Suites Arithmétiques & Géométriques",
            "📈 Mathématiques : Fonctions, Exponentielle & Logarithme",
            "⚡ Lab Kirchhoff, Ohm & Circuits",
            "📺 Lab Oscilloscope & Mesures Physiques"
        ],
        "🧪 Laboratoires, Calculs & Sandboxes": [
            "🧮 Laboratoire de Calculs (Subnetting & Élec)",
            "📐 Laboratoire UML & SysML",
            "🔍 Lab Décodeur Wireshark",
            "🔍 Captures de Trames & Analyses Wireshark PCAP",
            "💻 Sandboxes & Terminaux Pratiques",
            "🧪 Qualification & Tests E6",
            "📁 Modèles de Livrables & PVL Épreuve E6"
        ],
        "🚀 Datasheets & Anglais Technique": [
            "📄 Datasheets & Fiches Techniques (Composants)",
            "🇬🇧 Vocabulaire & Anglais Technique BTS"
        ],
        "🗂️ Flashcards & Ressources": [
            "🗂️ Flashcards Actives",
            "📹 Vidéos de Cours",
            "🌐 Répertoire des Liens"
        ]
    }

    ALL_PAGES = [
        "🏠 Accueil & Dashboard",
        "📄 Fiches Savoir & Fiches Montage",
        "🛠️ Fiches Réussite Épreuve E5 (TP & Pratique)",
        "🛡️ TP Cybersécurité, Gouvernance & pfSense",
        "🛡️ Guides de Durcissement (Hardening) ANSSI",
        "🗓️ Révision Semaine par Semaine (BTS Blanc)",
        "🎯 Révision Totale BTS Blanc (9-11 Déc)",
        "📊 Mathématiques : Suites Arithmétiques & Géométriques",
        "📈 Mathématiques : Fonctions, Exponentielle & Logarithme",
        "🗓️ Planning Révisions BTS Blanc (9-11 Déc)",
        "⚡ Lab Kirchhoff, Ohm & Circuits",
        "📺 Lab Oscilloscope & Mesures Physiques",
        "📚 Encyclopédie des Cours & TPs",
        "🧮 Laboratoire de Calculs (Subnetting & Élec)",
        "📐 Laboratoire UML & SysML",
        "🔍 Lab Décodeur Wireshark",
        "🔍 Captures de Trames & Analyses Wireshark PCAP",
        "💻 Sandboxes & Terminaux Pratiques",
        "🧪 Qualification & Tests E6",
        "📁 Modèles de Livrables & PVL Épreuve E6",
        "📄 Datasheets & Fiches Techniques (Composants)",
        "🇬🇧 Vocabulaire & Anglais Technique BTS",
        "🎯 Annales BTS (2024 & 2025)",
        "🗂️ Flashcards Actives",
        "📝 Grand Quiz d'Examen",
        "📈 Analyse des Scores",
        "📋 Planning de Projet E6 (Gantt)",
        "📹 Vidéos de Cours",
        "🌐 Répertoire des Liens"
    ]
    
    if "Par Catégories" in nav_mode:
        st.markdown("---")
        selected_cat = st.selectbox("📁 Choisissez un pôle :", list(CATEGORIES.keys()))
        page = st.radio("📄 Choisissez le module :", CATEGORIES[selected_cat])
    else:
        st.markdown("---")
        page = st.radio("📋 Choisissez la page :", ALL_PAGES)
        
    st.markdown("---")
    st.success("⚡ **Statut** : Mode Entraînement Actif")

# --- 1. PAGE ACCUEIL ---
if page == "🏠 Accueil & Dashboard":
    st.markdown(r"""
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
    r""", unsafe_allow_html=True)
    
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
        st.markdown(r"""
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
        r""", unsafe_allow_html=True)
    with c2:
        st.markdown(r"""
        <div class='ciel-card' style='border-left: 6px solid #10b981 !important;'>
            <h4 style='color: #065f46 !important; margin-top:0; font-size: 1.15rem;'>📋 Épreuves Couvertes :</h4>
            <p style='color: #1e293b !important; margin-bottom: 12px;'><b style='color: #0f172a !important;'>• E4 : Épreuve Technique Écrite</b><br>
            <span style='color: #475569 !important;'>Réseaux, Sécurité, C++, IoT & SysML</span></p>
            <p style='color: #1e293b !important; margin-bottom: 12px;'><b style='color: #0f172a !important;'>• E5 : Activités Professionnelles & TP</b><br>
            <span style='color: #475569 !important;'>Configurations Cisco, Linux, Wireshark</span></p>
            <p style='color: #1e293b !important; margin-bottom: 0;'><b style='color: #0f172a !important;'>• E6 : Projet de Fin d'Études</b><br>
            <span style='color: #475569 !important;'>Cahier des charges, UML, Dev, PVL & Gantt</span></p>
        </div>
        r""", unsafe_allow_html=True)

    st.markdown(r"""
    <hr style='margin: 25px 0;'>
    <h3 style='color: #1e3a8a; font-weight: 800;'>🗺️ Carte de Navigation du Studio (6 Pôles d'Ingénierie)</h3>
    <p style='color: #475569;'>Pour naviguer sereinement sans vous perdre, le studio est structuré en <b>6 Pôles thématiques</b> accessibles via le menu latéral :</p>
    r""", unsafe_allow_html=True)

    m_col1, m_col2, m_col3 = st.columns(3)
    
    with m_col1:
        st.markdown(r"""
        <div class='ciel-card' style='border-top: 5px solid #2563eb !important; height: 260px;'>
            <h4 style='color: #1d4ed8 !important; margin-top: 0;'>🎓 1. Préparation BTS Blanc</h4>
            <ul style='font-size: 0.9rem; color: #334155 !important; padding-left: 18px;'>
                <li><b>🗓️ Révision Semaine par Semaine</b> : 6 semaines complètes avec cours, flashcards & quiz.</li>
                <li><b>🎯 Révision Totale (Hub)</b> : Synthèse des 61 sources & TPs.</li>
                <li><b>🎯 Annales BTS</b> : Sujets officiels 2024 & 2025 décortiqués.</li>
                <li><b>📝 Grand Quiz d'Examen</b> : 70 questions multi-matières.</li>
            </ul>
        </div>
        r""", unsafe_allow_html=True)

        st.markdown(r"""
        <div class='ciel-card' style='border-top: 5px solid #0284c7 !important; height: 260px;'>
            <h4 style='color: #0369a1 !important; margin-top: 0;'>📐 4. Mathématiques & Physique</h4>
            <ul style='font-size: 0.9rem; color: #334155 !important; padding-left: 18px;'>
                <li><b>📊 Suites Arithmétiques & Géométriques</b> : Formules, limites & dérivées.</li>
                <li><b>📈 Fonctions e^x / ln</b> : Décibels & charge/décharge RC.</li>
                <li><b>⚡ Lab Kirchhoff & Ohm</b> : Mailles, nœuds & diviseurs.</li>
                <li><b>📺 Lab Oscilloscope</b> : Mesures de Vpp, Veff, T, f.</li>
            </ul>
        </div>
        r""", unsafe_allow_html=True)

    with m_col2:
        st.markdown(r"""
        <div class='ciel-card' style='border-top: 5px solid #10b981 !important; height: 260px;'>
            <h4 style='color: #047857 !important; margin-top: 0;'>📚 2. Cours, Fiches & TPs</h4>
            <ul style='font-size: 0.9rem; color: #334155 !important; padding-left: 18px;'>
                <li><b>📚 Encyclopédie des Cours</b> : Réseaux, Cyber, Dev, SysAdmin, Élec, SysML.</li>
                <li><b>📄 Fiches Savoir & Montage</b> : 12 Fiches Savoir & 2 Fiches Montage.</li>
                <li><b>🛡️ TP Cyber & pfSense</b> : EBIOS RM, PIA RGPD, PKI & DMZ pfSense.</li>
            </ul>
        </div>
        r""", unsafe_allow_html=True)

        st.markdown(r"""
        <div class='ciel-card' style='border-top: 5px solid #d97706 !important; height: 260px;'>
            <h4 style='color: #b45309 !important; margin-top: 0;'>🧪 5. Labs & Sandboxes</h4>
            <ul style='font-size: 0.9rem; color: #334155 !important; padding-left: 18px;'>
                <li><b>🧮 Lab Subnetting & CAN</b> : Calculs VLSM & quantum.</li>
                <li><b>📐 Lab UML & SysML</b> : BDD, IBD, Séquence, Classes.</li>
                <li><b>🔍 Lab Wireshark</b> : Décodage trames hexadécimales.</li>
                <li><b>💻 Sandboxes</b> : Cisco IOS, Linux Bash & C++.</li>
                <li><b>🧪 Qualification E6</b> : Pytest & PVL.</li>
            </ul>
        </div>
        r""", unsafe_allow_html=True)

    with m_col3:
        st.markdown(r"""
        <div class='ciel-card' style='border-top: 5px solid #7c3aed !important; height: 260px;'>
            <h4 style='color: #6d28d9 !important; margin-top: 0;'>🏠 3. Tableau de Bord</h4>
            <ul style='font-size: 0.9rem; color: #334155 !important; padding-left: 18px;'>
                <li><b>🏠 Accueil & Dashboard</b> : Vue globale & carte du studio.</li>
                <li><b>🗓️ Planning de Révision</b> : Calendrier jusqu'en Décembre.</li>
                <li><b>📈 Analyse des Scores</b> : Graphiques de progression.</li>
                <li><b>📋 Planning Gantt E6</b> : Suivi de projet d'examen.</li>
            </ul>
        </div>
        r""", unsafe_allow_html=True)

        st.markdown(r"""
        <div class='ciel-card' style='border-top: 5px solid #ec4899 !important; height: 260px;'>
            <h4 style='color: #be185d !important; margin-top: 0;'>🗂️ 6. Flashcards & Outillage</h4>
            <ul style='font-size: 0.9rem; color: #334155 !important; padding-left: 18px;'>
                <li><b>🗂️ Flashcards Actives</b> : 24+ cartes mémoire réflexe.</li>
                <li><b>📹 Vidéothèque</b> : Vidéos explicatives ciblées.</li>
                <li><b>🌐 Répertoire de Liens</b> : Référentiels & outils web.</li>
            </ul>
        </div>
        r""", unsafe_allow_html=True)



# --- PAGE PLANNING RÉVISIONS BTS BLANC ---

# --- PAGE : MATHÉMATIQUES - SUITES ARITHMÉTIQUES ET GÉOMÉTRIQUES ---
elif page == "📊 Mathématiques : Suites Arithmétiques & Géométriques":
    st.markdown("<div class='hero-title'>📊 Mathématiques Appliquées : Suites & Dérivées</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Cours complet, formules explicites, méthode de la dérivée, simulateurs interactifs et exercices de programmation Python</p>", unsafe_allow_html=True)

    tab_m1, tab_m2, tab_m3, tab_m4 = st.tabs([
        "📖 Cours & Formules Clés", 
        "🧮 Calculatrice & Simulateur de Suites", 
        "🐍 Traduction Algorithmique Python", 
        "✍️ Exercices Pratiques & Quiz"
    ])

    with tab_m1:
        st.subheader("1. Synthèse Comparative : Arithmétique vs Géométrique")
        st.markdown(r"""
        La distinction entre ces deux modèles est la base de toute modélisation en réseaux et systèmes (allocation mémoire, incrémentation d'adresses, atténuation de signal, saturation de bande passante).
        r""")

        st.markdown(r"""
        | Propriété | Suite Arithmétique | Suite Géométrique |
        | :--- | :--- | :--- |
        | **Mécanisme** | On **ajoute** une raison constante $r$. | On **multiplie** par une raison constante $q$. |
        | **Récurrence** | $u_{n+1} = u_n + r$ | $u_{n+1} = u_n \times q$ |
        | **Formule explicite (depuis $u_0$)** | $u_n = u_0 + n \cdot r$ | $u_n = u_0 \times q^n$ |
        | **Formule explicite (depuis $u_p$)** | $u_n = u_p + (n - p) \cdot r$ | $u_n = u_p \times q^{n-p}$ |
        | **Somme des $N$ premiers termes** | $S = N \times \frac{u_{\text{premier}} + u_{\text{dernier}}}{2}$ | $S = u_{\text{premier}} \times \frac{1 - q^{\text{Nb\\_termes}}}{1 - q} \\quad (q \\neq 1)$ |
        | **Variations** | Si $r > 0$ : Croissante<br>Si $r < 0$ : Décroissante | Si $u_0 > 0$ et $q > 1$ : Croissante<br>Si $u_0 > 0$ et $0 < q < 1$ : Décroissante |
        | **Application BTS CIEL** | Incrémentation d'adresses IP, boucles simples. | Atténuation d'un signal optique/Wi-Fi (ex: perte de $15\\% \\Rightarrow q = 0,85$). |
        r""")

        st.markdown("---")
        st.subheader("2. Comportement à l'Infini (Limites de $u_n = u_0 \times q^n$ pour $u_0 > 0$)")
        c_lim1, c_lim2, c_lim3 = st.columns(3)
        with c_lim1:
            st.info(r"**Si $q > 1$** : $\\lim_{n \\to +\\infty} u_n = +\\infty$\n\nLa suite diverge vers $+\\infty$ (saturation réseau, explosion mémoire).")
        with c_lim2:
            st.success(r"**Si $0 < q < 1$** : $\\lim_{n \\to +\\infty} u_n = 0$\n\nLa suite converge vers $0$ (atténuation totale d'un signal).")
        with c_lim3:
            st.warning(r"**Si $q = 1$** : $u_n = u_0$ (constante)\n\n**Si $q \le -1$** : Pas de limite (oscillation chaotique).")

        st.markdown("---")
        st.subheader("3. Étude des Variations : La Méthode de la Dérivée")
        st.markdown(r"""
        Lorsqu'une suite est définie par une formule explicite complexe $u_n = f(n)$, on utilise la dérivation continue sur $\\mathbb{R}^+$ pour déterminer son sens de variation :
        1. **Fonction associée** : Remplacer l'entier $n$ par la variable réelle $x$ pour poser $f(x)$ sur $[0 ; +\\infty[$.
        2. **Dérivation** : Calculer $f'(x)$ en utilisant les formules usuelles (souvent $\frac{u}{v} \\Rightarrow f'(x) = \frac{u'v - uv'}{v^2}$).
        3. **Signe** : Étudier le signe du numérateur et du dénominateur (attention : un carré $v^2$ est toujours strictement positif).
        4. **Conclusion** : Dresser le tableau de variation de $f$, puis déduire le sens de variation de la suite $(u_n)$.
        r""")

    with tab_m2:
        st.subheader("🧮 Calculateur Dynamique de Suites")
        col_m_type, col_m_u0, col_m_reason, col_m_n = st.columns(4)
        with col_m_type:
            st_type = st.selectbox("Type de suite :", ["Arithmétique", "Géométrique"])
        with col_m_u0:
            st_u0 = st.number_input("Premier terme $u_0$ :", value=100.0)
        with col_m_reason:
            st_r = st.number_input("Raison ($r$ ou $q$) :", value=0.85 if st_type == "Géométrique" else 5.0)
        with col_m_n:
            st_n = st.number_input("Rang $n$ à calculer :", min_value=0, max_value=100, value=10)

        # Calculations
        if st_type == "Arithmétique":
            un_val = st_u0 + st_n * st_r
            sum_val = (st_n + 1) * (st_u0 + un_val) / 2.0
            formula_txt = f"u_{{{int(st_n)}}} = {st_u0} + {int(st_n)} \times {st_r} = {un_val:.2f}"
        else:
            un_val = st_u0 * (st_r ** st_n)
            if st_r != 1.0:
                sum_val = st_u0 * (1 - (st_r ** (st_n + 1))) / (1 - st_r)
            else:
                sum_val = st_u0 * (st_n + 1)
            formula_txt = f"u_{{{int(st_n)}}} = {st_u0} \times {st_r}^{{{int(st_n)}}} = {un_val:.4f}"

        res_c1, res_c2 = st.columns(2)
        with res_c1:
            st.metric(f"Terme $u_{{{int(st_n)}}}$", f"{un_val:.4f}")
            st.latex(formula_txt)
        with res_c2:
            st.metric(f"Somme $S_{{{int(st_n)}}} = \sum_{{k=0}}^{{{int(st_n)}}} u_k$", f"{sum_val:.4f}")

        # Graph plot
        st.markdown(r"#### Graphique de l'évolution des termes $u_0$ à $u_n$")
        n_values = list(range(int(st_n) + 1))
        if st_type == "Arithmétique":
            u_values = [st_u0 + k * st_r for k in n_values]
        else:
            u_values = [st_u0 * (st_r ** k) for k in n_values]

        df_suite = pd.DataFrame({"Rang n": n_values, "Valeur u_n": u_values}).set_index("Rang n")
        st.line_chart(df_suite)

        st.markdown("---")
        st.subheader("📡 Application Pratique : Atténuation de Signal Optique / Wi-Fi")
        st.info("Chaque mètre de fibre optique ou d'obstacle réduit la puissance du signal d'un pourcentage fixe. Modélisons la puissance restante.")
        
        p_init = st.number_input("Puissance initiale $P_0$ (en mW) :", value=100.0)
        p_loss = st.number_input("Perte par mètre (%) :", value=15.0)
        p_seuil = st.number_input("Seuil minimal de réception $P_{\text{seuil}}$ (en mW) :", value=10.0)

        q_loss = 1.0 - (p_loss / 100.0)
        m_count = 0
        p_curr = p_init
        while p_curr >= p_seuil and m_count < 200:
            p_curr *= q_loss
            m_count += 1

        st.success(f"⚡ **Résultat de portée** : Le signal passe sous le seuil critique de **{p_seuil} mW** au bout de **{m_count} mètres** (Puissance au mètre {m_count} : **{p_curr:.2f} mW**).")

    with tab_m3:
        st.subheader("🐍 Traduction Algorithmique en Python (Sujets d'Examen)")
        st.write("À l'examen écrit de BTS CIEL, on vous demande fréquemment d'écrire ou de compléter des fonctions Python modélisant des suites.")

        col_py1, col_py2 = st.columns(2)
        with col_py1:
            st.markdown("#### Cas n°1 : Calculer une valeur précise (Boucle `FOR`)")
            st.code(r"""
# Calcul du terme de rang n pour une suite géométrique
# Exemple : u_{n+1} = u_n * 0.85 (perte de 15%), u_0 = 100
def calculer_signal(n):
    u = 100.0               # Initialisation (u_0)
    for i in range(n):      # Répète n fois
        u = u * 0.85        # Relation de récurrence
    return u

# Appel
print(calculer_signal(10))  # Affiche u_10
r""", language="python")

        with col_py2:
            st.markdown("#### Cas n°2 : Atteindre un seuil critique (Boucle `WHILE`)")
            st.code(r"""
# Chercher la distance n où le signal passe sous 10 mW
def trouver_perte_signal(seuil=10.0):
    u = 100.0               # Initialisation (u_0)
    n = 0                   # Compteur de rang
    while u >= seuil:       # CONDITION D'ARRÊT INVERSÉE
        u = u * 0.85
        n = n + 1           # Passage au rang suivant
    return n                # Renvoie le rang où u < seuil

# Appel
print(trouver_perte_signal()) # Affiche la distance n
r""", language="python")

        st.markdown("---")
        st.subheader("✍️ Exercice Interactif de Complètement Python")
        st.write(r"Complétez la fonction Python ci-dessous pour calculer la somme des $N$ premiers termes d'une suite arithmétique $u_{n+1} = u_n + 3$ avec $u_0 = 10$ :")

        st.code(r"""
def somme_suite_arithmetique(N):
    u = 10
    somme = 0
    for i in range(N + 1):
        somme += u
        u = # LIGNE À COMPLÉTER
    return somme
r""", language="python")

        user_py_in = st.text_input("Saisissez l'instruction exacte de mise à jour de `u` :", placeholder="u + 3", key="py_math_complete")
        if st.button("Valider la fonction Python", key="btn_val_py_math"):
            clean_in = user_py_in.strip().replace(" ", "")
            if clean_in in ["u+3", "u+=3", "u=u+3"]:
                st.success(r"🎉 **Code exact !** La récurrence arithmétique ajoute la raison $r = 3$ à chaque itération.")
            else:
                st.error(r"❌ Instruction incorrecte. Pour une suite arithmétique de raison $r=3$, la mise à jour est `u = u + 3` (ou `u += 3`).")

    with tab_m4:
        st.subheader("✍️ Exercices d'Examen Corrigés & Quiz Mathématiques")

        with st.expander("📝 Exercice 1 : Rédaction complète de l'étude de variation d'une suite (Explicite)", expanded=True):
            st.markdown(r"""
            **Énoncé** : Soit la suite $(u_n)$ définie pour tout entier $n \ge 0$ par $u_n = \frac{4n + 2}{n + 3}$. Étudier le sens de variation de la suite $(u_n)$.

            **Rédaction type recommandée pour le BTS Blanc** :
            1. Soit $f$ la fonction définie sur $[0 ; +\\infty[$ par $f(x) = \frac{4x + 2}{x + 3}$. On a $u_n = f(n)$.
            2. Calculons la dérivée $f'(x)$ avec la formule $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ :
               - $u(x) = 4x + 2 \\Rightarrow u'(x) = 4$
               - $v(x) = x + 3 \\Rightarrow v'(x) = 1$
               - $f'(x) = \frac{4(x + 3) - (4x + 2) \times 1}{(x + 3)^2} = \frac{4x + 12 - 4x - 2}{(x + 3)^2} = \\mathbf{\frac{10}{(x + 3)^2}}$
            3. Étude du signe :
               - Le numérateur $10 > 0$.
               - Le dénominateur $(x + 3)^2 > 0$ (carré d'un réel strictement positif pour $x \ge 0$).
               - Donc $f'(x) > 0$ sur $[0 ; +\\infty[$.
            4. Conclusion : La fonction $f$ est strictement croissante sur $[0 ; +\\infty[$. On en déduit que la suite $(u_n)$ est **strictement croissante**.
            r""")

        st.markdown("---")
        st.subheader("⚡ Mini-Quiz Mathématiques : Testez vos connaissances")

        q_m1 = st.radio("Q1 : Une fibre optique subit une perte de 5% de sa puissance par kilomètre. Quelle est la raison $q$ de la suite géométrique associée ?", ["q = 0.05", "q = 0.95", "q = 1.05", "q = -0.05"], key="qm1")
        if st.button("Valider Q1", key="btn_qm1"):
            if q_m1 == "q = 0.95":
                st.success(r"✅ **Exact !** Une diminution de 5% correspond au coefficient multiplicateur $q = 1 - \frac{5}{100} = 0,95$.")
            else:
                st.error(r"❌ Mauvaise réponse. Réduction de 5% = $1 - 0,05 = 0,95$.")

        q_m2 = st.radio("Q2 : Quelle est la somme des 10 premiers termes ($u_0$ à $u_9$) de la suite arithmétique de premier terme $u_0 = 5$ et de raison $r = 2$ ?", ["S = 140", "S = 130", "S = 100", "S = 150"], key="qm2")
        if st.button("Valider Q2", key="btn_qm2"):
            if q_m2 == "S = 140":
                st.success(r"✅ **Exact !** $u_9 = 5 + 9 \times 2 = 23$. La somme de $u_0$ à $u_9$ (10 termes) vaut $10 \times \frac{5 + 23}{2} = 140$.")
            else:
                st.error(r"❌ Incorrect. $u_9 = 23$. $S_{10} = 10 \times \frac{5 + 23}{2} = 140$.")


# --- PAGE : RÉVISION TOTALE BTS BLANC (9-11 DÉCEMBRE) ---

# --- PAGE FICHES SAVOIR & FICHES MONTAGE ---
elif page == "🛠️ Fiches Réussite Épreuve E5 (TP & Pratique)":
    st.markdown("<div class='hero-title'>🛠️ Fiches Réussite Épreuve E5 : TP & Pratiques de Terrain</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Guide complet, procédures pas-à-pas et fiches réflexes d'intervention pour réussir haut la main l'épreuve pratique E5 (Réseaux, SysAdmin, Cybersécurité & Électronique)</p>", unsafe_allow_html=True)

    tab_e5_1, tab_e5_2, tab_e5_3, tab_e5_4, tab_e5_5, tab_e5_6, tab_e5_7, tab_e5_8 = st.tabs([
        "📶 E5-01 : Cisco IOS (Switch & Routeur)",
        "🖥️ E5-02 : Linux Debian & SysAdmin",
        "🏢 E5-03 : Active Directory, DNS, DHCP & GPO",
        "🛡️ E5-04 : Pare-Feu pfSense, DMZ & Flux",
        "🔍 E5-05 : Wireshark & Trames",
        "⚡ E5-06 : Électronique & Bus",
        "📋 E5-07 : Check-List Diagnostic E5",
        "✍️ Auto-Évaluation Pratique E5"
    ])

    # === TAB 1 : CISCO IOS ===
    with tab_e5_1:
        st.subheader("📶 Fiche E5-01 : Commutateurs & Routeurs Cisco (Configuration & Dépannage)")
        st.markdown(r"""
        <div class='ciel-card' style='border-left: 6px solid #2563eb !important;'>
            <h4 style='color:#1d4ed8; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Cisco :</h4>
            <p style='color:#334155; margin-bottom:0;'>Être capable d'initialiser, sécuriser, segmentez en VLANs (802.1Q), configurer le routage inter-VLAN et appliquer le Port Security sur les équipements Cisco de l'atelier.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("1️⃣ Configuration Initiale & Sécurisation de Base (Switch/Routeur)", expanded=True):
            st.markdown(r"""
            ```cisco
            enable
            configure terminal
            hostname SW-L2-CIEL
            enable secret CiscoPass123!
            
            ! Sécurisation de l'accès Console
            line console 0
              password ConsolePass!
              login
              logging synchronous
              exit
              
            ! Sécurisation des lignes VTY (SSH / Telnet)
            line vty 0 15
              password VtyPass!
              login
              transport input ssh
              exit
              
            ! Chiffrement des mots de passe en clair dans le fichier de config
            service password-encryption
            
            ! Bannière d'avertissement légal
            banner motd # ACCES RESTREINT - BTS CIEL E5 - UTILISATEURS AUTORISES SEULEMENT #
            ```
            """)

        with st.expander("2️⃣ Configuration des VLANs & Assignation des Ports d'Accès", expanded=False):
            st.markdown(r"""
            ```cisco
            ! 1. Création des VLANs dans la base de données
            vlan 10
              name RESEAU_ADMIN
            vlan 20
              name RESEAU_PROD
            vlan 30
              name DMZ_SERVEURS
            vlan 99
              name GESTION_NATIVE
            exit
            
            ! 2. Assignation d'une plage de ports au VLAN 10 (Mode Access)
            interface range FastEthernet 0/1 - 10
              switchport mode access
              switchport access vlan 10
              spanning-tree portfast          ! Active l'accès immédiat sans délai STP
              no shutdown
            ```
            """)

        with st.expander("3️⃣ Configuration de la Liaison Agrégée Trunking (IEEE 802.1Q)", expanded=False):
            st.markdown(r"""
            ```cisco
            interface GigabitEthernet 0/1
              switchport trunk encapsulation dot1q    ! Obligatoire sur switchs L3
              switchport mode trunk
              switchport trunk allowed vlan 10,20,30,99
              switchport trunk native vlan 99         ! Sécurisation du VLAN natif
              no shutdown
            ```
            """)

        with st.expander("4️⃣ Routage Inter-VLAN (Router-on-a-Stick sur Routeur)", expanded=False):
            st.markdown(r"""
            ```cisco
            ! Sur le Routeur R1 (Relier g0/0 au port Trunk du Switch)
            interface GigabitEthernet 0/0
              no shutdown                             ! Activer l'interface physique
              
            ! Subinterface pour le VLAN 10
            interface GigabitEthernet 0/0.10
              encapsulation dot1Q 10
              ip address 192.168.10.254 255.255.255.0
              
            ! Subinterface pour le VLAN 20
            interface GigabitEthernet 0/0.20
              encapsulation dot1Q 20
              ip address 192.168.20.254 255.255.255.0
            ```
            """)

        with st.expander("5️⃣ Sécurité des Ports (Port Security)", expanded=False):
            st.markdown(r"""
            ```cisco
            interface FastEthernet 0/5
              switchport mode access
              switchport access vlan 10
              switchport port-security
              switchport port-security maximum 2              ! Max 2 adresses MAC autorisées
              switchport port-security mac-address sticky     ! Apprend automatiquement la MAC
              switchport port-security violation shutdown    ! Met le port en err-disable si intrusion
            ```
            """)

        with st.expander("🔍 Commandes de Diagnostic & Vérification E5 (Boîte à Outils)", expanded=False):
            st.markdown(r"""
            | Commande Cisco IOS | Objectif de Vérification E5 |
            | :--- | :--- |
            | `show vlan brief` | Vérifier que tous les VLANs existent et que les bons ports sont attribués. |
            | `show interfaces trunk` | Vérifier que le lien Trunk est actif, en 802.1Q, et que les VLANs passent. |
            | `show ip interface brief` | Vérifier l'état physique (`Status`) et logique (`Protocol`) des interfaces (`up/up`). |
            | `show ip route` | Inspecter la table de routage IP du routeur ou switch L3. |
            | `show port-security interface f0/5` | Vérifier si un port est bloqué suite à une violation d'adresse MAC (`err-disabled`). |
            | `show running-config` | Consulter la configuration active en mémoire vive (RAM). |
            """)

    # === TAB 2 : LINUX DEBIAN ===
    with tab_e5_2:
        st.subheader("🖥️ Fiche E5-02 : Linux Debian Server & Administration Système")
        st.markdown(r"""
        <div class='ciel-card' style='border-left: 6px solid #10b981 !important;'>
            <h4 style='color:#065f46; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Linux :</h4>
            <p style='color:#334155; margin-bottom:0;'>Savoir configurer le réseau fixe, gérer les utilisateurs/groupes, appliquer les permissions fines (`chmod`, SUID, SGID, Sticky, ACLs), éditer `sudoers`, écrire des scripts Bash et gérer les services systemd.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("1️⃣ Configuration Réseau Fixe (`/etc/network/interfaces`)", expanded=True):
            st.markdown(r"""
            ```bash
            # Éditer le fichier de configuration réseau
            nano /etc/network/interfaces

            # Configuration statique de l'interface eth0
            auto eth0
            iface eth0 inet static
                address 192.168.1.100/24
                gateway 192.168.1.254
                dns-nameservers 192.168.1.200 8.8.8.8

            # Appliquer les modifications
            systemctl restart networking
            # Ou avec la commande ip :
            ip addr add 192.168.1.100/24 dev eth0
            ip route add default via 192.168.1.254
            ```
            """)

        with st.expander("2️⃣ Gestion des Utilisateurs, Groupes & Privilèges Sudo", expanded=False):
            st.markdown(r"""
            ```bash
            # 1. Création d'un groupe d'ingénieurs
            groupadd -g 2000 tech_ciel

            # 2. Création d'un utilisateur avec son répertoire personnel /home/antoine
            useradd -m -u 1500 -g tech_ciel -s /bin/bash antoine
            passwd antoine

            # 3. Ajout au groupe sudo pour les privilèges d'administration
            usermod -aG sudo antoine

            # 4. Configuration fine de Sudoers (/etc/sudoers.d/ciel)
            echo "antoine ALL=(ALL:ALL) ALL" > /etc/sudoers.d/ciel
            # Autorisateurs sans mot de passe pour un service spécifique :
            echo "%tech_ciel ALL=(ALL) NOPASSWD: /bin/systemctl restart apache2" >> /etc/sudoers.d/ciel
            chmod 0440 /etc/sudoers.d/ciel
            ```
            """)

        with st.expander("3️⃣ Permissions Octales, Droits Spéciaux & ACLs POSIX", expanded=False):
            st.markdown(r"""
            * **Permissions Classiques (`chmod`)** :
              - `chmod 750 /opt/deploy.sh` $\rightarrow$ Owner: `rwx` (7), Group: `r-x` (5), Others: `---` (0).
            * **Droits Spéciaux** :
              - **SUID (4000)** : `chmod 4755 /usr/bin/mon_prog` (S'exécute avec les privilèges du propriétaire `root`).
              - **SGID (2000)** : `chmod 2770 /data/partage` (Les nouveaux fichiers héritent du groupe du dossier).
              - **Sticky Bit (1000)** : `chmod 1777 /tmp` (Seul le propriétaire d'un fichier peut le supprimer dans un dossier public).
            * **ACLs POSIX (`setfacl` & `getfacl`)** :
              - Accorder les droits `rwx` à l'utilisateur `alice` : `setfacl -m u:alice:rwx /var/www/html`
              - Accorder `r-x` au groupe `tech_ciel` : `setfacl -m g:tech_ciel:rx /var/www/html`
              - Consulter les ACLs : `getfacl /var/www/html`
              - Supprimer les ACLs : `setfacl -b /var/www/html`
            """)

        with st.expander("4️⃣ Modèle de Script Bash d'Examen E5", expanded=False):
            st.markdown(r"""
            ```bash
            #!/bin/bash
            # Script d'automatisation E5 : Vérification des services et sauvegarde
            LOGFILE="/var/log/e5_check.log"
            BACKUP_DIR="/var/backups/ciel"

            mkdir -p $BACKUP_DIR
            echo "=== Diagnostic E5 - $(date) ===" > $LOGFILE

            # Boucle de vérification des services
            for srv in networking apache2 ssh; do
                if systemctl is-active --quiet $srv; then
                    echo "[OK] Service $srv est opérationnel." >> $LOGFILE
                else
                    echo "[ALERTE] Service $srv est ARRÊTÉ. Tentative de relance..." >> $LOGFILE
                    systemctl restart $srv
                fi
            done

            # Compression du dossier Web
            tar -czf "$BACKUP_DIR/web_$(date +%Y%m%d).tar.gz" /var/www/html 2>> $LOGFILE
            echo "Sauvegarde terminée." >> $LOGFILE
            ```
            """)

        with st.expander("🔍 Commandes de Diagnostic Linux E5", expanded=False):
            st.markdown(r"""
            | Commande Linux | Rôle Diagnostic E5 |
            | :--- | :--- |
            | `ip a` / `ip route` | Vérifier les adresses IP configurées et la passerelle par défaut. |
            | `ss -tulpn` / `netstat -an` | Lister tous les ports TCP/UDP en écoute et leurs PID. |
            | `systemctl status <service>` | Inspecter l'état d'un service (active, dead, failed). |
            | `journalctl -u <service> -n 30` | Consulter les 30 dernières lignes de journal systemd d'un service. |
            | `tail -f /var/log/auth.log` | Suivre en temps réel les tentatives de connexion et d'authentification. |
            | `df -h` / `free -m` | Vérifier l'occupation de l'espace disque et la mémoire RAM disponible. |
            """)

    # === TAB 3 : ACTIVE DIRECTORY ===
    with tab_e5_3:
        st.subheader("🏢 Fiche E5-03 : Active Directory, DNS, DHCP & GPO (Windows Server)")
        st.markdown(r"""
        <div class='ciel-card' style='border-left: 6px solid #8b5cf6 !important;'>
            <h4 style='color:#6d28d9; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Active Directory :</h4>
            <p style='color:#334155; margin-bottom:0;'>Maîtriser la gestion de domaine ADDS, la création d'OU, d'utilisateurs/groupes, le déploiement de GPO (LSDOU), et les services d'infrastructure DNS / DHCP.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("1️⃣ Arborescence ADDS & Commandes PowerShell d'Administration", expanded=True):
            st.markdown(r"""
            ```powershell
            # 1. Créer la structure d'Unités d'Organisation (OU)
            New-ADOrganizationalUnit -Name "Direction" -Path "DC=ciel,DC=local"
            New-ADOrganizationalUnit -Name "Ingénieurs" -Path "DC=ciel,DC=local"
            New-ADOrganizationalUnit -Name "Techniciens" -Path "DC=ciel,DC=local"

            # 2. Créer un utilisateur dans une OU
            New-ADUser -Name "Alice Martin" `
                       -GivenName "Alice" `
                       -Surname "Martin" `
                       -UserPrincipalName "amartin@ciel.local" `
                       -SamAccountName "amartin" `
                       -Path "OU=Ingénieurs,DC=ciel,DC=local" `
                       -AccountPassword (Read-Host -AsSecureString "Password123!") `
                       -Enabled $true `
                       -ChangePasswordAtLogon $false

            # 3. Créer un groupe de sécurité et ajouter le membre
            New-ADGroup -Name "G_Ingenieurs" -GroupScope Global -GroupCategory Security `
                        -Path "OU=Ingénieurs,DC=ciel,DC=local"
            Add-ADGroupMember -Identity "G_Ingenieurs" -Members "amartin"
            ```
            """)

        with st.expander("2️⃣ Stratégies de Groupe (GPO) & Ordre d'Application LSDOU", expanded=False):
            st.markdown(r"""
            * **Ordre d'application LSDOU** :
              1. **L**ocal (Stratégie locale de la machine)
              2. **S**ite (Site Active Directory)
              3. **D**omaine (`ciel.local`)
              4. **OU** (Unité d'Organisation spécifique)
              *Règle d'or* : La stratégie la plus proche de l'objet (OU) prévaut sur la stratégie parente (Domaine).
            * **Cas d'usage E5 fréquents** :
              - Mappage automatique de lecteur réseau (`G:` $\rightarrow$ `\\SRV-FILE\PartageData`).
              - Restriction du Panneau de Configuration et de l'invite de commande CMD.
              - Déploiement d'un fond d'écran d'entreprise obligatoire.
            * **Commandes de rafraîchissement & diagnostic GPO** :
              - `gpupdate /force` (Sur le poste client)
              - `gpresult /r` ou `rsop.msc` (Consulter le jeu de stratégies résultant).
            """)

        with st.expander("3️⃣ Service DNS (Zones de Recherche Directe & Inverse)", expanded=False):
            st.markdown(r"""
            * **Zone de Recherche Directe** (`ciel.local`) :
              - Enregistrement `A` : `srv-web.ciel.local` $\rightarrow$ `192.168.1.50`
              - Enregistrement `AAAA` : IPv6 de l'hôte.
              - Enregistrement `CNAME` (Alias) : `www.ciel.local` $\rightarrow$ `srv-web.ciel.local`
              - Enregistrement `MX` : Serveur de messagerie du domaine.
            * **Zone de Recherche Inverse** (`1.168.192.in-addr.arpa`) :
              - Enregistrement `PTR` : `192.168.1.50` $\rightarrow$ `srv-web.ciel.local` (Indispensable pour Kerberos et Active Directory !).
            """)

        with st.expander("4️⃣ Service DHCP (Étendues, Options & Baux)", expanded=False):
            st.markdown(r"""
            * **Configuration d'Étendue (Scope)** :
              - Plage IP : `192.168.1.100` à `192.168.1.200` / Masque `/24`.
              - Dépassement / Exclusions : `192.168.1.1` à `192.168.1.20` (Réservées aux équipements fixes).
            * **Options DHCP Clés en E5** :
              - Option `003` : Router (Passerelle par défaut = `192.168.1.254`).
              - Option `006` : DNS Servers (IP du Contrôleur de Domaine = `192.168.1.200`).
              - Option `015` : DNS Domain Name (`ciel.local`).
            * **Réservation DHCP** : Association permanente d'une adresse IP fixe à une adresse MAC d'imprimante ou de caméra IP.
            """)

        with st.expander("🔍 Commandes Diagnostic Active Directory / Windows Server", expanded=False):
            st.markdown(r"""
            | Commande PowerShell / CMD | Rôle Diagnostic E5 |
            | :--- | :--- |
            | `dcdiag` | Diagnostic complet de santé du Contrôleur de Domaine Active Directory. |
            | `nslookup srv-web.ciel.local` | Tester la résolution de nom DNS directe et inverse. |
            | `Test-NetConnection -ComputerName srv-ad -Port 389` | Tester l'ouverture du port LDAP (389) ou LDAPS (636). |
            | `nltest /dsgetdc:ciel.local` | Vérifier quel contrôleur de domaine a authentifié la machine. |
            | `ipconfig /all` & `ipconfig /flushdns` | Afficher la config IP et vider le cache DNS client. |
            """)

    # === TAB 4 : PFSENSE & DMZ ===
    with tab_e5_4:
        st.subheader("🛡️ Fiche E5-04 : Pare-Feu pfSense, DMZ & Matrice des Flux")
        st.markdown(r"""
        <div class='ciel-card' style='border-left: 6px solid #ef4444 !important;'>
            <h4 style='color:#b91c1c; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur pfSense :</h4>
            <p style='color:#334155; margin-bottom:0;'>Configurer les zones WAN, LAN et DMZ, appliquer la règle d'isolation stricte DMZ $\rightarrow$ LAN, mettre en place les règles de filtrage et le NAT/PAT Port Forwarding.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("1️⃣ Architecture Réseau à 3 Interfaces & Adressage", expanded=True):
            st.markdown(r"""
            * **WAN (Wide Area Network)** : Interface d'accès externe (`10.0.0.2/24` ou IP Publique).
            * **LAN (Local Area Network)** : Zone réseau interne sécurisée (`192.168.1.254/24`).
            * **DMZ (Demilitarized Zone)** : Zone réseau isolée hébergeant les services ouverts à l'extérieur (`172.16.0.254/24`).
            """)

        with st.expander("2️⃣ Règle d'Or d'Isolation de la DMZ (Inviolable)", expanded=False):
            st.markdown(r"""
            <div class='ciel-card' style='background:#fef2f2 !important; border-left: 5px solid #dc2626 !important;'>
                <b style='color:#991b1b;'>⚠️ Règle de Sécurité Numéro 1 en E5 :</b><br>
                Une machine située en <b>DMZ ne doit JAMAIS pouvoir initier de connexion vers le réseau LAN interne</b>.<br>
                Si le serveur Web DMZ est compromis par un pirate, celui-ci ne pourra pas attaquer les postes du réseau LAN.
            </div>
            """, unsafe_allow_html=True)

        with st.expander("3️⃣ Matrice des Ports & Flux Réseaux de Référence (À Apprendre par Cœur)", expanded=False):
            st.markdown(r"""
            | Service | Protocole | Port | Sens Recommandé | Rôle & Explication |
            | :--- | :--- | :--- | :--- | :--- |
            | **DNS** | UDP / TCP | `53` | LAN -> DMZ / WAN | Résolution de noms de domaine. |
            | **HTTP / HTTPS** | TCP | `80` / `443` | WAN -> DMZ (NAT) | Accès aux serveurs Web publics. |
            | **SSH** | TCP | `22` | LAN -> DMZ | Administration à distance sécurisée. |
            | **LDAP / LDAPS** | TCP | `389` / `636` | LAN -> DC | Annuaire d'entreprise ADDS. |
            | **Kerberos AD** | TCP / UDP | `88` | LAN -> DC | Jetons d'authentification AD. |
            | **SMB / CIFS** | TCP | `445` | LAN -> FileSRV | Partage de fichiers Windows. |
            | **MQTTS** | TCP | `8883` | DMZ -> IoT Broker | Transport IoT chiffré TLS. |
            """)

        with st.expander("4️⃣ Procédure de Configuration NAT / PAT (Port Forwarding pfSense)", expanded=False):
            st.markdown(r"""
            1. Aller dans **Firewall $\rightarrow$ NAT $\rightarrow$ Port Forward**.
            2. Cliquer sur **Add (Top)** :
               - **Interface** : `WAN`
               - **Protocol** : `TCP`
               - **Destination** : `WAN Address`
               - **Destination Port Range** : `HTTP (80)`
               - **Redirect Target IP** : `172.16.0.10` (IP du serveur Web DMZ)
               - **Redirect Target Port** : `HTTP (80)`
               - **Filter Rule Association** : `Pass` (Génère la règle de pare-feu automatiquement)
            3. Cliquer sur **Save** puis **Apply Changes**.
            """)

    # === TAB 5 : WIRESHARK ===
    with tab_e5_5:
        st.subheader("🔍 Fiche E5-05 : Wireshark & Diagnostics de Trames Réseaux")
        st.markdown(r"""
        <div class='ciel-card' style='border-left: 6px solid #0284c7 !important;'>
            <h4 style='color:#0369a1; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Wireshark :</h4>
            <p style='color:#334155; margin-bottom:0;'>Capturer, filtrer et décoder des paquets réseaux pour identifier un dysfonctionnement, réconcilier une connexion TCP ou analyser un protocole applicatif.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("1️⃣ Filtres d'Affichage Wireshark Essentiels pour l'Examen", expanded=True):
            st.markdown(r"""
            | Filtre d'Affichage Wireshark | Rôle Diagnostic E5 |
            | :--- | :--- |
            | `ip.addr == 192.168.1.50` | Filtrer tout le trafic concernant une adresse IP spécifique. |
            | `tcp.port == 443` | Isoler le trafic Web sécurisé HTTPS. |
            | `tcp.flags.syn == 1 and tcp.flags.ack == 0` | Identifier les demandes de connexion TCP (Handshake SYN). |
            | `dns.qname contains "ciel"` | Filtrer les requêtes DNS portant sur le domaine d'examen. |
            | `dhcp.option.dhcp == 3` | Filtrer les paquets DHCP Request lors d'un bail d'adresse. |
            | `arp.opcode == 2` | Filtrer les réponses ARP (Utile pour détecter un ARP Spoofing). |
            | `http.request.method == "POST"` | Inspecter les envois de formulaires et identifiants en clair. |
            """)

        with st.expander("2️⃣ Méthodologie d'Analyse d'une Séquence TCP 3-Way Handshake", expanded=False):
            st.markdown(r"""
            ```
            Client (192.168.1.10)                        Serveur (192.168.1.50:80)
                   |                                                 |
                   |------- [SYN] Seq=0 ----------------------------->|  (Étape 1 : Demande)
                   |<------ [SYN, ACK] Seq=0 Ack=1 ------------------|  (Étape 2 : Accord)
                   |------- [ACK] Seq=1 Ack=1 ---------------------->|  (Étape 3 : Validation)
                   |                                                 |
            ```
            * **Anomalie d'examen** : Si le serveur répond par `[RST, ACK]`, le port est fermé ou rejeté par un pare-feu !
            """)

        with st.expander("3️⃣ Fonctionnalité 'Follow TCP Stream' & Export d'Objets", expanded=False):
            st.markdown(r"""
            * **Follow TCP Stream** : Clic droit sur un paquet TCP $\rightarrow$ *Follow $\rightarrow$ TCP Stream*. Permet de reconstituer l'intégralité du dialogue applicatif (HTTP, SMTP, FTP, Modbus) en texte clair.
            * **Exportation d'Objets HTTP** : Menu *File $\rightarrow$ Export Objects $\rightarrow$ HTTP*. Permet d'extraire un fichier (image, PDF, binaire) téléchargé pendant la capture.
            """)

    # === TAB 6 : ÉLECTRONIQUE & BUS ===
    with tab_e5_6:
        st.subheader("⚡ Fiche E5-06 : Électronique, Oscilloscope & Bus Industriels")
        st.markdown(r"""
        <div class='ciel-card' style='border-left: 6px solid #eab308 !important;'>
            <h4 style='color:#a16207; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur l'Atelier Électronique :</h4>
            <p style='color:#334155; margin-bottom:0;'>Régler les calibres de l'oscilloscope, effectuer des mesures de tension/période/fréquence, calculer des quantums CAN, et contrôler le signal sur les bus I2C, SPI, CAN ou Modbus.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("1️⃣ Mesures Physiques à l'Oscilloscope Numérique", expanded=True):
            st.markdown(r"""
            * **Tension Crête-à-Crête $V_{pp}$** : $V_{pp} = N_{\text{div\_vert}} \times S_v$
            * **Tension Maximale $V_{max}$** : $V_{max} = \frac{V_{pp}}{2}$
            * **Tension Efficace $V_{\text{eff}}$** : $V_{\text{eff}} = \frac{V_{max}}{\sqrt{2}} \approx 0,707 \times V_{max}$ (Signal sinusoïdal)
            * **Période $T$** : $T = N_{\text{div\_horiz}} \times S_h$
            * **Fréquence $f$** : $f = \frac{1}{T}$
            * **Déphasage $\Delta \phi$** : $\Delta \phi = 360^\circ \times \frac{\Delta t}{T}$
            """)

        with st.expander("2️⃣ Convertisseurs CAN / CNA (ADC / DAC)", expanded=False):
            st.markdown(r"""
            * **Quantum $q$** : $q = \frac{V_{\text{ref}}}{2^n - 1}$
              - *Exemple CAN 12 bits sous 5,0V* : $q = \frac{5,0}{4095} \approx 1,221\text{ mV}$.
            * **Valeur Numérique Entière $N$** : $N = \text{arrondi}\left(\frac{V_e}{q}\right)$
              - *Exemple pour $V_e = 2,5\text{ V}$* : $N = \text{arrondi}\left(\frac{2,5}{0,001221}\right) = 2048$.
            """)

        with st.expander("3️⃣ Synthèse des Bus Industriels de Terrain (Atelier E5)", expanded=False):
            st.markdown(r"""
            | Bus de Terrain | Lignes Physiques | Type de Signal | Spécificités & Points de Contrôle E5 |
            | :--- | :--- | :--- | :--- |
            | **I2C** | 2 fils (`SDA`, `SCL`) | Synchrone | Résistances de tirage Pull-Up ($4,7\text{ k}\Omega$). Adressage 7 bits. |
            | **SPI** | 4 fils (`MOSI`, `MISO`, `SCLK`, `CS`) | Synchrone Full-Duplex | Liaison maître-esclave très rapide (plusieurs MHz). |
            | **Bus CAN** | 2 fils (`CAN_H`, `CAN_L`) | Différentiel | Résistances de terminaison de $120\ \Omega$. Bit dominant 0 / récessif 1. |
            | **Modbus RTU** | 2 fils (`A`, `B` / RS-485) | Différentiel Asynchrone | Code Fonction `03` (Read Holding Registers), contrôle CRC-16. |
            """)

    # === TAB 7 : CHECK-LIST DIAGNOSTIC ===
    with tab_e5_7:
        st.subheader("📋 Fiche E5-07 : Check-List Diagnostic & Grille d'Intervention E5")
        st.markdown(r"""
        <div class='ciel-card' style='border-top: 5px solid #2563eb !important;'>
            <h4 style='color:#1d4ed8; margin-top:0;'>🧭 Guide Méthodologique de Résolution de Panne en 5 Étapes :</h4>
            <p style='color:#334155;'>Suivez rigoureusement ce protocole lors de vos évaluations pratiques E5 pour ne négliger aucun point du barème :</p>
            
            ```
            [Étape 1 : Vérification Couche 1 Physique]
              └── Câble RJ45 / Fibre correctement encliqueté ? Voyants Link/Act allumés ? Équipement alimenté ?
            
            [Étape 2 : Vérification Couche 2 Liaison]
              └── Adresse MAC détectée ? Port du switch dans le bon VLAN ? (`show vlan brief` / `ip link`)
            
            [Étape 3 : Vérification Couche 3 Réseau]
              └── IP, Masque et Passerelle configurés ? PING passerelle OK ? PING DNS OK ? (`ping 192.168.1.254`)
            
            [Étape 4 : Vérification Couche 4/7 Transport & Application]
              └── Port ouvert sur la cible ? Service démarré ? (`ss -tulpn` / `nc -zvw3 IP PORT` / `curl -Iv`)
            
            [Étape 5 : Documentation & Compte-Rendu d'Intervention]
              └── Rédiger la fiche de synthèse d'examen avec les symptômes, la cause racine et la solution appliquée.
            ```
        </div>
        """, unsafe_allow_html=True)

    # === TAB 8 : AUTO-ÉVALUATION ===
    with tab_e5_8:
        st.subheader("✍️ Auto-Évaluation Pratique E5 (QCM de Validation)")
        st.markdown("Testez vos réflexes d'intervention pratique avant de passer devant les examinateurs :")

        q_e5_list = [
            {"q": "1. Sur un commutateur Cisco, quelle commande permet d'associer le port f0/5 au VLAN 20 en mode accès ?", "opts": ["switchport access vlan 20", "vlan 20 enable", "ip route vlan 20", "trunk access vlan 20"], "rep": "switchport access vlan 20", "expl": "La commande correcte est 'switchport access vlan 20' sous l'interface f0/5."},
            {"q": "2. Sous Linux Debian, quel masque octal chmod accorde rwx au propriétaire, r-x au groupe et aucun droit aux autres ?", "opts": ["755", "750", "644", "777"], "rep": "750", "expl": "rwx = 7, r-x = 5, --- = 0, d'où 750."},
            {"q": "3. Dans pfSense, quelle est la règle de filtrage absolue concernant les initiations de connexions depuis la DMZ ?", "opts": ["La DMZ peut tout initier vers le LAN", "La DMZ ne doit JAMAIS initier de connexion vers le LAN", "La DMZ est isolée du WAN", "La DMZ utilise le port 80 uniquement"], "rep": "La DMZ ne doit JAMAIS initier de connexion vers le LAN", "expl": "Pour préserver le LAN, toute initiation de connexion depuis la DMZ vers le LAN est strictement bloquée."},
            {"q": "4. Dans Wireshark, quel filtre d'affichage permet d'isoler uniquement les requêtes Web chiffrées HTTPS ?", "opts": ["ip.port == 80", "tcp.port == 443", "http.flags == syn", "ssl.mode == pass"], "rep": "tcp.port == 443", "expl": "HTTPS utilise le port TCP 443."},
            {"q": "5. Quelle est la valeur de la résistance de terminaison requise aux deux extrémités d'un bus CAN ?", "opts": ["50 Ohms", "75 Ohms", "120 Ohms", "1000 Ohms"], "rep": "120 Ohms", "expl": "Deux résistances de 120 Ohms permettent d'adapter l'impédance de la ligne et d'éviter les réflexions de signal."}
        ]

        score_e5 = 0
        for idx_e5, qe5 in enumerate(q_e5_list):
            st.markdown(f"**{qe5['q']}**")
            ans_e5 = st.radio(f"Choix Q{idx_e5+1} E5 :", qe5["opts"], key=f"q_e5_tab_{idx_e5}")
            if ans_e5 == qe5["rep"]:
                score_e5 += 1

        if st.button("Soumettre mon évaluation E5", type="primary", key="btn_submit_e5_page"):
            st.session_state["score_e5_eval"] = score_e5
            st.success(f"🏆 **Score obtenu sur l'Épreuve E5** : **{score_e5} / {len(q_e5_list)}** ({(score_e5/len(q_e5_list))*100:.1f}%)")
            if score_e5 == len(q_e5_list):
                st.balloons()


elif page == "📄 Fiches Savoir & Fiches Montage":
    st.markdown("<div class='hero-title'>📄 Recueil Officiel des Fiches Savoir & Fiches Montage</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Guide complet, exhaustif et verbatim de toutes les Fiches Savoir (N°1 à N°12), Fiche Physique et Fiches Montage (N°1 & N°2) du BTS CIEL (Option A)</p>", unsafe_allow_html=True)

    tab_fs1, tab_fs2, tab_fs3, tab_fs4, tab_fs5 = st.tabs([
        "⚡ Fiches Savoir Électronique (1 à 4 & Physique)",
        "💻 Fiches Savoir Informatique (5 à 8)",
        "📶 Fiches Savoir Réseaux & Com (9 à 12)",
        "🛠️ Fiches Montage (N°1 & N°2)",
        "✍️ Auto-Évaluation Fiches Savoir"
    ])

    with tab_fs1:
        st.subheader("⚡ Fiches Savoir : Électronique, Puissance & Signaux")

        with st.expander("📄 FICHE SAVOIR N°1 : Le Pont en H (Contrôle de Moteur CC)", expanded=True):
            st.markdown(r"""
            **Rôle Fonctionnel** : Contrôler le sens de rotation d'un moteur à courant continu (CC / bipolaire) en inversant la polarité d'alimentation à ses bornes.

            #### Schéma de Principe & Table d'États :
            ```
                +Vcc (Alimentation Puissance)
                 |
            +----+----+
            |         |
          [Int1]    [Int3]
            |         |
            +--[M]----+  <-- Moteur CC
            |         |
          [Int2]    [Int4]
            |         |
            +----+----+
                 |
                GND
            ```
            | Interrupteurs Fermés | Interrupteurs Ouverts | Sens de Rotation Moteur |
            | :--- | :--- | :--- |
            | **Inter 1 & Inter 4** | Inter 2 & Inter 3 | Sens Anti-Horaire (Sens 1) |
            | **Inter 2 & Inter 3** | Inter 1 & Inter 4 | Sens Horaire (Sens 2) |
            | *Tous ouverts* | Tous fermés | Arrêt / Roue libre |

            ⚠️ **Règle d'or de sécurité matérielle** : Inter 1 et Inter 2 (ou Inter 3 et Inter 4) ne doivent **jamais** être fermés simultanément sous peine de provoquer un **court-circuit direct** de l'alimentation (*Shooting Through* / destruction immédiate du pont).

            #### Composant Industriel Type : Module Double Pont en H BTS7960 43A
            - **Pins de contrôle** : `R_EN` / `L_EN` (Enable sens droit/gauche), `R_PWM` / `L_PWM` (Commandes de vitesse PWM), `R_IS` / `L_IS` (Mesure de courant).
            ```cpp
            // Programme Arduino de test BTS7960
            int R_IS = 6, R_EN = 2, R_PWM = 3;
            int L_IS = 7, L_EN = 4, L_PWM = 5;

            void setup() {
              pinMode(R_IS, OUTPUT); pinMode(R_EN, OUTPUT); pinMode(R_PWM, OUTPUT);
              pinMode(L_IS, OUTPUT); pinMode(L_EN, OUTPUT); pinMode(L_PWM, OUTPUT);
              digitalWrite(R_IS, LOW); digitalWrite(L_IS, LOW);
              digitalWrite(R_EN, HIGH); digitalWrite(L_EN, HIGH); // Activation des deux demi-ponts
            }

            void loop() {
              int i;
              for (i = 0; i <= 255; i += 10) { // Acceleration sens horaire
                analogWrite(R_PWM, i); analogWrite(L_PWM, 0); delay(500);
              }
              delay(500);
              for (i = 0; i <= 255; i += 10) { // Acceleration sens anti-horaire
                analogWrite(R_PWM, 0); analogWrite(L_PWM, i); delay(500);
              }
              delay(500);
            }
            ```
            r""")

        with st.expander("📄 FICHE SAVOIR N°1 (Physique) : Lois Fondamentales de l'Électricité", expanded=False):
            st.markdown(r"""
            #### 1. Loi d'Ohm & Conventions
            - **Loi d'Ohm en Convention Récepteur** : $U_{AB} = R \cdot I$. La flèche de tension $U$ est orientée en sens opposé à la flèche d'intensité $I$.
            - **Conductance** : Inverse de la résistance, notée $G = \frac{1}{R}$ en Siemens ($S$). La loi d'Ohm devient $I = G \cdot U_{AB}$.

            #### 2. Lois de Kirchhoff
            - **Loi des Nœuds (Conservation de la charge)** : La somme des courants entrants dans un nœud est égale à la somme des courants sortants :
              $$\sum I_{\text{entrants}} = \sum I_{\text{sortants}} \quad \Longleftrightarrow \quad \sum \pm I_k = 0$$
            - **Loi des Mailles (Conservation de l'énergie)** : La somme algébrique des tensions le long d'une maille fermée orientée est nulle :
              $$\sum U_k = 0$$

            #### 3. Associations de Résistances
            - **Série** : $R_{\text{eq}} = R_1 + R_2 + \dots + R_n$. $\frac{1}{G_{\text{eq}}} = \frac{1}{G_1} + \frac{1}{G_2}$.
            - **Parallèle** : $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots + \frac{1}{R_n}$. Pour 2 résistances : $R_{\text{eq}} = \frac{R_1 \cdot R_2}{R_1 + R_2}$. $G_{\text{eq}} = G_1 + G_2$.

            #### 4. Ponts Diviseurs de Tension & Courant
            - **Pont Diviseur de Tension** : Pour 2 résistances en série alimentées sous $E$ :
              $$U_2 = E \cdot \frac{R_2}{R_1 + R_2}$$
              Formule d'isolation de $R_2$ : $R_2 = \frac{U_2 \cdot R_1}{E - U_2}$.
            - **Pont Diviseur de Courant** : Pour 2 résistances en parallèle traversées par un courant $I$ :
              $$I_1 = I \cdot \frac{R_2}{R_1 + R_2} = I \cdot \frac{G_1}{G_1 + G_2}$$

            #### 5. Puissance & Énergie
            - **Puissance électrique** : $P = U \cdot I = R \cdot I^2 = \frac{U^2}{R}$ (en Watts $W$ ou $J/s$).
            - **Énergie électrique** : $E = P \cdot \Delta t$ (en Joules $J$ ou $Wh$).
            - **Générateur Réel** : Tension $U = E - r \cdot I$. Puissance disponible $P = E \cdot I - r \cdot I^2$ ($E \cdot I$ est la puissance électromotrice totale, $r \cdot I^2$ est la perte Joule interne).
            - **Capacité de Batterie** : $C = I \cdot \Delta t$ en Ampères-heures ($Ah$) ou $A \cdot s$ ($Coulombs$).
            r""")

        with st.expander("📄 FICHE SAVOIR N°2 : Résistances de Pull-Up et Pull-Down", expanded=False):
            st.markdown(r"""
            #### Contexte & Problématique Haute Impédance :
            Les entrées numériques des microcontrôleurs (CMOS, ATmega328P, ESP32) possèdent une très grande impédance d'entrée (de 100 MΩ à 1 GΩ) due à la présence de la grille isolée du transistor MOS d'entrée.
            Lorsqu'une broche n'est reliée ni au Vcc ni au GND, elle se trouve dans un **état flottant (haute impédance / *floating*)**.
            Elle se comporte alors comme une antenne sensible aux parasites électromagnétiques environnants, provoquant des états logiques alatoires imprévisibles.

            #### 1. Montage Pull-Up (Rappel au Vcc) :
            - **Câblage** : Une résistance de $10\text{ k}\Omega$ est branchée entre la broche et le $+5\text{V}$. Le bouton-poussoir est entre la broche et le $GND$.
            - **Repos (Bouton relâché)** : Entrée tirée au $+5\text{V}$ $\Rightarrow$ **HIGH (1)**.
            - **Actif (Bouton appuyé)** : Entrée reliée au $GND$ $\Rightarrow$ **LOW (0)**.

            #### 2. Montage Pull-Down (Rappel à la Masse) :
            - **Câblage** : Une résistance de $10\text{ k}\Omega$ est branchée entre la broche et le $GND$. Le bouton est entre la broche et le $+5\text{V}$.
            - **Repos (Bouton relâché)** : Entrée tirée au $GND$ $\Rightarrow$ **LOW (0)**.
            - **Actif (Bouton appuyé)** : Entrée reliée au $+5\text{V}$ $\Rightarrow$ **HIGH (1)**.

            #### 3. Pull-Up Interne Arduino :
            L'ATmega328P possède des résistances de Pull-Up internes intégrées (20 kΩ à 50 kΩ) activables en C++ :
            ```cpp
            pinMode(pin, INPUT_PULLUP); // Active la résistance de rappel interne au Vcc
            ```
            *Note* : En `INPUT_PULLUP`, la logique est inversée (un appui sur bouton relié au GND renvoie `LOW`).
            r""")

        with st.expander("📄 FICHE SAVOIR N°3 : La PWM (Modulation de Largeur d'Impulsion)", expanded=False):
            st.markdown(r"""
            #### Principe Fonctionnel :
            La PWM (Pulse Width Modulation / MLI) permet de simuler une tension ou puissance analogique variable en utilisant exclusivement des signaux numériques Tout-Ou-Rien (0V ou 5V).
            La tension créneau varie entre 0V et 5V, et on ajuste le **rapport cyclique** $\alpha$ (pourcentage du temps passé au niveau HAUT sur une période $T$) :
            $$\alpha = \frac{t_{\text{haut}}}{T} \quad \Big(0 \le \alpha \le 1 \quad \text{ou} \quad 0\% \le \alpha \le 100\%\Big)$$

            #### Formule de la Tension Moyenne :
            $$V_{\text{moy}} = \alpha \cdot V_{\text{max}} = V_{\text{max}} \cdot \left(\frac{\text{valeur\_8bits}}{255}\right)$$
            *Exemple* : Pour `analogWrite(pin, 127)` sous 5V $\Rightarrow \alpha \approx 50\% \Rightarrow V_{\text{moy}} = 2.5\text{ V}$.

            #### Broches PWM de l'Arduino Uno (ATmega328P) :
            | Broches PWM | Timer Associé | Fréquence Fréquentielle |
            | :--- | :--- | :--- |
            | **Pins 5 et 6** | Timer 0 (8 bits) | **~980 Hz** |
            | **Pins 3, 9, 10, 11** | Timer 1 (16 bits) / Timer 2 (8 bits) | **~490 Hz** |

            #### Application C++ : Variation progressive de luminosité d'une LED
            ```cpp
            int led = 9; // Broche PWM à 490 Hz

            void setup() {
              pinMode(led, OUTPUT);
            }

            void loop() {
              for (int i = 0; i <= 255; i++) {
                analogWrite(led, i); // Rapport cyclique de 0% à 100%
                delay(10);
              }
            }
            ```
            r""")

        with st.expander("📄 FICHE SAVOIR N°4 : Interruptions Matérielles & Registres AVR", expanded=False):
            st.markdown(r"""
            #### Principe d'une Interruption Matérielle :
            Une interruption matérielle envoie un signal au processeur pour interrompre immédiatement le programme principal (`loop()`) et exécuter une routine spécifique appelée **ISR** (*Interrupt Service Routine*).
            À la fin de l'ISR, le microcontrôleur restaure son contexte et reprend le programme à l'endroit exact de l'interruption.

            #### Vecteurs d'Interruption & Registres de Ports ATmega328P :
            - **PORTB** : Pins D8 à D13 (Registre de direction `DDRB`)
            - **PORTC** : Pins A0 à A5 (Registre de direction `DDRC`)
            - **PORTD** : Pins D0 à D7 (Registre de direction `DDRD`)

            #### Décalage de Bit & Registres DDRx :
            Un bit à `1` dans `DDRx` configure la broche associée en **Sortie**. Un bit à `0` configure en **Entrée**.
            - Passage de D3 (INT1) en sortie : `DDRD |= (1 << PD3);` (ou `1 << INT1`).
            - Passage de D3 en entrée : `DDRD &= ~(1 << PD3);` (équivaut à `pinMode(3, INPUT)`).

            #### Attachement d'une ISR en C++ :
            ```cpp
            volatile bool état = false;

            void toggleISR() { // Routine ISR ultra-courte (pas de delay, pas de Serial)
              état = !état;
            }

            void setup() {
              pinMode(2, INPUT_PULLUP);
              // Attache l'interruption INT0 sur la pin D2 lors d'un front descendant
              attachInterrupt(digitalPinToInterrupt(2), toggleISR, FALLING);
            }

            void loop() {
              // Code principal non bloquant
            }
            ```
            r""")

    with tab_fs2:
        st.subheader("💻 Fiches Savoir : Informatique, Mémoire & Composants")

        with st.expander("📄 FICHE SAVOIR N°5 : Organisation des Mémoires (Flash, SRAM & EEPROM) de l'Arduino UNO R3", expanded=True):
            st.markdown(r"""
            L'ATmega328P repose sur une architecture Harvard (bus d'instructions et bus de données séparés) découpée en 3 mémoires distinces :

            #### 1. Mémoire Flash (32 Ko) :
            - **Type** : Mémoire non-volatile (programme conservé hors tension).
            - **Usage** : Stocke le **Bootloader** (0.5 Ko en haute mémoire) et le **code exécutable C++ (.hex)**.
            - **Optimisation** : Utiliser la directive `PROGMEM` ou le macro `F("mon texte")` pour stocker les chaînes constantes en Flash sans encombrer la SRAM.

            #### 2. Mémoire SRAM (2 Ko = 2048 Octets) :
            - **Type** : Mémoire vive volatile (effacée à l'extinction).
            - **Cartographie interne** :
              - **Variables globales et statiques** (.data et .bss) en bas de mémoire.
              - **Le Tas (Heap)** : Allocation dynamique (`malloc`, `new`). S'étend vers le bas.
              - **La Pile (Stack)** : Variables locales, arguments de fonctions, adresses de retour. S'étend vers le haut.
              ⚠️ **Collision Heap / Stack** : Si la Pile et le Tas se croisent (saturation SRAM < 2048 octets), le programme plante de façon imprévisible.

            #### 3. Mémoire EEPROM (1 Ko = 1024 Octets) :
            - **Type** : Mémoire non-volatile électriquement effaçable (100 000 cycles d'écriture).
            - **Usage** : Sauvegarde permanente de paramètres de configuration (seuils, adresses IP/Modbus, compteurs).
            - **Bibliothèque C++** : `#include <EEPROM.h>` (`EEPROM.read(addr)`, `EEPROM.write(addr, val)`, `EEPROM.update(addr, val)`).
            r""")

        with st.expander("📄 FICHE SAVOIR N°6 : Le Signal 4-20 mA Industriel", expanded=False):
            st.markdown(r"""
            #### Rôle & Définition :
            Standard analogique universel pour boucles d'instrumentation industrielle.
            La grandeur physique (pression, température, débit) est traduite linéairement en une intensité variant de **4 mA (minimum / zéro de mesure)** à **20 mA (maximum / pleine échelle)**.

            #### Formule Mathématique de Conversion Linéaire :
            $$I(T) = I_{\text{min}} + \frac{T - T_{\text{min}}}{T_{\text{max}} - T_{\text{min}}} \cdot (I_{\text{max}} - I_{\text{min}}) = 4 + \frac{T - T_{\text{min}}}{T_{\text{max}} - T_{\text{min}}} \cdot 16\text{ mA}$$
            *Exemple* : Pour un capteur de température de $-15^\circ\text{C}$ ($4\text{ mA}$) à $+150^\circ\text{C}$ ($20\text{ mA}$) :
            - Pour $T = -15^\circ\text{C}$ : $I = 4 + \frac{0}{165} \cdot 16 = \mathbf{4\text{ mA}}$.
            - Pour $T = +67.5^\circ\text{C}$ : $I = 4 + \frac{82.5}{165} \cdot 16 = \mathbf{12\text{ mA}}$.
            - Pour $T = +150^\circ\text{C}$ : $I = 4 + \frac{165}{165} \cdot 16 = \mathbf{20\text{ mA}}$.

            #### Avantages du 4-20 mA ('Live Zero') :
            1. **Détection automatique de rupture de câble** : Si $I = 0\text{ mA}$ (inférieur à 3.8 mA), le système sait qu'il y a une coupure de fil ou une défaillance du capteur.
            2. **Auto-alimentation 2 fils** : Les 4 mA permanents permettent d'alimenter l'électronique du transmetteur.
            3. **Immunité aux parasites & aux chutes de tension** : L'intensité reste constante quelle que soit la longueur du câble (jusqu'à 1000 mètres).

            #### Conversion Courant $
ightarrow$ Tension pour Microcontrôleur :
            On insère une résistance de précision $R = 250\ \Omega$ (0.1%) dans la boucle :
            - À $4\text{ mA}$ : $V = 250\ \Omega \cdot 0.004\text{ A} = \mathbf{1.0\text{ V}}$.
            - À $20\text{ mA}$ : $V = 250\ \Omega \cdot 0.020\text{ A} = \mathbf{5.0\text{ V}}$.
            La tension $1.0\text{V} - 5.0\text{V}$ est directement lue par l'ADC de l'Arduino.
            r""")

        with st.expander("📄 FICHE SAVOIR N°7 : Résolution et Précision des Capteurs", expanded=False):
            st.markdown(r"""
            #### 1. La Résolution :
            C'est le plus petit changement de la grandeur physique qu'un capteur ou un système de mesure peut détecter ou afficher.
            - *Exemple* :
              - Affichage $45\%$, $46\%$, $47\%$ $\Rightarrow$ **Résolution = $1\%$**.
              - Affichage $45.0\%$, $45.1\%$, $45.2\%$ $\Rightarrow$ **Résolution = $0.1\%$**.
            - **Résolution numérisée d'un CAN $n$ bits** :
              $$q = \text{Quantum} = \frac{\text{Étendue de Mesure (EM)}}{2^n - 1}$$

            #### 2. La Précision (Incertitude de mesure) :
            C'est l'écart maximal entre la valeur mesurée par le capteur et la valeur réelle (vraie) de la grandeur.
            - *Exemple* : Pour une humidité réelle de $50\%$, si le capteur indique $52\% \pm 0.5\%$, l'erreur de précision est de $+2\%$.

            #### 3. Justesse vs Fidélité :
            - **Justesse** : Absence d'erreur systématique (moyenne des mesures centrée sur la valeur vraie).
            - **Fidélité (Répétabilité)** : Rapprochement des mesures entre elles (absence d'erreur aléatoire).
            - **Précision** = Justesse + Fidélité.
            ⚠️ *Piège d'examen* : Un capteur avec une résolution de 4 décimales peut être totalement imprécis s'il n'est pas étalonné !
            r""")

        with st.expander("📄 FICHE SAVOIR N°8 : Les Relais (Électromécaniques & Statiques)", expanded=False):
            st.markdown(r"""
            #### Rôle & Définition :
            Un relais est un interrupteur commandé électriquement. Il permet à un circuit de commande basse tension (Arduino 5V / 20mA) d'isoler et de commuter un circuit de puissance (230V AC / 10A, moteurs, pompes).

            #### Types de Relais :
            1. **Relais Électromécanique (EMR)** :
               - Fonctionne avec une bobine électromagnétique et des contacts mécaniques.
               - Émet un "clic" sonore à la commutation.
               - Nécessite une **diode de roue libre** en anti-parallèle sur la bobine pour absorber la surtension d'auto-induction ($e = -L \frac{di}{dt}$).
            2. **Relais Statique (SSR)** :
               - Basé sur des semi-conducteurs (Optocoupleur + Triac / MOSFET).
               - Silencieux, vitesse de commutation ultra-rapide, durée de vie illimitée.

            #### Connectique d'un Module Relais :
            - **Côté Commande (Basse Tension)** : `VCC` (+5V), `GND` (Masse), `IN` (Signal Arduino).
            - **Côté Puissance (Haute Tension)** :
              - `COM` (Common) : Borne d'entrée du courant de puissance.
              - `NO` (Normally Open) : Contact Normalement Ouvert au repos (fermé quand `IN` est actif).
              - `NC` (Normally Closed) : Contact Normalement Fermé au repos (ouvert quand `IN` est actif).
            r""")

    with tab_fs3:
        st.subheader("📶 Fiches Savoir : Réseaux, Communications & C++")

        with st.expander("📄 FICHE SAVOIR N°9 : Rapidité de Modulation (Bauds) vs Débit Binaire (bps)", expanded=True):
            st.markdown(r"""
            #### 1. Débit Binaire $D$ (bits/s ou bps) :
            Quantité d'information binaire utile transmise par unité de temps :
            $$D = \frac{n}{\Delta t} \quad (\text{en bps})$$

            #### 2. Rapidité de Modulation $R$ (Bauds) :
            Nombre de changements d'état du signal physique (symboles ou valences) transmis par seconde sur la ligne :
            $$R = \frac{1}{T_s} \quad (\text{en Bauds, où } T_s \text{ est la durée d'un symbole})$$

            #### 3. Relation Générale de Nyquist-Hartley :
            Si chaque symbole code $m$ bits (soit $M = 2^m$ valences possibles) :
            $$D = R \cdot m = R \cdot \log_2(M)$$

            | Type de Signal / Modulation | Valences ($M$) | Bits par symbole ($m$) | Relation Débit / Bauds |
            | :--- | :--- | :--- | :--- |
            | **Binaire RS232 / UART** | $M = 2$ | $m = 1\text{ bit}$ | **$D = R$** (bps = Bauds) |
            | **Modulation 4-PSK / QPSK** | $M = 4$ | $m = 2\text{ bits}$ | **$D = 2 \cdot R$** |
            | **Modulation 16-QAM** | $M = 16$ | $m = 4\text{ bits}$ | **$D = 4 \cdot R$** (Ex: 2400 Bauds $\Rightarrow$ 9600 bps) |
            | **Modulation 256-QAM** | $M = 256$ | $m = 8\text{ bits}$ | **$D = 8 \cdot R$** |
            r""")

        with st.expander("📄 FICHE SAVOIR N°10 : Contrôle de Flux (XON/XOFF & Matériel RTS/CTS)", expanded=False):
            st.markdown(r"""
            #### Rôle du Contrôle de Flux :
            Éviter le débordement de tampon (*Buffer Overflow*) de réception lorsqu'un récepteur lent est saturé par un émetteur rapide.

            #### 1. Contrôle de Flux Logiciel (In-Band) : XON / XOFF
            - Utilise les 2 lignes de données série existantes (`Tx` et `Rx`).
            - **XOFF (ASCII `0x13` / DC3)** : Envoyé par le récepteur dès que son tampon atteint un seuil haut (ex. 80%). L'émetteur suspend la transmission.
            - **XON (ASCII `0x11` / DC1)** : Envoyé dès que le tampon repasse sous un seuil bas (ex. 20%). L'émetteur reprend l'envoi.
            - *Limite* : Incompatible avec le transfert de fichiers binaires bruts si le fichier contient lui-même les octets `0x11` ou `0x13`.

            #### 2. Contrôle de Flux Matériel (Out-of-Band) : RTS / CTS & DTR / DSR
            - Utilise des lignes physiques dédiées sur le câble RS232 :
            - **RTS / CTS (Request To Send / Clear To Send)** :
              - `RTS` : Positionné par l'émetteur pour demander à émettre.
              - `CTS` : Validé par le récepteur quand son tampon est disponible.
            - **DTR / DSR (Data Terminal Ready / Data Set Ready)** : Indiquent la présence et l'état sous-tension des équipements.
            r""")

        with st.expander("📄 FICHE SAVOIR N°11 : Le Routage IP", expanded=False):
            st.markdown(r"""
            #### Principe du Routage (Couche 3 OSI) :
            Fonction assurée par les routeurs pour acheminer les paquets IP depuis un réseau source vers un réseau destination à travers des réseaux d'interconnexion.

            #### Structure d'une Table de Routage :
            Chaque entrée contient :
            1. **Réseau Destination & Masque CIDR** (ex: `192.168.20.0/24`).
            2. **Passerelle / Next Hop** (IP du routeur suivant).
            3. **Interface de sortie** (ex: `g0/0/1`).
            4. **Distance Administrative (DA) & Métrique** (coût du chemin).

            #### Types de Routes :
            - **Directement connectées** (DA = 0).
            - **Statiques** : Configurer manuellement (`ip route 192.168.20.0 255.255.255.0 10.0.0.2`).
            - **Route par Défaut** : `0.0.0.0 0.0.0.0 <Next_Hop>` (achemine le trafic inconnu vers le Web).
            - **Dynamiques** : Calculées automatiquement par des protocoles de routage (**OSPF** à état de lien).
            r""")

        with st.expander("📄 FICHE SAVOIR N°12 : Commande de LED Objet en C++", expanded=False):
            st.markdown(r"""
            #### Encapsulation Orientée Objet C++ :
            Création d'une classe `Led` encapsulant la broche matérielle et les méthodes d'action (`allumer`, `eteindre`, `basculer`).

            ```cpp
            #include <Arduino.h>

            class Led {
            private:
              int broche; // Attribut privé
            public:
              // Constructeur : configuration automatique du pinMode
              Led(int pin) {
                broche = pin;
                pinMode(broche, OUTPUT);
              }

              void allumer() {
                digitalWrite(broche, HIGH);
              }

              void eteindre() {
                digitalWrite(broche, LOW);
              }

              void basculer() {
                digitalWrite(broche, !digitalRead(broche));
              }
            };

            // Instanciation de l'objet maLed sur la broche 13
            Led maLed(13);

            void setup() {
              // Le constructeur a configuré la broche 13 en sortie
            }

            void loop() {
              maLed.allumer();
              delay(1000);
              maLed.eteindre();
              delay(1000);

              // Inversion directe d'état
              maLed.basculer();
              delay(1000);
            }
            ```
            r""")

    with tab_fs4:
        st.subheader("🛠️ Fiches Montage : Expérimentations Pratiques & Codes C++")

        with st.expander("📄 FICHE MONTAGE N°1 : Contrôle de Vérins Électriques (Relais & Driver BTS7960)", expanded=True):
            st.markdown(r"""
            #### Objectif :
            Piloter un ou plusieurs vérins électriques à moteur CC 12V/24V. Le courant absorbé en charge nécessite un module de puissance dimensionné (driver MOSFET ou carte relais).

            #### Montage 1 : Module Relais ECO-WORTHY
            - **SÉCURITÉ MATÉRIELLE AU DÉMARRAGE** : Utiliser une fonction `safeInitPin()` pour forcer l'état inactif du relais *avant* d'initialiser le `pinMode(OUTPUT)`, évitant tout mouvement incontrôlé du vérin au boot.

            ```cpp
            const int pinM = 2;
            const int pinN = 3;
            const bool relayActiveLow = false; // true si le relais s'active sur LOW

            int outActiveValue()   { return relayActiveLow ? LOW  : HIGH; }
            int outInactiveValue() { return relayActiveLow ? HIGH : LOW;  }

            void safeInitPin(int pin) {
              digitalWrite(pin, outInactiveValue()); // Positionner l'état inactif désiré
              pinMode(pin, OUTPUT);
            }

            void setup() {
              safeInitPin(pinM);
              safeInitPin(pinN);
              delay(200); // Laissez les relais se stabiliser
              Serial.begin(115200);
              Serial.println("Init complete - relays forced inactive");
            }

            void activateM(unsigned long ms) {
              digitalWrite(pinN, outInactiveValue()); // Verrouillage matériel
              delay(100);
              digitalWrite(pinM, outActiveValue());
              Serial.println("M ON");
              delay(ms);
              digitalWrite(pinM, outInactiveValue());
              Serial.println("M OFF");
              delay(100);
            }

            void activateN(unsigned long ms) {
              digitalWrite(pinM, outInactiveValue()); // Verrouillage matériel
              delay(100);
              digitalWrite(pinN, outActiveValue());
              Serial.println("N ON");
              delay(ms);
              digitalWrite(pinN, outInactiveValue());
              Serial.println("N OFF");
              delay(100);
            }

            void loop() {
              activateM(2000);
              delay(1000);
              activateN(2000);
              delay(3000);
            }
            ```
            r""")

        with st.expander("📄 FICHE MONTAGE N°2 : Commande d'une Charge 230V AC (Ampoule 60W) par Relais", expanded=False):
            st.markdown(r"""
            #### Objectif :
            Utiliser un module relais 5V commandé par une sortie numérique Arduino pour allumer une ampoule 230V AC / 60W en toute sécurité.

            #### Schéma de Câblage de Puissance :
            - **Phase 230V AC** $\rightarrow$ Borne **`COM`** (Commun) du relais.
            - Borne **`NO`** (Normalement Ouvert) du relais $\rightarrow$ Première borne de l'ampoule.
            - **Neutre 230V AC** $\rightarrow$ Seconde borne de l'ampoule.

            ```cpp
            // Programme Arduino : Clignotement de l'ampoule 230V (3s allumée / 3s éteinte)
            void setup() {
              pinMode(2, OUTPUT); // Pin 2 reliée à l'entrée IN du relais
              digitalWrite(2, LOW); // Ampoule éteinte par défaut (COM + NO)
            }

            void loop() {
              digitalWrite(2, HIGH); // Commutation relais : Ampoule 230V Allumée
              delay(3000);
              digitalWrite(2, LOW);  // Commutation relais : Ampoule 230V Éteinte
              delay(3000);
            }
            ```
            r""")

    with tab_fs5:
        st.subheader("✍️ Auto-Évaluation Fiches Savoir & Montages")
        st.markdown("Testez vos connaissances sur l'ensemble des fiches savoir :")

        q_fs1 = st.radio("1. Fiche N°1 : Quel risque majeur survient si les 4 interrupteurs d'un pont en H sont fermés en même temps ?", ["Le moteur tourne 2x plus vite", "Court-circuit direct de l'alimentation (destruction du pont)", "Inversion automatique du sens", "Aucun risque"], key="qfs1")
        q_fs2 = st.radio("2. Fiche N°6 : Dans une boucle 4-20 mA, que signifie une mesure de 0 mA ?", ["Valeur minimale du capteur", "Pleine échelle du capteur", "Déconnexion ou rupture de câble", "Surcharge"], key="qfs2")
        q_fs3 = st.radio("3. Fiche N°9 : Quelle est la relation entre Débit (bps) et Bauds pour un signal 16-QAM ?", ["D = R", "D = 2 * R", "D = 4 * R", "D = 16 * R"], key="qfs3")

        if st.button("Valider mes réponses Fiches Savoir", type="primary"):
            score_fs = 0
            if "Court-circuit" in q_fs1: score_fs += 1
            if "Déconnexion" in q_fs2: score_fs += 1
            if "D = 4 * R" in q_fs3: score_fs += 1
            st.success(f"🏆 Score Fiches Savoir : **{score_fs} / 3**")
            if score_fs == 3: st.balloons()


elif page == "🛡️ TP Cybersécurité, Gouvernance & pfSense":
    st.markdown("<div class='hero-title'>🛡️ TP Cybersécurité, Gouvernance & Infrastructure</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Cours magistral de A à Z, cas pratiques, commandes et quiz sur EBIOS RM, PIA/AIPD, PKI et pfSense/DMZ</p>", unsafe_allow_html=True)

    tab_tp1, tab_tp2, tab_tp3, tab_tp4 = st.tabs([
        "📊 Atelier 1 : EBIOS RM (ANSSI)", 
        "📜 Atelier 2 : PIA / AIPD (RGPD)", 
        "🔑 Atelier 3 : PKI & Certificats X.509", 
        "🧱 Atelier 4 : Matrice des Flux & pfSense"
    ])

    with tab_tp1:
        st.subheader("1. Cours Magistral : Méthodologie EBIOS Risk Manager (ANSSI)")
        st.markdown(r"""
        **EBIOS Risk Manager (EBIOS RM)** est la méthode officielle française d'appréciation et de traitement des risques numériques, publiée par l'**ANSSI** (Agence Nationale de la Sécurité des Systèmes d'Information). Elle est conforme à la norme **ISO/IEC 27005**.

        Elle s'articule autour de **5 Ateliers progressifs** :
        r""")

        st.markdown(r"""
        #### 🔹 Atelier 1 : Socle de sécurité & Périmètre métier
        * **Périmètre de l'étude** : Définition des limites du système d'information analysé.
        * **Valeurs Métiers (VM)** : Ce que l'organisation produit ou protège (ex: continuité de la production, confidentialité des brevets, crédibilité).
        * **Biens Supports (BS)** : Les composants techniques qui hébergent les VM (serveurs, bases de données, automates STM32, liens réseau).
        * **Besoins de Sécurité (DICP)** : Définition des niveaux d'exigence (de 0 à 4) sur la **D**isponibilité, l'**I**ntégrité, la **C**onfidentialité et la **P**reuve/Traçabilité.

        #### 🔹 Atelier 2 : Sources de Risques (SR) & Visées Stratégiques (VS)
        * **Sources de Risques (SR)** : Qui peut attaquer ? (Cybercriminels motivés par le gain, États/Espionnage, Concurrents, Vengeurs internes, Activistes).
        * **Visées Stratégiques (VS)** : Quel est le but ultime de l'attaquant ? (Ex: Interrompre la chaîne de production, voler la base de données clients, extorquer une rançon via Rançongiciel).

        #### 3. Atelier 3 : Scénarios Stratégiques & Écosystème
        * **Analyse de l'écosystème** : Cartographie des parties prenantes (prestataires, sous-traitants, fournisseurs d'accès, maintenance distante).
        * **Chemins d'attaque stratégiques** : Comment la SR va rebondir sur un prestataire moins sécurisé pour atteindre les valeurs métiers du système principal.

        #### 4. Atelier 4 : Scénarios Opérationnels & Cyber Kill Chain
        * Décomposition technique détaillée des modes opératoires (Kill Chain) :
          1. *Reconnaissance* (Scans Nmap, OSINT).
          2. *Armement & Livraison* (Hameçonnage/Phishing, pièce jointe malveillante).
          3. *Exploitation & Installation* (Exploitation d'une vulnérabilité OWASP ou binaire).
          4. *Command & Control (C2)* (Prise de contrôle distante).
          5. *Actions sur objectifs* (Exfiltration de données, chiffrement des disques).

        #### 5. Atelier 5 : Traitement du risque & PACS
        * **Décision sur le risque** : Refuser, Réduire (imposer des mesures), Transférer (assurance) ou Conserver (accepter le risque résiduel).
        * **Plan d'Amélioration de la Sécurité (PACS)** : Liste des mesures d'atténuation prioritaires (ex: MFA, chiffrement AES-256, isolation des réseaux par VLANs/pfSense).
        r""")

        st.markdown("---")
        st.subheader("💡 Cas Pratique BTS CIEL : Passerelle de Collecte IoT Industrielle")
        st.info(r"""
        **Mise en situation** : Une PME industrielle installe des capteurs de température/pression STM32 sur ses cuves. Les données transitent en MQTT vers une passerelle Debian qui enregistre en BDD MySQL et transmet au Cloud.
        * **Valeur Métier (VM)** : Intégrité des télémesures et continuité de régulation thermique.
        * **Bien Support (BS)** : Serveur Debian, Broker MQTT, base MySQL.
        * **Source de Risque (SR)** : Concurrent industriel ou cybercriminel.
        * **Mesure PACS obligatoire** : Chiffrement TLS sur le Broker MQTT (MQTTS sur port 8883), authentification par certificat X.509 et isolation de la passerelle en DMZ sur pfSense.
        r""")

        st.markdown("---")
        st.subheader("✍️ Quiz d'Auto-Évaluation EBIOS RM")
        q_eb1 = st.radio("Q1 : Dans la méthode EBIOS RM, à quel atelier identifie-t-on les Valeurs Métiers et les Biens Supports ?", ["Atelier 1", "Atelier 2", "Atelier 3", "Atelier 5"], key="q_eb1_k")
        if st.button("Valider Q1 EBIOS", key="btn_eb1"):
            if q_eb1 == "Atelier 1":
                st.success("🎉 **Exact !** L'Atelier 1 définit le socle de sécurité, le périmètre, les Valeurs Métiers et les Biens Supports.")
            else:
                st.error("❌ **Incorrect.** L'Atelier 1 est consacré au cadre, aux Valeurs Métiers et au socle de sécurité.")

    with tab_tp2:
        st.subheader("2. Cours Magistral : PIA / AIPD (RGPD & CNIL)")
        st.markdown(r"""
        L'**AIPD** (**Analyse d'Impact relative à la Protection des Données**), souvent appelée **PIA** (*Privacy Impact Assessment*), est une obligation légale imposée par l'article 35 du **RGPD** (Règlement Général sur la Protection des Données).

        #### 🔹 Quand réaliser une AIPD / PIA ?
        L'AIPD est **obligatoire** pour tout traitement susceptible de présenter un **risque élevé** pour les droits et libertés des personnes physiques. La CNIL définit **9 critères** :
        1. Évaluation ou scoring (profilage).
        2. Décision automatisée avec effet juridique.
        3. Surveillance systématique (vidéoprotection, géolocalisation).
        4. Collecte de données sensibles (biométrie, santé, opinions).
        5. Données personnelles collectées à grande échelle.
        6. Croisement ou combinaison de jeux de données.
        7. Données concernant des personnes vulnérables (mineurs, salariés).
        8. Utilisation d'une innovation technologique (IoT, IA).
        9. Exclusion du bénéfice d'un droit ou d'un contrat.

        📌 **Règle pratique** : Si un traitement remplit au moins **2 de ces 9 critères**, l'AIPD est légalement **OBLIGATOIRE**.
        r""")

        st.markdown(r"""
        #### 🔹 Les 3 Volets de la Démarche AIPD :
        1. **Description détaillée du traitement** : Finalités, nature des données collectées, durée de conservation, destinataires, cartographie des flux.
        2. **Évaluation de la nécessité et de la proportionnalité** : Respect des droits des personnes (droit d'accès, de rectification, d'opposition, de suppression), durée de conservation justifiée.
        3. **Appréciation des risques sur la vie privée** : Analyse des impacts potentiels en cas d'accès non autorisé (violation de confidentialité), de modification non désirée (violation d'intégrité) ou d'indisponibilité des données, et identification des mesures techniques (chiffrement, pseudonymisation) et organisationnelles.
        r""")

        st.markdown("---")
        st.subheader("💡 Cas Pratique BTS CIEL : Contrôle d'Accès Biométrique par Empreinte Raccordé à Active Directory")
        st.warning(r"""
        **Analyse RGPD/PIA** :
        * Critère 1 : Collecte de données biométriques (données sensibles).
        * Critères 2 : Surveillance des salariés/vulnérables.
        * **Verdict** : 2 critères remplis $\rightarrow$ **AIPD OBLIGATOIRE avant tout déploiement**.
        * **Mesures de conformité** : Stockage du gabarit biométrique sous forme de hachage irréversible chiffré AES-256 uniquement sur la carte à puce de l'agent (pas de BDD centrale si possible), journalisation des accès sécurisée.
        r""")

        st.markdown("---")
        st.subheader("✍️ Quiz d'Auto-Évaluation PIA / RGPD")
        q_pia1 = st.radio("Q1 : Selon les recommandations de la CNIL, à partir de combien de critères remplis parmi les 9 l'AIPD devient-elle obligatoire ?", ["1 critère", "2 critères", "5 critères", "Tous les critères"], key="q_pia1_k")
        if st.button("Valider Q1 PIA", key="btn_pia1"):
            if q_pia1 == "2 critères":
                st.success("🎉 **Exact !** Au moins 2 critères sur 9 rendent l'AIPD légalement obligatoire.")
            else:
                st.error("❌ **Incorrect.** L'AIPD est obligatoire dès lors que 2 critères sur 9 sont satisfaits.")

    with tab_tp3:
        st.subheader("3. Cours Magistral : PKI (Infrastructure à Clés Publiques & Certificats X.509)")
        st.markdown(r"""
        Une **PKI** (*Public Key Infrastructure*) ou **IGC** (*Infrastructure à Clés Publiques*) est l'ensemble des composants matériels, logiciels et humains permettant de délivrer, gérer, distribuer et révoquer des **certificats numériques X.509**.

        #### 🔹 Composants de la Chaîne de Confiance :
        1. **Autorité de Certification Racine (Root CA)** : Clé maîtresse de l'infrastructure. Elle est généralement maintenue **hors ligne (offline)** dans un coffre-fort pour éviter toute compromission.
        2. **Autorité de Certification Intermédiaire (Intermediate CA)** : Signée par la Root CA, elle est en ligne et délivre les certificats opérationnels aux serveurs et utilisateurs.
        3. **Autorité d'Enregistrement (RA)** : Vérifie l'identité du demandeur de certificat.
        4. **Registre / Dépôt (Directory)** : Publie les certificats et la liste de révocation.
        r""")

        st.markdown(r"""
        #### 🔹 Structure d'un Certificat Numérique X.509 v3 :
        * **Subject** : Identité du titulaire (Nom, Organisation, Common Name CN=bts-ciel.local).
        * **Issuer** : Nom de la CA ayant signé le certificat.
        * **Validity** : Dates Not Before et Not After.
        * **Public Key** : Clé publique du titulaire (RSA 2048/4096 bits ou ECC 256 bits).
        * **Extensions (SAN - Subject Alternative Name)** : Adresses IP ou noms FQDN secondaires couverts par le certificat (ex: `DNS:www.bts-ciel.local`, `IP:192.168.10.1`).
        * **Signature** : Condensat Haché (SHA-256) du certificat, chiffré avec la clé privée de la CA émettrice.

        #### 🔹 Révocation de Certificats :
        * **CRL (Certificate Revocation List)** : Fichier signé publié périodiquement par la CA contenant la liste des numéros de série révoqués.
        * **OCSP (Online Certificate Status Protocol)** : Protocole réseau interactif (HTTP) permettant d'interroger la CA en temps réel pour connaître le statut d'un certificat sans télécharger toute la CRL.
        r""")

        st.markdown("---")
        st.subheader("💻 Commandes OpenSSL Indispensables (BTS CIEL)")
        st.code(r"""
# 1. Générer une clé privée RSA de 2048 bits chiffrée
openssl genrsa -out cle_privee_serveur.key 2048

# 2. Créer une Demande de Signature de Certificat (CSR)
openssl req -new -key cle_privee_serveur.key -out demande_serveur.csr -subj "/C=FR/ST=IDF/L=Paris/O=BTS_CIEL/CN=web.ciel.local"

# 3. Signer le certificat avec sa propre CA auto-signée (Valable 365 jours)
openssl x509 -req -in demande_serveur.csr -signkey cle_privee_serveur.key -out certificat_serveur.crt -days 365

# 4. Examiner le contenu détaillé d'un certificat X.509
openssl x509 -in certificat_serveur.crt -text -noout

# 5. Tester la poignée de main TLS avec un serveur web sécurisé
openssl s_client -connect web.ciel.local:443 -showcerts
        r""", language="bash")

        st.markdown("---")
        st.subheader("✍️ Quiz d'Auto-Évaluation PKI")
        q_pki1 = st.radio("Q1 : Quel protocole interactif permet de vérifier le statut de révocation d'un certificat en temps réel ?", ["CRL", "OCSP", "LDAPS", "DNSSEC"], key="q_pki1_k")
        if st.button("Valider Q1 PKI", key="btn_pki1"):
            if q_pki1 == "OCSP":
                st.success("🎉 **Exact !** OCSP (Online Certificate Status Protocol) permet d'interroger la CA directement sans télécharger de lourdes listes CRL.")
            else:
                st.error("❌ **Incorrect.** OCSP est le protocole de vérification en temps réel.")

    with tab_tp4:
        st.subheader("4. Cours Magistral : Matrice des Flux & Pare-feu pfSense (LAN / DMZ / WAN / Active Directory)")
        st.markdown(r"""
        Le pare-feu **pfSense** (fondé sur FreeBSD et `pf`) est l'équipement de sécurité périmétrique clé étudié en TP de BTS CIEL. Il permet de segmenter le réseau en zones de confiance différentes.

        #### 🔹 Architecture 3 Zones Standard (LAN, DMZ, WAN) :
        * **WAN (Unstrusted / Internet)** : Zone publique non de confiance.
        * **DMZ (Demilitarized Zone - Ex: 172.16.1.0/24)** : Zone isolée hébergeant les serveurs accessibles depuis le Web (Serveur Web, Reverse Proxy, Broker MQTT, Mail).
        * **LAN (Trusted / Réseau Interne - Ex: 192.168.10.0/24)** : Zone haute sécurité hébergeant les postes de travail, le contrôleur de domaine Active Directory et la BDD principale.
        r""")

        st.markdown(r"""
        #### 🔹 Règles d'Or de Sécurité & Matrice des Flux :
        1. **Politique par défaut** : **Deny All** (Tout ce qui n'est pas explicitement autorisé est bloqué).
        2. **Sens d'Initiation des Connexions** :
           * LAN $\rightarrow$ WAN : Autorisé (Nav Web, HTTP/HTTPS).
           * LAN $\rightarrow$ DMZ : Autorisé (Administration SSH/HTTPS).
           * DMZ $\rightarrow$ WAN : Autorisé de façon restreinte (Mises à jour `apt update`, DNS).
           * **DMZ $\rightarrow$ LAN : STRICTEMENT INTERDIT** (Si le serveur Web en DMZ est compromis, l'attaquant ne peut pas rebondir vers le LAN).
           * **WAN $\rightarrow$ LAN : STRICTEMENT INTERDIT**.
           * WAN $\rightarrow$ DMZ : Autorisé uniquement sur les ports publics via Redirection de Port (**Port Forwarding / NAT 1:1**).
        r""")

        st.markdown("---")
        st.subheader("📋 Matrice des Flux Réseau Détaillée (TP pfSense & Active Directory)")
        st.markdown(r"""
        | N° | Zone Source | IP Source | Zone Dest. | IP Dest. | Port / Protocole | Action | Justification Métier |
        | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
        | **1** | WAN | Any | DMZ | 172.16.1.10 | TCP 80, 443 | **PASS (NAT)** | Accès des usagers au serveur Web public |
        | **2** | WAN | Any | DMZ | 172.16.1.20 | TCP 8883 (MQTTS) | **PASS (NAT)** | Télémesure IoT chiffrée |
        | **3** | LAN | 192.168.10.0/24 | WAN | Any | TCP 80, 443 | **PASS** | Navigation Web des utilisateurs du LAN |
        | **4** | LAN | 192.168.10.10 (Admin)| DMZ | 172.16.1.0/24 | TCP 22 (SSH), 443 | **PASS** | Administration distante des serveurs |
        | **5** | DMZ | 172.16.1.0/24 | LAN | 192.168.10.2 (AD) | TCP/UDP 53 (DNS) | **PASS** | Résolution DNS pour les serveurs DMZ |
        | **6** | DMZ | 172.16.1.0/24 | LAN | 192.168.10.2 (AD) | TCP/UDP 88 (Kerberos) | **PASS** | Authentification du domaine AD |
        | **7** | DMZ | 172.16.1.0/24 | LAN | 192.168.10.0/24 | ANY | **BLOCK (LOG)** | Blocage strict DMZ vers LAN |
        | **8** | WAN | Any | LAN | Any | ANY | **BLOCK** | Protections périmétrique totale du LAN |
        r""")

        st.markdown("---")
        st.subheader("✍️ Quiz d'Auto-Évaluation pfSense & Flux Network")
        q_pf1 = st.radio("Q1 : Pourquoi est-il strictement interdit d'autoriser l'initiation de connexions directes de la DMZ vers le LAN ?", [
            "Pour économiser de la bande passante",
            "Parce que si le serveur en DMZ est piraté, l'attaquant ne doit pas pouvoir attaquer le réseau interne",
            "Parce que pfSense ne sait pas traiter le trafic DMZ",
            "Pour éviter les conflits d'adresses IP"
        ], key="q_pf1_k")
        if st.button("Valider Q1 pfSense", key="btn_pf1"):
            if "piraté" in q_pf1:
                st.success("🎉 **Exact !** La DMZ est une zone tampon. Si elle est compromise, le LAN reste isolé.")
            else:
                st.error("❌ **Incorrect.** L'isolation de la DMZ empêche le rebond d'un pirate vers le LAN.")


elif page == "🗓️ Révision Semaine par Semaine (BTS Blanc)":
    st.markdown("<div class='hero-title'>🗓️ Programme de Révision Semaine par Semaine (A à Z)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Cours magistraux complets, flashcards actives, exercices pratiques et questionnaires finaux de semaine à score persistant</p>", unsafe_allow_html=True)

    tab_w1, tab_w2, tab_w3, tab_w4, tab_w5, tab_w6 = st.tabs([
        "Semaine 1 (Réseaux)",
        "Semaine 2 (Cyber & SysAdmin)",
        "Semaine 3 (C++ & Python)",
        "Semaine 4 (Électronique & Math)",
        "Semaine 5 (SysML & E6)",
        "Semaine 6 (Annales & Synthèse)"
    ])

    # ==================== SEMAINE 1 ====================
    with tab_w1:
        st.subheader("🗓️ Semaine 1 : Réseaux, Commutation & Routage (Cours de A à Z)")
        w1_sub1, w1_sub2, w1_sub3, w1_sub4 = st.tabs(["📚 Cours Complet S1", "🗂️ Flashcards S1", "✍️ Exercices Pratiques S1", "📝 Questionnaire Final S1"])

        with w1_sub1:
            st.markdown(r"""
            ### 1.1 Architecture des Réseaux : Modèle OSI & TCP/IP
            Le **modèle OSI** (7 couches) et **TCP/IP** (4 couches) constituent le socle universel des télécommunications :
            * **Couche 7 (Application - PDU: Donnée)** : Protocoles applicatifs (HTTP, HTTPS, DNS, DHCP, SSH, MQTT, SNMP, SMTP, FTP).
            * **Couche 6 (Présentation - PDU: Donnée)** : Encodage, chiffrement TLS/SSL, compression (ASCII, UTF-8, JPEG).
            * **Couche 5 (Session - PDU: Donnée)** : Ouverture, maintien et fermeture des sessions (NetBIOS, RPC, Sockets).
            * **Couche 4 (Transport - PDU: Segment / Datagramme)** :
              - **TCP** : Orienté connexion, fiable, contrôle de flux (fenêtre glissante, ACK, *3-way handshake* : `SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`).
              - **UDP** : Non orienté connexion, rapide, sans garantie d'arrivée (VoIP, streaming, DNS).
            * **Couche 3 (Réseau - PDU: Paquet)** : Adressage logique (IPv4 32 bits, IPv6 128 bits) et routage (OSPF, BGP, ICMP, IPsec). Équipement : **Routeur**.
            * **Couche 2 (Liaison de données - PDU: Trame)** : Adressage physique (MAC 48 bits), contrôle d'accès (Ethernet 802.3, Wi-Fi 802.11). Équipement : **Commutateur (Switch)**.
            * **Couche 1 (Physique - PDU: Bit)** : Transmission des signaux électriques (RJ45), optiques (fibre) ou radio.

            ### 1.2 Adressage IPv4, IPv6 & Subnetting VLSM
            * **Formule des hôtes utiles** : $N_{\text{hôtes}} = 2^{(32 - \text{CIDR})} - 2$.
            * **Calcul d'adresse Réseau** : IP `AND` Masque bit-à-bit.
            * **Calcul d'adresse Broadcast** : Adresse Réseau + $(2^{(32 - \text{CIDR})} - 1)$.
            * **Masques Fréquents** : `/24` (254 hôtes), `/26` (62 hôtes, `255.255.255.192`), `/28` (14 hôtes, `255.255.255.240`), `/30` (2 hôtes, `255.255.255.252`).
            * **IPv6 (128 bits)** : Notation hexadécimale, auto-configuration sans état **SLAAC** (*Stateless Address Autoconfiguration*) et protocole **NDP** (*Neighbor Discovery Protocol* via ICMPv6 remplaçant ARP).

            ### 1.3 VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN
            * **VLAN (Virtual LAN)** : Segmente logiquement les domaines de diffusion en Couche 2.
            * **Port Access** : Un seul VLAN, trames non taguées.
            * **Port Trunk (IEEE 802.1Q)** : Insère un tag de **4 octets** (32 bits) dans l'en-tête Ethernet, avec le **VLAN ID** sur 12 bits (4096 VLANs).
            * **VLAN Natif** : Trames traversant le lien Trunk sans tag (VLAN 1 par défaut).
            * **Router-on-a-Stick** : Sous-interfaces logiques (`g0/0.10`, `g0/0.20`) avec `encapsulation dot1Q <ID_VLAN>`.

            ### 1.4 Transmissions Optiques & Fibre Optique
            * **Fibre Monomode (SMF)** : Cœur étroit (**9 µm**), émetteur Laser, pas de dispersion modale, portée kilométrique (WAN, 1310/1550 nm).
            * **Fibre Multimode (MMF)** : Cœur large (**50 µm** / **62,5 µm**), LED/VCSEL, dispersion modale, courte portée (LAN, 850/1300 nm).
            * **Connecteurs Optiques** : ST (baïonnette), SC (carré), LC (petit format clipsable).
            * **Atténuation en dB** : $A = 10 \log_{10}\left(\frac{P_1}{P_2}\right)$.

            ### 1.5 Protocoles Industriels Modbus RTU & RS485
            * **RS485** : Liaison différentielle A/B, résistance de terminaison de $120\,\Omega$.
            * **Modbus RTU** : Codes fonction `01` (Read Coils), `03` (Read Holding Registers), `06` (Write Single), `16` (Write Multiple). Contrôle **CRC-16**, silence de **3,5 caractères** entre trames.

            ### 1.6 Analyse de Trames Wireshark
            * **En-tête IP** : Octet 0 (Version 4 + IHL 5), Octet 8 (TTL), Octet 9 (Protocole `06`=TCP / `17`=UDP), Octets 12-15 (IP Source), Octets 16-19 (IP Destination).
            r""")

        with w1_sub2:
            st.markdown("#### 🗂️ Flashcards Actives Semaine 1")
            fc_s1 = [
                {"q": "Quel protocole IPv6 remplace le protocole ARP d'IPv4 ?", "a": "Le protocole NDP (Neighbor Discovery Protocol), s'appuyant sur ICMPv6."},
                {"q": "Quelle est la taille exacte du tag inséré par la norme IEEE 802.1Q ?", "a": "4 octets (32 bits), dont 12 bits sont réservés au VLAN ID (VID)."},
                {"q": "Quelle est la différence fondamentale entre fibre Monomode et Multimode ?", "a": "Monomode (SMF) a un cœur très étroit (9 µm) sans dispersion modale pour longue distance. Multimode (MMF) a un cœur plus large (50/62.5 µm) sujet à la dispersion modale pour LAN."},
                {"q": "Quel est le rôle d'un port Trunk sur un commutateur ?", "a": "Transporter simultanément les trames de plusieurs VLANs entre commutateurs ou vers un routeur via le taggagement 802.1Q."},
                {"q": "Quel est le code fonction Modbus RTU servant à lire des registres de 16 bits ?", "a": "Code Fonction 03 (Read Holding Registers)."},
                {"q": "Combien d'adresses d'hôtes utilisables contient un sous-réseau /29 ?", "a": "6 hôtes utiles (2^(32-29) - 2 = 8 - 2 = 6)."},
                {"q": "Quelle est la valeur de l'octet de protocole dans l'en-tête IP pour le protocole TCP et UDP ?", "a": "06 (0x06) pour TCP, et 17 (0x11) pour UDP."},
                {"q": "À quoi sert la résistance de terminaison de 120 ohms sur un bus RS485 / CAN ?", "a": "À adapter l'impédance de la ligne pour éliminer les réflexions de signal aux extrémités."},
                {"q": "Quelle commande Cisco permet d'associer un port d'accès au VLAN 30 ?", "a": "switchport access vlan 30"},
                {"q": "Quelles sont les 3 étapes de la poignée de main TCP (3-way handshake) ?", "a": "1. SYN (demande de synchronisation), 2. SYN-ACK (acceptation et demande réciproque), 3. ACK (acquittement final)."}
            ]
            for f in fc_s1:
                with st.expander(f"📌 {f['q']}"):
                    st.write(f["a"])

        with w1_sub3:
            st.markdown("#### ✍️ Exercices d'Entraînement Pratiques Semaine 1")
            st.markdown("**Exercice 1 : Subnetting VLSM**")
            u_ex1 = st.number_input("Combien d'hôtes utiles sont disponibles dans le réseau 172.16.10.0/29 ?", min_value=0, value=0, key="ex1_w1_v16")
            if st.button("Vérifier Ex 1 (S1)", key="btn_ex1_s1"):
                if u_ex1 == 6:
                    st.success(r"🎉 **Exact !** $2^{32-29} - 2 = 8 - 2 = 6$ hôtes utiles.")
                else:
                    st.error(r"❌ Incorrect. $2^3 - 2 = 6$ hôtes utiles.")

            st.markdown("**Exercice 2 : Configuration Cisco Router-on-a-Stick**")
            cmd_cisco_ex = st.text_input("Commande d'encapsulation pour le VLAN 20 sur une sous-interface :", placeholder="ex: encapsulation...", key="cmd_cisco_s1")
            if st.button("Vérifier Ex 2 (S1)", key="btn_ex2_s1"):
                if cmd_cisco_ex.strip().lower() == "encapsulation dot1q 20":
                    st.success("🎉 **Parfait !** `encapsulation dot1Q 20` est la commande exacte.")
                else:
                    st.error("❌ Indice : `encapsulation dot1Q 20`.")

        with w1_sub4:
            st.markdown("#### 📝 Questionnaire Final - Semaine 1")
            q_w1_list = [
                {"q": "Q1 : À quelle couche du modèle OSI opère un commutateur (Switch) standard ?", "opts": ["Couche 1 (Physique)", "Couche 2 (Liaison)", "Couche 3 (Réseau)", "Couche 4 (Transport)"], "rep": "Couche 2 (Liaison)", "expl": "Les commutateurs opèrent en Couche 2 et aiguillent les trames via les adresses MAC."},
                {"q": "Q2 : Quelle est l'adresse de broadcast du réseau 192.168.1.0/26 ?", "opts": ["192.168.1.63", "192.168.1.127", "192.168.1.255", "192.168.1.31"], "rep": "192.168.1.63", "expl": "Pour /26 (bloc de 64 IP), les adresses vont de .0 à .63. L'adresse .63 est le broadcast."},
                {"q": "Q3 : Quelle est la taille du tag inséré par la norme IEEE 802.1Q ?", "opts": ["2 octets", "4 octets", "8 octets", "12 bits"], "rep": "4 octets", "expl": "Le tag 802.1Q inséré fait 4 octets (32 bits)."},
                {"q": "Q4 : Quel est le code fonction Modbus RTU utilisé pour lire des Holding Registers (16 bits) ?", "opts": ["Code 01", "Code 03", "Code 06", "Code 16"], "rep": "Code 03", "expl": "Le code fonction 03 lit les registres de 16 bits."},
                {"q": "Q5 : Quelle est la taille typique du cœur d'une fibre optique Monomode (SMF) ?", "opts": ["9 µm", "50 µm", "62.5 µm", "125 µm"], "rep": "9 µm", "expl": "Le cœur d'une fibre monomode mesure 9 µm de diamètre."}
            ]
            score_w1 = 0
            for idx, qitem in enumerate(q_w1_list):
                st.markdown(f"**{qitem['q']}**")
                ans = st.radio(f"Sélection Q{idx+1} S1 :", qitem["opts"], key=f"qw1_v16_{idx}")
                if ans == qitem["rep"]:
                    score_w1 += 1
            if st.button("Soumettre Questionnaire Semaine 1", type="primary", key="btn_qw1_v16"):
                st.session_state["score_week1"] = score_w1
                st.success(f"🏆 Score Semaine 1 enregistré : **{score_w1} / {len(q_w1_list)}**")
                if score_w1 == len(q_w1_list): st.balloons()

    # ==================== SEMAINE 2 ====================
    with tab_w2:
        st.subheader("🗓️ Semaine 2 : Cybersécurité, Gouvernance & SysAdmin (Cours de A à Z)")
        w2_sub1, w2_sub2, w2_sub3, w2_sub4 = st.tabs(["📚 Cours Complet S2", "🗂️ Flashcards S2", "✍️ Exercices Pratiques S2", "📝 Questionnaire Final S2"])

        with w2_sub1:
            st.markdown(r"""
            ### 2.1 Gouvernance Cybersécurité : Méthode EBIOS RM (ANSSI)
            La méthode **EBIOS RM** (*Risk Management*) est la référence ANSSI pour l'appréciation des risques numériques en 5 Ateliers :
            * **Atelier 1 (Socle de sécurité & Valeurs métiers / Biens supports)** : Identification du périmètre, des valeurs métiers (processus, données sensibles) et des biens supports (serveurs, routeurs, BDD). Définition des besoins de sécurité selon la triade **DICP** (Disponibilité, Intégrité, Confidentialité, Preuve/Traçabilité) sur une échelle de 1 à 4.
            * **Atelier 2 (Sources de Risques SR & Visées Stratégiques VS)** : Identification des attaquants potentiels (Cybercriminels, États, Concurrents, Vengeurs internes) et de leurs objectifs de haut niveau.
            * **Atelier 3 (Scénarios Stratégiques & Écosystème)** : Cartographie de l'écosystème (partenaires, sous-traitants, fournisseurs Cloud) et modélisation des chemins d'attaque stratégiques traversant les parties prenantes les plus vulnérables.
            * **Atelier 4 (Scénarios Opérationnels & Cyber Kill Chain)** : Déclinaison technique des attaques sous forme de graphes d'attaque (*Cyber Kill Chain* : Reconnaissance $\rightarrow$ Armement $\rightarrow$ Livraison $\rightarrow$ Exploitation $\rightarrow$ Installation $\rightarrow$ Command & Control $\rightarrow$ Actions sur objectifs).
            * **Atelier 5 (Traitement du Risque & PACS)** : Définition de la stratégie de traitement (refus, réduction, transfert, acceptation) et élaboration du **PACS** (*Plan d'Amélioration de la Cybersécurité*).

            ### 2.2 Analyse d'Impact PIA / AIPD (RGPD & CNIL)
            * **Réglementation** : Article 35 du RGPD.
            * **Règle du Déclenchement** : Obligatoire si au moins **2 critères sur 9** de la grille CNIL/EDPB sont remplis (1. Évaluation/Profilage, 2. Décision automatisée, 3. Surveillance systématique, 4. Données sensibles/hautement personnelles, 5. Données à grande échelle, 6. Croisement de données, 7. Personnes vulnérables, 8. Usage d'innovations techniques, 9. Exclusion d'un droit/contrat).
            * **Les 3 Volets de la Démarche** :
              1. Description détaillée du traitement (données, finalités, durées de conservation).
              2. Évaluation de la nécessité et de la proportionnalité des données.
              3. Gestion des risques sur la vie privée des personnes (impacts sur la confidentialité, intégrité, disponibilité).

            ### 2.3 PKI & Certificats Numériques X.509
            * **PKI (Public Key Infrastructure)** :
              - **Root CA** : Autorité racine maîtresse (conservée hors ligne / *offline* pour des raisons de sécurité).
              - **Intermediate CA** : Autorité intermédiaire émettrice des certificats clients/serveurs.
              - **Extension SAN** (*Subject Alternative Name*) : Permet de sécuriser plusieurs noms de domaine / IPs sur un même certificat TLS.
              - **Commandes OpenSSL** :
                * Générer clé privée RSA : `openssl genrsa -out server.key 2048`
                * Créer demande `CSR` : `openssl req -new -key server.key -out server.csr`
                * Vérifier un certificat : `openssl x509 -in server.crt -text -noout`

            ### 2.4 Matrice des Flux & Pare-Feu pfSense (LAN / DMZ / WAN)
            * **DMZ (Zone Démilitarisée)** : Zone réseau tampon hébergeant les serveurs accessibles depuis l'extérieur (Web HTTPS, MQTTS, Mail).
            * **Règle d'Or de Sécurité** : **Interdiction stricte d'initiation de connexions DMZ $\rightarrow$ LAN**. Seul le LAN peut initier vers la DMZ.
            * **Matrice des Ports Active Directory** :
              - DNS : TCP/UDP 53 | Kerberos : TCP/UDP 88 | LDAP : TCP/UDP 389 | LDAPS : TCP 636 | SMB : TCP 445 | RPC : TCP 135.

            ### 2.5 Linux Permissions & Sécurisation
            * **Masque Octal `chmod`** : User/Group/Others. `750` = `rwx` / `r-x` / `---`.
            * **Droits Spéciaux** :
              - **SUID (4000)** : L'exécutable s'exécute avec les privilèges de son propriétaire (ex: `/usr/bin/passwd`).
              - **SGID (2000)** : Les nouveaux fichiers créés dans le dossier héritent du groupe du dossier.
              - **Sticky Bit (1000)** : Seul le propriétaire d'un fichier peut le supprimer dans un dossier partagé (ex: `/tmp`).
            * **ACLs Linux** : Permettent d'attribuer des droits fins à des utilisateurs spécifiques (`getfacl file`, `setfacl -m u:alice:rwx file`).

            ### 2.6 Active Directory & GPO
            * **Structure AD** : Forêt $\rightarrow$ Domaine $\rightarrow$ Unités d'Organisation (OU).
            * **GPO (Group Policy Object)** : Ordre d'application **LSDOU** (Local, Site, Domaine, OU). La règle la plus spécifique (OU) prévaut sur les règles parentes.
            r""")

        with w2_sub2:
            st.markdown("#### 🗂️ Flashcards Actives Semaine 2")
            fc_s2 = [
                {"q": "Combien de critères CNIL remplis déclenchent obligatoirement une analyse PIA/AIPD ?", "a": "Au moins 2 critères sur les 9 de la grille EDPB/CNIL."},
                {"q": "Dans la méthode EBIOS RM, quel atelier formalise les scénarios stratégiques ?", "a": "L'Atelier 3 (Scénarios stratégiques & Écosystème)."},
                {"q": "Pourquoi la CA Racine (Root CA) d'une PKI doit-elle être maintenue hors ligne (offline) ?", "a": "Pour empêcher toute compromission à distance. Si la Root CA est compromise, toute la chaîne de confiance s'effondre."},
                {"q": "Quelle est la règle d'isolation fondamentale entre la DMZ et le LAN ?", "a": "Interdiction absolue d'initiation de connexion depuis la DMZ vers le LAN."},
                {"q": "Quel est l'ordre d'application des GPO dans Active Directory ?", "a": "Ordre LSDOU : Local, Site, Domaine, Unité d'Organisation (OU)."},
                {"q": "Que signifie le droit spécial SUID (4000) sur un fichier exécutable Linux ?", "a": "L'exécutable est lancé avec les privilèges du propriétaire du fichier et non de l'utilisateur qui l'exécute."},
                {"q": "Quel port TCP est utilisé pour les requêtes Active Directory chiffrées en LDAPS ?", "a": "Le port TCP 636 (LDAP classique est sur le port 389)."},
                {"q": "Quelle commande Linux permet d'ajouter un droit de lecture/écriture spécifique à l'utilisateur 'bob' via les ACLs ?", "a": "setfacl -m u:bob:rw fichier"},
                {"q": "Quelle extension d'un certificat X.509 permet de déclarer plusieurs noms de domaine secondaires ?", "a": "L'extension SAN (Subject Alternative Name)."},
                {"q": "Quel port TCP/UDP est utilisé par le service d'authentification Kerberos d'Active Directory ?", "a": "Le port TCP/UDP 88."}
            ]
            for f in fc_s2:
                with st.expander(f"📌 {f['q']}"):
                    st.write(f["a"])

        with w2_sub3:
            st.markdown("#### ✍️ Exercices d'Entraînement Pratiques Semaine 2")
            st.markdown("**Exercice 1 : Déclenchement d'une AIPD / PIA**")
            p_ans = st.radio("Un système de pointeur biométrique d'entreprise traitant les données de 5000 salariés nécessite-t-il un PIA ?", ["Non, moins de 10 000 personnes", "Oui, car il associe données sensibles (biométrie) et personnes vulnérables (salariés)"], key="ex1_s2")
            if st.button("Vérifier Ex 1 (S2)", key="btn_ex1_s2"):
                if "Oui" in p_ans:
                    st.success("🎉 **Exact !** 2 critères CNIL remplis (biométrie + salariés) = PIA obligatoire.")
                else:
                    st.error("❌ Incorrect. Le PIA est obligatoire dès 2 critères remplis.")

            st.markdown("**Exercice 2 : Commande ACL Linux**")
            cmd_acl = st.text_input("Commande setfacl pour accorder rwx à l'utilisateur admin sur le dossier /data :", placeholder="ex: setfacl...", key="cmd_acl_s2")
            if st.button("Vérifier Ex 2 (S2)", key="btn_ex2_s2"):
                if "u:admin:rwx" in cmd_acl.strip():
                    st.success("🎉 **Exact !** `setfacl -m u:admin:rwx /data`.")
                else:
                    st.error("❌ Indice : `setfacl -m u:admin:rwx /data`.")

        with w2_sub4:
            st.markdown("#### 📝 Questionnaire Final - Semaine 2")
            q_w2_list = [
                {"q": "Q1 : Dans EBIOS RM, quel atelier traite le PACS (Plan d'Amélioration de la Cybersécurité) ?", "opts": ["Atelier 1", "Atelier 3", "Atelier 4", "Atelier 5"], "rep": "Atelier 5", "expl": "L'Atelier 5 formalise la stratégie de traitement des risques et le PACS."},
                {"q": "Q2 : Quel est le port standard utilisé par Kerberos dans un domaine Active Directory ?", "opts": ["Port 53", "Port 88", "Port 389", "Port 445"], "rep": "Port 88", "expl": "Kerberos utilise le port TCP/UDP 88."},
                {"q": "Q3 : Quelle est la valeur octale des permissions pour rwx (User), r-x (Group), --- (Others) ?", "opts": ["755", "750", "644", "700"], "rep": "750", "expl": "rwx = 7, r-x = 5, --- = 0, soit 750."},
                {"q": "Q4 : Quel est l'ordre d'application des GPO Active Directory ?", "opts": ["OU -> Domaine -> Site -> Local", "Local -> Site -> Domaine -> OU", "Domaine -> OU -> Site -> Local", "Site -> Local -> OU -> Domaine"], "rep": "Local -> Site -> Domaine -> OU", "expl": "L'ordre est LSDOU : Local, Site, Domaine, OU."},
                {"q": "Q5 : Quelle est la règle d'accès réseau stricte concernant la DMZ vis-à-vis du LAN ?", "opts": ["La DMZ peut tout initier vers le LAN", "La DMZ ne doit jamais initier de connexion vers le LAN", "Le LAN ne peut pas accéder à la DMZ", "La DMZ et le LAN sont bridged"], "rep": "La DMZ ne doit jamais initier de connexion vers le LAN", "expl": "Une DMZ compromise ne doit pas pouvoir attaquer le LAN."}
            ]
            score_w2 = 0
            for idx, qitem in enumerate(q_w2_list):
                st.markdown(f"**{qitem['q']}**")
                ans = st.radio(f"Sélection Q{idx+1} S2 :", qitem["opts"], key=f"qw2_v16_{idx}")
                if ans == qitem["rep"]:
                    score_w2 += 1
            if st.button("Soumettre Questionnaire Semaine 2", type="primary", key="btn_qw2_v16"):
                st.session_state["score_week2"] = score_w2
                st.success(f"🏆 Score Semaine 2 enregistré : **{score_w2} / {len(q_w2_list)}**")
                if score_w2 == len(q_w2_list): st.balloons()

    # ==================== SEMAINE 3 ====================
    with tab_w3:
        st.subheader("🗓️ Semaine 3 : C++, Sockets Python & Génie Logiciel (Cours de A à Z)")
        w3_sub1, w3_sub2, w3_sub3, w3_sub4 = st.tabs(["📚 Cours Complet S3", "🗂️ Flashcards S3", "✍️ Exercices Pratiques S3", "📝 Questionnaire Final S3"])

        with w3_sub1:
            st.markdown(r"""
            ### 3.1 Gestion de la Mémoire en C++ : Pile (Stack) vs Tas (Heap)
            * **La Pile (Stack)** : Mémoire rapide, gérée automatiquement par le compilateur. Les variables locales y sont détruites dès la sortie de portée (*scope*).
            * **Le Tas (Heap)** : Mémoire dynamique gérée manuellement par le développeur via les opérateurs `new` et `delete`.
            * **Allocation Dynamique de Tableaux** :
              - Allocation : `int* tab = new int[100];`
              - Libération : `delete[] tab;` (**impérativement avec `[]`** sous peine de fuite mémoire / *Memory Leak*).
            * **Pointeurs (`*`) vs Références (`&`)** : Un pointeur stocke l'adresse mémoire d'une variable. Une référence est un alias fixe non réassignable.

            ### 3.2 Structures & Unions en Langage C
            * **`struct`** : Chaque membre possède son propre espace mémoire contigu. La taille globale est la somme des tailles des membres.
            * **`union`** : Tous les membres **partagent le même espace mémoire** (égal à la taille du plus grand membre).
            * **Application BTS CIEL** : Décodage direct de trames réseau brutes (ex: convertir 4 octets de réception binaire en un `float` IEEE-754 32 bits).

            ### 3.3 Programmation Orientée Objet (POO) & Abstraction C++
            * **Encapsulation** : Protection des attributs (`private` / `protected`) accessibles via accesseurs `public`.
            * **Héritage** : Réutilisation de code (`class Fille : public Mere`).
            * **Polymorphisme & Destructeur Virtuel** :
              - Méthode virtuelle : `virtual void lire();`
              - **Méthode virtuelle pure** : `virtual void lire() = 0;`
              - **Classe de base abstraite** : Classe possédant au moins une méthode virtuelle pure (non instanciable directement).
              - **Destructeur virtuel obligatoire** : `virtual ~Mere() {}` pour assurer la destruction propre de la classe fille lors d'un `delete` sur un pointeur de classe mère.

            ### 3.4 Concurrence & Threads C++11
            * **`std::thread`** : Permet d'exécuter une fonction en parallèle.
            * **Section Critique & Race Condition** : Conflit d'accès simultané en écriture sur une variable partagée.
            * **`std::mutex` & `std::lock_guard`** : Verrouillage RAII garantissant l'exclusion mutuelle et le déverrouillage automatique.

            ### 3.5 Sockets & Réseau en Python
            * **Serveur TCP** : `socket.socket(AF_INET, SOCK_STREAM)`, `bind()`, `listen()`, `accept()`, `recv()`, `sendall()`.
            * **Client TCP** : `connect()`, `sendall()`, `recv()`.
            * **Formatage** : Encodage/Décodage UTF-8 (`.encode('utf-8')`, `.decode('utf-8')`) et trames `json.dumps()` / `json.loads()`.

            ### 3.6 Versioning Git
            * `git status`, `git add .`, `git commit -m "feat: msg"`, `git push origin main`, `git pull`, `git branch`, `git merge`.
            r""")

        with w3_sub2:
            st.markdown("#### 🗂️ Flashcards Actives Semaine 3")
            fc_s3 = [
                {"q": "Quel opérateur C++ doit être utilisé pour libérer la mémoire d'un tableau alloué avec new float[50] ?", "a": "delete[] (avec les crochets obligatoires)."},
                {"q": "Quelle est la différence d'occupation mémoire entre struct et union en C ?", "a": "Dans une struct, chaque membre a son propre espace. Dans une union, tous les membres partagent le même espace mémoire."},
                {"q": "Qu'est-ce qu'une méthode virtuelle pure en C++ ?", "a": "Une méthode déclarée avec '= 0' (ex: virtual void f() = 0;). Elle rend la classe abstraite."},
                {"q": "Pourquoi une classe mère de base doit-elle obligatoirement posséder un destructeur virtuel ?", "a": "Pour garantir que le destructeur de la classe fille dérivée soit bien appelé lors de la suppression d'un pointeur polymorphe."},
                {"q": "En Python socket, quelle méthode transforme une chaîne de caractères en octets prêts à être transmis ?", "a": "La méthode .encode('utf-8')."},
                {"q": "En C++11, quel objet RAII permet de verrouiller automatiquement un mutex et de le libérer en sortie de scope ?", "a": "std::lock_guard<std::mutex>"},
                {"q": "Quelle est la différence entre la mémoire Pile (Stack) et la mémoire Tas (Heap) ?", "a": "La Pile est rapide et gérée automatiquement. Le Tas est alloué dynamiquement (new/delete) et géré par le développeur."},
                {"q": "Dans Git, quelle commande permet d'enregistrer localement les modifications indexées ?", "a": "git commit -m 'message'"},
                {"q": "En C++, que fait l'opérateur & placé devant une variable existante ?", "a": "Il renvoie l'adresse mémoire de la variable (sa référence)."},
                {"q": "Quel module Python standard permet de manipuler les données au format JSON ?", "a": "Le module json (json.dumps() et json.loads())."}
            ]
            for f in fc_s3:
                with st.expander(f"📌 {f['q']}"):
                    st.write(f["a"])

        with w3_sub3:
            st.markdown("#### ✍️ Exercices d'Entraînement Pratiques Semaine 3")
            st.markdown("**Exercice 1 : Libération Mémoire C++**")
            cpp_ans = st.text_input("Saisissez l'instruction de libération de `float* tab = new float[20];` :", placeholder="ex: delete...", key="cpp_ex_s3")
            if st.button("Vérifier Ex 1 (S3)", key="btn_ex1_s3"):
                if cpp_ans.strip().replace(" ", "") == "delete[]tab;":
                    st.success("🎉 **Exact !** `delete[] tab;`.")
                else:
                    st.error("❌ Indice : `delete[] tab;`.")

            st.markdown("**Exercice 2 : Taille d'une Union C**")
            u_sz = st.number_input("Taille en octets de `union Data { char c; int i; float f; };` (avec int et float sur 4 octets) :", min_value=0, value=0, key="u_sz_s3")
            if st.button("Vérifier Ex 2 (S3)", key="btn_ex2_s3"):
                if u_sz == 4:
                    st.success("🎉 **Exact !** 4 octets (la taille du plus grand membre `float`/`int`).")
                else:
                    st.error("❌ Incorrect. Les membres d'une union partagent l'espace (4 octets ici).")

        with w3_sub4:
            st.markdown("#### 📝 Questionnaire Final - Semaine 3")
            q_w3_list = [
                {"q": "Q1 : Quel opérateur doit être utilisé pour libérer un tableau dynamique `double* d = new double[10];` ?", "opts": ["delete d;", "free(d);", "delete[] d;", "delete(d[]);"], "rep": "delete[] d;", "expl": "L'allocation par new[] requiert delete[]."},
                {"q": "Q2 : Comment qualifie-t-on une classe C++ possédant au moins une méthode virtuelle pure (`= 0`) ?", "opts": ["Classe finale", "Classe abstraite", "Classe statique", "Classe amie"], "rep": "Classe abstraite", "expl": "Une classe avec au moins une méthode virtuelle pure est une classe abstraite."},
                {"q": "Q3 : Quelle est la taille mémoire occupée par une `union` contenant un `char` (1 octet) et un `int` (4 octets) ?", "opts": ["1 octet", "4 octets", "5 octets", "8 octets"], "rep": "4 octets", "expl": "Une union réserve la taille du membre le plus grand (4 octets)."},
                {"q": "Q4 : En Python, quelle méthode du module `socket` permet d'attendre les connexions entrantes sur le serveur ?", "opts": ["connect()", "listen()", "accept()", "bind()"], "rep": "accept()", "expl": "accept() bloque jusqu'à l'arrivée d'un client et renvoie la socket et l'adresse."},
                {"q": "Q5 : Quel mécanisme C++11 évite les oublis de déverrouillage de mutex en cas d'exception ?", "opts": ["std::thread", "std::lock_guard", "std::vector", "std::shared_ptr"], "rep": "std::lock_guard", "expl": "std::lock_guard déverrouille automatiquement le mutex dans son destructeur (RAII)."}
            ]
            score_w3 = 0
            for idx, qitem in enumerate(q_w3_list):
                st.markdown(f"**{qitem['q']}**")
                ans = st.radio(f"Sélection Q{idx+1} S3 :", qitem["opts"], key=f"qw3_v16_{idx}")
                if ans == qitem["rep"]:
                    score_w3 += 1
            if st.button("Soumettre Questionnaire Semaine 3", type="primary", key="btn_qw3_v16"):
                st.session_state["score_week3"] = score_w3
                st.success(f"🏆 Score Semaine 3 enregistré : **{score_w3} / {len(q_w3_list)}**")
                if score_w3 == len(q_w3_list): st.balloons()

    # ==================== SEMAINE 4 ====================
    with tab_w4:
        st.subheader("🗓️ Semaine 4 : Électronique, Bus Industriels & Mathématiques (Cours de A à Z)")
        w4_sub1, w4_sub2, w4_sub3, w4_sub4 = st.tabs(["📚 Cours Complet S4", "🗂️ Flashcards S4", "✍️ Exercices Pratiques S4", "📝 Questionnaire Final S4"])

        with w4_sub1:
            st.markdown(r"""
            ### 4.1 Lois Fondamentales de l'Électricité en Régime Continu
            * **Loi d'Ohm** : $U = R \cdot I$.
            * **Loi des Nœuds (Kirchhoff)** : La somme des intensités entrantes est égale à la somme des intensités sortantes ($\sum I_{\text{entrants}} = \sum I_{\text{sortants}}$).
            * **Loi des Mailles (Kirchhoff)** : La somme algébrique des tensions le long d'une maille fermée est nulle ($\sum U = 0$).
            * **Pont Diviseur de Tension** : Pour deux résistances $R_1$ et $R_2$ en série sous tension $E$ :
              $$U_2 = E \cdot \frac{R_2}{R_1 + R_2}$$
            * **Résistances en Parallèle** : $R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2}$.

            ### 4.2 Condensateurs & Régime Transitoire
            * **Énergie emmagasinée** : $E_c = \frac{1}{2} C \cdot U^2$.
            * **Constante de temps** : $\tau = R \cdot C$ (en secondes).
            * **Équations de Tension** :
              - Charge : $u_C(t) = E \left(1 - e^{-t/\tau}\right)$
              - Décharge : $u_C(t) = E e^{-t/\tau}$
            * **Repères temporels** : À $t = \tau$, $u_C = 63,2\%$ de $E$. À $t = 3\tau$, $u_C = 95\%$. À $t = 5\tau$, régime permanent atteint ($99,3\%$).

            ### 4.3 Oscilloscope & Caractérisation des Signaux
            * **Tension crête-à-crête** : $V_{pp} = N_{\text{div\_vert}} \cdot S_v$.
            * **Amplitude max** : $V_{max} = \frac{V_{pp}}{2}$.
            * **Tension efficace** : $V_{\text{eff}} = \frac{V_{max}}{\sqrt{2}} \approx 0,707 \cdot V_{max}$ (pour un signal sinusoïdal pur).
            * **Période $T$** : $T = N_{\text{div\_horiz}} \cdot S_h$. Fréquence $f = \frac{1}{T}$.

            ### 4.4 Bus CAN Industriel & Automobile (ISO 11898)
            * **Support Physique** : Paires torsadées CAN_H / CAN_L avec $120\,\Omega$ aux terminaisons.
            * **Tensions et Niveaux Logiques** :
              - **Bit Dominant (Logique 0)** : CAN_H = 3.5V, CAN_L = 1.5V $\rightarrow V_{\text{diff}} = 2.0\text{ V}$.
              - **Bit Récessif (Logique 1)** : CAN_H = 2.5V, CAN_L = 2.5V $\rightarrow V_{\text{diff}} = 0.0\text{ V}$.
              - Le bit dominant (0) écrase le bit récessif (1).
            * **Arbitrage CSMA/CR** : Non destructif. L'identifiant (ID) le plus faible est le plus prioritaire.

            ### 4.5 Bus I2C, SPI, UART & CAN/CNA Quantum
            * **I2C** : Synchrone 2 fils (SDA, SCL), adresses 7 bits.
            * **SPI** : Synchrone full-duplex 4 fils (MOSI, MISO, SCLK, CS).
            * **UART** : Asynchrone 2 fils (Tx, Rx).
            * **CAN (ADC) Quantum** : $q = \frac{V_{\text{ref}}}{2^n - 1}$. Valeur brute $N = \text{arrondi}\left(\frac{V_e}{q}\right)$.

            ### 4.6 Mathématiques : Suites, Exponentielle & Logarithme
            * **Suite Arithmétique** : $u_n = u_0 + n \cdot r$. Somme $S = N \cdot \frac{u_{\text{premier}} + u_{\text{dernier}}}{2}$.
            * **Suite Géométrique** : $u_n = u_0 \cdot q^n$. Somme $S = u_{\text{premier}} \cdot \frac{1 - q^N}{1 - q}$.
            * **Exponentielle & Logarithme** : $e^{\ln(x)} = x$, $\ln(e^x) = x$.
            * **Décibels** : $A_{dB} = 10 \log_{10}\left(\frac{P_2}{P_1}\right) = 20 \log_{10}\left(\frac{V_2}{V_1}\right)$.
            r""")

        with w4_sub2:
            st.markdown("#### 🗂️ Flashcards Actives Semaine 4")
            fc_s4 = [
                {"q": "Quelle est la formule du quantum q pour un CAN de n bits sous Vref ?", "a": "q = Vref / (2^n - 1)."},
                {"q": "Sur le bus CAN, quel niveau logique correspond à un état dominant ?", "a": "Le bit 0 (avec Vdiff = 2.0 V). Il écrase le bit récessif 1."},
                {"q": "Quelle est la formule de la constante de temps tau d'un circuit RC ?", "a": "tau = R * C (en secondes)."},
                {"q": "À t = tau, quel pourcentage de la tension finale atteinte un condensateur en charge ?", "a": "63.2 % (1 - e^-1)."},
                {"q": "Quelle est la formule de la tension efficace Veff d'un signal sinusoïdal d'amplitude Vmax ?", "a": "Veff = Vmax / sqrt(2) ≈ 0.707 * Vmax."},
                {"q": "Quelle est la formule du terme général u_n d'une suite géométrique de premier terme u_0 et de raison q ?", "a": "u_n = u_0 * q^n."},
                {"q": "Quelle est la relation entre le gain en Décibels et le rapport de deux puissances P1 et P2 ?", "a": "G_dB = 10 * log10(P2 / P1)."},
                {"q": "Quelles sont les deux lignes du bus I2C ?", "a": "SDA (Serial Data Line) et SCL (Serial Clock Line)."},
                {"q": "Quelles sont les 4 lignes d'un bus SPI ?", "a": "MOSI (Master Out Slave In), MISO (Master In Slave Out), SCLK (Clock), CS/SS (Chip Select)."},
                {"q": "Quelle est la formule du pont diviseur de tension pour U2 aux bornes de R2 en série avec R1 sous E ?", "a": "U2 = E * (R2 / (R1 + R2))."}
            ]
            for f in fc_s4:
                with st.expander(f"📌 {f['q']}"):
                    st.write(f["a"])

        with w4_sub3:
            st.markdown("#### ✍️ Exercices d'Entraînement Pratiques Semaine 4")
            st.markdown("**Exercice 1 : Calcul de Quantum CAN 12 bits**")
            q_can_ex = st.number_input("Quantum en mV d'un CAN 12 bits sous Vref = 5.0 V (arrondi à 2 décimales) :", min_value=0.0, value=0.0, key="can_q_ex_s4")
            if st.button("Vérifier Ex 1 (S4)", key="btn_ex1_s4"):
                if abs(q_can_ex - 1.22) < 0.05:
                    st.success(r"🎉 **Exact !** $q = 5,0 / 4095 \approx 1,22\text{ mV}$.")
                else:
                    st.error(r"❌ Incorrect. $5,0 / 4095 \approx 1,22\text{ mV}$.")

            st.markdown("**Exercice 2 : Pont Diviseur de Tension**")
            u2_ex = st.number_input("Tension U2 pour E = 12V, R1 = 100 ohms, R2 = 300 ohms :", min_value=0.0, value=0.0, key="u2_ex_s4")
            if st.button("Vérifier Ex 2 (S4)", key="btn_ex2_s4"):
                if abs(u2_ex - 9.0) < 0.1:
                    st.success(r"🎉 **Exact !** $U_2 = 12 \cdot \frac{300}{400} = 9,0\text{ V}$.")
                else:
                    st.error(r"❌ Incorrect. $12 \cdot 300/400 = 9\text{ V}$.")

        with w4_sub4:
            st.markdown("#### 📝 Questionnaire Final - Semaine 4")
            q_w4_list = [
                {"q": "Q1 : Quel état logique est dominant sur un bus CAN ?", "opts": ["Le bit 1", "Le bit 0", "L'état haute impédance", "Le bit de parité"], "rep": "Le bit 0", "expl": "Le bit 0 est dominant et s'impose sur le bus."},
                {"q": "Q2 : Quel est le quantum d'un CAN 10 bits sous Vref = 3,3 V ?", "opts": ["3.22 mV", "4.88 mV", "1.22 mV", "6.45 mV"], "rep": "3.22 mV", "expl": "q = 3.3 / 1023 = 3.22 mV."},
                {"q": "Q3 : Quelle est la période T d'un signal de fréquence f = 50 Hz ?", "opts": ["10 ms", "20 ms", "50 ms", "100 ms"], "rep": "20 ms", "expl": "T = 1/50 = 0.020 s = 20 ms."},
                {"q": "Q4 : Quelle est la valeur de u_C à t = tau lors de la charge d'un condensateur sous E = 10V ?", "opts": ["5.0 V", "6.32 V", "9.5 V", "9.93 V"], "rep": "6.32 V", "expl": "u_C(tau) = 10 * (1 - e^-1) = 6.32 V."},
                {"q": "Q5 : Si une puissance P2 est 100 fois supérieure à P1, quel est le gain en Décibels ?", "opts": ["10 dB", "20 dB", "40 dB", "100 dB"], "rep": "20 dB", "expl": "10 * log10(100) = 10 * 2 = 20 dB."}
            ]
            score_w4 = 0
            for idx, qitem in enumerate(q_w4_list):
                st.markdown(f"**{qitem['q']}**")
                ans = st.radio(f"Sélection Q{idx+1} S4 :", qitem["opts"], key=f"qw4_v16_{idx}")
                if ans == qitem["rep"]:
                    score_w4 += 1
            if st.button("Soumettre Questionnaire Semaine 4", type="primary", key="btn_qw4_v16"):
                st.session_state["score_week4"] = score_w4
                st.success(f"🏆 Score Semaine 4 enregistré : **{score_w4} / {len(q_w4_list)}**")
                if score_w4 == len(q_w4_list): st.balloons()

    # ==================== SEMAINE 5 ====================
    with tab_w5:
        st.subheader("🗓️ Semaine 5 : Modélisation SysML/UML & Qualification E6 (Cours de A à Z)")
        w5_sub1, w5_sub2, w5_sub3, w5_sub4 = st.tabs(["📚 Cours Complet S5", "🗂️ Flashcards S5", "✍️ Exercices Pratiques S5", "📝 Questionnaire Final S5"])

        with w5_sub1:
            st.markdown(r"""
            ### 5.1 Modélisation Système SysML
            * **BDD (Block Definition Diagram)** : Représente la structure hiérarchique globale des blocs (composition, agrégation, généralisation).
            * **IBD (Internal Block Diagram)** : Représente la vue interne d'un bloc avec ses ports physiques (`[p_spi]`, `[p_i2c]`) et les flux échangés.
            * **Requirement Diagram (RD)** : Représente les exigences du cahier des charges et leurs relations (`deriveReqt`, `verify`).

            ### 5.2 Modélisation Logicielle UML
            * **Use Case Diagram** : Acteurs, cas d'utilisation, relations `<<include>>` (obligatoire) et `<<extend>>` (optionnel).
            * **Diagramme de Classes** : Attributs, méthodes, visibilité (`+` public, `-` private, `#` protected), agrégation simple (◇) et composition forte (◆).
            * **Diagramme de Séquence** : Chronologie des échanges entre lignes de vie (messages synchrones, asynchrones, retour, blocs `alt`/`loop`).
            * **Diagramme d'États-Transitions** : Comportement dynamique d'un objet (états, transitions, événements, conditions de garde `[ ]`, actions `entry`/`do`/`exit`).

            ### 5.3 Qualification & Plan de Validation Logicielle (PVL avec `pytest`)
            * **PVL** : Définit la stratégie de tests unitaires et d'intégration.
            * **Tests d'Intégration Python (`pytest`)** :
              ```python
              def test_integration_sensor():
                  payload = {"temp": 22.5, "status": "OK"}
                  assert payload["status"] == "OK"
                  assert 0.0 <= payload["temp"] <= 50.0
              ```

            ### 5.4 Gestion de Projet E6 & Diagramme de Gantt
            * **CdCf** : Cahier des Charges Fonctionnel.
            * **Sprint Agile & Gantt** : Découpage des tâches, jalons de livraison et suivi d'avancement.
            r""")

        with w5_sub2:
            st.markdown("#### 🗂️ Flashcards Actives Semaine 5")
            fc_s5 = [
                {"q": "Quel diagramme SysML modélise les flux internes entre les ports des blocs ?", "a": "L'IBD (Internal Block Diagram)."},
                {"q": "Quelle est la différence entre composition et agrégation en diagramme de classes UML ?", "a": "L'agrégation (losange vide ◇) est une association faible. La composition (losange plein ◆) est une relation forte d'appartenance où la destruction du conteneur détruit les composants."},
                {"q": "Dans un diagramme de cas d'utilisation, que signifie la relation <<include>> ?", "a": "Une inclusion obligatoire : le cas d'utilisation source exécute toujours le cas inclus."},
                {"q": "Quel framework Python standard permet de scripter les tests d'intégration du PVL ?", "a": "pytest (utilisant les instructions assert)."},
                {"q": "Dans un diagramme d'états-transitions, où place-t-on la condition de garde ?", "a": "Entre crochets [ condition ] sur la flèche de transition."},
                {"q": "Quel diagramme SysML est utilisé pour structurer les blocs matériels et logiciels globaux ?", "a": "Le BDD (Block Definition Diagram)."},
                {"q": "En UML, que signifie le symbole '+' devant un attribut ou une méthode ?", "a": "Visibilité publique (public)."},
                {"q": "Dans un diagramme de séquence, comment représente-t-on un message de retour ?", "a": "Une flèche pointillée ouverte de droite à gauche."},
                {"q": "Quelle section d'un PVL s'assure que les correctifs n'ont pas introduit d'effets de bord ?", "a": "Les tests de non-régression."},
                {"q": "Quel est l'objectif du Cahier des Charges Fonctionnel (CdCf) ?", "a": "Exprimer les besoins du client sous forme de fonctions de service et de contraintes avec des critères d'appréciation."}
            ]
            for f in fc_s5:
                with st.expander(f"📌 {f['q']}"):
                    st.write(f["a"])

        with w5_sub3:
            st.markdown("#### ✍️ Exercices d'Entraînement Pratiques Semaine 5")
            st.markdown("**Exercice 1 : Traçabilité SysML**")
            u_sys_ans = st.radio("Quelle relation relie un test de validation à son exigence dans un Requirement Diagram ?", ["<<deriveReqt>>", "<<verify>>", "<<include>>"], key="sys_ans_s5")
            if st.button("Vérifier Ex 1 (S5)", key="btn_ex1_s5"):
                if "<<verify>>" in u_sys_ans:
                    st.success("🎉 **Exact !** `<<verify>>`.")
                else:
                    st.error("❌ Incorrect. C'est `<<verify>>`.")

            st.markdown("**Exercice 2 : Assertion Pytest**")
            pytest_code = st.text_input("Instruction d'assertion pour vérifier que status vaut 'OK' :", placeholder="ex: assert...", key="pt_code_s5")
            if st.button("Vérifier Ex 2 (S5)", key="btn_ex2_s5"):
                if "assert" in pytest_code and "==" in pytest_code:
                    st.success("🎉 **Exact !** `assert status == 'OK'`.")
                else:
                    st.error("❌ Indice : `assert status == 'OK'`.")

        with w5_sub4:
            st.markdown("#### 📝 Questionnaire Final - Semaine 5")
            q_w5_list = [
                {"q": "Q1 : Quel diagramme SysML décrit les flux internes échangés entre les ports d'un bloc ?", "opts": ["BDD", "IBD", "Requirement Diagram", "Use Case"], "rep": "IBD", "expl": "L'IBD représente les flux internes et ports."},
                {"q": "Q2 : Quelle forme géométrique caractérise une relation de composition forte en UML ?", "opts": ["Losange vide ◇", "Losange plein ◆", "Triangle vide", "Flèche pointillée"], "rep": "Losange plein ◆", "expl": "La composition utilise le losange plein ◆."},
                {"q": "Q3 : En UML, que signifie la relation <<extend>> entre deux cas d'utilisation ?", "opts": ["Inclusion obligatoire", "Extension optionnelle conditionnelle", "Héritage de classe", "Lien réseau"], "rep": "Extension optionnelle conditionnelle", "expl": "extend représente une extension optionnelle sous condition."},
                {"q": "Q4 : Dans un diagramme d'états-transitions, où écrit-on la condition de garde ?", "opts": ["Entre parenthèses ( )", "Entre crochets [ ]", "Entre accolades { }", "Entre guillemets"], "rep": "Entre crochets [ ]", "expl": "La condition de garde est écrite entre crochets [ ]."},
                {"q": "Q5 : Quel outil Python est préconisé pour l'exécution automatique des fiches de tests du PVL ?", "opts": ["Django", "pytest", "Flask", "NumPy"], "rep": "pytest", "expl": "pytest permet de scripter et d'exécuter les tests automatiques."}
            ]
            score_w5 = 0
            for idx, qitem in enumerate(q_w5_list):
                st.markdown(f"**{qitem['q']}**")
                ans = st.radio(f"Sélection Q{idx+1} S5 :", qitem["opts"], key=f"qw5_v16_{idx}")
                if ans == qitem["rep"]:
                    score_w5 += 1
            if st.button("Soumettre Questionnaire Semaine 5", type="primary", key="btn_qw5_v16"):
                st.session_state["score_week5"] = score_w5
                st.success(f"🏆 Score Semaine 5 enregistré : **{score_w5} / {len(q_w5_list)}**")
                if score_w5 == len(q_w5_list): st.balloons()

    # ==================== SEMAINE 6 ====================
    with tab_w6:
        st.subheader("🗓️ Semaine 6 : Annales Officielles BTS CIEL & Synthèse (Cours de A à Z)")
        w6_sub1, w6_sub2, w6_sub3, w6_sub4 = st.tabs(["📚 Cours & Annales S6", "🗂️ Flashcards S6", "✍️ Exercices Pratiques S6", "📝 Questionnaire Final S6"])

        with w6_sub1:
            st.markdown(r"""
            ### 6.1 Annales Officielles BTS CIEL - Session 2024
            * **Sujet** : Station Industrielle de Surveillance Environnementale.
            * **Compétences clés** :
              - Réseau : Masquage `/28` (14 hôtes utiles).
              - C++ : Correction de fuite mémoire dynamique `delete[] releves;`.
              - IoT : Acquisition SPI à 4 fils.

            ### 6.2 Annales Officielles BTS CIEL - Session 2025
            * **Sujet** : Borne de Recharge de Véhicules Électriques Intelligente.
            * **Compétences clés** :
              - SysAdmin : Durcissement Linux et Active Directory GPO LSDOU.
              - Modélisation : Diagramme de séquence SysML d'authentification RFID.
              - Signal : Calcul du quantum CAN 12 bits sous Vref = 5,0V ($N = 2555$ pour 3,12V).

            ### 6.3 Synthèse des Annales BTS SN-IR (2022-2023)
            * **Sujet 2023** : Ruches connectées LoRaWAN (LPWAN, $868\text{ MHz}$).
            * **Sujet 2022** : Navire scientifique (SNMP, Wireshark, pare-feu).

            ### 6.4 Conseils de Passage des Épreuves Écrites (E4 - 4 Heures)
            * **Gestion du temps** : 1h par grande partie.
            * **Rédaction** : Justifier systématiquement chaque calcul par la formule littérale avant l'application numérique.
            r""")

        with w6_sub2:
            st.markdown("#### 🗂️ Flashcards Actives Semaine 6")
            fc_s6 = [
                {"q": "Dans le sujet BTS CIEL 2024, pourquoi la libération 'delete releves;' d'un tableau new float[24] provoquait-elle un crash ?", "a": "Car seule la mémoire du premier float était libérée. Les 23 autres restaient alloués sur le tas, saturant la mémoire du microcontrôleur."},
                {"q": "Dans le sujet BTS CIEL 2025, quel était le résultat N du CAN 12 bits sous 5V pour Ve = 3.12V ?", "a": "N = 2555 (avec q = 5.0 / 4095 = 1.221 mV)."},
                {"q": "Quelle est la fréquence de la bande ISM utilisée par le protocole LoRaWAN en Europe ?", "a": "868 MHz."},
                {"q": "Quel protocole réseau d'administration est basé sur les OIDs et MIBs pour superviser des équipements ?", "a": "SNMP (Simple Network Management Protocol)."},
                {"q": "Quelle formule littérale doit être écrite avant tout calcul de sous-réseau ?", "a": "N_hotes = 2^(32 - CIDR) - 2."},
                {"q": "Sur un oscilloscope, comment calcule-t-on la fréquence à partir du balayage horizontal ?", "a": "T = N_div * S_h, puis f = 1 / T."},
                {"q": "Quel est le port TCP d'écoute du protocole MQTTS (MQTT chiffré TLS) ?", "a": "Port TCP 8883 (au lieu du port 1883 en clair)."},
                {"q": "Quelle commande Linux affiche l'état d'un service systemd ?", "a": "systemctl status nom_du_service"},
                {"q": "Quelle est la durée d'une épreuve écrite E4 au BTS CIEL ?", "a": "4 heures de composition."},
                {"q": "Quelle est la règle d'or pour la présentation des calculs à l'examen E4 ?", "a": "1. Expression littérale, 2. Application numérique avec unités, 3. Résultat encadré."}
            ]
            for f in fc_s6:
                with st.expander(f"📌 {f['q']}"):
                    st.write(f["a"])

        with w6_sub3:
            st.markdown("#### ✍️ Exercices d'Entraînement Pratiques Semaine 6")
            st.markdown("**Exercice 1 : Question Type Annales 2025**")
            n_25_ex = st.number_input("Entrez la valeur N du CAN 12 bits 5V pour Ve = 3,12V :", min_value=0, value=0, key="n25_ex_s6")
            if st.button("Vérifier Ex 1 (S6)", key="btn_ex1_s6"):
                if n_25_ex == 2555:
                    st.success(r"🎉 **Exact !** $N = 2555$.")
                else:
                    st.error(r"❌ Incorrect. $N = 2555$.")

        with w6_sub4:
            st.markdown("#### 📝 Questionnaire Final - Semaine 6")
            q_w6_list = [
                {"q": "Q1 : Quelle correction doit être appliquée à `delete t;` pour un tableau `int* t = new int[30];` ?", "opts": ["delete t;", "delete[] t;", "free(t);", "delete(t);"], "rep": "delete[] t;", "expl": "Allocation par new[] requiert delete[] t;."},
                {"q": "Q2 : Quel est le nombre N généré par un CAN 12 bits sous 5V pour Ve = 3.12V ?", "opts": ["1024", "2048", "2555", "4095"], "rep": "2555", "expl": "q = 5/4095 = 1.221mV, N = 3.12 / 0.001221 = 2555."},
                {"q": "Q3 : Quelle est la fréquence européenne de transmission du réseau IoT LoRaWAN ?", "opts": ["433 MHz", "868 MHz", "2.4 GHz", "5 GHz"], "rep": "868 MHz", "expl": "LoRaWAN utilise la bande ISM 868 MHz en Europe."},
                {"q": "Q4 : Quel est le port sécurisé standard du protocole MQTTS (MQTT over TLS) ?", "opts": ["Port 1883", "Port 8883", "Port 443", "Port 8080"], "rep": "Port 8883", "expl": "MQTTS utilise le port 8883."},
                {"q": "Q5 : Quelle est la durée officielle de l'épreuve écrite E4 du BTS CIEL ?", "opts": ["2 heures", "3 heures", "4 heures", "5 heures"], "rep": "4 heures", "expl": "L'épreuve E4 dure 4 heures."}
            ]
            score_w6 = 0
            for idx, qitem in enumerate(q_w6_list):
                st.markdown(f"**{qitem['q']}**")
                ans = st.radio(f"Sélection Q{idx+1} S6 :", qitem["opts"], key=f"qw6_v16_{idx}")
                if ans == qitem["rep"]:
                    score_w6 += 1
            if st.button("Soumettre Questionnaire Semaine 6", type="primary", key="btn_qw6_v16"):
                st.session_state["score_week6"] = score_w6
                st.success(f"🏆 Score Semaine 6 enregistré : **{score_w6} / {len(q_w6_list)}**")
                if score_w6 == len(q_w6_list): st.balloons()


elif page == "🎯 Révision Totale BTS Blanc (9-11 Déc)":
    st.markdown("<div class='hero-title'>🎯 Hub de Révision Totale - BTS Blanc (9, 10 & 11 Décembre)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Centrale de préparation intensive regroupant l'intégralité des cours, TP, annales et fiches de synthèse du notebook</p>", unsafe_allow_html=True)

    st.markdown(r"""
    <div class='ciel-card' style='border-left: 6px solid #f59e0b !important; background: #fffbeb;'>
        <h3 style='color: #b45309; margin-top: 0;'>🚨 Objectif Échéance : Examens du 9, 10 et 11 Décembre 2026</h3>
        <p style='color: #78350f;'>Ce hub rassemble <b>l'ensemble des 61 sources et TPs</b> déposés dans votre notebook pour une révision transversale sans aucune impasse.</p>
    </div>
    r""", unsafe_allow_html=True)

    tab_tot1, tab_tot2, tab_tot3 = st.tabs([
        "📚 Synthèse Exhaustive des 6 Piliers", 
        "🛠️ Récapitulatif des TP de Réseau & SysAdmin", 
        "📝 Générateur d'Examen Blanc Multi-Matières"
    ])

    with tab_tot1:
        st.subheader("Synthèse Globale du Programme Officiel")
        st.markdown(r"""
        #### 1. 📶 Réseaux, Telecommunications & Commutation
        * **Modèle OSI / TCP-IP** : 7 couches OSI (PDU: Bit, Trame, Paquet, Segment, Donnée).
        * **Adressage IPv4 / IPv6 & VLSM** : Masques CIDR (`/24` à `/30`), calculs de réseau/broadcast, adresses IPv6 (128 bits, SLAAC, NDP).
        * **VLANs & Trunking 802.1Q** : Tag 4 octets, VLAN natif, routage inter-VLAN (*Router-on-a-Stick*).
        * **Routage** : Statique (`ip route 0.0.0.0 0.0.0.0`), dynamique OSPF (Aires/Areas, état de lien).
        * **Services Infrastructure** : DHCP (DORA), DNS (`A`, `AAAA`, `CNAME`, `MX`, `PTR`), NAT/PAT.
        * **Fibre Optique & RS485** : Réflexion totale interne, Snell-Descartes $\\sin(i_{\text{limite}}) = \frac{n_2}{n_1}$, Monomode (9 µm) vs Multimode, Modbus RTU (Function Code `03`).

        #### 2. 🔒 Cybersécurité, EBIOS RM & RGPD
        * **Cryptographie** : Chiffrement Symétrique (AES-128/256), Asymétrique (RSA, bi-clés), Hachage (SHA-256).
        * **Sécurité Applicative** : Top 10 OWASP (Injections SQL via requêtes préparées, XSS, CSRF).
        * **Sécurité Réseau & Système** : Cisco Port Security (`protect`, `restrict`, `shutdown`), UFW/IPTables, Tunnels VPN (IPsec L3 vs TLS L4), MQTTS.
        * **Méthodologie EBIOS RM (5 Ateliers)** : 1. Cadrage & Valeurs métiers $\rightarrow$ 2. Sources de risque (SR/OV) $\rightarrow$ 3. Scénarios stratégiques $\rightarrow$ 4. Scénarios opérationnels $\rightarrow$ 5. Traitement du risque.
        * **RGPD & PIA** : Privacy Impact Assessment (Art. 35 RGPD, principes de minimisation et de base légale).

        #### 3. 💻 Développement Software (C, C++, Python & Git)
        * **Gestion Mémoire C/C++** : Pile (Stack) vs Tas (Heap), allocation dynamique (`new[]`/`delete[]`), pointeurs bruts, références, fuites mémoire.
        * **Langage C** : Directives préprocesseur (`#define`, `#include`), structures (`struct`), unions (`union` à mémoire partagée), masquage de bits (`& 0x04`).
        * **POO C++** : Encapsulation (`private`/`protected`/`public`), héritage, polymorphisme, destructeurs virtuels, classes abstraites (`virtual void f() = 0;`), STL (`std::vector`, `std::thread`, `std::mutex`).
        * **Python Réseau** : Sockets client/serveur TCP/UDP, traitement HTTP/JSON.

        #### 4. 🖥️ Administration Système (Debian & Active Directory)
        * **Linux Debian** : Permissions octales `chmod` (`755`, `750`), SUID (4000), SGID (2000), Sticky Bit (1000), ACLs (`getfacl`/`setfacl`), `systemd`, `bash` redirection (`>`, `>>`, `|`).
        * **Windows Server Active Directory** : Forêt, Domaine, Unités d'Organisation (OU), GPO (Ordre LSDOU), rôles ADDS, DNS, DHCP.

        #### 5. 🔌 Électronique, Signaux & Bus
        * **Fiches Savoir & Montages** :
          - *Pont en H (Fiche Savoir N°1 & Fiche Montage N°1)* : Pilotage de sens de moteurs CC. Sécurité : ne jamais fermer les deux bras parallèles simultanément.
          - *Pull-Up & Pull-Down (Fiche Savoir N°2)* : Fixation de potentiel $10\text{ k}\Omega$ anti-parasites sur entrées CMOS.
          - *PWM / MLI (Fiche Savoir N°3)* : $V_{\text{moy}} = V_{\text{max}} \cdot \alpha$. Pins 3, 5, 6, 9, 10, 11 (490/980 Hz).
          - *Interruptions & Registres (Fiche Savoir N°4)* : `attachInterrupt()`, registres `DDRB/C/D` bit-à-bit (`DDRD |= (1 << PD3)`).
          - *Mémoire ATmega328P (Fiche Savoir N°5)* : Flash 32 Ko, SRAM 2 Ko (Pile/Tas), EEPROM 1 Ko.
          - *Signal 4-20 mA (Fiche Savoir N°6)* : Boucle de courant linéaire $I(T) = 4 + \frac{T-T_{\text{min}}}{T_{\text{max}}-T_{\text{min}}} \cdot 16\text{ mA}$. $0\text{ mA} = \text{rupture de ligne}$.
          - *Relais & Isolation (Fiche Savoir N°8 & Fiche Montage N°2)* : Isolation galvanique 5V/230V, contacts COM/NO/NC.
          - *Bauds vs bps (Fiche Savoir N°9)* : $D = R \cdot \log_2(M)$.
          - *XON/XOFF & RTS/CTS (Fiche Savoir N°10)* : Contrôle de flux logiciel (`0x11` / `0x13`) et matériel anti-débordement de buffer.
        * **Lois Générales** : Loi d'Ohm ($U = R \cdot I$), Lois de Kirchhoff (Nœuds, Mailles), Pont diviseur de tension ($S = E \cdot \frac{R_2}{R_1 + R_2}$).
        * **Signaux & Numérisation** : $V_{pp}, V_{max}, V_{eff} = \frac{V_{max}}{\\sqrt{2}}$, $f = \frac{1}{T}$, Théorème de Nyquist-Shannon ($Fe \ge 2 F_{max}$).
        * **CAN / CNA** : Résolution $n$ bits, Quantum $q = \frac{V_{ref}}{2^n - 1}$, valeur brute $N = \text{arrondi}\left(\frac{V_e}{q}\right)$.
        * **Bus de Terrain** : I2C (SDA, SCL), SPI (MOSI, MISO, SCLK, CS), UART, Bus CAN (CAN_H, CAN_L, arbitrage CSMA/CR, bit dominant 0 / récessif 1).

        #### 6. 📐 Modélisation UML/SysML & Anglais
        * **SysML** : BDD (Block Definition Diagram), IBD (Internal Block Diagram, ports `[p_spi]`, `[p_i2c]`), Requirement Diagram.
        * **UML** : Classes (Agrégation ◇ vs Composition ◆), Séquence, États-Transitions.
        * **Anglais Technique** : Conditionnels (1st, 2nd, 3rd conditionals) et communication d'incidents IT.
        r""")

    with tab_tot2:
        st.subheader("🛠️ Index des Travaux Pratiques (TPs) du Notebook")
        st.markdown(r"""
        * **TP00 Debian & VMware** : Virtualisation sous VMware Workstation Pro 17, installation ISO Debian 12 `deb-srv`.
        * **TP01 Linux Commandes** : Navigation FHS (`/etc`, `/var`, `/home`), `cat`, `less`, `cp`, `mv`, `mkdir -p`.
        * **TP01 à TP07 ADDS / DNS / DHCP** : Installation du rôle ADDS sous Windows Server, création de domaines, structuration en OUs (Direction, Production, R&D), groupes GG/DL, déploiement de GPO et DHCP/DNS.
        * **TP06 DL ACL** : Gestion des droits d'accès avancés (Domain Local Groups + ACLs sur dossiers partagés).
        * **TP3 Matrice des Flux** : Configuration pfSense Firewall (LAN 192.168.80.x, DMZ 192.168.90.x, WAN NAT), règles de filtrage.
        * **TP6.1 & TP6.2 Scripts Bash** : Automation d'administration système, création d'utilisateurs en masse via fichiers CSV, configuration Samba SMB et sudoers.
        r""")

    with tab_tot3:
        st.subheader("📝 Examen Blanc Global de Synthèse (Mise en Situation Réaliste)")
        st.info("Ce test génère une épreuve de synthèse tirant au sort des questions d'examen sur les 6 blocs du BTS CIEL Blanc.")
        
        if st.button("🚀 Lancer un Sujet Blanc Complet (12 Questions Multi-Matières)", type="primary", key="btn_run_bts_blanc"):
            st.session_state.bts_blanc_active = True

        if st.session_state.get("bts_blanc_active", False):
            st.success("Exam Blanc en cours. Répondez aux questions ci-dessous :")
            st.markdown("---")
            
            q_b1 = st.radio("1. Réseaux : Quelle est la taille du tag inséré dans l'en-tête Ethernet par le protocole IEEE 802.1Q ?", ["2 octets", "4 octets", "8 octets", "12 bits"], key="qb1")
            q_b2 = st.radio("2. Cybersécurité : Quelle méthode prémunit définitivement contre les injections SQL ?", ["Filtrage d'expressions régulières", "Requêtes préparées (paramétrées)", "Chiffrement AES de la BDD", "Désactivation du port 3306"], key="qb2")
            q_b3 = st.radio("3. C++ : Quel opérateur doit être utilisé pour libérer la mémoire de `int* tab = new int[100];` ?", ["delete tab;", "free(tab);", "delete[] tab;", "clear(tab);"], key="qb3")
            q_b4 = st.radio("4. SysAdmin : Quelle est la valeur octale chmod pour rwx (User), r-x (Group), --- (Others) ?", ["755", "750", "644", "777"], key="qb4")
            q_b5 = st.radio("5. Électronique : Quel est le quantum d'un CAN 12 bits sous Vref = 5.0 V ?", ["1.22 mV", "4.88 mV", "0.50 mV", "2.44 mV"], key="qb5")
            q_b6 = st.radio("6. Mathématiques : Si un signal Wi-Fi perd 15% de puissance par mètre, quelle est la raison $q$ de la suite géométrique ?", ["q = 0.15", "q = 0.85", "q = 1.15", "q = -0.15"], key="qb6")

            if st.button("Soumettre mon Sujet Blanc", key="btn_sub_bts_blanc"):
                score_b = 0
                if q_b1 == "4 octets": score_b += 1
                if q_b2 == "Requêtes préparées (paramétrées)": score_b += 1
                if q_b3 == "delete[] tab;": score_b += 1
                if q_b4 == "750": score_b += 1
                if q_b5 == "1.22 mV": score_b += 1
                if q_b6 == "q = 0.85": score_b += 1

                st.markdown(f"### 📊 Note finale Sujet Blanc : **{score_b} / 6** ({score_b/6.0*20:.1f} / 20)")
                if score_b >= 5:
                    st.balloons()
                    st.success("🏆 **Très bon niveau !** Vous êtes prêt pour le BTS Blanc des 9, 10 et 11 Décembre !")
                else:
                    st.warning("⚠️ Des révisions sont nécessaires. Consultez les onglets thématiques ci-dessus.")


elif page == "📈 Mathématiques : Fonctions, Exponentielle & Logarithme":
    st.markdown(r"<div class='hero-title'>📈 Mathématiques Appliquées : Fonctions de Référence, $e^x$ & $\\ln(x)$</div>", unsafe_allow_html=True)
    st.markdown(r"<p style='color:#64748b;'>Cours magistral, propriétés algébriques, dérivation, calculs de décibels, charge $RC$ et simulateurs interactifs</p>", unsafe_allow_html=True)

    tab_exp1, tab_exp2, tab_exp3, tab_exp4 = st.tabs([
        "📖 Cours, Formules & Propriétés Clés", 
        "🧮 Traceur Interactif & Simulateurs (RC, dB)", 
        "🐍 Traduction Algorithmique & Python", 
        "✍️ Exercices Pratiques & Mini-Quiz"
    ])

    with tab_exp1:
        st.subheader("1. Tableau Synthétique des Fonctions de Référence")
        st.markdown(r"""
        | Fonction $f(x)$ | Domaine $\\mathcal{D}_f$ | Dérivée $f'(x)$ | Limites aux Bornes | Sens de Variation |
        | :--- | :--- | :--- | :--- | :--- |
        | **Affine** : $a x + b$ | $\\mathbb{R}$ | $a$ | $\\pm \\infty$ selon le signe de $a$ | Stricte si $a \\neq 0$ (croissante si $a>0$) |
        | **Carré** : $x^2$ | $\\mathbb{R}$ | $2x$ | $\\lim_{x \\to \\pm \\infty} x^2 = +\\infty$ | Décroissante sur $]-\\infty; 0]$, Croissante sur $[0; +\\infty[$ |
        | **Cube** : $x^3$ | $\\mathbb{R}$ | $3x^2$ | $\\lim_{x \\to \\pm \\infty} x^3 = \\pm \\infty$ | Strictement croissante sur $\\mathbb{R}$ |
        | **Racine** : $\\sqrt{x}$ | $[0 ; +\\infty[$ | $\frac{1}{2\\sqrt{x}}$ sur $]0; +\\infty[$ | $\\lim_{x \\to +\\infty} \\sqrt{x} = +\\infty$ | Strictement croissante sur $[0 ; +\\infty[$ |
        | **Inverse** : $\frac{1}{x}$ | $\\mathbb{R}^*$ | $-\frac{1}{x^2}$ | $\\lim_{x \\to \\pm \\infty} \frac{1}{x} = 0$, $\\lim_{x \\to 0^0} \frac{1}{x} = \\pm \\infty$ | Strictement décroissante sur $]-\\infty; 0[$ et $]0; +\\infty[$ |
        | **Exponentielle** : $e^x$ | $\\mathbb{R}$ | $e^x$ | $\\lim_{x \\to -\\infty} e^x = 0$, $\\lim_{x \\to +\\infty} e^x = +\\infty$ | Strictement croissante sur $\\mathbb{R}$ |
        | **Logarithme** : $\\ln(x)$ | $]0 ; +\\infty[$ | $\frac{1}{x}$ | $\\lim_{x \\to 0^+} \\ln(x) = -\\infty$, $\\lim_{x \\to +\\infty} \\ln(x) = +\\infty$ | Strictement croissante sur $]0 ; +\\infty[$ |
        r""")

        st.markdown("---")
        st.subheader("2. La Fonction Exponentielle ($f(x) = e^x$)")
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.markdown(r"""
            #### 📌 Propriétés Fondamentales :
            * **Réciproque** : $e^x$ est la fonction réciproque du logarithme népérien $\\ln(x)$.
            * **Stricte Positivité** : Pour tout $x \\in \\mathbb{R}$, **$e^x > 0$**.
            * **Valeurs remarquables** : $e^0 = 1$, $e^1 = e \approx 2,71828$.
            * **Propriétés Algébriques** :
              * $e^{a+b} = e^a \cdot e^b$
              * $e^{-a} = \frac{1}{e^a}$
              * $e^{a-b} = \frac{e^a}{e^b}$
              * $(e^a)^b = e^{a \cdot b}$
            r""")
        with col_e2:
            st.markdown(r"""
            #### 📐 Dérivée & Croissances Comparées :
            * **Dérivée simple** : $(e^x)' = e^x$.
            * **Dérivée composée** : $(e^{u(x)})' = u'(x) \cdot e^{u(x)}$.
            * **Croissance comparée à $+\\infty$** : L'exponentielle l'emporte sur toute puissance polynomiale :
              $$\\lim_{x \\to +\\infty} \frac{e^x}{x^n} = +\\infty \\quad (n > 0)$$
              $$\\lim_{x \\to -\\infty} x^n e^x = 0$$
            r""")

        st.info(r"💡 **Application BTS CIEL** : Modélisation de la charge et décharge d'un condensateur de capacité $C$ à travers une résistance $R$ : $u_C(t) = E (1 - e^{-t/\tau})$ avec la constante de temps $tau = R \cdot C$.")

        st.markdown("---")
        st.subheader("3. La Fonction Logarithme Népérien ($f(x) = \\ln(x)$)")
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.markdown(r"""
            #### 📌 Propriétés Fondamentales :
            * **Domaine de définition** : Strictement définie sur **$]0 ; +\\infty[$**.
            * **Relations d'inversion** :
              * $e^{\\ln(x)} = x$ pour tout $x > 0$.
              * $\\ln(e^x) = x$ pour tout $x \\in \\mathbb{R}$.
            * **Valeurs remarquables** : $\\ln(1) = 0$, $\\ln(e) = 1$.
            * **Propriétés Algébriques** (Transformation de produit en somme) :
              * $\\ln(a \cdot b) = \\ln(a) + \\ln(b)$
              * $\\ln(\frac{1}{a}) = -\\ln(a)$
              * $\\ln(\frac{a}{b}) = \\ln(a) - \\ln(b)$
              * $\\ln(a^k) = k \cdot \\ln(a)$
              * $\\ln(\\sqrt{a}) = \frac{1}{2} \\ln(a)$
            r""")
        with col_l2:
            st.markdown(r"""
            #### 📐 Dérivée & Atténuation en Décibels :
            * **Dérivée simple** : $(\\ln(x))' = \frac{1}{x}$ sur $]0 ; +\\infty[$.
            * **Dérivée composée** : $(\\ln(u(x)))' = \frac{u'(x)}{u(x)}$ (pour $u(x) > 0$).
            * **Relation avec le Logarithme Décimal ($\\log_{10}$)** :
              $$\\log_{10}(x) = \frac{\\ln(x)}{\\ln(10)}$$
            * **Gain / Atténuation en Décibels (dB)** :
              $$A_{dB} = 10 \\log_{10}\left(\frac{P_2}{P_1}\right) = 20 \\log_{10}\left(\frac{V_2}{V_1}\right)$$
            r""")

        st.markdown("---")
        st.subheader("4. Méthodologie : Résolution d'Équations & Inéquations")
        st.markdown(r"""
        * **Type $e^{u(x)} = k$** :
          * Si $k \le 0$ : Impossible (pas de solution car $e^y > 0$).
          * Si $k > 0$ : Appliquer $\\ln \\Rightarrow u(x) = \\ln(k)$.
        * **Type $\\ln(u(x)) = k$** :
          * Vérifier la condition d'existence $u(x) > 0$.
          * Appliquer l'exponentielle $\\Rightarrow u(x) = e^k$.
        r""")

    with tab_exp2:
        st.subheader("🧮 Traceur & Simulateur Interactif")
        
        sim_choice = st.selectbox("Sélectionnez le module d'expérimentation :", [
            "⚡ Charge & Décharge de Condensateur RC",
            "📡 Calculateur de Gain / Atténuation en Décibels",
            "🔍 Résolveur d'Équations Exponentielles & Logarithmiques"
        ])

        if sim_choice == "⚡ Charge & Décharge de Condensateur RC":
            col_rc1, col_rc2, col_rc3 = st.columns(3)
            with col_rc1:
                val_E = st.number_input("Tension d'alimentation $E$ (V) :", min_value=1.0, max_value=48.0, value=5.0, step=1.0)
            with col_rc2:
                val_R = st.number_input("Résistance $R$ ($k\Omega$) :", min_value=0.1, max_value=500.0, value=10.0, step=1.0)
            with col_rc3:
                val_C = st.number_input("Capacité $C$ ($\\mu F$) :", min_value=0.1, max_value=1000.0, value=100.0, step=10.0)

            tau_ms = (val_R * 1e3) * (val_C * 1e-6) * 1e3  # tau en ms
            
            st.success(f"⚡ **Constante de temps calculée** : $tau = R \cdot C = {val_R}\text{{ k}}\Omega \times {val_C}\\mu\text{{F}} = \\mathbf{{{tau_ms:.2f}\text{{ ms}}}}$")

            # Plotting with matplotlib
            import matplotlib.pyplot as plt
            import numpy as np

            t = np.linspace(0, 5 * tau_ms, 500)
            u_charge = val_E * (1 - np.exp(-t / tau_ms))
            u_decharge = val_E * np.exp(-t / tau_ms)

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(t, u_charge, label=r"Charge : $u_C(t) = E(1 - e^{-t/\tau})$", color="#2563eb", linewidth=2.5)
            ax.plot(t, u_decharge, label=r"Décharge : $u_C(t) = E e^{-t/\tau}$", color="#dc2626", linestyle="--", linewidth=2)
            
            # Highlight tau points
            ax.axvline(x=tau_ms, color="#10b981", linestyle=":", label=f"tau = {tau_ms:.1f} ms")
            ax.axhline(y=0.632 * val_E, color="#10b981", linestyle=":", alpha=0.7)
            ax.scatter([tau_ms], [0.632 * val_E], color="#10b981", s=60, zorder=5)
            ax.annotate(f"63.2% ({0.632*val_E:.2f}V)", (tau_ms, 0.632 * val_E), textcoords="offset points", xytext=(10, -10), fontweight="bold", color="#047857")

            ax.set_title(f"Charge et Décharge RC (E = {val_E}V, tau = {tau_ms:.2f} ms)", fontsize=12, fontweight="bold", color="#1e293b")
            ax.set_xlabel("Temps t (ms)", fontsize=10)
            ax.set_ylabel("Tension uC (V)", fontsize=10)
            ax.grid(True, linestyle="--", alpha=0.5)
            ax.legend(loc="center right")
            plt.tight_layout()

            st.pyplot(fig)

            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.info(f"**À t = tau ({tau_ms:.2f} ms)** : Charge à **63.2%** -> {0.632*val_E:.2f} V")
            with col_m2:
                st.info(f"**À t = 3*tau ({3*tau_ms:.2f} ms)** : Charge à **95.0%** -> {0.95*val_E:.2f} V")
            with col_m3:
                st.info(f"**À t = 5*tau ({5*tau_ms:.2f} ms)** : Régime permanent **99.3%** -> {0.993*val_E:.2f} V")

        elif sim_choice == "📡 Calculateur de Gain / Atténuation en Décibels":
            st.markdown(r"#### Calcul de la variation en dB ($A_{dB} = 10 \\log_{10}(P_2 / P_1)$)")
            col_db1, col_db2 = st.columns(2)
            with col_db1:
                p_in = st.number_input("Puissance d'entrée $P_1$ (mW) :", min_value=0.001, value=100.0, step=10.0)
                p_out = st.number_input("Puissance de sortie $P_2$ (mW) :", min_value=0.001, value=10.0, step=1.0)
                
                gain_db = 10 * np.log10(p_out / p_in)
                if gain_db < 0:
                    st.warning(f"📉 **Atténuation du signal** : $A_{{dB}} = \\mathbf{{{gain_db:.2f}\text{{ dB}}}}$")
                else:
                    st.success(f"📈 **Gain d'amplification** : $G_{{dB}} = \\mathbf{{{gain_db:.2f}\text{{ dB}}}}$")

            with col_db2:
                v_in = st.number_input("Tension d'entrée $V_1$ (V) :", min_value=0.001, value=5.0, step=0.5)
                v_out = st.number_input("Tension de sortie $V_2$ (V) :", min_value=0.001, value=2.5, step=0.5)
                
                gain_v_db = 20 * np.log10(v_out / v_in)
                st.info(f"🔌 **Variation de tension** : $A_{{v, dB}} = 20 \\log_{{10}}(\frac{{{v_out}}}{{{v_in}}}) = \\mathbf{{{gain_v_db:.2f}\text{{ dB}}}}$")

        elif sim_choice == "🔍 Résolveur d'Équations Exponentielles & Logarithmiques":
            st.markdown(r"#### Résolveur de l'équation $A e^{k x} = B$")
            col_eq1, col_eq2, col_eq3 = st.columns(3)
            with col_eq1:
                param_A = st.number_input("Paramètre $A$ :", value=2.0, step=0.5)
            with col_eq2:
                param_k = st.number_input("Paramètre $k$ :", value=-0.5, step=0.1)
            with col_eq3:
                param_B = st.number_input("Résultat $B$ :", value=1.0, step=0.5)

            if param_A == 0 or param_k == 0:
                st.error("Les paramètres A et k doivent être non nuls.")
            else:
                ratio = param_B / param_A
                if ratio <= 0:
                    st.error(f"Impossible : e^({param_k} x) = {ratio:.2f} <= 0. Une exponentielle est toujours strictement positive !")
                else:
                    sol_x = np.log(ratio) / param_k
                    st.success(f"🎯 **Solution de l'équation** : x = **{sol_x:.4f}** (car {param_k}*x = ln({ratio:.4f}))")

    with tab_exp3:
        st.subheader("🐍 Implémentation Algorithmique en Python")
        st.markdown(r"""
        En Python, la bibliothèque standard `math` fournit les fonctions `math.exp(x)` et `math.log(x)` (logarithme népérien).
        Pour le logarithme décimal, on utilise `math.log10(x)`.
        r""")

        st.code(r"""import math

# 1. Calcul de la charge d'un condensateur u_C(t) = E * (1 - exp(-t / tau))
def tension_charge_rc(E, R, C, t):
    tau = R * C
    return E * (1 - math.exp(-t / tau))

# 2. Recherche du temps t requis pour atteindre une tension cible V_cible
def temps_seuil_rc(E, R, C, V_cible):
    if V_cible >= E or V_cible <= 0:
        raise ValueError("V_cible doit etre comprise strictement entre 0 et E")
    tau = R * C
    return -tau * math.log(1 - V_cible / E)

# Test des fonctions pour E=5V, R=10k, C=100uF
E, R, C = 5.0, 10000.0, 100e-6
tau = R * C  # 1.0 seconde
print(f"Constante de temps tau = {tau:.2f} s")
print(f"Tension a t=tau : {tension_charge_rc(E, R, C, tau):.3f} V")
print(f"Temps pour atteindre 4.0V : {temps_seuil_rc(E, R, C, 4.0):.3f} s")
r""", language="python")

        st.markdown("---")
        st.subheader("✍️ Exercice Interactif de Complémentation de Code Python")
        st.write("Complétez la ligne de code ci-dessous pour calculer l'atténuation en dB d'un signal à partir de `P_in` et `P_out` :")

        user_py_code = st.text_input("Complétez : `attenuation_db = ...`", placeholder="10 * math.log10(P_out / P_in)")
        if st.button("Vérifier le code Python"):
            clean_code = user_py_code.strip().replace(" ", "")
            if "10*math.log10(P_out/P_in)" in clean_code or "10*math.log10(p_out/p_in)" in clean_code:
                st.success("🎉 **Code exact !** La formule `10 * math.log10(P_out / P_in)` calcule le gain/atténuation en dB.")
            else:
                st.info("💡 **Indice** : Utilisez `10 * math.log10(P_out / P_in)`.")

    with tab_exp4:
        st.subheader("✍️ Exercices Pratiques Type Examen & Mini-Quiz")

        st.markdown(r"""
        #### 📄 Exercice d'Examen Résolu : Décharge d'un Condensateur
        **Sujet** : La tension de décharge d'un condensateur est donnée par $u_C(t) = 12 e^{-200 t}$ (avec $t$ en secondes).
        1. Quelle est la tension initiale $u_C(0)$ ?
        2. Quelle est la valeur de la constante de temps $tau$ ?
        3. Déterminer l'instant $t_1$ auquel la tension retombe à $1,5\text{ V}$.

        **Corrigé Détaillé** :
        1. $u_C(0) = 12 e^0 = 12 \times 1 = \\mathbf{12\text{ V}}$.
        2. L'exponentielle s'écrit $e^{-t/\tau} = e^{-200 t} \\Rightarrow \frac{1}{tau} = 200 \\Rightarrow tau = \frac{1}{200} = \\mathbf{0,005\text{ s} = 5\text{ ms}}$.
        3. On cherche $t_1$ tel que $12 e^{-200 t_1} = 1,5 \\Rightarrow e^{-200 t_1} = 0,125$.
           $-200 t_1 = \\ln(0,125) \\Rightarrow t_1 = \frac{\\ln(0,125)}{-200} \approx \\mathbf{0,0104\text{ s} = 10,4\text{ ms}}$.
        r""")

        st.markdown("---")
        st.subheader("⚡ Mini-Quiz de Validation : Fonctions Exponentielle & Logarithme")

        quiz_exp_q = [
            {
                "q": "1. Quelle est la valeur exacte de ln(e^3) ?",
                "opts": ["0", "1", "3", "e^3"],
                "rep": "3",
                "expl": "Par propriété d'inversion, ln(e^x) = x pour tout x réel. Donc ln(e^3) = 3."
            },
            {
                "q": "2. Que vaut la dérivée de la fonction f(x) = e^(-2x) ?",
                "opts": ["f'(x) = e^(-2x)", "f'(x) = -2 e^(-2x)", "f'(x) = -2 e^x", "f'(x) = 2 e^(-2x)"],
                "rep": "f'(x) = -2 e^(-2x)",
                "expl": "La dérivée de e^(u(x)) est u'(x) * e^(u(x)). Ici u(x) = -2x donc u'(x) = -2."
            },
            {
                "q": "3. Quelle est la limite de e^x quand x tend vers -infini ?",
                "opts": ["-infini", "0", "1", "+infini"],
                "rep": "0",
                "expl": "La fonction exponentielle possède une asymptote horizontale d'équation y = 0 en -infini : lim_{x -> -inf} e^x = 0."
            },
            {
                "q": "4. Si la puissance d'un signal optique est divisée par 2, quelle est l'atténuation en dB (approx) ?",
                "opts": ["-1 dB", "-3 dB", "-6 dB", "-10 dB"],
                "rep": "-3 dB",
                "expl": "10 * log10(0.5) = 10 * (-0.3010) = -3.01 dB. Une perte de 50% de puissance équivaut à une atténuation de 3 dB."
            }
        ]

        for q_idx, q_item in enumerate(quiz_exp_q):
            st.markdown(f"**{q_item['q']}**")
            ans = st.radio(f"Choix Q{q_idx+1} :", q_item["opts"], key=f"q_exp_{q_idx}")
            if st.button(f"Valider Q{q_idx+1}", key=f"btn_exp_{q_idx}"):
                if ans == q_item["rep"]:
                    st.success(f"🎉 **Exact !** {q_item['expl']}")
                else:
                    st.error(f"❌ **Incorrect.** Réponse attendue : **{q_item['rep']}**. Explication : {q_item['expl']}")
            st.markdown("<br>", unsafe_allow_html=True)



elif page == "🗓️ Planning Révisions BTS Blanc (9-11 Déc)":
    st.markdown("<div class='hero-title'>🗓️ Planning de Révision Intensif - BTS Blanc (9, 10 & 11 Déc 2026)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Programme d'entraînement structuré semaine par semaine pour réussir les épreuves écrites et pratiques</p>", unsafe_allow_html=True)
    
    st.markdown(r'''
    <div class='ciel-card' style='border-left: 6px solid #f59e0b !important;'>
        <h3 style='color: #92400e; margin-top:0;'>⚠️ Objectif Examen : Épreuves du 9, 10 et 11 Décembre 2026</h3>
        <p>Il vous reste <b>6 semaines intensives</b> pour maîtriser la totalité du programme du BTS CIEL Option A. Suivez cette feuille de route hebdomadaire :</p>
    </div>
    r''', unsafe_allow_html=True)
    
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.markdown(r'''
        <div class='ciel-card'>
            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 1 : Réseaux, Adressage & Commutation</h4>
            <ul>
                <li><b>Révisez</b> : Modèle OSI (7 couches), Adressage IPv4/IPv6, Masques VLSM.</li>
                <li><b>Pratiquez</b> : Le <i>Générateur de Subnetting</i> et la configuration des VLANs 802.1Q dans la sandbox <i>Cisco IOS</i>.</li>
                <li><b>Exercice clé</b> : Décodage de trames brutes dans le <i>Lab Wireshark</i>.</li>
            </ul>
        </div>
        
        <div class='ciel-card'>
            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 2 : Cybersécurité & Administration Système</h4>
            <ul>
                <li><b>Révisez</b> : Cryptographie (AES/RSA/SHA), Top 10 OWASP, Active Directory (OUs, GPO LSDOU) et droits Linux (chmod).</li>
                <li><b>Pratiquez</b> : Configuration de règles UFW/IPtables et sécurisation de bases SQL via des requêtes préparées.</li>
                <li><b>Exercice clé</b> : Sandbox <i>Linux Bash</i> (chmod octal) et analyse des tickets Kerberos.</li>
            </ul>
        </div>
        
        <div class='ciel-card'>
            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 3 : Développement C++ & Python Réseau</h4>
            <ul>
                <li><b>Révisez</b> : Gestion de la mémoire (Tas vs Pile), pointeurs `*`, références `&`, `new[]`/`delete[]`, POO (héritage, classes abstraites).</li>
                <li><b>Pratiquez</b> : Debugger C++ (correction de fuites mémoire) et programmation de Sockets TCP/UDP Python.</li>
                <li><b>Exercice clé</b> : Analyse des destructeurs virtuels et des conteneurs STL (`std::vector`).</li>
            </ul>
        </div>
        r''', unsafe_allow_html=True)
        
    with col_w2:
        st.markdown(r'''
        <div class='ciel-card'>
            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 4 : Électronique, Bus Terrain & Oscilloscope</h4>
            <ul>
                <li><b>Révisez</b> : Lois de Kirchhoff, Loi d'Ohm, Bus CAN (CAN_H/L, arbitrage CSMA/CR), Modbus RTU, I2C, SPI et numérisation (CAN/ADC).</li>
                <li><b>Pratiquez</b> : Le <i>Lab Kirchhoff & Ohm</i>, le <i>Lab Oscilloscope</i> (calcul de Vpp, Veff, T, f) et le générateur de Quantum.</li>
                <li><b>Exercice clé</b> : Décodage d'oscillogrammes et calculs de résistance équivalente.</li>
            </ul>
        </div>
        
        <div class='ciel-card'>
            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 5 : Modélisation UML, SysML & Projet E6</h4>
            <ul>
                <li><b>Révisez</b> : Diagrammes BDD, IBD, Exigences, Classes UML, Séquence et États-Transitions.</li>
                <li><b>Pratiquez</b> : Le <i>Lab UML & SysML</i> et la création de plans de tests d'intégration (PVL) avec `pytest`.</li>
                <li><b>Exercice clé</b> : Génération du diagramme de Gantt pour le suivi de projet E6.</li>
            </ul>
        </div>
        
        <div class='ciel-card'>
            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 6 : Annales Officielles & Marathons de Quiz</h4>
            <ul>
                <li><b>Révisez</b> : Sujets d'Annales BTS CIEL 2024 & 2025.</li>
                <li><b>Pratiquez</b> : Lancez le mode <i>Marathon / Méga-Marathon (40-50 questions)</i> dans le Grand Quiz d'Examen.</li>
                <li><b>Objectif Final</b> : Obtenir une moyenne supérieure à 80% sur l'ensemble des domaines !</li>
            </ul>
        </div>
        r''', unsafe_allow_html=True)

# --- PAGE LAB KIRCHHOFF & OHM ---
elif page == "⚡ Lab Kirchhoff, Ohm & Circuits":
    st.markdown("<div class='hero-title'>⚡ Lab Kirchhoff, Loi d'Ohm & Circuits Électriques</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Exercices interactifs d'entraînement sur les lois fondamentales de l'électricité en régime continu</p>", unsafe_allow_html=True)
    
    tab_k1, tab_k2, tab_k3 = st.tabs(["📝 Exercice 1 : Loi d'Ohm & Puissance", "🔗 Exercice 2 : Loi des Mailles & Diviseur de Tension", "🔀 Exercice 3 : Loi des Nœuds & Parallélisme"])
    
    with tab_k1:
        st.subheader("Exercice 1 : Calcul de courant, tension et puissance")
        st.markdown(r'''
        <div class='ciel-card'>
            <p><b>Énoncé</b> : Un sous-ensemble électronique embarqué comprend un résistor de résistance <b>R = 120 Ω</b> alimenté sous une tension continue de <b>U = 24 V</b>.</p>
        </div>
        r''', unsafe_allow_html=True)
        
        col_e1_1, col_e1_2 = st.columns(2)
        with col_e1_1:
            u_i1 = st.number_input("Calculer l'intensité I (en Ampères A) :", value=0.0, step=0.01, key="k_i1")
        with col_e1_2:
            u_p1 = st.number_input("Calculer la puissance dissipée P (en Watts W) :", value=0.0, step=0.1, key="k_p1")
            
        if st.button("Vérifier l'Exercice 1", type="primary", key="btn_ex1"):
            if abs(u_i1 - 0.2) <= 0.01 and abs(u_p1 - 4.8) <= 0.1:
                st.balloons()
                st.success(r"🎉 **Calculs exacts !**\\n- Intensité : $I = \\\frac{U}{R} = \\\frac{24}{120} = 0,20 \\\text{ A}$ (soit $200 \\\text{ mA}$)\\n- Puissance : $P = U \\\cdot I = 24 \\\cdot 0,2 = 4,80 \\\text{ W}$ (ou $P = R \\\cdot I^2 = 120 \\\cdot 0,04 = 4,80 \\\text{ W}$)")
            else:
                st.error(r"❌ **Réponse incorrecte.** Vérifiez vos formules : $I = \\\frac{U}{R}$ et $P = U \\\cdot I$.")
                st.info(r"💡 **Rappel** : $I = 24 / 120 = 0,20 \\\text{ A}$ et $P = 24 \\\times 0,20 = 4,80 \\\text{ W}$.")
                
    with tab_k2:
        st.subheader("Exercice 2 : Loi des Mailles & Pont Diviseur de Tension")
        st.markdown(r'''
        <div class='ciel-card'>
            <p><b>Énoncé</b> : Un capteur est alimenté par un générateur idéal $E = 15 \\\text{ V}$ connecté en série avec deux résistances $R_1 = 200 \\\Omega$ et $R_2 = 300 \\\Omega$.</p>
        </div>
        r''', unsafe_allow_html=True)
        
        u_u2 = st.number_input("Calculer la tension U2 aux bornes de R2 (en Volts V) :", value=0.0, step=0.1, key="k_u2")
        
        if st.button("Vérifier l'Exercice 2", type="primary", key="btn_ex2"):
            if abs(u_u2 - 9.0) <= 0.1:
                st.balloons()
                st.success(r"🎉 **Pont Diviseur de Tension exact !**\\n$$U_2 = E \\\cdot \\\frac{R_2}{R_1 + R_2} = 15 \\\cdot \\\frac{300}{200 + 300} = 15 \\\cdot \\\frac{300}{500} = 9,0 \\\text{ V}$$")
            else:
                st.error(r"❌ **Calcul incorrect.** Formule du pont diviseur : $U_2 = E \\\cdot \\\frac{R_2}{R_1 + R_2}$.")
                st.info(r"💡 **Démonstration** : $U_2 = 15 \\\times \\\frac{300}{500} = 9,0 \\\text{ V}$.")
                
    with tab_k3:
        st.subheader("Exercice 3 : Loi des Nœuds & Résistances en Parallèle")
        st.markdown(r'''
        <div class='ciel-card'>
            <p><b>Énoncé</b> : Un nœud d'un circuit reçoit un courant principal $I = 1,5 \\\text{ A}$ qui se sépare en deux branches en parallèle de résistances $R_1 = 60 \\\Omega$ et $R_2 = 120 \\\Omega$.</p>
        </div>
        r''', unsafe_allow_html=True)
        
        col_e3_1, col_e3_2 = st.columns(2)
        with col_e3_1:
            u_req = st.number_input("Résistance équivalente Req (en Ω) :", value=0.0, step=0.1, key="k_req")
        with col_e3_2:
            u_i1_par = st.number_input("Courant I1 traversant R1 (en Ampères A) :", value=0.0, step=0.1, key="k_i1_par")
            
        if st.button("Vérifier l'Exercice 3", type="primary", key="btn_ex3"):
            if abs(u_req - 40.0) <= 0.1 and abs(u_i1_par - 1.0) <= 0.1:
                st.balloons()
                st.success(r"🎉 **Calculs exacts !**\\n- Résistance équivalente : $R_{\\\text{eq}} = \\\frac{R_1 \\\cdot R_2}{R_1 + R_2} = \\\frac{60 \\\cdot 120}{180} = 40 \\\Omega$\\n- Tension totale : $U = R_{\\\text{eq}} \\\cdot I = 40 \\\cdot 1,5 = 60 \\\text{ V}$\\n- Courant I1 : $I_1 = \\\frac{U}{R_1} = \\\frac{60}{60} = 1,0 \\\text{ A}$ (et $I_2 = 0,5 \\\text{ A}$, vérifiant $1,0 + 0,5 = 1,5 \\\text{ A}$ par la Loi des Nœuds).")
            else:
                st.error(r"❌ **Résultat incorrect.** Formules : $R_{\\\text{eq}} = \\\frac{R_1 \\\cdot R_2}{R_1 + R_2}$ et $I_1 = I \\\cdot \\\frac{R_2}{R_1 + R_2}$.")

# --- PAGE LAB OSCILLOSCOPE ---
elif page == "📺 Lab Oscilloscope & Mesures Physiques":
    st.markdown("<div class='hero-title'>📺 Lab Oscilloscope & Analyse d'Oscillogrammes</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Analyse graphique de signaux temporels et réglages de sensibilité verticale / horizontale</p>", unsafe_allow_html=True)
    
    st.markdown(r'''
    <div class='ciel-card'>
        <h3 style='color:#1e3a8a; margin-top:0;'>🔍 Oscillogramme à analyser (Signal Sinusoïdal)</h3>
        <p>Réglages de l'oscilloscope :</p>
        <ul>
            <li><b>Sensibilité Verticale ($S_v$)</b> : <code>2,0 V/div</code></li>
            <li><b>Base de temps Horizontal ($S_h$)</b> : <code>1,0 ms/div</code></li>
        </ul>
    </div>
    r''', unsafe_allow_html=True)
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    fig_osc, ax_osc = plt.subplots(figsize=(9, 4.5))
    t_vals = np.linspace(0, 10, 500)
    v_vals = 3.0 * np.sin(2 * np.pi * t_vals / 4.0)
    
    ax_osc.plot(t_vals, v_vals, color='#10b981', linewidth=2.5, label='Voie CH1')
    ax_osc.set_facecolor('#020617')
    fig_osc.patch.set_facecolor('#0f172a')
    
    ax_osc.set_xlim(0, 10)
    ax_osc.set_ylim(-5, 5)
    ax_osc.set_xticks(np.arange(0, 11, 1))
    ax_osc.set_yticks(np.arange(-5, 6, 1))
    ax_osc.grid(True, which='both', color='#334155', linestyle='--', linewidth=0.8)
    
    ax_osc.axhline(0, color='#64748b', linewidth=1.2)
    ax_osc.axvline(0, color='#64748b', linewidth=1.2)
    ax_osc.set_xlabel('Temps (Divisions horizontales - 1 div = 1 ms)', color='#94a3b8', fontsize=10)
    ax_osc.set_ylabel('Tension (Divisions verticales - 1 div = 2 V)', color='#94a3b8', fontsize=10)
    ax_osc.tick_params(colors='#94a3b8')
    plt.title("Écran de l'Oscilloscope Numérique (CH1)", color='#38bdf8', fontsize=12, fontweight='bold')
    
    st.pyplot(fig_osc)
    
    st.markdown("### ✍️ Répondez aux questions d'analyse :")
    
    c_o1, c_o2 = st.columns(2)
    with c_o1:
        u_vpp = st.number_input("1. Tension crête-à-crête Vpp (en Volts V) :", value=0.0, step=1.0, key="osc_vpp")
        u_vmax = st.number_input("2. Amplitude / Tension maximale Vmax (en Volts V) :", value=0.0, step=1.0, key="osc_vmax")
        u_veff = st.number_input("3. Valeur efficace Veff (en Volts V, arrondi à 0.1) :", value=0.0, step=0.1, key="osc_veff")
    with c_o2:
        u_t_ms = st.number_input("4. Période T (en millisecondes ms) :", value=0.0, step=0.5, key="osc_t")
        u_freq = st.number_input("5. Fréquence f (en Hertz Hz) :", value=0.0, step=10.0, key="osc_f")
        
    if st.button("Vérifier l'analyse de l'oscillogramme", type="primary", key="btn_osc"):
        vpp_ok = (abs(u_vpp - 12.0) <= 0.1)
        vmax_ok = (abs(u_vmax - 6.0) <= 0.1)
        veff_ok = (abs(u_veff - 4.2) <= 0.2)
        t_ok = (abs(u_t_ms - 4.0) <= 0.1)
        f_ok = (abs(u_freq - 250.0) <= 5.0)
        
        if vpp_ok and vmax_ok and veff_ok and t_ok and f_ok:
            st.balloons()
            st.success(r"🏆 **Analyse d'oscillogramme parfaite !**\\n- $V_{\\\text{pp}} = 6 \\\text{ div} \\\times 2,0 \\\text{ V/div} = 12,0 \\\text{ V}$\\n- $V_{\\\text{max}} = 6,0 \\\text{ V}$\\n- $V_{\\\text{eff}} = \\\frac{6,0}{\\\\sqrt{2}} \\\approx 4,24 \\\text{ V}$\\n- Période $T = 4 \\\text{ div} \\\times 1,0 \\\text{ ms/div} = 4,0 \\\text{ ms} = 0,004 \\\text{ s}$\\n- Fréquence $f = \\\frac{1}{0,004} = 250 \\\text{ Hz}$")
        else:
            st.error("❌ **Certaines valeurs sont incorrectes.** Lisez le nombre de carreaux occupés par le motif sinusoïdal sur l'écran.")
            st.info(r"💡 **Aide du professeur** :\\n- Le signal s'étend de -3 div à +3 div $\\\\Rightarrow 6$ div au total $\\\\Rightarrow V_{\\\text{pp}} = 6 \\\times 2 = 12 \\\text{ V}$.\\n- Un motif complet se répète tous les 4 carreaux horizontaux $\\\\Rightarrow T = 4 \\\times 1 \\\text{ ms} = 4 \\\text{ ms}$.\\n- $f = 1 / 0,004 \\\text{ s} = 250 \\\text{ Hz}$.")


# --- 2. PAGE ENCYCLOPÉDIE DES COURS ---
elif page == "📚 Encyclopédie des Cours & TPs":
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
                st.markdown(fr"""
                **Démonstration du calcul :**
                1. Quantum : $$q = \frac{{V_{{ref}}}}{{2^n - 1}} = \frac{{{vref}}}{{2^{{{bits}}} - 1}} = \frac{{{vref}}}{{{(2**bits)-1}}} \approx {st.session_state.adc_sol_q_mv/1000.0:.6f} \text{{ V}}$$
                2. Valeur entière : $$N = \text{{arrondi}}\left(\frac{{V_e}}{{q}}\right) = \text{{arrondi}}\left(\frac{{{ve}}}{{{st.session_state.adc_sol_q_mv/1000.0:.6f}}}\right) = {st.session_state.adc_sol_n}$$
                r""")
                
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
            st.code(r"""
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
            r""", language="text")
        with col_s2:
            st.markdown("#### Internal Block Diagram (IBD)")
            st.code(r"""
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
            r""", language="text")
            
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
        st.code(r"""
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
        r""", language="text")

# --- 5. PAGE TESTS D'INTÉGRATION E6 ---
elif page == "🧪 Qualification & Tests E6":
    st.markdown("<div class='hero-title'>🧪 Qualification Logicielle & Tests E6</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Méthodologie du Plan de Validation Logicielle (PVL) et assertions de tests automatisés</p>", unsafe_allow_html=True)
    
    st.write(r"""
    Dans l'épreuve **E6**, vous devez prouver la conformité de vos développements avec le cahier des charges initial au moyen d'un **Plan de Validation Logicielle (PVL)** rigoureux.
    r""")
    
    st.markdown("### 💻 Exemple de Script de Test d'Intégration Réseau & BDD (Python / PyTest) :")
    st.code(r"""
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
    r""", language="python")
    
    st.markdown("### ✍️ Testez vos réflexes d'Assurance Qualité :")
    st.write("Complétez l'assertion Python pour valider qu'un code de retour HTTP reçu d'un serveur Web vaut bien **200 (OK)** :")
    user_assert = st.text_input("Saisissez votre ligne d'assertion :", placeholder="Entrez votre assertion (ex: assert ... == ...)", key="qa_assert")
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
        st.markdown(r"""
        **Mise en situation** : Une passerelle d'acquisition collecte les données de capteurs environnementaux et les publie sur un serveur sécurisé.
        r""")
        
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
        c_24 = st.text_input("Instruction C++ :", placeholder="Entrez votre instruction de libération C++...", key="c_24_in")
        if st.button("Valider la Q2 (2024)"):
            if c_24.strip().replace(" ", "") == "delete[]t;":
                st.success("✅ **Code conforme aux critères officiels d'examen !**")
            else:
                st.error("❌ **Erreur.** La commande exacte est `delete[] t;`.")
                
    else:
        st.markdown("### 📕 Session 2025 : Borne de Recharge de Véhicules Électriques")
        st.markdown(r"""
        **Mise en situation** : Une borne intelligente supervise la recharge de véhicules via une interface Linux connectée en réseau et surveille la tension secteur.
        r""")
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
    st.markdown("<div class='hero-title'>🗂️ Flashcards Actives & Auto-Évaluation</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Stimulez votre mémoire active avec 105 cartes mémoire réflexes couvrant tout le programme du BTS CIEL (avec conseils prof, redirections de cours et vidéos YouTube)</p>", unsafe_allow_html=True)
    
    if "fc_mastered" not in st.session_state:
        st.session_state.fc_mastered = set()
        
    yt_prefix = 'https://www.youtube.com/watch?v='
        
    col_f1, col_f2, col_f3 = st.columns([1.5, 1.5, 1])
    with col_f1:
        all_mods = ["Tous les modules"] + list(dict.fromkeys([f["module"] for f in FLASHCARDS_DATA]))
        sel_m = st.selectbox("📁 Filtrer par domaine :", all_mods)
        
    f_list = FLASHCARDS_DATA if sel_m == "Tous les modules" else [f for f in FLASHCARDS_DATA if f["module"] == sel_m]
    
    with col_f2:
        all_chaps = ["Tous les chapitres"] + list(dict.fromkeys([f["chap"] for f in f_list]))
        sel_c = st.selectbox("📖 Filtrer par chapitre :", all_chaps)
        
    if sel_c != "Tous les chapitres":
        f_list = [f for f in f_list if f["chap"] == sel_c]
        
    with col_f3:
        mode_fc = st.radio("👁️ Affichage :", ["🎴 Carte par Carte", "📋 Liste Complète"], horizontal=True)
        
    st.markdown("---")
    
    total_filtered = len(f_list)
    mastered_in_filter = len([f for f in f_list if f["id"] in st.session_state.fc_mastered])
    pct_mastered = (mastered_in_filter / total_filtered * 100) if total_filtered > 0 else 0
    
    st.progress(mastered_in_filter / max(1, total_filtered))
    st.caption(f"🏆 **Progression sur la sélection** : {mastered_in_filter} / {total_filtered} cartes maîtrisées ({pct_mastered:.1f}%)")
    
    if mode_fc == "🎴 Carte par Carte":
        if "fc_idx" not in st.session_state: st.session_state.fc_idx = 0
        if st.session_state.fc_idx >= len(f_list): st.session_state.fc_idx = 0
        
        cur_fc = f_list[st.session_state.fc_idx]
        is_mastered = cur_fc["id"] in st.session_state.fc_mastered
        
        st.markdown(f"**Domaine :** `{cur_fc['module']}` | **Chapitre :** *{cur_fc['chap']}* | **Carte `{st.session_state.fc_idx + 1} / {len(f_list)}`**")
        
        if is_mastered:
            st.success("✅ Carte enregistrée comme **Maîtrisée**")
        else:
            st.info("⏳ Carte en cours d'apprentissage")
            
        st.markdown(f"""
        <div class='ciel-card' style='border-left: 6px solid #2563eb !important; background: #f8fafc;'>
            <h3 style='color: #1e3a8a; margin-top: 0;'>❓ Question :</h3>
            <p style='font-size: 1.15rem; font-weight: 600; color: #0f172a;'>{cur_fc['q']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        user_fc_ans = st.text_area("✍️ Rédigez votre réponse réflexe avant de vérifier :", key=f"fc_txt_{cur_fc['id']}")
        
        rev = st.checkbox("👁️ Afficher la Solution & Conseils Examen", key=f"rev_{cur_fc['id']}")
        
        if rev:
            st.markdown("---")
            st.markdown("### ✅ Solution Détaillée & Fiche Réflexe")
            st.markdown(f"**Réponse attendue :**\n{cur_fc['a']}")
            st.markdown(f"{cur_fc['note']}")
            st.info(f"**{cur_fc['cours_ref']}**")
            
            yt_link = yt_prefix + cur_fc['v_id']
            st.markdown(f"#### 📹 Leçon Vidéo Recommandée : *{cur_fc['v_title']}*")
            st.link_button("▶️ Regarder la leçon sur YouTube", yt_link, type="primary")
            
        st.markdown("<br>", unsafe_allow_html=True)
        bcol1, bcol2, bcol3, bcol4 = st.columns(4)
        with bcol1:
            if st.button("⬅️ Précédente", use_container_width=True):
                st.session_state.fc_idx = (st.session_state.fc_idx - 1) % len(f_list)
                st.rerun()
        with bcol2:
            if st.button("✅ Maîtrisée", use_container_width=True):
                st.session_state.fc_mastered.add(cur_fc["id"])
                st.success("Carte ajoutée aux acquis !")
                st.rerun()
        with bcol3:
            if st.button("❌ À Revoir", use_container_width=True):
                st.session_state.fc_mastered.discard(cur_fc["id"])
                st.warning("Carte conservée dans la liste de révision.")
                st.rerun()
        with bcol4:
            if st.button("➡️ Suivante", use_container_width=True):
                st.session_state.fc_idx = (st.session_state.fc_idx + 1) % len(f_list)
                st.rerun()
                
    else:
        st.markdown(f"### 📋 Liste des {len(f_list)} Flashcards sélectionnées")
        for fc in f_list:
            m_status = "✅" if fc["id"] in st.session_state.fc_mastered else "⏳"
            with st.expander(f"{m_status} Carte N°{fc['id']} : {fc['q']}"):
                st.markdown(f"**Module :** `{fc['module']}` | **Chapitre :** *{fc['chap']}*")
                st.markdown(f"**Réponse :** {fc['a']}")
                st.markdown(f"{fc['note']}")
                st.info(f"**{fc['cours_ref']}**")
                yt_link = yt_prefix + fc['v_id']
                st.link_button(f"▶️ Vidéo : {fc['v_title']}", yt_link)


elif page == "🔍 Lab Décodeur Wireshark":
    st.markdown("<div class='hero-title'>🔍 Lab Décodeur Wireshark</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Apprenez à décoder les octets hexadécimaux bruts d'une capture réseau</p>", unsafe_allow_html=True)
    
    st.markdown(r"""
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
    r""", unsafe_allow_html=True)
    
    st.markdown("### Décryptage des champs du paquet :")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        ans_ver = st.selectbox("Version IP (Premier nibble '4') :", ["IPv4 (4)", "IPv6 (6)"])
        ans_ihl = st.number_input("Longueur de l'en-tête (IHL) en mots de 32 bits (Deuxième nibble '5') :", min_value=0, max_value=15, value=0)
        ans_ttl = st.number_input("TTL décimal (Octet 8 : hex '40') :", min_value=0, max_value=255, value=0)
    with col_w2:
        ans_proto = st.selectbox("Protocole encapsulé (Octet 9 : hex '06') :", ["ICMP (1)", "TCP (6)", "UDP (17)"])
        ans_src = st.text_input("IP Source décodée (Octets 12-15 : 'C0 A8 0A 05') :", placeholder="Format: X.X.X.X")
        ans_dst = st.text_input("IP Destination décodée (Octets 16-19 : 'C0 A8 0A 01') :", placeholder="Format: X.X.X.X")
        
    if st.button("Valider l'analyse de trame", type="primary"):
        ok = (ans_ver == "IPv4 (4)" and ans_ihl == 5 and ans_ttl == 64 and ans_proto == "TCP (6)" and ans_src.strip() == "192.168.10.5" and ans_dst.strip() == "192.168.10.1")
        if ok:
            st.balloons()
            st.success("🏆 **Décodage parfait ! Vous maîtrisez l'anatomie de l'en-tête IPv4.**")
        else:
            st.error("❌ **Certains champs sont incorrects.**")
            st.info(r"💡 **Aide** : C0 = 192, A8 = 168, 0A = 10, 05 = 5 $\rightarrow$ `192.168.10.5` | TTL 0x40 = 64 en décimal.")

# --- 9. PAGE SANDBOXES DE COMMANDES ---
elif page == "💻 Sandboxes & Terminaux Pratiques":
    st.markdown("<div class='hero-title'>⚡ Sandboxes & Terminaux Pratiques</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Environnement d'entraînement interactif complet : exercez-vous aux commandes d'examen sous Cisco IOS, Linux, C++, PowerShell Active Directory et IoT Industriel.</p>", unsafe_allow_html=True)
    
    t_cisco, t_linux, t_cpp, t_ad, t_iot = st.tabs([
        "📶 Cisco IOS (Switch & Routeur)",
        "🖥️ Linux Bash & SysAdmin",
        "💻 C++ Debugger & Mémoire",
        "🔒 Active Directory & PowerShell",
        "🔌 IoT & Bus Industriels (Modbus/MQTT)"
    ])
    
    # ------------------ TAB 1 : CISCO IOS ------------------
    with t_cisco:
        st.subheader("📶 Centre de Commandes Cisco IOS (Épreuves E4 & E5)")
        cisco_scenario = st.selectbox(
            "Choisissez un scénario de configuration Cisco :",
            [
                "1. Affectation de VLAN sur Port d'Accès",
                "2. Liaison Trunking 802.1Q & VLAN Natif",
                "3. Routage Inter-VLAN (Router-on-a-Stick)",
                "4. Sécurité des Ports (Port Security)",
                "5. Routage Statique IPv4 par Défaut"
            ],
            key="cisco_scen_select"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if "1. Affectation" in cisco_scenario:
            st.info("📋 **Objectif** : Vous êtes connecté sur l'interface `FastEthernet0/5` du commutateur. Configurez ce port en mode accès et affectez-le au **VLAN 30**.")
            st.markdown("<div class='terminal-header'>Switch-BTS-CIEL(config-if)#</div>", unsafe_allow_html=True)
            c1_in = st.text_input("Saisissez la commande Cisco :", placeholder="ex: switchport...", key="c1_in")
            if st.button("Valider la commande Cisco (VLAN Accès)", type="primary", key="btn_c1"):
                cmd_clean = c1_in.strip().lower()
                if cmd_clean in ["switchport access vlan 30", "sw acc vl 30", "switchport access vlan30"]:
                    st.success("✅ **Commande exacte !** Le port FastEthernet0/5 est désormais membre actif du VLAN 30.")
                else:
                    st.error("❌ Commande rejetée par l'interpréteur Cisco IOS.")
                    st.info("💡 **Commande attendue** : `switchport access vlan 30`")

        elif "2. Liaison Trunking" in cisco_scenario:
            st.info("📋 **Objectif** : Sur l'interface `GigabitEthernet0/1` reliant deux commutateurs, activez le mode **Trunk**, autorisez les VLANs **10, 20 et 30**, et définissez le **VLAN natif 99**.")
            st.markdown("<div class='terminal-header'>Switch-BTS-CIEL(config-if)#</div>", unsafe_allow_html=True)
            c2_m = st.text_input("1. Commande d'activation du mode Trunk :", placeholder="ex: switchport mode...", key="c2_m")
            c2_v = st.text_input("2. Commande d'autorisation des VLANs 10,20,30 :", placeholder="ex: switchport trunk allowed...", key="c2_v")
            c2_n = st.text_input("3. Commande d'assignation du VLAN natif 99 :", placeholder="ex: switchport trunk native...", key="c2_n")
            if st.button("Valider la configuration Trunking", type="primary", key="btn_c2"):
                ok1 = c2_m.strip().lower() in ["switchport mode trunk", "sw mo tr"]
                ok2 = "allowed vlan" in c2_v.strip().lower() and "10" in c2_v and "20" in c2_v and "30" in c2_v
                ok3 = c2_n.strip().lower() in ["switchport trunk native vlan 99", "sw tr nat vl 99"]
                if ok1 and ok2 and ok3:
                    st.success("🎉 **Lien Trunk entièrement configuré avec succès !**")
                else:
                    if not ok1: st.error("❌ Étape 1 : Utilisez `switchport mode trunk`")
                    if not ok2: st.error("❌ Étape 2 : Utilisez `switchport trunk allowed vlan 10,20,30`")
                    if not ok3: st.error("❌ Étape 3 : Utilisez `switchport trunk native vlan 99`")

        elif "3. Routage Inter-VLAN" in cisco_scenario:
            st.info("📋 **Objectif** : Sur la sous-interface `GigabitEthernet0/0.10` du routeur, activez l'encapsulation **dot1Q pour le VLAN 10** puis attribuez l'adresse IP `192.168.10.254/24`.")
            st.markdown("<div class='terminal-header'>Router-CIEL(config-subif)#</div>", unsafe_allow_html=True)
            c3_enc = st.text_input("1. Commande d'encapsulation 802.1Q :", placeholder="ex: encapsulation...", key="c3_enc")
            c3_ip = st.text_input("2. Commande d'attribution de l'adresse IP :", placeholder="ex: ip address...", key="c3_ip")
            if st.button("Valider le Router-on-a-Stick", type="primary", key="btn_c3"):
                ok_enc = c3_enc.strip().lower() in ["encapsulation dot1q 10", "encap dot1q 10"]
                ok_ip = c3_ip.strip().lower() == "ip address 192.168.10.254 255.255.255.0"
                if ok_enc and ok_ip:
                    st.success("🎉 **Sous-interface de routage inter-VLAN opérationnelle !**")
                else:
                    if not ok_enc: st.error("❌ Encapsulation : `encapsulation dot1Q 10`")
                    if not ok_ip: st.error("❌ Adresse IP : `ip address 192.168.10.254 255.255.255.0`")

        elif "4. Sécurité des Ports" in cisco_scenario:
            st.info("📋 **Objectif** : Sur le port `FastEthernet0/1`, activez la sécurité de port, fixez la limite à **2 adresses MAC**, et définissez la violation sur `protect`.")
            st.markdown("<div class='terminal-header'>Switch-BTS-CIEL(config-if)#</div>", unsafe_allow_html=True)
            c4_sec = st.text_input("1. Activer le Port Security :", placeholder="ex: switchport port-security", key="c4_sec")
            c4_max = st.text_input("2. Limiter à 2 adresses MAC :", placeholder="ex: switchport port-security maximum...", key="c4_max")
            c4_vio = st.text_input("3. Fixer la violation en mode protect :", placeholder="ex: switchport port-security violation...", key="c4_vio")
            if st.button("Valider le Port Security", type="primary", key="btn_c4"):
                ok1 = c4_sec.strip().lower() == "switchport port-security"
                ok2 = c4_max.strip().lower() == "switchport port-security maximum 2"
                ok3 = c4_vio.strip().lower() == "switchport port-security violation protect"
                if ok1 and ok2 and ok3:
                    st.success("🏆 **Port Security configuré selon les exigences ANSSI !**")
                else:
                    if not ok1: st.error("❌ Étape 1 : `switchport port-security`")
                    if not ok2: st.error("❌ Étape 2 : `switchport port-security maximum 2`")
                    if not ok3: st.error("❌ Étape 3 : `switchport port-security violation protect`")

        elif "5. Routage Statique" in cisco_scenario:
            st.info("📋 **Objectif** : Sur le routeur de bordure, ajoutez une route statique par défaut IPv4 routant tout le trafic inconnu vers la passerelle `10.0.0.1`.")
            st.markdown("<div class='terminal-header'>Router-CIEL(config)#</div>", unsafe_allow_html=True)
            c5_rt = st.text_input("Saisissez la commande de route statique :", placeholder="ex: ip route...", key="c5_rt")
            if st.button("Valider la Route Statique", type="primary", key="btn_c5"):
                if c5_rt.strip().lower() == "ip route 0.0.0.0 0.0.0.0 10.0.0.1":
                    st.success("✅ **Route statique par défaut injectée dans la table de routage !**")
                else:
                    st.error("❌ Commande incorrecte.")
                    st.info("💡 **Commande attendue** : `ip route 0.0.0.0 0.0.0.0 10.0.0.1`")

    # ------------------ TAB 2 : LINUX BASH ------------------
    with t_linux:
        st.subheader("🖥️ Console Linux Bash & Administration Système")
        linux_scenario = st.selectbox(
            "Choisissez un scénario de commandes Linux :",
            [
                "1. Permissions Octales (chmod)",
                "2. Droits Spéciaux (SUID, SGID, Sticky Bit)",
                "3. Listes de Contrôle d'Accès POSIX (ACLs)",
                "4. Création & Gestion d'Utilisateurs (useradd / usermod)",
                "5. Gestion des Services (systemd) & Filtrage de Logs (grep)"
            ],
            key="linux_scen_select"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if "1. Permissions Octales" in linux_scenario:
            st.info("📋 **Objectif** : Sécurisez le script `/opt/deploy.sh` : Propriétaire = `rwx` (7), Groupe = `r-x` (5), Autres = Aucun droit (0).")
            st.markdown("<div class='terminal-header'>root@debian-srv:~#</div>", unsafe_allow_html=True)
            l1_in = st.text_input("Saisissez la commande chmod :", placeholder="ex: chmod...", key="l1_in")
            if st.button("Appliquer les permissions", type="primary", key="btn_l1"):
                if l1_in.strip() in ["chmod 750 /opt/deploy.sh", "chmod 750 deploy.sh"]:
                    st.success("✅ **Permissions appliquées ! Masque octal : 750 (rwxr-x---).**")
                else:
                    st.error("❌ Masque octal incorrect.")
                    st.info("💡 **Commande attendue** : `chmod 750 /opt/deploy.sh`")

        elif "2. Droits Spéciaux" in linux_scenario:
            st.info("📋 **Objectif** : Appliquez le droit spécial **SUID** (4000) avec les permissions 755 sur l'exécutable `/usr/bin/custom_pass`.")
            st.markdown("<div class='terminal-header'>root@debian-srv:~#</div>", unsafe_allow_html=True)
            l2_in = st.text_input("Saisissez la commande chmod avec SUID :", placeholder="ex: chmod 4...", key="l2_in")
            if st.button("Appliquer le SUID", type="primary", key="btn_l2"):
                if l2_in.strip() in ["chmod 4755 /usr/bin/custom_pass", "chmod u+s /usr/bin/custom_pass"]:
                    st.success("🎉 **Bit SUID configuré !** L'exécutable fonctionnera avec les privilèges de root.")
                else:
                    st.error("❌ Commande incorrecte.")
                    st.info("💡 **Commande attendue** : `chmod 4755 /usr/bin/custom_pass`")

        elif "3. Listes de Contrôle" in linux_scenario:
            st.info("📋 **Objectif** : Accordez les droits complets `rwx` à l'utilisateur `alice` sur le dossier `/data/projets` via les ACLs POSIX.")
            st.markdown("<div class='terminal-header'>root@debian-srv:~#</div>", unsafe_allow_html=True)
            l3_in = st.text_input("Saisissez la commande setfacl :", placeholder="ex: setfacl -m...", key="l3_in")
            if st.button("Appliquer l'ACL", type="primary", key="btn_l3"):
                if "u:alice:rwx" in l3_in.strip() and "/data/projets" in l3_in.strip():
                    st.success("✅ **ACL ajoutée avec succès !** `setfacl -m u:alice:rwx /data/projets`")
                else:
                    st.error("❌ Syntaxe ACL incorrecte.")
                    st.info("💡 **Commande attendue** : `setfacl -m u:alice:rwx /data/projets`")

        elif "4. Création & Gestion" in linux_scenario:
            st.info("📋 **Objectif** : Créez l'utilisateur `bob` avec son répertoire personnel (`-m`), son shell `/bin/bash` (`-s`), puis ajoutez-le au groupe `sudo` (`usermod`).")
            st.markdown("<div class='terminal-header'>root@debian-srv:~#</div>", unsafe_allow_html=True)
            l4_u = st.text_input("1. Commande de création de l'utilisateur bob :", placeholder="ex: useradd...", key="l4_u")
            l4_g = st.text_input("2. Commande d'ajout de bob au groupe sudo :", placeholder="ex: usermod...", key="l4_g")
            if st.button("Valider la gestion utilisateur", type="primary", key="btn_l4"):
                ok_u = "useradd" in l4_u and "-m" in l4_u and "/bin/bash" in l4_u and "bob" in l4_u
                ok_g = l4_g.strip() in ["usermod -aG sudo bob", "usermod -a -G sudo bob", "adduser bob sudo"]
                if ok_u and ok_g:
                    st.success("🎉 **Utilisateur bob créé et promu administrateur sudo !**")
                else:
                    if not ok_u: st.error("❌ Création : `useradd -m -s /bin/bash bob`")
                    if not ok_g: st.error("❌ Ajout au groupe : `usermod -aG sudo bob`")

        elif "5. Gestion des Services" in linux_scenario:
            st.info("📋 **Objectif** : Redémarrez le service `apache2`, activez son démarrage automatique au boot (`systemctl`), puis cherchez les lignes contenant le terme `FAILED` dans `/var/log/auth.log` (`grep`).")
            st.markdown("<div class='terminal-header'>root@debian-srv:~#</div>", unsafe_allow_html=True)
            l5_s = st.text_input("1. Redémarrer et activer le service apache2 :", placeholder="ex: systemctl restart...", key="l5_s")
            l5_g = st.text_input("2. Recherche grep dans le journal auth.log :", placeholder="ex: grep...", key="l5_g")
            if st.button("Exécuter la séquence SysAdmin", type="primary", key="btn_l5"):
                ok_s = "systemctl restart apache2" in l5_s or "systemctl reload apache2" in l5_s
                ok_g = "grep" in l5_g.lower() and "failed" in l5_g.lower() and "auth.log" in l5_g
                if ok_s and ok_g:
                    st.success("🏆 **Séquence d'administration système exécutée sans erreur !**")
                else:
                    if not ok_s: st.error("❌ Service : `systemctl restart apache2`")
                    if not ok_g: st.error("❌ Grep : `grep -i 'failed' /var/log/auth.log`")

    # ------------------ TAB 3 : C++ DEBUGGER ------------------
    with t_cpp:
        st.subheader("💻 Debugger & Analyseur Mémoire C++ / C")
        cpp_scenario = st.selectbox(
            "Choisissez un scénario de débuggage C++ :",
            [
                "1. Libération de Tableau Dynamique (new[] / delete[])",
                "2. Classe Abstraite & Méthode Virtuelle Pure",
                "3. Pointeur Intelligent (std::unique_ptr)",
                "4. Union C & Masquage de Bits",
                "5. Exclusion Mutuelle (std::mutex & std::lock_guard)"
            ],
            key="cpp_scen_select"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if "1. Libération de Tableau" in cpp_scenario:
            st.info("📋 **Code défectueux** : Identifiez et corrigez la ligne de suppression provoquant une fuite de mémoire.")
            st.code(r"""
int* mesures = new int[1024];
// ... traitement des mesures ...
delete mesures; // <-- ERREUR ! Fuite mémoire sur le tableau !
            r""", language="cpp")
            c1_code = st.text_input("Saisissez la ligne C++ corrigée :", placeholder="ex: delete[]...", key="c1_code")
            if st.button("Corriger la fuite mémoire", type="primary", key="btn_c1_cpp"):
                if c1_code.strip().replace(" ", "") in ["delete[]mesures;", "delete[]mesures"]:
                    st.success("🎉 **Fuite mémoire colmatée !** L'opérateur `delete[]` détruit bien l'ensemble des 1024 éléments du tableau.")
                else:
                    st.error("❌ Erreur de syntaxe. N'oubliez pas les crochets `[]`.")
                    st.info("💡 **Correction** : `delete[] mesures;`")

        elif "2. Classe Abstraite" in cpp_scenario:
            st.info("📋 **Objectif** : Dans la classe de base `Capteur`, déclarez la méthode virtuelle pure `lireTension()` renvoyant un `double` afin de rendre la classe abstraite.")
            st.code(r"""
class Capteur {
public:
    // Complétez la déclaration de la méthode virtuelle pure ci-dessous :
};
            r""", language="cpp")
            c2_code = st.text_input("Saisissez la déclaration virtuelle pure :", placeholder="ex: virtual double...", key="c2_code")
            if st.button("Valider la méthode virtuelle pure", type="primary", key="btn_c2_cpp"):
                clean2 = c2_code.strip().replace(" ", "")
                if "virtual" in c2_code and "double" in c2_code and "lireTension()" in c2_code and "=0" in clean2:
                    st.success("✅ **Classe abstraite valide !** Toutes les classes filles devront réimplémenter `lireTension()`.")
                else:
                    st.error("❌ Syntaxe virtuelle pure incorrecte.")
                    st.info("💡 **Déclaration attendue** : `virtual double lireTension() = 0;`")

        elif "3. Pointeur Intelligent" in cpp_scenario:
            st.info("📋 **Objectif** : Remplacez la gestion par pointeur brut `Capteur* c = new CapteurTemp();` par un pointeur intelligent C++11 `std::unique_ptr`.")
            c3_code = st.text_input("Saisissez la ligne d'instanciation C++11 :", placeholder="ex: std::unique_ptr<Capteur>...", key="c3_code")
            if st.button("Valider le Smart Pointer", type="primary", key="btn_c3_cpp"):
                if "unique_ptr" in c3_code and "make_unique" in c3_code:
                    st.success("🏆 **Code C++ moderne et totalement sécurisé contre les fuites mémoire !**")
                else:
                    st.error("❌ Utilisez `std::unique_ptr<Capteur> c = std::make_unique<CapteurTemp>();`")

        elif "4. Union C & Masquage" in cpp_scenario:
            st.info("📋 **Objectif** : Écrivez l'expression logique d'ET bit-à-bit pour vérifier si le 3ème bit (poids 4, `0x04`) de la variable `uint8_t status` est actif.")
            c4_code = st.text_input("Saisissez l'expression de masquage de bit :", placeholder="ex: status & ...", key="c4_code")
            if st.button("Valider le masquage de bit", type="primary", key="btn_c4_cpp"):
                clean4 = c4_code.strip().replace(" ", "")
                if clean4 in ["status&0x04", "status&(1<<2)", "(status&0x04)", "status&4"]:
                    st.success("✅ **Masquage parfait !** `status & 0x04` isole exactement le bit recherché.")
                else:
                    st.error("❌ Expression incorrecte. Utilisez l'opérateur ET bit-à-bit `& 0x04`.")

        elif "5. Exclusion Mutuelle" in cpp_scenario:
            st.info("📋 **Objectif** : Dans une fonction exécutée par plusieurs threads, sécurisez l'accès à une ressource partagée avec `std::lock_guard` et le mutex `mtx`.")
            c5_code = st.text_input("Saisissez la ligne d'instanciation du verrou RAII :", placeholder="ex: std::lock_guard...", key="c5_code")
            if st.button("Valider l'exclusion mutuelle", type="primary", key="btn_c5_cpp"):
                if "lock_guard" in c5_code and "mutex" in c5_code and "mtx" in c5_code:
                    st.success("🎉 **Section critique protégée contre les Race Conditions !**")
                else:
                    st.error("❌ Utilisation : `std::lock_guard<std::mutex> lock(mtx);`")

    # ------------------ TAB 4 : ACTIVE DIRECTORY & POWERSHELL ------------------
    with t_ad:
        st.subheader("🔒 Active Directory & PowerShell Windows Server (Épreuve E5)")
        st.info("📋 **Scénarios d'Administration PowerShell Active Directory**")
        
        ad_scen = st.radio(
            "Sélectionnez le cas pratique PowerShell :",
            [
                "A. Création d'un compte utilisateur AD (New-ADUser)",
                "B. Liaison d'une Stratégie de Groupe GPO (New-GPLink)",
                "C. Test de connectivité port LDAPS 636 (Test-NetConnection)"
            ],
            key="ad_scen_radio"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if "A. Création" in ad_scen:
            st.markdown("**Énoncé** : Créez l'utilisateur `John Doe` (identifiant `jdoe`) dans l'OU `OU=Ingenieurs,DC=ciel,DC=local`.")
            st.markdown(r"<div class='terminal-header'>PS C:\Users\Administrator></div>", unsafe_allow_html=True)
            ad1_in = st.text_input("Commande PowerShell New-ADUser :", placeholder="ex: New-ADUser -Name...", key="ad1_in")
            if st.button("Exécuter le script PowerShell (User)", type="primary", key="btn_ad1"):
                if "New-ADUser" in ad1_in and "jdoe" in ad1_in and "OU=Ingenieurs" in ad1_in:
                    st.success("🎉 **Compte utilisateur Active Directory créé dans l'OU ciblée !**")
                else:
                    if not ("New-ADUser" in ad1_in): st.error("❌ Utiliser l'applet de commande `New-ADUser`")
                    if not ("jdoe" in ad1_in): st.error("❌ Indiquer le SamAccountName `jdoe`")

        elif "B. Liaison" in ad_scen:
            st.markdown("**Énoncé** : Liez la GPO nommée `GPO_Securite_Mdp` à l'Unité d'Organisation `OU=Ingenieurs,DC=ciel,DC=local`.")
            st.markdown(r"<div class='terminal-header'>PS C:\Users\Administrator></div>", unsafe_allow_html=True)
            ad2_in = st.text_input("Commande PowerShell New-GPLink :", placeholder="ex: New-GPLink -Name...", key="ad2_in")
            if st.button("Lier la GPO dans Active Directory", type="primary", key="btn_ad2"):
                if "New-GPLink" in ad2_in and "GPO_Securite_Mdp" in ad2_in and "OU=Ingenieurs" in ad2_in:
                    st.success("✅ **GPO liée avec succès à l'OU !** L'ordre de priorité LSDOU s'applique.")
                else:
                    st.error("❌ Syntaxe New-GPLink incorrecte.")

        elif "C. Test" in ad_scen:
            st.markdown("**Énoncé** : Testez si le port sécurisé **LDAPS (636)** est bien ouvert sur le contrôleur de domaine `dc1.ciel.local` via `Test-NetConnection`.")
            st.markdown(r"<div class='terminal-header'>PS C:\Users\Administrator></div>", unsafe_allow_html=True)
            ad3_in = st.text_input("Commande Test-NetConnection :", placeholder="ex: Test-NetConnection...", key="ad3_in")
            if st.button("Tester le port LDAPS 636", type="primary", key="btn_ad3"):
                if "Test-NetConnection" in ad3_in and "dc1.ciel.local" in ad3_in and "636" in ad3_in:
                    st.success("🏆 **Connexion LDAPS établie avec succès ! Port 636 Ouvert.**")
                else:
                    st.error("❌ Commande incorrecte. Exemple : `Test-NetConnection -ComputerName dc1.ciel.local -Port 636`")

    # ------------------ TAB 5 : IOT & BUS INDUSTRIELS ------------------
    with t_iot:
        st.subheader("🔌 Console IoT & Bus Industriels (Modbus RTU, MQTT & Sockets)")
        st.info("📋 **Scénarios de Communication Réseau & Industrielle**")
        
        iot_scen = st.radio(
            "Sélectionnez le protocole à tester :",
            [
                "1. Modbus RTU : Lecture de Holding Registers (PyModbus)",
                "2. Mosquitto MQTT : Souscription à un Topic en Ligne de Commande",
                "3. Socket TCP Python : Connexion Client à une Passerelle"
            ],
            key="iot_scen_radio"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if "1. Modbus" in iot_scen:
            st.markdown("**Énoncé** : Appelez la méthode de lecture de **4 registres de mots** (*Holding Registers*) à partir de l'adresse `0` sur l'esclave Modbus `slave=1`.")
            iot1_in = st.text_input("Méthode PyModbus :", placeholder="ex: client.read_holding_registers...", key="iot1_in")
            if st.button("Exécuter la requête Modbus RTU", type="primary", key="btn_iot1"):
                if "read_holding_registers" in iot1_in and "0" in iot1_in and ("slave=1" in iot1_in or "unit=1" in iot1_in or "1" in iot1_in):
                    st.success("🎉 **Trame Modbus RTU envoyée ! Code Fonction 03 (Read Holding Registers).**")
                else:
                    st.error("❌ Méthode Modbus incorrecte. Attendu : `client.read_holding_registers(address=0, count=4, slave=1)`")

        elif "2. Mosquitto" in iot_scen:
            st.markdown("**Énoncé** : Souscrivez au topic `ciel/usine/temperature` sur le broker MQTT `192.168.1.100` avec l'outil CLI `mosquitto_sub`.")
            st.markdown(r"<div class='terminal-header'>user@debian-iot:~$</div>", unsafe_allow_html=True)
            iot2_in = st.text_input("Commande mosquitto_sub :", placeholder="ex: mosquitto_sub -h...", key="iot2_in")
            if st.button("Lancer la souscription MQTT", type="primary", key="btn_iot2"):
                if "mosquitto_sub" in iot2_in and "192.168.1.100" in iot2_in and "ciel/usine/temperature" in iot2_in:
                    st.success("✅ **Souscription active ! Réception des messages de télémétrie en temps réel.**")
                else:
                    st.error("❌ Commande mosquitto_sub incorrecte. Attendu : `mosquitto_sub -h 192.168.1.100 -t ciel/usine/temperature`")

        elif "3. Socket" in iot_scen:
            st.markdown("**Énoncé** : En Python, établissez la connexion du socket `s` vers le serveur `192.168.10.254` sur le port `8080`.")
            st.code(r"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Saisissez la ligne de connexion ci-dessous :
            r""", language="python")
            iot3_in = st.text_input("Méthode de connexion du socket :", placeholder="ex: s.connect...", key="iot3_in")
            if st.button("Connecter le Socket TCP", type="primary", key="btn_iot3"):
                if "s.connect" in iot3_in and "192.168.10.254" in iot3_in and "8080" in iot3_in:
                    st.success("🏆 **Connexion TCP établie avec la passerelle !**")
                else:
                    st.error(r"❌ Syntaxe incorrecte. N'oubliez pas le tuple d'arguments `(\"192.168.10.254\", 8080)`.")


# --- 10. PAGE GRAND QUIZ D'EXAMEN ---
elif page == "📝 Grand Quiz d'Examen":
    st.markdown("<div class='hero-title'>📝 Simulateur de Questionnaires Personnalisés & Marathons</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Configurez votre session de révision : du quiz standard de 10 questions au méga-marathon de 40 questions !</p>", unsafe_allow_html=True)
    
    # Configuration du Quiz
    st.markdown("<div class='ciel-card'>", unsafe_allow_html=True)
    col_cfg1, col_cfg2, col_cfg3 = st.columns([1.5, 1.5, 1])
    with col_cfg1:
        quiz_type = st.selectbox(
            "Format du questionnaire :",
            ["Standard (10 questions)", "Moyen (20 questions)", "Marathon (30 questions)", "Méga-Marathon (40 questions)", "Intégral (Toutes les questions)"]
        )
    with col_cfg2:
        selected_mod_filter = st.selectbox(
            "Filtrer par domaine technique :",
            ["Tous les domaines", "📶 Réseaux & Télécoms", "🔒 Cybersécurité", "💻 Programmation / Dev", "🖥️ Administration Système", "🔌 Électronique & IoT", "📐 Modélisation UML & SysML"]
        )
    with col_cfg3:
        st.markdown("<div style='padding-top:24px;'></div>", unsafe_allow_html=True)
        if st.button("🚀 Générer le Questionnaire", use_container_width=True, type="primary") or "active_quiz" not in st.session_state:
            count_map = {
                "Standard (10 questions)": 10,
                "Moyen (20 questions)": 20,
                "Marathon (30 questions)": 30,
                "Méga-Marathon (40 questions)": 40,
                "Intégral (Toutes les questions)": len(GRAND_QUIZ_DATA)
            }
            limit = count_map.get(quiz_type, 10)
            
            # Filtrer le pool de questions
            pool = GRAND_QUIZ_DATA
            if selected_mod_filter != "Tous les domaines":
                pool = [q for q in GRAND_QUIZ_DATA if q["mod"] == selected_mod_filter]
                
            sample_size = min(limit, len(pool))
            if sample_size > 0:
                st.session_state.active_quiz = random.sample(pool, sample_size)
            else:
                st.session_state.active_quiz = []
            
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
            
    if not st.session_state.get("active_quiz", []):
        st.warning("Aucune question ne correspond à vos critères de filtrage. Veuillez sélectionner un autre domaine ou générer à nouveau.")
    else:
        active_q = st.session_state.active_quiz
        st.info(f"📋 **Questionnaire actif** : {len(active_q)} questions générées (Domaine : *{selected_mod_filter}*). Répondez ci-dessous puis cliquez sur 'Soumettre mon questionnaire'.")
        
        # Affichage des questions
        scores = {}
        for idx, q_item in enumerate(active_q):
            st.markdown(f"### Q{idx+1} : {q_item['q']}")
            st.markdown(f"**Domaine :** `{q_item['mod']}` | **Chapitre :** *{q_item['chap']}*")
            
            key_ans = f"active_q_ans_{idx}"
            user_sel = st.radio(
                "Sélectionnez votre réponse :",
                q_item["options"],
                key=key_ans,
                disabled=st.session_state.quiz_submitted
            )
            scores[idx] = (user_sel, q_item["rep"], q_item["expl"], q_item["mod"], q_item["chap"])
            st.markdown("<hr style='border: 1px dashed #e2e8f0; margin: 15px 0;'/>", unsafe_allow_html=True)
            
        # Bouton de soumission
        if not st.session_state.quiz_submitted:
            if st.button("📥 Soumettre mon questionnaire", use_container_width=True, type="primary"):
                st.session_state.quiz_submitted = True
                st.rerun()
                
        if st.session_state.quiz_submitted:
            total_correct = 0
            wrong_answers = []
            details_stats = {"Réseaux": 0, "Cybersécurité": 0, "Prog": 0, "SysAdmin": 0, "Elec": 0, "UML": 0}
            
            for idx, (user_sel, rep, expl, m_ref, c_ref) in scores.items():
                k_mod = "Réseaux"
                if "Cyber" in m_ref: k_mod = "Cybersécurité"
                elif "Prog" in m_ref: k_mod = "Prog"
                elif "SysAdmin" in m_ref: k_mod = "SysAdmin"
                elif "Élec" in m_ref: k_mod = "Elec"
                elif "Modélisation" in m_ref: k_mod = "UML"
                
                if user_sel == rep:
                    total_correct += 1
                    details_stats[k_mod] += 1
                else:
                    wrong_answers.append({
                        "num": idx + 1,
                        "mod": m_ref,
                        "chap": c_ref,
                        "user_sel": user_sel,
                        "rep": rep,
                        "expl": expl
                    })
                    
            # Enregistrement dans l'historique
            save_score(total_correct, len(active_q), details_stats)
            
            # Affichage du score final
            st.markdown("## 📊 Votre Bilan du Questionnaire")
            pct = total_correct / len(active_q)
            st.progress(pct)
            
            st.markdown(f"<div style='font-size: 1.5rem; font-weight: 700; color: #1e3a8a;'>Votre score final : {total_correct} / {len(active_q)} ({pct*100:.1f}%)</div>", unsafe_allow_html=True)
            
            if pct >= 0.8:
                st.success("🏆 **Niveau d'Excellence atteint !** Vos connaissances techniques sont extrêmement solides. Prêt pour l'examen final !")
            elif pct >= 0.5:
                st.info("👍 **Bon niveau global !** La plupart des concepts sont acquis. Revoyez vos erreurs pour viser la perfection.")
            else:
                st.warning("⚠️ **Niveau fragile.** Prenez le temps de bien relire vos fiches de cours ci-dessous pour combler vos lacunes.")
                
            if wrong_answers:
                st.markdown("---")
                st.markdown("### 🔄 Pont de Correction Automatique")
                st.write("Le système a identifié des erreurs. Voici les explications et les fiches de cours correspondantes pour vous corriger :")
                for w in wrong_answers:
                    st.error(f"**Question {w['num']} ({w['mod']} - {w['chap']})**")
                    st.write(f"Votre choix : *{w['user_sel']}* | Bonne réponse : **{w['rep']}**")
                    st.info(f"💡 *Explication de l'expert : {w['expl']}*")
                    try:
                        c_txt = COURS_BASE[w['mod']][w['chap']]
                        with st.expander(f"📖 Relire la fiche de cours : {w['chap']}", expanded=True):
                            st.markdown(c_txt)
                    except:
                        pass
                        
            if st.button("🔄 Lancer un nouveau Questionnaire", use_container_width=True):
                st.session_state.quiz_submitted = False
                st.session_state.active_quiz = []
                st.rerun()

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



elif page == "📄 Datasheets & Fiches Techniques (Composants)":
    st.markdown("<div class='hero-title'>📄 Datasheets & Fiches Techniques de Composants (en Anglais)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Guide d'analyse et de décodage des fiches constructeurs pour l'épreuve écrite E4 et les travaux pratiques E5/E6</p>", unsafe_allow_html=True)

    tab_ds1, tab_ds2, tab_ds3, tab_ds4, tab_ds5 = st.tabs([
        "⚙️ Microcontrôleurs 8/32 bits",
        "🔌 Bus & Transceivers (MCP2515/MAX485)",
        "⚡ Drivers Moteurs & Puissance",
        "🌡️ Capteurs Industriels (4-20mA/MAX6675)",
        "✍️ Quiz Datasheets & Anglais Technique"
    ])

    with tab_ds1:
        st.subheader("1. Microcontrôleurs 8 bits & 32 bits (ATmega328P, ESP32, STM32)")
        st.markdown(r"""
        #### 🔹 ATmega328P (Microchip / Atmel 8-bit AVR)
        * **Features** : High Performance 8-bit AVR RISC Architecture, 32 KB Flash, 2 KB SRAM, 1 KB EEPROM, 16 MHz Clock Speed.
        * **Key Registers for Timers & PWM** :
          - `TCCR1A` / `TCCR1B` (*Timer/Counter1 Control Register*) : Configures Waveform Generation Mode (Fast PWM, Phase Correct) and Clock Prescaler ($1, 8, 64, 256, 1024$).
          - `OCR1A` / `OCR1B` (*Output Compare Register*) : Holds the 16-bit value compared with the counter value to adjust the PWM duty cycle.
        * **USART Control Registers** :
          - `UBRR0H` / `UBRR0L` (*USART Baud Rate Register*) :
            $$\text{UBRR0} = \frac{F_{\text{OSC}}}{16 \times \text{Baud}} - 1$$
            *Example for 9600 Baud @ 16 MHz* : $\text{UBRR0} = \frac{16000000}{16 \times 9600} - 1 = 103,16 \Rightarrow \mathbf{103} \quad (0x0067)$.

        #### 🔹 ESP32 (Espressif Systems 32-bit Dual-Core Xtensa LX6)
        * **Features** : Tensilica LX6 @ 240 MHz, 520 KB SRAM, Integrated 2.4 GHz Wi-Fi 802.11 b/g/n & Bluetooth 4.2 / BLE.
        * **Low Power Modes** : Active Mode, Modem-sleep, Light-sleep, **Deep-sleep** (RTC Memory active, current consumption down to $10~\mu\text{A}$).
        * **Peripherals** : 12-bit SAR ADC (up to 18 channels), Capacitive Touch, DAC, I2C, SPI, UART, PWM (LEDC controller).

        #### 🔹 STM32F4 (STMicroelectronics ARM Cortex-M4 32-bit)
        * **Core** : 32-bit ARM Cortex-M4 with FPU (Floating Point Unit) @ 84 MHz / 180 MHz, DSP instructions.
        * **HAL Architecture** : Hardware Abstraction Layer (`HAL_GPIO_WritePin()`, `HAL_UART_Transmit()`, `HAL_ADC_Start()`).
        """)

        st.info("💡 **Conseil Examen E4** : Quand un extrait de datasheet en anglais est fourni dans le sujet, repérez immédiatement le tableau **'Absolute Maximum Ratings'** (tensions/courants limites) et le chapitre **'Register Description'** pour identifier le rôle de chaque bit.")

    with tab_ds2:
        st.subheader("2. Contrôleurs de Bus & Transceivers (MCP2515, MAX485, SN75176)")
        st.markdown(r"""
        #### 🔹 MCP2515 (Microchip Standalone CAN Controller with SPI)
        * **Role** : Implements CAN Specification V2.0B at up to 1 Mb/s over an SPI interface.
        * **SPI Commands** :
          - `RESET` (`0xC0`) : Resets internal registers to default state.
          - `READ` (`0x03`) : Reads data from the register at selected address.
          - `WRITE` (`0x02`) : Writes data to selected register.
          - `BIT MODIFY` (`0x05`) : Modifies specific bits in control registers (`CANCTRL`, `BFPCTRL`).
        * **Acceptance Filters & Masks** :
          - `RXF0` to `RXF5` (*Filter Registers*) : Define the exact 11-bit or 29-bit CAN IDs accepted by the node.
          - `RXM0`, `RXM1` (*Mask Registers*) : Bits set to `1` mean "check filter bit", bits set to `0` mean "don't care".

        #### 🔹 MAX485 / SN75176 (RS-485 Transceiver)
        * **Features** : Low-power transceiver for RS-485 and RS-422 communication, Half-Duplex, differential transmission lines `A` and `B`.
        * **Control Pins** :
          - `RO` (*Receiver Output*) : Connected to MCU Rx.
          - `RE` (*Receiver Enable*) : Active Low ($\overline{\text{RE}}$). Set `0` to enable receiver.
          - `DE` (*Driver Enable*) : Active High. Set `1` to enable transmitter.
          - `DI` (*Driver Input*) : Connected to MCU Tx.
        * **Common Wiring Tip** : Connect `RE` and `DE` together to a single MCU GPIO pin (`DIR`). Set `DIR = 1` for Transmission (Tx) and `DIR = 0` for Reception (Rx).
        """)

    with tab_ds3:
        st.subheader("3. Drivers de Moteurs & Electronique de Puissance (BTS7960, L298N)")
        st.markdown(r"""
        #### 🔹 BTS7960 (Infineon High Current PN Half Bridge - 43A)
        * **Application** : High power DC motor drive up to 43A continuous under 6V to 28V.
        * **Pin Functionality** :
          - `R_IS` / `L_IS` (*Current Sense Output*) : Provides a current proportional to motor load for overload detection.
          - `R_EN` / `L_EN` (*Enable Inputs*) : Logic High enables right/left half bridge.
          - `RPWM` / `LPWM` (*PWM Control Inputs*) : Speed control input up to 25 kHz.
        * **Protection Features** : Over-temperature shutdown, Short-circuit protection, Under-voltage lockout.

        #### 🔹 L298N (STMicroelectronics Dual Full-Bridge Driver)
        * **Features** : Integrated dual H-bridge driver up to 46V and 2A per channel.
        * **Flyback Diodes Requirement** : Inductive loads (motors, relays) require 8 external fast-recovery freewheeling diodes to absorb back-EMF spikes ($e = -L \frac{di}{dt}$).
        """)

    with tab_ds4:
        st.subheader("4. Capteurs Industriels (DHT22, BME280, MAX6675, Boucles 4-20mA)")
        st.markdown(r"""
        #### 🔹 MAX6675 (Thermocouple K-Type to Digital Converter)
        * **Interface** : SPI Read-Only (3-wire: `SO`, `CS`, `SCK`).
        * **Resolution** : 12-bit ADC with 0.25°C resolution over 0°C to +1024°C range.
        * **Open Thermocouple Detection** : Bit D2 goes HIGH when the thermocouple wire is broken.

        #### 🔹 Boucle de Courant Industrielle 4-20 mA
        * **Datasheet Specification** : Output current $I_{\text{out}}$ varies linearly from $4\text{ mA}$ (minimum scale) to $20\text{ mA}$ (maximum scale).
        * **Conversion Formula** :
          $$I = 4 + \frac{T - T_{\text{min}}}{T_{\text{max}} - T_{\text{min}}} \times 16 \quad [\text{mA}]$$
        """)

    with tab_ds5:
        st.subheader("✍️ Quiz Datasheets & Anglais Technique Composants")
        q1 = st.radio("1. What is the value of UBRR0 for 9600 Baud under a 16 MHz clock on an ATmega328P?", ["103", "207", "51", "128"], key="ds_q1")
        q2 = st.radio("2. On a MAX485 transceiver, what pin state enables Transmit mode?", ["DE = 1, RE = 1", "DE = 0, RE = 0", "DE = 1, RE = 0", "DE = 0, RE = 1"], key="ds_q2")
        if st.button("Check Datasheets Quiz", type="primary", key="btn_ds_quiz"):
            score = 0
            if q1 == "103": score += 1
            if q2 == "DE = 1, RE = 1" or q2 == "DE = 1, RE = 0": score += 1
            st.success(f"Score : **{score} / 2**")



elif page == "🔍 Captures de Trames & Analyses Wireshark PCAP":
    st.markdown("<div class='hero-title'>🔍 Captures de Trames & Analyses Wireshark PCAP Commentées</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Décryptage pas-à-pas de paquets réseaux réels, captures de trames industrielles et simulateur d'analyse d'examen</p>", unsafe_allow_html=True)

    tab_pc1, tab_pc2, tab_pc3, tab_pc4, tab_pc5 = st.tabs([
        "🌐 TCP/IP & Handshake 3-Way",
        "⚙️ Services Réseaux (DHCP & DNS)",
        "🏭 Bus Industriels (Modbus & CAN)",
        "🔒 Sessions TLS 1.3 & SSH",
        "✍️ Simulateur d'Analyse Hex"
    ])

    with tab_pc1:
        st.subheader("1. Établissement de Connexion TCP (Handshake 3-Way) & Fermeture")
        st.markdown(r"""
        #### 🔹 Trame #1 : Client $\rightarrow$ Serveur (SYN)
        ```text
        Frame 1: 66 bytes on wire
        Ethernet II, Src: 00:0c:29:1f:8a:12, Dst: 00:50:56:a1:02:bb
        Internet Protocol Version 4, Src: 192.168.10.15, Dst: 192.168.10.254
        Transmission Control Protocol, Src Port: 49152, Dst Port: 80, Seq: 0, Flags: 0x002 (SYN)
            Source Port: 49152
            Destination Port: 80
            Sequence Number: 0 (relative sequence number)
            Header Length: 32 bytes
            Flags: 0x002 (SYN)
            Window: 64240
            MSS: 1460 bytes
        ```
        * **Analyse** : Le client (`192.168.10.15`) envoie un paquet TCP avec le bit **SYN** activé (`Flags: 0x002`) sur le port HTTP 80 du serveur (`192.168.10.254`). Son numéro de séquence initial relatif est `Seq = 0`. Le MSS (*Maximum Segment Size*) négocié est de `1460 octets`.

        #### 🔹 Trame #2 : Serveur $\rightarrow$ Client (SYN-ACK)
        ```text
        Frame 2: 66 bytes on wire
        Transmission Control Protocol, Src Port: 80, Dst Port: 49152, Seq: 0, Ack: 1, Flags: 0x012 (SYN, ACK)
            Sequence Number: 0
            Acknowledgment Number: 1 (relative ack)
            Flags: 0x012 (SYN, ACK)
        ```
        * **Analyse** : Le serveur répond avec les bits **SYN** et **ACK** (`Flags: 0x012`). Il valide le paquet SYN reçu en renvoyant `Ack = 1` ($0 + 1$).

        #### 🔹 Trame #3 : Client $\rightarrow$ Serveur (ACK)
        ```text
        Frame 3: 54 bytes on wire
        Transmission Control Protocol, Src Port: 49152, Dst Port: 80, Seq: 1, Ack: 1, Flags: 0x010 (ACK)
        ```
        * **Analyse** : La connexion TCP est **ESTABLISHED**. Les données applicatives HTTP peuvent maintenant transiter.
        """)

    with tab_pc2:
        st.subheader("2. Services Infrastructure : DHCP DORA & DNS")
        st.markdown(r"""
        #### 🔹 Processus DHCP DORA (Dynamic Host Configuration Protocol)
        ```text
        1. DHCP Discover : Src IP 0.0.0.0 -> Dst IP 255.255.255.255 (UDP 67->68) [Option 53 = 1]
        2. DHCP Offer    : Src IP 192.168.1.254 -> Dst IP 192.168.1.50 (UDP 68->67) [Option 53 = 2, Offered IP = 192.168.1.50]
        3. DHCP Request  : Src IP 0.0.0.0 -> Dst IP 255.255.255.255 (UDP 67->68) [Option 53 = 3, Requested IP = 192.168.1.50]
        4. DHCP ACK      : Src IP 192.168.1.254 -> Dst IP 192.168.1.50 (UDP 68->67) [Option 53 = 5, Lease Time = 86400s]
        ```
        * **Options DHCP Clés à Connaître pour E5/E4** :
          - **Option 53** : DHCP Message Type (1=Discover, 2=Offer, 3=Request, 5=ACK, 6=NAK).
          - **Option 1** : Subnet Mask (ex: `255.255.255.0`).
          - **Option 3** : Router / Default Gateway (ex: `192.168.1.254`).
          - **Option 6** : DNS Servers (ex: `192.168.1.10`).
          - **Option 15** : Domain Name (ex: `ciel.local`).

        #### 🔹 Requête DNS (Domain Name System)
        ```text
        Domain Name System (query)
            Transaction ID: 0x2a1b
            Flags: 0x0100 Standard query
            Questions: 1
                srv-web.ciel.local: type A, class IN
        ```
        """)

    with tab_pc3:
        st.subheader("3. Bus Industriels : Modbus RTU sur RS-485 & Trames Bus CAN")
        st.markdown(r"""
        #### 🔹 Trame Modbus RTU (Lecture de Registres - Function Code 03)
        ```text
        Trame Hexadécimale de Requête : [ 01 ] [ 03 ] [ 00 6B ] [ 00 03 ] [ 76 87 ]
        - 01    : Adresse Esclave (Slave ID = 1)
        - 03    : Code Fonction (03 = Read Holding Registers)
        - 00 6B : Adresse du Premier Registre (107 en décimal)
        - 00 03 : Nombre de Registres à Lire (3 registres = 6 octets)
        - 76 87 : Contrôle d'erreur CRC-16 (Cyclic Redundancy Check)

        Trame Hexadécimale de Réponse : [ 01 ] [ 03 ] [ 06 ] [ 02 2B ] [ 00 00 ] [ 01 00 ] [ C5 A1 ]
        - 01    : Adresse Esclave
        - 03    : Code Fonction
        - 06    : Nombre d'Octets de Données Renvoyés (6 octets)
        - 02 2B : Valeur Registre 107 (555 en décimal -> Température 55.5°C)
        - 00 00 : Valeur Registre 108 (0)
        - 01 00 : Valeur Registre 109 (256)
        - C5 A1 : CRC-16 de validation
        ```

        #### 🔹 Trame Bus CAN 2.0A (Standard 11-bit ID)
        ```text
        Controller Area Network (CAN)
            [SOF] Start of Frame : 0 (bit dominant)
            Arbitration Field : Identifier = 0x3A4 (11 bits) [RTR = 0 Data Frame]
            Control Field : DLC = 4 (Data Length Code = 4 octets)
            Data Field : 12 34 56 78
            CRC Field : 15 bits CRC + Delimiter
            ACK Field : Slot (1 bit écrasé par le récepteur)
        ```
        """)

    with tab_pc4:
        st.subheader("4. Tunnels Sécurisés : TLS 1.3 / HTTPS & SSH")
        st.markdown(r"""
        #### 🔹 Handshake TLS 1.3 (Transport Layer Security)
        ```text
        1. Client Hello :
           - Supported Versions : TLS 1.3, TLS 1.2
           - Key Share : Offre de clé publique Diffie-Hellman (ECDHE_RSA)
           - Extension SNI (Server Name Indication) : srv-app.ciel.fr
        2. Server Hello :
           - Version sélectionnée : TLS 1.3
           - Cipher Suite : TLS_AES_256_GCM_SHA384
           - Certificate : Certificat X.509 du serveur transmis
           - Finished : Validation chiffrée
        3. Application Data : Trafic HTTPS 100% chiffré.
        ```
        """)

    with tab_pc5:
        st.subheader("✍️ Simulateur d'Analyse de Trame Hexadécimale")
        st.markdown("**Trame à Analyser** : `00 0c 29 1f 8a 12 00 50 56 a1 02 bb 08 00 45 00`")
        q_p1 = st.radio("Quel est le protocole de Couche 3 indiqué par `EtherType = 0x0800` ?", ["IPv6", "IPv4", "ARP", "VLAN 802.1Q"], key="pcap_q1")
        if st.button("Valider Analyse Hex", type="primary", key="btn_pcap"):
            if q_p1 == "IPv4":
                st.success("🎉 **Exact !** EtherType `0x0800` désigne le protocole IPv4 (`0x0806` pour ARP, `0x86DD` pour IPv6, `0x8100` pour VLAN 802.1Q).")
            else:
                st.error("❌ Incorrect. `0x0800` est l'EtherType d'IPv4.")



elif page == "📁 Modèles de Livrables & PVL Épreuve E6":
    st.markdown("<div class='hero-title'>📁 Modèles de Livrables & PVL (Épreuve E6 - Projet de Fin d'Études)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Gabarits officiels, cahier des charges AFNOR, matrice de traçabilité des exigences, et scripts de tests d'intégration Pytest</p>", unsafe_allow_html=True)

    tab_e6_1, tab_e6_2, tab_e6_3, tab_e6_4, tab_e6_5 = st.tabs([
        "📋 Cahier des Charges AFNOR (CdCf)",
        "📐 Matrice de Traçabilité ReqIF",
        "🧪 Plan de Validation (PVL & Pytest)",
        "📜 Dossier de Recette (FAT/SAT)",
        "✍️ Auto-Évaluation Livrables E6"
    ])

    with tab_e6_1:
        st.subheader("1. Structure Normée du Cahier des Charges Fonctionnel (CdCf - Norme NF X50-151)")
        st.markdown(r"""
        #### 🔹 1. Présentation Générale du Projet
        * **Intitulé du Projet** : Système de Surveillance Industrielle et Passerelle Multi-Protocoles IoT.
        * **Demandeur / Client** : Direction des Systèmes d'Information (DSI).
        * **Objectif Métier** : Remonter en temps réel les mesures de température et de pression d'un parc de machines via le réseau Modbus RTU vers un serveur Cloud sécurisé en MQTTS.

        #### 🔹 2. Analyse Fonctionnelle du Besoin (Diagramme Pieuvre / APTE)
        * **Fonctions Principales (FP)** :
          - **FP1** : Acquérir les données physiques de la chaîne de production via le bus RS-485 Modbus.
          - **FP2** : Transmettre de manière chiffrée (MQTTS / TLS 1.3) les télémesures vers le Broker central.
        * **Fonctions de Contrainte (FC)** :
          - **FC1** : Respecter les contraintes d'alimentation électrique industrielle ($24\text{V DC} \pm 10\%$).
          - **FC2** : Assurer une autonomie minimale sur batterie de secours de $2\text{ heures}$ en cas de coupure secteur.
          - **FC3** : Respecter les réglementations RGPD et la politique de durcissement ANSSI.

        #### 🔹 3. Caractérisation des Exigences Fonctionnelles
        | Identifiant | Libellé de l'Exigence | Critère d'Appréciation | Niveau d'Exigence | Flexibilité |
        | :--- | :--- | :--- | :--- | :--- |
        | **REQ_ACQ_01** | Fréquence de rafraîchissement des mesures | Période d'échantillonnage | $1.0\text{ seconde} \pm 50\text{ ms}$ | **F0 (Inflexible)** |
        | **REQ_SEC_02** | Chiffrement des données en transit | Version du protocole TLS | TLS 1.3 obligatoire | **F0 (Inflexible)** |
        | **REQ_NET_03** | Reprise automatique sur perte de lien Wi-Fi | Temps de reconnexion | $< 5.0\text{ secondes}$ | **F1 (Peu flexible)** |
        """)

    with tab_e6_2:
        st.subheader("2. Matrice de Traçabilité des Exigences (ReqIF / SysML)")
        st.markdown(r"""
        #### 🔹 Traçabilité Exigences $\rightarrow$ Conception $\rightarrow$ Tests de Qualification
        La matrice de traçabilité garantit devant le jury E6 que **100% des exigences** énoncées dans le CdCf sont couvertes par un composant d'architecture et validées par un test d'intégration :

        | Exigence CdCf | Bloc SysML / Classe UML | Fiche de Test PVL | Statut Recette |
        | :--- | :--- | :--- | :--- |
        | **REQ_ACQ_01** | Bloc `CapteurModbus` / Classe `ModbusMaster` | `TEST_ACQ_01.py` | **PASS (100%)** |
        | **REQ_SEC_02** | Bloc `PasserelleMQTTS` / Classe `MqttClientTLS` | `TEST_SEC_02.py` | **PASS (100%)** |
        | **REQ_NET_03** | Bloc `GestionnaireReseau` / Classe `WiFiWatchdog` | `TEST_NET_03.py` | **PASS (100%)** |
        """)

    with tab_e6_3:
        st.subheader("3. Plan de Validation Logicielle (PVL) avec Scripts Automated Pytest")
        st.markdown(r"""
        #### 🔹 Code Python de Test d'Intégration Automated (`test_pvl_passerelle.py`)
        ```python
        import pytest
        import time
        import socket
        import json

        # Test d'intégration de l'exigence REQ_ACQ_01 (Période d'échantillonnage < 1s)
        def test_req_acq_01_sampling_rate():
            start_time = time.time()
            # Simulation d'acquisition de registre Modbus
            data_sample = {"temp_celsius": 24.5, "pressure_bar": 2.1}
            elapsed = time.time() - start_time
            
            assert elapsed < 1.0, f"Erreur REQ_ACQ_01 : temps d'acquisition trop long ({elapsed:.3f}s)"
            assert "temp_celsius" in data_sample
            assert data_sample["temp_celsius"] > -40.0 and data_sample["temp_celsius"] < 125.0

        # Test d'intégration de l'exigence REQ_SEC_02 (Vérification port MQTTS 8883)
        def test_req_sec_02_mqtts_port_open():
            host = "192.168.10.254"
            port = 8883  # Port MQTTS sur TLS
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)
            
            result = sock.connect_ex((host, port))
            sock.close()
            assert result == 0, f"Erreur REQ_SEC_02 : Le port MQTTS {port} est fermé sur {host}"
        ```

        * **Lancement du Test PVL** : `pytest -v test_pvl_passerelle.py`
        """)

    with tab_e6_4:
        st.subheader("4. Dossier de Recette Technique (FAT / SAT & Procès-Verbal)")
        st.markdown(r"""
        #### 🔹 Procès-Verbal (PV) de Recette Finale
        * **Date de Qualification** : 15 Juin 2026
        * **Membres de la Commission** : Chef de Projet DSI, Expert Cybersécurité, Ingénieur Intégrateur.
        * **Décision de Recette** :
          - [x] **Prononcée Sans Réserve** : Le système répond entièrement aux spécifications.
          - [ ] Prononcée Avec Réserves Mineures.
          - [ ] Refusée pour Non-Conformité Majeure.
        """)

    with tab_e6_5:
        st.subheader("✍️ Auto-Évaluation Livrables E6")
        q_e6_1 = st.radio("Quel outil de test Python standard est préconisé pour automatiser le PVL de l'épreuve E6 ?", ["unittest / pytest", "Postman", "Wireshark", "OpenSSL"], key="e6_q1")
        if st.button("Valider Quiz E6", type="primary", key="btn_e6_q"):
            if "pytest" in q_e6_1:
                st.success("🎉 **Exact !** `pytest` permet d'exécuter des assertions automatisées et de générer un rapport de qualification E6.")
            else:
                st.error("❌ Incorrect. `pytest` est le framework de test automatisé recommandé.")



elif page == "🛡️ Guides de Durcissement (Hardening) ANSSI":
    st.markdown("<div class='hero-title'>🛡️ Guides de Durcissement (Hardening) ANSSI & PSSI</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Règles de sécurité fondamentales publiées par l'ANSSI pour le durcissement de Linux Debian, Active Directory et des passerelles IoT</p>", unsafe_allow_html=True)

    tab_an1, tab_an2, tab_an3, tab_an4, tab_an5 = st.tabs([
        "🖥️ Hardening Linux Debian",
        "🏢 Durcissement Active Directory (Tiering)",
        "📶 Sécurisation Wi-Fi & IoT",
        "📜 PSSI & Directives ANSSI",
        "✍️ Quiz Hardening & Sécurité"
    ])

    with tab_an1:
        st.subheader("1. Recommandations de Durcissement Linux Debian (Guide ANSSI - Niveau Intermédiaire)")
        st.markdown(r"""
        #### 🔹 1. Fichier de Configuration de Réseau & Noyau (`/etc/sysctl.d/99-anssi-hardening.conf`)
        ```ini
        # Désactiver le transfert d'IP (si le serveur n'est pas un routeur)
        net.ipv4.ip_forward = 0
        net.ipv6.conf.all.forwarding = 0

        # Désactiver la réponse aux pings Broadcast (protection contre attaques Smurf)
        net.ipv4.icmp_echo_ignore_broadcasts = 1

        # Ignorer les fausses erreurs ICMP
        net.ipv4.icmp_ignore_bogus_error_responses = 1

        # Protection contre les attaques SYN Flood
        net.ipv4.tcp_syncookies = 1

        # Rejeter les redirections ICMP
        net.ipv4.conf.all.accept_redirects = 0
        net.ipv4.conf.default.accept_redirects = 0
        ```
        * Appliquer la configuration sysctl : `sysctl -p /etc/sysctl.d/99-anssi-hardening.conf`

        #### 🔹 2. Durcissement du Daemon SSH (`/etc/ssh/sshd_config.d/anssi.conf`)
        ```text
        # Interdire la connexion directe du compte root
        PermitRootLogin no

        # Interdire l'authentification par mot de passe (clés SSH RSA 4096 / Ed25519 obligatoires)
        PasswordAuthentication no
        PubkeyAuthentication yes

        # Changer le port standard pour limiter le bruit du scan automatisé
        Port 2222

        # Déconnexion automatique des sessions inactives (5 minutes)
        ClientAliveInterval 300
        ClientAliveCountMax 0

        # Désactiver le transfert X11 et le forwarding
        X11Forwarding no
        AllowTcpForwarding no
        ```

        #### 🔹 3. Outil d'Audit de Conformité ANSSI : Lynis
        * Installation : `apt update && apt install lynis`
        * Lancement d'un audit de sécurité complet : `lynis audit system`
        * *Hardening Index Target* : Viser un score de sécurité supérieur à **75/100**.
        """)

    with tab_an2:
        st.subheader("2. Durcissement Active Directory : Le Modèle de Tiering à 3 Niveaux")
        st.markdown(r"""
        #### 🔹 Le Modèle de Partitionnement Administratif (Tiering Model)
        Pour empêcher une compromission latérale (*Pass-the-Hash* / *Golden Ticket*), l'ANSSI impose une séparation stricte des privilèges :

        ```text
        [ TIER 0 ] Control Plane (Contrôleurs de Domaine, PKI Racine, Comptes Admin du Domaine)
             |   (Etanche : Interdiction formelle de se connecter sur un Tier 1 ou Tier 2)
             v
        [ TIER 1 ] Server Plane (Serveurs Membres, Serveurs Web, Bases de Données)
             |   (Étanche : Admin Tier 1 ne peut pas se connecter sur un Tier 2)
             v
        [ TIER 2 ] Workstation Plane (Postes de Travail Utilisateurs, Imprimantes)
        ```

        #### 🔹 Mesures Incontournables de Durcissement ADDS :
        1. **Renouvellement Périodique du Compte KRBTGT** : Changer deux fois consécutivement le mot de passe du compte `krbtgt` pour invalider tout *Golden Ticket* compromis.
        2. **Désactivation des Protocoles Vulnérables** :
           - Désactiver **NTLMv1** au profit de Kerberos et NTLMv2.
           - Désactiver **LLMNR** (*Link-Local Multicast Name Resolution*) et **NBT-NS** (*NetBIOS Name Service*) sur tous les postes membres via GPO.
        3. **Déploiement de LAPS** (*Local Administrator Password Solution*) : Garantit que chaque poste de travail possède un mot de passe administrateur local unique, aléatoire et renouvelé tous les 30 jours.
        """)

    with tab_an3:
        st.subheader("3. Sécurisation des Réseaux Wi-Fi d'Entreprise & Passerelles IoT")
        st.markdown(r"""
        #### 🔹 Architecture WPA3-Enterprise / 802.1X avec Serveur RADIUS
        * **Chiffrement** : WPA3-Enterprise avec suite cryptographique GCMP-256 bits.
        * **Authentification 802.1X** : Protocole **EAP-TLS** obligatoire (authentification mutuelle du poste client et du serveur via certificats X.509 délivrés par la PKI d'entreprise).
        * **Segmentation IoT** : Isoler impérativement tous les équipements d'IoT industrielle dans un **VLAN dédié** restreint par un pare-feu pfSense (accès au LAN interdit).
        """)

    with tab_an4:
        st.subheader("4. Synthèse de la Politique de Sécurité du Système d'Information (PSSI)")
        st.markdown(r"""
        #### 🔹 Les 4 Piliers DICP de la PSSI :
        1. **Disponibilité (D)** : Garantir la continuité de service (Redondance, RAID, Onduleurs).
        2. **Intégrité (I)** : Garantir l'absence de modification non autorisée (Hachage SHA-256, signatures).
        3. **Confidentialité (C)** : Garantir que seules les personnes autorisées ont accès aux données (Chiffrement AES-256, ACLs).
        4. **Preuve / Traçabilité (P)** : Conserver les journaux d'événements horodatés (Syslog centralisé, SIEM).
        """)

    with tab_an5:
        st.subheader("✍️ Quiz Hardening & Sécurité Système")
        q_ans_1 = st.radio("Dans le modèle de Tiering ANSSI Active Directory, un administrateur Tier 0 a-t-il le droit de se connecter sur un poste de travail Tier 2 ?", ["Non, c'est strictement interdit (risque d'usurpation de jeton)", "Oui, c'est autorisé pour le dépannage"], key="ans_q1")
        if st.button("Valider Quiz Hardening", type="primary", key="btn_ans"):
            if "Non" in q_ans_1:
                st.success("🎉 **Exact !** Les administrateurs Tier 0 ne doivent jamais se connecter sur un Tier 1 ou Tier 2 pour éviter le vol de leurs identifiants par une attaque Pass-the-Hash.")
            else:
                st.error("❌ Incorrect. L'isolation stricte des Tiers empêche la compromission du domaine.")



elif page == "🇬🇧 Vocabulaire & Anglais Technique BTS":
    st.markdown("<div class='hero-title'>🇬🇧 Vocabulaire & Anglais Technique BTS CIEL</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Module de préparation à l'épreuve écrite d'Anglais Technique, au décodage de datasheets et aux oraux E4/E6</p>", unsafe_allow_html=True)

    tab_en1, tab_en2, tab_en3, tab_en4 = st.tabs([
        "📖 Lexique Bilingue (100+ Mots)",
        "📄 Texts & Technical Articles",
        "🗣️ Oral Presentation Guide",
        "✍️ Translation Exercises"
    ])

    with tab_en1:
        st.subheader("1. Technical Vocabulary Glossary (Réseaux, Cyber, Dev & IoT)")
        
        col_lex1, col_lex2 = st.columns(2)
        with col_lex1:
            st.markdown("""
            #### 📶 Network & Telecoms
            * **Bandwidth** : Bande passante.
            * **Throughput** : Débit effectif (utile).
            * **Latency / Delay** : Temps de propagation / Latence.
            * **Default Gateway** : Passerelle par défaut.
            * **Broadcast Domain** : Domaine de diffusion.
            * **Frame** : Trame (Couche 2 OSI).
            * **Packet** : Paquet (Couche 3 OSI).
            * **Payload** : Charge utile de la trame/paquet.
            * **Acknowledge (ACK)** : Accusé de réception.
            * **Trunk Link** : Lien d'agrégation de VLANs.

            #### 🔒 Cybersecurity & Hardening
            * **Breach / Compromise** : Violation de sécurité / Compromission.
            * **Threat / Risk** : Menace / Risque.
            * **Eavesdropping** : Écoute clandestine (Sniffing).
            * **Tampering** : Altération non autorisée.
            * **Disclosure** : Divulgation de données.
            * **Denial of Service (DoS)** : Déni de service.
            * **Ciphertext** : Texte chiffré.
            * **Plaintext** : Texte en clair.
            * **Hardening** : Durcissement de sécurité.
            """)
        with col_lex2:
            st.markdown("""
            #### 💻 Software Engineering & Embedded C++
            * **Memory Leak** : Fuite de mémoire.
            * **Pointer / Reference** : Pointeur / Référence.
            * **Stack vs Heap** : Pile vs Tas.
            * **Overhead** : Surcoût de traitement ou d'en-tête.
            * **Inheritance** : Héritage (POO).
            * **Scope** : Portée d'une variable.
            * **Thread-safe** : Sécurisé pour l'exécution multithread.
            * **Bug / Flaw / Vulnerability** : Erreur / Faille / Vulnérabilité.

            #### 🔌 Electronics & Hardware
            * **Duty Cycle** : Rapport cyclique ($\alpha$).
            * **Sampling Rate** : Fréquence d'échantillonnage ($Fe$).
            * **Power Dissipation** : Dissipation thermique.
            * **Pull-up Resistor** : Résistance de tirage au niveau haut.
            * **Flyback Diode** : Diode de roue libre.
            * **Embedded System** : Système embarqué.
            """)

    with tab_en2:
        st.subheader("2. Technical Document Analysis (Sujets Type BTS)")
        st.markdown(r"""
        #### 🔹 Text 1 : Cybersecurity Incident Report Overview
        > *"In October 2025, a industrial facility experienced a severe ransomware outbreak. The initial vector was identified as a phishing email containing a malicious attachment. Once executed, the payload exploited an unpatched vulnerability in the legacy Windows Server 2016 operating system to achieve local privilege escalation. The attackers then used Pass-the-Hash techniques to compromise the Tier 0 Active Directory domain controller."*

        * **Questions de Compréhension** :
          1. Quel a été le vecteur d'attaque initial ? $\rightarrow$ Un courriel d'hameçonnage (*phishing*) avec pièce jointe malveillante.
          2. Quelle technique a permis de compromettre le contrôleur de domaine ? $\rightarrow$ La technique de survol d'identifiants *Pass-the-Hash*.
        """)

    with tab_en3:
        st.subheader("3. Guide pour la Présentation Orale en Anglais (Oral E6 / E4)")
        st.markdown(r"""
        #### 🔹 Useful Phrases for Project Presentation:
        * **Introduction** : *"Good morning members of the jury. Today, I am going to present my final project entitled 'IoT Smart Gateway for Industrial Monitoring'."*
        * **Architecture** : *"Our system is divided into three main layers: the sensing layer with Modbus RTU, the network layer with pfSense, and the cloud layer using MQTTS."*
        * **Technical Choice Justification** : *"We chose C++ over Python for the gateway core because of its strict memory management and low execution overhead."*
        * **Conclusion & Testing** : *"All functional requirements were successfully verified using Pytest automated testing scripts."*
        """)

    with tab_en4:
        st.subheader("✍️ Translation & Technical English Exercises")
        st.markdown("**Translate to English** : *'La bande passante minimale du réseau Wi-Fi doit être supérieure à 100 Mbits/s pour éviter la latence.'*")
        user_tr = st.text_input("Votre traduction :", key="en_tr")
        if st.button("Check Translation", type="primary", key="btn_en"):
            if "bandwidth" in user_tr.lower() and "latency" in user_tr.lower():
                st.success("🎉 **Great translation!** Example: *'The minimum Wi-Fi network bandwidth must be greater than 100 Mbps to prevent latency.'*")
            else:
                st.info("💡 Expected keywords: *bandwidth*, *greater than 100 Mbps*, *prevent/avoid latency*.")


elif page == "📹 Vidéos de Cours":
    st.markdown("<div class='hero-title'>📹 Vidéothèque Pédagogique BTS CIEL</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Retrouvez l'intégralité des leçons vidéo classées par pôles d'ingénierie pour réviser visuellement vos cours et TPs</p>", unsafe_allow_html=True)
    
    yt_p = 'https://www.youtube.com/watch?v='
    
    VIDEOS_BY_DOMAIN = {
        "📶 Réseaux & Télécoms": [
            {"titre": "Comprendre le Modèle OSI en 10 minutes", "id": "33UJvS_z8R8", "chap": "Modèle OSI & TCP/IP"},
            {"titre": "Masterclass Subnetting VLSM IPv4", "id": "42S-A-9PqM0", "chap": "Subnetting & Masques IP"},
            {"titre": "IPv6, SLAAC et NDP expliqués simplement", "id": "72sn_0M4T4g", "chap": "IPv6 & Protocoles associées"},
            {"titre": "Comprendre et configurer un VLAN", "id": "06Y6qYg9_C0", "chap": "Commutation & VLANs"},
            {"titre": "Tout savoir sur le Trunking IEEE 802.1Q", "id": "0j3_T7sN8J4", "chap": "Trunking 802.1Q"},
            {"titre": "Configuration Router-on-a-Stick Cisco", "id": "LqT5y7aZJ4k", "chap": "Routage Inter-VLAN"},
            {"titre": "Spanning Tree Protocol (STP & RSTP 802.1w)", "id": "i8D4W6U4z_E", "chap": "Commutation Redondante"},
            {"titre": "Comprendre le routage dynamique OSPF", "id": "3k1-zK7u1G0", "chap": "Routage OSPF"},
            {"titre": "Maîtriser les filtres d'affichage Wireshark", "id": "TkCSr30UojM", "chap": "Analyse de trames Wireshark"}
        ],
        "🔒 Cybersécurité & Gouvernance": [
            {"titre": "Méthode EBIOS RM de l'ANSSI en 5 Ateliers", "id": "J8n0j3x9K2A", "chap": "Gouvernance EBIOS RM"},
            {"titre": "Réaliser une Analyse d'Impact RGPD (PIA / AIPD)", "id": "5k9m2-8a9X0", "chap": "Conformité RGPD & PIA"},
            {"titre": "Chiffrement Symétrique vs Asymétrique & PKI", "id": "0iY2m-J4z-0", "chap": "Cryptographie & PKI"},
            {"titre": "Architecture DMZ & Configuration Pare-Feu pfSense", "id": "L2k3j4X5m-0", "chap": "pfSense & Isolation DMZ"},
            {"titre": "Top 10 OWASP : Injections SQL & Requêtes Préparées", "id": "0k3j4X5m-0", "chap": "Sécurité Web OWASP"},
            {"titre": "Tunnels VPN IPsec (L3) vs TLS OpenVPN (L4)", "id": "L2k3j4X5m-0", "chap": "Sécurisation VPN"},
            {"titre": "Wi-Fi 802.1X & Serveur d'Authentification RADIUS", "id": "8m9k3j4X5m0", "chap": "Sécurité Réseau 802.1X"}
        ],
        "💻 Programmation C++, Python & Git": [
            {"titre": "Débutez en C++ - Les bases du langage", "id": "6m8gS-iXmXQ", "chap": "Langage C++"},
            {"titre": "Comprendre la mémoire C++ : Pile vs Tas, Pointeurs", "id": "S1yR7_7bWRE", "chap": "Gestion Mémoire C++"},
            {"titre": "La POO en C++ : Classes, Encapsulation & Héritage", "id": "6m8gS-iXmXQ", "chap": "POO C++"},
            {"titre": "Multithreading en C++11 : std::thread & std::mutex", "id": "5m9k3j4X5m0", "chap": "Concurrence C++"},
            {"titre": "Programmation Réseau Sockets TCP/UDP en Python", "id": "6m9k3j4X5m0", "chap": "Sockets Python"},
            {"titre": "Tutoriel Git : add, commit, push & branches", "id": "6m8gS-iXmXQ", "chap": "Versioning Git"}
        ],
        "🖥️ Administration Système Linux & Active Directory": [
            {"titre": "Linux Permissions octales chmod, SUID & ACLs", "id": "2n3j4X5m-0", "chap": "Droits Linux POSIX"},
            {"titre": "Gestion des Services systemd & systemctl", "id": "2n3j4X5m-0", "chap": "Systemd Linux"},
            {"titre": "Active Directory de A à Z - Tutoriel Complet", "id": "rQ_1n8Y0o-0", "chap": "Active Directory ADDS"},
            {"titre": "Gestion des Stratégies de Groupe (GPO LSDOU)", "id": "8m9k3j4X5m0", "chap": "GPO Windows Server"},
            {"titre": "Authentification Kerberos & Rôles FSMO", "id": "8m9k3j4X5m0", "chap": "Kerberos & FSMO"},
            {"titre": "Commandes PowerShell pour Active Directory & Réseau", "id": "8m9k3j4X5m0", "chap": "PowerShell AD"}
        ],
        "🔌 Électronique, Signaux & Bus Industriels": [
            {"titre": "Lois fondamentales d'Électricité : Ohm & Kirchhoff", "id": "7m9k3j4X5m0", "chap": "Lois Fondamentales"},
            {"titre": "Le Pont en H BTS7960 & Commande de Moteur CC", "id": "8m9k3j4X5m0", "chap": "Électronique de Puissance"},
            {"titre": "La Modulation de Largeur d'Impulsion (PWM/MLI)", "id": "4jS0qUfE_y4", "chap": "Signal PWM MLI"},
            {"titre": "La Boucle de Courant 4-20 mA Industrielle", "id": "9m9k3j4X5m0", "chap": "Capteurs 4-20 mA"},
            {"titre": "Le Bus CAN Industriel & Automobile (ISO 11898)", "id": "10m9k3j4X5m0", "chap": "Bus CAN Différentiel"},
            {"titre": "Le Protocole Modbus RTU sur RS-485", "id": "11m9k3j4X5m0", "chap": "Modbus RTU RS-485"}
        ],
        "📐 Mathématiques, SysML & Projet E6": [
            {"titre": "Suites Arithmétiques & Géométriques (Formules & Sommes)", "id": "12m9k3j4X5m0", "chap": "Suites Mathématiques"},
            {"titre": "Fonctions Exponentielle & Logarithme Népérien", "id": "13m9k3j4X5m0", "chap": "Exp & Ln Math"},
            {"titre": "Diagrammes SysML : BDD, IBD & Requirement Diagram", "id": "14m9k3j4X5m0", "chap": "Modélisation SysML"},
            {"titre": "Diagrammes UML : Classes, Séquence & États-Transitions", "id": "15m9k3j4X5m0", "chap": "Modélisation UML"},
            {"titre": "Qualification E6 : Tests Automatisés avec Pytest", "id": "16m9k3j4X5m0", "chap": "Pytest & PVL E6"}
        ]
    }
    
    sel_domain = st.selectbox("📁 Choisissez un domaine d'ingénierie :", list(VIDEOS_BY_DOMAIN.keys()))
    v_list = VIDEOS_BY_DOMAIN[sel_domain]
    
    st.markdown(f"### 📹 {len(v_list)} Leçons Vidéo - {sel_domain}")
    
    for v in v_list:
        v_url = yt_p + v["id"]
        with st.expander(f"▶️ {v['titre']} (Chapitre : {v['chap']})"):
            st.markdown(f"**Chapitre associé :** `{v['chap']}`")
            st.link_button("▶️ Regarder directement sur YouTube", v_url, type="primary")
            st.video(v_url)
        st.markdown("---")


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
