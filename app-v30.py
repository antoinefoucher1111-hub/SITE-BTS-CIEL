import streamlit as st
import random
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
st.set_page_config(page_title='BTS CIEL Pro Studio - Excellence Numérique', page_icon='⚡', layout='wide', initial_sidebar_state='expanded')
import matplotlib
matplotlib.use('Agg')
st.markdown(r'''/* Modern Clean Tech CSS for BTS CIEL Studio Pro */
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    :root {
        --bg-main: #050811;
        --card-bg: rgba(13, 19, 36, 0.75);
        --card-border: rgba(255, 255, 255, 0.08);
        --card-border-hover: rgba(56, 189, 248, 0.4);
        --accent-glow: radial-gradient(circle at 50% 0%, rgba(29, 78, 216, 0.25), transparent 70%);
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --brand-blue: #38bdf8;
        --brand-orange: #fb923c;
        --brand-emerald: #34d399;
        --brand-purple: #c084fc;
    }
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #050811 !important;
        color: #f8fafc !important;
    }
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    /* Global scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #050811;
    }
    ::-webkit-scrollbar-thumb {
        background: #1e293b;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #334155;
    }

    /* Container constraints */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1250px !important;
    }
    
    /* Header hero with subtle noise & Monopo-like warm-cold gradient */
    .hero-container {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, #090e1d 0%, #0d1527 45%, #181d33 80%, #201724 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 20px !important;
        padding: 32px 36px !important;
        margin-bottom: 24px !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
    }
    .hero-container::before {
        content: "";
        position: absolute;
        top: -50%;
        right: -10%;
        width: 500px;
        height: 350px;
        background: radial-gradient(circle, rgba(251, 146, 60, 0.15) 0%, rgba(56, 189, 248, 0.12) 50%, transparent 80%);
        filter: blur(50px);
        pointer-events: none;
    }
    .hero-title {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em !important;
        background: linear-gradient(110deg, #ffffff 0%, #cbd5e1 50%, #93c5fd 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 6px !important;
    }
    .hero-subtitle {
        font-size: 1.05rem !important;
        color: #94a3b8 !important;
        font-weight: 400 !important;
        line-height: 1.6 !important;
        max-width: 850px !important;
    }
    
    /* Badges */
    .badge {
        display: inline-flex !important;
        align-items: center !important;
        padding: 4px 12px !important;
        border-radius: 9999px !important;
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        margin-right: 8px !important;
        margin-top: 6px !important;
        backdrop-filter: blur(8px);
    }
    .badge-blue { background: rgba(56, 189, 248, 0.12) !important; color: #38bdf8 !important; border: 1px solid rgba(56, 189, 248, 0.3) !important; }
    .badge-emerald { background: rgba(52, 211, 153, 0.12) !important; color: #34d399 !important; border: 1px solid rgba(52, 211, 153, 0.3) !important; }
    .badge-purple { background: rgba(192, 132, 252, 0.12) !important; color: #c084fc !important; border: 1px solid rgba(192, 132, 252, 0.3) !important; }
    .badge-amber { background: rgba(251, 146, 60, 0.12) !important; color: #fb923c !important; border: 1px solid rgba(251, 146, 60, 0.3) !important; }
    .badge-rose { background: rgba(244, 63, 94, 0.12) !important; color: #f43f5e !important; border: 1px solid rgba(244, 63, 94, 0.3) !important; }
    
    /* Cards - Premium Dark Glassmorphism */
    .ciel-card {
        background: rgba(13, 20, 38, 0.7) !important;
        color: #f1f5f9 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 8px 24px -6px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.06) !important;
        backdrop-filter: blur(12px) !important;
        transition: all 0.25s ease !important;
    }
    .ciel-card:hover {
        border-color: rgba(56, 189, 248, 0.35) !important;
        transform: translateY(-2px);
        box-shadow: 0 12px 30px -8px rgba(56, 189, 248, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    }
    .ciel-card h3 {
        color: #f8fafc !important;
        font-weight: 700 !important;
        font-size: 1.25rem !important;
        margin-bottom: 12px !important;
    }
    .ciel-card h4 {
        color: #38bdf8 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        margin-bottom: 10px !important;
    }
    .ciel-card p, .ciel-card li, .ciel-card ul, .ciel-card span {
        color: #cbd5e1 !important;
        line-height: 1.7 !important;
    }
    
    /* User Profile Card */
    .user-profile-header {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 16px !important;
        padding: 16px 20px !important;
        margin-bottom: 20px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3) !important;
    }
    
    /* Interactive Terminal & Lab Simulator UI */
    .terminal-header {
        background: #090d16 !important;
        color: #38bdf8 !important;
        padding: 12px 18px !important;
        border-top-left-radius: 14px !important;
        border-top-right-radius: 14px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    .terminal-body {
        background: #03060d !important;
        color: #e2e8f0 !important;
        padding: 20px !important;
        border-bottom-left-radius: 14px !important;
        border-bottom-right-radius: 14px !important;
        font-family: 'JetBrains Mono', monospace !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-top: none !important;
        margin-bottom: 18px !important;
        font-size: 0.9rem !important;
        line-height: 1.65 !important;
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.6) !important;
    }
    .terminal-dot {
        width: 10px !important;
        height: 10px !important;
        border-radius: 50% !important;
        display: inline-block !important;
    }
    .dot-red { background: #ef4444 !important; box-shadow: 0 0 8px rgba(239, 68, 68, 0.6); }
    .dot-yellow { background: #f59e0b !important; box-shadow: 0 0 8px rgba(245, 158, 11, 0.6); }
    .dot-green { background: #10b981 !important; box-shadow: 0 0 8px rgba(16, 185, 129, 0.6); }
    
    /* Stats & Metric Tiles */
    .stat-box {
        background: rgba(15, 23, 42, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important;
        padding: 20px 16px !important;
        text-align: center !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }
    .stat-number {
        font-size: 2rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    .stat-label {
        font-size: 0.85rem !important;
        color: #94a3b8 !important;
        font-weight: 600 !important;
        margin-top: 4px !important;
    }
    
    /* Flashcard UI */
    .flashcard-box-modern {
        background: linear-gradient(145deg, #0d1527 0%, #111b33 100%) !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 20px !important;
        padding: 36px 30px !important;
        text-align: center !important;
        min-height: 220px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        margin: 18px 0 !important;
        color: #f8fafc !important;
    }
    .flashcard-q-text {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        line-height: 1.55 !important;
    }
    .flashcard-a-box {
        background: rgba(6, 78, 59, 0.25) !important;
        border: 1px solid rgba(52, 211, 153, 0.4) !important;
        border-radius: 14px !important;
        padding: 22px !important;
        margin-top: 18px !important;
        color: #d1fae5 !important;
        font-size: 1.05rem !important;
        text-align: left !important;
        line-height: 1.7 !important;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
    }
    .flashcard-a-box p, .flashcard-a-box span, .flashcard-a-box div, .flashcard-a-box b {
        color: #d1fae5 !important;
    }
    
    /* Streamlit tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px !important;
        background: rgba(15, 23, 42, 0.8) !important;
        padding: 6px !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        margin-bottom: 24px !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px !important;
        padding: 10px 18px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        color: #94a3b8 !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.2s ease !important;
    }
    .stTabs [aria-selected="true"] {
        background: #1e293b !important;
        color: #38bdf8 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
    }
</style>
''', unsafe_allow_html=True)
COURS_BASE = {'📶 Réseaux & Télécoms': {'1. Modèle OSI vs TCP/IP & Encapsulation': "### 🌐 Architecture des Protocoles en Réseau\nLe **modèle OSI (Open Systems Interconnection)** découpe la communication en 7 couches standardisées :\n* **7. Application (PDU: Donnée)** : Protocoles applicatifs de haut niveau (HTTP, HTTPS, DNS, DHCP, SSH, MQTT, SNMP, SMTP).\n* **6. Présentation** : Formatage des données, chiffrement (TLS/SSL) et compression (ASCII, UTF-8, JPEG).\n* **5. Session** : Gestion et synchronisation des sessions d'échanges (NetBIOS, RPC, Sockets).\n* **4. Transport (PDU: Segment / Datagramme)** : Communication de bout en bout et contrôle de flux. **TCP** (orienté connexion, fiable avec accusé de réception ACK et fenêtre glissante) vs **UDP** (sans connexion, rapide, sans garantie d'arrivée, idéal streaming/VoIP/DNS).\n* **3. Réseau (PDU: Paquet)** : Routage logique et adressage mondial (IPv4, IPv6, ICMP, IPsec, protocoles OSPF/BGP). Equipement : **Routeur**.\n* **2. Liaison de données (PDU: Trame)** : Adressage physique (adresses MAC 48 bits), détection d'erreurs (FCS/CRC32), protocoles Ethernet (802.3), Wi-Fi (802.11). Equipement : **Commutateur (Switch)**.\n* **1. Physique (PDU: Bit)** : Transmission des signaux électriques, optiques ou électromagnétiques (RJ45, fibre optique, radio).\n\n**Modèle TCP/IP (4 couches)** : Application, Transport, Internet, Accès Réseau.", '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)': "### 🧮 Méthodologie du Calcul de Masque & Subnetting\nUne adresse **IPv4** fait 32 bits (4 octets). Elle est scindée en **Partie Réseau (NetID)** et **Partie Hôte (HostID)** via le masque de sous-réseau.\n\n#### Règles Fondamentales :\n* **Nombre total d'adresses dans un bloc** = $2^{(32 - \\text{CIDR})}$\n* **Nombre d'adresses d'hôtes utilisables** = $2^{(32 - \\text{CIDR})} - 2$ (on soustrait l'adresse Réseau où tous les bits d'hôte sont à 0, et l'adresse de Broadcast où tous les bits d'hôte sont à 1).\n* **Calcul d'adresse Réseau** = Opération logique `ET (AND)` bit-à-bit entre l'IP et le Masque.\n* **Calcul du Broadcast** = Adresse Réseau + $(2^{(32 - \\text{CIDR})} - 1)$.\n\n#### Table Rapide des Masques Fréquents :\n* `/24` $\\rightarrow$ `255.255.255.0` (256 adresses, 254 hôtes)\n* `/25` $\\rightarrow$ `255.255.255.128` (128 adresses, 126 hôtes)\n* `/26` $\\rightarrow$ `255.255.255.192` (64 adresses, 62 hôtes)\n* `/27` $\\rightarrow$ `255.255.255.224` (32 adresses, 30 hôtes)\n* `/28` $\\rightarrow$ `255.255.255.240` (16 adresses, 14 hôtes)\n* `/29` $\\rightarrow$ `255.255.255.248` (8 adresses, 6 hôtes)\n* `/30` $\\rightarrow$ `255.255.255.252` (4 adresses, 2 hôtes - Liens point-à-point)\n\n#### Notions IPv6 (128 bits) :\n* Notation en 8 groupes de 4 caractères hexadécimaux séparés par des `:`.\n* Règle de compression : omission des zéros en tête (`0db8` $\\rightarrow$ `db8`) et remplacement d'une suite continue de groupes de zéros par `::` (une seule fois par adresse).", '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN': "### 🔀 Segmentation & Routage Virtuel\nUn **VLAN (Virtual LAN)** isole logiquement les domaines de diffusion au sein d'un même commutateur physique.\n\n#### Modes de Ports Switch :\n* **Port Access** : Appartient à un seul VLAN. Les trames y circulent détaguées (standard Ethernet 802.3).\n* **Port Trunk** : Fait transiter plusieurs VLANs simultanément entre switchs ou vers un routeur. Utilise la norme **IEEE 802.1Q** qui insère un tag de **4 octets** dans l'en-tête Ethernet (incluant le VID sur 12 bits, soit 4096 VLANs possibles).\n\n#### Routage Inter-VLAN (Router-on-a-Stick) :\nSur le routeur, une seule interface physique (ex: `g0/0/0`) est découpée en sous-interfaces logiques (`g0/0/0.10`, `g0/0/0.20`) avec la commande `encapsulation dot1Q <ID>`.", "4. Services d'Infrastructure : DHCP, DNS, NAT/PAT": "### ⚙️ Services Réseaux Indispensables\n* **DHCP (Dynamic Host Configuration Protocol)** : Attribution dynamique de configuration IP. Processus **DORA** :\n  1. `Discover` (Client $\\rightarrow$ 255.255.255.255 en UDP 67/68)\n  2. `Offer` (Serveur $\\rightarrow$ Client)\n  3. `Request` (Client $\\rightarrow$ Serveur)\n  4. `Acknowledge` (Serveur valide le bail IP)\n* **DNS (Domain Name System)** : Résolution de noms d'hôtes. Types d'enregistrements : `A` (IPv4), `AAAA` (IPv6), `CNAME` (Alias), `MX` (Serveur mail), `PTR` (Résolution inverse).\n* **NAT / PAT (Port Address Translation)** : Translation d'adresses privées (RFC 1918) vers une adresse publique unique en multiplexant les numéros de ports source TCP/UDP.", '5. Protocoles Industriels & Bus de terrain (Modbus, Profibus)': "### 🏭 Protocoles Industriels & Bus de terrain (Modbus, Profibus)\nDans l'option A du BTS CIEL, l'étude des réseaux industriels est incontournable. Le protocole **Modbus RTU** (communiquant généralement sur une liaison physique **RS-485**) est un modèle de communication de type maître-esclave.\n\n#### Caractéristiques de Modbus RTU :\n* **Format des trames** : Composé de l'Adresse de l'esclave (1 octet), du Code Fonction (1 octet), des Données (variable) et du contrôle d'erreur CRC-16 (2 octets).\n* **Fonctions de lecture/écriture de registres de base** :\n  * `01` : Read Coils (Sorties binaires)\n  * `02` : Read Discrete Inputs (Entrées binaires)\n  * `03` : Read Holding Registers (Sorties analogiques en lecture/écriture, de taille 16 bits par registre)\n  * `04` : Read Input Registers (Entrées analogiques en lecture seule)\n  * `05` : Write Single Coil (Écriture d'une seule sortie binaire)\n  * `06` : Write Single Register (Écriture d'un seul registre analogique 16 bits)", '6. Transmission optique (Fibres optiques Monomodes & Multimodes)': "### ⚡ Transmission optique (Fibres optiques Monomodes & Multimodes)\nLa fibre optique utilise le principe de réflexion totale interne pour propager des impulsions lumineuses.\n\n#### Fibre Monomode (Single-mode) :\n* **Structure** : Cœur extrêmement étroit (environ 9 micromètres), gaine de 125 micromètres.\n* **Propagation** : Un seul chemin rectiligne de la lumière (un seul mode).\n* **Source** : Diode Laser de forte puissance.\n* **Performance** : Absence quasi-totale de dispersion modale, portée kilométrique très longue distance, idéale pour les réseaux d'interconnexion WAN.\n\n#### Fibre Multimode (Multi-mode) :\n* **Structure** : Cœur plus large (50 ou 62,5 micromètres).\n* **Propagation** : Plusieurs modes de propagation par rebonds (dispersion modale importante provoquant un étalement des impulsions dans le temps).\n* **Source** : LED ou VCSEL.\n* **Performance** : Portée réduite (courte distance comme les LANs d'entreprises ou Data Centers)."}, '🔒 Cybersécurité': {'1. Cryptographie : Symétrique, Asymétrique & Hachage': "### 🛡️ Les Fondements Cryptographiques\nLa sécurité repose sur la triade **CIA** (Confidentialité, Intégrité, Disponibilité) + Authenticité et Non-répudiation.\n\n* **Chiffrement Symétrique** : Même clé secrète pour chiffrer et déchiffrer. Rapide, adapté aux flux volumineux. Standard : **AES-128 / AES-256** (modes CBC, GCM avec authentification intégrée).\n* **Chiffrement Asymétrique** : Paire de clés mathématiquement liées (Clé Publique distribuable, Clé Privée secrète). Algorithmes : **RSA (2048/4096 bits)**, **ECC (Courbes Elliptiques)**. Utilisé pour l'échange de clés de session et les signatures numériques.\n* **Fonctions de Hachage** : Condensat à sens unique de taille fixe. Vérifie l'intégrité stricte. Algorithmes : **SHA-256**, **SHA-3** (MD5 et SHA-1 sont aujourd'hui vulnérables aux collisions).\n* **Certificats X.509 & PKI** : Une Autorité de Certification (CA) signe la clé publique d'un serveur pour attester de son identité.", '2. Top 10 OWASP & Sécurité Applicative': '### 🚨 Vulnérabilités Web et Remédiations\n* **Injections SQL** : L\'attaquant injecte du code SQL non filtré pour manipuler la BDD.\n  * *Exemple vulnérable* : `query = "SELECT * FROM users WHERE user=\'" + input + "\'"`\n  * *Remédiation absolue* : Utiliser exclusivement des **requêtes préparées (paramétrées)** via PDO en PHP ou `cursor.execute("SELECT * FROM users WHERE user=%s", (input,))` en Python.\n* **Cross-Site Scripting (XSS)** : Injection de scripts JavaScript malveillants exécutés par les navigateurs clients.\n  * *Remédiation* : Échappement des caractères HTML (`htmlspecialchars()`), CSP (Content Security Policy).\n* **CSRF (Cross-Site Request Forgery)** : Forcer un utilisateur authentifié à exécuter des actions non désirées. *Remédiation* : Jetons (tokens) anti-CSRF aléatoires et synchronisés.', '3. Pare-feux, VPN & Sécurisation Système': "### 🧱 Défense Périmétrique et Durcissement\n* **Pare-feu Stateful** : Analyse l'état des connexions (table d'états TCP). Sous Linux : `iptables` / `nftables` ou `ufw`.\n* **VPN (Virtual Private Network)** :\n  * **IPsec** : Opère en couche 3. Protocoles `AH` (Intégrité/Authentification) et `ESP` (Chiffrement + Intégrité). Modes : Transport (hôte à hôte) ou Tunnel (site à site).\n  * **OpenVPN / WireGuard** : VPN applicatif et niveau kernel moderne utilisant TLS/chiffrement moderne.\n* **Port Security Cisco** : Limite le nombre d'adresses MAC autorisées par port de switch pour contrer le MAC Flooding (`switchport port-security maximum 1`, `switchport port-security violation shutdown`).", '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)': "### 🛡️ Protocoles Sécurisés : Chiffrement & Authentification\n* **VPN (Virtual Private Network)** : Crée un tunnel sécurisé à travers un réseau non sécurisé (Internet).\n  * **IPsec** : Opère en couche 3 (Réseau) pour chiffrer l'intégralité du trafic IP d'un site à un autre (VPN Site-à-Site).\n  * **OpenVPN / WireGuard** : Utilise le protocole SSL/TLS ou des mécanismes cryptographiques modernes (Noise protocol) de couche Transport pour les connexions clients d'accès à distance.\n* **HTTPS** : Sécurisation du protocole HTTP par l'utilisation d'une couche TLS. Lors du **TLS Handshake** (poignée de main TLS), le client et le serveur s'accordent sur les algorithmes (Cipher Suite), s'authentifient via des certificats X.509 et génèrent une clé symétrique de session temporaire.\n* **MQTTS** : Variante sécurisée de MQTT qui utilise TLS (Port par défaut 8883) pour chiffrer les flux d'objets connectés et authentifier les clients de manière robuste."}, '💻 Programmation / Dev': {'1. Langage C++ : Mémoire, Pointeurs & POO': "### ⚡ Maîtrise Bas Niveau & Orientée Objet en C++\nLe C++ est au cœur du BTS CIEL pour la programmation système et microcontrôleurs embarqués.\n\n#### Gestion de la Mémoire :\n* **Pile (Stack)** : Gestion automatique, rapide, portée limitée au bloc `{}`.\n* **Tas (Heap)** : Allocation manuelle dynamique avec `new` / `new[]`. Doit obligatoirement être libérée avec `delete` / `delete[]` pour éviter les **fuites de mémoire (Memory Leaks)**.\n* **Pointeurs & Références** :\n  * `int x = 42; int* p = &x;` $\\rightarrow$ `p` contient l'adresse, `*p` accède à la valeur.\n  * `void modifier(int& ref)` $\\rightarrow$ passage par référence (sans copie mémoire).\n\n#### Programmation Orientée Objet (POO) :\n* **Encapsulation** : Données membres `private` accessibles via `getters`/`setters` `public`.\n* **Héritage** : `class CapteurTemperature : public Capteur`.\n* **Polymorphisme & Classes Abstraites** : Méthode déclarée `virtual void mesurer() = 0;` (méthode virtuelle pure). La classe devient abstraite et impose l'implémentation dans les classes dérivées.", '2. Python Réseau, Systèmes & Sockets': "### 🐍 Automatisation & Sockets Réseau en Python\nPython est l'outil privilégié pour les scripts de passerelle, de traitement de données IoT et d'administration système.\n\n#### Client TCP Sockets :\n```python\nimport socket\nwith socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:\n    s.connect(('192.168.1.50', 8080))\n    s.sendall(b'GET_TELEMETRY\\n')\n    data = s.recv(1024)\n    print('Reçu:', data.decode('utf-8'))\n```\n\n#### Manipulation de données JSON :\n```python\nimport json\npayload = {'capteur_id': 'TEMP_01', 'valeur': 23.4, 'unite': 'C'}\njson_str = json.dumps(payload)\n```", '3. Structures de données avancées & Unions en Langage C': "### 🏗️ Structures de données avancées & Unions en Langage C\n* **Structures (`struct`)** : Regroupement de plusieurs variables de types différents. En mémoire, chaque variable possède sa propre adresse, et la taille globale est au minimum égale à la somme des membres, plus d'éventuels octets de bourrage (padding) insérés par le compilateur pour l'alignement mémoire.\n* **Unions (`union`)** : Regroupement de membres de types différents partageant la **même zone mémoire**. À tout moment, un seul membre peut être stocké dans l'union. L'occupation mémoire totale d'une union est égale à la taille de son membre le plus volumineux.\n* **Exemple d'union** :\n  ```cpp\n  union Paquet {\n      char brut[4];\n      float valeur; // Partage le même espace de 4 octets\n  };\n  ```"}, '🖥️ Administration Système': {'1. Droits Linux & Commandes Système': '### 🐧 Administration GNU/Linux\n* **Droits Octaux (`chmod`)** :\n  * `r` (Lecture) = 4, `w` (Écriture) = 2, `x` (Exécution) = 1.\n  * `chmod 750 script.sh` : Propriétaire = `rwx` (7), Groupe = `r-x` (5), Autres = `---` (0).\n* **Droits Spéciaux** : SUID (`4000`), SGID (`2000`), Sticky Bit (`1000` ex: `/tmp`).\n* **Services Systemd** : `systemctl start|stop|restart|status|enable service_name`.\n* **Supervision des logs** : `journalctl -u service_name -f` ou `tail -f /var/log/syslog`.', '2. Active Directory, Domaines & GPO': "### 🏢 Gestion de Parc sous Windows Server\n* **Active Directory Domain Services (AD DS)** : Annuaire d'objets (Utilisateurs, Groupes, Ordinateurs).\n* **Unités d'Organisation (OU)** : Conteneurs logiques pour organiser le domaine.\n* **GPO (Group Policy Object)** : Politiques de configuration et de durcissement centralisées.\n* **Ordre d'application des GPO (LSDOU)** : **L**ocal $\\rightarrow$ **S**ite $\\rightarrow$ **D**omaine $\\rightarrow$ **O**U (la dernière stratégie appliquée prévaut sauf configuration 'Enforced').", '3. Virtualisation & Environnements Serveurs (Debian, VMware)': "### 🖥️ Virtualisation & Environnements Serveurs (Debian, VMware)\nLa virtualisation permet de faire fonctionner plusieurs machines virtuelles (VM) sur un unique serveur physique (Hyperviseur).\n\n#### Hyperviseurs de Type 1 (Bare Metal) :\n* Opèrent directement sur le matériel physique du serveur, sans système d'exploitation hôte préalable.\n* Offrent des performances optimales et une isolation stricte des ressources.\n* Exemples : **VMware ESXi**, Microsoft Hyper-V Server, Proxmox VE (KVM).\n\n#### Hyperviseurs de Type 2 (Hosted) :\n* S'exécutent comme des applications au-dessus d'un système d'exploitation hôte existant (Windows, Linux, macOS).\n* Exemples : **VMware Workstation**, Oracle VM VirtualBox.\n\n#### Serveur Linux Debian :\n* Système d'exploitation stable par excellence pour héberger des serveurs d'infrastructure (DNS Bind9, DHCP isc-dhcp-server, Apache, etc.)."}, '🔌 Électronique & IoT': {'1. Échantillonnage, CAN/CNA & Théorème de Shannon': "### 📡 Numérisation & Traitement du Signal\n* **Théorème de Nyquist-Shannon** : La fréquence d'échantillonnage $Fe$ doit respecter $Fe \\ge 2 \\times F_{max}$ pour éviter tout **repliement de spectre (Aliasing)**. On place un filtre passe-bas anti-repliement avant le CAN.\n* **Convertisseur Analogique-Numérique (CAN / ADC)** :\n  * Résolution : $n$ bits $\\rightarrow 2^n$ niveaux de quantification (de $0$ à $2^n - 1$).\n  * **Quantum ($q$)** : Plus petite variation de tension détectable :\n    $$q = \\frac{V_{ref}}{2^n - 1} \\approx \\frac{V_{ref}}{2^n}$$\n  * **Valeur numérique entière ($N$)** pour une tension d'entrée $V_e$ :\n    $$N = \\text{arrondi}\\left(\\frac{V_e}{q}\\right) = \\text{arrondi}\\left(\\frac{V_e \\times (2^n - 1)}{V_{ref}}\\right)$$r", '2. Bus Série Matériels : I2C, SPI, UART & CAN Bus': "### 🔌 Liaisons de Données Embarquées\n* **I2C** : 2 lignes bidirectionnelles (`SDA` Données, `SCL` Horloge). Maître-Esclave, adresses matérielles 7 bits sur bus avec résistances de Pull-up.\n* **SPI** : 4 lignes full-duplex rapide (`MOSI`, `MISO`, `SCLK`, `SS/CS`). Sélection d'esclave active à l'état bas.\n* **UART** : Liaison asynchrone point-à-point (2 fils `Tx`, `Rx`). Nécessite le même débit en bauds (ex: 115200 bauds, 8N1).\n* **Bus CAN** : Bus différentiel robuste (`CAN_H`, `CAN_L`), résistant aux parasites industriels et automobiles. Résistances de terminaison de 120 $\\Omega$ à chaque extrémité.", '3. Protocoles Connectés : MQTT & LoRaWAN': "### ☁️ Protocoles IoT & Télémesure\n* **MQTT (Message Queuing Telemetry Transport)** : Architecture Publish/Subscribe autour d'un courtier (**Broker**). Messages légers publiés sur des thèmes (**Topics** ex: `site/batA/temp`). Niveaux de QoS :\n  * `QoS 0` : Délivré au plus une fois (sans confirmation).\n  * `QoS 1` : Délivré au moins une fois (avec accusé PUBACK).\n  * `QoS 2` : Délivré exactement une fois (four-way handshake).\n* **LoRaWAN** : Réseau LPWAN longue portée (plusieurs kilomètres) à très faible consommation d'énergie sur fréquences sans licence (868 MHz en Europe).", "4. Lois Fondamentales d'Électricité & Composants Passifs": "### 🔌 Lois Fondamentales d'Électricité & Composants Passifs\n* **Loi d'Ohm** : $U = R \\times I$ (la tension en Volts est égale à la résistance en Ohms multipliée par l'intensité en Ampères).\n* **Loi de Joule (Puissance)** : $P = U \\times I = R \\times I^2 = \\frac{U^2}{R}$ (la puissance dissipée par effet Joule est exprimée en Watts).\n* **Lois de Kirchhoff** :\n  * **Loi des Nœuds** : La somme des intensités des courants entrant dans un nœud est égale à la somme des intensités sortant du même nœud.\n  * **Loi des Mailles** : La somme algébrique des tensions le long d'une maille fermée est nulle.\n* **Condensateur** : Stocke des charges électriques.\n  * **Relation Charge-Tension** : $Q = C \\times U$ (la charge en Coulombs est proportionnelle à la capacité en Farads).\n  * **Énergie emmagasinée** : $E_c = \\frac{1}{2} C \\times U^2$ (l'énergie stockée s'exprime en Joules)."}, '📐 Modélisation UML & SysML': {'1. Diagrammes UML Essentiels (Classes, Séquence, Use Case)': "### 📐 Ingénierie Logicielle UML\n* **Diagramme de Classes** : Modèle statique. Multiplicités (`1`, `0..1`, `1..*`, `*`).\n  * **Agrégation (Losange blanc $\\diamond$)** : Relation 'fait partie de' faible. L'élément peut exister sans le conteneur.\n  * **Composition (Losange noir $\\blacklozenge$)** : Relation d'appartenance forte. La destruction du conteneur détruit ses composants.\n  * **Généralisation/Héritage (Flèche à triangle vide $\\rightarrow$)** : Spécialisation de classe.\n* **Diagramme de Séquence** : Chronologie des échanges d'objets au cours du temps. Flèche pleine pour appel synchrone, flèche ouverte pour asynchrone, pointillé pour retour.", '2. Diagrammes SysML (BDD, IBD, Exigences)': "### 🏗️ Modélisation Système SysML\n* **BDD (Block Definition Diagram)** : Découpage structurel global du système en blocs matériels et logiciels.\n* **IBD (Internal Block Diagram)** : Vue interne des flux de données (`flow ports`), d'énergie et de signaux circulant entre les ports des sous-blocs.\n* **Diagramme d'Exigences (Requirement Diagram)** : Définition des critères du cahier des charges avec stéréotypes `<<deriveReqt>>`, `<<satisfy>>` (par un bloc) et `<<verify>>` (par un cas de test)."}}
MINI_QUIZ_COURS = {"1. Modèle OSI vs TCP/IP & Encapsulation": [{"q": "Quelle est l'unité de données de protocole (PDU) de la couche 2 (Liaison de données) ?", "options": ["Bit", "Trame (Frame)", "Paquet", "Segment"], "rep": "Trame (Frame)", "expl": "En couche 2 (Ethernet, Wi-Fi), le PDU est la Trame, adressée par adresses MAC physiques."}, {"q": "Quel protocole opère au niveau de la couche Réseau (Couche 3) ?", "options": ["Ethernet", "IPv4 / IPv6", "TCP", "HTTP"], "rep": "IPv4 / IPv6", "expl": "La couche 3 assure l'adressage logique et le routage mondial via IP."}, {"q": "Combien de couches compte le modèle de référence OSI ?", "options": ["4 couches", "5 couches", "7 couches", "8 couches"], "rep": "7 couches", "expl": "Physique, Liaison, Réseau, Transport, Session, Présentation, Application."}, {"q": "Quelle couche du modèle OSI prend en charge le chiffrement TLS et la compression des données ?", "options": ["Couche 5 (Session)", "Couche 6 (Présentation)", "Couche 7 (Application)", "Couche 4 (Transport)"], "rep": "Couche 6 (Présentation)", "expl": "La couche Présentation standardise le formatage (ASCII, UTF-8, JSON) et gère le chiffrement de bout en bout."}, {"q": "Quel est le PDU spécifique manipulé par le protocole TCP en couche 4 ?", "options": ["Datagramme", "Segment", "Paquet", "Message"], "rep": "Segment", "expl": "En TCP, la couche Transport découpe le flux applicatif en Segments munis de numéros de séquence."}, {"q": "Dans le modèle TCP/IP historique à 4 couches, quelle couche fusionne les couches 1 et 2 du modèle OSI ?", "options": ["Internet", "Accès Réseau", "Transport", "Application"], "rep": "Accès Réseau", "expl": "La couche Accès Réseau (Network Access) regroupe les spécifications matérielles et protocoles de trames (Ethernet, Wi-Fi)."}, {"q": "Comment qualifie-t-on l'opération qui consiste à ajouter un en-tête à chaque descente de couche dans la pile réseau ?", "options": ["Désencapsulation", "Encapsulation", "Multiplexage", "Séquençage"], "rep": "Encapsulation", "expl": "L'encapsulation encapsule la donnée supérieure en lui ajoutant des métadonnées de contrôle propres à la couche."}, {"q": "Quelle est la taille de l'en-tête minimal d'un paquet IPv4 sans options ?", "options": ["8 octets", "20 octets", "32 octets", "40 octets"], "rep": "20 octets", "expl": "L'en-tête IPv4 standard compte 20 octets (IHL = 5 mots de 32 bits). En IPv6, l'en-tête de base est fixe à 40 octets."}, {"q": "Quelle information critique se trouve dans l'en-tête de couche 2 Ethernet II pour désigner le protocole de couche supérieure ?", "options": ["Port source", "EtherType (ex: 0x0800)", "TTL (Time to Live)", "Checksum"], "rep": "EtherType (ex: 0x0800)", "expl": "L'EtherType indique à la couche Liaison quel protocole réseau démultiplexer (0x0800 pour IPv4, 0x86DD pour IPv6, 0x0806 pour ARP)."}, {"q": "Lors du franchissement d'un routeur de niveau 3, qu'advient-il des adresses MAC de la trame ?", "options": ["Elles restent identiques de bout en bout", "Elles sont remplacées par les adresses MAC du saut suivant (Hop-by-Hop)", "Elles sont supprimées définitivement", "Elles sont inversées"], "rep": "Elles sont remplacées par les adresses MAC du saut suivant (Hop-by-Hop)", "expl": "Les adresses IP restent constantes, mais la trame Ethernet est réécrite à chaque saut avec les MAC des interfaces locales."}], "2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)": [{"q": "Combien d'adresses d'hôtes utilisables contient un sous-réseau avec un masque /27 ?", "options": ["32 hôtes", "30 hôtes", "62 hôtes", "14 hôtes"], "rep": "30 hôtes", "expl": "32 - 27 = 5 bits hôtes. 2^5 - 2 = 32 - 2 = 30 adresses utilisables."}, {"q": "Quel est le masque de sous-réseau décimal correspondant à la notation CIDR /28 ?", "options": ["255.255.255.192", "255.255.255.224", "255.255.255.240", "255.255.255.248"], "rep": "255.255.255.240", "expl": "240 = 128 + 64 + 32 + 16 (4 bits à 1 dans le dernier octet : 24 + 4 = 28)."}, {"q": "Pour l'adresse IP 192.168.1.130/26, quelle est l'adresse de diffusion (Broadcast) ?", "options": ["192.168.1.191", "192.168.1.192", "192.168.1.255", "192.168.1.128"], "rep": "192.168.1.191", "expl": "Le pas du /26 est 64. Les blocs sont 0-63, 64-127, 128-191. Le broadcast est 192.168.1.191."}, {"q": "Sur un lien point-à-point entre deux routeurs, quel est le masque CIDR le plus économe en adresses IPv4 ?", "options": ["/29", "/30", "/31", "/28"], "rep": "/30", "expl": "Le /30 fournit 4 adresses au total dont exactement 2 utilisables pour les deux interfaces de routage."}, {"q": "Combien de bits compte une adresse IPv6 complète ?", "options": ["32 bits", "64 bits", "128 bits", "256 bits"], "rep": "128 bits", "expl": "Une adresse IPv6 fait 128 bits, représentée en 8 groupes de 4 caractères hexadécimaux."}, {"q": "Quelle règle s'applique lors de la compression d'une suite continue de zéros en IPv6 avec le symbole '::' ?", "options": ["On peut l'utiliser autant de fois qu'on veut", "Elle n'est autorisée qu'une seule fois par adresse", "Elle ne s'applique qu'au début de l'adresse", "Elle est interdite en production"], "rep": "Elle n'est autorisée qu'une seule fois par adresse", "expl": "Le double deux-points '::' ne peut apparaître qu'une seule fois dans une adresse IPv6."}, {"q": "Quelle est la plage d'adresses privées de Classe B selon la RFC 1918 ?", "options": ["10.0.0.0 à 10.255.255.255", "172.16.0.0 à 172.31.255.255", "192.168.0.0 à 192.168.255.255", "169.254.0.0 à 169.254.255.255"], "rep": "172.16.0.0 à 172.31.255.255", "expl": "La classe B privée comprend 16 blocs /16 contigus de 172.16.0.0 à 172.31.255.255."}, {"q": "Dans le mécanisme SLAAC en IPv6, comment est calculé l'Interface-ID 64 bits selon la méthode EUI-64 depuis l'adresse MAC ?", "options": ["On hache la MAC avec SHA-256", "On insère FFFE au milieu et on inverse le 7e bit (Universal/Local)", "On concatène 0000 au début", "On ajoute l'adresse IP du routeur"], "rep": "On insère FFFE au milieu et on inverse le 7e bit (Universal/Local)", "expl": "Pour une MAC à 48 bits, on insère FF:FE entre le 3e et 4e octet, et on inverse le bit universel/local."}, {"q": "Quel type d'adresse commence toujours par le préfixe fe80::/10 en IPv6 ?", "options": ["Global Unicast (GUA)", "Link-Local (Lien local)", "Multicast", "Unique Local (ULA)"], "rep": "Link-Local (Lien local)", "expl": "Les adresses Link-Local (fe80::/10) sont auto-générées pour chaque interface réseau et ne sont pas routables hors du lien."}, {"q": "Si un sous-réseau IPv4 a pour adresse réseau 10.20.30.0 et masque 255.255.255.128, quelle est sa première adresse hôte utilisable ?", "options": ["10.20.30.0", "10.20.30.1", "10.20.30.2", "10.20.30.127"], "rep": "10.20.30.1", "expl": "La première adresse assignable est immédiatement l'adresse réseau + 1, soit 10.20.30.1."}], "3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN": [{"q": "Sur un commutateur Cisco, quelle commande active le mode Trunk sur une interface GigabitEthernet0/1 ?", "options": ["switchport mode access", "switchport mode trunk", "spanning-tree trunk", "vlan trunk enable"], "rep": "switchport mode trunk", "expl": "La commande 'switchport mode trunk' configure le port pour agréger plusieurs flux VLAN étiquetés."}, {"q": "Quelle est la taille de l'en-tête (tag) inséré dans la trame Ethernet par le protocole IEEE 802.1Q ?", "options": ["2 octets", "4 octets", "8 octets", "12 octets"], "rep": "4 octets", "expl": "Le tag 802.1Q fait 4 octets (32 bits), dont 12 bits réservés pour le VLAN ID (valeurs de 1 à 4094)."}, {"q": "Comment voyage le trafic appartenant au VLAN Natif sur une liaison Trunk 802.1Q ?", "options": ["Il est chiffré en AES", "Il n'est pas étiqueté (Untagged)", "Il possède un tag de 8 octets", "Il est rejeté automatiquement"], "rep": "Il n'est pas étiqueté (Untagged)", "expl": "Par défaut (VLAN 1 sur Cisco), le VLAN natif transite sans tag 802.1Q pour préserver la rétrocompatibilité."}, {"q": "Dans une architecture 'Router-on-a-Stick', comment configure-t-on le routeur pour desservir le VLAN 20 ?", "options": ["On achète une carte réseau physique dédiée par VLAN", "On crée une sous-interface logique (ex: g0/0.20) avec 'encapsulation dot1Q 20'", "On active le protocole NAT sur chaque port", "On configure une passerelle par défaut 0.0.0.0"], "rep": "On crée une sous-interface logique (ex: g0/0.20) avec 'encapsulation dot1Q 20'", "expl": "Une sous-interface logique encapsule et désencapsule le tag 802.1Q avant d'appliquer les règles de routage inter-VLAN."}, {"q": "Quelle commande Cisco IOS permet de lister de manière concise tous les VLANs et leurs ports associés ?", "options": ["show ip interface brief", "show vlan brief", "show mac address-table", "show trunk all"], "rep": "show vlan brief", "expl": "La commande 'show vlan brief' affiche les VLANs configurés, leur nom et la liste des interfaces d'accès assignées."}, {"q": "Quel protocole permet d'éviter les boucles de commutation de niveau 2 lors de liaisons redondantes entre switchs ?", "options": ["OSPF", "Spanning Tree Protocol (STP / 802.1D ou RSTP / 802.1w)", "RIPv2", "BGP"], "rep": "Spanning Tree Protocol (STP / 802.1D ou RSTP / 802.1w)", "expl": "STP bloque logiquement les ports redondants pour supprimer les tempêtes de broadcast et les boucles infinies de niveau 2."}, {"q": "Quelle fonctionnalité Cisco permet à un port de passer immédiatement à l'état Forwarding sans attendre les délais STP de 30s ?", "options": ["PortFast", "BPDU Guard", "EtherChannel", "VTP Pruning"], "rep": "PortFast", "expl": "PortFast est destiné exclusivement aux ports connectés à des postes clients (terminaux, serveurs), court-circuitant l'écoute/apprentissage."}, {"q": "Quelle commande restreint la liste des VLANs autorisés sur un Trunk aux VLANs 10 et 30 ?", "options": ["switchport trunk vlan 10,30", "switchport trunk allowed vlan 10,30", "vlan allowed 10 30", "trunk permit 10,30"], "rep": "switchport trunk allowed vlan 10,30", "expl": "La directive 'switchport trunk allowed vlan' filtre les flux autorisés à emprunter la liaison inter-commutateurs."}, {"q": "Sur un commutateur de niveau 3 (Switch L3), qu'est-ce qu'une interface SVI (Switch Virtual Interface) ?", "options": ["Un câble virtuel en fibre optique", "Une interface logique de routage associée à un VLAN (ex: interface vlan 10)", "Un mot de passe de console", "Un port USB de débogage"], "rep": "Une interface logique de routage associée à un VLAN (ex: interface vlan 10)", "expl": "L'interface SVI sert de passerelle par défaut pour tous les hôtes membres de ce VLAN, routant les paquets à la vitesse du silicium (ASIC)."}, {"q": "Quel est le comportement d'un switch quand une trame arrive pour une adresse MAC destination inconnue ?", "options": ["Il détruit la trame immédiatement", "Il diffuse la trame sur tous les ports du même VLAN sauf le port récepteur (Flooding)", "Il envoie une alerte SNMP", "Il redémarre son système d'exploitation"], "rep": "Il diffuse la trame sur tous les ports du même VLAN sauf le port récepteur (Flooding)", "expl": "L'inondation (Unknown Unicast Flooding) permet à la trame d'atteindre le destinataire, dont la réponse permettra au switch d'apprendre son port."}], "4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)": [{"q": "Quel protocole de couche Application sécurise l'administration à distance sur le port TCP 22 ?", "options": ["Telnet", "SSH (Secure Shell)", "RDP", "SNMP"], "rep": "SSH (Secure Shell)", "expl": "SSHv2 chiffre l'ensemble des commandes, mots de passe et transferts de fichiers pour remplacer Telnet non sécurisé."}, {"q": "Dans quel fichier de configuration Linux Debian configure-t-on les paramètres du démon serveur SSH ?", "options": ["/etc/ssh/ssh_config", "/etc/ssh/sshd_config", "/var/log/auth.log", "/etc/hosts.allow"], "rep": "/etc/ssh/sshd_config", "expl": "/etc/ssh/sshd_config gère le démon serveur (sshd), tandis que ssh_config gère le client."}, {"q": "Quelle directive dans /etc/ssh/sshd_config interdit la connexion directe de l'administrateur root ?", "options": ["RootLogin disabled", "PermitRootLogin no", "AllowRoot false", "DenyUser root"], "rep": "PermitRootLogin no", "expl": "Recommandation ANSSI essentielle : désactiver l'accès root direct pour imposer l'authentification par compte individuel et sudo."}, {"q": "Dans un tunnel VPN IPsec, quel protocole assure à la fois le chiffrement, l'authentification et l'intégrité des paquets ?", "options": ["AH (Authentication Header)", "ESP (Encapsulating Security Payload)", "IKEv2", "Diffie-Hellman"], "rep": "ESP (Encapsulating Security Payload)", "expl": "ESP (numéro de protocole IP 50) fournit la confidentialité (chiffrement) et l'intégrité, contrairement à AH qui ne chiffre pas les données."}, {"q": "Quel port standard utilise le protocole HTTPS sécurisé par TLS ?", "options": ["Port 80", "Port 443", "Port 8080", "Port 8443"], "rep": "Port 443", "expl": "HTTPS opère par défaut en TCP sur le port 443."}, {"q": "Dans le protocole IoT MQTT sécurisé (MQTTS), quel port TCP est conventionnellement utilisé sur le Broker ?", "options": ["1883", "8883", "8080", "5683"], "rep": "8883", "expl": "Le port 1883 correspond à MQTT en clair ; le port 8883 correspond à MQTT encapsulé dans une session TLS (MQTTS)."}, {"q": "Dans le protocole TLS 1.3, combien d'allers-retours (Round-Trip Times) sont nécessaires pour établir la négociation de clé de session ?", "options": ["0 ou 1 RTT", "2 RTTs", "3 RTTs", "4 RTTs"], "rep": "0 ou 1 RTT", "expl": "TLS 1.3 accélère la connexion en réalisant la poignée de main en seulement 1 RTT (ou 0-RTT en reprise de session avec PSK)."}, {"q": "Quel composant d'un certificat numérique X.509 atteste de la validité et de l'authenticité de la clé publique présentée ?", "options": ["L'adresse MAC du serveur", "La signature numérique de l'Autorité de Certification (AC / CA)", "Le numéro de série de la carte mère", "Le mot de passe de l'utilisateur"], "rep": "La signature numérique de l'Autorité de Certification (AC / CA)", "expl": "La CA signe le certificat avec sa propre clé privée ; le client vérifie cette signature grâce au magasin de certificats racine de son OS."}, {"q": "Quelle extension d'un certificat TLS permet de protéger plusieurs noms de domaines et sous-domaines (ex: api.ciel.fr, www.ciel.fr) ?", "options": ["SAN (Subject Alternative Name)", "CRL Distribution Point", "Key Usage", "Basic Constraints"], "rep": "SAN (Subject Alternative Name)", "expl": "L'extension SAN liste tous les FQDNs et adresses IP légitimes pour lesquels le certificat est valide."}, {"q": "Quel protocole réseau en ligne remplace avantageusement le téléchargement lourd des listes de révocation de certificats (CRL) ?", "options": ["OCSP (Online Certificate Status Protocol)", "LDAP", "DNSSEC", "NTP"], "rep": "OCSP (Online Certificate Status Protocol)", "expl": "OCSP (et l'agrafage OCSP Stapling) permet de vérifier en temps réel le statut d'un certificat unique sans charger une CRL de plusieurs mégaoctets."}], "1. Cryptographie : Symétrique, Asymétrique & Hachage": [{"q": "Quel algorithme parmi les suivants est un algorithme de chiffrement asymétrique ?", "options": ["AES-256", "RSA", "SHA-256", "DES"], "rep": "RSA", "expl": "RSA est un algorithme asymétrique reposant sur la difficulté de factorisation de grands nombres premiers. AES et DES sont symétriques."}, {"q": "Quelle est la caractéristique fondamentale d'un chiffrement symétrique ?", "options": ["Il utilise une paire de clés publique et privée", "La même clé secrète partagée sert au chiffrement et au déchiffrement", "Il ne peut chiffrer que des chaînes de moins de 128 caractères", "Il est plus lent que le chiffrement asymétrique"], "rep": "La même clé secrète partagée sert au chiffrement et au déchiffrement", "expl": "En cryptographie symétrique (AES, ChaCha20), la même clé doit être conservée secrète par les deux correspondants."}, {"q": "Quelle fonction cryptographique produit une empreinte de taille fixe irréversible (sens unique) à partir de données de taille arbitraire ?", "options": ["Chiffrement par bloc", "Fonction de hachage (ex: SHA-256)", "Stéganographie", "Générateur pseudo-aléatoire"], "rep": "Fonction de hachage (ex: SHA-256)", "expl": "Une fonction de hachage est non inversible et résistante aux collisions, idéale pour vérifier l'intégrité des fichiers."}, {"q": "Quelle clé est utilisée pour créer une signature numérique garantissant l'authenticité et la non-répudiation d'un message ?", "options": ["La clé publique de l'expéditeur", "La clé privée de l'expéditeur", "La clé publique du destinataire", "La clé secrète du serveur"], "rep": "La clé privée de l'expéditeur", "expl": "L'expéditeur signe avec sa clé privée secrète ; n'importe qui peut vérifier la validité de la signature avec sa clé publique."}, {"q": "Quel problème majeur de la cryptographie symétrique l'algorithme d'échange de clés Diffie-Hellman résout-il ?", "options": ["La lenteur des calculs processeur", "L'échange sécurisé d'une clé secrète sur un canal de communication non sécurisé", "La taille des clés qui dépasse 1024 octets", "La détection des coupures de câbles réseau"], "rep": "L'échange sécurisé d'une clé secrète sur un canal de communication non sécurisé", "expl": "Diffie-Hellman permet à deux interlocuteurs de déduire une clé secrète commune sans jamais la faire circuler en clair sur le réseau."}, {"q": "Quelle est la taille en bits de l'empreinte produite par l'algorithme de hachage SHA-256 ?", "options": ["128 bits", "160 bits", "256 bits (32 octets)", "512 bits"], "rep": "256 bits (32 octets)", "expl": "SHA-256 génère une empreinte de 256 bits (64 caractères hexadécimaux)."}, {"q": "Pourquoi les algorithmes de hachage MD5 et SHA-1 sont-ils formellement proscrits par l'ANSSI en production ?", "options": ["Ils ne fonctionnent pas sous Linux", "Des collisions cryptographiques pratiques ont été démontrées", "Leur exécution consomme trop d'électricité", "Ils ont été rachetés par un éditeur propriétaire"], "rep": "Des collisions cryptographiques pratiques ont été démontrées", "expl": "Il est possible de fabriquer deux documents différents produisant la même empreinte MD5 ou SHA-1, ruinant l'intégrité."}, {"q": "En cryptographie asymétrique, avec quelle clé chiffre-t-on un message pour que SEUL le destinataire légitime puisse le déchiffrer ?", "options": ["Avec la clé privée de l'expéditeur", "Avec la clé publique du destinataire", "Avec la clé privée du destinataire", "Avec la clé publique de l'Autorité racine"], "rep": "Avec la clé publique du destinataire", "expl": "On chiffre avec la clé publique du destinataire ; seul ce dernier, détenteur de la clé privée correspondante, peut déchiffrer le texte."}, {"q": "Dans le mode de chiffrement AES-GCM, quel avantage fondamental obtient-on en plus de la confidentialité ?", "options": ["Une compression de données ZIP", "L'authentification et l'intégrité intégrées (AEAD)", "La compatibilité avec les modems 56k", "L'absence de clé de session"], "rep": "L'authentification et l'intégrité intégrées (AEAD)", "expl": "AES-GCM est un mode AEAD (Authenticated Encryption with Associated Data) garantissant à la fois le secret et la non-altération."}, {"q": "Quelle est la taille de clé recommandée par l'ANSSI pour l'algorithme asymétrique RSA au-delà de 2025 ?", "options": ["1024 bits", "2048 bits", "Au moins 3072 bits (ou courbes elliptiques 256 bits)", "512 bits"], "rep": "Au moins 3072 bits (ou courbes elliptiques 256 bits)", "expl": "RSA 2048 bits approche de sa fin de vie recommandée ; l'ANSSI préconise RSA >= 3072 bits ou les courbes elliptiques (ECC 256/384 bits)."}], "2. Top 10 OWASP & Sécurité Applicative": [{"q": "Quelle technique de développement logiciel prévient infailliblement les injections SQL dans les applications web et C++ ?", "options": ["L'utilisation de requêtes préparées avec paramètres liés (Prepared Statements / Bind)", "La conversion des chaînes en majuscules", "L'utilisation exclusive de la méthode HTTP GET", "L'hébergement sur serveur Windows"], "rep": "L'utilisation de requêtes préparées avec paramètres liés (Prepared Statements / Bind)", "expl": "Les requêtes paramétrées séparent rigoureusement le code SQL exécutable des données saisies par l'utilisateur."}, {"q": "Quel type de vulnérabilité web consiste à faire exécuter du code JavaScript malveillant dans le navigateur de la victime ?", "options": ["Injection SQL", "Cross-Site Scripting (XSS)", "Déni de Service (DoS)", "Dépassement de tampon (Buffer Overflow)"], "rep": "Cross-Site Scripting (XSS)", "expl": "Une faille XSS (Reflected, Stored ou DOM-based) injecte des scripts dans les pages consultées pour voler des cookies de session."}, {"q": "Quelle est la mesure de protection indispensable pour neutraliser une vulnérabilité XSS ?", "options": ["Échapper/encoder systématiquement les caractères HTML spéciaux (&lt;, &gt;, &quot;, &amp;) avant affichage", "Désactiver le protocole HTTPS", "Utiliser un mot de passe de plus de 12 caractères", "Supprimer les bases de données SQLite"], "rep": "Échapper/encoder systématiquement les caractères HTML spéciaux (&lt;, &gt;, &quot;, &amp;) avant affichage", "expl": "L'encodage HTML transforme les balises <script> en texte inoffensif (&lt;script&gt;) non interprété par le moteur JavaScript."}, {"q": "Que permet d'empêcher l'attribut de cookie 'HttpOnly' face aux attaques XSS ?", "options": ["Le transit du cookie sur les réseaux Wi-Fi", "L'accès au cookie de session via le code JavaScript (document.cookie)", "L'expiration du cookie après 24 heures", "L'utilisation du protocole HTTP standard"], "rep": "L'accès au cookie de session via le code JavaScript (document.cookie)", "expl": "Même si un pirate réussit une injection XSS, l'attribut HttpOnly empêche son script de lire le cookie de session."}, {"q": "Quel en-tête HTTP de sécurité permet de définir les sources autorisées pour charger des scripts, feuilles de style et images ?", "options": ["X-Frame-Options", "Content-Security-Policy (CSP)", "Strict-Transport-Security (HSTS)", "Access-Control-Allow-Origin"], "rep": "Content-Security-Policy (CSP)", "expl": "La politique CSP bloque l'exécution de scripts inline non autorisés et empêche le chargement de ressources depuis des serveurs tiers suspects."}, {"q": "En quoi consiste l'attaque CSRF (Cross-Site Request Forgery) ?", "options": ["À bloquer les serveurs DNS par inondation de requêtes UDP", "À tromper un utilisateur authentifié pour lui faire exécuter une action non désirée à son insu sur une application de confiance", "À deviner le mot de passe de l'administrateur par dictionnaire", "À intercepter les trames réseau sur le port 80"], "rep": "À tromper un utilisateur authentifié pour lui faire exécuter une action non désirée à son insu sur une application de confiance", "expl": "L'attaque CSRF exploite la confiance qu'un site web accorde au navigateur d'un utilisateur connecté (via ses cookies automatiques)."}, {"q": "Quelle défense neutralise efficacement les attaques de type CSRF ?", "options": ["L'implémentation de jetons aléatoires anti-CSRF (Anti-CSRF Tokens synchronisés) et l'attribut SameSite sur les cookies", "L'augmentation de la RAM du serveur", "Le passage à IPv6", "L'ouverture du port SSH"], "rep": "L'implémentation de jetons aléatoires anti-CSRF (Anti-CSRF Tokens synchronisés) et l'attribut SameSite sur les cookies", "expl": "Un jeton secret unique par formulaire empêche un site malveillant tiers de forger une requête valide."}, {"q": "Quel en-tête HTTP force les navigateurs à communiquer exclusivement en HTTPS avec le site pendant une durée définie ?", "options": ["X-XSS-Protection", "Strict-Transport-Security (HSTS)", "X-Content-Type-Options", "Referrer-Policy"], "rep": "Strict-Transport-Security (HSTS)", "expl": "HSTS interdit tout repli non chiffré en HTTP (attaques SSL Stripping)."}, {"q": "Dans l'OWASP Top 10, que désigne la faille 'Security Misconfiguration' (Mauvaise configuration de sécurité) ?", "options": ["Un câble Ethernet débranché", "L'utilisation de comptes et mots de passe par défaut, de messages d'erreur verbeux avec stack traces, ou de services inutiles activés", "Une panne de disque dur", "L'absence de licence commerciale"], "rep": "L'utilisation de comptes et mots de passe par défaut, de messages d'erreur verbeux avec stack traces, ou de services inutiles activés", "expl": "Laisser 'admin/admin', les pages de debug actives ou des ports non utilisés expose le système à des intrusions immédiates."}, {"q": "Comment doit-on stocker les mots de passe des utilisateurs dans une base de données sécurisée ?", "options": ["En clair pour pouvoir les renvoyer en cas d'oubli", "Chiffrés en symétrique avec AES-128", "Hachés avec un sel cryptographique unique à l'aide d'un algorithme robuste (Argon2, bcrypt ou PBKDF2)", "Compressés avec l'algorithme ZIP"], "rep": "Hachés avec un sel cryptographique unique à l'aide d'un algorithme robuste (Argon2, bcrypt ou PBKDF2)", "expl": "Le salage aléatoire empêche l'utilisation de tables arc-en-ciel (Rainbow Tables), et la lenteur voulue d'Argon2/bcrypt bloque les attaques par force brute."}], "1. Langage C++ : Mémoire, Pointeurs & POO": [{"q": "En C++, où sont allouées les variables dynamiques créées avec l'opérateur 'new' ?", "options": ["Sur la Pile (Stack)", "Sur le Tas (Heap / Mémoire dynamique)", "Dans le registre processeur", "Dans la mémoire morte ROM"], "rep": "Sur le Tas (Heap / Mémoire dynamique)", "expl": "L'opérateur 'new' alloue de la mémoire sur le Tas, dont la durée de vie persiste jusqu'à un appel explicite à 'delete'."}, {"q": "Quelle instruction libère correctement un tableau dynamique alloué par 'int* t = new int[50];' ?", "options": ["delete t;", "delete[] t;", "free(t);", "remove t;"], "rep": "delete[] t;", "expl": "Pour les tableaux alloués avec new[], il faut obligatoirement utiliser 'delete[]' pour appeler les destructeurs de chaque élément et éviter les fuites."}, {"q": "Qu'est-ce qu'une méthode virtuelle pure en C++ ?", "options": ["Une méthode déclarée avec la syntaxe 'virtual void action() = 0;'", "Une méthode statique qui ne prend aucun paramètre", "Une méthode privée sans corps de code", "Une fonction inline"], "rep": "Une méthode déclarée avec la syntaxe 'virtual void action() = 0;'", "expl": "Une méthode virtuelle pure n'a pas d'implémentation dans la classe de base et rend la classe abstraite."}, {"q": "Pourquoi doit-on déclarer le destructeur d'une classe de base 'virtual' dès qu'elle possède des méthodes virtuelles ?", "options": ["Pour accélérer le programme", "Pour garantir que le destructeur de la classe dérivée soit appelé lors de la suppression d'un objet via un pointeur de base", "C'est une obligation du compilateur pour compiler en 64 bits", "Pour rendre la mémoire accessible en lecture seule"], "rep": "Pour garantir que le destructeur de la classe dérivée soit appelé lors de la suppression d'un objet via un pointeur de base", "expl": "Sans destructeur virtuel, seul le destructeur de base serait exécuté, laissant les ressources de la classe dérivée non libérées (fuite mémoire)."}, {"q": "Quel pointeur intelligent standard de C++11 assure la propriété exclusive d'une ressource sans surcoût de compteur de références ?", "options": ["std::shared_ptr", "std::unique_ptr", "std::weak_ptr", "std::auto_ptr"], "rep": "std::unique_ptr", "expl": "std::unique_ptr gère la destruction automatique dès la sortie de portée et ne peut pas être copié (uniquement déplacé avec std::move)."}, {"q": "Que garantit le mot-clé 'const' placé à la fin d'une méthode (ex: float getVitesse() const;) ?", "options": ["Que la méthode ne modifie aucun attribut de l'objet sur lequel elle est invoquée", "Que la méthode s'exécute en un temps constant de 1 ms", "Que la valeur retournée ne peut pas être négative", "Que la méthode ne peut être appelée qu'une seule fois"], "rep": "Que la méthode ne modifie aucun attribut de l'objet sur lequel elle est invoquée", "expl": "Les accesseurs (Getters) doivent être qualifiés 'const' pour pouvoir être appelés sur des instances constantes et sécuriser l'encapsulation."}, {"q": "Quelle est la différence fondamentale entre le passage d'argument par valeur et le passage par référence constante (const Type&) ?", "options": ["Le passage par valeur est toujours plus rapide", "Le passage par référence évite une copie mémoire lourde de l'objet tout en interdisant sa modification", "Le passage par référence modifie toujours l'original", "Le compilateur interdit les références en C++"], "rep": "Le passage par référence évite une copie mémoire lourde de l'objet tout en interdisant sa modification", "expl": "Passer un objet lourd (std::string, objet métier) par 'const Type&' évite de dupliquer les octets en mémoire tout en garantissant sa protection."}, {"q": "Quel mot-clé de C++11 place-t-on après la signature d'une méthode dérivée pour demander au compilateur de vérifier qu'elle redéfinit bien une méthode virtuelle mère ?", "options": ["virtual", "override", "final", "redef"], "rep": "override", "expl": "Le spécificateur 'override' déclenche une erreur de compilation si la signature ne correspond pas exactement à une méthode virtuelle de la classe parente."}, {"q": "Dans quel ordre s'exécutent les constructeurs lors de l'instanciation d'une classe dérivée ?", "options": ["D'abord le constructeur de la classe dérivée, puis celui de la classe mère", "D'abord le constructeur de la classe mère, puis celui de la classe dérivée", "Ils s'exécutent simultanément en multi-thread", "L'ordre est indéterminé"], "rep": "D'abord le constructeur de la classe mère, puis celui de la classe dérivée", "expl": "La classe de base doit être initialisée et valide avant que la classe fille ne construise ses propres attributs spécifiques."}, {"q": "Que contient une variable de type pointeur (ex: int* ptr) ?", "options": ["Une valeur entière comprise entre -32768 et 32767", "L'adresse mémoire d'une autre variable en mémoire vive", "Une chaîne de caractères", "Le code assembleur de la fonction main"], "rep": "L'adresse mémoire d'une autre variable en mémoire vive", "expl": "Un pointeur stocke l'adresse octet d'une zone mémoire ; l'opérateur d'indirection '*' permet d'accéder à la valeur stockée à cette adresse."}], "3. Structures de données avancées & Unions en Langage C": [{"q": "En langage C, quelle est la particularité mémoire d'une 'union' par rapport à une 'struct' ?", "options": ["Une union alloue de la mémoire pour chaque membre séparément", "Tous les membres d'une union partagent le même espace mémoire physique (taille égale au plus grand membre)", "Une union ne peut contenir que des entiers", "Une union est stockée uniquement sur disque dur"], "rep": "Tous les membres d'une union partagent le même espace mémoire physique (taille égale au plus grand membre)", "expl": "Dans une union, modifier un membre écrase la mémoire des autres membres, ce qui est idéal pour manipuler des registres ou décoder des trames brutes."}, {"q": "Si une union C contient un 'char c' (1 octet) et un 'int i' (4 octets), quelle sera sa taille totale en mémoire ?", "options": ["1 octet", "4 octets", "5 octets", "8 octets"], "rep": "4 octets", "expl": "La taille d'une union est au moins égale à la taille de son plus grand membre (ici l'entier de 4 octets)."}, {"q": "Quelle directive préprocesseur permet de forcer le compilateur à supprimer les octets de rembourrage (padding) dans une structure de trame réseau ?", "options": ["#pragma pack(1) ou __attribute__((packed))", "#define NO_PADDING", "#include <netinet/in.h>", "#pragma fast"], "rep": "#pragma pack(1) ou __attribute__((packed))", "expl": "L'alignement par défaut sur 32 ou 64 bits insère des octets vides ; 'packed' aligne octet par octet pour correspondre exactement aux trames réseau."}, {"q": "Quel opérateur utilise-t-on en C pour accéder à un membre d'une structure à travers un pointeur (ex: struct Capteur* ptr;) ?", "options": [". (point)", "-> (flèche)", ":: (double deux-points)", "# (dièse)"], "rep": "-> (flèche)", "expl": "L'opérateur flèche '->' combine l'opération de déréférencement et d'accès au membre : 'ptr->valeur' équivaut à '(*ptr).valeur'."}, {"q": "Dans une structure de données de type 'Liste Chaînée Simple', que contient chaque nœud en plus de sa charge utile ?", "options": ["L'adresse IP du serveur", "Un pointeur vers le nœud suivant de la liste (ex: struct Node* next;)", "Un entier représentant le nombre total d'éléments", "Une table de hachage"], "rep": "Un pointeur vers le nœud suivant de la liste (ex: struct Node* next;)", "expl": "Chaque maillon pointe vers le suivant ; le dernier élément pointe vers NULL pour marquer la fin de la chaîne."}, {"q": "En langage C, quelle fonction de la bibliothèque standard libère un bloc de mémoire alloué avec malloc() ?", "options": ["delete()", "free()", "release()", "dispose()"], "rep": "free()", "expl": "La fonction 'free(ptr)' restitue la mémoire dynamique au gestionnaire du système d'exploitation."}, {"q": "Que retourne la fonction 'sizeof(struct MonType)' en C ?", "options": ["Le nombre de variables déclarées dans le fichier", "La taille occupée en octets par la structure en mémoire", "Le temps d'exécution de la structure en microsecondes", "L'adresse mémoire du premier membre"], "rep": "La taille occupée en octets par la structure en mémoire", "expl": "L'opérateur 'sizeof' est évalué à la compilation et fournit le nombre total d'octets requis par le type."}, {"q": "Comment qualifie-t-on un champ de structure C dont on spécifie explicitement la largeur en bits (ex: unsigned int flag : 1;) ?", "options": ["Un champ de bits (Bit-field)", "Un pointeur nul", "Une variable flottante", "Un registre statique"], "rep": "Un champ de bits (Bit-field)", "expl": "Les champs de bits permettent de mapper précisément les bits individuels de drapeaux (Flags) d'un en-tête matériel ou protocolaire."}, {"q": "Quelle erreur critique survient si l'on tente d'accéder à la mémoire pointée par un pointeur contenant l'adresse NULL ?", "options": ["Un ralentissement du réseau", "Une faute de segmentation (Segmentation Fault / Signal SIGSEGV)", "Une augmentation de la tension électrique", "Une alerte sonore de la carte mère"], "rep": "Une faute de segmentation (Segmentation Fault / Signal SIGSEGV)", "expl": "Déréférencer un pointeur NULL (adresse 0x0) est une violation d'accès mémoire protégée par le système d'exploitation."}, {"q": "Dans une union mixte permettant de convertir un entier 16 bits en 2 octets séparés (MSB et LSB), qu'est-ce qui conditionne l'ordre des octets en mémoire ?", "options": ["Le protocole DHCP", "L'Endianness de l'architecture du processeur (Little-Endian vs Big-Endian)", "La vitesse de la liaison série", "La version du langage C"], "rep": "L'Endianness de l'architecture du processeur (Little-Endian vs Big-Endian)", "expl": "Sur x86/ARM (Little-Endian), l'octet de poids faible (LSB) est stocké à l'adresse mémoire la plus basse ; en réseau (Big-Endian), c'est le MSB en premier."}], "1. Échantillonnage, CAN/CNA & Théorème de Shannon": [{"q": "Selon le théorème de Nyquist-Shannon, quelle condition doit respecter la fréquence d'échantillonnage Fe pour numériser sans repliement spectral un signal de fréquence maximale Fmax ?", "options": ["Fe <= Fmax", "Fe >= 2 * Fmax", "Fe = Fmax / 2", "Fe >= 10 * Fmax"], "rep": "Fe >= 2 * Fmax", "expl": "Fe doit être au moins le double de la fréquence maximale contenue dans le spectre (Fe >= 2*Fmax) pour éviter le repliement de spectre (Aliasing)."}, {"q": "Quelle est la formule du quantum q d'un convertisseur analogique-numérique (CAN) à n bits pour une plage de pleine échelle Vref ?", "options": ["q = Vref / n", "q = Vref / (2^n - 1)  (ou approx Vref / 2^n)", "q = Vref * 2^n", "q = 2^n / Vref"], "rep": "q = Vref / (2^n - 1)  (ou approx Vref / 2^n)", "expl": "Le quantum q est la plus petite variation de tension analogique détectable correspondant à un incrément d'un bit de poids faible (LSB)."}, {"q": "Pour un CAN 12 bits alimenté sous Vref = 5,0 V, quelle est la valeur approximative du quantum q ?", "options": ["4,88 mV", "1,22 mV", "0,61 mV", "19,5 mV"], "rep": "1,22 mV", "expl": "q = 5,0 / (2^12 - 1) = 5,0 / 4095 = 0,001221 V = 1,22 mV."}, {"q": "Quel filtre analogique doit-on impérativement placer AVANT l'entrée d'un CAN pour respecter la condition de Shannon ?", "options": ["Un filtre passe-haut", "Un filtre passe-bas anti-repliement (Anti-Aliasing Filter)", "Un filtre réjecteur de bande 50 Hz", "Un amplificateur logarithmique"], "rep": "Un filtre passe-bas anti-repliement (Anti-Aliasing Filter)", "expl": "Le filtre anti-repliement élimine toutes les composantes fréquentielles supérieures à Fe/2 pour empêcher la corruption du signal numérisé."}, {"q": "Quelle valeur numérique entière N (code brut) est générée par un CAN 10 bits (Vref = 5,0 V) pour une tension d'entrée Ve = 2,5 V ?", "options": ["256", "512", "1024", "128"], "rep": "512", "expl": "Pour une tension égale à la moitié de Vref (2,5V / 5,0V), le code vaut la moitié de l'échelle maximale (1023 / 2 = 511,5 -> arrondi à 511 ou 512)."}, {"q": "Combien de niveaux de quantification distincts offre un convertisseur numérique-analogique (CNA) de résolution 8 bits ?", "options": ["8 niveaux", "16 niveaux", "128 niveaux", "256 niveaux (de 0 à 255)"], "rep": "256 niveaux (de 0 à 255)", "expl": "2^8 = 256 niveaux discrets possibles."}, {"q": "Dans un circuit échantillonneur-bloqueur (Sample & Hold), quel composant passif mémorise la tension pendant la durée de conversion du CAN ?", "options": ["Une inductance", "Un condensateur de maintien", "Une résistance de tirage", "Une diode Zener"], "rep": "Un condensateur de maintien", "expl": "L'interrupteur analogique charge le condensateur de maintien (Hold Capacitor) qui fige la tension pendant que le CAN quantifie la valeur."}, {"q": "Si un signal audio contient des fréquences jusqu'à 20 kHz, quelle est la fréquence d'échantillonnage minimale théorique selon Shannon ?", "options": ["10 kHz", "20 kHz", "40 kHz", "44,1 kHz"], "rep": "40 kHz", "expl": "2 * 20 kHz = 40 kHz. (Dans l'industrie du CD audio, on utilise 44,1 kHz pour ménager une bande de transition pour les filtres réels)."}, {"q": "Comment évolue le rapport signal sur bruit de quantification théorique (SNR) lorsqu'on augmente la résolution d'un CAN d'un bit supplémentaire ?", "options": ["Il diminue de 3 dB", "Il augmente d'environ 6,02 dB par bit supplémentaire", "Il reste constant", "Il est multiplié par 10"], "rep": "Il augmente d'environ 6,02 dB par bit supplémentaire", "expl": "La formule théorique est SNR = 6,02 * n + 1,76 dB. Chaque bit gagné divise le pas de bruit par 2, apportant +6 dB de dynamique."}, {"q": "Qu'est-ce que l'erreur de non-linéarité différentielle (DNL) d'un CAN ?", "options": ["L'erreur de dérive en température de la carte mère", "L'écart entre la largeur réelle d'un échelon de quantification et la valeur idéale du quantum q", "Le retard de propagation de l'horloge SPI", "L'erreur de décalage à l'origine (Offset)"], "rep": "L'écart entre la largeur réelle d'un échelon de quantification et la valeur idéale du quantum q", "expl": "Une DNL supérieure à 1 LSB peut provoquer des codes manquants (Missing Codes), altérant la fidélité de conversion."}], "4. Lois Fondamentales d'Électricité & Composants Passifs": [{"q": "Quelle est l'expression mathématique de la loi d'Ohm pour un dipôle récepteur linéaire de résistance R ?", "options": ["U = R * I", "I = R * U", "P = U / R", "U = R / I"], "rep": "U = R * I", "expl": "La tension U en Volts est égale au produit de la résistance R en Ohms par l'intensité I en Ampères."}, {"q": "Quelle est la formule de la résistance équivalente Req de deux résistances R1 et R2 connectées en parallèle ?", "options": ["Req = R1 + R2", "Req = (R1 * R2) / (R1 + R2)", "Req = (R1 + R2) / (R1 * R2)", "Req = R1 - R2"], "rep": "Req = (R1 * R2) / (R1 + R2)", "expl": "1/Req = 1/R1 + 1/R2, ce qui donne Req = (R1 * R2) / (R1 + R2). La résistance résultante est toujours inférieure à la plus petite des deux."}, {"q": "Dans un circuit comprenant deux résistances R1 et R2 en série alimentées par une tension E, quelle est la formule du pont diviseur de tension aux bornes de R2 ?", "options": ["U2 = E * (R1 / (R1 + R2))", "U2 = E * (R2 / (R1 + R2))", "U2 = E * (R1 + R2) / R2", "U2 = E / (R1 * R2)"], "rep": "U2 = E * (R2 / (R1 + R2))", "expl": "La tension se répartit proportionnellement à la valeur de chaque résistance de la branche série."}, {"q": "Quelle est la puissance dissipée par effet Joule dans une résistance R traversée par un courant I ?", "options": ["P = R * I", "P = R * I^2 = U^2 / R = U * I", "P = U / I", "P = R^2 * I"], "rep": "P = R * I^2 = U^2 / R = U * I", "expl": "La puissance s'exprime en Watts (W) selon la relation P = U * I = R * I^2 = U^2 / R."}, {"q": "Quelle est la relation fondamentale entre la charge électrique Q (en Coulombs) et la tension U aux bornes d'un condensateur de capacité C ?", "options": ["Q = C * U", "U = C * Q", "C = Q * U", "Q = C / U"], "rep": "Q = C * U", "expl": "La charge stockée Q = C * U, et l'intensité instantanée vaut i(t) = C * du/dt."}, {"q": "Quelle est l'expression de la constante de temps tau d'un circuit RC série ?", "options": ["tau = R / C", "tau = R * C", "tau = 1 / (R * C)", "tau = 2 * pi * R * C"], "rep": "tau = R * C", "expl": "tau = R * C s'exprime en secondes (Ohms * Farads = secondes)."}, {"q": "Au bout d'une durée égale à 1 constante de temps (t = tau), à quel pourcentage de la tension finale E un condensateur est-il chargé ?", "options": ["50 %", "63,2 %", "95 %", "99 %"], "rep": "63,2 %", "expl": "u_C(tau) = E * (1 - e^-1) = E * (1 - 0,368) = 0,632 * E (soit 63,2 %). À t = 3*tau on atteint 95 %, et à t = 5*tau la charge est considérée terminée (99,3 %)."}, {"q": "Quelle est la quantité d'énergie électrique Ec emmagasinée dans un condensateur de capacité C sous une tension U ?", "options": ["Ec = C * U", "Ec = 1/2 * C * U^2", "Ec = C * U^2", "Ec = 1/2 * C^2 * U"], "rep": "Ec = 1/2 * C * U^2", "expl": "L'énergie stockée dans le champ électrostatique s'exprime en Joules (J) selon Ec = 1/2 * C * U^2."}, {"q": "Que stipule la loi des mailles de Kirchhoff dans un circuit électrique fermé orienté ?", "options": ["La somme algébrique des différences de potentiel le long d'une maille fermée est nulle", "Le courant entrant est égal au courant sortant", "La tension totale est toujours égale à 230V", "Toutes les résistances s'additionnent"], "rep": "La somme algébrique des différences de potentiel le long d'une maille fermée est nulle", "expl": "Somme(U_k) = 0 le long de n'importe quel circuit fermé d'un réseau électrique."}, {"q": "Comment se comporte un condensateur parfait lorsqu'il est soumis à un régime continu permanent stabilisé depuis longtemps ?", "options": ["Comme un court-circuit (fil conducteur)", "Comme un circuit ouvert (interrupteur ouvert, courant nul)", "Comme une résistance de 50 Ohms", "Comme un générateur de tension autonome"], "rep": "Comme un circuit ouvert (interrupteur ouvert, courant nul)", "expl": "En régime continu, la dérivée du/dt est nulle, donc le courant i = C*du/dt est nul : le condensateur se comporte en circuit ouvert."}], "5. Protocoles Industriels & Bus de terrain (Modbus, Profibus)": [{"q": "Quel type de liaison physique différentielle est couramment utilisé comme support de transmission pour le protocole Modbus RTU en milieu industriel ?", "options": ["Liaison asymétrique RS-232", "Liaison différentielle RS-485 sur paire torsadée blindée", "Câble HDMI", "Câble ruban nappe IDE"], "rep": "Liaison différentielle RS-485 sur paire torsadée blindée", "expl": "La norme RS-485 utilise deux lignes différentielles (A et B ou D+ et D-) insensibles aux bruits de mode commun industriels."}, {"q": "Quelle valeur de résistance de terminaison normalisée doit-on placer à chaque extrémité d'un bus RS-485 ou CAN pour adapter l'impédance de ligne ?", "options": ["10 kOhms", "120 Ohms", "1 kOhm", "4,7 kOhms"], "rep": "120 Ohms", "expl": "Les résistances de terminaison de 120 Ohms adaptent la ligne à son impédance caractéristique et suppriment les réflexions d'ondes aux extrémités."}, {"q": "Dans le protocole Modbus RTU, quel mécanisme de contrôle d'erreur sur 2 octets termine chaque trame ?", "options": ["Un bit de parité simple", "Un contrôle de redondance cyclique CRC-16", "Une somme Checksum 8 bits", "Un hachage SHA-1"], "rep": "Un contrôle de redondance cyclique CRC-16", "expl": "Modbus RTU calcule un polynôme CRC-16 envoyé en fin de trame (Low byte puis High byte)."}, {"q": "Quel code fonction Modbus standard permet de lire un ou plusieurs registres de maintien (Read Holding Registers 16 bits) ?", "options": ["Fonction 01", "Fonction 03", "Fonction 06", "Fonction 16"], "rep": "Fonction 03", "expl": "La fonction 03 lit les Holding Registers (mots de 16 bits). La fonction 06 écrit un seul mot et la fonction 16 (0x10) écrit plusieurs mots."}, {"q": "Dans une trame Modbus RTU, comment les récepteurs esclaves détectent-ils la fin d'une trame ou le début d'une nouvelle trame ?", "options": ["Par un caractère ASCII spécial <CR><LF>", "Par un silence sur la ligne (absence de transmission) d'au moins 3,5 temps caractères (3.5 char times)", "Par un signal d'interruption sur un fil dédié", "Par un paquet d'acquittement ACK"], "rep": "Par un silence sur la ligne (absence de transmission) d'au moins 3,5 temps caractères (3.5 char times)", "expl": "Le protocole Modbus RTU est délimité par des intervalles de silence d'au moins 3,5 fois la durée d'un caractère (T3.5)."}, {"q": "Quelle est la plage d'adresses d'esclaves valides sur un réseau Modbus (l'adresse 0 étant réservée au Broadcast) ?", "options": ["De 1 à 16", "De 1 à 127", "De 1 à 247", "De 1 à 1024"], "rep": "De 1 à 247", "expl": "Les adresses d'esclaves Modbus s'étendent de 1 à 247. Les adresses 248 à 255 sont réservées."}, {"q": "Sur le bus CAN automobile et industriel, comment résout-on les collisions lorsque deux nœuds émettent simultanément sur le bus ?", "options": ["Par l'algorithme CSMA/CD comme Ethernet avec attente aléatoire", "Par arbitrage bit-à-bit non destructif (CSMA/CR) où l'identifiant le plus bas (bit dominant 0) gagne la priorité", "Le nœud maître coupe le signal du nœud esclave", "Les deux trames sont détruites et redemandées"], "rep": "Par arbitrage bit-à-bit non destructif (CSMA/CR) où l'identifiant le plus bas (bit dominant 0) gagne la priorité", "expl": "Le niveau 0 est dominant sur le bus CAN : le message ayant l'ID numérique le plus petit écrase les 1 récessifs sans interrompre sa transmission."}, {"q": "Sur un bus I2C, quel est le rôle des deux lignes de communication bidirectionnelles SDA et SCL ?", "options": ["SDA pour l'alimentation 12V, SCL pour la terre", "SDA pour les Données (Serial Data), SCL pour l'Horloge (Serial Clock)", "SDA pour l'émission, SCL pour la réception", "SDA pour le reset, SCL pour l'interruption"], "rep": "SDA pour les Données (Serial Data), SCL pour l'Horloge (Serial Clock)", "expl": "L'I2C utilise 2 lignes à collecteur ouvert nécessitant des résistances de tirage au +Vcc (Pull-up typique 4,7 kOhms)."}, {"q": "Combien de lignes physiques de signaux maîtres-esclaves utilise une liaison synchrone SPI standard ?", "options": ["1 ligne", "2 lignes", "4 lignes (MOSI, MISO, SCK, CS / SS)", "8 lignes"], "rep": "4 lignes (MOSI, MISO, SCK, CS / SS)", "expl": "Master Out Slave In (MOSI), Master In Slave Out (MISO), Serial Clock (SCK) et Chip Select (CS/SS)."}, {"q": "Dans une liaison série UART, que signifie la configuration standard '9600 8N1' ?", "options": ["9600 octets par seconde, 8 bits de stop, pas de données", "Vitesse 9600 Bauds, 8 bits de données, Pas de parité (None), 1 bit de Stop", "9600 MHz, 8 trames, 1 bit de parité", "Adresse IP 9600 sur port 8N1"], "rep": "Vitesse 9600 Bauds, 8 bits de données, Pas de parité (None), 1 bit de Stop", "expl": "8N1 est le format de cadrage asynchrone le plus classique en électronique et télémesure."}], "6. Transmission optique (Fibres optiques Monomodes & Multimodes)": [{"q": "Sur quel principe physique fondamental de réfraction et réflexion des ondes repose le guidage de la lumière dans le cœur d'une fibre optique ?", "options": ["La diffraction de Fraunhofer", "La réflexion totale interne à l'interface cœur-gaine selon les lois de Snell-Descartes", "L'effet photoélectrique", "La polarisation circulaire"], "rep": "La réflexion totale interne à l'interface cœur-gaine selon les lois de Snell-Descartes", "expl": "La réflexion totale interne exige que l'indice de réfraction du cœur (n1) soit strictement supérieur à l'indice de réfraction de la gaine (n2)."}, {"q": "Quelle condition sur les indices de réfraction du cœur n1 et de la gaine n2 est indispensable pour assurer le guidage optique ?", "options": ["n1 < n2", "n1 > n2", "n1 = n2", "n1 * n2 = 1"], "rep": "n1 > n2", "expl": "Si n1 n'était pas supérieur à n2, le faisceau lumineux serait réfracté vers l'extérieur et s'échapperait dans la gaine."}, {"q": "Quel est le diamètre standard du cœur d'une fibre optique Monomode (SMF - Single Mode Fiber) ?", "options": ["9 micromètres", "50 micromètres", "62,5 micromètres", "1 millimètre"], "rep": "9 micromètres", "expl": "La fibre monomode possède un cœur très étroit (~9 µm) pour une gaine de 125 µm, ce qui ne laisse propager qu'un seul mode électromagnétique fondamental."}, {"q": "Quelle est la principale source de dégradation de la bande passante sur de longues distances dans une fibre optique Multimode ?", "options": ["La dispersion intermodale (différence de temps de parcours entre les différents trajets de rayons)", "La corrosion du verre", "L'échauffement thermique des photons", "La gravité terrestre"], "rep": "La dispersion intermodale (différence de temps de parcours entre les différents trajets de rayons)", "expl": "Dans une fibre multimode, les rayons parcourent des trajets de longueurs différentes, ce qui élargit l'impulsion lumineuse et limite le débit sur longue distance."}, {"q": "Quelle source lumineuse semi-conductrice monochromatique et directive utilise-t-on pour injecter le signal dans une fibre Monomode ?", "options": ["Une diode électroluminescente (LED)", "Une diode Laser (Laser Diode / DFB)", "Une lampe halogène", "Un néon"], "rep": "Une diode Laser (Laser Diode / DFB)", "expl": "Le cœur très étroit de 9 µm requiert la finesse spectrale et la directivité d'une diode Laser."}, {"q": "Quelles sont les longueurs d'onde standards utilisées pour les transmissions sur fibre optique Monomode dans les réseaux métropolitains et WAN ?", "options": ["850 nm", "1310 nm et 1550 nm (fenêtres de moindre atténuation)", "650 nm (lumière rouge visible)", "2,4 GHz"], "rep": "1310 nm et 1550 nm (fenêtres de moindre atténuation)", "expl": "1310 nm correspond à la dispersion chromatique nulle de la silice, et 1550 nm correspond au minimum d'atténuation optique (~0,2 dB/km)."}, {"q": "Comment calcule-t-on l'atténuation A en décibels (dB) d'une liaison optique connaissant la puissance d'entrée P_in et la puissance de sortie P_out ?", "options": ["A = P_in - P_out", "A = 10 * log10(P_in / P_out)", "A = 20 * ln(P_out / P_in)", "A = (P_in * P_out) / 2"], "rep": "A = 10 * log10(P_in / P_out)", "expl": "Pour les puissances, l'atténuation en dB s'exprime par A = 10 * log10(P_in / P_out)."}, {"q": "Si un signal optique subit une atténuation de 3 dB le long d'une fibre, quelle fraction de sa puissance initiale parvient au récepteur ?", "options": ["90 %", "50 % (la puissance est divisée par deux)", "25 %", "10 %"], "rep": "50 % (la puissance est divisée par deux)", "expl": "10 * log10(0,5) = -3,01 dB. Une atténuation de 3 dB correspond exactement à une division par deux de la puissance lumineuse."}, {"q": "Quel équipement de mesure optique professionnel envoie des impulsions lumineuses pour cartographier les défauts, soudures et épissures le long de la fibre ?", "options": ["Un multimètre numérique", "Un réflectomètre optique temporel (OTDR)", "Un oscilloscope analogique", "Un analyseur de spectre radio"], "rep": "Un réflectomètre optique temporel (OTDR)", "expl": "L'OTDR analyse la rétrodiffusion Rayleigh et les réflexions de Fresnel pour localiser au mètre près les ruptures ou atténuations anormales."}, {"q": "Quel type de connecteur optique dispose d'une férule polie avec un angle de 8 degrés pour réduire la réflectance (Return Loss) ?", "options": ["Connecteur PC (Physical Contact)", "Connecteur UPC (Ultra Physical Contact)", "Connecteur APC (Angled Physical Contact - couleur verte)", "Connecteur RJ-45"], "rep": "Connecteur APC (Angled Physical Contact - couleur verte)", "expl": "Les connecteurs APC (verts) sont biseautés à 8°, déviant la lumière réfléchie vers la gaine pour atteindre un affaiblissement de réflexion > 60 dB."}], "2. Services Active Directory & GPO (Windows Server)": [{"q": "Dans quel ordre hiérarchique s'appliquent les stratégies de groupe (GPO) dans un domaine Active Directory Windows Server ?", "options": ["Domaine -> Site -> OU -> Local", "LSDOU : Local -> Site -> Domaine -> Unité d'Organisation (OU)", "OU -> Domaine -> Site -> Local", "Aléatoire selon la charge processeur"], "rep": "LSDOU : Local -> Site -> Domaine -> Unité d'Organisation (OU)", "expl": "L'ordre LSDOU permet aux règles les plus spécifiques (placées sur les OU) de prévaloir sur les règles globales héritées du domaine."}, {"q": "Quelle commande en ligne de commande ou PowerShell force l'actualisation immédiate des GPO sur un poste client Windows ?", "options": ["gprefresh /now", "gpupdate /force", "net stop gpo && net start gpo", "dsmod gpo -apply"], "rep": "gpupdate /force", "expl": "La commande 'gpupdate /force' contacte le contrôleur de domaine pour réappliquer immédiatement les stratégies ordinateurs et utilisateurs."}, {"q": "Quel protocole d'authentification réseau à base de tickets (Ticket Granting Ticket) utilise nativement un domaine Active Directory ?", "options": ["NTLMv1", "Kerberos (port TCP/UDP 88)", "RADIUS", "PAP"], "rep": "Kerberos (port TCP/UDP 88)", "expl": "Kerberos s'appuie sur le KDC (Key Distribution Center) du contrôleur de domaine pour délivrer des tickets chiffrés TGT évitant la transmission de mots de passe."}, {"q": "Quel protocole d'annuaire interroge et modifie les objets de la base Active Directory (utilisateurs, groupes, ordinateurs) ?", "options": ["HTTP", "LDAP (port 389) et LDAPS sécurisé (port 636)", "SMTP", "SNMP"], "rep": "LDAP (port 389) et LDAPS sécurisé (port 636)", "expl": "LDAP (Lightweight Directory Access Protocol) structure la hiérarchie des objets via des noms distingués (DN: CN=..., OU=..., DC=...)."}, {"q": "Dans le modèle de durcissement Active Directory (Tiering Model de l'ANSSI), qu'est-ce que le 'Tier 0' ?", "options": ["Les postes de travail des stagiaires", "Les imprimantes réseau", "Le plan de contrôle le plus sensible (Contrôleurs de domaine, comptes Admins du Domaine, PKI)", "Les serveurs d'impression bureautique"], "rep": "Le plan de contrôle le plus sensible (Contrôleurs de domaine, comptes Admins du Domaine, PKI)", "expl": "Le Tier 0 regroupe tous les systèmes capables de compromettre l'ensemble de la forêt AD ; les administrateurs T0 ne doivent jamais se connecter sur un poste T1 ou T2."}, {"q": "Quelle solution logicielle gratuite de Microsoft génère un mot de passe administrateur local unique, aléatoire et renouvelé pour chaque machine du parc ?", "options": ["LAPS (Local Administrator Password Solution)", "BitLocker", "Windows Defender", "Sysinternals"], "rep": "LAPS (Local Administrator Password Solution)", "expl": "LAPS stocke le mot de passe de chaque compte administrateur local dans un attribut sécurisé de l'ordinateur dans Active Directory, bloquant les attaques Pass-the-Hash."}, {"q": "Quelle commande PowerShell permet de créer un nouveau compte utilisateur dans l'Unité d'Organisation 'Informatique' ?", "options": ["Add-User -Name 'Alice'", "New-ADUser -Name 'Alice' -Path 'OU=Informatique,DC=ciel,DC=local' -AccountPassword ... -Enabled $true", "Create-DomainAccount 'Alice'", "Set-ADUser 'Alice' -Create"], "rep": "New-ADUser -Name 'Alice' -Path 'OU=Informatique,DC=ciel,DC=local' -AccountPassword ... -Enabled $true", "expl": "Le module ActiveDirectory de PowerShell standardise la création d'objets avec New-ADUser, New-ADGroup, New-ADOrganizationalUnit."}, {"q": "Quel enregistrement DNS de type SRV est indispensable pour que les postes de travail localisent les contrôleurs de domaine lors de l'ouverture de session ?", "options": ["_ldap._tcp.dc._msdcs.domaine.local", "mail.domaine.local", "ftp.domaine.local", "router.domaine.local"], "rep": "_ldap._tcp.dc._msdcs.domaine.local", "expl": "Les enregistrements SRV dans la zone DNS interne associent le service LDAP et Kerberos aux adresses IP des contrôleurs de domaine."}, {"q": "Que permet la corbeille Active Directory (Active Directory Recycle Bin) lorsqu'elle est activée ?", "options": ["De vider les journaux d'événements du serveur", "De restaurer un objet supprimé par erreur avec l'intégralité de ses attributs et appartenances de groupes sans restaurer de sauvegarde complète", "D'économiser de l'espace sur le disque C:", "De bloquer les virus"], "rep": "De restaurer un objet supprimé par erreur avec l'intégralité de ses attributs et appartenances de groupes sans restaurer de sauvegarde complète", "expl": "La corbeille AD restaure immédiatement un utilisateur ou une OU via 'Restore-ADObject' sans redémarrer le serveur en mode DSRM."}, {"q": "Dans une GPO, quelle est la conséquence de l'activation de l'option 'Appliquer' (Enforced) ?", "options": ["La stratégie ne s'applique qu'aux ordinateurs portables", "La GPO prévaut sur toute stratégie conflictuelle d'une unité d'organisation enfant, annulant le blocage d'héritage (Block Inheritance)", "La GPO s'applique toutes les 5 secondes", "Les utilisateurs doivent obligatoirement saisir un code SMS"], "rep": "La GPO prévaut sur toute stratégie conflictuelle d'une unité d'organisation enfant, annulant le blocage d'héritage (Block Inheritance)", "expl": "L'option Enforced force l'application descendante de la politique à travers toute la hiérarchie en court-circuitant les blocages locaux."}], "3. Virtualisation & Environnements Serveurs (Debian, VMware)": [{"q": "Quelle est la caractéristique fondamentale d'un hyperviseur de Type 1 (Bare-Metal) ?", "options": ["Il s'exécute comme un logiciel applicatif au-dessus de Windows", "Il s'installe et s'exécute directement sur le matériel physique du serveur sans système d'exploitation hôte intermédiaire", "Il ne peut faire tourner que des conteneurs légers", "Il nécessite obligatoirement une carte graphique dédiée"], "rep": "Il s'installe et s'exécute directement sur le matériel physique du serveur sans système d'exploitation hôte intermédiaire", "expl": "Les hyperviseurs de Type 1 (VMware ESXi, Proxmox VE, KVM) contrôlent directement le processeur et la mémoire vive pour des performances maximales."}, {"q": "Quel produit parmi les suivants est un hyperviseur de Type 2 (Hébergé) ?", "options": ["VMware ESXi", "Oracle VM VirtualBox", "Proxmox VE", "Microsoft Hyper-V Server Bare-metal"], "rep": "Oracle VM VirtualBox", "expl": "VirtualBox et VMware Workstation s'exécutent au-dessus d'un système d'exploitation hôte existant (Windows, Linux, macOS)."}, {"q": "En quoi la conteneurisation (Docker) diffère-t-elle de la virtualisation lourde par machines virtuelles (VM) ?", "options": ["Les conteneurs embarquent chacun leur propre noyau Linux complet", "Les conteneurs partagent le noyau du système hôte et isolent uniquement l'espace utilisateur (User Space), étant beaucoup plus légers et rapides à démarrer", "Les conteneurs ne peuvent pas communiquer en réseau", "Les conteneurs consomment 10 fois plus de mémoire RAM"], "rep": "Les conteneurs partagent le noyau du système hôte et isolent uniquement l'espace utilisateur (User Space), étant beaucoup plus légers et rapides à démarrer", "expl": "Grâce aux cgroups et namespaces du noyau Linux, Docker isole les processus sans virtualiser le matériel ni émuler un OS complet."}, {"q": "Dans VMware ou VirtualBox, quel mode de carte réseau isole la machine virtuelle sur un commutateur virtuel purement interne sans aucun accès physique extérieur ?", "options": ["Accès par pont (Bridged)", "Réseau privé hôte (Host-Only / Réseau interne)", "NAT", "Adaptateur générique"], "rep": "Réseau privé hôte (Host-Only / Réseau interne)", "expl": "Le mode Host-Only ou Réseau Interne permet de créer des bacs à sable d'expérimentation isolés du réseau de l'établissement ou de la maison."}, {"q": "Sous Linux Debian, quelle commande du gestionnaire de paquets APT met à jour la liste des versions logicielles disponibles dans les dépôts ?", "options": ["apt upgrade", "apt update", "apt install", "apt clean"], "rep": "apt update", "expl": "'apt update' télécharge les métadonnées fraîches des paquets depuis les miroirs ; 'apt upgrade' procède ensuite à la mise à niveau effective."}, {"q": "Quel système d'initialisation et gestionnaire de services est utilisé par défaut sous Linux Debian moderne ?", "options": ["SysVinit", "systemd (commandes systemctl et journalctl)", "Upstart", "OpenRC"], "rep": "systemd (commandes systemctl et journalctl)", "expl": "systemd gère le démarrage des démons, les cgroups, les dépendances de services et les logs unifiés."}, {"q": "Quelle commande systemd permet de recharger la configuration du serveur web Apache sans couper les connexions actives des clients ?", "options": ["systemctl stop apache2", "systemctl reload apache2", "systemctl reboot", "systemctl kill apache2"], "rep": "systemctl reload apache2", "expl": "L'action 'reload' envoie un signal au démon pour qu'il relise ses fichiers de configuration sans interrompre le processus en cours."}, {"q": "Quel fichier de configuration Debian définit les adresses IP statiques et masques des interfaces réseau physiques traditionnelles ?", "options": ["/etc/resolv.conf", "/etc/network/interfaces", "/etc/hosts", "/etc/fstab"], "rep": "/etc/network/interfaces", "expl": "Le fichier /etc/network/interfaces contient les blocs 'iface eth0 inet static' avec address, netmask et gateway."}, {"q": "Quelle commande affiche en temps réel la liste des ports TCP et UDP en écoute sur un serveur Linux avec les processus associés ?", "options": ["ls -la", "ss -tulpn (ou netstat -tulpn)", "cat /etc/services", "ping localhost"], "rep": "ss -tulpn (ou netstat -tulpn)", "expl": "'ss -tulpn' liste les sockets d'écoute (t: TCP, u: UDP, l: listening, p: process, n: numeric)."}, {"q": "Quelle est l'utilité d'un 'Snapshot' (instantané) sur une machine virtuelle ?", "options": ["Prendre une photo de l'écran avec la webcam", "Sauvegarder l'état exact du disque et de la mémoire à un instant T pour pouvoir y revenir instantanément en cas d'erreur", "Augmenter la vitesse du processeur", "Installer un antivirus"], "rep": "Sauvegarder l'état exact du disque et de la mémoire à un instant T pour pouvoir y revenir instantanément en cas d'erreur", "expl": "Le snapshot fige l'état de la VM avant une manipulation critique (mise à jour de noyau, test de script), permettant un rollback immédiat."}]}

FLASHCARDS_DATA = [{'id': 1, 'module': '📶 Réseaux & Télécoms', 'chap': '1. Modèle OSI vs TCP/IP', 'q': 'Quelles sont les 7 couches du modèle OSI et leurs PDU respectifs ?', 'a': '7. Application (Donnée), 6. Présentation (Donnée), 5. Session (Donnée), 4. Transport (Segment TCP / Datagramme UDP), 3. Réseau (Paquet IP), 2. Liaison (Trame Ethernet/MAC), 1. Physique (Bit/Signal).', 'note': '💡 **Conseil Examen** : Mnémonique de haut en bas : Après Plusieurs Semaines Tout Revient Logiquement Propre. Ne confondez jamais Trame (C2) et Paquet (C3) !', 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 1. Modèle OSI vs TCP/IP', 'v_id': '33UJvS_z8R8', 'v_title': 'Comprendre le Modèle OSI en 10 minutes'}, {'id': 2, 'module': '📶 Réseaux & Télécoms', 'chap': '1. Modèle OSI vs TCP/IP', 'q': 'Quel est le processus de connexion à 3 voies (3-way handshake) du protocole TCP ?', 'a': '1. Client -> Serveur : SYN (séquence x). 2. Serveur -> Client : SYN-ACK (séquence y, ack x+1). 3. Client -> Serveur : ACK (ack y+1). La connexion TCP est établie.', 'note': "💡 **Conseil Examen** : La retransmission d'un segment manquant s'effectue soit par le temporisateur RTO, soit par 3 DupACKs consécutifs.", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 1. Modèle OSI vs TCP/IP', 'v_id': '0j3_T7sN8J4', 'v_title': 'Fonctionnement détaillé de TCP & Handshake'}, {'id': 3, 'module': '📶 Réseaux & Télécoms', 'chap': '2. Adressage IPv4/IPv6 & VLSM', 'q': "Quelle est la formule du nombre d'hôtes utiles dans un sous-réseau IPv4 de CIDR donné ?", 'a': "N_hôtes = 2^(32 - CIDR) - 2. On soustrait l'adresse Réseau (bits hôtes à 0) et l'adresse de Broadcast (bits hôtes à 1).", 'note': '💡 **Conseil Examen** : Pour un masque /28, 32-28 = 4 bits. 2^4 - 2 = 14 hôtes utilisables. Soustrayez toujours 2 !', 'cours_ref': '🧮 Laboratoire de Calculs -> Subnetting VLSM IPv4', 'v_id': '42S-A-9PqM0', 'v_title': 'Masterclass Subnetting VLSM IPv4'}, {'id': 4, 'module': '📶 Réseaux & Télécoms', 'chap': '2. Adressage IPv4/IPv6 & VLSM', 'q': 'Quel protocole remplace le protocole ARP en IPv6 pour découvrir les adresses MAC des voisins ?', 'a': "Le protocole NDP (Neighbor Discovery Protocol), s'appuyant sur des messages ICMPv6 Neighbor Solicitation (NS) et Neighbor Advertisement (NA).", 'note': "💡 **Conseil Examen** : En IPv6, le broadcast n'existe plus ! Il est entièrement remplacé par le Multicast (ex: ff02::1 pour tous les nœuds).", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 2. Adressage IPv4/IPv6', 'v_id': '72sn_0M4T4g', 'v_title': 'IPv6, SLAAC et NDP expliqués simplement'}, {'id': 5, 'module': '📶 Réseaux & Télécoms', 'chap': '3. Commutation & VLANs', 'q': 'Comment un commutateur (Switch) remplit-il sa table de commutation (table MAC / CAM) ?', 'a': "Par apprentissage passif (Learning) : à la réception d'une trame, il lit l'adresse MAC source et l'associe au port d'entrée. Pour commuter, il consulte la MAC destination.", 'note': '💡 **Conseil Examen** : Si la MAC destination est inconnue, le switch effectue un inondage (Flooding) sur tous les ports du VLAN sauf le port récepteur.', 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Commutation & VLANs', 'v_id': '06Y6qYg9_C0', 'v_title': 'Commutation Ethernet & Table CAM'}, {'id': 6, 'module': '📶 Réseaux & Télécoms', 'chap': '3. Commutation & VLANs', 'q': 'Quelle est la taille exacte et le rôle du tag inséré par la norme IEEE 802.1Q ?', 'a': "Le tag mesure 4 octets (32 bits), dont 12 bits sont dédiés au VID (VLAN ID), permettant de faire transiter jusqu'à 4094 VLANs sur une liaison Trunk.", 'note': '💡 **Conseil Examen** : Le VLAN Natif (VLAN 1 par défaut) voyage non étiqueté sur le Trunk. Il doit être identique aux deux extrémités du lien.', 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Commutation & VLANs', 'v_id': '0j3_T7sN8J4', 'v_title': 'Tout savoir sur le Trunking 802.1Q'}, {'id': 7, 'module': '📶 Réseaux & Télécoms', 'chap': '4. Routage Inter-VLAN', 'q': 'Quelle est la séquence de commandes Cisco IOS pour configurer Router-on-a-Stick sur le VLAN 20 ?', 'a': 'interface GigabitEthernet0/0.20 -> encapsulation dot1Q 20 -> ip address 192.168.20.254 255.255.255.0.', 'note': "💡 **Conseil Examen** : Pensez à activer l'interface physique parente avec no shutdown sous interface g0/0 !", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 4. Routage Inter-VLAN', 'v_id': 'LqT5y7aZJ4k', 'v_title': 'Configuration Router-on-a-Stick Cisco'}, {'id': 8, 'module': '📶 Réseaux & Télécoms', 'chap': '3. Commutation & Spanning Tree', 'q': 'Quel est le rôle principal du protocole Spanning Tree (STP 802.1D / RSTP 802.1w) ?', 'a': 'Éviter les boucles logiques de Niveau 2 (tempêtes de broadcast) en bloquant les ports redondants pour former une topologie en arbre sans boucle.', 'note': '💡 **Conseil Examen** : Le Root Bridge est élu selon le Bridge ID (Priority + MAC) le plus faible. RSTP converge en moins de 2 secondes.', 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Commutation & Spanning Tree', 'v_id': 'i8D4W6U4z_E', 'v_title': 'Spanning Tree & RSTP 802.1w'}, {'id': 9, 'module': '📶 Réseaux & Télécoms', 'chap': '5. Services Infrastructure', 'q': 'Quels sont les 4 messages du processus DHCP DORA ?', 'a': '1. Discover (Broadcast client UDP 67). 2. Offer (Proposition serveur UDP 68). 3. Request (Demande client). 4. Acknowledge (Validation du bail par le serveur).', 'note': "💡 **Conseil Examen** : Pour relayer DHCP à travers un routeur, configurez ip helper-address <IP_Serveur_DHCP> sur l'interface du sous-réseau client.", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 5. Services Infrastructure', 'v_id': '72sn_0M4T4g', 'v_title': 'Services DHCP & Relai DHCP'}, {'id': 10, 'module': '📶 Réseaux & Télécoms', 'chap': '5. Services Infrastructure', 'q': 'À quoi servent les enregistrements DNS de type A, AAAA, CNAME, MX et PTR ?', 'a': 'A : Nom -> IPv4. AAAA : Nom -> IPv6. CNAME : Alias. MX : Serveur Mail. PTR : Résolution inverse (IP -> Nom FQDN).', 'note': "💡 **Conseil Examen** : L'enregistrement PTR se situe dans la zone de recherche inverse (ex: 1.168.192.in-addr.arpa).", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 5. Services Infrastructure', 'v_id': '72sn_0M4T4g', 'v_title': 'Architecture du DNS & Enregistrements'}, {'id': 11, 'module': '📶 Réseaux & Télécoms', 'chap': '5. Services Infrastructure', 'q': 'Quelle est la différence entre NAT Statique et PAT (Overload) ?', 'a': "NAT Statique : traduction 1-à-1 fixe d'IP privée vers publique. PAT (Port Address Translation) : multiple IP privées sur 1 IP publique grâce aux ports TCP/UDP.", 'note': '💡 **Conseil Examen** : La commande Cisco PAT est ip nat inside source list <ACL> interface <WAN> overload.', 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 5. Services Infrastructure', 'v_id': 'LqT5y7aZJ4k', 'v_title': 'Comprendre le NAT/PAT & Port Forwarding'}, {'id': 12, 'module': '📶 Réseaux & Télécoms', 'chap': '6. Routage Dynamique OSPF', 'q': 'Sur quelle métrique et quel algorithme repose le protocole de routage OSPF ?', 'a': "Algorithme d'État de Lien (Dijkstra / Shortest Path First) avec métrique basée sur le Coût de Bande Passante (Coût = 10^8 / Débit bps).", 'note': "💡 **Conseil Examen** : Toutes les zones OSPF (Areas) doivent obligatoirement se raccorder à l'Area 0 (Backbone Area).", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 6. Routage Dynamique', 'v_id': '3k1-zK7u1G0', 'v_title': 'Routage OSPF & Aires OSPF'}, {'id': 13, 'module': '📶 Réseaux & Télécoms', 'chap': '7. Transmissions Optiques', 'q': 'Quelles sont les caractéristiques comparées des fibres Monomode (SMF) et Multimode (MMF) ?', 'a': 'Monomode (SMF) : cœur 9 µm, émetteur Laser (1310/1550 nm), très longue portée, pas de dispersion modale. Multimode (MMF) : cœur 50/62.5 µm, émetteur LED (850/1300 nm), portée < 500m.', 'note': "💡 **Conseil Examen** : L'angle limite de réflexion totale interne suit sin(i_lim) = n2/n1 (avec n1 cœur > n2 gaine).", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 7. Transmissions Optiques', 'v_id': '3Z8oE-pCq00', 'v_title': 'Fibre Optique : Monomode vs Multimode'}, {'id': 14, 'module': '📶 Réseaux & Télécoms', 'chap': "7. Théorie de l'Information", 'q': "Quelle est la formule de la capacité maximale binaire d'un canal bruité (Shannon-Hartley) ?", 'a': 'C = B * log2(1 + S/N) en bps, avec B la bande passante (Hz) et S/N le rapport signal sur bruit en puissance linéaire.', 'note': "💡 **Conseil Examen** : Si le rapport S/N est donné en dB, convertissez-le d'abord en linéaire : S/N = 10^(SNR_dB / 10).", 'cours_ref': '📊 Mathématiques Appliquées -> Calculs de Décibels', 'v_id': '3Z8oE-pCq00', 'v_title': 'Capacité de Shannon & Rapport Signal/Bruit'}, {'id': 15, 'module': '📶 Réseaux & Télécoms', 'chap': "7. Théorie de l'Information", 'q': 'Quelle est la relation entre Débit binaire D (bps) et Rapidité de modulation R (Bauds) ?', 'a': 'D = R * log2(M) = R * n, où n est le nombre de bits transmis par symbole (valence M = 2^n).', 'note': '💡 **Conseil Examen** : Pour une modulation 16-QAM (M = 16), n = log2(16) = 4 bits/symbole. Un débit de 2400 Bauds donne 9600 bps.', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°9 Bauds vs bps', 'v_id': '3Z8oE-pCq00', 'v_title': 'Bauds vs Bits par seconde et Valences'}, {'id': 16, 'module': '📶 Réseaux & Télécoms', 'chap': '8. Wireshark & Analyse', 'q': 'Quels filtres Wireshark isolent le trafic HTTP, DNS, IP source 192.168.1.10 et TCP 80 ?', 'a': 'http, dns, ip.src == 192.168.1.10, tcp.port == 80. Combinaisons avec && ou and.', 'note': "💡 **Conseil Examen** : Ne confondez pas Filtre de Capture (host 10.0.0.1) et Filtre d'Affichage (ip.addr == 10.0.0.1).", 'cours_ref': '🔍 Lab Décodeur Wireshark', 'v_id': 'TkCSr30UojM', 'v_title': 'Maîtriser les filtres Wireshark'}, {'id': 17, 'module': '📶 Réseaux & Télécoms', 'chap': '3. Sécurité Switchs Cisco', 'q': 'Quels sont les 3 modes de violation pour Cisco Port Security ?', 'a': '1. protect : jette sans alerte. 2. restrict : jette + alerte SNMP + incrémente compteur. 3. shutdown : désactive le port (err-disabled).', 'note': "💡 **Conseil Examen** : Pour réactiver un port en err-disabled : faites shutdown puis no shutdown sous l'interface.", 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 3. Sécurité des Commutateurs', 'v_id': '0j3_T7sN8J4', 'v_title': 'Sécuriser les ports avec Port Security'}, {'id': 18, 'module': '📶 Réseaux & Télécoms', 'chap': '2. En-tête IPv4', 'q': "Quel est le rôle des champs TTL et Protocol dans l'en-tête IPv4 ?", 'a': 'TTL : décrémenté de 1 par chaque routeur (évite les boucles). Protocol : indique le protocole encapsulé (6 = TCP, 17 = UDP, 1 = ICMP).', 'note': '💡 **Conseil Examen** : En valeur hexadécimale Wireshark : 0x06 = TCP, 0x11 = UDP, 0x01 = ICMP.', 'cours_ref': '📚 Encyclopédie des Cours & TPs -> 📶 Réseaux -> 2. En-tête IP', 'v_id': 'TkCSr30UojM', 'v_title': "Décodage d'en-tête IP sous Wireshark"}, {'id': 19, 'module': '🔒 Cybersécurité', 'chap': '1. Méthode EBIOS RM', 'q': "Quels sont les 5 Ateliers de la méthode EBIOS RM de l'ANSSI ?", 'a': '1. Cadrage & Socle de sécurité. 2. Sources de Risques (SR). 3. Scénarios Stratégiques. 4. Scénarios Opérationnels (Kill Chain). 5. Traitement des Risques (PACS).', 'note': "💡 **Conseil Examen** : Retenez les critères d'impact DICP : Disponibilité, Intégrité, Confidentialité, Preuve/Traçabilité.", 'cours_ref': '🛡️ TP Cybersécurité -> Ateliers EBIOS RM ANSSI', 'v_id': 'J8n0j3x9K2A', 'v_title': 'Méthode EBIOS RM ANSSI en 5 Ateliers'}, {'id': 20, 'module': '🔒 Cybersécurité', 'chap': '2. Analyse PIA / AIPD', 'q': "Quand une Analyse d'Impact relative à la Protection des Données (AIPD/PIA) est-elle obligatoire ?", 'a': "Conformément à l'Art. 35 du RGPD, dès qu'un traitement est susceptible d'engendrer un risque élevé pour la vie privée, notamment lorsqu'il remplit au moins 2 critères sur 9 de la grille CNIL.", 'note': '💡 **Conseil Examen** : Exemples de critères CNIL : profilage, données sensibles/biométriques, personnes vulnérables (salariés/mineurs), grande échelle.', 'cours_ref': '🛡️ TP Cybersécurité -> Atelier PIA / AIPD RGPD', 'v_id': '5k9m2-8a9X0', 'v_title': 'Réaliser une AIPD / PIA RGPD'}, {'id': 21, 'module': '🔒 Cybersécurité', 'chap': '3. Cryptographie', 'q': 'Quelle est la différence fondamentale entre le chiffrement symétrique et asymétrique ?', 'a': 'Symétrique : une seule clé secrète partagée pour chiffrer/déchiffrer (rapide, ex: AES-256). Asymétrique : clé publique pour chiffrer, clé privée pour déchiffrer (résout le partage de clé, ex: RSA-2048).', 'note': '💡 **Conseil Examen** : En pratique, on utilise un chiffrement hybride : RSA pour échanger une clé de session AES, puis AES pour les données.', 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 1. Cryptographie', 'v_id': '0iY2m-J4z-0', 'v_title': 'Chiffrement Symétrique vs Asymétrique'}, {'id': 22, 'module': '🔒 Cybersécurité', 'chap': '3. Cryptographie', 'q': "Qu'est-ce qu'une fonction de hachage irréversible et à quoi sert une empreinte SHA-256 ?", 'a': "Une fonction mathématique à sens unique qui transforme un message de taille quelconque en une empreinte de taille fixe (256 bits). Utilisée pour vérifier l'Intégrité.", 'note': "💡 **Conseil Examen** : Une fonction de hachage est irréversible (impossible de retrouver le message d'origine) et déterministe.", 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 1. Cryptographie', 'v_id': '0iY2m-J4z-0', 'v_title': 'Hachage SHA-256 & Intégrité'}, {'id': 23, 'module': '🔒 Cybersécurité', 'chap': '4. PKI & Certificats X.509', 'q': "Pourquoi la CA Racine (Root CA) d'une PKI doit-elle être conservée hors ligne (offline) ?", 'a': "Pour empêcher toute compromission à distance. Si la clé privée de la Root CA est compromise, toute la chaîne de confiance s'effondre.", 'note': '💡 **Conseil Examen** : Ce sont les CA Intermédiaires (Issuing CAs) en ligne qui émettent les certificats clients et serveurs.', 'cours_ref': '🛡️ TP Cybersécurité -> PKI & Certificats X.509', 'v_id': '0iY2m-J4z-0', 'v_title': 'Architecture PKI & Autorités de Certification'}, {'id': 24, 'module': '🔒 Cybersécurité', 'chap': '4. PKI & Certificats X.509', 'q': "Quelle extension d'un certificat X.509 permet de déclarer plusieurs noms de domaine / IPs ?", 'a': "L'extension SAN (Subject Alternative Name).", 'note': "💡 **Conseil Examen** : Sans l'extension SAN, les navigateurs modernes rejettent le certificat TLS même si le Common Name (CN) est correct.", 'cours_ref': '🛡️ TP Cybersécurité -> PKI & Certificats X.509', 'v_id': '0iY2m-J4z-0', 'v_title': 'Certificats TLS X.509 & Extension SAN'}, {'id': 25, 'module': '🔒 Cybersécurité', 'chap': '4. PKI & Certificats X.509', 'q': 'Quelles sont les commandes OpenSSL pour générer une clé privée RSA et une demande CSR ?', 'a': 'Clé : openssl genrsa -out server.key 2048. Demande CSR : openssl req -new -key server.key -out server.csr.', 'note': "💡 **Conseil Examen** : Pour inspecter le contenu binaire d'un certificat : openssl x509 -in server.crt -text -noout.", 'cours_ref': '🛡️ TP Cybersécurité -> PKI & Certificats X.509', 'v_id': '0iY2m-J4z-0', 'v_title': 'Tutoriel Commandes OpenSSL'}, {'id': 26, 'module': '🔒 Cybersécurité', 'chap': '5. Architecture DMZ & pfSense', 'q': "Quelle est la règle d'isolation réseau fondamentale entre la DMZ et le LAN ?", 'a': "Interdiction stricte d'initiation de connexion depuis la DMZ vers le LAN. Seul le LAN ou le WAN peuvent initier une connexion vers la DMZ.", 'note': '💡 **Conseil Examen** : Si un serveur Web en DMZ est compromis par un pirate, celui-ci ne doit pas pouvoir attaquer le LAN interne.', 'cours_ref': '🛡️ TP Cybersécurité -> Pare-Feu pfSense & DMZ', 'v_id': 'L2k3j4X5m-0', 'v_title': 'Architecture DMZ & Configuration pfSense'}, {'id': 27, 'module': '🔒 Cybersécurité', 'chap': '5. Architecture DMZ & pfSense', 'q': "Quels sont les ports TCP/UDP indispensables à autoriser pour le fonctionnement d'Active Directory ?", 'a': 'DNS : 53 (TCP/UDP), Kerberos : 88 (TCP/UDP), LDAP : 389 (TCP/UDP), LDAPS : 636 (TCP), SMB : 445 (TCP), RPC : 135 (TCP).', 'note': "💡 **Conseil Examen** : Kerberos gère l'authentification (port 88) tandis que LDAP gère les requêtes d'annuaire (port 389/636).", 'cours_ref': '🛡️ TP Cybersécurité -> Matrice des Flux AD', 'v_id': '8m9k3j4X5m0', 'v_title': 'Ports & Flux Active Directory'}, {'id': 28, 'module': '🔒 Cybersécurité', 'chap': '6. Top 10 OWASP', 'q': 'Quelle technique prémunit définitivement une application web contre les injections SQL ?', 'a': "L'utilisation de requêtes préparées (paramétrées / Prepared Statements) qui séparent strictly le code SQL des données utilisateurs.", 'note': "💡 **Conseil Examen** : Le simple filtrage d'expressions régulières ou l'échappement manuel de caractères ne suffit pas face aux contournements OWASP.", 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 3. Top 10 OWASP', 'v_id': '0k3j4X5m-0', 'v_title': 'Injections SQL & Requêtes Préparées'}, {'id': 29, 'module': '🔒 Cybersécurité', 'chap': '6. Top 10 OWASP', 'q': 'Quelle est la différence entre une faille XSS Stored et XSS Reflected ?', 'a': "XSS Stored : le script malveillant est stocké en BDD et exécuté pour tous les visiteurs. XSS Reflected : le script est réfléchi immédiatement dans l'URL.", 'note': "💡 **Conseil Examen** : La parade contre le XSS est l'échappement systématique des caractères HTML (&lt;, &gt;, quotes) et l'en-tête CSP (Content Security Policy).", 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 3. Top 10 OWASP', 'v_id': '0k3j4X5m-0', 'v_title': 'OWASP XSS & Sécurisation Web'}, {'id': 30, 'module': '🔒 Cybersécurité', 'chap': '6. Top 10 OWASP', 'q': 'En quoi consiste une attaque CSRF (Cross-Site Request Forgery) et comment la contrecarrer ?', 'a': 'Attaque qui piège un utilisateur authentifié pour exécuter des actions non voulues à son insu. Parade : utiliser un Jetons Anti-CSRF imprédictible.', 'note': '💡 **Conseil Examen** : Le jeton anti-CSRF est un token unique généré par session et vérifié lors de chaque soumission de formulaire POST.', 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 3. Top 10 OWASP', 'v_id': '0k3j4X5m-0', 'v_title': 'Faille CSRF & Protection par Tokens'}, {'id': 31, 'module': '🔒 Cybersécurité', 'chap': '5. Pare-feu & Filtrage', 'q': 'Quelle est la politique de filtrage recommandée par défaut sur un pare-feu réseau ?', 'a': "Politique Deny All (Tout refuser par défaut) et n'autoriser explicitement que les flux strictement nécessaires (Whitelisting).", 'note': "💡 **Conseil Examen** : La dernière règle d'un pare-feu (règle 999) est toujours Deny Any Any.", 'cours_ref': '🛡️ TP Cybersécurité -> Pare-Feu pfSense', 'v_id': 'L2k3j4X5m-0', 'v_title': 'Filtrage Réseau & Politiques Pare-Feu'}, {'id': 32, 'module': '🔒 Cybersécurité', 'chap': '7. Tunnels VPN', 'q': 'Quelle est la différence entre un VPN IPsec (Couche 3) et un VPN TLS / OpenVPN (Couche 4) ?', 'a': 'IPsec (Couche 3) : chiffrement au niveau paquet IP (site-à-site), transparent pour les applications. TLS (Couche 4) : VPN client-à-site via port TCP 443.', 'note': '💡 **Conseil Examen** : IPsec utilise le protocole ESP (IP 50) pour le chiffrement/authentification et IKE (UDP 500) pour la négociation de clés.', 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 4. Tunnels VPN', 'v_id': 'L2k3j4X5m-0', 'v_title': 'Tunnels VPN IPsec vs TLS'}, {'id': 33, 'module': '🔒 Cybersécurité', 'chap': '8. Sécurité IoT', 'q': 'Sur quel port et quel protocole repose la version sécurisée de MQTT (MQTTS) ?', 'a': "MQTTS s'appuie sur MQTT encapsulé dans une couche TLS/SSL, fonctionnant par défaut sur le port TCP 8883 (au lieu du port 1883 en clair).", 'note': "💡 **Conseil Examen** : MQTTS garantit la confidentialité des messages de télémétrie capteurs et l'authentification du Broker par certificat X.509.", 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 5. Sécurité IoT', 'v_id': '0iY2m-J4z-0', 'v_title': 'Protocole MQTTS & Sécurisation IoT'}, {'id': 34, 'module': '🔒 Cybersécurité', 'chap': '9. Attaques Réseau', 'q': 'Comment fonctionne une attaque SYN Flood et comment la neutraliser ?', 'a': 'Le pirate envoie une masse de paquets TCP SYN sans répondre au SYN-ACK, saturant la table de connexions du serveur. Parade : activer les SYN Cookies.', 'note': "💡 **Conseil Examen** : La technologie SYN Cookies permet au serveur d'encode l'état de la connexion dans le numéro de séquence sans allouer de mémoire.", 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 6. Attaques Réseau', 'v_id': '0k3j4X5m-0', 'v_title': 'Attaques DoS/DDoS & SYN Flood'}, {'id': 35, 'module': '🔒 Cybersécurité', 'chap': '10. Sécurité Wi-Fi', 'q': "Quel est le rôle d'un serveur RADIUS dans une architecture Wi-Fi 802.1X / WPA3-Enterprise ?", 'a': "Le serveur RADIUS agit comme serveur d'authentification centralisé : il vérifie les identifiants/certificats des utilisateurs auprès de l'annuaire (AD/LDAP).", 'note': "💡 **Conseil Examen** : En WPA2/WPA3-Personal, la clé est partagée (PSK). En WPA-Enterprise, chaque utilisateur a son propre compte d'accès.", 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 7. Sécurité Wi-Fi', 'v_id': '8m9k3j4X5m0', 'v_title': 'Wi-Fi 802.1X & Serveur RADIUS'}, {'id': 36, 'module': '🔒 Cybersécurité', 'chap': '11. Exploitation de vulnérabilité', 'q': "Qu'est-ce qu'une attaque par Dépassement de Tampon (Buffer Overflow) ?", 'a': "Écriture de données au-delà de la mémoire allouée à un tableau, écrasant l'adresse de retour dans la Pile pour exécuter du code malveillant (Shellcode).", 'note': '💡 **Conseil Examen** : Parades : fonctions C sûres (strncpy au lieu de strcpy) et protections compilateur (ASLR, NX Bit / DEP, Stack Canaries).', 'cours_ref': '📚 Encyclopédie des Cours -> 🔒 Cybersécurité -> 8. Développement Sécurisé', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Buffer Overflow & Protections Mémoire'}, {'id': 37, 'module': '💻 Programmation / Dev', 'chap': '1. Gestion Mémoire C++', 'q': 'Quelle est la différence entre la mémoire Pile (Stack) et la mémoire Tas (Heap) ?', 'a': 'Pile (Stack) : automatique, rapide, taille limitée, portée locale. Tas (Heap) : dynamique, allouée avec new/delete, gérée par le développeur, risque de fuites.', 'note': '💡 **Conseil Examen** : Toute allocation avec new doit être libérée avec delete. Tout new[] doit être libéré avec delete[].', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++', 'v_id': 'S1yR7_7bWRE', 'v_title': 'Mémoire C++ : Pile vs Tas'}, {'id': 38, 'module': '💻 Programmation / Dev', 'chap': '1. Gestion Mémoire C++', 'q': "Pourquoi est-il obligatoire d'utiliser delete[] pour un tableau alloué dynamiquement ?", 'a': "L'opérateur delete[] appelle le destructeur pour chaque élément du tableau avant de restituer la mémoire. delete seul ne détruit que le premier élément.", 'note': "💡 **Conseil Examen** : L'oubli des crochets [] lors de la libération d'un tableau dynamique provoque une fuite de mémoire (Memory Leak).", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++', 'v_id': 'S1yR7_7bWRE', 'v_title': 'Allocation Dynamique delete[] C++'}, {'id': 39, 'module': '💻 Programmation / Dev', 'chap': '1. Gestion Mémoire C++', 'q': 'Quelle est la différence entre un pointeur (*) et une référence (&) en C++ ?', 'a': "Un pointeur est une variable qui contient une adresse mémoire (peut être NULL et réassignable). Une référence est un alias fixe d'une variable existante (non NULL).", 'note': '💡 **Conseil Examen** : Préférez le passage de grands objets par référence constante (const MaClasse& obj) pour éviter les copies coûteuses en mémoire.', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++', 'v_id': 'S1yR7_7bWRE', 'v_title': 'Pointeurs et Références en C++'}, {'id': 40, 'module': '💻 Programmation / Dev', 'chap': '1. Smart Pointers C++11', 'q': 'Quelle est la différence entre std::unique_ptr et std::shared_ptr en C++11 ?', 'a': "std::unique_ptr : propriété exclusive d'une ressource (non copiable, libération auto). std::shared_ptr : propriété partagée avec compteur de références.", 'note': '💡 **Conseil Examen** : Les Smart Pointers gèrent automatiquement le cycle de vie de la mémoire (RAII) et éliminent les fuites mémoire.', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++', 'v_id': 'S1yR7_7bWRE', 'v_title': 'Smart Pointers C++11'}, {'id': 41, 'module': '💻 Programmation / Dev', 'chap': '2. Langage C', 'q': "Quelle est la différence d'occupation mémoire entre une struct et une union en C ?", 'a': 'struct : chaque membre possède son propre espace mémoire (somme des tailles). union : tous les membres partagent la même adresse (taille du plus grand).', 'note': "💡 **Conseil Examen** : L'union est idéale pour décoder des trames réseau brutes (ex: lire un float 32 bits sous forme de 4 octets char[4]).", 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°12 C/C++', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Structures et Unions en Langage C'}, {'id': 42, 'module': '💻 Programmation / Dev', 'chap': '3. POO C++', 'q': "À quoi servent les niveaux d'accès private, protected et public en POO C++ ?", 'a': 'private : accessible uniquement dans la classe. protected : accessible dans la classe et ses classes dérivées. public : accessible partout.', 'note': "💡 **Conseil Examen** : C'est le principe d'Encapsulation : masquez les attributs en private et fournissez des accesseurs public (getters/setters).", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++', 'v_id': '6m8gS-iXmXQ', 'v_title': "Encapsulation & Niveaux d'Accès POO"}, {'id': 43, 'module': '💻 Programmation / Dev', 'chap': '3. POO C++', 'q': "Comment s'écrit l'héritage public d'une classe Fille depuis une classe Mere en C++ ?", 'a': 'class Fille : public Mere { public: Fille(); };', 'note': "💡 **Conseil Examen** : L'héritage public préserve les droits public et protected de la classe mère dans la classe fille.", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Héritage POO C++'}, {'id': 44, 'module': '💻 Programmation / Dev', 'chap': '3. POO C++', 'q': "Qu'est-ce qu'une méthode virtuelle pure en C++ et quel est son impact ?", 'a': "Une méthode déclarée avec virtual void f() = 0;. Elle n'a pas d'implémentation dans la classe mère et rend la classe Abstraite (non instanciable).", 'note': '💡 **Conseil Examen** : Une classe fille doit obligatoirement redéfinir toutes les méthodes virtuelles pures de la classe mère pour pouvoir être instanciée.', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Classes Abstraites & Méthodes Virtuelles Pures'}, {'id': 45, 'module': '💻 Programmation / Dev', 'chap': '3. POO C++', 'q': "Pourquoi le destructeur d'une classe mère polymorphe doit-il obligatoirement être virtual ?", 'a': "Pour garantir que lors de la suppression d'un objet via un pointeur de classe mère (delete ptr), le destructeur de la classe fille soit correctement exécuté.", 'note': "💡 **Conseil Examen** : Si le destructeur n'est pas virtuel, seul le destructeur de la classe mère est appelé, provoquant une fuite de la mémoire de la fille.", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Destructeurs Virtuels en C++'}, {'id': 46, 'module': '💻 Programmation / Dev', 'chap': '4. Multithreading C++11', 'q': 'Comment instancier et exécuter un thread en parallèle en C++11 avec std::thread ?', 'a': 'std::thread t(maFonction, arg1); t.join(); (ou t.detach();).', 'note': "💡 **Conseil Examen** : N'oubliez jamais d'appeler t.join() pour attendre la fin du thread avant la destruction de l'objet std::thread.", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 3. Multithreading C++', 'v_id': '5m9k3j4X5m0', 'v_title': 'Multithreading C++11 avec std::thread'}, {'id': 47, 'module': '💻 Programmation / Dev', 'chap': '4. Multithreading C++11', 'q': 'Comment protéger une variable partagée contre les Race Conditions avec std::mutex ?', 'a': 'En utilisant un verrou RAII std::lock_guard<std::mutex> lock(mon_mutex); au début de la section critique.', 'note': '💡 **Conseil Examen** : lock_guard verrouille le mutex au constructeur et le libère automatiquement au destructeur (fin de portée/scope).', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 3. Multithreading C++', 'v_id': '5m9k3j4X5m0', 'v_title': 'Exclusion Mutuelle std::mutex & RAII'}, {'id': 48, 'module': '💻 Programmation / Dev', 'chap': '5. Sockets Python TCP', 'q': 'Quelles sont les 5 méthodes sockets exécutées côté serveur TCP en Python ?', 'a': '1. socket.socket() -> 2. bind((ip, port)) -> 3. listen(backlog) -> 4. accept() -> 5. recv(buffer) / sendall(data).', 'note': '💡 **Conseil Examen** : La méthode accept() est bloquante et renvoie un tuple (conn_socket, (client_ip, client_port)).', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 4. Sockets Python', 'v_id': '6m9k3j4X5m0', 'v_title': 'Programmation Sockets TCP en Python'}, {'id': 49, 'module': '💻 Programmation / Dev', 'chap': '5. Sockets Python UDP', 'q': 'Quelles sont les méthodes sockets utilisées pour envoyer et recevoir des datagrammes UDP en Python ?', 'a': "sendto(data, (ip, port)) pour envoyer, et recvfrom(buffer_size) pour recevoir (renvoie data et l'adresse de l'expéditeur).", 'note': "💡 **Conseil Examen** : UDP étant sans connexion, il n'y a ni connect(), ni listen(), ni accept() !", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 4. Sockets Python', 'v_id': '6m9k3j4X5m0', 'v_title': 'Sockets UDP Python sendto recvfrom'}, {'id': 50, 'module': '💻 Programmation / Dev', 'chap': '5. Encodage & JSON', 'q': "Comment convertir une chaîne de caractères en octets pour l'envoyer sur une socket en Python ?", 'a': "En utilisant la méthode .encode('utf-8') (et .decode('utf-8') à la réception). Pour le JSON : json.dumps(dict) et json.loads(str).", 'note': '💡 **Conseil Examen** : Les sockets transmettent des octets (bytes) et non des chaînes de caractères brutes (str).', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 4. Sockets Python', 'v_id': '6m9k3j4X5m0', 'v_title': 'Encodage UTF-8 & Formats JSON Python'}, {'id': 51, 'module': '💻 Programmation / Dev', 'chap': '6. Versioning Git', 'q': 'Quelles sont les commandes Git pour ajouter, valider et envoyer des modifications localement et à distance ?', 'a': 'git add . -> git commit -m msg -> git push origin main.', 'note': "💡 **Conseil Examen** : git status permet de vérifier l'état de l'index et des fichiers modifiés à tout moment.", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 5. Versioning Git', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Commandes Git Essentielles'}, {'id': 52, 'module': '💻 Programmation / Dev', 'chap': '3. Surcharge & Override C++11', 'q': 'À quoi sert le mot-clé override placé en fin de déclaration de méthode en C++11 ?', 'a': 'Il indique au compilateur que la méthode redéfinit explicitement une méthode virtuelle de la classe mère, générant une erreur en cas de signature incorrecte.', 'note': "💡 **Conseil Examen** : override évite les bogues subtils liés aux fautes de frappe dans le nom ou les arguments d'une méthode virtuelle.", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 2. POO C++', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Surcharge & Mot-clé override C++11'}, {'id': 53, 'module': '💻 Programmation / Dev', 'chap': '2. Directives Préprocesseur C', 'q': "À quoi servent les directives #ifndef, #define, #endif (Include Guards) dans un fichier d'en-tête .h ?", 'a': "À éviter les inclusions multiples d'un même fichier d'en-tête lors de la compilation, prévenant les erreurs de re-déclaration.", 'note': '💡 **Conseil Examen** : Alternative moderne : la directive préprocesseur #pragma once en tête de fichier .h.', 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 1. Compilateur C/C++', 'v_id': '6m8gS-iXmXQ', 'v_title': 'Include Guards & Préprocesseur C'}, {'id': 54, 'module': '💻 Programmation / Dev', 'chap': '1. Pointeurs & Références', 'q': "Que fait l'opérateur & placé devant une variable existante en C++ ?", 'a': "Il renvoie l'adresse mémoire de la variable (ex: int* p = &x;).", 'note': "💡 **Conseil Examen** : Ne confondez pas l'opérateur adresse & en expression et la déclaration de référence int& ref = x;.", 'cours_ref': '📚 Encyclopédie des Cours -> 💻 Dev -> 1. Mémoire C++', 'v_id': 'S1yR7_7bWRE', 'v_title': 'Opérateurs Pointeur et Adresse C++'}, {'id': 55, 'module': '🖥️ Administration Système', 'chap': '1. Permissions Linux', 'q': 'Que signifie le masque octal 750 sur un fichier ou dossier Linux ?', 'a': 'Owner (Utilisateur) = 7 (rwx), Group (Groupe) = 5 (r-x), Others (Autres) = 0 (---).', 'note': '💡 **Conseil Examen** : Valeurs des droits : Read r = 4, Write w = 2, Execute x = 1. 7 = 4+2+1, 5 = 4+1, 0 = 0.', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'Permissions Linux chmod Octal'}, {'id': 56, 'module': '🖥️ Administration Système', 'chap': '1. Permissions Linux', 'q': 'Que signifie le droit spécial SUID (4000) sur un fichier exécutable Linux ?', 'a': "L'exécutable est lancé avec les privilèges du propriétaire du fichier (ex: root) et non de l'utilisateur qui le lance (ex: /usr/bin/passwd).", 'note': "💡 **Conseil Examen** : En notation symbolique, le SUID apparaît sous la forme d'un s à la place du x utilisateur (ex: -rwsr-xr-x).", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'Droits Spéciaux Linux : SUID, SGID, Sticky'}, {'id': 57, 'module': '🖥️ Administration Système', 'chap': '1. Permissions Linux', 'q': 'À quoi sert le droit spécial SGID (2000) appliqué sur un répertoire Linux ?', 'a': "Tous les nouveaux fichiers et dossiers créés à l'intérieur héritent automatiquement du groupe du répertoire parent.", 'note': "💡 **Conseil Examen** : Le SGID est idéal pour configurer des dossiers de travail partagés entre plusieurs membres d'un même groupe.", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'Droit SGID & Dossiers Partagés Linux'}, {'id': 58, 'module': '🖥️ Administration Système', 'chap': '1. Permissions Linux', 'q': 'À quoi sert le droit spécial Sticky Bit (1000) sur un répertoire comme /tmp ?', 'a': 'Il empêche les utilisateurs de supprimer ou renommer les fichiers dont ils ne sont pas les propriétaires.', 'note': "💡 **Conseil Examen** : En notation symbolique, le Sticky Bit s'affiche t à la place du x des autres (ex: drwxrwxrwt /tmp).", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'Sticky Bit & Répertoire /tmp'}, {'id': 59, 'module': '🖥️ Administration Système', 'chap': '1. Permissions Linux', 'q': "Quelles commandes Linux permettent de lire et d'attribuer une ACL POSIX personnalisée à l'utilisateur alice ?", 'a': 'Lecture : getfacl fichier. Modification : setfacl -m u:alice:rwx fichier.', 'note': "💡 **Conseil Examen** : L'option -m signifie modify. Pour supprimer les ACLs : setfacl -b fichier.", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Permissions Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'ACLs Linux getfacl setfacl'}, {'id': 60, 'module': '🖥️ Administration Système', 'chap': '2. Services Linux systemd', 'q': "Quelles commandes systemctl permettent de vérifier l'état, redémarrer et activer un service au démarrage ?", 'a': 'État : systemctl status service. Redémarrer : systemctl restart service. Activer au boot : systemctl enable service.', 'note': '💡 **Conseil Examen** : Ne confondez pas systemctl start (lance immédiatement) et systemctl enable (programme le lancement au boot).', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. Services Linux systemd', 'v_id': '2n3j4X5m-0', 'v_title': 'Gestion des Services systemd systemctl'}, {'id': 61, 'module': '🖥️ Administration Système', 'chap': '2. Outils de Recherche Linux', 'q': 'Comment chercher tous les fichiers .log modifiés depuis 7 jours et contenant le mot Failed ?', 'a': 'find /var/log -name "*.log" -mtime -7 -exec grep -H "Failed" {} +.', 'note': '💡 **Conseil Examen** : La commande grep -rnI "motif" /chemin cherche récursivement en ignorant les fichiers binaires.', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. CLI Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'Recherche Linux find & grep'}, {'id': 62, 'module': '🖥️ Administration Système', 'chap': '2. Scripting Bash', 'q': 'Que contiennent les variables spéciales 0, 0,  et -bash dans un script Bash ?', 'a': "0 : code de retour de la dernière commande (0 = succès). 0 : nombre d'arguments.  : tous les arguments. -bash : nom du script.", 'note': '💡 **Conseil Examen** : Testez toujours si [ 0 -eq 0 ] après une commande critique (ex: ping, rsync, compilation) pour gérer les erreurs.', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. Scripting Bash', 'v_id': '2n3j4X5m-0', 'v_title': 'Variables Spéciales Bash 0 0'}, {'id': 63, 'module': '🖥️ Administration Système', 'chap': '2. Redirections Linux', 'q': 'Quelle est la différence entre les opérateurs de redirection >, >> et 2>&1 en Bash ?', 'a': '> : écrase le fichier cible avec stdout. >> : ajoute à la fin du fichierTarget. 2>&1 : redirige stderr (canal 2) vers stdout (canal 1).', 'note': "💡 **Conseil Examen** : Pour masquer totalement les messages d'erreur d'une commande : commande 2> /dev/null.", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 2. CLI Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'Redirections & Pipes Linux'}, {'id': 64, 'module': '🖥️ Administration Système', 'chap': '3. Active Directory', 'q': "Quels sont les composants hiérarchiques d'un annuaire Active Directory (ADDS) ?", 'a': "Forêt (limite de sécurité) -> Domaine -> Unités d'Organisation (OU - conteneurs pour appliquer des GPO) -> Objets (Utilisateurs, Groupes, PC).", 'note': "💡 **Conseil Examen** : Les GPO ne s'appliquent directement qu'aux Unités d'Organisation (OU), pas aux groupes de sécurité !", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory', 'v_id': '8m9k3j4X5m0', 'v_title': 'Architecture Active Directory Forêt Domaine OU'}, {'id': 65, 'module': '🖥️ Administration Système', 'chap': '3. Active Directory GPO', 'q': "Quel est l'ordre d'application des stratégies de groupe (GPO) dans Active Directory ?", 'a': "Ordre LSDOU : 1. Local -> 2. Site -> 3. Domaine -> 4. Unité d'Organisation (OU).", 'note': "💡 **Conseil Examen** : La règle la plus spécifique (OU) s'applique en dernier et prévaut sur les règles parentes (Domaine/Site).", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory GPO', 'v_id': '8m9k3j4X5m0', 'v_title': "Ordre d'Application des GPO LSDOU"}, {'id': 66, 'module': '🖥️ Administration Système', 'chap': '3. Active Directory FSMO', 'q': "Quel est le rôle FSMO chargé de la synchronisation de l'heure et de la réinitialisation des mots de passe ?", 'a': 'Le rôle FSMO PDC Emulator (Primary Domain Controller Emulator).', 'note': '💡 **Conseil Examen** : Il existe 5 rôles FSMO dans un domaine AD (Schema Master, Domain Naming, PDC Emulator, RID Master, Infrastructure Master).', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory FSMO', 'v_id': '8m9k3j4X5m0', 'v_title': 'Rôles FSMO Active Directory'}, {'id': 67, 'module': '🖥️ Administration Système', 'chap': '3. Active Directory Services', 'q': "Quels sont les rôles serveurs nécessaires au fonctionnement d'un domaine Active Directory ?", 'a': 'ADDS (Active Directory Domain Services) et DNS (Domain Name System). Optionnellement DHCP.', 'note': '💡 **Conseil Examen** : Sans un DNS fonctionnel résolvant les enregistrements SRV (_ldap._tcp.dc._msdcs), les clients ne peuvent pas rejoindre le domaine.', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory Services', 'v_id': '8m9k3j4X5m0', 'v_title': 'Services ADDS & DNS'}, {'id': 68, 'module': '🖥️ Administration Système', 'chap': '3. Active Directory Kerberos', 'q': "Comment fonctionne l'authentification Kerberos dans un domaine Active Directory ?", 'a': "Le client s'authentifie auprès du KDC (Key Distribution Center - port 88) qui lui délivre un TGT (Ticket Granting Ticket) puis des tickets de service.", 'note': '💡 **Conseil Examen** : Kerberos requiert une synchronisation temporelle stricte entre les ordinateurs (écart max de 5 minutes par défaut).', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. Active Directory Kerberos', 'v_id': '8m9k3j4X5m0', 'v_title': 'Authentification Kerberos Active Directory'}, {'id': 69, 'module': '🖥️ Administration Système', 'chap': '3. PowerShell Active Directory', 'q': "Quelle est la commande PowerShell pour créer un compte utilisateur dans l'OU Ingénieurs ?", 'a': 'New-ADUser -Name "Alice Martin" -SamAccountName "amartin" -UserPrincipalName "amartin@ciel.local" -Path "OU=Ingenieurs,DC=ciel,DC=local" -Enabled .', 'note': "💡 **Conseil Examen** : N'oubliez pas le commutateur -Enabled , sinon le compte créé reste désactivé.", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. PowerShell AD', 'v_id': '8m9k3j4X5m0', 'v_title': 'PowerShell New-ADUser'}, {'id': 70, 'module': '🖥️ Administration Système', 'chap': '3. PowerShell Réseau', 'q': "Quelle commande PowerShell remplace telnet pour tester l'ouverture du port LDAPS 636 sur le serveur AD ?", 'a': 'Test-NetConnection -ComputerName "dc1.ciel.local" -Port 636.', 'note': "💡 **Conseil Examen** : L'alias court est tnc dc1.ciel.local -p 636. Il renvoie TcpTestSucceeded : True.", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 3. PowerShell Réseau', 'v_id': '8m9k3j4X5m0', 'v_title': 'PowerShell Test-NetConnection'}, {'id': 71, 'module': '🖥️ Administration Système', 'chap': '4. Virtualisation', 'q': 'Quelle est la différence entre un hyperviseur de Type 1 (Bare-Metal) et de Type 2 (Hébergé) ?', 'a': "Type 1 : s'installe directement sur le matériel (ex: VMware ESXi, Proxmox). Type 2 : s'installe au-dessus d'un OS hôte (ex: VMware Workstation, VirtualBox).", 'note': '💡 **Conseil Examen** : Les hyperviseurs Type 1 offrent de bien meilleures performances et sont utilisés en production industrielle.', 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 4. Virtualisation', 'v_id': 'rQ_1n8Y0o-0', 'v_title': 'Virtualisation Type 1 vs Type 2'}, {'id': 72, 'module': '🖥️ Administration Système', 'chap': '1. Privilèges Linux Sudo', 'q': "Quel fichier de configuration sécurisé régit les droits d'élévation de privilèges sudo et quelle commande l'édite ?", 'a': 'Le fichier /etc/sudoers, édité exclusivement avec la commande sécurisée visudo.', 'note': "💡 **Conseil Examen** : visudo vérifie la syntaxe avant de sauvegarder, évitant de bloquer l'accès root sur le système.", 'cours_ref': '📚 Encyclopédie des Cours -> 🖥️ SysAdmin -> 1. Privilèges Linux', 'v_id': '2n3j4X5m-0', 'v_title': 'Fichier sudoers & Commande visudo'}, {'id': 73, 'module': '🔌 Électronique & IoT', 'chap': "1. Lois d'Électricité", 'q': "Quelles sont les formules de la Loi d'Ohm, de la conductance G et de la Puissance Joule P ?", 'a': "Loi d'Ohm : U = R * I. Conductance : G = 1/R (Siemens S) => I = G * U. Puissance Joule : P = U * I = R * I^2 = U^2 / R.", 'note': '💡 **Conseil Examen** : En convention récepteur, la tension U et le courant I sont orientés en sens opposés.', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°1 Physique CIEL', 'v_id': '7m9k3j4X5m0', 'v_title': "Lois d'Ohm, Conductance & Puissance Joule"}, {'id': 74, 'module': '🔌 Électronique & IoT', 'chap': '1. Lois de Kirchhoff', 'q': 'Énoncez la Loi des Nœuds et la Loi des Mailles de Kirchhoff.', 'a': "Loi des Nœuds : la somme des intensités entrantes est égale à la somme des intensités sortantes (sum I_in = sum I_out). Loi des Mailles : la somme algébrique des tensions le long d'une maille fermée est nulle (sum U = 0).", 'note': '💡 **Conseil Examen** : Pour appliquer la loi des mailles, choisissez arbitrairement un sens de parcours et comptez positivement les tensions fléchées dans le sens du parcours.', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°1 Physique CIEL', 'v_id': '7m9k3j4X5m0', 'v_title': 'Lois de Kirchhoff Nœuds et Mailles'}, {'id': 75, 'module': '🔌 Électronique & IoT', 'chap': '1. Pont Diviseur', 'q': "Quelle est la formule de la tension de sortie U2 d'un pont diviseur de tension formé de R1 et R2 ?", 'a': 'U2 = E * (R2 / (R1 + R2)).', 'note': "💡 **Conseil Examen** : Formule d'isolation de R2 si U2 et E sont connus : R2 = (U2 * R1) / (E - U2).", 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°1 Physique CIEL', 'v_id': '7m9k3j4X5m0', 'v_title': 'Pont Diviseur de Tension'}, {'id': 76, 'module': '🔌 Électronique & IoT', 'chap': '2. Pont en H', 'q': 'Quel est le rôle du pont en H (ex: BTS7960 43A) et quelle règle de sécurité est critique ?', 'a': "Permet d'inverser le sens de rotation d'un moteur CC bipolaire. Règle critique : interdiction de fermer simultanément les interrupteurs d'une même branche (Shooting Through / court-circuit direct).", 'note': "💡 **Conseil Examen** : Le pilotage PWM s'effectue sur les broches R_PWM / L_PWM avec les broches R_EN / L_EN à l'état HAUT (5V).", 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°1 Le Pont en H', 'v_id': '8m9k3j4X5m0', 'v_title': 'Pont en H BTS7960 & Moteur CC'}, {'id': 77, 'module': '🔌 Électronique & IoT', 'chap': '3. Pull-Up / Pull-Down', 'q': 'Pourquoi utilise-t-on des résistances de Pull-Up ou Pull-Down (10 kΩ) sur les entrées numériques CMOS ?', 'a': 'Pour fixer un potentiel logique stable (HIGH ou LOW) au repos et éviter la haute impédance (état flottant / effet antenne aux parasites).', 'note': '💡 **Conseil Examen** : Sur Arduino ATmega328P, activez la résistance de tirage interne avec pinMode(pin, INPUT_PULLUP) (niveau repos = HIGH).', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°2 Pull-Up Pull-Down', 'v_id': '7m9k3j4X5m0', 'v_title': 'Résistances Pull-Up & Pull-Down'}, {'id': 78, 'module': '🔌 Électronique & IoT', 'chap': '4. PWM / MLI', 'q': "Quelle est la formule du rapport cyclique alpha et de la tension moyenne V_moy d'une PWM ?", 'a': 'Rapport cyclique : alpha = t_haut / T (entre 0 et 1). Tension moyenne : V_moy = alpha * V_max = V_max * (valeur_8bits / 255).', 'note': '💡 **Conseil Examen** : Pour analogWrite(pin, 127) sous 5V : alpha ~ 50% => V_moy = 2.5 V.', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°3 La PWM', 'v_id': '4jS0qUfE_y4', 'v_title': 'Signal PWM MLI & Rapport Cyclique'}, {'id': 79, 'module': '🔌 Électronique & IoT', 'chap': '5. Interruptions AVR', 'q': 'Comment fonctionne une interruption matérielle (ISR) et quel mot-clé qualifie une variable modifiée dans une ISR ?', 'a': "L'ISR interrompt le programme principal, sauvegarde le contexte, s'exécute rapidement, puis reprend le programme. La variable partagée doit être déclarée volatile.", 'note': "💡 **Conseil Examen** : Ne faites JAMAIS d'appels à delay() ou d'impressions Serial.print() à l'intérieur d'une routine d'interruption ISR !", 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°4 Interruptions', 'v_id': '7m9k3j4X5m0', 'v_title': 'Interruptions Matérielles & Mot-clé Volatile'}, {'id': 80, 'module': '🔌 Électronique & IoT', 'chap': '6. Mémoire Microcontrôleur', 'q': 'Quelles sont les 3 zones mémoires du microcontrôleur ATmega328P et leurs capacités ?', 'a': '1. Flash (32 Ko) : code programme non-volatile. 2. SRAM (2 Ko) : variables volatiles (Pile + Tas). 3. EEPROM (1 Ko) : données permanentes non-volatiles.', 'note': '💡 **Conseil Examen** : Pour stocker des chaînes constantes en Flash et économiser la SRAM limitée (2 Ko), utilisez la macro PROGMEM / F().', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°5 Mémoire UNO R3', 'v_id': '7m9k3j4X5m0', 'v_title': 'Mémoire Flash SRAM EEPROM ATmega328P'}, {'id': 81, 'module': '🔌 Électronique & IoT', 'chap': '7. Capteur 4-20 mA', 'q': 'Pourquoi la boucle de courant 4-20 mA industrielle est-elle dite à sécurité Live Zero ?', 'a': "Car un courant I = 0 mA signale immédiatement une rupture de câble ou une panne d'alimentation, contrairement au 0-20 mA où 0 mA peut être une mesure valide.", 'note': '💡 **Conseil Examen** : Pour lire un 4-20 mA sur une entrée CAN 0-5V, insérez une résistance de précision de 250 Ω en série (U = 250 * I => 1V à 5V).', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°6 Signal 4-20 mA', 'v_id': '9m9k3j4X5m0', 'v_title': 'Boucle de Courant 4-20 mA Industrielle'}, {'id': 82, 'module': '🔌 Électronique & IoT', 'chap': '8. CAN / ADC Quantum', 'q': 'Quelle est la formule du quantum q et de la valeur numérique N restituée par un CAN n bits ?', 'a': 'Quantum : q = V_ref / (2^n - 1). Valeur entière N = arrondi(V_entrée / q).', 'note': '💡 **Conseil Examen** : Pour un CAN 12 bits (2^12 - 1 = 4095) sous V_ref = 5.0 V : q = 5.0 / 4095 ~ 1.221 mV par LSB.', 'cours_ref': '🧮 Laboratoire de Calculs -> Quantum CAN 10/12/16 bits', 'v_id': '7m9k3j4X5m0', 'v_title': 'Convertisseur Analogique Numérique CAN ADC'}, {'id': 83, 'module': '🔌 Électronique & IoT', 'chap': '9. Capteurs & Métrologie', 'q': "Quelle est la différence entre Justesse et Fidélité d'un capteur de mesure ?", 'a': "Justesse : absence d'erreur systématique (moyenne des mesures centrée sur la valeur vraie). Fidélité : répétabilité des mesures (faible dispersion / écart-type).", 'note': '💡 **Conseil Examen** : Précision globale = Justesse + Fidélité. La sensibilité est la pente d S / d E de la caractéristique de transfert.', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°7 Métrologie Capteurs', 'v_id': '7m9k3j4X5m0', 'v_title': 'Métrologie Capteurs Justesse Fidélité'}, {'id': 84, 'module': '🔌 Électronique & IoT', 'chap': '10. Relais & Commande', 'q': "Quelle composant est obligatoire en anti-parallèle sur la bobine d'un relais électromécanique ?", 'a': "Une Diode de Roue Libre (ex: 1N4007) pour évacuer la surtension d'auto-induction (e = -L di/dt) lors de l'ouverture du transistor de commande.", 'note': '💡 **Conseil Examen** : Un relais statique (SSR) utilise un optocoupleur et un Triac/MOSFET, offrant une commutation silencieuse sans usure mécanique.', 'cours_ref': '📄 Fiches Savoir -> Fiche Savoir N°8 Relais', 'v_id': '7m9k3j4X5m0', 'v_title': 'Relais & Diode de Roue Libre'}, {'id': 85, 'module': '🔌 Électronique & IoT', 'chap': '11. Bus I2C', 'q': "Quelles sont les 2 lignes du bus I2C et comment est géré l'adressage des esclaves ?", 'a': "SDA (Serial Data) et SCL (Serial Clock), bidirectionnelles à drain ouvert avec résistances de Pull-Up. L'adressage s'effectue sur 7 bits (128 adresses).", 'note': '💡 **Conseil Examen** : Chaque trame I2C débute par une condition START (SDA descend quand SCL est HAUT) et se termine par STOP.', 'cours_ref': '📚 Encyclopédie des Cours -> 🔌 Électronique -> Bus I2C', 'v_id': '7m9k3j4X5m0', 'v_title': 'Bus I2C SDA SCL'}, {'id': 86, 'module': '🔌 Électronique & IoT', 'chap': '12. Bus SPI', 'q': 'Quelles sont les 4 lignes du bus SPI et quel est son mode de fonctionnement ?', 'a': 'MOSI (Master Out Slave In), MISO (Master In Slave Out), SCLK (Horloge), CS/SS (Chip Select). Bus synchrone Full-Duplex très rapide.', 'note': "💡 **Conseil Examen** : La ligne CS/SS est active au niveau BAS (0V). Il faut autant de lignes CS séparées que d'esclaves SPI connectés au maître.", 'cours_ref': '📚 Encyclopédie des Cours -> 🔌 Électronique -> Bus SPI', 'v_id': '7m9k3j4X5m0', 'v_title': 'Bus SPI MOSI MISO SCLK CS'}, {'id': 87, 'module': '🔌 Électronique & IoT', 'chap': '13. Bus CAN', 'q': "Comment fonctionne la signalisation différentielle et l'arbitrage non destructif CSMA/CR du Bus CAN ?", 'a': 'Bus 2 fils CAN_H et CAN_L avec terminaisons 120 Ω. Bit dominant (0) : V_diff = 2V. Bit récessif (1) : V_diff = 0V. Le bit dominant (0) écrase le récessif (1).', 'note': "💡 **Conseil Examen** : Lors de l'arbitrage d'identifiants, l'ID de valeur numérique la plus faible possède la priorité absolue (ex: 0x001 prioritaire sur 0x01A).", 'cours_ref': '📚 Encyclopédie des Cours -> 🔌 Électronique -> Bus CAN', 'v_id': '10m9k3j4X5m0', 'v_title': 'Bus CAN Differential CSMA/CR'}, {'id': 88, 'module': '🔌 Électronique & IoT', 'chap': '14. Modbus RTU / RS-485', 'q': 'Quels sont les rôles des Code Fonction 03 et 16 dans le protocole Modbus RTU sur RS-485 ?', 'a': 'Code Fonction 03 (0x03) : Lecture de mots de registres (Read Holding Registers). Code Fonction 16 (0x10) : Écriture de mots multiples (Write Multiple Registers).', 'note': "💡 **Conseil Examen** : Les trames Modbus RTU se terminent par un contrôle d'erreur de 2 octets CRC-16 (Cyclic Redundancy Check).", 'cours_ref': '📚 Encyclopédie des Cours -> 🔌 Électronique -> Modbus RTU', 'v_id': '11m9k3j4X5m0', 'v_title': 'Modbus RTU RS-485'}, {'id': 89, 'module': '🔌 Électronique & IoT', 'chap': '1. Circuits RC', 'q': "Quelle est la formule de la constante de temps tau d'un circuit RC et de la tension de charge u_C(t) ?", 'a': 'Tau = R * C (secondes). Charge : u_C(t) = E * (1 - e^(-t/tau)). Décharge : u_C(t) = E * e^(-t/tau).', 'note': '💡 **Conseil Examen** : À t = tau, la charge atteint 63.2% de E. À t = 5*tau, la charge est considérée comme totale (99.3% de E).', 'cours_ref': '📊 Mathématiques Appliquées -> Fonctions, Exponentielle & Logarithme', 'v_id': '13m9k3j4X5m0', 'v_title': 'Circuit RC Constante de Temps Tau'}, {'id': 90, 'module': '🔌 Électronique & IoT', 'chap': '1. Mesures Oscilloscope', 'q': "Comment calculer la tension efficace V_eff et la fréquence f d'un signal sinusoïdal sur oscilloscope ?", 'a': "V_eff = V_max / sqrt(2) ~ 0.707 * V_max. Fréquence : f = 1 / T (Hz), où T est la période mesurée sur l'axe horizontal en ms/div.", 'note': "💡 **Conseil Examen** : N'oubliez pas que V_max = V_pp / 2 (tension crête-à-crête mesurée du bas au haut de la sinusoïde).", 'cours_ref': '📺 Lab Oscilloscope & Mesures Physiques', 'v_id': '7m9k3j4X5m0', 'v_title': 'Mesures Oscilloscope Vpp Veff Fréquence'}, {'id': 91, 'module': '📐 Modélisation UML & SysML', 'chap': '1. Suites Arithmétiques', 'q': "Quelles sont les formules de récurrence, explicite et de somme des termes d'une suite arithmétique ?", 'a': 'Récurrence : u_(n+1) = u_n + r. Explicite : u_n = u_0 + n * r. Somme : S_N = N * ((u_premier + u_dernier) / 2).', 'note': '💡 **Conseil Examen** : La somme de n premiers termes de u_0 à u_(n-1) comporte exactement n termes.', 'cours_ref': '📊 Mathématiques Appliquées -> Suites Arithmétiques', 'v_id': '12m9k3j4X5m0', 'v_title': 'Suites Arithmétiques Formules & Somme'}, {'id': 92, 'module': '📐 Modélisation UML & SysML', 'chap': '1. Suites Géométriques', 'q': "Quelles sont les formules de récurrence, explicite et de somme des termes d'une suite géométrique ?", 'a': 'Récurrence : u_(n+1) = u_n * q. Explicite : u_n = u_0 * q^n. Somme : S_N = u_premier * ((1 - q^N) / (1 - q)) (si q != 1).', 'note': '💡 **Conseil Examen** : Une atténuation de 15% de puissance optique correspond à une raison q = 1 - 0.15 = 0.85.', 'cours_ref': '📊 Mathématiques Appliquées -> Suites Géométriques', 'v_id': '12m9k3j4X5m0', 'v_title': 'Suites Géométriques Atténuation & Somme'}, {'id': 93, 'module': '📐 Modélisation UML & SysML', 'chap': '1. Limites de Suites', 'q': "Quel est le comportement à l'infini d'une suite géométrique u_n = u_0 * q^n pour u_0 > 0 ?", 'a': 'Si q > 1 : lim u_n = +infini (divergence). Si 0 < q < 1 : lim u_n = 0 (convergence vers 0 / signal éteint). Si q = 1 : constante.', 'note': "💡 **Conseil Examen** : Si 0 < q < 1, le signal s'atténue progressivement jusqu'à devenir indétectable.", 'cours_ref': '📊 Mathématiques Appliquées -> Limites de Suites', 'v_id': '12m9k3j4X5m0', 'v_title': 'Limites de Suites Géométriques'}, {'id': 94, 'module': '📐 Modélisation UML & SysML', 'chap': '1. Étude de Variations', 'q': "Quelle est la méthode pour étudier le sens de variation d'une suite u_n = f(n) via la dérivée ?", 'a': "1. Poser f(x) sur [0, +infini[. 2. Calculer f'(x). 3. Étudier le signe de f'(x). 4. Si f'(x) > 0, f est croissante donc la suite (u_n) est croissante.", 'note': "💡 **Conseil Examen** : Le dénominateur d'une dérivée de quotient (u/v)' = (u'v - uv') / v^2 est un carré toujours strictly positif.", 'cours_ref': '📊 Mathématiques Appliquées -> Méthode de la Dérivée', 'v_id': '12m9k3j4X5m0', 'v_title': 'Méthode de la Dérivée u_n = f(n)'}, {'id': 95, 'module': '📐 Modélisation UML & SysML', 'chap': '2. Fonctions Exp & Ln', 'q': 'Quelles sont les dérivées et propriétés algébriques remarquables des fonctions e^x et ln(x) ?', 'a': "(e^x)' = e^x, (e^(u(x)))' = u'(x) e^(u(x)). (ln(x))' = 1/x, (ln(u(x)))' = u'(x)/u(x). ln(a * b) = ln(a) + ln(b), ln(1/a) = -ln(a).", 'note': "💡 **Conseil Examen** : La fonction e^x est strictement positive pour tout x réel (e^x > 0). ln(x) n'est définie que pour x > 0.", 'cours_ref': '📊 Mathématiques Appliquées -> Fonctions Exp & Ln', 'v_id': '13m9k3j4X5m0', 'v_title': 'Fonctions Exponentielle & Logarithme Népérien'}, {'id': 96, 'module': '📐 Modélisation UML & SysML', 'chap': '2. Calcul de Décibels', 'q': 'Quelles sont les formules du gain/atténuation en Décibels pour la Puissance P et la Tension V ?', 'a': 'Puissance : A_dB = 10 * log10(P2 / P1). Tension : A_v_dB = 20 * log10(V2 / V1).', 'note': '💡 **Conseil Examen** : Une division par 2 de la puissance correspond à une atténuation de -3 dB (10 * log10(0.5) ~ -3.01 dB).', 'cours_ref': '📊 Mathématiques Appliquées -> Calculs de Décibels', 'v_id': '13m9k3j4X5m0', 'v_title': 'Calculs de Gain & Atténuation en Décibels'}, {'id': 97, 'module': '📐 Modélisation UML & SysML', 'chap': '3. SysML BDD', 'q': 'Quel est le rôle du diagramme SysML BDD (Block Definition Diagram) ?', 'a': 'Il représente la structure globale du système, la hiérarchie des blocs, leurs compositions (black diamond) et leurs propriétés.', 'note': '💡 **Conseil Examen** : La composition forte (losange noir) signifie que la destruction du bloc parent entraîne la destruction des sous-blocs.', 'cours_ref': '📐 Laboratoire UML & SysML -> Diagrammes SysML', 'v_id': '14m9k3j4X5m0', 'v_title': 'Diagramme SysML BDD Structure Globale'}, {'id': 98, 'module': '📐 Modélisation UML & SysML', 'chap': '3. SysML IBD', 'q': 'À quoi sert le diagramme SysML IBD (Internal Block Diagram) et que représentent ses Flow Ports ?', 'a': "Il décrit l'assemblage interne d'un bloc, les liaisons entre sous-composants via des ports d'interfaçage physiques ou de flux de données (Flow Ports).", 'note': '💡 **Conseil Examen** : Les flèches sur les Flow Ports indiquent la direction des flux de données (in, out, inout).', 'cours_ref': '📐 Laboratoire UML & SysML -> Diagrammes SysML', 'v_id': '14m9k3j4X5m0', 'v_title': 'Diagramme SysML IBD Flow Ports'}, {'id': 99, 'module': '📐 Modélisation UML & SysML', 'chap': '3. SysML Requirement', 'q': 'Quelles sont les deux relations clés dans un diagramme SysML Requirement Diagram ?', 'a': "deriveReqt (une exigence dérive d'une autre) et verify (un cas de test ou sous-système vérifie qu'une exigence est satisfaite).", 'note': '💡 **Conseil Examen** : Chaque exigence possède un identifiant unique (Id) et un texte de critère de satisfaction.', 'cours_ref': '📐 Laboratoire UML & SysML -> Diagrammes SysML', 'v_id': '14m9k3j4X5m0', 'v_title': 'Requirement Diagram & Traçabilité'}, {'id': 100, 'module': '📐 Modélisation UML & SysML', 'chap': '4. UML Diagramme de Classes', 'q': 'Quelle est la différence entre une Agrégation (losange blanc) et une Composition (losange noir) en UML ?', 'a': "Agrégation (losange blanc) : relation faible, l'élément contenu peut exister indépendamment. Composition (losange noir) : relation forte, cycle de vie lié.", 'note': '💡 **Conseil Examen** : La multiplicité 1..* indique un-à-plusieurs, 0..1 indique optionnel.', 'cours_ref': '📐 Laboratoire UML & SysML -> Diagrammes UML', 'v_id': '15m9k3j4X5m0', 'v_title': 'Diagramme de Classes UML Associations'}, {'id': 101, 'module': '📐 Modélisation UML & SysML', 'chap': '4. UML Diagramme de Séquence', 'q': 'Que représentent les fragments alt et loop dans un diagramme de séquence UML ?', 'a': "alt : bloc conditionnel (alternative Si / Sinon). loop : boucle d'itération répétitive (Tant que / Pour).", 'note': '💡 **Conseil Examen** : Les lignes verticales représentent la ligne de vie des objets. Les flèches pleines sont synchrones, flèches ouvertes asynchrones.', 'cours_ref': '📐 Laboratoire UML & SysML -> Diagrammes UML', 'v_id': '15m9k3j4X5m0', 'v_title': 'Diagramme de Séquence UML Fragments'}, {'id': 102, 'module': '📐 Modélisation UML & SysML', 'chap': '4. UML États-Transitions', 'q': "Quels sont les éléments constituants d'une transition dans un diagramme d'États-Transitions UML ?", 'a': 'Événement déclencheur [ Condition de garde ] / Action exécutée (ex: boutonAppuye [ tension > 3.3V ] / allumerLED()).', 'note': "💡 **Conseil Examen** : La condition de garde [ ] est une condition booléenne qui doit être VRAIE pour que la transition franchisse l'état.", 'cours_ref': '📐 Laboratoire UML & SysML -> Diagrammes UML', 'v_id': '15m9k3j4X5m0', 'v_title': "Diagramme d'États-Transitions UML"}, {'id': 103, 'module': '📐 Modélisation UML & SysML', 'chap': '5. Qualification E6 & PVL', 'q': "Qu'est-ce qu'un Plan de Validation Logicielle (PVL) pour l'épreuve du Projet E6 ?", 'a': 'Un document formalisant la matrice de traçabilité des exigences, décrivant la procédure de test, le résultat attendu et le statut (PASS / FAIL).', 'note': '💡 **Conseil Examen** : Chaque test du PVL doit être directement associé à une exigence du Cahier des Charges Fonctionnel (CdCf).', 'cours_ref': '🧪 Qualification & Tests E6', 'v_id': '16m9k3j4X5m0', 'v_title': 'Plan de Validation Logicielle PVL E6'}, {'id': 104, 'module': '📐 Modélisation UML & SysML', 'chap': '5. Tests Automated Pytest', 'q': 'Comment rédiger une fonction de test automatisée sous Python avec le framework pytest ?', 'a': 'def test_calcul_quantum(): assert calcul_quantum(5.0, 12) == pytest.approx(0.001221, rel=1e-3)', 'note': '💡 **Conseil Examen** : Les fonctions de test doivent impérativement commencer par le mot-clé test_ pour être détectées par pytest.', 'cours_ref': '🧪 Qualification & Tests E6 -> Framework Pytest', 'v_id': '16m9k3j4X5m0', 'v_title': 'Tests Unitaires & Automatisés Pytest'}, {'id': 105, 'module': '📐 Modélisation UML & SysML', 'chap': '5. Gestion de Projet Gantt', 'q': "Qu'est-ce que le Chemin Critique dans le suivi de projet E6 (Diagramme de Gantt) ?", 'a': 'La séquence de tâches sans aucune marge. Tout retard sur une tâche du chemin critique décale la date de fin globale du projet.', 'note': '💡 **Conseil Examen** : Identifiez les tâches jalons (Milestones) de durée nulle marquant la fin des phases clés (ex: Validation du PVL).', 'cours_ref': '📋 Planning de Projet E6 (Gantt)', 'v_id': '16m9k3j4X5m0', 'v_title': 'Diagramme de Gantt & Chemin Critique E6'}]


GRAND_QUIZ_DATA = [{'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)', 'expl': 'Pour faire 4 sous-réseaux (2^2), il faut emprunter 2 bits au masque /24, ce qui donne un masque /26, soit 255.255.255.192.', 'mod': '📶 Réseaux & Télécoms', 'options': ['255.255.255.128 (/25)', '255.255.255.192 (/26)', '255.255.255.224 (/27)', '255.255.255.240 (/28)'], 'q': 'Q1 : Vous disposez du réseau 192.168.10.0/24. Vous devez créer 4 sous-réseaux de taille égale. Quel sera le nouveau masque ?', 'rep': '255.255.255.192 (/26)'}, {'chap': '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN', 'expl': "Sur une sous-interface de routeur (ex: g0/0.10), on configure l'encapsulation de type trunking à l'aide de la commande 'encapsulation dot1Q 10' où 10 est l'ID du VLAN.", 'mod': '📶 Réseaux & Télécoms', 'options': ['switchport access vlan 10', 'encapsulation dot1Q 10', 'trunk allowed vlan 10', 'ip route vlan 10'], 'q': "Q2 : Quelle commande Cisco IOS permet d'activer le routage inter-VLAN sur une sous-interface de routeur en spécifiant l'encapsulation 802.1Q pour le VLAN 10 ?", 'rep': 'encapsulation dot1Q 10'}, {'chap': '1. Langage C++ : Mémoire, Pointeurs & POO', 'expl': 'Une classe comportant au moins une méthode virtuelle pure (déclarée avec = 0) est appelée classe de base abstraite. Elle ne peut pas être instanciée.', 'mod': '💻 Programmation / Dev', 'options': ['Une classe scellée (sealed)', 'Une interface statique', 'Une classe de base abstraite', 'Une classe dérivée'], 'q': 'Q3 : En C++, si une classe B hérite publiquement de la classe A, et que la classe A possède au moins une méthode virtuelle pure, comment qualifie-t-on la classe A ?', 'rep': 'Une classe de base abstraite'}, {'chap': '1. Permissions GNU/Linux & Services système', 'expl': "'u+x' signifie User + eXecution (droit d'exécution pour le propriétaire). 'g-w' signifie Group - Write (retrait du droit d'écriture pour le groupe).", 'mod': '🖥️ Administration Système', 'options': ["Ajoute le droit d'exécution au propriétaire et retire le droit d'écriture au groupe", "Ajoute l'écriture pour l'utilisateur et retire l'exécution pour le groupe", 'Donne tous les droits au propriétaire et supprime les droits du groupe', 'Rend le fichier exécutable par tout le monde'], 'q': "Q4 : Quel est l'effet de la commande Linux 'chmod u+x,g-w script.sh' ?", 'rep': "Ajoute le droit d'exécution au propriétaire et retire le droit d'écriture au groupe"}, {'chap': '1. Échantillonnage, CAN/CNA & Théorème de Shannon', 'expl': 'q = 5 / (2^12 - 1) = 5 / 4095 = 0.001221 V. N = arrondi(3.12 / 0.001221) = 2555. (Sujet officiel BTS CIEL 2025).', 'mod': '🔌 Électronique & IoT', 'options': ['2048', '2555', '2560', '3120'], 'q': "Q5 : Un convertisseur analogique-numérique (CAN) possède une résolution de 12 bits et une plage d'entrée de 0 à 5V. Quelle est la valeur numérique entière générée pour une tension de 3.12V ?", 'rep': '2555'}, {'chap': '1. Modèle OSI vs TCP/IP & Encapsulation', 'expl': "IPsec opère au niveau de la couche Réseau (couche 3) pour chiffrer et encapsuler l'intégralité du trafic entre deux passerelles réseau.", 'mod': '📶 Réseaux & Télécoms', 'options': ['TLS/SSL', 'IPsec', 'HTTPS', 'WPA3'], 'q': 'Q6 : Quel protocole de sécurisation réseau fournit une authentification et un chiffrement robustes au niveau de la couche réseau (Couche 3 du modèle OSI) ?', 'rep': 'IPsec'}, {'chap': '2. Services Active Directory & GPO (Windows Server)', 'expl': "Les stratégies de groupe (GPO) permettent d'appliquer de façon centralisée des configurations de sécurité et des environnements aux postes de travail.", 'mod': '🖥️ Administration Système', 'options': ['Enregistrements DNS', 'Base SAM locale', 'GPO (Group Policy Object)', 'Serveur DHCP'], 'q': "Q7 : Quel composant Active Directory gère l'application centralisée de stratégies de groupe sur les ordinateurs du domaine ?", 'rep': 'GPO (Group Policy Object)'}, {'chap': '2. Protocoles IoT (MQTT & LoRaWAN)', 'expl': "LoRaWAN est conçu pour transmettre de petits volumes de données sur des distances kilométriques à partir d'objets alimentés sur piles.", 'mod': '🔌 Électronique & IoT', 'options': ['Wi-Fi 6', 'LoRaWAN', 'WebSockets', 'HTTP REST'], 'q': 'Q8 : Quel protocole IoT est particulièrement optimisé pour la communication longue portée (LPWAN) avec une consommation ultra-faible ?', 'rep': 'LoRaWAN'}, {'chap': '2. Scripting & Automatisation en Python (Réseaux)', 'expl': 'La commande \'git commit -m "message"\' crée un point de sauvegarde local de vos modifications indexées dans l\'historique du dépôt.', 'mod': '💻 Programmation / Dev', 'options': ['git push', 'git save', 'git commit', 'git checkout'], 'q': "Q9 : Dans Git, quelle commande permet d'enregistrer localement vos modifications indexées en y associant un message explicatif ?", 'rep': 'git commit'}, {'chap': '2. Diagrammes SysML (BDD, IBD, Exigences)', 'expl': "L'IBD (Internal Block Diagram) représente l'agencement interne et les flux de matière, d'énergie ou de données reliant les ports d'un bloc.", 'mod': '📐 Modélisation UML & SysML', 'options': ['BDD (Block Definition Diagram)', 'IBD (Internal Block Diagram)', 'Requirement Diagram', 'Use Case Diagram'], 'q': 'Q10 : En SysML, quel diagramme permet de modéliser les flux internes (matière, énergie, données) entre les ports des blocs ?', 'rep': 'IBD (Internal Block Diagram)'}, {'chap': '5. Modulations & Transmissions de Signaux (FSK, ASK, PSK, QAM)', 'expl': 'Une modulation 16-QAM code n = log2(16) = 4 bits par symbole. Le débit binaire est D = R * n. Donc R = D / n = 9600 / 4 = 2400 Bauds.', 'mod': '📶 Réseaux & Télécoms', 'options': ['2400 Bauds', '4800 Bauds', '9600 Bauds', '19200 Bauds'], 'q': 'Q11 : Quelle est la rapidité de modulation minimale (en Bauds) pour transmettre un débit binaire de 9600 bps avec une modulation 16-QAM ?', 'rep': '2400 Bauds'}, {'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)', 'expl': "Le protocole NDP (Neighbor Discovery Protocol) s'appuie sur ICMPv6 pour réaliser la découverte d'adresse physique (ARP en IPv4), la détection d'adresses dupliquées, et la découverte de routeurs (SLAAC).", 'mod': '📶 Réseaux & Télécoms', 'options': ['ICMPv4', 'NDP (Neighbor Discovery Protocol)', 'DHCPv6', 'SNDP'], 'q': "Q12 : Quel protocole de l'architecture IPv6 prend en charge la découverte des voisins et l'auto-configuration SLAAC, remplaçant le protocole ARP ?", 'rep': 'NDP (Neighbor Discovery Protocol)'}, {'chap': '3. Durcissement & Filtrage : Pare-feux (Linux) & Port Security', 'expl': "Le mode 'protect' rejette silencieusement le trafic suspect sans bloquer l'interface et sans incrémenter le compteur de violation, à l'inverse du mode 'restrict' qui l'incrémente.", 'mod': '🔒 Cybersécurité', 'options': ['switchport port-security violation shutdown', 'switchport port-security violation restrict', 'switchport port-security violation protect', 'switchport port-security violation disable'], 'q': "Q13 : Dans un commutateur Cisco, comment configure-t-on le Port Security pour rejeter silencieusement le trafic suspect en cas d'intrusion, sans désactiver l'interface ?", 'rep': 'switchport port-security violation protect'}, {'chap': '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)', 'expl': "La poignée de main TLS commence par le 'Client Hello' (propositions d'algorithmes), suivi du 'Server Hello' (choix d'algorithme), de l'envoi des certificats par le serveur, de l'échange de clés (Key Exchange) et de la validation finale ('Finished').", 'mod': '🔒 Cybersécurité', 'options': ['Client Hello -> Server Hello -> Exchange Certificates -> Key Exchange -> Finished', 'Server Hello -> Client Hello -> Exchange Certificates -> Finished', 'Exchange Certificates -> Client Hello -> Server Hello -> Finished', 'Client Hello -> Exchange Certificates -> finished'], 'q': "Q14 : Quel est l'ordre des messages échangés lors de la poignée de main TLS (TLS Handshake) au début d'une connexion HTTPS ?", 'rep': 'Client Hello -> Server Hello -> Exchange Certificates -> Key Exchange -> Finished'}, {'chap': '3. Threads, Mutex & Sockets Multi-Client (C++11)', 'expl': "std::lock_guard utilise le principe RAII. Si une fonction lève une exception ou se termine prématurément par un 'return', le destructeur de std::lock_guard est invoqué et le mutex est libéré, évitant un interblocage permanent (Deadlock).", 'mod': '💻 Programmation / Dev', 'options': ['Il permet de verrouiller plusieurs mutex simultanément de manière statique', 'Il garantit le déverrouillage automatique en fin de bloc, même si une exception est levée', "Il est plus rapide à l'exécution de 50%", 'Il supprime automatiquement les conditions de concurrence'], 'q': "Q15 : En C++, quel est le principal avantage de l'utilisation de 'std::lock_guard' par rapport à l'appel direct de '.lock()' et '.unlock()' sur un mutex ?", 'rep': 'Il garantit le déverrouillage automatique en fin de bloc, même si une exception est levée'}, {'chap': '2. Scripting & Automatisation en Python (Réseaux)', 'expl': "La méthode 'accept()' est bloquante. Dès qu'un client se connecte, elle renvoie une nouvelle socket dédiée à la communication avec ce client, ainsi qu'un tuple contenant son adresse IP et son port.", 'mod': '💻 Programmation / Dev', 'options': ['bind()', 'listen()', 'connect()', 'accept()'], 'q': "Q16 : Quelle méthode de la bibliothèque 'socket' en Python bloque l'exécution du serveur et attend la connexion d'un client distant ?", 'rep': 'accept()'}, {'chap': '3. Gestion Avancée Linux & Sécurisation (ACLs, SUID/SGID, umask)', 'expl': "La commande 'umask 002' soustrait le bit d'écriture aux Autres (Others) lors de la création d'un fichier (666 - 002 = 664) ou d'un dossier (777 - 002 = 775).", 'mod': '🖥️ Administration Système', 'options': ['chmod 775', 'umask 002', 'setfacl -m umask:002', 'chown 002'], 'q': "Q17 : Sous Linux, comment définit-on un umask égal à 002 pour s'assurer que les nouveaux répertoires de projet soient créés par défaut avec les droits 775 (rwxrwxr-x) ?", 'rep': 'umask 002'}, {'chap': '4. Bus Réseau Industriel CAN (Controller Area Network)', 'expl': "Le bus CAN utilise le protocole CSMA/CR. Lorsqu'un bit dominant (0) est émis en même temps qu'un bit récessif (1), l'état dominant (0) l'emporte physiquement sur la ligne. Le nœud émettant le bit récessif détecte cette différence et s'arrête instantanément de transmettre.", 'mod': '🔌 Électronique & IoT', 'options': ['Le protocole CSMA/CD basé sur la détection de collision physique', "L'identifiant de la trame et la priorité des bits dominants (0) sur les bits récessifs (1)", "Un jeton d'émission circulant d'un contrôleur à l'autre", "Le signal d'horloge commun SCL"], 'q': "Q18 : Sur le bus réseau de communication CAN, quel élément garantit l'arbitrage non destructif et instantané lorsque deux nœuds transmettent au même moment ?", 'rep': "L'identifiant de la trame et la priorité des bits dominants (0) sur les bits récessifs (1)"}, {'chap': "1. Modélisation Logicielle UML (Classes, Séquence, Cas d'Utilisation)", 'expl': "En diagramme de classes UML, l'agrégation se dessine avec un losange vide ◇ à l'extrémité du contenant, tandis que la composition se dessine avec un losange plein ◆.", 'mod': '📐 Modélisation UML & SysML', 'options': ['Agrégation = Losange vide ◇ | Composition = Losange plein ◆', 'Agrégation = Losange plein ◆ | Composition = Losange vide ◇', 'Agrégation = Flèche simple -> | Composition = Flèche double =>', 'Agrégation = Ligne pointillée | Composition = Ligne continue'], 'q': "Q19 : En UML, comment représente-t-on graphiquement une relation d'agrégation simple par rapport à une relation de composition ?", 'rep': 'Agrégation = Losange vide ◇ | Composition = Losange plein ◆'}, {'chap': "3. Diagramme d'États-Transitions UML", 'expl': "Le diagramme de machine à états (State Machine) modélise le cycle de vie réactif d'un objet, en décrivant ses états, ses transitions et ses actions d'états (entry, do, exit).", 'mod': '📐 Modélisation UML & SysML', 'options': ['Le diagramme de séquence', "Le diagramme de cas d'utilisation", 'Le diagramme de machine à états', "Le diagramme d'activité"], 'q': "Q20 : Quel diagramme d'États-Transitions UML permet de modéliser le comportement réactif d'un objet en définissant des actions à l'entrée et à la sortie d'un état ?", 'rep': 'Le diagramme de machine à états'}, {'chap': '1. Modèle OSI vs TCP/IP & Encapsulation', 'expl': "OSPF (Open Shortest Path First) est un protocole de routage dynamique interne à état de lien (Link-State) qui utilise l'algorithme de Dijkstra pour calculer le chemin le plus court.", 'mod': '📶 Réseaux & Télécoms', 'options': ['RIP', 'BGP', 'OSPF', 'EIGRP'], 'q': "Q21 : Quel est le protocole de routage dynamique interne de type 'État de lien' le plus utilisé, fonctionnant avec le découpage de zones (Areas) ?", 'rep': 'OSPF'}, {'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)', 'expl': "Pour /28, la taille de sous-réseau est de 16 IP. Les sous-réseaux commencent à 172.16.50.0, .16, .32, .48, etc. L'IP .40 est dans le sous-réseau .32. L'adresse réseau est .32, et la première IP d'hôte utilisable est .33.", 'mod': '📶 Réseaux & Télécoms', 'options': ['172.16.50.32', '172.16.50.33', '172.16.50.41', '172.16.50.1'], 'q': "Q22 : En adressage IPv4, quelle est la première adresse IP d'hôte utilisable pour le sous-réseau contenant l'hôte 172.16.50.40/28 ?", 'rep': '172.16.50.33'}, {'chap': '1. Cryptographie : Symétrique, Asymétrique & Hachage', 'expl': "L'autorité de certification est un tiers de confiance qui valide l'identité du possesseur du certificat en le signant avec sa propre clé privée, permettant l'utilisation de HTTPS en toute confiance.", 'mod': '🔒 Cybersécurité', 'options': ['Chiffrer les requêtes de base de données à la volée', 'Générer et signer numériquement des certificats X.509 pour lier une clé publique à une identité', 'Bloquer les attaques par déni de service distribué (DDoS)', 'Détecter les intrusions physiques sur les commutateurs Cisco'], 'q': "Q23 : En cybersécurité, quelle est la principale fonction d'une autorité de certification (CA) ?", 'rep': 'Générer et signer numériquement des certificats X.509 pour lier une clé publique à une identité'}, {'chap': '3. Gestion Avancée Linux & Sécurisation (ACLs, SUID/SGID, umask)', 'expl': "La commande 'getfacl' permet d'afficher les permissions étendues (ACLs) configurées sur un fichier ou un répertoire Linux.", 'mod': '🖥️ Administration Système', 'options': ['ls -la', 'getfacl', 'setfacl -l', 'acl-list'], 'q': "Q24 : Quelle commande Linux permet de lister de manière détaillée les listes de contrôle d'accès (ACL) configurées sur un dossier spécifique ?", 'rep': 'getfacl'}, {'chap': '1. Langage C++ : Mémoire, Pointeurs & POO', 'expl': 'RAII est le paradigme fondamental en C++. Les classes encapsulent la gestion des ressources dans leur constructeur et leur destructeur (comme std::lock_guard ou std::unique_ptr), rendant la gestion de ressources automatique et sûre.', 'mod': '💻 Programmation / Dev', 'options': ["L'héritage virtuel", 'Le patron de conception (design pattern)', 'Le RAII (Resource Acquisition Is Initialization)', 'Le polymorphisme dynamique'], 'q': "Q25 : En C++, comment s'appelle le mécanisme qui permet de s'assurer qu'une ressource (comme de la mémoire ou un verrou) est acquise lors de l'instanciation d'un objet et libérée automatiquement lors de sa destruction ?", 'rep': 'Le RAII (Resource Acquisition Is Initialization)'}, {'chap': '2. Protocoles IoT (MQTT & LoRaWAN)', 'expl': 'MQTT est le standard de fait en IoT industriel pour transmettre de manière asynchrone des télémétries à un Broker via un modèle Publish/Subscribe.', 'mod': '🔌 Électronique & IoT', 'options': ['HTTP REST', 'FTP', 'MQTT', 'SNMP'], 'q': "Q26 : Dans un projet d'examen E6, quel protocole est typiquement utilisé pour transmettre de manière fiable et périodique des mesures de capteurs IoT à travers une passerelle via des Topics ?", 'rep': 'MQTT'}, {'chap': '3. Bus de Communication Série (I2C, SPI, UART)', 'expl': "C'est toujours le maître qui prend l'initiative de la communication et génère le signal d'horloge de synchronisation SCL.", 'mod': '🔌 Électronique & IoT', 'options': ['Le circuit de tirage (Pull-up)', 'Le composant maître (Master)', "N'importe quel esclave actif", 'Le courtier réseau'], 'q': "Q27 : Sur un bus de communication I2C, quel est le composant responsable de générer l'horloge SCL servant de cadencement ?", 'rep': 'Le composant maître (Master)'}, {'chap': '2. Diagrammes SysML (BDD, IBD, Exigences)', 'expl': "Le BDD (Block Definition Diagram) permet d'avoir une vision globale statique de la structure du système, équivalent SysML du diagramme de classes UML.", 'mod': '📐 Modélisation UML & SysML', 'options': ["Le diagramme d'exigences (RD)", 'Le diagramme de définition de bloc (BDD)', "Le diagramme de cas d'utilisation (UCD)", 'Le diagramme de séquence (SD)'], 'q': "Q28 : Quel diagramme SysML modélise le découpage hiérarchique et les relations structurelles globales (physiques ou logiques) entre les blocs d'un système ?", 'rep': 'Le diagramme de définition de bloc (BDD)'}, {'chap': '3. Threads, Mutex & Sockets Multi-Client (C++11)', 'expl': "std::thread est l'objet natif en C++11 pour créer et démarrer un nouveau thread d'exécution parallèle au sein d'un processus.", 'mod': '💻 Programmation / Dev', 'options': ['std::thread', 'std::mutex', 'std::fork', 'std::async_task'], 'q': "Q29 : En C++11, quelle classe permet d'instancier et de démarrer l'exécution parallèle d'une fonction dans un fil d'exécution séparé ?", 'rep': 'std::thread'}, {'chap': '2. Services Active Directory & GPO (Windows Server)', 'expl': "Active Directory s'appuie obligatoirement sur un serveur DNS (souvent hébergé directement sur le DC) pour stocker les enregistrements de service de domaine (SRV).", 'mod': '🖥️ Administration Système', 'options': ['Le service WINS', 'Le service DNS', 'Le service DHCP', 'Le service IIS'], 'q': "Q30 : Dans Active Directory, quel service réseau indispensable s'occupe de traduire les requêtes de résolution de noms de domaine des contrôleurs de domaine (DC) ?", 'rep': 'Le service DNS'}, {'chap': '2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)', 'expl': "Un /28 offre 16 adresses IP au total. Moins l'adresse réseau et l'adresse de broadcast, il reste 14 adresses d'hôtes utilisables. C'est le dimensionnement exact.", 'mod': '📶 Réseaux & Télécoms', 'options': ['/26', '/27', '/28', '/29'], 'q': "Q31 : Dans le sujet d'examen officiel BTS CIEL 2024, quel masque de sous-réseau CIDR est préconisé pour un réseau de 14 hôtes utiles au maximum ?", 'rep': '/28'}, {'chap': '2. Top 10 OWASP & Sécurité Applicative', 'expl': "Le CSRF consiste à usurper l'identité d'un utilisateur connecté en transmettant des requêtes malveillantes à son insu via son propre navigateur vers un site qu'il a déjà authentifié.", 'mod': '🔒 Cybersécurité', 'options': ['CSRF (Cross-Site Request Forgery)', 'Injection SQL', 'XSS (Cross-Site Scripting)', 'Broken Authentication'], 'q': "Q32 : Quelle vulnérabilité web critique (Top 10 OWASP) permet à un attaquant de forcer le navigateur d'une victime authentifiée à exécuter des actions non souhaitées sur un site tiers ?", 'rep': 'CSRF (Cross-Site Request Forgery)'}, {'chap': '3. Gestion Avancée Linux & Sécurisation (ACLs, SUID/SGID, umask)', 'expl': "L'ajout du SUID s'effectue via 'chmod u+s' (ou au format octal chmod 4755, où le 4 active le SUID).", 'mod': '🖥️ Administration Système', 'options': ['chmod u+s <programme>', 'chmod 777 <programme>', 'chmod +x <programme>', 'chown root <programme>'], 'q': "Q33 : Quelle commande Linux permet d'accorder le droit d'exécution temporaire avec les privilèges de son propriétaire (SUID) à un programme exécutable ?", 'rep': 'chmod u+s <programme>'}, {'chap': '1. Échantillonnage, CAN/CNA & Théorème de Shannon', 'expl': 'La fréquence maximale du signal est Fmax = 12 kHz. Selon Shannon, Fe >= 2 * Fmax = 2 * 12 kHz = 24 kHz.', 'mod': '🔌 Électronique & IoT', 'options': ['12 kHz', '24 kHz', '24.2 kHz', '48 kHz'], 'q': "Q34 : Quelle est la fréquence d'échantillonnage minimale requise pour numériser un signal analogique dont la bande passante s'étend de 100 Hz à 12 kHz sans subir de repliement de spectre ?", 'rep': '24 kHz'}, {'chap': "1. Modélisation Logicielle UML (Classes, Séquence, Cas d'Utilisation)", 'expl': 'Le diagramme de séquence est un diagramme dynamique temporel décrivant la chronologie des échanges de messages entre lignes de vie.', 'mod': '📐 Modélisation UML & SysML', 'options': ['Diagramme de classes', "Diagramme de cas d'utilisation", 'Diagramme de séquence', "Diagramme d'activité"], 'q': "Q35 : En UML, comment s'appelle le diagramme comportemental décrivant l'enchaînement chronologique des interactions entre acteurs et objets à l'aide de lignes de vie ?", 'rep': 'Diagramme de séquence'}, {'chap': "1. Modélisation Logicielle UML (Classes, Séquence, Cas d'Utilisation)", 'expl': "Les tests de non-régression consistent à rejouer le plan de test suite à des modifications pour s'assurer que les fonctionnalités stables antérieures n'ont pas subi d'altérations.", 'mod': '📐 Modélisation UML & SysML', 'options': ['Les tests unitaires', "Les tests d'intégration", 'Les tests de régression (ou non-régression)', 'Les tests de boîte blanche'], 'q': "Q36 : Dans un projet d'examen E6, quelle section du Plan de Validation Logicielle (PVL) s'assure que les modifications apportées à un module n'ont pas introduit d'effets de bord négatifs sur les modules existants ?", 'rep': 'Les tests de régression (ou non-régression)'}, {'chap': '4. Bus Réseau Industriel CAN (Controller Area Network)', 'expl': "À l'état récessif (bit 1), les fils CAN_H et CAN_L sont tous deux maintenus à une tension moyenne d'environ 2.5V, la tension différentielle mesurée est nulle ($V_{diff} = 0 \\text{V}$).", 'mod': '🔌 Électronique & IoT', 'options': ['CAN_H = 3.5V et CAN_L = 1.5V (Vdiff = 2.0V)', 'CAN_H = 2.5V et CAN_L = 2.5V (Vdiff = 0V)', 'CAN_H = 5.0V et CAN_L = 0V (Vdiff = 5.0V)', 'CAN_H = 0V et CAN_L = 5.0V'], 'q': 'Q37 : Sur un bus différentiel CAN, quel état physique des tensions sur les fils correspond à un bit récessif (Logique 1) ?', 'rep': 'CAN_H = 2.5V et CAN_L = 2.5V (Vdiff = 0V)'}, {'chap': '1. Permissions GNU/Linux & Services système', 'expl': "En Bash Linux, la variable '$?' contient le statut de sortie de la dernière commande. Un code de 0 indique un succès, et un code supérieur à 0 indique une erreur.", 'mod': '🖥️ Administration Système', 'options': ['$?', '$#', '$$', '$*'], 'q': "Q38 : Dans un script d'administration Linux, quelle variable spéciale renvoie le code de retour d'erreur de la dernière commande exécutée en console ?", 'rep': '$?'}, {'chap': '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)', 'expl': "HTTPS est le protocole de navigation Web sécurisé. Il encapsule le protocole HTTP classique au sein d'une session de chiffrement TLS de couche Transport/Application.", 'mod': '🔒 Cybersécurité', 'options': ["HTTPS (s'appuyant sur TLS)", 'IPsec', 'WPA3', 'SSHv2'], 'q': 'Q39 : Quel protocole sécurisé opère au niveau de la couche Application (Port TCP 443) pour négocier des connexions Web chiffrées ?', 'rep': "HTTPS (s'appuyant sur TLS)"}, {'chap': '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN', 'expl': "Par convention sous la norme IEEE 802.1Q, les trames appartenant au VLAN natif (souvent le VLAN 1 par défaut) traversent les liens Trunk sans recevoir de tag d'identification.", 'mod': '📶 Réseaux & Télécoms', 'options': ['Elle est taguée obligatoirement avec un VLAN ID égal à 1', 'Elle circule de manière non taguée', "Elle est chiffrée avec l'algorithme AES", 'Elle est rejetée silencieusement'], 'q': "Q40 : Sur un lien d'interconnexion Trunk entre deux commutateurs, comment circule une trame Ethernet appartenant au VLAN natif ?", 'rep': 'Elle circule de manière non taguée'}, {'chap': '5. Protocoles Industriels & Bus de terrain (Modbus, Profibus)', 'expl': "Le code de fonction standard 03 (Read Holding Registers) permet de lire les registres d'écriture/lecture analogiques de 16 bits (Holding Registers). Le code 04 permet de lire les registres d'entrée en lecture seule (Input Registers).", 'mod': '📶 Réseaux & Télécoms', 'options': ['01 (Read Coils)', '02 (Read Discrete Inputs)', '03 (Read Holding Registers)', '04 (Read Input Registers)'], 'q': "Q41 : Dans le cadre de l'interfaçage de réseaux industriels avec le protocole Modbus RTU (série RS-485), quel code de fonction (Function Code) standard permet de lire la valeur de registres de sortie analogiques (Holding Registers) ?", 'rep': '03 (Read Holding Registers)'}, {'chap': "4. Services d'Infrastructure : DHCP, DNS, NAT/PAT", 'expl': "L'émission de la requête ARP (ARP Request) s'effectue par diffusion générale (Broadcast) à destination de toutes les machines du domaine de diffusion locale (adresse MAC destination FF:FF:FF:FF:FF:FF). La réponse (ARP Reply) est ensuite renvoyée en Unicast.", 'mod': '📶 Réseaux & Télécoms', 'options': ['Unicast (adresse MAC du routeur)', 'Multicast (adresse MAC IPv6)', 'Broadcast (adresse MAC FF:FF:FF:FF:FF:FF)', 'Anycast (adresse MAC dynamique)'], 'q': "Q42 : Lors de la résolution d'adresse physique via le protocole ARP (Address Resolution Protocol), quel type de trame Ethernet est émise par une machine pour interroger le réseau, et quelle est l'adresse MAC de destination de cette trame ?", 'rep': 'Broadcast (adresse MAC FF:FF:FF:FF:FF:FF)'}, {'chap': "4. Lois Fondamentales d'Électricité & Composants Passifs", 'expl': "L'énergie emmagasinée dans un condensateur se calcule par la formule E = (1/2) * C * U^2. Donc, E = 0,5 * (220 * 10^-6 F) * (10 V)^2 = 0,5 * 0,00022 * 100 = 0,011 J = 11 mJ.", 'mod': '🔌 Électronique & IoT', 'options': ['1,1 mJ', '11 mJ', '22 mJ', '110 mJ'], 'q': "Q43 : Un condensateur de capacité C = 220 µF est raccordé dans un circuit électrique continu sous une tension d'alimentation stable U = 10 V. Quelle est l'énergie électrostatique E emmagasinée par ce condensateur ?", 'rep': '11 mJ'}, {'chap': "4. Lois Fondamentales d'Électricité & Composants Passifs", 'expl': "Pour deux résistances en parallèle, la résistance équivalente s'obtient par la formule : Req = (R1 * R2) / (R1 + R2) = (100 * 300) / (100 + 300) = 30000 / 400 = 75 Ω.", 'mod': '🔌 Électronique & IoT', 'options': ['75 Ω', '200 Ω', '400 Ω', '300 Ω'], 'q': 'Q44 : Deux résistances ohmiques R1 = 100 Ω et R2 = 300 Ω sont branchées en parallèle dans un circuit de filtrage. Quelle est la valeur de la résistance équivalente Req de cette association ?', 'rep': '75 Ω'}, {'chap': '6. Transmission optique (Fibres optiques Monomodes & Multimodes)', 'expl': 'La fibre Monomode possède un cœur très étroit (9 µm) par rapport à la Multimode (50 µm ou 62,5 µm). Elle limite la propagation à un faisceau rectiligne unique (mode axial), ce qui annule la dispersion modale temporelle et permet de très hauts débits sur de très longues distances sans répéteur.', 'mod': '📶 Réseaux & Télécoms', 'options': ["La fibre Monomode a un diamètre de cœur très fin (≈ 9 µm) et ne transmet qu'un seul mode de propagation laser, réduisant presque à zéro la dispersion modale.", "La fibre Monomode utilise une source lumineuse LED de faible coût et souffre d'une forte atténuation sur de courtes distances.", 'La fibre Multimode est réservée exclusivement aux liaisons océaniques intercontinentales de très longue distance.', "La fibre Monomode utilise un cœur de grand diamètre (≈ 50 µm ou 62,5 µm) permettant d'injecter plusieurs longueurs d'ondes à la fois."], 'q': "Q45 : Dans l'épreuve de transmission optique, quelle caractéristique distingue fondamentalement une fibre optique Monomode (Single-mode) d'une fibre optique Multimode (Multi-mode) ?", 'rep': "La fibre Monomode a un diamètre de cœur très fin (≈ 9 µm) et ne transmet qu'un seul mode de propagation laser, réduisant presque à zéro la dispersion modale."}, {'chap': '3. Structures de données avancées & Unions en Langage C', 'expl': 'Contrairement à une structure (struct) qui additionne la taille de ses membres (plus alignement), une union partage le même espace mémoire pour tous ses membres. Sa taille totale correspond donc à la taille de son plus grand membre, qui est ici le float (4 octets).', 'mod': '💻 Programmation / Dev', 'options': ['1 octet', '4 octets', '7 octets', '8 octets'], 'q': "Q46 : En programmation système C/C++ pour l'embarqué, si un programme définit un type 'union' contenant un 'char' (1 octet), un 'short' (2 octets) et un 'float' (4 octets), quelle sera l'occupation mémoire en octets d'une instance de cette union ?", 'rep': '4 octets'}, {'chap': '2. Active Directory, Domaines & GPO', 'expl': "L'enregistrement PTR (Pointer Record) est utilisé dans la zone de recherche inverse (Reverse Lookup Zone) pour associer une adresse IP à un nom DNS, indispensable pour certains services de sécurité et de filtrage anti-spam.", 'mod': '🖥️ Administration Système', 'options': ['Enregistrement A', 'Enregistrement CNAME', 'Enregistrement PTR', 'Enregistrement NS'], 'q': "Q47 : Dans la configuration de zones d'un serveur de noms de domaine (DNS), quel type d'enregistrement (Resource Record) doit obligatoirement être créé pour assurer la résolution inverse (traduire une adresse IP publique ou privée en nom de domaine complet FQDN) ?", 'rep': 'Enregistrement PTR'}, {'chap': '1. Droits Linux & Commandes Système', 'expl': "Le SUID (Set User ID) permet d'exécuter un fichier binaire avec les droits de son propriétaire (généralement root). Il est représenté par la lettre 's' à la place du droit d'exécution du propriétaire (ex: rwsr-xr-x) et vaut 4 au premier chiffre en octal (ex: chmod 4755).", 'mod': '🖥️ Administration Système', 'options': ['Le SUID (Set User ID, valeur numérique 4000)', 'Le SGID (Set Group ID, valeur numérique 2000)', 'Le Sticky Bit (valeur numérique 1000)', "L'ACL d'accès spécifique"], 'q': "Q48 : Sous GNU/Linux, quelle permission spéciale permet à un utilisateur d'exécuter un fichier binaire avec les privilèges d'accès du propriétaire du fichier (par exemple, pour permettre à un simple utilisateur de changer son mot de passe avec l'exécutable '/usr/bin/passwd') ?", 'rep': 'Le SUID (Set User ID, valeur numérique 4000)'}, {'chap': "4. Lois Fondamentales d'Électricité & Composants Passifs", 'expl': "D'après la formule du pont diviseur de tension, la tension aux bornes de R2 s'exprime par : U_R2 = E * [R2 / (R1 + R2)] = 12 V * [400 / (800 + 400)] = 12 V * [400 / 1200] = 12 V * (1/3) = 4 V.", 'mod': '🔌 Électronique & IoT', 'options': ['4 V', '6 V', '8 V', '12 V'], 'q': 'Q49 : Dans un montage électrique continu alimenté par un générateur de tension E = 12 V, un pont diviseur de tension est constitué de deux résistances en série R1 = 800 Ω et R2 = 400 Ω. Quelle est la tension de sortie U_R2 mesurée aux bornes de la résistance R2 ?', 'rep': '4 V'}, {'chap': '2. Active Directory, Domaines & GPO', 'expl': "Une Unité d'Organisation (OU) est un conteneur logique. On ne peut pas y attribuer directement des droits de partage de fichiers (ce n'est pas un groupe de sécurité), mais elle permet d'organiser les comptes utilisateurs/ordinateurs pour y lier des GPO ou déléguer le contrôle d'administration (ex: réinitialiser un mot de passe).", 'mod': '🖥️ Administration Système', 'options': ["Organiser logiquement les objets du domaine pour appliquer des stratégies de groupe (GPO) et déléguer des tâches d'administration.", "Créer des principaux de sécurité sur lesquels on peut attribuer directement des droits d'accès aux partages de fichiers.", "Établir des relations d'approbation d'accès sécurisées (Trust Relationships) avec d'autres forêts de serveurs.", "Augmenter le niveau fonctionnel global de la forêt AD sans modifier l'infrastructure physique."], 'q': "Q50 : Dans la structuration hiérarchique d'un annuaire Active Directory sous Windows Server, quel est le principal intérêt de la création d'Unités d'Organisation (OU) ?", 'rep': "Organiser logiquement les objets du domaine pour appliquer des stratégies de groupe (GPO) et déléguer des tâches d'administration."}, {'q': "Q41 : En transmission par fibre optique, quelle est la caractéristique majeure d'une fibre Monomode (SMF) par rapport à une fibre Multimode (MMF) ?", 'options': ["Un cœur large de 50 µm et l'utilisation de LED sur courte distance", "Un cœur très étroit (~9 µm), l'absence de dispersion modale et des portées de plusieurs dizaines de kilomètres", 'Une forte dispersion modale limitant la portée à 300 mètres', "L'utilisation exclusive de connecteurs ST"], 'rep': "Un cœur très étroit (~9 µm), l'absence de dispersion modale et des portées de plusieurs dizaines de kilomètres", 'mod': '📶 Réseaux & Télécoms', 'chap': '6. Transmissions Optiques & Fibre Optique (Monomode vs Multimode)', 'expl': "La fibre Monomode (SMF) possède un cœur très fin (~9 µm) dans lequel ne se propage qu'un seul mode lumineux (Laser). Sans dispersion modale, elle permet d'atteindre des distances de 40 à 100 km."}, {'q': 'Q42 : Dans le protocole Modbus RTU, quel code fonction (Function Code) permet de lire des registres de lecture/écriture 16 bits (Holding Registers) ?', 'options': ['Code 01', 'Code 03', 'Code 06', 'Code 16 (0x10)'], 'rep': 'Code 03', 'mod': '📶 Réseaux & Télécoms', 'chap': '7. Protocoles Industriels : Modbus RTU & Bus RS485', 'expl': 'Le code fonction Modbus 03 (Read Holding Registers) permet au maître de lire le contenu de registres de configuration ou de données 16 bits.'}, {'q': "Q43 : Conformément au RGPD et aux directives CNIL, quand la réalisation d'une Analyse d'Impact relative à la Protection des Données (AIPD / PIA) est-elle légalement obligatoire ?", 'options': ['Uniquement pour les entreprises de plus de 500 salariés', 'Dès lors que le traitement répond à au moins 2 des 9 critères de risque de la grille CNIL/CEPD', 'Uniquement en cas de traitement de coordonnées bancaires', 'Elle est toujours facultative'], 'rep': 'Dès lors que le traitement répond à au moins 2 des 9 critères de risque de la grille CNIL/CEPD', 'mod': '🔒 Cybersécurité', 'chap': "6. Analyse d'Impact sur la Vie Privée PIA / AIPD (RGPD & CNIL)", 'expl': "L'AIPD devient légalement obligatoire si un traitement de données personnelles accumule au moins 2 critères parmi les 9 définis par les autorités européennes (profilage, données sensibles, grande échelle, personnes vulnérables, etc.)."}, {'q': "Q44 : Dans une architecture de pare-feu pfSense, pourquoi est-il strictement interdit d'autoriser le flux d'initiation de connexion depuis la DMZ vers le réseau interne LAN ?", 'options': ['Parce que pfSense ne sait pas router les paquets entre DMZ et LAN', "Pour éviter qu'un attaquant compromettant un serveur public en DMZ ne puisse pivoter vers le réseau interne de l'entreprise", 'Parce que les requêtes DNS ne fonctionnent que du LAN vers la DMZ', "Pour économiser la bande passante de l'interface WAN"], 'rep': "Pour éviter qu'un attaquant compromettant un serveur public en DMZ ne puisse pivoter vers le réseau interne de l'entreprise", 'mod': '🔒 Cybersécurité', 'chap': '8. Matrice des Flux & Architecture Pare-Feu pfSense (LAN/DMZ/WAN/AD)', 'expl': "La DMZ héberge des serveurs exposés à Internet. En interdisant l'initiation de connexions de la DMZ vers le LAN, on empêche un pirate d'utiliser le serveur compromis comme rebond vers les machines internes."}, {'q': "Q45 : En langage C, quelle est la particularité fondamentale de la mémoire d'une 'union' par rapport à une 'struct' ?", 'options': ["Une union est allouée dynamiquement sur le tas alors qu'une struct est sur la pile", "Tous les membres d'une union partagent le même espace mémoire, et sa taille vaut celle de son plus grand membre", 'Une union ne peut pas contenir de variables entières', "Une struct utilise systématiquement moins de mémoire qu'une union"], 'rep': "Tous les membres d'une union partagent le même espace mémoire, et sa taille vaut celle de son plus grand membre", 'mod': '💻 Programmation / Dev', 'chap': '2. Langage C : Structures struct & Unions union', 'expl': "Dans une union, les membres chevauchent la même adresse mémoire. Écrire dans un membre écrase la valeur des autres. C'est idéal pour convertir un float 32 bits en 4 octets."}, {'q': 'Q46 : En C++11 multithread, quel composant doit être utilisé pour protéger une variable partagée dans une section critique contre les conditions de concurrence (Race Conditions) ?', 'options': ['std::vector', 'std::mutex avec std::lock_guard', 'std::thread::sleep_for', 'std::atomic_bool uniquement'], 'rep': 'std::mutex avec std::lock_guard', 'mod': '💻 Programmation / Dev', 'chap': '4. Programmation Concurrente C++11 : Threads, Mutex & Section Critique', 'expl': "Un mutex verrouille l'accès à la section critique. Le wrapper std::lock_guard applique le principe RAII : il verrouille le mutex à l'instanciation et le libère automatiquement à la sortie du bloc."}, {'q': "Q47 : Dans la technologie IoT LoRaWAN, quelle classe d'équipements offre la plus faible consommation énergétique en n'ouvrant des fenêtres de réception qu'immédiatement après une émission ?", 'options': ['Classe A', 'Classe B', 'Classe C', 'Classe D'], 'rep': 'Classe A', 'mod': '🔌 Électronique & IoT', 'chap': '5. Protocoles Connectés : MQTT & LoRaWAN', 'expl': "Les équipements LoRaWAN de Classe A restent en veille quasi-permanente. Ils n'ouvrent deux courtes fenêtres de réception qu'après avoir émis un message, offrant une autonomie de batterie maximale."}, {'q': "Q48 : Dans une architecture PKI, quel est le rôle principal d'une Autorité de Certification Intermédiaire (Issuing CA) ?", 'options': ['Signer le certificat de la CA Racine', 'Délivrer et signer les certificats X.509 opérationnels des serveurs et utilisateurs tout en gardant la CA Racine hors ligne', 'Stocker les clés privées de tous les utilisateurs Internet', 'Remplacer le serveur DNS'], 'rep': 'Délivrer et signer les certificats X.509 opérationnels des serveurs et utilisateurs tout en gardant la CA Racine hors ligne', 'mod': '🔒 Cybersécurité', 'chap': '7. PKI & Gestion des Certificats Numériques X.509', 'expl': 'Pour protéger la CA Racine (Root CA) maintenue hors ligne dans un coffre-fort, la CA Intermédiaire prend en charge la délivrance quotidienne des certificats.'}, {'q': "Q49 : En communication Modbus RTU sur liaison RS485, comment la fin d'une trame est-elle détectée par les automates récepteurs ?", 'options': ['Par un caractère de saut de ligne ASCII \\r\\n', 'Par un silence sur le bus supérieur ou égal à 3,5 temps caractères', "Par un octet d'en-tête specifique 0x7E", 'Par une impulsion sur une ligne physique séparée'], 'rep': 'Par un silence sur le bus supérieur ou égal à 3,5 temps caractères', 'mod': '📶 Réseaux & Télécoms', 'chap': '7. Protocoles Industriels : Modbus RTU & Bus RS485', 'expl': "Modbus RTU utilise un délimiteur temporel : un intervalle de silence de 3.5 caractères marque la fin d'une trame et le début de la suivante."}, {'q': "Q50 : Quel est l'intérêt principal des extensions SAN (Subject Alternative Name) dans un certificat TLS X.509 ?", 'options': ['Compresser la taille du certificat', 'Autoriser plusieurs noms de domaine (FQDN) et adresses IP sous un seul et même certificat', 'Chiffrer la clé privée sur le disque', 'Désactiver TLS 1.3'], 'rep': 'Autoriser plusieurs noms de domaine (FQDN) et adresses IP sous un seul et même certificat', 'mod': '🔒 Cybersécurité', 'chap': '7. PKI & Gestion des Certificats Numériques X.509', 'expl': "L'extension SAN permet de lister l'ensemble des noms d'hôtes (ex: www.ciel.fr, mail.ciel.fr, IP) valides pour le certificat."}, {'q': "Q61 : Selon la loi de Shannon-Hartley, quelle est la capacité maximale C d'un canal de bande passante B = 1 MHz ayant un rapport signal/bruit S/N = 15 (linéaire) ?", 'options': ['1 Mbps', '4 Mbps', '15 Mbps', '16 Mbps'], 'rep': '4 Mbps', 'mod': '📶 Réseaux & Télécoms', 'chap': '5. Modulations & Transmissions de Signaux (FSK, ASK, PSK, QAM)', 'expl': 'C = B * log2(1 + S/N) = 1 MHz * log2(1 + 15) = 1 MHz * log2(16) = 1 MHz * 4 = 4 Mbps.'}, {'q': 'Q62 : Quel protocole de prévention des boucles de commutation (Spanning Tree) offre une convergence rapide en quelques millisecondes sous la norme IEEE 802.1w ?', 'options': ['STP (802.1D)', 'RSTP (802.1w)', 'PVST+', 'MSTP (802.1s)'], 'rep': 'RSTP (802.1w)', 'mod': '📶 Réseaux & Télécoms', 'chap': '3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN', 'expl': 'Rapid Spanning Tree Protocol (RSTP - 802.1w) offre une réadaptation quasi-instantanée de la topologie réseau.'}, {'q': "Q63 : En C++11, quel pointeur intelligent (Smart Pointer) doit être utilisé pour garantir qu'un objet dynamique ne possède qu'un seul et unique propriétaire ?", 'options': ['std::shared_ptr', 'std::unique_ptr', 'std::weak_ptr', 'std::auto_ptr'], 'rep': 'std::unique_ptr', 'mod': '💻 Programmation / Dev', 'chap': '1. Langage C++ : Mémoire, Pointeurs & POO', 'expl': 'std::unique_ptr exécute la gestion de propriété exclusive sans surcoût de compteur de références.'}, {'q': "Q64 : Quelle commande Linux permet de rechercher toutes les lignes contenant le mot 'ERROR' dans tous les fichiers .log du dossier /var/log de manière récursive ?", 'options': ["find /var/log -name 'ERROR'", "grep -r 'ERROR' /var/log/*.log", "cat /var/log | grep 'ERROR'", "locate 'ERROR' /var/log"], 'rep': "grep -r 'ERROR' /var/log/*.log", 'mod': '🖥️ Administration Système', 'chap': '1. Droits Linux & Commandes Système', 'expl': "L'option -r de grep effectue une recherche récursive dans tous les fichiers correspondant au motif."}, {'q': "Q65 : Quelle est la fréquence de coupure fc d'un filtre RC passe-bas constitué d'une résistance R = 1 kΩ et d'un condensateur C = 159 nF ?", 'options': ['100 Hz', '1 kHz', '10 kHz', '100 kHz'], 'rep': '1 kHz', 'mod': '🔌 Électronique & IoT', 'chap': '1. Échantillonnage, CAN/CNA & Théorème de Shannon', 'expl': 'fc = 1 / (2 * pi * R * C) = 1 / (2 * 3.14159 * 1000 * 159e-9) ≈ 1000 Hz = 1 kHz.'}, {'q': "Q66 : En mathématiques, quelle est la dérivée f'(x) de la fonction f(x) = ln(3x^2 + 1) sur R ?", 'options': ["f'(x) = 1 / (3x^2 + 1)", "f'(x) = 6x / (3x^2 + 1)", "f'(x) = 6x * (3x^2 + 1)", "f'(x) = 3 / x"], 'rep': "f'(x) = 6x / (3x^2 + 1)", 'mod': '📈 Mathématiques', 'chap': 'Fonctions, Exponentielle & Logarithme', 'expl': "Pour f(x) = ln(u(x)), la dérivée est u'(x) / u(x). Avec u(x) = 3x^2 + 1, u'(x) = 6x. Donc f'(x) = 6x / (3x^2 + 1)."}, {'q': "Q67 : Dans le protocole d'authentification Wi-Fi 802.1X / Enterprise, quel serveur est chargé de vérifier les identifiants et certificats des utilisateurs ?", 'options': ['Serveur DHCP', 'Serveur RADIUS', 'Serveur DNS', 'Serveur NTP'], 'rep': 'Serveur RADIUS', 'mod': '🔒 Cybersécurité', 'chap': '4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)', 'expl': "Le serveur RADIUS centralise la gestion de l'authentification AAA (Authentication, Authorization, Accounting) en 802.1X."}, {'q': "Q68 : Sur un réseau de communication Modbus RTU sur liaison série RS-485, quel est le nombre maximal théorique d'esclaves adressables sans répéteur ?", 'options': ['16 esclaves', '32 esclaves', '127 esclaves', '247 esclaves'], 'rep': '247 esclaves', 'mod': '🔌 Électronique & IoT', 'chap': '2. Bus Série Matériels : I2C, SPI, UART & CAN Bus', 'expl': "La plage d'adresses esclaves Modbus s'étend de 1 à 247 (l'adresse 0 étant réservée à la diffusion / broadcast)."}, {'q': 'Q69 : En SysML, quel diagramme permet de définir la hiérarchie des exigences du cahier des charges et leurs relations de traçabilité (deriveReqt, verify) ?', 'options': ['BDD (Block Definition Diagram)', 'IBD (Internal Block Diagram)', 'Requirement Diagram', 'Use Case Diagram'], 'rep': 'Requirement Diagram', 'mod': '📐 Modélisation UML & SysML', 'chap': '2. Diagrammes SysML (BDD, IBD, Exigences)', 'expl': 'Le Requirement Diagram modélise les exigences fonctionnelles et non-fonctionnelles et leur traçabilité.'}, {'q': "Q70 : En C++, quel mot-clé permet d'indiquer qu'une méthode d'une classe dérivée est destinée à redéfinir une méthode virtuelle de sa classe mère ?", 'options': ['virtual', 'override', 'overload', 'static'], 'rep': 'override', 'mod': '💻 Programmation / Dev', 'chap': '1. Langage C++ : Mémoire, Pointeurs & POO', 'expl': "Le spécificateur 'override' (C++11) garantit au compilateur que la méthode redéfinit exactement une méthode virtuelle de la classe de base."}]
# Advanced Multi-User & Stats Engine for BTS CIEL Studio Pro
import json
import os
import hashlib
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

USERS_FILE = 'users_db_v2.json'

DEFAULT_USER = 'Invité BTS CIEL'

def get_current_user_name():
    return st.session_state.get('current_user', DEFAULT_USER)

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_users(db):
    try:
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def create_default_user_data(username="Invité BTS CIEL", role="Candidat Option A"):
    today = datetime.now()
    default_history = [
        {'date': (today - timedelta(days=14)).strftime('%Y-%m-%d %H:%M'), 'quiz': 'Diagnostic Initial', 'score': 6, 'total': 10, 'details': {'Réseaux': 2, 'Cybersécurité': 1, 'Prog': 1, 'SysAdmin': 1, 'Elec': 1, 'Maths': 0, 'UML': 0}},
        {'date': (today - timedelta(days=7)).strftime('%Y-%m-%d %H:%M'), 'quiz': 'Entraînement S1', 'score': 8, 'total': 10, 'details': {'Réseaux': 3, 'Cybersécurité': 2, 'Prog': 1, 'SysAdmin': 1, 'Elec': 1, 'Maths': 0, 'UML': 0}},
        {'date': (today - timedelta(days=2)).strftime('%Y-%m-%d %H:%M'), 'quiz': 'Grand Quiz Examen', 'score': 9, 'total': 10, 'details': {'Réseaux': 2, 'Cybersécurité': 2, 'Prog': 2, 'SysAdmin': 1, 'Elec': 1, 'Maths': 1, 'UML': 0}}
    ]
    return {
        'username': username,
        'role': role,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'last_login': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'points': 75,
        'level': 'Technicien Supérieur Confirmé ⚡',
        'history': default_history,
        'domain_mastery': {
            'Réseaux & Télécoms': 70,
            'Cybersécurité & Hardening': 65,
            'Programmation C++ & Python': 55,
            'Administration Système & AD': 60,
            'Électronique & Bus': 50,
            'Mathématiques Appliquées': 45,
            'Modélisation SysML & E6': 40
        },
        'completed_activities': {
            'w1_diag': True
        },
        'badges': [
            {'id': 'first_step', 'nom': 'Pied à l\'Étrier', 'desc': 'Première session d\'évaluation complétée', 'icon': '🎯', 'date': (today - timedelta(days=14)).strftime('%Y-%m-%d')},
            {'id': 'net_rookie', 'nom': 'Architecte Réseau', 'desc': 'Score >= 8/10 en Réseaux & Commutation', 'icon': '📶', 'date': (today - timedelta(days=7)).strftime('%Y-%m-%d')}
        ],
        'notes': 'Objectif : Obtenir la mention Très Bien au BTS CIEL Option A.'
    }

def init_user_session():
    if 'current_user' not in st.session_state:
        st.session_state.current_user = DEFAULT_USER
    if 'user_role' not in st.session_state:
        st.session_state.user_role = 'Candidat Option A'
    if 'user_progress' not in st.session_state:
        db = load_users()
        user_data = db.get(st.session_state.current_user, create_default_user_data(st.session_state.current_user))
        st.session_state.user_progress = user_data
    if 'cloud_sync_status' not in st.session_state:
        st.session_state.cloud_sync_status = 'Mode Local Synchrone'

def get_active_user_data():
    init_user_session()
    u = st.session_state.current_user
    db = load_users()
    if u not in db:
        user_data = create_default_user_data(u, st.session_state.get('user_role', 'Candidat Option A'))
        db[u] = user_data
        save_users(db)
        st.session_state.user_progress = user_data
        return user_data
    return db[u]

def update_active_user_data(user_data):
    init_user_session()
    u = st.session_state.current_user
    db = load_users()
    db[u] = user_data
    save_users(db)
    st.session_state.user_progress = user_data

def add_user_points(points, activity_key, domain=None):
    init_user_session()
    user_data = get_active_user_data()
    
    if activity_key not in user_data['completed_activities']:
        user_data['completed_activities'][activity_key] = True
        user_data['points'] += points
        
        # Domain boost if specified
        if domain and domain in user_data['domain_mastery']:
            current_m = user_data['domain_mastery'][domain]
            user_data['domain_mastery'][domain] = min(100, current_m + int(points * 0.4))
            
        pts = user_data['points']
        if pts >= 600:
            user_data['level'] = 'Major National BTS CIEL 🎓'
        elif pts >= 400:
            user_data['level'] = 'Expert Cybersécurité & Réseaux 🛡️'
        elif pts >= 250:
            user_data['level'] = 'Technicien Supérieur Confirmé ⚡'
        elif pts >= 100:
            user_data['level'] = 'Développeur & Intégrateur 💻'
        else:
            user_data['level'] = 'Apprenti Technicien 🚀'
            
        # Check badge unlocks
        unlocked_ids = [b['id'] for b in user_data.get('badges', [])]
        if pts >= 100 and 'pts_100' not in unlocked_ids:
            user_data.setdefault('badges', []).append({
                'id': 'pts_100', 'nom': 'Centurion CIEL', 'desc': 'Cap des 100 points XP franchi !', 'icon': '💯', 'date': datetime.now().strftime('%Y-%m-%d')
            })
        if pts >= 300 and 'pts_300' not in unlocked_ids:
            user_data.setdefault('badges', []).append({
                'id': 'pts_300', 'nom': 'Maître de l\'Atelier', 'desc': 'Cap des 300 points XP franchi !', 'icon': '🏆', 'date': datetime.now().strftime('%Y-%m-%d')
            })

        update_active_user_data(user_data)

def save_score(score, total, details, quiz_name="Quiz"):
    init_user_session()
    user_data = get_active_user_data()
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    user_data.setdefault('history', []).append({
        'date': now_str,
        'quiz': quiz_name,
        'score': score,
        'total': total,
        'details': details
    })
    
    # Update domain masteries based on details
    for d_name, d_score in details.items():
        # Match domain name
        for target_d in user_data.get('domain_mastery', {}):
            if d_name.lower() in target_d.lower():
                gain = int((d_score / max(1, total)) * 8)
                user_data['domain_mastery'][target_d] = min(100, user_data['domain_mastery'][target_d] + gain)
                
    update_active_user_data(user_data)

def load_scores():
    init_user_session()
    user_data = get_active_user_data()
    return user_data.get('history', [])


def render_10_questions_quiz(category_or_module, quiz_key):
    """
    Rendu dynamique d'un quiz certifiant de 10 questions avec calcul de score,
    explications détaillées et attribution de points XP au profil utilisateur.
    """
    import streamlit as st
    
    # 1. Recherche des questions dans QUIZZES_BANK_10
    questions = []
    if category_or_module in QUIZZES_BANK_10:
        questions = QUIZZES_BANK_10[category_or_module]
    else:
        # Recherche par module dans GRAND_QUIZ_DATA
        cat_lower = category_or_module.lower()
        matching = []
        for q in GRAND_QUIZ_DATA:
            m_mod = q.get('mod', '').lower()
            if ('réseau' in cat_lower and 'réseau' in m_mod) or \
               ('cyber' in cat_lower and 'cyber' in m_mod) or \
               ('prog' in cat_lower and ('prog' in m_mod or 'dev' in m_mod)) or \
               ('élec' in cat_lower and ('élec' in m_mod or 'iot' in m_mod)) or \
               ('modél' in cat_lower and ('uml' in m_mod or 'sysml' in m_mod)) or \
               ('math' in cat_lower and 'math' in m_mod) or \
               ('sys' in cat_lower and ('sys' in m_mod or 'admin' in m_mod)):
                matching.append({
                    'q': q['q'],
                    'opts': q.get('options', q.get('opts', [])),
                    'rep': q['rep'],
                    'expl': q.get('expl', 'Conforme aux exigences officielles du BTS CIEL.')
                })
        questions = matching[:10]
        if len(questions) < 10 and 'Suites' in QUIZZES_BANK_10:
            # Fallback
            questions = (questions + QUIZZES_BANK_10['Suites'])[:10]

    st.markdown(f"<div style='background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 12px; padding: 14px 18px; margin-bottom: 20px;'>"
                f"<b style='color: #38bdf8;'>🎯 Questionnaire Certifiant</b> : 10 questions à choix multiples pour valider vos acquis en <b>{category_or_module}</b>. "
                f"<span style='color: #94a3b8; font-size: 0.85rem;'>Gagnez jusqu'à <b>+50 XP</b> sur votre profil !</span></div>", unsafe_allow_html=True)

    user_answers = {}
    for idx, item in enumerate(questions):
        q_num = idx + 1
        st.markdown(f"**Q{q_num} : {item['q']}**")
        opts = item.get('opts', item.get('options', []))
        user_answers[idx] = st.radio(f"Choix pour Q{q_num} :", opts, key=f"{quiz_key}_rad_{idx}")
        st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

    if st.button("Valider mon questionnaire (10 questions)", type="primary", key=f"{quiz_key}_submit_btn"):
        score = 0
        st.markdown("---")
        st.markdown("### 📊 Résultats & Corrigé Détaillé")
        for idx, item in enumerate(questions):
            q_num = idx + 1
            user_ans = user_answers[idx]
            rep_exacte = item['rep']
            if user_ans == rep_exacte:
                score += 1
                st.success(f"✅ **Q{q_num} Exact !** ({user_ans})\n\n💡 *Explication :* {item['expl']}")
            else:
                st.error(f"❌ **Q{q_num} Incorrect.** Vous avez répondu : *{user_ans}* | Réponse attendue : **{rep_exacte}**\n\n💡 *Explication :* {item['expl']}")

        # Attribution XP & Bilan
        pct = (score / len(questions)) * 100
        pts_earned = score * 5
        add_user_points(pts_earned, quiz_key, domain=category_or_module)
        save_score(score, len(questions), {category_or_module: score}, quiz_name=f"Quiz Certifiant {category_or_module}")
        
        if score >= 8:
            st.success(f"🏆 **Excellente Maîtrise ! Note : {score} / 10 ({pct:.0f}%)** — Vous avez gagné **+{pts_earned} XP** !")
            st.balloons()
        elif score >= 5:
            st.info(f"👍 **Score Honorable : {score} / 10 ({pct:.0f}%)** — Vous avez gagné **+{pts_earned} XP**. Relisez les mémos pour viser le 10/10.")
        else:
            st.warning(f"⚠️ **Score Insuffisant : {score} / 10 ({pct:.0f}%)** — Vous avez gagné **+{pts_earned} XP**. Révisez le cours de la semaine avant de retenter.")



# Module de Rendu Analyse des Scores pour BTS CIEL Studio Pro
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def render_page_analyse_scores():
    init_user_session()
    user_data = get_active_user_data()
    u_name = user_data['username']
    u_role = user_data['role']
    u_pts = user_data['points']
    u_lvl = user_data['level']
    hist = user_data.get('history', [])

    st.markdown(f"""
    <div class='hero-container'>
        <div style='display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 15px;'>
            <div>
                <span class='badge badge-blue'>ESPACE PERSONNEL CERTIFIANT</span>
                <div class='hero-title'>📈 Bilan Analytique & Performances Individuelles</div>
                <div class='hero-subtitle'>Profil actif : <b style='color:#38bdf8;'>{u_name}</b> ({u_role}) — Grade : <b style='color:#34d399;'>{u_lvl}</b></div>
            </div>
            <div style='background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 16px; padding: 14px 20px; text-align: center;'>
                <div style='font-size: 0.8rem; color: #94a3b8; font-weight: 700; text-transform: uppercase;'>Total XP Acquis</div>
                <div style='font-size: 2.2rem; font-weight: 800; color: #fb923c;'>{u_pts} <span style='font-size: 1.1rem; color: #cbd5e1;'>XP</span></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab_an1, tab_an2, tab_an3, tab_an4 = st.tabs([
        "📊 Statistiques & Évolution",
        "🕸️ Radar de Compétences BTS CIEL",
        "🏆 Badges & Succès Débloqués",
        "⚙️ Gestion du Compte & Cloud Sync"
    ])

    with tab_an1:
        st.subheader(f"1. Métriques Individuelles de {u_name}")
        if hist:
            df = pd.DataFrame(hist)
            nb_tentatives = len(df)
            moyenne = (df['score'] / df['total']).mean() * 100
            best_score = df['score'].max()
            last_score = df['score'].iloc[-1]
            last_total = df['total'].iloc[-1]
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f"<div class='stat-box'><div class='stat-number'>{nb_tentatives}</div><div class='stat-label'>Évaluations Passées</div></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='stat-box'><div class='stat-number'>{moyenne:.1f}%</div><div class='stat-label'>Moyenne Générale</div></div>", unsafe_allow_html=True)
            with c3:
                st.markdown(f"<div class='stat-box'><div class='stat-number'>{best_score}/10</div><div class='stat-label'>Meilleure Performance</div></div>", unsafe_allow_html=True)
            with c4:
                st.markdown(f"<div class='stat-box'><div class='stat-number'>{last_score}/{last_total}</div><div class='stat-label'>Dernière Note</div></div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📈 Courbe d'Évolution des Notes dans le Temps")
            df_chart = df.copy()
            df_chart['Pourcentage'] = (df_chart['score'] / df_chart['total']) * 100
            df_chart['Date_Label'] = df_chart['date'].apply(lambda d: d.split(' ')[0] if ' ' in d else d)
            
            fig, ax = plt.subplots(figsize=(10, 3.5), facecolor='#090e1d')
            ax.set_facecolor('#090e1d')
            ax.plot(df_chart['Date_Label'], df_chart['Pourcentage'], marker='o', color='#38bdf8', linewidth=2.5, markersize=8, label='Performance (%)')
            ax.axhline(50, color='#ef4444', linestyle='--', alpha=0.6, label='Seuil Admission (50%)')
            ax.axhline(80, color='#34d399', linestyle='--', alpha=0.6, label='Seuil Mention Bien (80%)')
            ax.set_ylim(0, 105)
            ax.set_ylabel('Score (%)', color='#cbd5e1', fontsize=10)
            ax.tick_params(colors='#94a3b8', labelsize=9)
            ax.grid(color='#1e293b', linestyle=':', alpha=0.5)
            for spine in ax.spines.values():
                spine.set_color('#1e293b')
            ax.legend(facecolor='#0f172a', edgecolor='#334155', labelcolor='#e2e8f0', fontsize=9)
            st.pyplot(fig)
            plt.close()

            st.markdown("### 📜 Historique Détaillé de vos Passages")
            hist_display = []
            for h in reversed(hist):
                pct = (h['score'] / h['total']) * 100
                mention = "🥇 Excellent" if pct >= 80 else ("🥈 Validé" if pct >= 50 else "⚠️ À Consolider")
                hist_display.append({
                    'Date & Heure': h['date'],
                    'Épreuve / Quiz': h.get('quiz', 'Grand Quiz'),
                    'Note Obtenue': f"{h['score']} / {h['total']}",
                    'Taux de Réussite': f"{pct:.1f} %",
                    'Statut d\'Acquisition': mention
                })
            st.dataframe(pd.DataFrame(hist_display), use_container_width=True)

        else:
            st.info("💡 Vous n'avez pas encore passé d'évaluation enregistrée. Lancez un test dans 'Programme Semaine par Semaine' ou le 'Grand Quiz' pour générer vos premières métriques !")

    with tab_an2:
        st.subheader("2. Radar de Maîtrise des 7 Domaines du BTS CIEL")
        st.markdown("<p style='color: #94a3b8;'>Ce radar est calculé en temps réel d'après vos résultats aux quiz, aux laboratoires pratiques et aux 105 flashcards d'examen.</p>", unsafe_allow_html=True)
        
        mastery = user_data.get('domain_mastery', {
            'Réseaux & Télécoms': 70,
            'Cybersécurité & Hardening': 65,
            'Programmation C++ & Python': 55,
            'Administration Système & AD': 60,
            'Électronique & Bus': 50,
            'Mathématiques Appliquées': 45,
            'Modélisation SysML & E6': 40
        })

        col_rad, col_rec = st.columns([1.2, 1])
        with col_rad:
            labels = list(mastery.keys())
            values = list(mastery.values())
            num_vars = len(labels)
            
            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
            values_plot = values + [values[0]]
            angles += angles[:1]
            
            fig_rad, ax_rad = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True), facecolor='#090e1d')
            ax_rad.set_facecolor('#0d1527')
            ax_rad.plot(angles, values_plot, color='#38bdf8', linewidth=2.5, linestyle='solid')
            ax_rad.fill(angles, values_plot, color='#38bdf8', alpha=0.3)
            ax_rad.set_xticks(angles[:-1])
            ax_rad.set_xticklabels(labels, color='#f8fafc', fontsize=9, fontweight=600)
            ax_rad.set_ylim(0, 100)
            ax_rad.set_yticks([25, 50, 75, 100])
            ax_rad.set_yticklabels(['25%', '50%', '75%', '100%'], color='#64748b', fontsize=8)
            ax_rad.grid(color='#1e293b', linestyle='--')
            ax_rad.spines['polar'].set_color('#334155')
            st.pyplot(fig_rad)
            plt.close()

        with col_rec:
            st.markdown("#### 🎯 Diagnostic Personnalisé de l'Assistant")
            weakest_dom = min(mastery, key=mastery.get)
            weakest_val = mastery[weakest_dom]
            strongest_dom = max(mastery, key=mastery.get)
            strongest_val = mastery[strongest_dom]
            
            st.markdown(f"""
            <div class='ciel-card' style='border-left: 5px solid #34d399 !important; margin-bottom: 14px;'>
                <h5 style='color: #34d399; margin: 0;'>🌟 Votre Point Fort Majeur</h5>
                <p style='margin: 4px 0; color: #f8fafc;'><b>{strongest_dom}</b> : <b>{strongest_val}%</b> de maîtrise.</p>
                <span style='font-size: 0.85rem; color: #94a3b8;'>Vos automatismes sont excellents sur ce pilier. Poursuivez les révisions réflexes.</span>
            </div>
            
            <div class='ciel-card' style='border-left: 5px solid #f43f5e !important;'>
                <h5 style='color: #f43f5e; margin: 0;'>⚠️ Votre Priorité de Travail Actuelle</h5>
                <p style='margin: 4px 0; color: #f8fafc;'><b>{weakest_dom}</b> : <b>{weakest_val}%</b> de maîtrise.</p>
                <span style='font-size: 0.85rem; color: #cbd5e1;'>C'est le module où vous avez le plus de points à gagner pour le BTS Blanc. Révisez les fiches associées dans le Grand Référentiel !</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### 📊 Taux de Maîtrise Détaillés")
            for d, rate in mastery.items():
                st.write(f"**{d}** : {rate}% de réussite")
                st.progress(rate / 100)

    with tab_an3:
        st.subheader("3. Galerie des Trophées & Badges Débloqués")
        badges = user_data.get('badges', [])
        
        col_b1, col_b2, col_b3 = st.columns(3)
        all_possible_badges = [
            {'id': 'first_step', 'nom': 'Pied à l\'Étrier', 'desc': 'Première session d\'évaluation complétée', 'icon': '🎯'},
            {'id': 'net_rookie', 'nom': 'Architecte Réseau', 'desc': 'Score >= 8/10 en Réseaux & Commutation', 'icon': '📶'},
            {'id': 'pts_100', 'nom': 'Centurion CIEL', 'desc': 'Cap des 100 points XP franchi !', 'icon': '💯'},
            {'id': 'pts_300', 'nom': 'Maître de l\'Atelier', 'desc': 'Cap des 300 points XP franchi !', 'icon': '🏆'},
            {'id': 'cyber_ninja', 'nom': 'Gardien ANSSI', 'desc': 'Tous les labs de durcissement réussis', 'icon': '🛡️'},
            {'id': 'code_master', 'nom': 'As du C++', 'desc': 'Zéro fuite mémoire dans les sandboxes', 'icon': '💻'}
        ]
        
        unlocked_ids = {b['id']: b for b in badges}
        
        for idx, b in enumerate(all_possible_badges):
            target_col = [col_b1, col_b2, col_b3][idx % 3]
            is_unlocked = b['id'] in unlocked_ids
            b_info = unlocked_ids[b['id']] if is_unlocked else b
            
            with target_col:
                if is_unlocked:
                    st.markdown(f"""
                    <div class='ciel-card' style='border: 1px solid #34d399 !important; background: rgba(6, 78, 59, 0.2); text-align: center; padding: 20px 14px;'>
                        <div style='font-size: 2.5rem; margin-bottom: 6px;'>{b_info['icon']}</div>
                        <h4 style='color: #34d399; margin: 0;'>{b_info['nom']}</h4>
                        <p style='font-size: 0.85rem; color: #cbd5e1; margin: 6px 0;'>{b_info['desc']}</p>
                        <span class='badge badge-emerald'>Débloqué le {b_info.get('date', 'Récemment')}</span>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='ciel-card' style='border: 1px solid rgba(255, 255, 255, 0.08) !important; background: rgba(15, 23, 42, 0.4); text-align: center; padding: 20px 14px; opacity: 0.6;'>
                        <div style='font-size: 2.5rem; margin-bottom: 6px; filter: grayscale(100%);'>{b['icon']}</div>
                        <h4 style='color: #94a3b8; margin: 0;'>{b['nom']}</h4>
                        <p style='font-size: 0.85rem; color: #64748b; margin: 6px 0;'>{b['desc']}</p>
                        <span class='badge' style='background: rgba(100, 116, 139, 0.2); color: #94a3b8; border: 1px solid #475569;'>🔒 Verrouillé</span>
                    </div>
                    """, unsafe_allow_html=True)

    with tab_an4:
        st.subheader("4. Gestion Multi-Profils & Synchronisation Cloud")
        st.markdown("<p style='color: #94a3b8;'>Passez d'un compte étudiant à un autre, sauvegardez votre progression ou restaurez vos scores depuis un autre appareil.</p>", unsafe_allow_html=True)
        
        c_u1, c_u2 = st.columns(2)
        with c_u1:
            st.markdown("#### 👥 Changer d'Utilisateur ou Créer un Compte")
            users_db = load_users()
            all_known = list(users_db.keys())
            if not all_known:
                all_known = [DEFAULT_USER]
            if DEFAULT_USER not in all_known:
                all_known = [DEFAULT_USER] + all_known
                
            cur_idx = all_known.index(u_name) if u_name in all_known else 0
            selected_existing = st.selectbox("Basculer vers un profil existant :", all_known, index=cur_idx, key="sel_switch_user")
            
            if st.button("Charger ce profil", key="btn_switch_profile"):
                if selected_existing != u_name:
                    st.session_state.current_user = selected_existing
                    st.session_state.user_progress = users_db.get(selected_existing, create_default_user_data(selected_existing))
                    st.session_state.user_role = st.session_state.user_progress.get('role', 'Candidat Option A')
                    st.success(f"Session basculée sur : {selected_existing} !")
                    st.rerun()

            st.markdown("---")
            st.markdown("#### ➕ Créer un Nouveau Profil Étudiant")
            new_u_name = st.text_input("Nom de l'étudiant ou Pseudo :", placeholder="ex: Thomas_R, Sarah_CIEL...", key="new_u_field")
            new_u_role = st.selectbox("Spécialité :", ["Candidat Option A (Informatique & Réseaux)", "Candidat Option B (Électronique & Réseaux)", "Enseignant / Tuteur"], key="new_u_role_sel")
            
            if st.button("Créer & Activer ce Profil", key="btn_create_new_u"):
                clean_name = new_u_name.strip()
                if clean_name:
                    db = load_users()
                    if clean_name not in db:
                        new_data = create_default_user_data(clean_name, new_u_role)
                        db[clean_name] = new_data
                        save_users(db)
                    st.session_state.current_user = clean_name
                    st.session_state.user_role = new_u_role
                    st.session_state.user_progress = db[clean_name]
                    st.success(f"Profil '{clean_name}' créé et activé avec succès !")
                    st.rerun()
                else:
                    st.warning("Veuillez saisir un nom ou pseudo valide.")

        with c_u2:
            st.markdown("#### ☁️ Sauvegarde Cloud & Export / Import JSON")
            st.info("Toutes vos données (scores, dates d'examens, progression des flashcards et points XP) sont conservées en local et peuvent être téléchargées sous forme de fichier JSON léger pour être transférées vers un autre PC ou smartphone.")
            
            export_payload = {
                'app': 'BTS_CIEL_Studio_Pro',
                'version': 'v37',
                'exported_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'user_profile': user_data
            }
            st.download_button(
                label=f"📥 Télécharger ma progression ({u_name}.json)",
                data=json.dumps(export_payload, ensure_ascii=False, indent=2),
                file_name=f"bts_ciel_backup_{u_name}_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json",
                key="btn_download_backup"
            )
            
            st.markdown("---")
            st.markdown("#### 📤 Restaurer un Profil depuis un fichier JSON")
            uploaded_backup = st.file_uploader("Importer une sauvegarde (.json) :", type=['json'], key="upload_backup_file")
            if uploaded_backup is not None:
                try:
                    data_imported = json.load(uploaded_backup)
                    if 'user_profile' in data_imported and 'username' in data_imported['user_profile']:
                        imported_prof = data_imported['user_profile']
                        imp_name = imported_prof['username']
                        db = load_users()
                        db[imp_name] = imported_prof
                        save_users(db)
                        st.session_state.current_user = imp_name
                        st.session_state.user_progress = imported_prof
                        st.session_state.user_role = imported_prof.get('role', 'Candidat Option A')
                        st.success(f"🎉 Profil '{imp_name}' restauré avec succès ! Score et progression actualisés.")
                        st.rerun()
                    else:
                        st.error("Format de sauvegarde invalide (clé 'user_profile' absente).")
                except Exception as e:
                    st.error(f"Erreur lors du décodage du fichier : {e}")

            st.markdown("---")
            st.markdown("#### 🗑️ Zone de Réinitialisation")
            if st.button("Réinitialiser l'historique de mes scores uniquement", key="btn_reset_my_scores"):
                user_data['history'] = []
                update_active_user_data(user_data)
                st.success("Votre historique de scores a été remis à zéro.")
                st.rerun()



# Advanced Interactive Simulator & Practice Lab for BTS CIEL (All 5 Sections Expanded)
import streamlit as st

def render_extended_lab():
    st.markdown("<div class='hero-title'>🧪 Le Laboratoire Pratique & Simulateurs Avancés</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Environnement d'expérimentation interactive : exécutez et validez des commandes réelles sous Cisco IOS, Linux Debian, C++ Debugging, Active Directory PowerShell et IoT Industriel. <i>Les champs sont vierges pour tester vos réflexes d'examen — utilisez le bouton 'Indice' en cas d'hésitation.</i></p>", unsafe_allow_html=True)

    t_cisco, t_linux, t_cpp, t_ad, t_iot = st.tabs([
        "📶 1. Cisco IOS Switch & Routeur",
        "🖥️ 2. Linux Debian & Administration",
        "💻 3. C++ Debugger, Mémoire & POO",
        "🔒 4. Active Directory & PowerShell",
        "🔌 5. IoT Industriel, Modbus & MQTT"
    ])

    # =========================================================================
    # 1. CISCO IOS TERMINAL LAB
    # =========================================================================
    with t_cisco:
        st.subheader("📶 Centre de Commandes Cisco IOS (Épreuves E4 & E5)")
        st.markdown("<p style='color:#94a3b8;'>Simulateur en ligne de commandes avec invite réaliste et validation de conformité syntaxique.</p>", unsafe_allow_html=True)
        
        cisco_mode = st.selectbox("Sélectionnez l'atelier Cisco :", [
            "Atelier 1 : Configuration VLAN & Mode Accès",
            "Atelier 2 : Configuration d'un Trunk 802.1Q",
            "Atelier 3 : Routage Inter-VLAN (Router-on-a-Stick)",
            "Atelier 4 : Sécurité des Ports (Port Security Sticky & Violation)",
            "Atelier 5 : Routage Statique IPv4 & Route par Défaut",
            "Atelier 6 : Serveur DHCP Cisco avec Plage d'Exclusion",
            "Atelier 7 : Translation NAT Dynamique avec Surcharge (PAT)",
            "Atelier 8 : Sécurisation SSH VTY & Crypto RSA",
            "Atelier 9 : Rapid Spanning Tree Protocol (RSTP 802.1w & PortFast)",
            "Atelier 10 : Diagnostic Réseau & Commandes 'Show' Cruciales"
        ], key="sel_cisco_lab")

        st.markdown("<div class='terminal-header'><span class='terminal-dot dot-red'></span><span class='terminal-dot dot-yellow'></span><span class='terminal-dot dot-green'></span> &nbsp; Cisco Catalyst Switch / Router IOS Shell</div>", unsafe_allow_html=True)

        if "Atelier 1 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Switch# configure terminal<br>Switch(config)# interface FastEthernet0/5</div>", unsafe_allow_html=True)
            st.write("1. Passez le port `FastEthernet0/5` en mode accès inconditionnel :")
            c1_1 = st.text_input("Commande 1 :", value="", key="lab_c1_1")
            st.write("2. Affectez ce port au **VLAN 40** (département R&D) :")
            c1_2 = st.text_input("Commande 2 :", value="", key="lab_c1_2")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c1 = st.button("Valider la configuration", key="btn_chk_c1")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Cisco** : Pour passer en mode accès, la syntaxe est `switchport mode access`. Pour lier le port à un VLAN, utilisez `switchport access vlan <ID>`.")
            
            if chk_c1:
                r1 = c1_1.strip().lower().replace("  ", " ")
                r2 = c1_2.strip().lower().replace("  ", " ")
                if r1 in ["switchport mode access", "sw m a"] and r2 in ["switchport access vlan 40", "sw acc vlan 40"]:
                    st.success("✅ **Configuration IOS Parfaite !** Le port est configuré en mode accès sur le VLAN 40 (+20 XP).")
                    add_user_points(20, "lab_cisco_vlan_access")
                else:
                    st.error("❌ Erreur. Commandes attendues : `switchport mode access` puis `switchport access vlan 40`.")

        elif "Atelier 2 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Switch(config)# interface GigabitEthernet0/1</div>", unsafe_allow_html=True)
            st.write("1. Activez le mode Trunk IEEE 802.1Q inconditionnel sur l'interface `g0/1` :")
            c2_1 = st.text_input("Commande Trunk :", value="", key="lab_c2_1")
            st.write("2. Définissez le **VLAN 99** comme VLAN natif non tagué :")
            c2_2 = st.text_input("Commande VLAN Natif :", value="", key="lab_c2_2")
            st.write("3. Restreignez les VLANs autorisés aux seuls VLANs 10, 20 et 40 :")
            c2_3 = st.text_input("Commande Filtrage VLANs :", value="", key="lab_c2_3")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c2 = st.button("Valider le Trunk", key="btn_chk_c2")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Trunking** : `switchport mode trunk`, `switchport trunk native vlan <ID>`, et `switchport trunk allowed vlan <liste>`.")
            
            if chk_c2:
                if "switchport mode trunk" in c2_1.lower() and "switchport trunk native vlan 99" in c2_2.lower() and ("allowed vlan 10,20,40" in c2_3.lower().replace(" ", "") or "allowed vlan 10, 20, 40" in c2_3.lower()):
                    st.success("✅ **Trunk 802.1Q Conforme !** Le lien d'agrégation filtre les flux et sécurise le VLAN natif (+25 XP).")
                    add_user_points(25, "lab_cisco_trunk")
                else:
                    st.error("❌ Erreur. Commandes : `switchport mode trunk`, `switchport trunk native vlan 99`, `switchport trunk allowed vlan 10,20,40`.")

        elif "Atelier 3 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Router(config)# interface GigabitEthernet0/0/0.20</div>", unsafe_allow_html=True)
            st.write("1. Activez l'encapsulation 802.1Q pour le **VLAN 20** sur cette sous-interface :")
            c3_1 = st.text_input("Commande Encapsulation :", value="", key="lab_c3_1")
            st.write("2. Attribuez l'adresse IP de passerelle `192.168.20.254` avec le masque `/24` :")
            c3_2 = st.text_input("Commande Adresse IP :", value="", key="lab_c3_2")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c3 = st.button("Valider la sous-interface", key="btn_chk_c3")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Router-on-a-Stick** : Définissez impérativement l'encapsulation AVANT d'attribuer l'adresse IP : `encapsulation dot1Q <vlan_id>` puis `ip address <ip> <masque_décimal_pointé>`.")
            
            if chk_c3:
                if "encapsulation dot1q 20" in c3_1.lower() and "192.168.20.254 255.255.255.0" in c3_2:
                    st.success("✅ **Sous-Interface Opérationnelle !** Le routeur assure désormais le routage inter-VLAN (+25 XP).")
                    add_user_points(25, "lab_cisco_subif")
                else:
                    st.error("❌ Commandes attendues : `encapsulation dot1Q 20` puis `ip address 192.168.20.254 255.255.255.0`.")

        elif "Atelier 4 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Switch(config-if)# [Port Security Configuration]</div>", unsafe_allow_html=True)
            st.write("1. Activez la sécurité des ports (*Port-Security*) :")
            c4_1 = st.text_input("Activation :", value="", key="lab_c4_1")
            st.write("2. Fixez le nombre maximal d'adresses MAC autorisées à **2** :")
            c4_2 = st.text_input("Maximum :", value="", key="lab_c4_2")
            st.write("3. Activez l'apprentissage dynamique et persistant des adresses (**Sticky**) :")
            c4_3 = st.text_input("Mode Sticky :", value="", key="lab_c4_3")
            st.write("4. Configurez l'action en cas d'intrusion pour désactiver le port (**Shutdown**) :")
            c4_4 = st.text_input("Violation :", value="", key="lab_c4_4")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c4 = st.button("Valider Port Security", key="btn_chk_c4")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Port Security** : `switchport port-security`, `switchport port-security maximum 2`, `switchport port-security mac-address sticky`, et `switchport port-security violation shutdown`.")
            
            if chk_c4:
                cond = ("switchport port-security" in c4_1.lower() and "maximum 2" in c4_2.lower() and 
                        "sticky" in c4_3.lower() and "shutdown" in c4_4.lower())
                if cond:
                    st.success("✅ **Port Sécurisé contre les intrusions !** En cas de branchement pirate, le port passe en état *err-disabled* (+25 XP).")
                    add_user_points(25, "lab_cisco_port_sec")
                else:
                    st.error("❌ Vérifiez la syntaxe complète des 4 commandes switchport port-security.")

        elif "Atelier 5 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Router(config)# [Routage Statique IPv4]</div>", unsafe_allow_html=True)
            st.write("Saisissez la commande pour créer une **route par défaut** (toutes destinations) pointant vers la passerelle FAI `203.0.113.1` :")
            c5 = st.text_input("Commande Route par Défaut :", value="", key="lab_c5")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c5 = st.button("Valider la route", key="btn_chk_c5")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Routage Statique** : La route par défaut utilise le préfixe quadruple zéro : `ip route 0.0.0.0 0.0.0.0 <IP_NextHop>`.")
            
            if chk_c5:
                if c5.strip() == "ip route 0.0.0.0 0.0.0.0 203.0.113.1":
                    st.success("✅ **Route par Défaut Active !** Tout trafic sans route plus spécifique est routé vers le FAI (+15 XP).")
                    add_user_points(15, "lab_cisco_route_def")
                else:
                    st.error("❌ Commande exacte : `ip route 0.0.0.0 0.0.0.0 203.0.113.1`.")

        elif "Atelier 6 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Router(config)# [Serveur DHCP Cisco IOS]</div>", unsafe_allow_html=True)
            st.write("1. Excluez les adresses statiques de `192.168.10.1` à `192.168.10.20` de la distribution DHCP :")
            c6_1 = st.text_input("Commande d'Exclusion :", value="", key="lab_c6_1")
            st.write("2. Créez le pool DHCP nommé `POOL_LAN` :")
            c6_2 = st.text_input("Création du Pool :", value="", key="lab_c6_2")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c6 = st.button("Valider DHCP", key="btn_chk_c6")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo DHCP Cisco** : Pour exclure : `ip dhcp excluded-address <start> <end>`. Pour créer le pool : `ip dhcp pool <NOM>`.")
            
            if chk_c6:
                if "ip dhcp excluded-address 192.168.10.1 192.168.10.20" in c6_1.strip() and "ip dhcp pool POOL_LAN" in c6_2.strip():
                    st.success("✅ **Pool DHCP Configuré !** Les adresses statiques sont protégées contre les conflits (+20 XP).")
                    add_user_points(20, "lab_cisco_dhcp")
                else:
                    st.error("❌ Commandes attendues : `ip dhcp excluded-address 192.168.10.1 192.168.10.20` et `ip dhcp pool POOL_LAN`.")

        elif "Atelier 7 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Router(config)# [Translation NAT Dynamique / PAT]</div>", unsafe_allow_html=True)
            st.write("Saisissez la commande de surcharge (PAT) liant la liste d'accès 1 à l'interface de sortie `GigabitEthernet0/0/1` :")
            c7 = st.text_input("Commande NAT Overload :", value="", key="lab_c7")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c7 = st.button("Valider le PAT", key="btn_chk_c7")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo NAT/PAT** : Syntaxe universelle : `ip nat inside source list <ACL_ID> interface <INTERFACE_OUT> overload`.")
            
            if chk_c7:
                if "ip nat inside source list 1 interface gigabitethernet0/0/1 overload" in c7.strip().lower():
                    st.success("✅ **PAT Opérationnel !** Les flux internes sont traduits avec multiplexage des numéros de ports (+25 XP).")
                    add_user_points(25, "lab_cisco_pat")
                else:
                    st.error("❌ Commande exacte : `ip nat inside source list 1 interface GigabitEthernet0/0/1 overload`.")

        elif "Atelier 8 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Router(config)# [Génération de Clé Cryptographique SSH]</div>", unsafe_allow_html=True)
            st.write("Saisissez la commande pour générer une bi-clé asymétrique RSA de 2048 bits pour le serveur SSH :")
            c8 = st.text_input("Commande Crypto RSA :", value="", key="lab_c8")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c8 = st.button("Valider la clé RSA", key="btn_chk_c8")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo SSH Cisco** : `crypto key generate rsa general-keys modulus 2048`.")
            
            if chk_c8:
                if "crypto key generate rsa" in c8.lower() and "2048" in c8:
                    st.success("✅ **Clé RSA de 2048 bits générée !** Le démon SSHv2 est désormais activé (+20 XP).")
                    add_user_points(20, "lab_cisco_rsa")
                else:
                    st.error("❌ Commande exacte : `crypto key generate rsa general-keys modulus 2048`.")

        elif "Atelier 9 :" in cisco_mode:
            st.markdown("<div class='terminal-body'>Switch(config)# [Spanning Tree Protocol Rapid STP]</div>", unsafe_allow_html=True)
            st.write("1. Activez le protocole Rapid Spanning-Tree (IEEE 802.1w) sur l'ensemble du switch :")
            c9_1 = st.text_input("Mode Spanning-Tree :", value="", key="lab_c9_1")
            st.write("2. Sur le port hôte utilisateur `FastEthernet0/10`, activez l'activation immédiate sans écoute (*PortFast*) :")
            c9_2 = st.text_input("Activation PortFast :", value="", key="lab_c9_2")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c9 = st.button("Valider RSTP", key="btn_chk_c9")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Spanning Tree** : `spanning-tree mode rapid-pvst` puis sous l'interface `spanning-tree portfast`.")
            
            if chk_c9:
                if "spanning-tree mode rapid-pvst" in c9_1.lower() and "spanning-tree portfast" in c9_2.lower():
                    st.success("✅ **RSTP & PortFast activés !** La convergence est instantanée et les postes accèdent au réseau en < 1s (+20 XP).")
                    add_user_points(20, "lab_cisco_rstp")
                else:
                    st.error("❌ Commandes : `spanning-tree mode rapid-pvst` et `spanning-tree portfast`.")

        else:
            st.markdown("<div class='terminal-body'>Switch# [Diagnostic de Trame & Table CAM]</div>", unsafe_allow_html=True)
            st.write("Quelle commande privilégiée permet d'afficher la table complète des adresses MAC apprises par le switch ?")
            c10 = st.text_input("Commande d'affichage MAC :", value="", key="lab_c10")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_c10 = st.button("Exécuter la commande show", key="btn_chk_c10")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Diagnostic** : `show mac address-table` (ou `show mac-address-table` selon les versions IOS).")
            
            if chk_c10:
                if c10.strip().lower() in ["show mac address-table", "show mac-address-table", "sh mac address-table"]:
                    st.success("✅ **Table CAM affichée !** La table associe les adresses MAC aux ports et aux VLANs (+15 XP).")
                    add_user_points(15, "lab_cisco_show_mac")
                else:
                    st.error("❌ Commande exacte : `show mac address-table`.")

    # =========================================================================
    # 2. LINUX DEBIAN LAB
    # =========================================================================
    with t_linux:
        st.subheader("🖥️ Centre de Commandes Linux Debian & SysAdmin")
        st.markdown("<p style='color:#94a3b8;'>Simulateur Bash Debian : saisissez les commandes d'administration et de gestion des droits système.</p>", unsafe_allow_html=True)
        
        lx_mode = st.selectbox("Sélectionnez l'atelier Linux :", [
            "Atelier 1 : Attribution de Droits Fines (chmod octal & symbolique)",
            "Atelier 2 : Droits Spéciaux (SUID, SGID, Sticky Bit)",
            "Atelier 3 : Listes de Contrôle d'Accès (ACLs POSIX getfacl / setfacl)",
            "Atelier 4 : Gestion des Utilisateurs & Fichier Sudoers",
            "Atelier 5 : Contrôle des Services avec systemctl & Logs journalctl",
            "Atelier 6 : Analyse Réseau & Sockets Écoute (ss / ip)",
            "Atelier 7 : Scripting Bash & Variables Spéciales ($?, $#, $*)"
        ], key="sel_lx_lab")

        st.markdown("<div class='terminal-header'><span class='terminal-dot dot-red'></span><span class='terminal-dot dot-yellow'></span><span class='terminal-dot dot-green'></span> &nbsp; root@debian-server:~# (Bash Shell)</div>", unsafe_allow_html=True)

        if "Atelier 1 :" in lx_mode:
            st.write("Saisissez la commande octale pour que le script `/srv/deploy.sh` soit en lecture/écriture/exécution (rwx) pour le propriétaire, lecture/exécution (r-x) pour le groupe, et aucun accès pour les tiers :")
            lx1 = st.text_input("Commande chmod :", value="", key="lab_lx1")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_lx1 = st.button("Exécuter chmod", key="btn_chk_lx1")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo chmod** : `rwx` = 4+2+1 = 7, `r-x` = 4+0+1 = 5, `---` = 0. Soit `chmod 750 <fichier>`.")
            
            if chk_lx1:
                if lx1.strip() == "chmod 750 /srv/deploy.sh":
                    st.success("✅ **Permissions appliquées !** Droits : `-rwxr-x---` (+15 XP).")
                    add_user_points(15, "lab_lx_chmod")
                else:
                    st.error("❌ Commande exacte attendue : `chmod 750 /srv/deploy.sh`.")

        elif "Atelier 2 :" in lx_mode:
            st.write("Saisissez la commande pour activer le **SGID** (2000) et donner les droits 770 au répertoire collaboratif `/var/partage` :")
            lx2 = st.text_input("Commande SGID :", value="", key="lab_lx2")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_lx2 = st.button("Exécuter SGID", key="btn_chk_lx2")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo SGID** : La valeur du droit spécial SGID est 2. On préfixe les 3 chiffres classiques : `chmod 2770 <dossier>`.")
            
            if chk_lx2:
                if lx2.strip() == "chmod 2770 /var/partage":
                    st.success("✅ **SGID appliqué !** Tout nouveau fichier hérite désormais du groupe propriétaire (+20 XP).")
                    add_user_points(20, "lab_lx_sgid")
                else:
                    st.error("❌ Commande exacte attendue : `chmod 2770 /var/partage`.")

        elif "Atelier 3 :" in lx_mode:
            st.write("Attribuez les droits d'écriture et de lecture (`rw-`) spécifiquement à l'utilisateur `bob` sur le fichier `/etc/app.conf` via une ACL POSIX :")
            lx3 = st.text_input("Commande setfacl :", value="", key="lab_lx3")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_lx3 = st.button("Exécuter setfacl", key="btn_chk_lx3")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo ACL POSIX** : `setfacl -m u:<user>:<droits> <chemin_fichier>`.")
            
            if chk_lx3:
                if lx3.strip() in ["setfacl -m u:bob:rw- /etc/app.conf", "setfacl -m u:bob:rw /etc/app.conf"]:
                    st.success("✅ **ACL POSIX créée avec succès !** `getfacl` affichera désormais la ligne `user:bob:rw-` (+20 XP).")
                    add_user_points(20, "lab_lx_acl")
                else:
                    st.error("❌ Commande exacte : `setfacl -m u:bob:rw /etc/app.conf`.")

        elif "Atelier 4 :" in lx_mode:
            st.write("Créez un nouvel utilisateur nommé `technicien` avec création de son dossier personnel `/home/technicien` et assignation du shell `/bin/bash` :")
            lx4 = st.text_input("Commande useradd :", value="", key="lab_lx4")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_lx4 = st.button("Exécuter useradd", key="btn_chk_lx4")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Gestion Comptes** : `useradd -m -s /bin/bash <nom>` (-m pour créer le home, -s pour le shell).")
            
            if chk_lx4:
                if "useradd" in lx4 and "-m" in lx4 and "/bin/bash" in lx4 and "technicien" in lx4:
                    st.success("✅ **Compte utilisateur créé avec succès !** (+15 XP).")
                    add_user_points(15, "lab_lx_useradd")
                else:
                    st.error("❌ Commande exacte : `useradd -m -s /bin/bash technicien`.")

        elif "Atelier 5 :" in lx_mode:
            st.write("Rechargez à chaud la configuration du démon SSH sans couper les connexions actives :")
            lx5 = st.text_input("Commande systemctl :", value="", key="lab_lx5")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_lx5 = st.button("Exécuter systemctl", key="btn_chk_lx5")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Services** : `systemctl reload ssh` (ou `systemctl reload sshd`).")
            
            if chk_lx5:
                if lx5.strip().lower() in ["systemctl reload ssh", "systemctl reload sshd"]:
                    st.success("✅ **Démon rechargé avec succès !** La directive reload relit `/etc/ssh/sshd_config` sans rupture (+15 XP).")
                    add_user_points(15, "lab_lx_systemctl")
                else:
                    st.error("❌ Commande exacte : `systemctl reload ssh`.")

        elif "Atelier 6 :" in lx_mode:
            st.write("Affichez tous les ports en écoute (**Listening**) en **TCP** et **UDP** avec les numéros de ports numériques et les noms de processus via la commande moderne `ss` :")
            lx6 = st.text_input("Commande ss :", value="", key="lab_lx6")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_lx6 = st.button("Exécuter ss", key="btn_chk_lx6")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Sockets** : Les options sont : `t` (TCP), `u` (UDP), `l` (Listening), `p` (Process), `n` (Numeric). Soit `ss -tulpn`.")
            
            if chk_lx6:
                opt = lx6.strip().replace(" ", "").replace("-", "")
                if "ss" in lx6 and all(c in opt for c in ["t", "u", "l", "p", "n"]):
                    st.success("✅ **Inspection des Sockets Réseau Conforme !** Commande : `ss -tulpn` (+20 XP).")
                    add_user_points(20, "lab_lx_ss")
                else:
                    st.error("❌ Commande exacte : `ss -tulpn`.")

        else:
            st.write("En script Bash Linux, quelle variable spéciale contient le **code de retour (statut de sortie)** de la dernière commande exécutée ?")
            lx7 = st.text_input("Variable Bash spéciale :", value="", key="lab_lx7")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_lx7 = st.button("Valider la variable", key="btn_chk_lx7")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Bash** : `$?` renvoie 0 en cas de succès, une valeur non nulle en cas d'erreur. `$#` donne le nombre d'arguments, `$$` le PID.")
            
            if chk_lx7:
                if lx7.strip() == "$?":
                    st.success("✅ **Exact !** `$?` vaut 0 si la commande s'est déroulée avec succès (+15 XP).")
                    add_user_points(15, "lab_lx_var")
                else:
                    st.error("❌ La variable d'état de sortie est `$?`.")

    # =========================================================================
    # 3. C++ DEBUGGER & POO LAB
    # =========================================================================
    with t_cpp:
        st.subheader("💻 Centre de Programmation C++ & Débogage Mémoire")
        st.markdown("<p style='color:#94a3b8;'>Entraînez-vous aux pièges mémoires et à la rigueur de la Programmation Orientée Objet en C++.</p>", unsafe_allow_html=True)
        
        cpp_mode = st.selectbox("Sélectionnez l'exercice C++ :", [
            "Exercice 1 : Libération d'un Tableau Dynamique (new[] vs delete[])",
            "Exercice 2 : Déclaration d'une Méthode Virtuelle Pure (Classe Abstraite)",
            "Exercice 3 : Pointeur Intelligent Unique (std::unique_ptr en C++11)",
            "Exercice 4 : Encapsulation & Accesseur const (Getter)"
        ], key="sel_cpp_lab")

        st.markdown("<div class='terminal-header'><span class='terminal-dot dot-red'></span><span class='terminal-dot dot-yellow'></span><span class='terminal-dot dot-green'></span> &nbsp; g++ -std=c++17 -Wall -Werror main.cpp</div>", unsafe_allow_html=True)

        if "Exercice 1 :" in cpp_mode:
            st.code("""
int* bufferMesures = new int[4096];
// ... acquisition et traitement des données ...
// Écrivez l'instruction de libération mémoire ci-dessous :
            """, language="cpp")
            cpp1 = st.text_input("Instruction C++ :", value="", key="lab_cpp1")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_cpp1 = st.button("Compiler & Exécuter", key="btn_chk_cpp1")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo C++ Mémoire** : Tout tableau alloué avec `new Type[taille]` doit être libéré avec `delete[] nomPointeur;`.")
            
            if chk_cpp1:
                if cpp1.strip().replace(" ", "") == "delete[]bufferMesures;":
                    st.success("✅ **Zéro fuite mémoire !** L'opérateur `delete[]` libère l'intégralité du tableau (+20 XP).")
                    add_user_points(20, "lab_cpp_leak")
                else:
                    st.error("❌ Syntaxe exacte attendue : `delete[] bufferMesures;`.")

        elif "Exercice 2 :" in cpp_mode:
            st.code("""
class Capteur {
public:
    virtual ~Capteur() {}
    // Déclarez la méthode virtuelle pure 'lireValeur' retournant un float sans paramètre :
};
            """, language="cpp")
            cpp2 = st.text_input("Déclaration de la méthode virtuelle pure :", value="", key="lab_cpp2")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_cpp2 = st.button("Vérifier la classe abstraite", key="btn_chk_cpp2")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Méthode Virtuelle Pure** : Syntaxe : `virtual float lireValeur() = 0;`.")
            
            if chk_cpp2:
                if cpp2.strip().replace(" ", "").rstrip(";") == "virtualfloatlireValeur()=0":
                    st.success("✅ **Classe de Base Abstraite Validée !** Capteur devient une interface non instanciable (+20 XP).")
                    add_user_points(20, "lab_cpp_pure")
                else:
                    st.error("❌ Déclaration attendue : `virtual float lireValeur() = 0;`.")

        elif "Exercice 3 :" in cpp_mode:
            st.code("""
#include <memory>
// Instanciez un pointeur intelligent exclusif gérant dynamiquement un int valant 100 :
// auto ptr = ...
            """, language="cpp")
            cpp3 = st.text_input("Instruction make_unique :", value="", key="lab_cpp3")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_cpp3 = st.button("Vérifier le smart pointer", key="btn_chk_cpp3")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo C++11/14** : `std::make_unique<int>(100);` assure la sécurité RAII sans risque d'oubli de delete.")
            
            if chk_cpp3:
                if "std::make_unique<int>(100)" in cpp3.replace(" ", "") or "make_unique<int>(100)" in cpp3.replace(" ", ""):
                    st.success("✅ **Smart Pointer Robuste !** Libération automatique de la ressource en fin de portée (+20 XP).")
                    add_user_points(20, "lab_cpp_smart")
                else:
                    st.error("❌ Syntaxe attendue : `std::make_unique<int>(100);`.")

        else:
            st.code("""
class SondePression {
private:
    float pressionBar;
public:
    // Rédigez le getter en ligne (in-class) garantissant la non-modification de l'objet :
};
            """, language="cpp")
            cpp4 = st.text_input("Méthode accesseur const :", value="", key="lab_cpp4")
            
            col_b1, col_b2 = st.columns([1, 4])
            with col_b1:
                chk_cpp4 = st.button("Vérifier le getter", key="btn_chk_cpp4")
            with col_b2:
                with st.expander("💡 Indice & Mémo de Cours"):
                    st.info("📌 **Mémo Encapsulation** : `float getPressionBar() const { return pressionBar; }`.")
            
            if chk_cpp4:
                clean = cpp4.strip().replace(" ", "")
                if "float" in clean and "const" in clean and "returnpressionBar;" in clean:
                    st.success("✅ **Accesseur const Conforme !** L'encapsulation est parfaitement respectée (+20 XP).")
                    add_user_points(20, "lab_cpp_getter")
                else:
                    st.error("❌ Syntaxe attendue : `float getPressionBar() const { return pressionBar; }`.")

    # =========================================================================
    # 4. ACTIVE DIRECTORY & POWERSHELL LAB
    # =========================================================================
    with t_ad:
        st.subheader("🔒 Centre d'Administration Active Directory & PowerShell")
        st.markdown("<p style='color:#94a3b8;'>Automatisez l'administration du domaine Windows Server avec les cmdlets ActiveDirectory officielles.</p>", unsafe_allow_html=True)
        
        st.markdown("<div class='terminal-header'><span class='terminal-dot dot-red'></span><span class='terminal-dot dot-yellow'></span><span class='terminal-dot dot-green'></span> &nbsp; PS C:\\Windows\\System32\\WindowsPowerShell\\v1.0></div>", unsafe_allow_html=True)
        
        st.write("1. Créez une nouvelle Unité d'Organisation (OU) nommée `Ingénieurs` à la racine du domaine `DC=ciel,DC=local` :")
        ad1 = st.text_input("Cmdlet New-ADOrganizationalUnit :", value="", key="lab_ad1")
        
        st.write("2. Quelle commande force le rafraîchissement immédiat de toutes les stratégies de groupe (**GPO**) sur un poste client Windows ?")
        ad2 = st.text_input("Commande GPO Refresh :", value="", key="lab_ad2")
        
        col_b1, col_b2 = st.columns([1, 4])
        with col_b1:
            chk_ad = st.button("Exécuter sous PowerShell", key="btn_chk_ad")
        with col_b2:
            with st.expander("💡 Indice & Mémo de Cours"):
                st.info("📌 **Mémo PowerShell AD** : `New-ADOrganizationalUnit -Name 'Ingénieurs' -Path 'DC=ciel,DC=local'`. Pour forcer la GPO : `gpupdate /force`.")
        
        if chk_ad:
            c_ou = "new-adorganizationalunit" in ad1.lower() and "ingénieurs" in ad1.lower()
            c_gp = ad2.strip().lower() == "gpupdate /force"
            if c_ou and c_gp:
                st.success("✅ **Scripts PowerShell Validés !** L'OU est créée et les stratégies GPO sont actualisées (+25 XP).")
                add_user_points(25, "lab_ad_ps")
            else:
                st.error("❌ Vérifiez la syntaxe : `New-ADOrganizationalUnit -Name 'Ingénieurs' -Path 'DC=ciel,DC=local'` et `gpupdate /force`.")

    # =========================================================================
    # 5. IOT INDUSTRIEL, MODBUS & MQTT LAB
    # =========================================================================
    with t_iot:
        st.subheader("🔌 Centre d'Expérimentation IoT Industriel & Bus de Terrain")
        st.markdown("<p style='color:#94a3b8;'>Décodez des trames industrielles réelles et configurez les communications d'atelier.</p>", unsafe_allow_html=True)
        
        st.markdown("""
**Analyse de Trame Hexadécimale Modbus RTU (sur liaison série RS-485)** :
```text
[01] [03] [00 0A] [00 02] [E4 09]
```
        """)
        st.write("1. Quel est le rôle du premier octet `01` ?")
        iot1 = st.text_input("Rôle de l'octet 01 :", value="", key="lab_iot1")
        
        st.write("2. Quelle est la fonction Modbus standard invoquée par le code `03` ?")
        iot2 = st.text_input("Nom de la fonction 03 :", value="", key="lab_iot2")
        
        st.write("3. Combien de registres de 16 bits le maître demande-t-il de lire avec `00 02` ?")
        iot3 = st.text_input("Nombre de registres (chiffre) :", value="", key="lab_iot3")
        
        col_b1, col_b2 = st.columns([1, 4])
        with col_b1:
            chk_iot = st.button("Valider l'analyse de trame", key="btn_chk_iot")
        with col_b2:
            with st.expander("💡 Indice & Mémo de Cours"):
                st.info("📌 **Mémo Modbus RTU** : L'octet 1 est l'adresse de l'esclave (Slave ID). Le code `03` est **Read Holding Registers** (lecture de registres de maintien). `00 02` signifie 2 registres consécutifs.")
        
        if chk_iot:
            c1 = "esclave" in iot1.lower() or "slave" in iot1.lower() or "1" in iot1
            c2 = "holding" in iot2.lower() or "registre" in iot2.lower()
            c3 = iot3.strip() == "2"
            if c1 and c2 and c3:
                st.success("✅ **Trame Modbus Parfaitement Décortiquée !** Esclave N°1, fonction 03 (Read Holding Registers), lecture de 2 mots de 16 bits (+25 XP).")
                add_user_points(25, "lab_iot_modbus")
            else:
                st.error("❌ Réponses attendues : 1) Adresse Esclave (Slave ID 1), 2) Read Holding Registers, 3) 2 registres.")


HUBS_CONFIG = {
    "🏠 Mon Tableau de Bord & Profil": [
        ("Vue d'Ensemble & Métriques", "🏠 Accueil & Dashboard"),
        ("Remédiation & Lacunes Ciblées", "🎯 Remédiation & Lacunes Ciblées (BTS Blanc)"),
        ("Planning BTS Blanc (6 Semaines)", "🗓️ Planning Révisions BTS Blanc (9-11 Déc)"),
        ("Suivi & Analyse des Scores", "📈 Analyse des Scores"),
        ("Gestion de Projet E6 (Gantt)", "📋 Planning de Projet E6 (Gantt)"),
        ("Vidéothèque Recommandée", "📹 Vidéos de Cours"),
        ("Répertoire des Liens & Ressources", "🌐 Répertoire des Liens")
    ],
    "📖 Grand Référentiel Rangé par Matière": [
        ("📶 Réseaux & Télécoms (OSI, IP, VLAN, Routage)", "📶 Réseaux & Télécoms"),
        ("🛡️ Master Cybersécurité (EBIOS, PKI, pfSense, VPN)", "🛡️ TP Cybersécurité, Gouvernance & pfSense"),
        ("🔒 Cybersécurité Fondamentale (OWASP & Cryptographie)", "🔒 Cybersécurité & Gouvernance"),
        ("💻 Programmation & Dev (C++, Python, Algorithmique)", "💻 Programmation C++ & Python"),
        ("🖥️ Administration Système (Linux Debian & Active Directory)", "🖥️ Système Linux & Windows Server"),
        ("🔌 Électronique, Signaux & Bus (CAN, Modbus, I2C)", "🔌 Électronique & Bus Industriels"),
        ("📐 Mathématiques Appliquées (Suites, Exp/Ln, Décibels)", "📐 Mathématiques Appliquées"),
        ("🇬🇧 Anglais Technique & Datasheets Composants", "🇬🇧 Anglais Technique & Datasheets"),
        ("📖 Culture Générale & Expression (CGE 2025/2026)", "📖 Culture Générale & Expression (CGE)"),
        ("🛠️ Guide Pratique d'Atelier Épreuve E5", "🛠️ Fiches Réussite Épreuve E5 (TP & Pratique)")
    ],
    "🧪 Le Laboratoire Pratique & Expérimentations": [
        ("Centre de Commandes & Sandboxes Interactives", "💻 Sandboxes & Terminaux Pratiques"),
        ("Lab Décodeur Wireshark (Hex)", "🔍 Lab Décodeur Wireshark"),
        ("Captures de Trames PCAP Commentées", "🔍 Captures de Trames & Analyses Wireshark PCAP"),
        ("Calculateur de Subnetting VLSM & CAN", "🧮 Laboratoire de Calculs (Subnetting & Élec)"),
        ("Lab Oscilloscope & Mesures Physiques", "📺 Lab Oscilloscope & Mesures Physiques"),
        ("Lab Kirchhoff, Ohm & Circuits Élec", "⚡ Lab Kirchhoff, Ohm & Circuits"),
        ("Laboratoire Modélisation SysML & UML", "📐 Laboratoire UML & SysML"),
        ("Qualification Logicielle & Tests E6 (Pytest)", "🧪 Qualification & Tests E6"),
        ("Modèles de Livrables & Dossier PVL E6", "📁 Modèles de Livrables & PVL Épreuve E6")
    ],
    "🎯 Entraînement, Flashcards & Examens": [
        ("105 Flashcards Actives Interactives", "🗂️ Flashcards Actives"),
        ("Annales Officielles BTS (2024 à 2026)", "🎯 Annales BTS (2024 & 2025)"),
        ("Grand Quiz d'Examen (70 Questions)", "📝 Grand Quiz d'Examen"),
        ("Programme Semaine par Semaine (BTS Blanc)", "🗓️ Révision Semaine par Semaine (BTS Blanc)"),
        ("Hub de Révision Totale (131 Sources)", "🎯 Révision Totale BTS Blanc (9-11 Déc)")
    ]
}
# Sidebar Modern Header & Switcher
with st.sidebar:
    init_user_session()
    
    # Modern Monopo User Profile Header
    u_name = st.session_state.current_user
    u_pts = st.session_state.user_progress['points']
    u_lvl = st.session_state.user_progress['level']
    u_role = st.session_state.user_role
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(29, 78, 216, 0.15) 0%, rgba(15, 23, 42, 0.8) 100%); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 16px; padding: 16px; margin-bottom: 16px;'>
        <div style='display: flex; align-items: center; justify-content: space-between;'>
            <div>
                <span style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: #38bdf8; font-weight: 700;'>PROFIL ÉTUDIANT</span>
                <h3 style='margin: 2px 0 0 0; font-size: 1.15rem; color: #ffffff; font-weight: 700;'>{u_name}</h3>
                <span style='font-size: 0.8rem; color: #94a3b8;'>{u_role}</span>
            </div>
            <div style='background: rgba(56, 189, 248, 0.1); border-radius: 50%; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(56, 189, 248, 0.3); font-size: 1.3rem;'>
                ⚡
            </div>
        </div>
        <div style='margin-top: 12px; padding-top: 10px; border-top: 1px solid rgba(255, 255, 255, 0.08); display: flex; justify-content: space-between; align-items: center;'>
            <div>
                <span style='font-size: 0.72rem; color: #64748b; font-weight: 600;'>POINTS XP</span>
                <div style='font-size: 1.1rem; font-weight: 800; color: #fb923c;'>{u_pts} pts</div>
            </div>
            <div style='text-align: right;'>
                <span style='font-size: 0.72rem; color: #64748b; font-weight: 600;'>GRADE</span>
                <div style='font-size: 0.85rem; font-weight: 700; color: #34d399;'>{u_lvl}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("👤 Gérer mon Compte & Profil Cloud", expanded=False):
        c_mode = st.radio("Action :", ["Connexion / Création", "Exporter mes données (Cloud Sync)"], horizontal=True, key="user_act_radio")
        if "Connexion" in c_mode:
            nom_in = st.text_input("Nom d'utilisateur :", value="" if u_name == "Invité BTS CIEL" else u_name, key="input_username")
            role_in = st.selectbox("Option de spécialité :", ["Candidat Option A (Informatique & Réseaux)", "Candidat Option B (Électronique & Réseaux)", "Enseignant / Tuteur"], key="sel_role")
            if st.button("Enregistrer mon profil", key="btn_save_profile"):
                if nom_in.strip():
                    st.session_state.current_user = nom_in.strip()
                    st.session_state.user_role = role_in
                    db = load_users()
                    if nom_in not in db:
                        db[nom_in] = {'role': role_in, 'progress': st.session_state.user_progress}
                    else:
                        st.session_state.user_progress = db[nom_in].get('progress', st.session_state.user_progress)
                    save_users(db)
                    st.success(f"Bienvenue, {nom_in} ! Vos scores et accomplissements sont synchronisés.")
                    st.rerun()
        else:
            st.info("☁️ **Cloud Ready** : Vous pouvez exporter votre sauvegarde JSON pour la charger sur n'importe quel autre appareil ou la synchroniser.")
            st.download_button("Télécharger ma progression (JSON)", data=json.dumps(st.session_state.user_progress, indent=2), file_name=f"progression_ciel_{u_name}.json", mime="application/json")
    
    st.markdown("---")
    hub_choisi = st.radio("🚀 ESPACE DE TRAVAIL (4 HUBS) :", list(HUBS_CONFIG.keys()), index=0)
    
    st.markdown("---")
    modules_du_hub = HUBS_CONFIG[hub_choisi]
    labels_modules = [m[0] for m in modules_du_hub]
    label_choisi = st.selectbox("📂 Module actif :", labels_modules, key=f"sel_mod_{hub_choisi}")
    page = next((m[1] for m in modules_du_hub if m[0] == label_choisi), modules_du_hub[0][1])
    st.caption(f"📍 Navigation : `{hub_choisi}` › **{label_choisi}**")


if page == '🏠 Accueil & Dashboard':
    st.markdown("""
    <div class='hero-container'>
        <div class='hero-title'>⚡ BTS CIEL - Studio d'Excellence Numérique</div>
        <div class='hero-subtitle'>Plateforme d'élite pour la réussite des épreuves E4, E5 et E6 du BTS Cybersécurité, Informatique et réseaux, Électronique</div>
        <div style='margin-top: 15px; display: flex; flex-wrap: wrap; gap: 6px;'>
            <span class='badge badge-blue'>Option A : Informatique & Réseaux</span>
            <span class='badge badge-emerald'>Option B : Électronique & Réseaux</span>
            <span class='badge badge-purple'>UML & SysML Pro</span>
            <span class='badge badge-amber'>Conforme Annales 2024-2026</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='stat-box'><div class='stat-number'>8</div><div class='stat-label'>Matières Structurées</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stat-box'><div class='stat-number'>140+</div><div class='stat-label'>Questions de Cours & Quiz</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='stat-box'><div class='stat-number'>5</div><div class='stat-label'>Sandboxes Pratiques Réelles</div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='stat-box'><div class='stat-number'>105</div><div class='stat-label'>Flashcards Actives 3D</div></div>", unsafe_allow_html=True)
    
    st.markdown('<br>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div class='ciel-card'>
            <h3 style='color: #38bdf8; margin-top:0; font-size: 1.3rem;'>🎯 Méthode de Travail Optimale</h3>
            <p style='color: #cbd5e1; font-size: 0.98rem; line-height: 1.6;'>Cette plateforme a été restructurée en <b>4 Hubs Thématiques</b> pour correspondre aux exigences strictes des jurys d'examen :</p>
            <ul style='color: #cbd5e1; line-height: 1.8;'>
                <li><b style='color: #ffffff;'>📖 Référentiel par Matière</b> : Cours rangés par discipline (Maths, Réseaux, Cyber, Dev C++, Linux AD, Élec, CGE, Anglais) avec <b>10 questions d'application directe</b> à chaque fin de chapitre.</li>
                <li><b style='color: #ffffff;'>🧪 Laboratoire Pratique</b> : Entraînez-vous à saisir de véritables commandes sous Cisco IOS, Bash Debian, C++ Debugger, PowerShell Active Directory et bus IoT.</li>
                <li><b style='color: #ffffff;'>🎯 Entraînement & Examens</b> : 105 Flashcards actives, Annales réelles 2024-2026 décortiquées et Grand Quiz de 70 questions.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='ciel-card' style='border-left: 4px solid #34d399;'>
            <h4 style='color: #34d399; margin-top:0; font-size: 1.15rem;'>📋 Épreuves Certifiantes :</h4>
            <p style='color: #cbd5e1; margin-bottom: 12px;'><b style='color: #ffffff;'>• E4 : Étude & Conception (Coeff 4)</b><br>
            <span style='color: #94a3b8; font-size: 0.88rem;'>6h d'épreuve : 4h30 Info/Réseaux (70 pts) + 1h30 Physique (30 pts)</span></p>
            <p style='color: #cbd5e1; margin-bottom: 12px;'><b style='color: #ffffff;'>• E5 : Intervention & Maintenance (Coeff 3)</b><br>
            <span style='color: #94a3b8; font-size: 0.88rem;'>Configurations réelles Cisco, Linux, pfSense, Wireshark</span></p>
            <p style='color: #cbd5e1; margin-bottom: 0;'><b style='color: #ffffff;'>• E6 : Projet Professionnel (Coeff 7)</b><br>
            <span style='color: #94a3b8; font-size: 0.88rem;'>Soutenance orale 1h, Cahier des charges, UML/SysML & PVL Pytest</span></p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <div style='margin-top: 30px; margin-bottom: 20px;'>
        <h3 style='color: #38bdf8; font-weight: 800; font-size: 1.4rem; margin-bottom: 6px;'>🗺️ Carte d'Accès Rapide aux 4 Hubs du Studio</h3>
        <p style='color: #94a3b8; font-size: 0.95rem;'>Chaque espace est accessible via le menu latéral gauche :</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown("""
        <div class='ciel-card' style='border-top: 3px solid #38bdf8; min-height: 140px;'>
            <h4 style='color: #38bdf8; margin-top: 0;'>🏠 1. Mon Tableau de Bord & Profil</h4>
            <p style='color: #94a3b8; font-size: 0.9rem;'>Pilotez vos révisions personnalisées : métriques, plan de remédiation ciblée, planning 6 semaines et profil utilisateur avec gain d'XP.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='ciel-card' style='border-top: 3px solid #34d399; min-height: 140px;'>
            <h4 style='color: #34d399; margin-top: 0;'>🧪 2. Le Laboratoire Pratique</h4>
            <p style='color: #94a3b8; font-size: 0.9rem;'>Manipulez des simulateurs avancés : 5 consoles réelles (Cisco, Linux, C++, AD, IoT), décodeur Wireshark, calculateurs VLSM et tests Pytest E6.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("""
        <div class='ciel-card' style='border-top: 3px solid #818cf8; min-height: 140px;'>
            <h4 style='color: #818cf8; margin-top: 0;'>📖 3. Référentiel Rangé par Matière</h4>
            <p style='color: #94a3b8; font-size: 0.9rem;'>Tous vos cours structurés rigoureusement par discipline académique (Maths, Réseaux, Cyber, Dev C++, Linux AD, Élec, Anglais, CGE) avec 10 questions certifiantes par cours.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='ciel-card' style='border-top: 3px solid #fb923c; min-height: 140px;'>
            <h4 style='color: #fb923c; margin-top: 0;'>🎯 4. Entraînement & Examens</h4>
            <p style='color: #94a3b8; font-size: 0.9rem;'>Entraînement réflexe : 105 flashcards interactives 3D, annales officielles 2024-2026 décortiquées et grand quiz de 70 questions avec correction active.</p>
        </div>
        """, unsafe_allow_html=True)

elif page == '📊 Mathématiques : Suites Arithmétiques & Géométriques':
    st.markdown("<div class='hero-title'>📊 Mathématiques Appliquées : Suites & Dérivées</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Cours complet, formules explicites, méthode de la dérivée, simulateurs interactifs et exercices de programmation Python</p>", unsafe_allow_html=True)
    tab_m1, tab_m2, tab_m3, tab_m4 = st.tabs(['📖 Cours & Formules Clés', '🧮 Calculatrice & Simulateur de Suites', '🐍 Traduction Algorithmique Python', '✍️ Exercices Pratiques & Quiz'])
    with tab_m1:
        st.subheader('1. Synthèse Comparative : Arithmétique vs Géométrique')
        st.markdown("\n        La distinction entre ces deux modèles est la base de toute modélisation en réseaux et systèmes (allocation mémoire, incrémentation d'adresses, atténuation de signal, saturation de bande passante).")
        st.markdown("\n        | Propriété | Suite Arithmétique | Suite Géométrique |\n        | :--- | :--- | :--- |\n        | **Mécanisme** | On **ajoute** une raison constante $r$. | On **multiplie** par une raison constante $q$. |\n        | **Récurrence** | $u_{n+1} = u_n + r$ | $u_{n+1} = u_n \\times q$ |\n        | **Formule explicite (depuis $u_0$)** | $u_n = u_0 + n \\cdot r$ | $u_n = u_0 \\times q^n$ |\n        | **Formule explicite (depuis $u_p$)** | $u_n = u_p + (n - p) \\cdot r$ | $u_n = u_p \\times q^{n-p}$ |\n        | **Somme des $N$ premiers termes** | $S = N \\times \\frac{u_{\\text{premier}} + u_{\\text{dernier}}}{2}$ | $S = u_{\\text{premier}} \\times \\frac{1 - q^{\\text{Nb\\\\_termes}}}{1 - q} \\quad (q \\neq 1)$ |\n        | **Variations** | Si $r > 0$ : Croissante<br>Si $r < 0$ : Décroissante | Si $u_0 > 0$ et $q > 1$ : Croissante<br>Si $u_0 > 0$ et $0 < q < 1$ : Décroissante |\n        | **Application BTS CIEL** | Incrémentation d'adresses IP, boucles simples. | Atténuation d'un signal optique/Wi-Fi (ex: perte de $15\\\\% \\Rightarrow q = 0,85$). |")
        st.markdown('---')
        st.subheader("2. Comportement à l'Infini (Limites de $u_n = u_0 \\times q^n$ pour $u_0 > 0$)")
        c_lim1, c_lim2, c_lim3 = st.columns(3)
        with c_lim1:
            st.info('**Si $q > 1$** : $\\lim_{n \\to +\\infty} u_n = +\\infty$\\n\\nLa suite diverge vers $+\\infty$ (saturation réseau, explosion mémoire).')
        with c_lim2:
            st.success("**Si $0 < q < 1$** : $\\lim_{n \\to +\\infty} u_n = 0$\\n\\nLa suite converge vers $0$ (atténuation totale d'un signal).")
        with c_lim3:
            st.warning('**Si $q = 1$** : $u_n = u_0$ (constante)\\n\\n**Si $q \\le -1$** : Pas de limite (oscillation chaotique).')
        st.markdown('---')
        st.subheader('3. Étude des Variations : La Méthode de la Dérivée')
        st.markdown("\n        Lorsqu'une suite est définie par une formule explicite complexe $u_n = f(n)$, on utilise la dérivation continue sur $\\mathbb{R}^+$ pour déterminer son sens de variation :\n        1. **Fonction associée** : Remplacer l'entier $n$ par la variable réelle $x$ pour poser $f(x)$ sur $[0 ; +\\infty[$.\n        2. **Dérivation** : Calculer $f'(x)$ en utilisant les formules usuelles (souvent $\\frac{u}{v} \\Rightarrow f'(x) = \\frac{u'v - uv'}{v^2}$).\n        3. **Signe** : Étudier le signe du numérateur et du dénominateur (attention : un carré $v^2$ est toujours strictement positif).\n        4. **Conclusion** : Dresser le tableau de variation de $f$, puis déduire le sens de variation de la suite $(u_n)$.")
    with tab_m2:
        st.subheader('🧮 Calculateur Dynamique de Suites')
        col_m_type, col_m_u0, col_m_reason, col_m_n = st.columns(4)
        with col_m_type:
            st_type = st.selectbox('Type de suite :', ['Arithmétique', 'Géométrique'])
        with col_m_u0:
            st_u0 = st.number_input('Premier terme $u_0$ :', value=100.0)
        with col_m_reason:
            st_r = st.number_input('Raison ($r$ ou $q$) :', value=0.85 if st_type == 'Géométrique' else 5.0)
        with col_m_n:
            st_n = st.number_input('Rang $n$ à calculer :', min_value=0, max_value=100, value=10)
        if st_type == 'Arithmétique':
            un_val = st_u0 + st_n * st_r
            sum_val = (st_n + 1) * (st_u0 + un_val) / 2.0
            formula_txt = f'u_{{{int(st_n)}}} = {st_u0} + {int(st_n)} \\times {st_r} = {un_val:.2f}'
        else:
            un_val = st_u0 * st_r ** st_n
            if st_r != 1.0:
                sum_val = st_u0 * (1 - st_r ** (st_n + 1)) / (1 - st_r)
            else:
                sum_val = st_u0 * (st_n + 1)
            formula_txt = f'u_{{{int(st_n)}}} = {st_u0} \\times {st_r}^{{{int(st_n)}}} = {un_val:.4f}'
        res_c1, res_c2 = st.columns(2)
        with res_c1:
            st.metric(f'Terme $u_{{{int(st_n)}}}$', f'{un_val:.4f}')
            st.latex(formula_txt)
        with res_c2:
            st.metric(f'Somme $S_{{{int(st_n)}}} = \\sum_{{k=0}}^{{{int(st_n)}}} u_k$', f'{sum_val:.4f}')
        st.markdown("#### Graphique de l'évolution des termes $u_0$ à $u_n$")
        n_values = list(range(int(st_n) + 1))
        if st_type == 'Arithmétique':
            u_values = [st_u0 + k * st_r for k in n_values]
        else:
            u_values = [st_u0 * st_r ** k for k in n_values]
        df_suite = pd.DataFrame({'Rang n': n_values, 'Valeur u_n': u_values}).set_index('Rang n')
        st.line_chart(df_suite)
        st.markdown('---')
        st.subheader('📡 Application Pratique : Atténuation de Signal Optique / Wi-Fi')
        st.info("Chaque mètre de fibre optique ou d'obstacle réduit la puissance du signal d'un pourcentage fixe. Modélisons la puissance restante.")
        p_init = st.number_input('Puissance initiale $P_0$ (en mW) :', value=100.0)
        p_loss = st.number_input('Perte par mètre (%) :', value=15.0)
        p_seuil = st.number_input('Seuil minimal de réception $P_{\\text{seuil}}$ (en mW) :', value=10.0)
        q_loss = 1.0 - p_loss / 100.0
        m_count = 0
        p_curr = p_init
        while p_curr >= p_seuil and m_count < 200:
            p_curr *= q_loss
            m_count += 1
        st.success(f'⚡ **Résultat de portée** : Le signal passe sous le seuil critique de **{p_seuil} mW** au bout de **{m_count} mètres** (Puissance au mètre {m_count} : **{p_curr:.2f} mW**).')
    with tab_m3:
        st.subheader("🐍 Traduction Algorithmique en Python (Sujets d'Examen)")
        st.write("À l'examen écrit de BTS CIEL, on vous demande fréquemment d'écrire ou de compléter des fonctions Python modélisant des suites.")
        col_py1, col_py2 = st.columns(2)
        with col_py1:
            st.markdown('#### Cas n°1 : Calculer une valeur précise (Boucle `FOR`)')
            st.code('\n# Calcul du terme de rang n pour une suite géométrique\n# Exemple : u_{n+1} = u_n * 0.85 (perte de 15%), u_0 = 100\ndef calculer_signal(n):\n    u = 100.0               # Initialisation (u_0)\n    for i in range(n):      # Répète n fois\n        u = u * 0.85        # Relation de récurrence\n    return u\n\n# Appel\nprint(calculer_signal(10))  # Affiche u_10', language='python')
        with col_py2:
            st.markdown('#### Cas n°2 : Atteindre un seuil critique (Boucle `WHILE`)')
            st.code("\n# Chercher la distance n où le signal passe sous 10 mW\ndef trouver_perte_signal(seuil=10.0):\n    u = 100.0               # Initialisation (u_0)\n    n = 0                   # Compteur de rang\n    while u >= seuil:       # CONDITION D'ARRÊT INVERSÉE\n        u = u * 0.85\n        n = n + 1           # Passage au rang suivant\n    return n                # Renvoie le rang où u < seuil\n\n# Appel\nprint(trouver_perte_signal()) # Affiche la distance n", language='python')
        st.markdown('---')
        st.subheader('✍️ Exercice Interactif de Complètement Python')
        st.write("Complétez la fonction Python ci-dessous pour calculer la somme des $N$ premiers termes d'une suite arithmétique $u_{n+1} = u_n + 3$ avec $u_0 = 10$ :")
        st.code('\ndef somme_suite_arithmetique(N):\n    u = 10\n    somme = 0\n    for i in range(N + 1):\n        somme += u\n        u = # LIGNE À COMPLÉTER\n    return somme', language='python')
        user_py_in = st.text_input("Saisissez l'instruction exacte de mise à jour de `u` :", placeholder='u + 3', key='py_math_complete')
        if st.button('Valider la fonction Python', key='btn_val_py_math'):
            clean_in = user_py_in.strip().replace(' ', '')
            if clean_in in ['u+3', 'u+=3', 'u=u+3']:
                st.success('🎉 **Code exact !** La récurrence arithmétique ajoute la raison $r = 3$ à chaque itération.')
            else:
                st.error('❌ Instruction incorrecte. Pour une suite arithmétique de raison $r=3$, la mise à jour est `u = u + 3` (ou `u += 3`).')
    with tab_m4:
        st.subheader("✍️ Exercices d'Examen Corrigés & Quiz Mathématiques")
        with st.expander("📝 Exercice 1 : Rédaction complète de l'étude de variation d'une suite (Explicite)", expanded=True):
            st.markdown("\n            **Énoncé** : Soit la suite $(u_n)$ définie pour tout entier $n \\ge 0$ par $u_n = \\frac{4n + 2}{n + 3}$. Étudier le sens de variation de la suite $(u_n)$.\n\n            **Rédaction type recommandée pour le BTS Blanc** :\n            1. Soit $f$ la fonction définie sur $[0 ; +\\infty[$ par $f(x) = \\frac{4x + 2}{x + 3}$. On a $u_n = f(n)$.\n            2. Calculons la dérivée $f'(x)$ avec la formule $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$ :\n               - $u(x) = 4x + 2 \\Rightarrow u'(x) = 4$\n               - $v(x) = x + 3 \\Rightarrow v'(x) = 1$\n               - $f'(x) = \\frac{4(x + 3) - (4x + 2) \\times 1}{(x + 3)^2} = \\frac{4x + 12 - 4x - 2}{(x + 3)^2} = \\mathbf{\\frac{10}{(x + 3)^2}}$\n            3. Étude du signe :\n               - Le numérateur $10 > 0$.\n               - Le dénominateur $(x + 3)^2 > 0$ (carré d'un réel strictement positif pour $x \\ge 0$).\n               - Donc $f'(x) > 0$ sur $[0 ; +\\infty[$.\n            4. Conclusion : La fonction $f$ est strictement croissante sur $[0 ; +\\infty[$. On en déduit que la suite $(u_n)$ est **strictement croissante**.")
        st.markdown('---')
        st.subheader('⚡ Mini-Quiz Mathématiques : Testez vos connaissances')
        q_m1 = st.radio('Q1 : Une fibre optique subit une perte de 5% de sa puissance par kilomètre. Quelle est la raison $q$ de la suite géométrique associée ?', ['q = 0.05', 'q = 0.95', 'q = 1.05', 'q = -0.05'], key='qm1')
        if st.button('Valider Q1', key='btn_qm1'):
            if q_m1 == 'q = 0.95':
                st.success('✅ **Exact !** Une diminution de 5% correspond au coefficient multiplicateur $q = 1 - \\frac{5}{100} = 0,95$.')
            else:
                st.error('❌ Mauvaise réponse. Réduction de 5% = $1 - 0,05 = 0,95$.')
        q_m2 = st.radio('Q2 : Quelle est la somme des 10 premiers termes ($u_0$ à $u_9$) de la suite arithmétique de premier terme $u_0 = 5$ et de raison $r = 2$ ?', ['S = 140', 'S = 130', 'S = 100', 'S = 150'], key='qm2')
        if st.button('Valider Q2', key='btn_qm2'):
            if q_m2 == 'S = 140':
                st.success('✅ **Exact !** $u_9 = 5 + 9 \\times 2 = 23$. La somme de $u_0$ à $u_9$ (10 termes) vaut $10 \\times \\frac{5 + 23}{2} = 140$.')
            else:
                st.error('❌ Incorrect. $u_9 = 23$. $S_{10} = 10 \\times \\frac{5 + 23}{2} = 140$.')


    st.markdown("---")
    st.subheader("✍️ Grand Test d'Entraînement : 10 Questions Officielles sur les Suites")
    st.markdown("<p style='color:#94a3b8;'>Testez votre maîtrise sur l'ensemble des notions de ce chapitre. Vos points sont automatiquement comptabilisés dans votre profil utilisateur !</p>", unsafe_allow_html=True)
    
    score_suites = 0
    for idx_s, q_s in enumerate(QUIZZES_BANK_10["Suites"]):
        st.markdown(f"**{q_s['q']}**")
        rep_s = st.radio(f"Votre choix (Q{idx_s + 1}) :", q_s["opts"], key=f"rad_suites_10_{idx_s}")
        if rep_s == q_s["rep"]:
            score_suites += 1
            
    if st.button("Valider le Test des 10 Questions (Suites)", type="primary", key="btn_val_suites_10"):
        add_user_points(score_suites * 10, "quiz_suites_10")
        if score_suites >= 8:
            st.success(f"🏆 **Excellente performance : {score_suites} / 10 !** Vous avez remporté {score_suites * 10} points d'expérience !")
            st.balloons()
        elif score_suites >= 5:
            st.info(f"👍 **Bon travail : {score_suites} / 10.** Gain : +{score_suites * 10} points. Révisez les questions signalées ci-dessus.")
        else:
            st.warning(f"⚠️ **Résultat : {score_suites} / 10.** Gain : +{score_suites * 10} points. Relisez attentivement la fiche de cours.")


elif page == '🛠️ Fiches Réussite Épreuve E5 (TP & Pratique)':
    st.markdown("<div class='hero-title'>🛠️ Fiches Réussite Épreuve E5 : TP & Pratiques de Terrain</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Guide complet, procédures pas-à-pas et fiches réflexes d'intervention pour réussir haut la main l'épreuve pratique E5 (Réseaux, SysAdmin, Cybersécurité & Électronique)</p>", unsafe_allow_html=True)
    tab_e5_1, tab_e5_2, tab_e5_3, tab_e5_4, tab_e5_5, tab_e5_6, tab_e5_7, tab_e5_8 = st.tabs(['📶 E5-01 : Cisco IOS (Switch & Routeur)', '🖥️ E5-02 : Linux Debian & SysAdmin', '🏢 E5-03 : Active Directory, DNS, DHCP & GPO', '🛡️ E5-04 : Pare-Feu pfSense, DMZ & Flux', '🔍 E5-05 : Wireshark & Trames', '⚡ E5-06 : Électronique & Bus', '📋 E5-07 : Check-List Diagnostic E5', '✍️ Auto-Évaluation Pratique E5'])
    with tab_e5_1:
        st.subheader('📶 Fiche E5-01 : Commutateurs & Routeurs Cisco (Configuration & Dépannage)')
        st.markdown("\n        <div class='ciel-card' style='border-left: 6px solid #2563eb !important;'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Cisco :</h4>\n            <p style='color:#334155; margin-bottom:0;'>Être capable d'initialiser, sécuriser, segmentez en VLANs (802.1Q), configurer le routage inter-VLAN et appliquer le Port Security sur les équipements Cisco de l'atelier.</p>\n        </div>\n        ", unsafe_allow_html=True)
        with st.expander('1️⃣ Configuration Initiale & Sécurisation de Base (Switch/Routeur)', expanded=True):
            st.markdown("\n            ```cisco\n            enable\n            configure terminal\n            hostname SW-L2-CIEL\n            enable secret CiscoPass123!\n            \n            ! Sécurisation de l'accès Console\n            line console 0\n              password ConsolePass!\n              login\n              logging synchronous\n              exit\n              \n            ! Sécurisation des lignes VTY (SSH / Telnet)\n            line vty 0 15\n              password VtyPass!\n              login\n              transport input ssh\n              exit\n              \n            ! Chiffrement des mots de passe en clair dans le fichier de config\n            service password-encryption\n            \n            ! Bannière d'avertissement légal\n            banner motd # ACCES RESTREINT - BTS CIEL E5 - UTILISATEURS AUTORISES SEULEMENT #\n            ```\n            ")
        with st.expander("2️⃣ Configuration des VLANs & Assignation des Ports d'Accès", expanded=False):
            st.markdown("\n            ```cisco\n            ! 1. Création des VLANs dans la base de données\n            vlan 10\n              name RESEAU_ADMIN\n            vlan 20\n              name RESEAU_PROD\n            vlan 30\n              name DMZ_SERVEURS\n            vlan 99\n              name GESTION_NATIVE\n            exit\n            \n            ! 2. Assignation d'une plage de ports au VLAN 10 (Mode Access)\n            interface range FastEthernet 0/1 - 10\n              switchport mode access\n              switchport access vlan 10\n              spanning-tree portfast          ! Active l'accès immédiat sans délai STP\n              no shutdown\n            ```\n            ")
        with st.expander('3️⃣ Configuration de la Liaison Agrégée Trunking (IEEE 802.1Q)', expanded=False):
            st.markdown('\n            ```cisco\n            interface GigabitEthernet 0/1\n              switchport trunk encapsulation dot1q    ! Obligatoire sur switchs L3\n              switchport mode trunk\n              switchport trunk allowed vlan 10,20,30,99\n              switchport trunk native vlan 99         ! Sécurisation du VLAN natif\n              no shutdown\n            ```\n            ')
        with st.expander('4️⃣ Routage Inter-VLAN (Router-on-a-Stick sur Routeur)', expanded=False):
            st.markdown("\n            ```cisco\n            ! Sur le Routeur R1 (Relier g0/0 au port Trunk du Switch)\n            interface GigabitEthernet 0/0\n              no shutdown                             ! Activer l'interface physique\n              \n            ! Subinterface pour le VLAN 10\n            interface GigabitEthernet 0/0.10\n              encapsulation dot1Q 10\n              ip address 192.168.10.254 255.255.255.0\n              \n            ! Subinterface pour le VLAN 20\n            interface GigabitEthernet 0/0.20\n              encapsulation dot1Q 20\n              ip address 192.168.20.254 255.255.255.0\n            ```\n            ")
        with st.expander('5️⃣ Sécurité des Ports (Port Security)', expanded=False):
            st.markdown('\n            ```cisco\n            interface FastEthernet 0/5\n              switchport mode access\n              switchport access vlan 10\n              switchport port-security\n              switchport port-security maximum 2              ! Max 2 adresses MAC autorisées\n              switchport port-security mac-address sticky     ! Apprend automatiquement la MAC\n              switchport port-security violation shutdown    ! Met le port en err-disable si intrusion\n            ```\n            ')
        with st.expander('🔍 Commandes de Diagnostic & Vérification E5 (Boîte à Outils)', expanded=False):
            st.markdown("\n            | Commande Cisco IOS | Objectif de Vérification E5 |\n            | :--- | :--- |\n            | `show vlan brief` | Vérifier que tous les VLANs existent et que les bons ports sont attribués. |\n            | `show interfaces trunk` | Vérifier que le lien Trunk est actif, en 802.1Q, et que les VLANs passent. |\n            | `show ip interface brief` | Vérifier l'état physique (`Status`) et logique (`Protocol`) des interfaces (`up/up`). |\n            | `show ip route` | Inspecter la table de routage IP du routeur ou switch L3. |\n            | `show port-security interface f0/5` | Vérifier si un port est bloqué suite à une violation d'adresse MAC (`err-disabled`). |\n            | `show running-config` | Consulter la configuration active en mémoire vive (RAM). |\n            ")
    with tab_e5_2:
        st.subheader('🖥️ Fiche E5-02 : Linux Debian Server & Administration Système')
        st.markdown("\n        <div class='ciel-card' style='border-left: 6px solid #10b981 !important;'>\n            <h4 style='color:#065f46; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Linux :</h4>\n            <p style='color:#334155; margin-bottom:0;'>Savoir configurer le réseau fixe, gérer les utilisateurs/groupes, appliquer les permissions fines (`chmod`, SUID, SGID, Sticky, ACLs), éditer `sudoers`, écrire des scripts Bash et gérer les services systemd.</p>\n        </div>\n        ", unsafe_allow_html=True)
        with st.expander('1️⃣ Configuration Réseau Fixe (`/etc/network/interfaces`)', expanded=True):
            st.markdown("\n            ```bash\n            # Éditer le fichier de configuration réseau\n            nano /etc/network/interfaces\n\n            # Configuration statique de l'interface eth0\n            auto eth0\n            iface eth0 inet static\n                address 192.168.1.100/24\n                gateway 192.168.1.254\n                dns-nameservers 192.168.1.200 8.8.8.8\n\n            # Appliquer les modifications\n            systemctl restart networking\n            # Ou avec la commande ip :\n            ip addr add 192.168.1.100/24 dev eth0\n            ip route add default via 192.168.1.254\n            ```\n            ")
        with st.expander('2️⃣ Gestion des Utilisateurs, Groupes & Privilèges Sudo', expanded=False):
            st.markdown('\n            ```bash\n            # 1. Création d\'un groupe d\'ingénieurs\n            groupadd -g 2000 tech_ciel\n\n            # 2. Création d\'un utilisateur avec son répertoire personnel /home/antoine\n            useradd -m -u 1500 -g tech_ciel -s /bin/bash antoine\n            passwd antoine\n\n            # 3. Ajout au groupe sudo pour les privilèges d\'administration\n            usermod -aG sudo antoine\n\n            # 4. Configuration fine de Sudoers (/etc/sudoers.d/ciel)\n            echo "antoine ALL=(ALL:ALL) ALL" > /etc/sudoers.d/ciel\n            # Autorisateurs sans mot de passe pour un service spécifique :\n            echo "%tech_ciel ALL=(ALL) NOPASSWD: /bin/systemctl restart apache2" >> /etc/sudoers.d/ciel\n            chmod 0440 /etc/sudoers.d/ciel\n            ```\n            ')
        with st.expander('3️⃣ Permissions Octales, Droits Spéciaux & ACLs POSIX', expanded=False):
            st.markdown("\n            * **Permissions Classiques (`chmod`)** :\n              - `chmod 750 /opt/deploy.sh` $\\rightarrow$ Owner: `rwx` (7), Group: `r-x` (5), Others: `---` (0).\n            * **Droits Spéciaux** :\n              - **SUID (4000)** : `chmod 4755 /usr/bin/mon_prog` (S'exécute avec les privilèges du propriétaire `root`).\n              - **SGID (2000)** : `chmod 2770 /data/partage` (Les nouveaux fichiers héritent du groupe du dossier).\n              - **Sticky Bit (1000)** : `chmod 1777 /tmp` (Seul le propriétaire d'un fichier peut le supprimer dans un dossier public).\n            * **ACLs POSIX (`setfacl` & `getfacl`)** :\n              - Accorder les droits `rwx` à l'utilisateur `alice` : `setfacl -m u:alice:rwx /var/www/html`\n              - Accorder `r-x` au groupe `tech_ciel` : `setfacl -m g:tech_ciel:rx /var/www/html`\n              - Consulter les ACLs : `getfacl /var/www/html`\n              - Supprimer les ACLs : `setfacl -b /var/www/html`\n            ")
        with st.expander("4️⃣ Modèle de Script Bash d'Examen E5", expanded=False):
            st.markdown('\n            ```bash\n            #!/bin/bash\n            # Script d\'automatisation E5 : Vérification des services et sauvegarde\n            LOGFILE="/var/log/e5_check.log"\n            BACKUP_DIR="/var/backups/ciel"\n\n            mkdir -p $BACKUP_DIR\n            echo "=== Diagnostic E5 - $(date) ===" > $LOGFILE\n\n            # Boucle de vérification des services\n            for srv in networking apache2 ssh; do\n                if systemctl is-active --quiet $srv; then\n                    echo "[OK] Service $srv est opérationnel." >> $LOGFILE\n                else\n                    echo "[ALERTE] Service $srv est ARRÊTÉ. Tentative de relance..." >> $LOGFILE\n                    systemctl restart $srv\n                fi\n            done\n\n            # Compression du dossier Web\n            tar -czf "$BACKUP_DIR/web_$(date +%Y%m%d).tar.gz" /var/www/html 2>> $LOGFILE\n            echo "Sauvegarde terminée." >> $LOGFILE\n            ```\n            ')
        with st.expander('🔍 Commandes de Diagnostic Linux E5', expanded=False):
            st.markdown("\n            | Commande Linux | Rôle Diagnostic E5 |\n            | :--- | :--- |\n            | `ip a` / `ip route` | Vérifier les adresses IP configurées et la passerelle par défaut. |\n            | `ss -tulpn` / `netstat -an` | Lister tous les ports TCP/UDP en écoute et leurs PID. |\n            | `systemctl status <service>` | Inspecter l'état d'un service (active, dead, failed). |\n            | `journalctl -u <service> -n 30` | Consulter les 30 dernières lignes de journal systemd d'un service. |\n            | `tail -f /var/log/auth.log` | Suivre en temps réel les tentatives de connexion et d'authentification. |\n            | `df -h` / `free -m` | Vérifier l'occupation de l'espace disque et la mémoire RAM disponible. |\n            ")
    with tab_e5_3:
        st.subheader('🏢 Fiche E5-03 : Active Directory, DNS, DHCP & GPO (Windows Server)')
        st.markdown("\n        <div class='ciel-card' style='border-left: 6px solid #8b5cf6 !important;'>\n            <h4 style='color:#6d28d9; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Active Directory :</h4>\n            <p style='color:#334155; margin-bottom:0;'>Maîtriser la gestion de domaine ADDS, la création d'OU, d'utilisateurs/groupes, le déploiement de GPO (LSDOU), et les services d'infrastructure DNS / DHCP.</p>\n        </div>\n        ", unsafe_allow_html=True)
        with st.expander("1️⃣ Arborescence ADDS & Commandes PowerShell d'Administration", expanded=True):
            st.markdown('\n            ```powershell\n            # 1. Créer la structure d\'Unités d\'Organisation (OU)\n            New-ADOrganizationalUnit -Name "Direction" -Path "DC=ciel,DC=local"\n            New-ADOrganizationalUnit -Name "Ingénieurs" -Path "DC=ciel,DC=local"\n            New-ADOrganizationalUnit -Name "Techniciens" -Path "DC=ciel,DC=local"\n\n            # 2. Créer un utilisateur dans une OU\n            New-ADUser -Name "Alice Martin" `\n                       -GivenName "Alice" `\n                       -Surname "Martin" `\n                       -UserPrincipalName "amartin@ciel.local" `\n                       -SamAccountName "amartin" `\n                       -Path "OU=Ingénieurs,DC=ciel,DC=local" `\n                       -AccountPassword (Read-Host -AsSecureString "Password123!") `\n                       -Enabled $true `\n                       -ChangePasswordAtLogon $false\n\n            # 3. Créer un groupe de sécurité et ajouter le membre\n            New-ADGroup -Name "G_Ingenieurs" -GroupScope Global -GroupCategory Security `\n                        -Path "OU=Ingénieurs,DC=ciel,DC=local"\n            Add-ADGroupMember -Identity "G_Ingenieurs" -Members "amartin"\n            ```\n            ')
        with st.expander("2️⃣ Stratégies de Groupe (GPO) & Ordre d'Application LSDOU", expanded=False):
            st.markdown("\n            * **Ordre d'application LSDOU** :\n              1. **L**ocal (Stratégie locale de la machine)\n              2. **S**ite (Site Active Directory)\n              3. **D**omaine (`ciel.local`)\n              4. **OU** (Unité d'Organisation spécifique)\n              *Règle d'or* : La stratégie la plus proche de l'objet (OU) prévaut sur la stratégie parente (Domaine).\n            * **Cas d'usage E5 fréquents** :\n              - Mappage automatique de lecteur réseau (`G:` $\\rightarrow$ `\\\\SRV-FILE\\PartageData`).\n              - Restriction du Panneau de Configuration et de l'invite de commande CMD.\n              - Déploiement d'un fond d'écran d'entreprise obligatoire.\n            * **Commandes de rafraîchissement & diagnostic GPO** :\n              - `gpupdate /force` (Sur le poste client)\n              - `gpresult /r` ou `rsop.msc` (Consulter le jeu de stratégies résultant).\n            ")
        with st.expander('3️⃣ Service DNS (Zones de Recherche Directe & Inverse)', expanded=False):
            st.markdown("\n            * **Zone de Recherche Directe** (`ciel.local`) :\n              - Enregistrement `A` : `srv-web.ciel.local` $\\rightarrow$ `192.168.1.50`\n              - Enregistrement `AAAA` : IPv6 de l'hôte.\n              - Enregistrement `CNAME` (Alias) : `www.ciel.local` $\\rightarrow$ `srv-web.ciel.local`\n              - Enregistrement `MX` : Serveur de messagerie du domaine.\n            * **Zone de Recherche Inverse** (`1.168.192.in-addr.arpa`) :\n              - Enregistrement `PTR` : `192.168.1.50` $\\rightarrow$ `srv-web.ciel.local` (Indispensable pour Kerberos et Active Directory !).\n            ")
        with st.expander('4️⃣ Service DHCP (Étendues, Options & Baux)', expanded=False):
            st.markdown("\n            * **Configuration d'Étendue (Scope)** :\n              - Plage IP : `192.168.1.100` à `192.168.1.200` / Masque `/24`.\n              - Dépassement / Exclusions : `192.168.1.1` à `192.168.1.20` (Réservées aux équipements fixes).\n            * **Options DHCP Clés en E5** :\n              - Option `003` : Router (Passerelle par défaut = `192.168.1.254`).\n              - Option `006` : DNS Servers (IP du Contrôleur de Domaine = `192.168.1.200`).\n              - Option `015` : DNS Domain Name (`ciel.local`).\n            * **Réservation DHCP** : Association permanente d'une adresse IP fixe à une adresse MAC d'imprimante ou de caméra IP.\n            ")
        with st.expander('🔍 Commandes Diagnostic Active Directory / Windows Server', expanded=False):
            st.markdown("\n            | Commande PowerShell / CMD | Rôle Diagnostic E5 |\n            | :--- | :--- |\n            | `dcdiag` | Diagnostic complet de santé du Contrôleur de Domaine Active Directory. |\n            | `nslookup srv-web.ciel.local` | Tester la résolution de nom DNS directe et inverse. |\n            | `Test-NetConnection -ComputerName srv-ad -Port 389` | Tester l'ouverture du port LDAP (389) ou LDAPS (636). |\n            | `nltest /dsgetdc:ciel.local` | Vérifier quel contrôleur de domaine a authentifié la machine. |\n            | `ipconfig /all` & `ipconfig /flushdns` | Afficher la config IP et vider le cache DNS client. |\n            ")
    with tab_e5_4:
        st.subheader('🛡️ Fiche E5-04 : Pare-Feu pfSense, DMZ & Matrice des Flux')
        st.markdown("\n        <div class='ciel-card' style='border-left: 6px solid #ef4444 !important;'>\n            <h4 style='color:#b91c1c; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur pfSense :</h4>\n            <p style='color:#334155; margin-bottom:0;'>Configurer les zones WAN, LAN et DMZ, appliquer la règle d'isolation stricte DMZ $\\rightarrow$ LAN, mettre en place les règles de filtrage et le NAT/PAT Port Forwarding.</p>\n        </div>\n        ", unsafe_allow_html=True)
        with st.expander('1️⃣ Architecture Réseau à 3 Interfaces & Adressage', expanded=True):
            st.markdown("\n            * **WAN (Wide Area Network)** : Interface d'accès externe (`10.0.0.2/24` ou IP Publique).\n            * **LAN (Local Area Network)** : Zone réseau interne sécurisée (`192.168.1.254/24`).\n            * **DMZ (Demilitarized Zone)** : Zone réseau isolée hébergeant les services ouverts à l'extérieur (`172.16.0.254/24`).\n            ")
        with st.expander("2️⃣ Règle d'Or d'Isolation de la DMZ (Inviolable)", expanded=False):
            st.markdown("\n            <div class='ciel-card' style='background:#fef2f2 !important; border-left: 5px solid #dc2626 !important;'>\n                <b style='color:#991b1b;'>⚠️ Règle de Sécurité Numéro 1 en E5 :</b><br>\n                Une machine située en <b>DMZ ne doit JAMAIS pouvoir initier de connexion vers le réseau LAN interne</b>.<br>\n                Si le serveur Web DMZ est compromis par un pirate, celui-ci ne pourra pas attaquer les postes du réseau LAN.\n            </div>\n            ", unsafe_allow_html=True)
        with st.expander('3️⃣ Matrice des Ports & Flux Réseaux de Référence (À Apprendre par Cœur)', expanded=False):
            st.markdown("\n            | Service | Protocole | Port | Sens Recommandé | Rôle & Explication |\n            | :--- | :--- | :--- | :--- | :--- |\n            | **DNS** | UDP / TCP | `53` | LAN -> DMZ / WAN | Résolution de noms de domaine. |\n            | **HTTP / HTTPS** | TCP | `80` / `443` | WAN -> DMZ (NAT) | Accès aux serveurs Web publics. |\n            | **SSH** | TCP | `22` | LAN -> DMZ | Administration à distance sécurisée. |\n            | **LDAP / LDAPS** | TCP | `389` / `636` | LAN -> DC | Annuaire d'entreprise ADDS. |\n            | **Kerberos AD** | TCP / UDP | `88` | LAN -> DC | Jetons d'authentification AD. |\n            | **SMB / CIFS** | TCP | `445` | LAN -> FileSRV | Partage de fichiers Windows. |\n            | **MQTTS** | TCP | `8883` | DMZ -> IoT Broker | Transport IoT chiffré TLS. |\n            ")
        with st.expander('4️⃣ Procédure de Configuration NAT / PAT (Port Forwarding pfSense)', expanded=False):
            st.markdown('\n            1. Aller dans **Firewall $\\rightarrow$ NAT $\\rightarrow$ Port Forward**.\n            2. Cliquer sur **Add (Top)** :\n               - **Interface** : `WAN`\n               - **Protocol** : `TCP`\n               - **Destination** : `WAN Address`\n               - **Destination Port Range** : `HTTP (80)`\n               - **Redirect Target IP** : `172.16.0.10` (IP du serveur Web DMZ)\n               - **Redirect Target Port** : `HTTP (80)`\n               - **Filter Rule Association** : `Pass` (Génère la règle de pare-feu automatiquement)\n            3. Cliquer sur **Save** puis **Apply Changes**.\n            ')
    with tab_e5_5:
        st.subheader('🔍 Fiche E5-05 : Wireshark & Diagnostics de Trames Réseaux')
        st.markdown("\n        <div class='ciel-card' style='border-left: 6px solid #0284c7 !important;'>\n            <h4 style='color:#0369a1; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur Wireshark :</h4>\n            <p style='color:#334155; margin-bottom:0;'>Capturer, filtrer et décoder des paquets réseaux pour identifier un dysfonctionnement, réconcilier une connexion TCP ou analyser un protocole applicatif.</p>\n        </div>\n        ", unsafe_allow_html=True)
        with st.expander("1️⃣ Filtres d'Affichage Wireshark Essentiels pour l'Examen", expanded=True):
            st.markdown('\n            | Filtre d\'Affichage Wireshark | Rôle Diagnostic E5 |\n            | :--- | :--- |\n            | `ip.addr == 192.168.1.50` | Filtrer tout le trafic concernant une adresse IP spécifique. |\n            | `tcp.port == 443` | Isoler le trafic Web sécurisé HTTPS. |\n            | `tcp.flags.syn == 1 and tcp.flags.ack == 0` | Identifier les demandes de connexion TCP (Handshake SYN). |\n            | `dns.qname contains "ciel"` | Filtrer les requêtes DNS portant sur le domaine d\'examen. |\n            | `dhcp.option.dhcp == 3` | Filtrer les paquets DHCP Request lors d\'un bail d\'adresse. |\n            | `arp.opcode == 2` | Filtrer les réponses ARP (Utile pour détecter un ARP Spoofing). |\n            | `http.request.method == "POST"` | Inspecter les envois de formulaires et identifiants en clair. |\n            ')
        with st.expander("2️⃣ Méthodologie d'Analyse d'une Séquence TCP 3-Way Handshake", expanded=False):
            st.markdown("\n            ```\n            Client (192.168.1.10)                        Serveur (192.168.1.50:80)\n                   |                                                 |\n                   |------- [SYN] Seq=0 ----------------------------->|  (Étape 1 : Demande)\n                   |<------ [SYN, ACK] Seq=0 Ack=1 ------------------|  (Étape 2 : Accord)\n                   |------- [ACK] Seq=1 Ack=1 ---------------------->|  (Étape 3 : Validation)\n                   |                                                 |\n            ```\n            * **Anomalie d'examen** : Si le serveur répond par `[RST, ACK]`, le port est fermé ou rejeté par un pare-feu !\n            ")
        with st.expander("3️⃣ Fonctionnalité 'Follow TCP Stream' & Export d'Objets", expanded=False):
            st.markdown("\n            * **Follow TCP Stream** : Clic droit sur un paquet TCP $\\rightarrow$ *Follow $\\rightarrow$ TCP Stream*. Permet de reconstituer l'intégralité du dialogue applicatif (HTTP, SMTP, FTP, Modbus) en texte clair.\n            * **Exportation d'Objets HTTP** : Menu *File $\\rightarrow$ Export Objects $\\rightarrow$ HTTP*. Permet d'extraire un fichier (image, PDF, binaire) téléchargé pendant la capture.\n            ")
    with tab_e5_6:
        st.subheader('⚡ Fiche E5-06 : Électronique, Oscilloscope & Bus Industriels')
        st.markdown("\n        <div class='ciel-card' style='border-left: 6px solid #eab308 !important;'>\n            <h4 style='color:#a16207; margin-top:0;'>🎯 Objectifs de l'Épreuve E5 sur l'Atelier Électronique :</h4>\n            <p style='color:#334155; margin-bottom:0;'>Régler les calibres de l'oscilloscope, effectuer des mesures de tension/période/fréquence, calculer des quantums CAN, et contrôler le signal sur les bus I2C, SPI, CAN ou Modbus.</p>\n        </div>\n        ", unsafe_allow_html=True)
        with st.expander("1️⃣ Mesures Physiques à l'Oscilloscope Numérique", expanded=True):
            st.markdown('\n            * **Tension Crête-à-Crête $V_{pp}$** : $V_{pp} = N_{\\text{div\\_vert}} \\times S_v$\n            * **Tension Maximale $V_{max}$** : $V_{max} = \\frac{V_{pp}}{2}$\n            * **Tension Efficace $V_{\\text{eff}}$** : $V_{\\text{eff}} = \\frac{V_{max}}{\\sqrt{2}} \\approx 0,707 \\times V_{max}$ (Signal sinusoïdal)\n            * **Période $T$** : $T = N_{\\text{div\\_horiz}} \\times S_h$\n            * **Fréquence $f$** : $f = \\frac{1}{T}$\n            * **Déphasage $\\Delta \\phi$** : $\\Delta \\phi = 360^\\circ \\times \\frac{\\Delta t}{T}$\n            ')
        with st.expander('2️⃣ Convertisseurs CAN / CNA (ADC / DAC)', expanded=False):
            st.markdown('\n            * **Quantum $q$** : $q = \\frac{V_{\\text{ref}}}{2^n - 1}$\n              - *Exemple CAN 12 bits sous 5,0V* : $q = \\frac{5,0}{4095} \\approx 1,221\\text{ mV}$.\n            * **Valeur Numérique Entière $N$** : $N = \\text{arrondi}\\left(\\frac{V_e}{q}\\right)$\n              - *Exemple pour $V_e = 2,5\\text{ V}$* : $N = \\text{arrondi}\\left(\\frac{2,5}{0,001221}\\right) = 2048$.\n            ')
        with st.expander('3️⃣ Synthèse des Bus Industriels de Terrain (Atelier E5)', expanded=False):
            st.markdown('\n            | Bus de Terrain | Lignes Physiques | Type de Signal | Spécificités & Points de Contrôle E5 |\n            | :--- | :--- | :--- | :--- |\n            | **I2C** | 2 fils (`SDA`, `SCL`) | Synchrone | Résistances de tirage Pull-Up ($4,7\\text{ k}\\Omega$). Adressage 7 bits. |\n            | **SPI** | 4 fils (`MOSI`, `MISO`, `SCLK`, `CS`) | Synchrone Full-Duplex | Liaison maître-esclave très rapide (plusieurs MHz). |\n            | **Bus CAN** | 2 fils (`CAN_H`, `CAN_L`) | Différentiel | Résistances de terminaison de $120\\ \\Omega$. Bit dominant 0 / récessif 1. |\n            | **Modbus RTU** | 2 fils (`A`, `B` / RS-485) | Différentiel Asynchrone | Code Fonction `03` (Read Holding Registers), contrôle CRC-16. |\n            ')
    with tab_e5_7:
        st.subheader("📋 Fiche E5-07 : Check-List Diagnostic & Grille d'Intervention E5")
        st.markdown("\n        <div class='ciel-card' style='border-top: 5px solid #2563eb !important;'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>🧭 Guide Méthodologique de Résolution de Panne en 5 Étapes :</h4>\n            <p style='color:#334155;'>Suivez rigoureusement ce protocole lors de vos évaluations pratiques E5 pour ne négliger aucun point du barème :</p>\n            \n            ```\n            [Étape 1 : Vérification Couche 1 Physique]\n              └── Câble RJ45 / Fibre correctement encliqueté ? Voyants Link/Act allumés ? Équipement alimenté ?\n            \n            [Étape 2 : Vérification Couche 2 Liaison]\n              └── Adresse MAC détectée ? Port du switch dans le bon VLAN ? (`show vlan brief` / `ip link`)\n            \n            [Étape 3 : Vérification Couche 3 Réseau]\n              └── IP, Masque et Passerelle configurés ? PING passerelle OK ? PING DNS OK ? (`ping 192.168.1.254`)\n            \n            [Étape 4 : Vérification Couche 4/7 Transport & Application]\n              └── Port ouvert sur la cible ? Service démarré ? (`ss -tulpn` / `nc -zvw3 IP PORT` / `curl -Iv`)\n            \n            [Étape 5 : Documentation & Compte-Rendu d'Intervention]\n              └── Rédiger la fiche de synthèse d'examen avec les symptômes, la cause racine et la solution appliquée.\n            ```\n        </div>\n        ", unsafe_allow_html=True)
    with tab_e5_8:
        st.subheader('✍️ Auto-Évaluation Pratique E5 (QCM de Validation)')
        st.markdown("Testez vos réflexes d'intervention pratique avant de passer devant les examinateurs :")
        q_e5_list = [{'q': "1. Sur un commutateur Cisco, quelle commande permet d'associer le port f0/5 au VLAN 20 en mode accès ?", 'opts': ['switchport access vlan 20', 'vlan 20 enable', 'ip route vlan 20', 'trunk access vlan 20'], 'rep': 'switchport access vlan 20', 'expl': "La commande correcte est 'switchport access vlan 20' sous l'interface f0/5."}, {'q': '2. Sous Linux Debian, quel masque octal chmod accorde rwx au propriétaire, r-x au groupe et aucun droit aux autres ?', 'opts': ['755', '750', '644', '777'], 'rep': '750', 'expl': "rwx = 7, r-x = 5, --- = 0, d'où 750."}, {'q': '3. Dans pfSense, quelle est la règle de filtrage absolue concernant les initiations de connexions depuis la DMZ ?', 'opts': ['La DMZ peut tout initier vers le LAN', 'La DMZ ne doit JAMAIS initier de connexion vers le LAN', 'La DMZ est isolée du WAN', 'La DMZ utilise le port 80 uniquement'], 'rep': 'La DMZ ne doit JAMAIS initier de connexion vers le LAN', 'expl': 'Pour préserver le LAN, toute initiation de connexion depuis la DMZ vers le LAN est strictement bloquée.'}, {'q': "4. Dans Wireshark, quel filtre d'affichage permet d'isoler uniquement les requêtes Web chiffrées HTTPS ?", 'opts': ['ip.port == 80', 'tcp.port == 443', 'http.flags == syn', 'ssl.mode == pass'], 'rep': 'tcp.port == 443', 'expl': 'HTTPS utilise le port TCP 443.'}, {'q': "5. Quelle est la valeur de la résistance de terminaison requise aux deux extrémités d'un bus CAN ?", 'opts': ['50 Ohms', '75 Ohms', '120 Ohms', '1000 Ohms'], 'rep': '120 Ohms', 'expl': "Deux résistances de 120 Ohms permettent d'adapter l'impédance de la ligne et d'éviter les réflexions de signal."}]
        score_e5 = 0
        for idx_e5, qe5 in enumerate(q_e5_list):
            st.markdown(f'**{qe5["q"]}**')
            ans_e5 = st.radio(f'Choix Q{idx_e5 + 1} E5 :', qe5["opts"], key=f'q_e5_tab_{idx_e5}')
            if ans_e5 == qe5['rep']:
                score_e5 += 1
        if st.button('Soumettre mon évaluation E5', type='primary', key='btn_submit_e5_page'):
            st.session_state['score_e5_eval'] = score_e5
            st.success(f"🏆 **Score obtenu sur l'Épreuve E5** : **{score_e5} / {len(q_e5_list)}** ({score_e5 / len(q_e5_list) * 100:.1f}%)")
            if score_e5 == len(q_e5_list):
                st.balloons()



elif page == '📄 Fiches Savoir & Fiches Montage':
    st.markdown("<div class='hero-title'>📄 Recueil Officiel des Fiches Savoir & Fiches Montage</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Guide complet, exhaustif et verbatim de toutes les Fiches Savoir (N°1 à N°12), Fiche Physique et Fiches Montage (N°1 & N°2) du BTS CIEL (Option A)</p>", unsafe_allow_html=True)
    tab_fs1, tab_fs2, tab_fs3, tab_fs4, tab_fs5 = st.tabs(['⚡ Fiches Savoir Électronique (1 à 4 & Physique)', '💻 Fiches Savoir Informatique (5 à 8)', '📶 Fiches Savoir Réseaux & Com (9 à 12)', '🛠️ Fiches Montage (N°1 & N°2)', '✍️ Auto-Évaluation Fiches Savoir'])
    with tab_fs1:
        st.subheader('⚡ Fiches Savoir : Électronique, Puissance & Signaux')
        with st.expander('📄 FICHE SAVOIR N°1 : Le Pont en H (Contrôle de Moteur CC)', expanded=True):
            st.markdown("\n            **Rôle Fonctionnel** : Contrôler le sens de rotation d'un moteur à courant continu (CC / bipolaire) en inversant la polarité d'alimentation à ses bornes.\n\n            #### Schéma de Principe & Table d'États :\n            ```\n                +Vcc (Alimentation Puissance)\n                 |\n            +----+----+\n            |         |\n          [Int1]    [Int3]\n            |         |\n            +--[M]----+  <-- Moteur CC\n            |         |\n          [Int2]    [Int4]\n            |         |\n            +----+----+\n                 |\n                GND\n            ```\n            | Interrupteurs Fermés | Interrupteurs Ouverts | Sens de Rotation Moteur |\n            | :--- | :--- | :--- |\n            | **Inter 1 & Inter 4** | Inter 2 & Inter 3 | Sens Anti-Horaire (Sens 1) |\n            | **Inter 2 & Inter 3** | Inter 1 & Inter 4 | Sens Horaire (Sens 2) |\n            | *Tous ouverts* | Tous fermés | Arrêt / Roue libre |\n\n            ⚠️ **Règle d'or de sécurité matérielle** : Inter 1 et Inter 2 (ou Inter 3 et Inter 4) ne doivent **jamais** être fermés simultanément sous peine de provoquer un **court-circuit direct** de l'alimentation (*Shooting Through* / destruction immédiate du pont).\n\n            #### Composant Industriel Type : Module Double Pont en H BTS7960 43A\n            - **Pins de contrôle** : `R_EN` / `L_EN` (Enable sens droit/gauche), `R_PWM` / `L_PWM` (Commandes de vitesse PWM), `R_IS` / `L_IS` (Mesure de courant).\n            ```cpp\n            // Programme Arduino de test BTS7960\n            int R_IS = 6, R_EN = 2, R_PWM = 3;\n            int L_IS = 7, L_EN = 4, L_PWM = 5;\n\n            void setup() {\n              pinMode(R_IS, OUTPUT); pinMode(R_EN, OUTPUT); pinMode(R_PWM, OUTPUT);\n              pinMode(L_IS, OUTPUT); pinMode(L_EN, OUTPUT); pinMode(L_PWM, OUTPUT);\n              digitalWrite(R_IS, LOW); digitalWrite(L_IS, LOW);\n              digitalWrite(R_EN, HIGH); digitalWrite(L_EN, HIGH); // Activation des deux demi-ponts\n            }\n\n            void loop() {\n              int i;\n              for (i = 0; i <= 255; i += 10) { // Acceleration sens horaire\n                analogWrite(R_PWM, i); analogWrite(L_PWM, 0); delay(500);\n              }\n              delay(500);\n              for (i = 0; i <= 255; i += 10) { // Acceleration sens anti-horaire\n                analogWrite(R_PWM, 0); analogWrite(L_PWM, i); delay(500);\n              }\n              delay(500);\n            }\n            ```")
        with st.expander("📄 FICHE SAVOIR N°1 (Physique) : Lois Fondamentales de l'Électricité", expanded=False):
            st.markdown("\n            #### 1. Loi d'Ohm & Conventions\n            - **Loi d'Ohm en Convention Récepteur** : $U_{AB} = R \\cdot I$. La flèche de tension $U$ est orientée en sens opposé à la flèche d'intensité $I$.\n            - **Conductance** : Inverse de la résistance, notée $G = \\frac{1}{R}$ en Siemens ($S$). La loi d'Ohm devient $I = G \\cdot U_{AB}$.\n\n            #### 2. Lois de Kirchhoff\n            - **Loi des Nœuds (Conservation de la charge)** : La somme des courants entrants dans un nœud est égale à la somme des courants sortants :\n              $$\\sum I_{\\text{entrants}} = \\sum I_{\\text{sortants}} \\quad \\Longleftrightarrow \\quad \\sum \\pm I_k = 0$$\n            - **Loi des Mailles (Conservation de l'énergie)** : La somme algébrique des tensions le long d'une maille fermée orientée est nulle :\n              $$\\sum U_k = 0$$\n\n            #### 3. Associations de Résistances\n            - **Série** : $R_{\\text{eq}} = R_1 + R_2 + \\dots + R_n$. $\\frac{1}{G_{\\text{eq}}} = \\frac{1}{G_1} + \\frac{1}{G_2}$.\n            - **Parallèle** : $\\frac{1}{R_{\\text{eq}}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\dots + \\frac{1}{R_n}$. Pour 2 résistances : $R_{\\text{eq}} = \\frac{R_1 \\cdot R_2}{R_1 + R_2}$. $G_{\\text{eq}} = G_1 + G_2$.\n\n            #### 4. Ponts Diviseurs de Tension & Courant\n            - **Pont Diviseur de Tension** : Pour 2 résistances en série alimentées sous $E$ :\n              $$U_2 = E \\cdot \\frac{R_2}{R_1 + R_2}$$\n              Formule d'isolation de $R_2$ : $R_2 = \\frac{U_2 \\cdot R_1}{E - U_2}$.\n            - **Pont Diviseur de Courant** : Pour 2 résistances en parallèle traversées par un courant $I$ :\n              $$I_1 = I \\cdot \\frac{R_2}{R_1 + R_2} = I \\cdot \\frac{G_1}{G_1 + G_2}$$\n\n            #### 5. Puissance & Énergie\n            - **Puissance électrique** : $P = U \\cdot I = R \\cdot I^2 = \\frac{U^2}{R}$ (en Watts $W$ ou $J/s$).\n            - **Énergie électrique** : $E = P \\cdot \\Delta t$ (en Joules $J$ ou $Wh$).\n            - **Générateur Réel** : Tension $U = E - r \\cdot I$. Puissance disponible $P = E \\cdot I - r \\cdot I^2$ ($E \\cdot I$ est la puissance électromotrice totale, $r \\cdot I^2$ est la perte Joule interne).\n            - **Capacité de Batterie** : $C = I \\cdot \\Delta t$ en Ampères-heures ($Ah$) ou $A \\cdot s$ ($Coulombs$).")
        with st.expander('📄 FICHE SAVOIR N°2 : Résistances de Pull-Up et Pull-Down', expanded=False):
            st.markdown("\n            #### Contexte & Problématique Haute Impédance :\n            Les entrées numériques des microcontrôleurs (CMOS, ATmega328P, ESP32) possèdent une très grande impédance d'entrée (de 100 MΩ à 1 GΩ) due à la présence de la grille isolée du transistor MOS d'entrée.\n            Lorsqu'une broche n'est reliée ni au Vcc ni au GND, elle se trouve dans un **état flottant (haute impédance / *floating*)**.\n            Elle se comporte alors comme une antenne sensible aux parasites électromagnétiques environnants, provoquant des états logiques alatoires imprévisibles.\n\n            #### 1. Montage Pull-Up (Rappel au Vcc) :\n            - **Câblage** : Une résistance de $10\\text{ k}\\Omega$ est branchée entre la broche et le $+5\\text{V}$. Le bouton-poussoir est entre la broche et le $GND$.\n            - **Repos (Bouton relâché)** : Entrée tirée au $+5\\text{V}$ $\\Rightarrow$ **HIGH (1)**.\n            - **Actif (Bouton appuyé)** : Entrée reliée au $GND$ $\\Rightarrow$ **LOW (0)**.\n\n            #### 2. Montage Pull-Down (Rappel à la Masse) :\n            - **Câblage** : Une résistance de $10\\text{ k}\\Omega$ est branchée entre la broche et le $GND$. Le bouton est entre la broche et le $+5\\text{V}$.\n            - **Repos (Bouton relâché)** : Entrée tirée au $GND$ $\\Rightarrow$ **LOW (0)**.\n            - **Actif (Bouton appuyé)** : Entrée reliée au $+5\\text{V}$ $\\Rightarrow$ **HIGH (1)**.\n\n            #### 3. Pull-Up Interne Arduino :\n            L'ATmega328P possède des résistances de Pull-Up internes intégrées (20 kΩ à 50 kΩ) activables en C++ :\n            ```cpp\n            pinMode(pin, INPUT_PULLUP); // Active la résistance de rappel interne au Vcc\n            ```\n            *Note* : En `INPUT_PULLUP`, la logique est inversée (un appui sur bouton relié au GND renvoie `LOW`).")
        with st.expander("📄 FICHE SAVOIR N°3 : La PWM (Modulation de Largeur d'Impulsion)", expanded=False):
            st.markdown("\n            #### Principe Fonctionnel :\n            La PWM (Pulse Width Modulation / MLI) permet de simuler une tension ou puissance analogique variable en utilisant exclusivement des signaux numériques Tout-Ou-Rien (0V ou 5V).\n            La tension créneau varie entre 0V et 5V, et on ajuste le **rapport cyclique** $\\alpha$ (pourcentage du temps passé au niveau HAUT sur une période $T$) :\n            $$\\alpha = \\frac{t_{\\text{haut}}}{T} \\quad \\Big(0 \\le \\alpha \\le 1 \\quad \\text{ou} \\quad 0\\% \\le \\alpha \\le 100\\%\\Big)$$\n\n            #### Formule de la Tension Moyenne :\n            $$V_{\\text{moy}} = \\alpha \\cdot V_{\\text{max}} = V_{\\text{max}} \\cdot \\left(\\frac{\\text{valeur\\_8bits}}{255}\\right)$$\n            *Exemple* : Pour `analogWrite(pin, 127)` sous 5V $\\Rightarrow \\alpha \\approx 50\\% \\Rightarrow V_{\\text{moy}} = 2.5\\text{ V}$.\n\n            #### Broches PWM de l'Arduino Uno (ATmega328P) :\n            | Broches PWM | Timer Associé | Fréquence Fréquentielle |\n            | :--- | :--- | :--- |\n            | **Pins 5 et 6** | Timer 0 (8 bits) | **~980 Hz** |\n            | **Pins 3, 9, 10, 11** | Timer 1 (16 bits) / Timer 2 (8 bits) | **~490 Hz** |\n\n            #### Application C++ : Variation progressive de luminosité d'une LED\n            ```cpp\n            int led = 9; // Broche PWM à 490 Hz\n\n            void setup() {\n              pinMode(led, OUTPUT);\n            }\n\n            void loop() {\n              for (int i = 0; i <= 255; i++) {\n                analogWrite(led, i); // Rapport cyclique de 0% à 100%\n                delay(10);\n              }\n            }\n            ```")
        with st.expander('📄 FICHE SAVOIR N°4 : Interruptions Matérielles & Registres AVR', expanded=False):
            st.markdown("\n            #### Principe d'une Interruption Matérielle :\n            Une interruption matérielle envoie un signal au processeur pour interrompre immédiatement le programme principal (`loop()`) et exécuter une routine spécifique appelée **ISR** (*Interrupt Service Routine*).\n            À la fin de l'ISR, le microcontrôleur restaure son contexte et reprend le programme à l'endroit exact de l'interruption.\n\n            #### Vecteurs d'Interruption & Registres de Ports ATmega328P :\n            - **PORTB** : Pins D8 à D13 (Registre de direction `DDRB`)\n            - **PORTC** : Pins A0 à A5 (Registre de direction `DDRC`)\n            - **PORTD** : Pins D0 à D7 (Registre de direction `DDRD`)\n\n            #### Décalage de Bit & Registres DDRx :\n            Un bit à `1` dans `DDRx` configure la broche associée en **Sortie**. Un bit à `0` configure en **Entrée**.\n            - Passage de D3 (INT1) en sortie : `DDRD |= (1 << PD3);` (ou `1 << INT1`).\n            - Passage de D3 en entrée : `DDRD &= ~(1 << PD3);` (équivaut à `pinMode(3, INPUT)`).\n\n            #### Attachement d'une ISR en C++ :\n            ```cpp\n            volatile bool état = false;\n\n            void toggleISR() { // Routine ISR ultra-courte (pas de delay, pas de Serial)\n              état = !état;\n            }\n\n            void setup() {\n              pinMode(2, INPUT_PULLUP);\n              // Attache l'interruption INT0 sur la pin D2 lors d'un front descendant\n              attachInterrupt(digitalPinToInterrupt(2), toggleISR, FALLING);\n            }\n\n            void loop() {\n              // Code principal non bloquant\n            }\n            ```")
    with tab_fs2:
        st.subheader('💻 Fiches Savoir : Informatique, Mémoire & Composants')
        with st.expander("📄 FICHE SAVOIR N°5 : Organisation des Mémoires (Flash, SRAM & EEPROM) de l'Arduino UNO R3", expanded=True):
            st.markdown('\n            L\'ATmega328P repose sur une architecture Harvard (bus d\'instructions et bus de données séparés) découpée en 3 mémoires distinces :\n\n            #### 1. Mémoire Flash (32 Ko) :\n            - **Type** : Mémoire non-volatile (programme conservé hors tension).\n            - **Usage** : Stocke le **Bootloader** (0.5 Ko en haute mémoire) et le **code exécutable C++ (.hex)**.\n            - **Optimisation** : Utiliser la directive `PROGMEM` ou le macro `F("mon texte")` pour stocker les chaînes constantes en Flash sans encombrer la SRAM.\n\n            #### 2. Mémoire SRAM (2 Ko = 2048 Octets) :\n            - **Type** : Mémoire vive volatile (effacée à l\'extinction).\n            - **Cartographie interne** :\n              - **Variables globales et statiques** (.data et .bss) en bas de mémoire.\n              - **Le Tas (Heap)** : Allocation dynamique (`malloc`, `new`). S\'étend vers le bas.\n              - **La Pile (Stack)** : Variables locales, arguments de fonctions, adresses de retour. S\'étend vers le haut.\n              ⚠️ **Collision Heap / Stack** : Si la Pile et le Tas se croisent (saturation SRAM < 2048 octets), le programme plante de façon imprévisible.\n\n            #### 3. Mémoire EEPROM (1 Ko = 1024 Octets) :\n            - **Type** : Mémoire non-volatile électriquement effaçable (100 000 cycles d\'écriture).\n            - **Usage** : Sauvegarde permanente de paramètres de configuration (seuils, adresses IP/Modbus, compteurs).\n            - **Bibliothèque C++** : `#include <EEPROM.h>` (`EEPROM.read(addr)`, `EEPROM.write(addr, val)`, `EEPROM.update(addr, val)`).')
        with st.expander('📄 FICHE SAVOIR N°6 : Le Signal 4-20 mA Industriel', expanded=False):
            st.markdown("\n            #### Rôle & Définition :\n            Standard analogique universel pour boucles d'instrumentation industrielle.\n            La grandeur physique (pression, température, débit) est traduite linéairement en une intensité variant de **4 mA (minimum / zéro de mesure)** à **20 mA (maximum / pleine échelle)**.\n\n            #### Formule Mathématique de Conversion Linéaire :\n            $$I(T) = I_{\\text{min}} + \\frac{T - T_{\\text{min}}}{T_{\\text{max}} - T_{\\text{min}}} \\cdot (I_{\\text{max}} - I_{\\text{min}}) = 4 + \\frac{T - T_{\\text{min}}}{T_{\\text{max}} - T_{\\text{min}}} \\cdot 16\\text{ mA}$$\n            *Exemple* : Pour un capteur de température de $-15^\\circ\\text{C}$ ($4\\text{ mA}$) à $+150^\\circ\\text{C}$ ($20\\text{ mA}$) :\n            - Pour $T = -15^\\circ\\text{C}$ : $I = 4 + \\frac{0}{165} \\cdot 16 = \\mathbf{4\\text{ mA}}$.\n            - Pour $T = +67.5^\\circ\\text{C}$ : $I = 4 + \\frac{82.5}{165} \\cdot 16 = \\mathbf{12\\text{ mA}}$.\n            - Pour $T = +150^\\circ\\text{C}$ : $I = 4 + \\frac{165}{165} \\cdot 16 = \\mathbf{20\\text{ mA}}$.\n\n            #### Avantages du 4-20 mA ('Live Zero') :\n            1. **Détection automatique de rupture de câble** : Si $I = 0\\text{ mA}$ (inférieur à 3.8 mA), le système sait qu'il y a une coupure de fil ou une défaillance du capteur.\n            2. **Auto-alimentation 2 fils** : Les 4 mA permanents permettent d'alimenter l'électronique du transmetteur.\n            3. **Immunité aux parasites & aux chutes de tension** : L'intensité reste constante quelle que soit la longueur du câble (jusqu'à 1000 mètres).\n\n            #### Conversion Courant $\nightarrow$ Tension pour Microcontrôleur :\n            On insère une résistance de précision $R = 250\\ \\Omega$ (0.1%) dans la boucle :\n            - À $4\\text{ mA}$ : $V = 250\\ \\Omega \\cdot 0.004\\text{ A} = \\mathbf{1.0\\text{ V}}$.\n            - À $20\\text{ mA}$ : $V = 250\\ \\Omega \\cdot 0.020\\text{ A} = \\mathbf{5.0\\text{ V}}$.\n            La tension $1.0\\text{V} - 5.0\\text{V}$ est directement lue par l'ADC de l'Arduino.")
        with st.expander('📄 FICHE SAVOIR N°7 : Résolution et Précision des Capteurs', expanded=False):
            st.markdown("\n            #### 1. La Résolution :\n            C'est le plus petit changement de la grandeur physique qu'un capteur ou un système de mesure peut détecter ou afficher.\n            - *Exemple* :\n              - Affichage $45\\%$, $46\\%$, $47\\%$ $\\Rightarrow$ **Résolution = $1\\%$**.\n              - Affichage $45.0\\%$, $45.1\\%$, $45.2\\%$ $\\Rightarrow$ **Résolution = $0.1\\%$**.\n            - **Résolution numérisée d'un CAN $n$ bits** :\n              $$q = \\text{Quantum} = \\frac{\\text{Étendue de Mesure (EM)}}{2^n - 1}$$\n\n            #### 2. La Précision (Incertitude de mesure) :\n            C'est l'écart maximal entre la valeur mesurée par le capteur et la valeur réelle (vraie) de la grandeur.\n            - *Exemple* : Pour une humidité réelle de $50\\%$, si le capteur indique $52\\% \\pm 0.5\\%$, l'erreur de précision est de $+2\\%$.\n\n            #### 3. Justesse vs Fidélité :\n            - **Justesse** : Absence d'erreur systématique (moyenne des mesures centrée sur la valeur vraie).\n            - **Fidélité (Répétabilité)** : Rapprochement des mesures entre elles (absence d'erreur aléatoire).\n            - **Précision** = Justesse + Fidélité.\n            ⚠️ *Piège d'examen* : Un capteur avec une résolution de 4 décimales peut être totalement imprécis s'il n'est pas étalonné !")
        with st.expander('📄 FICHE SAVOIR N°8 : Les Relais (Électromécaniques & Statiques)', expanded=False):
            st.markdown('\n            #### Rôle & Définition :\n            Un relais est un interrupteur commandé électriquement. Il permet à un circuit de commande basse tension (Arduino 5V / 20mA) d\'isoler et de commuter un circuit de puissance (230V AC / 10A, moteurs, pompes).\n\n            #### Types de Relais :\n            1. **Relais Électromécanique (EMR)** :\n               - Fonctionne avec une bobine électromagnétique et des contacts mécaniques.\n               - Émet un "clic" sonore à la commutation.\n               - Nécessite une **diode de roue libre** en anti-parallèle sur la bobine pour absorber la surtension d\'auto-induction ($e = -L \\frac{di}{dt}$).\n            2. **Relais Statique (SSR)** :\n               - Basé sur des semi-conducteurs (Optocoupleur + Triac / MOSFET).\n               - Silencieux, vitesse de commutation ultra-rapide, durée de vie illimitée.\n\n            #### Connectique d\'un Module Relais :\n            - **Côté Commande (Basse Tension)** : `VCC` (+5V), `GND` (Masse), `IN` (Signal Arduino).\n            - **Côté Puissance (Haute Tension)** :\n              - `COM` (Common) : Borne d\'entrée du courant de puissance.\n              - `NO` (Normally Open) : Contact Normalement Ouvert au repos (fermé quand `IN` est actif).\n              - `NC` (Normally Closed) : Contact Normalement Fermé au repos (ouvert quand `IN` est actif).')
    with tab_fs3:
        st.subheader('📶 Fiches Savoir : Réseaux, Communications & C++')
        with st.expander('📄 FICHE SAVOIR N°9 : Rapidité de Modulation (Bauds) vs Débit Binaire (bps)', expanded=True):
            st.markdown("\n            #### 1. Débit Binaire $D$ (bits/s ou bps) :\n            Quantité d'information binaire utile transmise par unité de temps :\n            $$D = \\frac{n}{\\Delta t} \\quad (\\text{en bps})$$\n\n            #### 2. Rapidité de Modulation $R$ (Bauds) :\n            Nombre de changements d'état du signal physique (symboles ou valences) transmis par seconde sur la ligne :\n            $$R = \\frac{1}{T_s} \\quad (\\text{en Bauds, où } T_s \\text{ est la durée d'un symbole})$$\n\n            #### 3. Relation Générale de Nyquist-Hartley :\n            Si chaque symbole code $m$ bits (soit $M = 2^m$ valences possibles) :\n            $$D = R \\cdot m = R \\cdot \\log_2(M)$$\n\n            | Type de Signal / Modulation | Valences ($M$) | Bits par symbole ($m$) | Relation Débit / Bauds |\n            | :--- | :--- | :--- | :--- |\n            | **Binaire RS232 / UART** | $M = 2$ | $m = 1\\text{ bit}$ | **$D = R$** (bps = Bauds) |\n            | **Modulation 4-PSK / QPSK** | $M = 4$ | $m = 2\\text{ bits}$ | **$D = 2 \\cdot R$** |\n            | **Modulation 16-QAM** | $M = 16$ | $m = 4\\text{ bits}$ | **$D = 4 \\cdot R$** (Ex: 2400 Bauds $\\Rightarrow$ 9600 bps) |\n            | **Modulation 256-QAM** | $M = 256$ | $m = 8\\text{ bits}$ | **$D = 8 \\cdot R$** |")
        with st.expander('📄 FICHE SAVOIR N°10 : Contrôle de Flux (XON/XOFF & Matériel RTS/CTS)', expanded=False):
            st.markdown("\n            #### Rôle du Contrôle de Flux :\n            Éviter le débordement de tampon (*Buffer Overflow*) de réception lorsqu'un récepteur lent est saturé par un émetteur rapide.\n\n            #### 1. Contrôle de Flux Logiciel (In-Band) : XON / XOFF\n            - Utilise les 2 lignes de données série existantes (`Tx` et `Rx`).\n            - **XOFF (ASCII `0x13` / DC3)** : Envoyé par le récepteur dès que son tampon atteint un seuil haut (ex. 80%). L'émetteur suspend la transmission.\n            - **XON (ASCII `0x11` / DC1)** : Envoyé dès que le tampon repasse sous un seuil bas (ex. 20%). L'émetteur reprend l'envoi.\n            - *Limite* : Incompatible avec le transfert de fichiers binaires bruts si le fichier contient lui-même les octets `0x11` ou `0x13`.\n\n            #### 2. Contrôle de Flux Matériel (Out-of-Band) : RTS / CTS & DTR / DSR\n            - Utilise des lignes physiques dédiées sur le câble RS232 :\n            - **RTS / CTS (Request To Send / Clear To Send)** :\n              - `RTS` : Positionné par l'émetteur pour demander à émettre.\n              - `CTS` : Validé par le récepteur quand son tampon est disponible.\n            - **DTR / DSR (Data Terminal Ready / Data Set Ready)** : Indiquent la présence et l'état sous-tension des équipements.")
        with st.expander('📄 FICHE SAVOIR N°11 : Le Routage IP', expanded=False):
            st.markdown("\n            #### Principe du Routage (Couche 3 OSI) :\n            Fonction assurée par les routeurs pour acheminer les paquets IP depuis un réseau source vers un réseau destination à travers des réseaux d'interconnexion.\n\n            #### Structure d'une Table de Routage :\n            Chaque entrée contient :\n            1. **Réseau Destination & Masque CIDR** (ex: `192.168.20.0/24`).\n            2. **Passerelle / Next Hop** (IP du routeur suivant).\n            3. **Interface de sortie** (ex: `g0/0/1`).\n            4. **Distance Administrative (DA) & Métrique** (coût du chemin).\n\n            #### Types de Routes :\n            - **Directement connectées** (DA = 0).\n            - **Statiques** : Configurer manuellement (`ip route 192.168.20.0 255.255.255.0 10.0.0.2`).\n            - **Route par Défaut** : `0.0.0.0 0.0.0.0 <Next_Hop>` (achemine le trafic inconnu vers le Web).\n            - **Dynamiques** : Calculées automatiquement par des protocoles de routage (**OSPF** à état de lien).")
        with st.expander('📄 FICHE SAVOIR N°12 : Commande de LED Objet en C++', expanded=False):
            st.markdown("\n            #### Encapsulation Orientée Objet C++ :\n            Création d'une classe `Led` encapsulant la broche matérielle et les méthodes d'action (`allumer`, `eteindre`, `basculer`).\n\n            ```cpp\n            #include <Arduino.h>\n\n            class Led {\n            private:\n              int broche; // Attribut privé\n            public:\n              // Constructeur : configuration automatique du pinMode\n              Led(int pin) {\n                broche = pin;\n                pinMode(broche, OUTPUT);\n              }\n\n              void allumer() {\n                digitalWrite(broche, HIGH);\n              }\n\n              void eteindre() {\n                digitalWrite(broche, LOW);\n              }\n\n              void basculer() {\n                digitalWrite(broche, !digitalRead(broche));\n              }\n            };\n\n            // Instanciation de l'objet maLed sur la broche 13\n            Led maLed(13);\n\n            void setup() {\n              // Le constructeur a configuré la broche 13 en sortie\n            }\n\n            void loop() {\n              maLed.allumer();\n              delay(1000);\n              maLed.eteindre();\n              delay(1000);\n\n              // Inversion directe d'état\n              maLed.basculer();\n              delay(1000);\n            }\n            ```")
    with tab_fs4:
        st.subheader('🛠️ Fiches Montage : Expérimentations Pratiques & Codes C++')
        with st.expander('📄 FICHE MONTAGE N°1 : Contrôle de Vérins Électriques (Relais & Driver BTS7960)', expanded=True):
            st.markdown('\n            #### Objectif :\n            Piloter un ou plusieurs vérins électriques à moteur CC 12V/24V. Le courant absorbé en charge nécessite un module de puissance dimensionné (driver MOSFET ou carte relais).\n\n            #### Montage 1 : Module Relais ECO-WORTHY\n            - **SÉCURITÉ MATÉRIELLE AU DÉMARRAGE** : Utiliser une fonction `safeInitPin()` pour forcer l\'état inactif du relais *avant* d\'initialiser le `pinMode(OUTPUT)`, évitant tout mouvement incontrôlé du vérin au boot.\n\n            ```cpp\n            const int pinM = 2;\n            const int pinN = 3;\n            const bool relayActiveLow = false; // true si le relais s\'active sur LOW\n\n            int outActiveValue()   { return relayActiveLow ? LOW  : HIGH; }\n            int outInactiveValue() { return relayActiveLow ? HIGH : LOW;  }\n\n            void safeInitPin(int pin) {\n              digitalWrite(pin, outInactiveValue()); // Positionner l\'état inactif désiré\n              pinMode(pin, OUTPUT);\n            }\n\n            void setup() {\n              safeInitPin(pinM);\n              safeInitPin(pinN);\n              delay(200); // Laissez les relais se stabiliser\n              Serial.begin(115200);\n              Serial.println("Init complete - relays forced inactive");\n            }\n\n            void activateM(unsigned long ms) {\n              digitalWrite(pinN, outInactiveValue()); // Verrouillage matériel\n              delay(100);\n              digitalWrite(pinM, outActiveValue());\n              Serial.println("M ON");\n              delay(ms);\n              digitalWrite(pinM, outInactiveValue());\n              Serial.println("M OFF");\n              delay(100);\n            }\n\n            void activateN(unsigned long ms) {\n              digitalWrite(pinM, outInactiveValue()); // Verrouillage matériel\n              delay(100);\n              digitalWrite(pinN, outActiveValue());\n              Serial.println("N ON");\n              delay(ms);\n              digitalWrite(pinN, outInactiveValue());\n              Serial.println("N OFF");\n              delay(100);\n            }\n\n            void loop() {\n              activateM(2000);\n              delay(1000);\n              activateN(2000);\n              delay(3000);\n            }\n            ```')
        with st.expander("📄 FICHE MONTAGE N°2 : Commande d'une Charge 230V AC (Ampoule 60W) par Relais", expanded=False):
            st.markdown("\n            #### Objectif :\n            Utiliser un module relais 5V commandé par une sortie numérique Arduino pour allumer une ampoule 230V AC / 60W en toute sécurité.\n\n            #### Schéma de Câblage de Puissance :\n            - **Phase 230V AC** $\\rightarrow$ Borne **`COM`** (Commun) du relais.\n            - Borne **`NO`** (Normalement Ouvert) du relais $\\rightarrow$ Première borne de l'ampoule.\n            - **Neutre 230V AC** $\\rightarrow$ Seconde borne de l'ampoule.\n\n            ```cpp\n            // Programme Arduino : Clignotement de l'ampoule 230V (3s allumée / 3s éteinte)\n            void setup() {\n              pinMode(2, OUTPUT); // Pin 2 reliée à l'entrée IN du relais\n              digitalWrite(2, LOW); // Ampoule éteinte par défaut (COM + NO)\n            }\n\n            void loop() {\n              digitalWrite(2, HIGH); // Commutation relais : Ampoule 230V Allumée\n              delay(3000);\n              digitalWrite(2, LOW);  // Commutation relais : Ampoule 230V Éteinte\n              delay(3000);\n            }\n            ```")
    with tab_fs5:
        st.subheader('✍️ Auto-Évaluation Fiches Savoir & Montages')
        st.markdown("Testez vos connaissances sur l'ensemble des fiches savoir :")
        q_fs1 = st.radio("1. Fiche N°1 : Quel risque majeur survient si les 4 interrupteurs d'un pont en H sont fermés en même temps ?", ['Le moteur tourne 2x plus vite', "Court-circuit direct de l'alimentation (destruction du pont)", 'Inversion automatique du sens', 'Aucun risque'], key='qfs1')
        q_fs2 = st.radio('2. Fiche N°6 : Dans une boucle 4-20 mA, que signifie une mesure de 0 mA ?', ['Valeur minimale du capteur', 'Pleine échelle du capteur', 'Déconnexion ou rupture de câble', 'Surcharge'], key='qfs2')
        q_fs3 = st.radio('3. Fiche N°9 : Quelle est la relation entre Débit (bps) et Bauds pour un signal 16-QAM ?', ['D = R', 'D = 2 * R', 'D = 4 * R', 'D = 16 * R'], key='qfs3')
        if st.button('Valider mes réponses Fiches Savoir', type='primary'):
            score_fs = 0
            if 'Court-circuit' in q_fs1:
                score_fs += 1
            if 'Déconnexion' in q_fs2:
                score_fs += 1
            if 'D = 4 * R' in q_fs3:
                score_fs += 1
            st.success(f'🏆 Score Fiches Savoir : **{score_fs} / 3**')
            if score_fs == 3:
                st.balloons()



elif page == '🛡️ TP Cybersécurité, Gouvernance & pfSense':
    st.markdown("<div class='hero-title'>🛡️ Master Hub Cybersécurité Avancée & Gouvernance</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Plateforme de référence regroupant l'intégralité des 4 cours d'expertise : EBIOS RM & PIA CNIL, PKI & Certificats X.509, Matrice des Flux & Pare-feu pfSense, Chiffrage & VPN (IPsec / OpenVPN).</p>", unsafe_allow_html=True)

    tab_c1, tab_c2, tab_c3, tab_c4, tab_c5, tab_c6, tab_c7 = st.tabs([
        "📊 1. EBIOS RM & PIA (CNIL)",
        "🔑 2. PKI, X.509 & Certificats",
        "🧱 3. pfSense, DMZ & Matrice des Flux",
        "🔒 4. Chiffrage & VPN (IPsec / OpenVPN)",
        "🧪 5. Laboratoire & Simulateurs Pratiques",
        "🗂️ 6. Flashcards Spécifiques (20 Cartes)",
        "📝 7. Grand Examen Blanc Cyber (20 Q)"
    ])

    # =========================================================================
    # TAB 1 : EBIOS RM & PIA
    # =========================================================================
    with tab_c1:
        st.subheader("1. Analyse des Risques : Méthode EBIOS RM & PIA (RGPD / CNIL)")
        st.markdown("""
        <div class='ciel-card'>
            <h4 style='color: #38bdf8; margin-top: 0;'>📌 Deux méthodes complémentaires de référence en France</h4>
            <p>La sécurité informatique ne se limite pas à des outils techniques : elle repose sur une analyse formelle des menaces et de la conformité réglementaire :</p>
            <ul>
                <li><b>EBIOS RM (ANSSI)</b> : <i>Expression des Besoins et Identification des Objectifs de Sécurité - Risk Manager</i>. Protège les <b>actifs métiers et le système d'information de l'organisation</b> (conformité ISO/IEC 27005).</li>
                <li><b>PIA / AIPD (CNIL)</b> : <i>Analyse d'Impact relative à la Protection des Données</i> (RGPD Art. 35). Protège <b>les droits et libertés des personnes physiques</b>. La CNIL recommande expressément de s'appuyer sur EBIOS RM pour l'étude des risques.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🔹 Les 5 Ateliers Collaboratifs d'EBIOS Risk Manager (ANSSI)")
        col_eb1, col_eb2 = st.columns(2)
        with col_eb1:
            st.markdown("""
            **Atelier 1 : Cadrage et socle de sécurité**
            * *Question clé* : **Qu'est-ce qui compte pour nous ?**
            * **Valeurs Métiers (VM)** : Processus, informations stratégiques ou savoir-faire critiques (ex: continuité de télémétrie, secrets de fabrication, réputation).
            * **Biens Supports (BS)** : Éléments matériels, logiciels ou organisationnels hébergeant les VM (serveur Debian, base de données PostgreSQL, automates STM32, administrateurs).
            * **Événements Redoutés (ER)** : Atteintes aux critères **DICP** (*Disponibilité, Intégrité, Confidentialité, Preuve/Traçabilité*) sur une valeur métier (ex: perte d'intégrité de la télémétrie entraînant un diagnostic erroné).
            * *Livrable* : **Fiche de cadrage** et tableau des événements redoutés avec échelle de gravité (de 1-Négligeable à 4-Critique).

            **Atelier 2 : Sources de risque (SR)**
            * *Question clé* : **Qui peut nous attaquer et pourquoi ?**
            * Identification des **Sources de Risque (SR)** : Cybercriminels motivés par le gain financier, concurrents (espionnage), hacktivistes, collaborateurs malveillants ou négligents.
            * Formulation des **Objectifs Visés (OV)** : Vol de données médicales, rançonnage par chiffrement (Ransomware), sabotage industriel.
            * *Livrable* : **Cartographie des couples SR / OV priorisés**.
            """)
        with col_eb2:
            st.markdown("""
            **Atelier 3 : Scénarios stratégiques**
            * *Question clé* : **Par quel chemin macroscopique la menace peut-elle frapper ?**
            * Évaluation de l'**Écosystème** : Fournisseurs de maintenance, prestataires cloud, partenaires réseau.
            * **Chemins d'attaque** : Attaque directe sur le périmètre ou attaque indirecte par rebond via un tiers de confiance moins protégé (attaque par chaîne logistique / *Supply Chain*).
            * *Livrable* : **Matrice de risque stratégique (Gravité x Vraisemblance)**.

            **Atelier 4 : Scénarios opérationnels**
            * *Question clé* : **Concrètement, par quelles techniques l'attaquant progresse-t-il ?**
            * Décomposition en chaînes d'attaque techniques étape par étape (modèle Cyber Kill Chain / MITRE ATT&CK) : Reconnaissance -> Intrusion initiale (Phishing) -> Élévation de privilèges -> Mouvement latéral -> Exfiltration ou sabotage.
            * *Livrable* : **Chaîne d'attaque opérationnelle détaillée**.

            **Atelier 5 : Traitement du risque**
            * *Question clé* : **Que fait-on et à quel coût ?**
            * 4 options : **Réduction/Atténuation** (mesures de sécurité), **Refus/Évitement** (supprimer l'activité), **Partage/Transfert** (assurance), **Maintien/Acceptation** (pour le risque résiduel).
            * *Livrable* : **Plan de traitement du risque priorisé** et fiche d'acceptation du **risque résiduel**.
            """)

        st.markdown("---")
        st.markdown("#### 🔹 L'AIPD / PIA (CNIL) : Protection des Données Personnelles")
        st.markdown("""
        * **Obligation Légale (RGPD Article 35)** : Obligatoire dès qu'un traitement présente un risque élevé pour les droits et libertés. La CNIL définit **9 critères de déclenchement** (ex: données sensibles/santé, surveillance systématique, profilage, personnes vulnérables, volume important). Si au moins **2 critères** sont réunis, le PIA est **juridiquement obligatoire**.
        * **Différence Fondamentale** :
          * **EBIOS RM** protège l'**organisation** contre les pertes financières, d'image ou juridiques.
          * **Le PIA** protège l'**individu** (le citoyen, le patient, l'employé) contre la discrimination, le vol d'identité ou la violation de sa vie privée.
        """)

    # =========================================================================
    # TAB 2 : PKI & CERTIFICATS X.509
    # =========================================================================
    with tab_c2:
        st.subheader("2. Infrastructure à Clés Publiques (PKI) & Certificats X.509")
        st.markdown("""
        <div class='ciel-card'>
            <h4 style='color: #38bdf8; margin-top: 0;'>🔑 Qu'est-ce qu'un Certificat Numérique X.509 ?</h4>
            <p>Un certificat est un <b>fichier électronique standardisé</b> qui lie formellement une <b>identité</b> (Nom de domaine FQDN, serveur, personne, objet connecté) à une <b>clé publique</b>. Cette liaison n'a de valeur que parce qu'elle est <b>cryptographiquement signée par une Autorité de Certification (CA) de confiance</b>.</p>
        </div>
        """, unsafe_allow_html=True)

        col_pk1, col_pk2 = st.columns(2)
        with col_pk1:
            st.markdown("""
            #### 🏛️ Architecture & Hiérarchie de Confiance
            * **Autorité de Certification Racine (Root CA)** :
              * Clé maîtresse de l'organisation. Son certificat est auto-signé.
              * **Règle d'or de sécurité** : La CA Racine doit être **HORS LIGNE (Offline)** et physiquement sécurisée pour être protégée de toute intrusion réseau.
            * **Autorité de Certification Subordonnée / Intermédiaire (Intermediate CA)** :
              * Signée par la Root CA. Elle est en ligne (Online) et signe les certificats d'extrémité du quotidien (serveurs web, VPN, contrôleurs de domaine).
              * Si l'intermédiaire est compromise, seule cette branche est révoquée, préservant la confiance globale.
            * **Magasin de confiance (*Trust Store*)** : Liste des certificats racines pré-installés dans le système d'exploitation ou le navigateur.

            #### 📄 Structure du Certificat X.509 v3
            * **Common Name (CN)** : FQDN principal du serveur (ex: `glpi.labo.local`).
            * **Subject Alternative Name (SAN)** : **Obligatoire aujourd'hui** ! Permet d'associer plusieurs noms alternatifs ou adresses IP (`DNS:srv-glpi`, `IP:192.168.90.10`). Un certificat sans SAN est rejeté par les navigateurs modernes.
            * **Période de validité** : *Not Before* et *Not After* (durée maximale recommandée : 1 an / 398 jours pour le Web).
            * **Signature de la CA** : Hash du certificat chiffré avec la clé privée de l'autorité.
            """)
        with col_pk2:
            st.markdown("""
            #### 🔄 Le Cycle de Vie Complet d'un Certificat (4 Étapes)
            1. **Génération & Demande (CSR - Certificate Signing Request)** :
               * Générée par la machine cliente (Debian, pfSense).
               * Contient l'identité (CN, SAN) et la **clé publique**.
               * ⚠️ **Règle absolue** : La **clé privée ne quitte JAMAIS la machine** qui l'a créée ! Elle n'apparaît jamais dans la CSR.
            2. **Émission & Signature** : La CA valide l'identité et signe le certificat avec sa clé privée.
            3. **Vérification de la Chaîne de Confiance (AIA)** :
               * **AIA (*Authority Information Access*)** : Extension URL embarquée dans le certificat pointant vers le certificat public de la CA émettrice. Permet au client de télécharger le maillon manquant pour remonter la chaîne jusqu'à la racine.
            4. **Révocation (CRL & OCSP)** :
               * **CRL (*Certificate Revocation List*)** : Fichier contenant la liste noire des certificats invalidés avant échéance (vol de clé, départ d'employé).
               * **CDP (*CRL Distribution Point*)** : URL HTTP embarquée dans le certificat où télécharger la CRL.
               * **OCSP (*Online Certificate Status Protocol*)** : Protocole temps réel interrogeant le statut d'un certificat unique sans télécharger l'intégralité de la CRL.
               * ⚠️ **Le piège du "Soft Fail"** : Si le serveur de CRL/CDP est injoignable, de nombreux clients acceptent le certificat par défaut, créant une faille si le service n'est pas hautement disponible.
            """)

    # =========================================================================
    # TAB 3 : PFSENSE & MATRICE DES FLUX
    # =========================================================================
    with tab_c3:
        st.subheader("3. Pare-feu pfSense, DMZ & Matrice des Flux Réseau")
        st.markdown("""
        <div class='ciel-card'>
            <h4 style='color: #38bdf8; margin-top: 0;'>🧱 Pourquoi une Matrice des Flux avant de Configurer ?</h4>
            <p><b>Pas de pare-feu sans plan !</b> Configurer un pare-feu au jugé crée des "trous de sécurité" béants ou bloque des services indispensables. La <b>Matrice des Flux</b> est le document de référence normatif validé par les équipes qui recense chaque communication autorisée.</p>
        </div>
        """, unsafe_allow_html=True)

        col_pf1, col_pf2 = st.columns(2)
        with col_pf1:
            st.markdown("""
            #### 📐 Méthodologie en 4 Étapes
            1. **Inventorier** : Recenser les équipements et leurs rôles (Clients Windows, Serveur AD, DMZ GLPI, Pare-feu pfSense).
            2. **Lister les flux par service** : Identifier les couples source/destination, les protocoles (TCP/UDP) et les ports d'écoute.
            3. **Identifier la traversée du pare-feu** :
               * *Intra-VLAN / Intra-LAN (ex: Client vers SRV-AD01 sur le même switch)* : Le trafic ne traverse **PAS** pfSense -> Pas de règle !
               * *Inter-Zones (ex: LAN -> DMZ, WAN -> DMZ)* : Le trafic traverse pfSense -> **Règle obligatoire sur l'interface d'entrée**.
            4. **Traduire en configuration pfSense** : Créer des **Alias** (groupes d'IP ou de ports) et définir la règle `Action: Pass`, `Interface: Entrée`, `Source`, `Destination`, `Port`.

            #### 🛡️ Architecture & Rôle de la DMZ
            * **Zone Démilitarisée (DMZ)** : Zone tampon isolée accueillant les serveurs exposés à l'extérieur ou aux utilisateurs (Web, GLPI, DNS public).
            * **Règle d'or absolue** :
              * Un flux **DMZ -> LAN** est **STRICTEMENT INTERDIT** par défaut !
              * Si le serveur GLPI en DMZ est compromis par une faille applicative, l'attaquant reste enfermé dans la DMZ et ne peut pas rebondir sur le contrôleur de domaine (AD) du LAN.
            """)
        with col_pf2:
            st.markdown("""
            #### 📋 Extrait de la Matrice des Flux Officielle (TP3)
            | N° | Source | Destination | Proto/Port | Sens | Justification | Règle pfSense |
            | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
            | **1** | Client LAN | SRV-AD01 (LAN) | UDP/TCP 53 | Client -> AD | Résolution DNS | *Intra-LAN (Pas de règle)* |
            | **2** | Client LAN | SRV-AD01 (LAN) | TCP 88, 389 | Client -> AD | Auth Kerberos & LDAP | *Intra-LAN (Pas de règle)* |
            | **3** | Client LAN | Debian GLPI (DMZ) | TCP 443 | Client -> DMZ | Accès Web HTTPS GLPI | **Pass sur Interface LAN** |
            | **4** | Client LAN | pfSense (LAN) | TCP 443 | Client -> FW | Admin Web pfSense | **Pass sur Interface LAN** |
            | **5** | Debian DMZ | SRV-AD01 (LAN) | TCP 636 | DMZ -> AD | Annuaire sécurisé LDAPS | **Pass restreint sur DMZ** |
            | **6** | Debian DMZ | LAN (Tout le reste) | ANY | DMZ -> LAN | Trafic non sollicité | **BLOCK (Par défaut)** |
            | **7** | WAN (Internet)| Debian GLPI (DMZ) | TCP 443 | WAN -> DMZ | Accès public distant | **NAT Port Forward sur WAN** |

            #### 🔍 Audit des Logs & Preuve de Blocage
            * Pour valider une règle, on consulte **Status > System Logs > Firewall**.
            * Un paquet bloqué (croix rouge) sur WAN ou DMZ prouve que la politique restrictive s'applique.
            """)

    # =========================================================================
    # TAB 4 : CHIFFRAGE & VPN
    # =========================================================================
    with tab_c4:
        st.subheader("4. Chiffrage Cryptographique & Tunnels VPN (IPsec / OpenVPN)")
        st.markdown("""
        <div class='ciel-card'>
            <h4 style='color: #38bdf8; margin-top: 0;'>🔒 Les 5 Piliers de la Cryptographie & Réseaux Privés Virtuels</h4>
            <p>Concevoir un réseau sécurisé implique de protéger les communications en transit à travers des réseaux non fiables (Internet). Les protocoles VPN créent un tunnel chiffré étanche entre deux sites distants ou pour des utilisateurs nomades.</p>
        </div>
        """, unsafe_allow_html=True)

        col_vpn1, col_vpn2 = st.columns(2)
        with col_vpn1:
            st.markdown("""
            #### 🛡️ Les 3 Familles de Chiffrement
            * **Chiffrement Symétrique (Clé partagée secrète unique)** :
              * Rapide, idéal pour chiffrer les gros volumes de données en transit.
              * Standards certifiés ANSSI : **AES-128 / AES-256** (modes CBC ou GCM).
            * **Chiffrement Asymétrique (Bi-clé Publique / Privée)** :
              * Plus lent, utilisé pour l'authentification et l'échange de clés secrètes initial.
              * Standards : **RSA (>= 2048 bits)**, **ECC / Ed25519** (courbes elliptiques).
            * **Fonctions de Hachage (Empreinte à sens unique)** :
              * Garantit l'**Intégrité** des paquets.
              * Standards : **SHA-256 / SHA-512** (MD5 et SHA-1 sont formellement proscrits).

            #### 🌐 VPN IPsec (Site-à-Site) : Les 2 Phases IKE
            Le protocole IPsec s'articule impérativement en deux étapes distinctes :
            * **Phase 1 (IKE SA - Internet Key Exchange)** :
              * *Question* : **QUI êtes-vous ?**
              * Authentification mutuelle des routeurs/pare-feux distants (via PSK ou certificat X.509) et négociation d'un canal sécurisé Diffie-Hellman (DH Group 14).
              * Paramètres : Mode IKEv2, AES-256, SHA-256, DH 14, durée de vie **28 800 s (8 h)**.
            * **Phase 2 (IPsec SA)** :
              * *Question* : **QUOI protège-t-on ?**
              * Spécifie les sous-réseaux locaux et distants autorisés à communiquer à travers le tunnel, et chiffre les paquets avec le protocole **ESP (Encapsulating Security Payload)**.
              * Durée de vie plus courte : **3 600 s (1 h)**.
            """)
        with col_vpn2:
            st.markdown("""
            #### 💻 VPN Nomade : OpenVPN vs IPsec
            * **Protocole OpenVPN** :
              * Fonctionne en couche transport au-dessus de **UDP 1194** (rapide) ou **TCP 443** (permet de contourner les pare-feux stricts d'hôtels/entreprises).
              * Utilise deux canaux étanches : **Canal de contrôle (chiffré en TLS)** et **Canal de données**.
              * Modes d'interface : **TUN** (Routage IP Couche 3 - standard recommandé) ou **TAP** (Pontage Ethernet Couche 2).
              * Déploiement : Exportation d'un profil client unique `.ovpn` intégrant la configuration et les certificats via le package `openvpn-client-export`.

            #### ⚡ Split-Tunnel vs Full-Tunnel
            | Mode | Trafic Internet du Client | Avantage | Risque |
            | :--- | :--- | :--- | :--- |
            | **Split Tunnel** | Sort directement par sa box/FAI locale | Économise la bande passante du siège | Le poste distant connecté n'est pas filtré |
            | **Full Tunnel** | Tout le trafic passe par le VPN et pfSense | Filtrage et logs d'entreprise centralisés | Surcharge la ligne Internet du siège |

            *Option pfSense* : Case à cocher **Redirect IPv4 Gateway** pour forcer le Full Tunnel.

            #### 🔑 PSK vs Certificats : Le Scénario de Compromission
            * **Pourquoi préférer les Certificats X.509 pour un VPN ?**
              * Avec une **clé pré-partagée (PSK)** : si un ordinateur portable d'un salarié est volé, il faut modifier la clé secrète chez **l'ensemble des 50 salariés** !
              * Avec des **Certificats X.509** : il suffit de **révoquer l'unique certificat du salarié volé dans la CRL** sur pfSense. Les 49 autres utilisateurs continuent de travailler sans interruption.
            """)

    # =========================================================================
    # TAB 5 : LABS & SIMULATEURS PRATIQUES
    # =========================================================================
    with tab_c5:
        st.subheader("5. Simulateurs & Exercices Pratiques d'Ingénierie Cyber")
        lab_sel = st.selectbox("Sélectionnez l'atelier pratique à exécuter :", [
            "Atelier A : Diagnostic d'une Panne VPN IPsec (Phase 1 vs Phase 2)",
            "Atelier B : Détermination d'une Règle de Pare-feu pfSense (DMZ / LAN)",
            "Atelier C : Analyse du Cycle de Vie d'un Certificat (CSR / CRL)"
        ], key="sel_cyber_lab")

        if "Atelier A" in lab_sel:
            st.markdown("""
            **Scénario d'incident en entreprise** :
            Deux sites distants (Siège et Usine) sont interconnectés via un tunnel VPN IPsec configuré sur deux pare-feux pfSense.
            *Symptôme constaté* : Les logs de pfSense indiquent `IKE SA established successfully`, mais aucun ping ne passe entre les postes du LAN Siège (`192.168.10.0/24`) et du LAN Usine (`192.168.20.0/24`). Les compteurs de paquets IPsec SA restent à 0.
            """)
            st.write("1. Quelle phase du tunnel IPsec est à l'origine du dysfonctionnement ?")
            q_vpn_p = st.radio("Phase en cause :", ["Phase 1 (IKE SA)", "Phase 2 (IPsec SA)", "Panne physique du câble WAN", "Erreur DNS"], key="rad_vpn_p")
            st.write("2. Quelle est la cause la plus probable de cet incident ?")
            q_vpn_c = st.radio("Cause racine identifiée :", [
                "Erreur de clé pré-partagée (Pre-Shared Key)",
                "Désaccord sur la déclaration des réseaux locaux/distants (Phase 2 Proposals) ou règle manquante sur l'onglet IPsec",
                "Le groupe Diffie-Hellman est mal configuré en Phase 1",
                "Le port UDP 500 est bloqué sur le WAN"
            ], key="rad_vpn_c")
            if st.button("Valider le diagnostic IPsec", key="btn_diag_ipsec"):
                if "Phase 2" in q_vpn_p and "Désaccord sur la déclaration" in q_vpn_c:
                    st.success("🏆 **Diagnostic Parfait !** Si la Phase 1 est établie, l'authentification est réussie. Le blocage vient obligatoirement d'une discordance sur les réseaux Phase 2 ou de l'absence de règle autorisant le trafic dans Rules > IPsec (+25 XP).")
                    add_user_points(25, "lab_ipsec_diag")
                else:
                    st.error("❌ Analysez bien : si l'IKE SA est 'established', la Phase 1 est opérationnelle. Le problème se situe en Phase 2.")

        elif "Atelier B" in lab_sel:
            st.markdown("""
            **Scénario pfSense** :
            Un nouveau serveur d'inventaire **GLPI** vient d'être déployé en DMZ (`192.168.90.10`). Les utilisateurs du LAN (`192.168.80.0/24`) doivent y accéder en interface web sécurisée HTTPS.
            """)
            st.write("Sur quelle interface de pfSense devez-vous créer la règle de filtrage pour autoriser ce trafic ?")
            q_pf_int = st.radio("Interface cible :", ["Interface LAN", "Interface DMZ", "Interface WAN", "Onglet Floating Rules"], key="rad_pf_int")
            st.write("Quelle doit être la règle de filtrage exacte ?")
            q_pf_r = st.radio("Configuration de la règle :", [
                "Action: Pass | Source: DMZ net | Dest: LAN net | Port: 443",
                "Action: Pass | Source: LAN net | Dest: 192.168.90.10 | Port: TCP 443 (HTTPS)",
                "Action: Pass | Source: ANY | Dest: ANY | Port: ALL",
                "Action: Block | Source: 192.168.90.10 | Dest: LAN net"
            ], key="rad_pf_r")
            if st.button("Valider la règle pfSense", key="btn_val_pfsense"):
                if "Interface LAN" in q_pf_int and "Source: LAN net | Dest: 192.168.90.10" in q_pf_r:
                    st.success("✅ **Règle pfSense Exacte !** pfSense filtre toujours le trafic sur son **interface d'entrée** (LAN pour les paquets venant des utilisateurs). La règle autorise explicitement le port HTTPS vers l'IP cible (+20 XP).")
                    add_user_points(20, "lab_pfsense_rule")
                else:
                    st.error("❌ Rappel de cours : Dans pfSense, les règles s'appliquent sur l'interface d'ENTRÉE du paquet (ici LAN) et ciblent le serveur DMZ.")

        else:
            st.markdown("""
            **Scénario PKI / X.509** :
            Un administrateur souhaite sécuriser l'accès au serveur web `pfsense.labo.local`. Il génère une requête de signature de certificat (**CSR**).
            """)
            st.write("1. Que contient impérativement le fichier CSR généré ?")
            q_csr1 = st.radio("Contenu de la CSR :", [
                "La clé publique et les identités demandées (CN, SAN)",
                "La clé privée du serveur et son mot de passe",
                "La liste de révocation CRL complète",
                "Le certificat racine de la CA"
            ], key="rad_csr1")
            st.write("2. Si la clé privée du serveur vient à être dérobée par un attaquant, quelle action d'urgence neutralise la menace ?")
            q_csr2 = st.radio("Action d'urgence :", [
                "Supprimer le fichier temporaire sur le serveur",
                "Révoquer le certificat auprès de l'Autorité de Certification et publier la mise à jour sur le point de distribution CRL (CDP)",
                "Changer simplement l'adresse IP du serveur",
                "Redémarrer le service Apache"
            ], key="rad_csr2")
            if st.button("Valider l'analyse PKI", key="btn_val_pki"):
                if "clé publique" in q_csr1 and "Révoquer le certificat" in q_csr2:
                    st.success("✅ **Parfait !** La CSR ne contient que la clé publique. En cas de vol de clé privée, la révocation immédiate via la CRL/CDP est la seule parade efficace (+20 XP).")
                    add_user_points(20, "lab_pki_csr")
                else:
                    st.error("❌ Relisez le cours : la clé privée ne quitte jamais la machine, et la compromission s'arrête par révocation CRL.")

    # =========================================================================
    # TAB 6 : FLASHCARDS SPÉCIFIQUES CYBER (20 CARTES)
    # =========================================================================
    with tab_c6:
        st.subheader("6. Flashcards Réflexes Spéciales Cybersécurité (20 Cartes)")
        st.markdown("<p style='color:#94a3b8;'>Entraînez votre mémoire active sur les notions incontournables des 4 nouveaux cours d'examen.</p>", unsafe_allow_html=True)
        
        CYBER_CARDS_20 = [
            {"q": "Quelle est la différence fondamentale d'objectif entre EBIOS RM et le PIA / AIPD ?", "a": "EBIOS RM (ANSSI) protège le système d'information et les actifs de l'organisation. Le PIA (CNIL) protège la vie privée, les droits et les libertés des personnes physiques (RGPD Art. 35)."},
            {"q": "Quels sont les 5 ateliers d'EBIOS Risk Manager ?", "a": "1. Cadrage et socle de sécurité, 2. Sources de risque, 3. Scénarios stratégiques, 4. Scénarios opérationnels, 5. Traitement du risque."},
            {"q": "Dans EBIOS RM, quelle est la distinction entre une Valeur Métier et un Bien Support ?", "a": "Une Valeur Métier est un processus ou une information critique (ex: facturation, brevets). Un Bien Support est la composante technique qui l'héberge (serveur, base de données, câble, admin)."},
            {"q": "Qu'est-ce qu'une attaque par chaîne logistique (Supply Chain Attack) dans l'Atelier 3 d'EBIOS ?", "a": "Une attaque indirecte qui compromet d'abord un sous-traitant ou un partenaire de confiance moins bien sécurisé pour atteindre le système d'information cible par rebond."},
            {"q": "Quelles sont les 4 options possibles pour le traitement d'un risque dans l'Atelier 5 d'EBIOS ?", "a": "1. Réduction/Atténuation (mesures de sécurité), 2. Refus/Évitement (abandon de l'activité), 3. Transfert/Partage (assurance), 4. Maintien/Acceptation (du risque résiduel)."},
            {"q": "Pourquoi la clé privée ne doit-elle JAMAIS figurer dans une demande de certificat (CSR) ?", "a": "Parce que si la clé privée circulait sur le réseau, n'importe quel attaquant pourrait usurper l'identité du serveur. Elle reste strictement confinée sur la machine qui l'a créée."},
            {"q": "Quelle est l'utilité essentielle de l'extension SAN (Subject Alternative Name) dans un certificat X.509 v3 ?", "a": "Elle permet de certifier plusieurs noms de domaine (FQDN) et adresses IP pour une même machine. Obligatoire pour être validé par les navigateurs modernes."},
            {"q": "Quelle est la différence technique entre une CRL et le protocole OCSP ?", "a": "La CRL est une liste complète des certificats révoqués téléchargée périodiquement (fichier lourd). OCSP interroge le statut d'un certificat unique en temps réel (requête légère)."},
            {"q": "Qu'est-ce que l'extension AIA (Authority Information Access) dans un certificat ?", "a": "Une URL pointant vers le certificat public de la CA émettrice, permettant au client de remonter la chaîne de certification jusqu'à la racine de confiance."},
            {"q": "Quel est le risque de sécurité lié au phénomène de 'Soft Fail' lors de la vérification de révocation ?", "a": "Si le serveur CDP/OCSP est injoignable, le navigateur accepte quand même le certificat par défaut. Un attaquant bloquant l'accès au CDP peut donc faire accepter un certificat révoqué."},
            {"q": "Pourquoi une Autorité de Certification Racine (Root CA) doit-elle être maintenue hors ligne (Offline) ?", "a": "Pour garantir qu'aucune cyberattaque réseau ne puisse compromettre la clé maîtresse suprême de l'organisation. Seules les CA subordonnées sont en ligne."},
            {"q": "Dans une architecture pfSense, pourquoi interdit-on tout flux d'initiative DMZ vers LAN ?", "a": "Pour confiner un attaquant qui compromettrait un serveur web exposé en DMZ, l'empêchant de pivoter vers le cœur de réseau interne (Active Directory, bases sensibles)."},
            {"q": "Sur quelle interface pfSense doit-on positionner une règle de pare-feu ?", "a": "Toujours sur l'interface d'ENTRÉE où pénètrent les paquets (sur l'interface LAN pour le trafic généré par les clients, sur WAN pour les accès extérieurs)."},
            {"q": "Dans pfSense, qu'est-ce qu'un Alias et quel est son intérêt pour la sécurité ?", "a": "Un nom logique regroupant des adresses IP, réseaux ou ports. Il simplifie les règles de pare-feu, évite les erreurs humaines et facilite la maintenance centralisée."},
            {"q": "Pourquoi une communication entre deux postes du même sous-réseau LAN ne nécessite-t-elle aucune règle pfSense ?", "a": "Parce que les paquets sont commutés directement en couche 2 par le switch Ethernet et ne traversent jamais la passerelle/pare-feu pfSense."},
            {"q": "Dans un VPN IPsec, quelle est la différence entre la Phase 1 (IKE) et la Phase 2 (IPsec SA) ?", "a": "La Phase 1 répond à 'Qui êtes-vous ?' (authentification mutuelle des routeurs et canal sécurisé). La Phase 2 répond à 'Que protège-t-on ?' (déclaration des sous-réseaux et chiffrement ESP)."},
            {"q": "Sur quels ports et protocoles opère OpenVPN et pourquoi peut-il utiliser le port TCP 443 ?", "a": "OpenVPN utilise par défaut UDP 1194. Il peut utiliser TCP 443 pour se fondre dans le trafic web HTTPS standard et traverser les pare-feux stricts d'hôtels ou d'entreprises."},
            {"q": "Quelle est la différence entre un VPN en mode Split-Tunnel et en mode Full-Tunnel ?", "a": "Split-Tunnel : seul le trafic d'entreprise passe dans le tunnel (Internet sort par le FAI local). Full-Tunnel : l'intégralité du trafic passe par le VPN et le pare-feu central."},
            {"q": "Pourquoi l'authentification par certificats X.509 est-elle supérieure à une clé partagée (PSK) pour un VPN de 50 nomades ?", "a": "En cas de vol d'un ordinateur portable, il suffit de révoquer son certificat dans la CRL sans impacter les 49 autres collègues. Avec une PSK, il faudrait reconfigurer les 50 postes."},
            {"q": "Pourquoi le chiffrement d'un tunnel VPN ne dispense-t-il pas d'appliquer des règles de pare-feu (ACL) ?", "a": "Parce que le VPN sécurise uniquement le transport des données. Une fois les paquets sortis du tunnel, des ACL strictes doivent vérifier que l'utilisateur n'accède qu'aux serveurs autorisés."}
        ]

        if "fc_cyber_idx" not in st.session_state:
            st.session_state.fc_cyber_idx = 0

        idx_c = st.session_state.fc_cyber_idx
        card = CYBER_CARDS_20[idx_c]

        st.markdown(f"**Carte {idx_c + 1} / {len(CYBER_CARDS_20)}**")
        st.markdown(f"""
        <div class='flashcard-box-modern'>
            <span style='font-size: 0.8rem; text-transform: uppercase; color: #38bdf8; font-weight: 700; letter-spacing: 0.05em;'>QUESTION CYBERSÉCURITÉ</span>
            <div class='flashcard-q-text' style='margin-top: 12px;'>{card['q']}</div>
        </div>
        """, unsafe_allow_html=True)

        rev_c = st.checkbox("👁️ Révéler la Réponse Certifiée", key=f"rev_cyber_{idx_c}")
        if rev_c:
            st.markdown(f"""
            <div class='flashcard-a-box'>
                <b style='color: #059669;'>Réponse officielle :</b><br>
                {card['a']}
            </div>
            """, unsafe_allow_html=True)

        c_prev, c_next = st.columns(2)
        with c_prev:
            if st.button("⬅️ Carte Précédente", key="btn_c_prev") and idx_c > 0:
                st.session_state.fc_cyber_idx -= 1
                st.rerun()
        with c_next:
            if st.button("Carte Suivante ➡️", key="btn_c_next") and idx_c < len(CYBER_CARDS_20) - 1:
                st.session_state.fc_cyber_idx += 1
                st.rerun()

    # =========================================================================
    # TAB 7 : GRAND EXAMEN BLANC CYBER (20 QUESTIONS AVEC XP)
    # =========================================================================
    with tab_c7:
        st.subheader("7. Grand Examen Blanc Certifiant : 20 Questions de Synthèse")
        st.markdown("<p style='color:#94a3b8;'>Testez l'ensemble de vos connaissances sur les 4 cours pour valider votre maîtrise et créditer jusqu'à <b>+100 XP</b> sur votre profil.</p>", unsafe_allow_html=True)

        CYBER_EXAM_20 = [
            {"q": "1. Quel organisme français est l'auteur officiel de la méthode d'analyse de risques EBIOS Risk Manager ?", "opts": ["L'ANSSI", "La CNIL", "Le Ministère des Armées", "L'AFNOR"], "rep": "L'ANSSI", "expl": "EBIOS RM est développé et publié par l'ANSSI (conforme ISO 27005)."},
            {"q": "2. Dans le cadre du RGPD, quel article impose la réalisation d'une Analyse d'Impact (PIA / AIPD) pour les traitements à risque élevé ?", "opts": ["Article 5", "Article 28", "Article 32", "Article 35"], "rep": "Article 35", "expl": "L'article 35 du RGPD régit l'AIPD."},
            {"q": "3. Dans l'Atelier 1 d'EBIOS RM, un serveur de base de données PostgreSQL hébergeant des dossiers médicaux est qualifié de :", "opts": ["Valeur Métier", "Bien Support", "Source de Risque", "Événement Redouté"], "rep": "Bien Support", "expl": "Le serveur héberge la valeur métier (les dossiers médicaux), c'est donc un Bien Support."},
            {"q": "4. Quel livrable clé est produit à l'issue de l'Atelier 3 d'EBIOS RM ?", "opts": ["La matrice de risques stratégiques (Gravité x Vraisemblance)", "Le rapport de câblage réseau", "Le fichier de révocation CRL", "La liste des employés formés"], "rep": "La matrice de risques stratégiques (Gravité x Vraisemblance)", "expl": "L'atelier 3 confronte les sources de risque à l'écosystème pour bâtir la matrice stratégique."},
            {"q": "5. Quelle extension d'un certificat X.509 v3 est aujourd'hui impérativement exigée par les navigateurs pour valider un nom de domaine ou une IP ?", "opts": ["CN (Common Name)", "SAN (Subject Alternative Name)", "CRL (Certificate Revocation List)", "AIA (Authority Information Access)"], "rep": "SAN (Subject Alternative Name)", "expl": "Le champ SAN est obligatoire sous peine de rejet par Chrome, Edge et Firefox."},
            {"q": "6. Dans une PKI d'entreprise, pour quelle raison fondamentale la CA Racine est-elle conservée HORS LIGNE (Offline) ?", "opts": ["Pour économiser l'électricité du data center", "Pour la prémunir totalement contre les compromissions réseau distantes", "Parce que Windows Server interdit la connexion réseau d'une CA racine", "Pour empêcher le renouvellement des baux DHCP"], "rep": "Pour la prémunir totalement contre les compromissions réseau distantes", "expl": "Si la Root CA est compromise, toute l'infrastructure s'effondre. Elle est donc physiquement isolée."},
            {"q": "7. Quel élément d'un certificat indique au client l'adresse URL où il peut télécharger le certificat de l'autorité émettrice pour valider la chaîne ?", "opts": ["L'extension CDP", "L'extension AIA (Authority Information Access)", "La clé publique", "L'empreinte SHA-256"], "rep": "L'extension AIA (Authority Information Access)", "expl": "AIA fournit l'URL du certificat de l'autorité émettrice."},
            {"q": "8. Quelle est la faiblesse de sécurité du protocole de révocation OCSP en mode 'Soft Fail' ?", "opts": ["Il ralentit la navigation web de 10 secondes", "Si le serveur OCSP est injoignable, le client valide quand même le certificat révoqué par défaut", "Il ne fonctionne pas avec l'algorithme RSA", "Il nécessite obligatoirement une connexion en UDP 53"], "rep": "Si le serveur OCSP est injoignable, le client valide quand même le certificat révoqué par défaut", "expl": "Le Soft Fail privilégie la disponibilité au détriment de la sécurité en cas de panne du répondeur."},
            {"q": "9. Sur un pare-feu pfSense, sur quelle interface doit-on créer une règle autorisant un client du LAN à naviguer sur un serveur GLPI en DMZ ?", "opts": ["Sur l'interface LAN", "Sur l'interface DMZ", "Sur l'interface WAN", "Sur l'interface IPsec"], "rep": "Sur l'interface LAN", "expl": "pfSense filtre à l'ENTRÉE des paquets. Le flux étant émis par le client LAN, la règle se place sur LAN."},
            {"q": "10. Dans une architecture réseau sécurisée avec pare-feu, pourquoi interdit-on catégoriquement les flux d'initiative DMZ vers LAN ?", "opts": ["Parce que le routeur ne dispose pas d'assez de mémoire vive", "Pour empêcher un attaquant ayant piraté un service web exposé en DMZ d'infiltrer le cœur du réseau interne", "Parce que le protocole TCP ne fonctionne pas de la DMZ vers le LAN", "Pour obliger l'utilisation du Wi-Fi invité"], "rep": "Pour empêcher un attaquant ayant piraté un service web exposé en DMZ d'infiltrer le cœur du réseau interne", "expl": "La DMZ est une zone semi-sûre qui ne doit jamais pouvoir initier de connexion vers le LAN sécurisé."},
            {"q": "11. Quel protocole et quel port par défaut sont utilisés par OpenVPN ?", "opts": ["TCP 80", "UDP 1194", "TCP 22", "UDP 500"], "rep": "UDP 1194", "expl": "OpenVPN utilise standardisé UDP 1194 (pouvant être basculé sur TCP 443 si nécessaire)."},
            {"q": "12. Dans un tunnel VPN IPsec, à quelle interrogation précise répond la Phase 1 (IKE SA) ?", "opts": ["Quels sont les sous-réseaux locaux et distants à chiffrer ?", "Qui êtes-vous ? (Authentification mutuelle des équipements et négociation du canal sécurisé)", "Combien d'octets ont été transférés ?", "Quel est le nom du serveur DNS de l'entreprise ?"], "rep": "Qui êtes-vous ? (Authentification mutuelle des équipements et négociation du canal sécurisé)", "expl": "Phase 1 = Identité et négociation IKE SA. Phase 2 = Quels réseaux transitent sous scellé IPsec SA."},
            {"q": "13. Quelle est la durée de vie standard recommandée d'une Phase 1 (IKE) sous pfSense ?", "opts": ["60 secondes", "3 600 secondes (1 h)", "28 800 secondes (8 h)", "86 400 secondes (24 h)"], "rep": "28 800 secondes (8 h)", "expl": "La Phase 1 dure 28 800 s (8h) tandis que la Phase 2 est renouvelée toutes les 3 600 s (1h)."},
            {"q": "14. Quel mode VPN fait passer l'intégralité du trafic Internet de l'utilisateur par le pare-feu du siège pour être filtré et journalisé ?", "opts": ["Split-Tunnel", "Full-Tunnel (Redirect Gateway)", "Tunnel GRE simple", "Proxy transparent"], "rep": "Full-Tunnel (Redirect Gateway)", "expl": "Le Full Tunnel achemine 100% des flux via la passerelle d'entreprise."},
            {"q": "15. En cas de vol d'un PC portable chez un utilisateur nomade utilisant un VPN, quel est l'avantage décisif d'une authentification par certificat X.509 sur une clé partagée PSK ?", "opts": ["Le certificat est plus facile à taper sur le clavier", "Il suffit de révoquer l'unique certificat du poste volé dans la CRL sans impacter aucun autre utilisateur", "Le chiffrement par certificat est 1000 fois plus rapide", "La PSK est interdite par la norme IEEE"], "rep": "Il suffit de révoquer l'unique certificat du poste volé dans la CRL sans impacter aucun autre utilisateur", "expl": "Avec des certificats, la gestion de compromission est unitaire et indolore pour le reste de l'entreprise."},
            {"q": "16. Quel protocole IPsec assure à la fois la confidentialité (chiffrement) et l'intégrité/authentification des paquets en Phase 2 ?", "opts": ["AH (Authentication Header)", "ESP (Encapsulating Security Payload)", "ICMP", "IGMP"], "rep": "ESP (Encapsulating Security Payload)", "expl": "ESP encapsule et chiffre les données tout en assurant l'intégrité."},
            {"q": "17. Dans pfSense, quelle fonctionnalité permet d'accéder depuis l'extérieur (WAN) à un serveur web hébergé en DMZ sur une IP privée ?", "opts": ["Le routage dynamique OSPF", "Le NAT Port Forwarding (DNAT)", "L'agent relais DHCP", "Le protocole Spanning Tree"], "rep": "Le NAT Port Forwarding (DNAT)", "expl": "Le DNAT (redirection de port) mappe l'IP WAN publique sur l'IP privée du serveur en DMZ."},
            {"q": "18. Pourquoi le chiffrement d'un tunnel VPN n'affranchit-il pas l'administrateur de configurer des règles de filtrage (ACL) sur le pare-feu ?", "opts": ["Parce que le tunnel VPN tombe en panne après 10 minutes", "Parce que le VPN sécurise uniquement le transport, mais des ACL restent indispensables pour contrôler ce que le client connecté a le droit d'atteindre", "Parce que le protocole IPsec désactive automatiquement le routage", "Pour faire plaisir aux auditeurs de l'ANSSI"], "rep": "Parce que le VPN sécurise uniquement le transport, mais des ACL restent indispensables pour contrôler ce que le client connecté a le droit d'atteindre", "expl": "Le chiffrement sécurise le canal de transit ; le pare-feu régule les autorisations d'accès aux ressources."},
            {"q": "19. Quelle commande OpenSSL permet de vérifier les certificats présentés par un serveur distant sur le port 443 ?", "opts": ["openssl s_client -connect host:443 -showcerts", "openssl verify -all 443", "openssl ca -revoke 443", "openssl genrsa 443"], "rep": "openssl s_client -connect host:443 -showcerts", "expl": "s_client permet d'établir une session SSL/TLS de test et d'afficher la chaîne de certificats reçue."},
            {"q": "20. Quelle action mène-t-on dans l'Atelier 4 d'EBIOS RM ?", "opts": ["La signature de la charte informatique par les salariés", "La construction technique des chaînes d'attaque opérationnelles détaillant le mode opératoire de l'attaquant", "L'achat d'un nouveau pare-feu pfSense", "La suppression de tous les comptes administrateurs"], "rep": "La construction technique des chaînes d'attaque opérationnelles détaillant le mode opératoire de l'attaquant", "expl": "L'atelier 4 décortique concrètement le mode opératoire technique (Cyber Kill Chain)."}
        ]

        with st.form(key="form_cyber_exam_20"):
            user_exam_ans = {}
            for idx_e, qitem in enumerate(CYBER_EXAM_20):
                st.markdown(f"**Q{idx_e + 1} : {qitem['q']}**")
                user_exam_ans[idx_e] = st.radio(f"Choix Q{idx_e + 1} :", qitem["opts"], key=f"rad_exam_c_{idx_e}")
                st.markdown("<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True)
            
            sub_exam = st.form_submit_button("Valider mon Examen Blanc Cybersécurité (20 Questions)", type="primary")

        if sub_exam:
            score_e = 0
            st.markdown("---")
            st.markdown("### 📊 Résultats Officiels de l'Examen Blanc")
            for idx_e, qitem in enumerate(CYBER_EXAM_20):
                u_a = user_exam_ans[idx_e]
                if u_a == qitem["rep"]:
                    score_e += 1
                    st.success(f"✅ **Q{idx_e + 1} Exact !** ({u_a})\n\n💡 *Explication :* {qitem['expl']}")
                else:
                    st.error(f"❌ **Q{idx_e + 1} Erreur.** Vous avez répondu : *{u_a}* | Attendu : **{qitem['rep']}**\n\n💡 *Explication :* {qitem['expl']}")

            pct_e = (score_e / len(CYBER_EXAM_20)) * 100
            xp_gagnes = score_e * 5
            add_user_points(xp_gagnes, "cyber_master_exam")
            save_score(score_e, len(CYBER_EXAM_20), {"Cybersécurité": score_e})

            if score_e >= 16:
                st.success(f"🏆 **Félicitations ! Score Remarquable : {score_e} / 20 ({pct_e:.1f}%) !** Vous remportez **+{xp_gagnes} XP** sur votre profil.")
                st.balloons()
            elif score_e >= 10:
                st.info(f"👍 **Examen Validé : {score_e} / 20 ({pct_e:.1f}%) !** Vous remportez **+{xp_gagnes} XP**. Relisez les points où vous avez hésité.")
            else:
                st.warning(f"⚠️ **Score : {score_e} / 20 ({pct_e:.1f}%)**. Vous gagnez **+{xp_gagnes} XP**. Révisez les onglets de cours et pratiquez les 20 flashcards.")


elif page == '📖 Culture Générale & Expression (CGE)':
    st.markdown("<div class='hero-title'>📖 Culture Générale & Expression (Épreuve E1)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Préparation méthodologique de l'épreuve écrite E1 (Coefficient 2, 3h), thèmes officiels 2025/2026/2027 et entraînements</p>", unsafe_allow_html=True)

    tab_cge1, tab_cge2, tab_cge3, tab_cge4 = st.tabs([
        "🎯 Réforme & Méthodologie E1",
        "🐾 Thème 2026 : « Les animaux et nous »",
        "🍽️ Thème 2025 : « À table ! »",
        "✍️ Entraînement & Sujets Zéro"
    ])

    with tab_cge1:
        st.subheader("1. Modalités Officielles & Structure de l'Épreuve E1")
        st.markdown("""
<div class='ciel-card' style='border-left: 6px solid #2563eb !important;'>
    <h4 style='color: #1d4ed8; margin-top: 0;'>📋 Cadre Réglementaire de l'Épreuve Écrite E1</h4>
    <ul style='color: #1e293b; line-height: 1.8;'>
        <li><b>Coefficient officiel</b> : <b>2</b> (Épreuve écrite nationale de <b>3 heures</b>, réformée depuis l'arrêté de juillet 2023).</li>
        <li><b>Notation globale</b> : Notée sur <b>20 points</b>, scindée en deux parties équilibrées (10 pts + 10 pts).</li>
        <li><b>Changement majeur de la réforme</b> : Fin de la synthèse de documents académique stricte et de l'écriture personnelle isolée ! L'épreuve privilégie désormais la confrontation d'idées, la finesse d'analyse et l'argumentation critique.</li>
    </ul>
</div>
        """, unsafe_allow_html=True)

        col_cge_p1, col_cge_p2 = st.columns(2)
        with col_cge_p1:
            st.markdown("""
<div class='ciel-card'>
    <h4 style='color: #0284c7; margin-top: 0;'>Partie 1 : Questions sur le Corpus (10 pts)</h4>
    <p><b>Durée conseillée : 1h15 à 1h20</b></p>
    <ul>
        <li><b>Composition du corpus</b> : 2 à 3 documents complémentaires (textes littéraires, essais philosophiques ou sociologiques, articles de presse, documents iconographiques ou artistiques).</li>
        <li><b>Objectif</b> : Répondre à <b>2 ou 3 questions d'analyse et de confrontation</b>.</li>
        <li><b>Méthode clé</b> : Ne jamais résumer document par document ! Il faut croiser les points de vue, identifier les convergences, les nuances et les oppositions entre les auteurs.</li>
        <li><b>Règle d'or</b> : Citer précisément le texte (« ... ») en indiquant les lignes pour justifier chaque affirmation.</li>
    </ul>
</div>
            """, unsafe_allow_html=True)

        with col_cge_p2:
            st.markdown("""
<div class='ciel-card'>
    <h4 style='color: #7c3aed; margin-top: 0;'>Partie 2 : Rédaction d'un Essai (10 pts)</h4>
    <p><b>Durée conseillée : 1h20 à 1h30 (dont 15 min de relecture)</b></p>
    <ul>
        <li><b>Sujet au choix</b> : Choix entre 2 sujets d'essai problématisés en lien direct avec le thème annuel de deuxième année.</li>
        <li><b>Structure attendue</b> :
            <ul>
                <li><b>Introduction</b> : Accroche d'actualité/culturelle, définition des termes clés, problématique claire et annonce du plan (2 ou 3 axes).</li>
                <li><b>Développement (2 ou 3 parties)</b> : Chaque partie défend une thèse nuancée avec arguments logiques et exemples précis (littérature, cinéma, histoire, sciences).</li>
                <li><b>Conclusion</b> : Bilan synthétique répondant à la problématique et ouverture pertinente.</li>
            </ul>
        </li>
    </ul>
</div>
            """, unsafe_allow_html=True)

    with tab_cge2:
        st.subheader("2. Thème de 2e Année (Session 2026) : « Les animaux et nous : imaginer, connaître, comprendre l'animal »")
        st.markdown("""
<div class='ciel-card' style='border-left: 6px solid #10b981 !important; background: #f0fdf4;'>
    <h4 style='color: #065f46; margin-top: 0;'>📖 Problématique Officielle du Bulletin Officiel (BO n°17)</h4>
    <p style='color: #166534;'>L'homme n'a cessé de rêver les animaux comme autant de miroirs, d'emblèmes voire de repoussoirs de lui-même. Objets de fascination, de délectation ou d'effroi, les animaux suscitent une multiplicité de représentations artistiques et philosophiques. Ce thème invite à interroger la frontière poreuse entre l'humain et l'animal, la hiérarchie des espèces et les responsabilités éthiques contemporaines.</p>
</div>
        """, unsafe_allow_html=True)

        col_th1, col_th2 = st.columns(2)
        with col_th1:
            st.markdown("""
#### 🐾 4 Axes Clés d'Analyse
1. **L'animal-miroir & les mythes fondateurs** :
   * Des fables d'Ésope et de La Fontaine aux métamorphoses d'Ovide ou de Kafka. L'animal sert à démasquer les vices humains, à satiriser le pouvoir et à explorer nos pulsions refoulées.
2. **La frontière homme/animal et les savoirs scientifiques** :
   * De la théorie cartésienne de l'« animal-machine » (Descartes) aux découvertes éthologiques modernes (Frans de Waal, Jane Goodall).
   * La reconnaissance de la **sentience**, de l'intelligence animale, de la transmission culturelle et des émotions chez les bêtes.
3. **Exploitation, domination et hiérarchies** :
   * L'élevage industriel, l'expérimentation animale, la domestication sélective vs les animaux sacralisés ou compagnons d'affection.
4. **Éthique animale & nouveaux rapports au vivant** :
   * L'antispécisme (Peter Singer, *La Libération animale*), le bien-être animal, les droits juridiques (l'animal reconnu comme « être vivant doué de sensibilité » dans le Code civil) et la préservation de la biodiversité menacée.
            """)

        with col_th2:
            st.markdown("""
#### 📚 Références & Exemples Culturels Incontournables
* **Littérature classique & moderne** :
  * Jean de La Fontaine, *Fables* (« Les Animaux malades de la peste », « Le Loup et l'Agneau »).
  * George Orwell, *La Ferme des animaux* (allégorie politique du totalitarisme).
  * Franz Kafka, *La Métamorphose* (l'aliénation humaine à travers l'insecte).
  * Vercors, *Les Animaux dénaturés* (questionnement de la définition légale de l'humain).
* **Philosophie & Essais** :
  * Michel de Montaigne, *Essais* (« Quand je me joue avec ma chatte, qui sait si elle passe son temps de moi plus que je ne fais d'elle ? »).
  * Élisabeth de Fontenay, *Le silence des bêtes*.
  * Jean-Baptiste Jeangène Vilmer, *L'éthique animale*.
* **Cinéma & Documentaires** :
  * *Princesse Mononoké* (Hayao Miyazaki) : la confrontation entre industrialisation humaine et dieux-animaux de la forêt.
  * *Okja* (Bong Joon-ho) : dérive de l'élevage transgénique capitaliste.
            """)

    with tab_cge3:
        st.subheader("3. Thème Précédent (Session 2025) : « À table ! : formes et enjeux du repas »")
        st.markdown("""
<div class='ciel-card' style='border-left: 6px solid #f59e0b !important;'>
    <h4 style='color: #b45309; margin-top: 0;'>🍽️ Enjeux Sociologiques, Anthropologiques & Écologiques du Repas</h4>
    <p>Le repas n'est pas un simple besoin biologique de nutrition : c'est un <b>fait social total</b>, un rituel de commensalité, d'intégration sociale et un miroir des inégalités.</p>
    <ul>
        <li><b>Commensalité & Liens sociaux</b> : Partager le pain (*cum panis* = compagnon). Le banquet platonicien, les repas de famille, la fête villageoise.</li>
        <li><b>Distinction sociale & Codes de table</b> : Pierre Bourdieu (*La Distinction*) et Norbert Elias (*La Civilisation des mœurs*). La manière de se tenir à table, le choix des aliments et les arts de la table manifestent le statut social.</li>
        <li><b>Industrialisation, Fast-food vs Terroir</b> : La standardisation de l'alimentation, la malbouffe, face au renouveau du bio, des circuits courts et du repas gastronomique des Français (classé au patrimoine immatériel de l'UNESCO).</li>
        <li><b>Écologie & Éthique alimentaire</b> : Gaspillage alimentaire, empreinte carbone de la viande, végétarisme et transition agricole.</li>
    </ul>
</div>
        """, unsafe_allow_html=True)

    with tab_cge4:
        st.subheader("4. Entraînement Pratique & Sujets Zéro")
        st.markdown("""
<div class='ciel-card'>
    <h4>Exemple de Sujet d'Essai (Thème 2026) :</h4>
    <p><i>« Pensez-vous que mieux connaître les animaux conduit nécessairement les êtres humains à mieux les respecter ? »</i></p>
    <p><b>Pistes de problématisation :</b></p>
    <ul>
        <li><b>Thèse 1 (Oui)</b> : L'éthologie et les neurosciences révèlent la sensibilité, l'intelligence et la vie émotionnelle des bêtes, faisant reculer la thèse de l'animal-machine et inspirant de nouvelles lois de protection animale.</li>
        <li><b>Thèse 2 (Nuance / Limites)</b> : Pourtant, la connaissance accrue des espèces n'empêche pas l'optimisation industrielle de leur exploitation (zootechnie, élevages intensifs ultra-rationnalisés, biopiraterie), subordonnant le respect aux impératifs économiques.</li>
        <li><b>Synthèse / Dépassement</b> : Le respect ne découle pas seulement du savoir scientifique, mais d'une révolution éthique et philosophique repensant la place de l'homme au sein du vivant (cohabitation harmonieuse, décentrement anthropocentrique).</li>
    </ul>
</div>
        """, unsafe_allow_html=True)




elif page == '🗓️ Révision Semaine par Semaine (BTS Blanc)':
    st.markdown("<div class='hero-title'>🗓️ Programme de Révision Semaine par Semaine (A à Z)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Cours magistraux exhaustifs issus des 132 sources officielles, fiches savoirs, travaux pratiques, flashcards actives et examens blancs à scores persistants</p>", unsafe_allow_html=True)
    
    tab_w1, tab_w2, tab_w3, tab_w4, tab_w5, tab_w6 = st.tabs([
        'Semaine 1 (Réseaux & Commutation)', 
        'Semaine 2 (Cyber & Administration)', 
        'Semaine 3 (C++, Python & Sockets)', 
        'Semaine 4 (Électronique, Signaux & Maths)', 
        'Semaine 5 (SysML, UML & Projet E6)', 
        'Semaine 6 (Annales 2024-2026 & Synthèse)'
    ])
    
    # =========================================================================
    # SEMAINE 1 : RÉSEAUX & COMMUTATION
    # =========================================================================
    with tab_w1:
        st.subheader('🗓️ Semaine 1 : Réseaux, Commutation & Routage (Programme Complet)')
        w1_sub1, w1_sub2, w1_sub3, w1_sub4 = st.tabs(['📚 Cours Magistral Approfondi S1', '🗂️ Flashcards S1', '✍️ Exercices Pratiques S1', '📝 Examen Blanc S1'])
        
        with w1_sub1:
            st.markdown(r"""
### 1.1 Architecture des Réseaux : Modèles OSI & TCP/IP
Le **modèle OSI** (Open Systems Interconnection - 7 couches ISO) et le **modèle TCP/IP** (modèle Internet - 4 couches DoD) régissent l'interopérabilité mondiale des systèmes hétérogènes.

| Couche OSI | Nom Couche | PDU (Unité de Donnée) | Rôle & Fonctions Principales | Protocoles & Normes de Référence |
| :---: | :---: | :---: | :--- | :--- |
| **7** | **Application** | Donnée (Data) | Interface directe avec les processus logiciels et l'utilisateur. | HTTP/HTTPS (80/443), DNS (53), DHCP (67/68), SSH (22), FTP (20/21), SMTP (25), MQTT (1883), SNMP (161/162). |
| **6** | **Présentation** | Donnée (Data) | Formatage, sérialisation syntaxique, compression et chiffrement/déchiffrement. | TLS 1.3 / SSL, ASCII, UTF-8, JSON, XML, ASN.1, MIME, JPEG, MPEG. |
| **5** | **Session** | Donnée (Data) | Établissement, gestion, synchronisation et terminaison des dialogues entre applications. | RPC, NetBIOS, Sockets POSIX, NFS, SMB (445), TLS Session Handshake. |
| **4** | **Transport** | **Segment** (TCP) / **Datagramme** (UDP) | Communication de bout en bout (*End-to-End*) entre processus applicatifs via les numéros de ports (0 à 65535). Segmentation et réassemblage. | **TCP** (orienté connexion, fiable, séquencé, contrôle de flux) / **UDP** (non connecté, rapide, sans garantie d'acheminement). |
| **3** | **Réseau** | **Paquet** (Packet) | Adressage logique universel (IPv4, IPv6) et détermination du meilleur chemin (Routage dynamique et statique). | IPv4, IPv6, ICMP, ICMPv6, ARP (pivot C2/C3), OSPF, RIP, BGP, IPsec. |
| **2** | **Liaison** | **Trame** (Frame) | Adressage physique matériel (Adresse MAC sur 48 bits), contrôle d'accès au support (CSMA/CD en Ethernet, CSMA/CA en Wi-Fi) et détection d'erreurs (FCS / CRC32). | Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), VLAN Trunking (IEEE 802.1Q), Spanning Tree (802.1D/802.1w), PPP, HDLC. |
| **1** | **Physique** | **Bit** / Signal | Transmission brute des éléments binaires sous forme de signaux électriques, d'impulsions optiques ou d'ondes électromagnétiques radio. | Câbles cuivre RJ45 (Cat 6/6a), Fibre optique Monomode (SMF) & Multimode (MMF), RS-485, Bus CAN (ISO 11898), modulation LoRa. |

#### Le Mécanisme Fondamental d'Encapsulation et de Désencapsulation
* **Encapsulation (Émission)** : Les données applicatives descendent la pile. Chaque couche ajoute son propre en-tête (*Header*) contenant les informations de contrôle spécifiques (ex: ports TCP en C4, adresses IP en C3, adresses MAC et Tag 802.1Q en C2, préambule de synchronisation en C1).
* **Désencapsulation (Réception)** : Le récepteur vérifie la conformité de l'en-tête de la couche correspondante (ex: calcul du CRC/FCS pour vérifier l'intégrité de la trame en C2), retire l'en-tête et transmet le payload (*charge utile*) à la couche supérieure.

---

### 1.2 Adressage IPv4, Classes, CIDR et Méthodologie Complète VLSM
Une adresse IPv4 est codée sur **32 bits** (4 octets), scindée en deux parties fondamentales : l'identifiant du réseau (**NetID**) et l'identifiant de l'hôte (**HostID**).

#### Adresses Privées (Norme RFC 1918) :
Ces plages sont strictement réservées aux réseaux locaux (LAN/DMZ) et ne sont **jamais routées sur Internet public** :
* **Classe A** : `10.0.0.0` à `10.255.255.255` (Masque par défaut : `/8` soit `255.0.0.0`).
* **Classe B** : `172.16.0.0` à `172.31.255.255` (16 blocs `/16` contigus, masque par défaut : `255.255.0.0`).
* **Classe C** : `192.168.0.0` à `192.168.255.255` (256 blocs `/24` contigus, masque par défaut : `255.255.255.0`).
* **Adresses Particulières d'Examen** :
  * `127.0.0.0/8` : Boucle locale de test (*Loopback*, ex: `127.0.0.1` localhost).
  * `169.254.0.0/16` : Adresses d'auto-configuration de secours **APIPA** attribuées lorsque le serveur DHCP ne répond pas (aucun accès Internet possible).
  * `224.0.0.0` à `239.255.255.255` : Classe D (Multicast/Diffusion groupée, ex: `224.0.0.5` pour OSPF).

#### Formules Mathématiques Incontournables :
Pour un sous-réseau défini par son préfixe CIDR ($n$ bits de masque) :
1. **Nombre total d'adresses du bloc** :
   $$N_{\text{total}} = 2^{(32 - n)}$$
2. **Nombre d'adresses d'hôtes assignables (utiles)** :
   $$N_{\text{hôtes utiles}} = 2^{(32 - n)} - 2$$
   *(On retire obligatoirement 2 adresses : l'adresse Réseau où tous les bits d'hôtes sont à 0, et l'adresse de Diffusion/Broadcast où tous les bits d'hôtes sont à 1).*
3. **Pas de progression (Intervalle magique $\Delta$)** :
   $$\Delta = 256 - \text{valeur décimale de l'octet de masque modifié}$$

---

### 1.3 Adressage IPv6 : Structure, Types et Calcul EUI-64
L'IPv6 résout la pénurie d'adresses en utilisant **128 bits** (16 octets), écrits sous la forme de 8 groupes de 4 chiffres hexadécimaux séparés par des deux-points (ex: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).

#### Règles de Simplification d'Écriture :
1. **Omission des zéros non significatifs en tête** de chaque bloc (ex: `0db8` devient `db8`, `0000` devient `0`).
2. **Double deux-points (`::`)** : Remplace une suite unique de blocs contigus constitués exclusivement de zéros. *Attention : le symbole `::` ne peut être utilisé qu'une seule fois par adresse.*

#### Typologie des Adresses IPv6 :
* **Global Unicast (GUA)** : Préfixe `2000::/3` (routables publiquement sur Internet).
* **Unique Local (ULA)** : Préfixe `fc00::/7` (équivalent IPv6 des adresses privées RFC 1918).
* **Link-Local (Lien Local)** : Préfixe `fe80::/10` (obligatoires sur chaque interface active, non routables, utilisées par les protocoles de découverte et de routage).
* **Multicast** : Préfixe `ff00::/8` (ex: `ff02::1` tous les nœuds du lien, `ff02::2` tous les routeurs). *Le broadcast n'existe plus en IPv6 !*
* **Boucle locale** : `::1/128`.

#### Méthode Officielle de Calcul EUI-64 (Sujets E4 2024 & 2025) :
Pour générer automatiquement les 64 bits d'hôte (Interface ID) à partir de l'adresse MAC (48 bits) :
1. Séparer l'adresse MAC en deux moitiés de 24 bits (ex: `fc:c2:3d` et `0a:68:07`).
2. Insérer les 16 bits `ff:fe` au milieu : `fc:c2:3d:ff:fe:0a:68:07`.
3. Inverser le 7e bit (bit Universel/Local U/L) du premier octet :
   `fc` en binaire vaut `1111 1100`. Le 7e bit (en partant de la gauche) est 0 ; inversé, il devient 1 $\Rightarrow$ `1111 1110` en binaire = `fe` en hexadécimal.
4. L'identifiant EUI-64 généré est donc : `fec2:3dff:fe0a:6807`.

---

### 1.4 Commutation Ethernet, VLANs & Trunking IEEE 802.1Q
Un commutateur (*Switch*) opère en Couche 2 du modèle OSI. Il bâtit dynamiquement sa **table d'adresses MAC** (table CAM) par apprentissage passif :
1. À la réception d'une trame, il lit la **MAC Source** et l'associe au port physique d'entrée avec une durée de vie (*Aging Timer* typique de 300 s).
2. Pour acheminer la trame, il consulte la **MAC Destination** :
   * Si la MAC est connue dans la table CAM : transmission point-à-point vers le port associé (*Forwarding*).
   * Si la MAC est inconnue ou de Broadcast (`ff:ff:ff:ff:ff:ff`) : diffusion sur tous les ports du VLAN sauf le port d'entrée (*Flooding*).

#### Segmentation par VLANs et Trunking 802.1Q :
* Les **VLANs (Virtual Local Area Networks)** scindent le réseau en plusieurs domaines de diffusion étanches, renforçant la sécurité et limitant les tempêtes de broadcast.
* Pour transporter plusieurs VLANs sur un même câble physique reliant deux switchs ou un switch et un routeur, on utilise un lien **Trunk** conforme au standard **IEEE 802.1Q**.
* La norme insère un **Tag de 4 octets** (32 bits) entre les champs MAC Source et EtherType de la trame Ethernet :
  * **TPID (16 bits)** : `0x8100` (identifie une trame étiquetée 802.1Q).
  * **PCP (3 bits)** : Priorité de Qualité de Service (QoS 802.1p).
  * **DEI (1 bit)** : Éligibilité à l'abandon en cas d'encombrement.
  * **VID (12 bits)** : Identifiant du VLAN (de 1 à 4094, les IDs 0 et 4095 étant réservés).
* **VLAN Natif** : VLAN dont les trames transitent **sans étiquette (non taguées)** sur le Trunk (par défaut VLAN 1). Il doit impérativement être identique aux deux extrémités du lien Trunk sous peine de failles de sécurité.

---

### 1.5 Routage Inter-VLAN (Router-on-a-Stick) & Protocoles de Routage
Pour faire communiquer des équipements situés dans des VLANs distincts, l'intervention d'une passerelle de niveau 3 (Routeur ou Switch L3) est obligatoire.

#### Technique Router-on-a-Stick :
Une seule interface physique de routeur (ex: `GigabitEthernet0/0/0`) est reliée à un port Trunk du commutateur. On crée des sous-interfaces logiques virtuelles associées à chaque VLAN :
```text
Router(config)# interface g0/0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.254 255.255.255.0

Router(config)# interface g0/0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.254 255.255.255.0
```

#### Protocoles de Routage : Statique vs Dynamique :
* **Routage Statique** : Configuration manuelle par l'administrateur (`ip route <réseau_cible> <masque> <passerelle_suivante>`). Idéal pour la route par défaut (`ip route 0.0.0.0 0.0.0.0 <IP_FAI>`).
* **Routage Dynamique OSPF (Open Shortest Path First - RFC 2328)** :
  * Protocole à **état de liens** utilisant l'algorithme de Dijkstra (SPF - Shortest Path First).
  * Métrique basée sur le coût inversement proportionnel à la bande passante :
    $$\text{Coût} = \frac{\text{Bande Passante de Référence (100 Mbps)}}{\text{Bande Passante de l'Interface}}$$
  * Organisation hiérarchique en zones (*Areas*). Toutes les zones doivent obligatoirement être raccordées à la zone dorsale **Area 0 (Backbone)**.
  * Convergence ultra-rapide sans boucle de routage grâce aux paquets LSA (Link-State Advertisements).
            """)
        
        with w1_sub2:
            st.markdown("#### 🗂️ Flashcards Réflexes Spécifiques à la Semaine 1")
            fc_s1 = [f for f in FLASHCARDS_DATA if f.get('module') == '📶 Réseaux & Télécoms']
            for fc in fc_s1[:12]:
                with st.expander(f"📌 Carte N°{fc['id']} : {fc['q']}"):
                    st.markdown(f"**Réponse :** {fc['a']}")
                    st.info(f"{fc['note']}")
        
        with w1_sub3:
            st.markdown("#### ✍️ Exercices Pratiques d'Application (Réseaux & Commutation)")
            st.markdown("""
**Exercice 1 : Découpage VLSM d'un réseau d'entreprise**
Vous disposez de l'adresse réseau `192.168.10.0/24`. Vous devez créer :
* Sous-réseau A : 60 postes pour le département Ingénierie.
* Sous-réseau B : 25 postes pour le département Administration.
* Sous-réseau C : 12 postes pour le réseau Wi-Fi Invités.
* Sous-réseau D : 2 adresses pour le lien point-à-point routeur-switch.
            """)
            ex_ans = st.text_input("Indiquez le CIDR nécessaire pour le Sous-réseau A (60 postes) :", placeholder="ex: /26", key="w1_ex_cidr")
            if st.button("Vérifier l'exercice VLSM", key="w1_btn_check"):
                if ex_ans.strip() == "/26":
                    st.success("✅ **Exact !** 2^(32-26) - 2 = 64 - 2 = 62 hôtes utilisables. Le masque est 255.255.255.192.")
                    add_user_points(15, "w1_vlsm_ex")
                else:
                    st.error("❌ Pour 60 hôtes, il faut au moins 6 bits d'hôtes (2^6 - 2 = 62). 32 - 6 = 26, soit un masque /26.")

        with w1_sub4:
            st.markdown("#### 📝 Questionnaire Certifiant de Fin de Semaine 1")
            render_10_questions_quiz("Réseaux", "w1_final_quiz")

    # =========================================================================
    # SEMAINE 2 : CYBERSÉCURITÉ & SYSADMIN
    # =========================================================================
    with tab_w2:
        st.subheader('🗓️ Semaine 2 : Cybersécurité, Gouvernance & Administration Système')
        w2_sub1, w2_sub2, w2_sub3, w2_sub4 = st.tabs(['📚 Cours Magistral Approfondi S2', '🗂️ Flashcards S2', '✍️ Exercices Pratiques S2', '📝 Examen Blanc S2'])
        
        with w2_sub1:
            st.markdown(r"""
### 2.1 Gouvernance de la Cybersécurité : Méthode EBIOS Risk Manager (ANSSI)
La méthode **EBIOS RM** (*Expression des Besoins et Identification des Objectifs de Sécurité*) est la méthodologie nationale française pilotée par l'ANSSI pour évaluer et traiter les risques numériques. Elle s'articule rigoureusement autour de **5 Ateliers collaboratifs progressifs** :

```text
[ Atelier 1 : Cadrage & Socle de Sécurité ]
                     │
                     ▼
[ Atelier 2 : Sources de Risque (SR) & Objectifs Visés (OV) ]
                     │
                     ▼
[ Atelier 3 : Scénarios Stratégiques (Écosystème & Parties Prenantes) ]
                     │
                     ▼
[ Atelier 4 : Scénarios Opérationnels (Chemins d'attaque Cyber & MITRE ATT&CK) ]
                     │
                     ▼
[ Atelier 5 : Traitement du Risque & Plan de Sécurité (PACS) ]
```

1. **Atelier 1 : Cadrage & Socle de Sécurité**
   * Définition du périmètre de l'étude (système d'information, chaîne de production industrielle).
   * Recensement des **Valeurs Métiers** (processus critiques, données sensibles) et des **Biens Supports** matériels ou logiciels qui les hébergent (serveurs AD, bases de données, automates PLC).
   * Évaluation des **Besoins de Sécurité** selon les critères fondamentaux **DICP** : Disponibilité, Intégrité, Confidentialité, Preuve/Traçabilité (notés sur une échelle de 1 à 4).
   * Vérification de la conformité au **Socle de Sécurité** (règles d'hygiène informatique de l'ANSSI, guides de durcissement, ISO 27001).
2. **Atelier 2 : Sources de Risque (SR)**
   * Identification et caractérisation des attaquants potentiels : cybercriminels motivés par l'appât du gain (rançongiciels), États/agences de renseignement (cyber-espionnage), concurrents déloyaux, hacktivistes, ou initiés malveillants/négligents.
   * Détermination de leurs **Objectifs Visés (OV)**.
3. **Atelier 3 : Scénarios Stratégiques**
   * Cartographie de l'écosystème : identification des **parties prenantes les plus vulnérables** (fournisseurs de maintenance, prestataires cloud, sous-traitants d'infogérance).
   * Modélisation des voies d'attaque globales empruntant des tiers de confiance pour atteindre la cible principale.
4. **Atelier 4 : Scénarios Opérationnels**
   * Description technique pas-à-pas des **modes opératoires d'attaque** (Kill Chain cyber, matrice MITRE ATT&CK) : hameçonnage initial (phishing), exploitation de vulnérabilités CVE, élévation de privilèges (Pass-the-Hash), mouvement latéral, exfiltration et chiffrement des données.
5. **Atelier 5 : Traitement du Risque**
   * Arbitrage des mesures de traitement : Réduction (mise en œuvre de contre-mesures techniques et organisationnelles), Refus/Évitement, Transfert (cyber-assurance) ou Rétention/Acceptation du risque résiduel.
   * Élaboration du **Plan d'Amélioration Continue de la Sécurité (PACS)**.

---

### 2.2 Analyse d'Impact relative à la Protection des Données (PIA / AIPD - RGPD)
En vertu de l'article 35 du **RGPD**, la réalisation d'une **AIPD (Analyse d'Impact sur la Protection des Données)** est juridiquement **obligatoire** avant tout traitement de données personnelles susceptible d'engendrer un risque élevé pour les droits et libertés des personnes physiques.

#### Les 9 Critères Européens du CEPD / CNIL :
Si un traitement coche au moins **2 des 9 critères suivants**, l'AIPD est indispensable :
1. Évaluation ou notation des personnes (scoring bancaire, profiling).
2. Prise de décision automatisée avec effet juridique ou similaire.
3. Surveillance systématique des personnes (vidéoprotection dans l'espace public, tracking GPS).
4. Données sensibles ou à caractère hautement personnel (données de santé, opinions politiques, condamnations, biométrie).
5. Données collectées à grande échelle (volume de personnes concernées très élevé).
6. Croisement ou combinaison d'ensembles de données hétérogènes.
7. Données concernant des personnes vulnérables (enfants, patients, personnes âgées, salariés face à leur employeur).
8. Utilisation de technologies innovantes ou nouvelles applications de solutions existantes (reconnaissance faciale par IA).
9. Traitement empêchant les personnes d'exercer un droit ou de bénéficier d'un service.

---

### 2.3 Administration GNU/Linux : Permissions, Droits Spéciaux & Hardening
Le système de fichiers Linux utilise un contrôle d'accès discrétionnaire (DAC) fondé sur 3 triplets de bits (User, Group, Others) :

#### Droits Classiques en Notation Octale :
* `r` (Read / Lecture) = **4**
* `w` (Write / Écriture) = **2**
* `x` (Execute / Exécution ou Traversée de dossier) = **1**
* *Exemple d'Examen* : `chmod 750 fichier.sh` accorde `rwx` (7) au propriétaire, `r-x` (5) au groupe, et aucun accès `---` (0) aux tiers.

#### Droits Spéciaux Avancés (Obligatoires BTS CIEL) :
* **SUID (Set User ID - Valeur 4000)** : Appliqué à un exécutable, le programme s'exécute avec les privilèges du **propriétaire du fichier** (souvent root) et non avec ceux de l'utilisateur qui l'invoque (ex: `/usr/bin/passwd`). Noté avec un `s` à la place du `x` utilisateur (`-rwsr-xr-x`).
* **SGID (Set Group ID - Valeur 2000)** :
  * Sur un exécutable : s'exécute avec les privilèges du groupe propriétaire.
  * Sur un répertoire partagé : **tout nouveau fichier ou dossier créé hérite automatiquement du groupe propriétaire du dossier parent** (idéal pour le travail collaboratif).
* **Sticky Bit (Valeur 1000)** : Appliqué à un répertoire accessible en écriture à tous (ex: `/tmp`), **seul le propriétaire d'un fichier a le droit de le renommer ou de le supprimer**. Noté avec un `t` à la place du `x` pour Others (`drwxrwxrwt`).

#### Listes de Contrôle d'Accès (ACLs POSIX) :
Pour attribuer des permissions granulaires à un utilisateur spécifique sans modifier le propriétaire du fichier :
* `setfacl -m u:alice:rwx document.pdf` (attribue les droits rwx spécifiquement à Alice).
* `getfacl document.pdf` (affiche la liste détaillée des ACLs).
            """)
            
        with w2_sub2:
            st.markdown("#### 🗂️ Flashcards Réflexes Spécifiques à la Semaine 2")
            fc_s2 = [f for f in FLASHCARDS_DATA if f.get('module') in ['🔒 Cybersécurité', '🖥️ Administration Système']]
            for fc in fc_s2[:12]:
                with st.expander(f"📌 Carte N°{fc['id']} : {fc['q']}"):
                    st.markdown(f"**Réponse :** {fc['a']}")
                    st.info(f"{fc['note']}")
                    
        with w2_sub3:
            st.markdown("#### ✍️ Exercices Pratiques d'Application (Cyber & Linux)")
            st.write("1. Quel masque octal doit-on appliquer avec la commande `chmod` pour qu'un dossier partagé collaborativement `/data/projets` active le **SGID**, permette les pleins droits au propriétaire et au groupe (rwx), et interdise tout accès aux tiers ?")
            q_lx_oct = st.text_input("Masque octal (4 chiffres) :", placeholder="ex: 2770", key="w2_q_lx_oct")
            if st.button("Vérifier le masque SGID", key="w2_btn_check"):
                if q_lx_oct.strip() == "2770":
                    st.success("✅ **Parfait !** 2 (SGID) + 7 (User rwx) + 7 (Group rwx) + 0 (Others aucun droit) = 2770.")
                    add_user_points(15, "w2_chmod_sgid")
                else:
                    st.error("❌ Le chiffre des droits spéciaux est 2 pour le SGID. Le masque complet est 2770.")

        with w2_sub4:
            st.markdown("#### 📝 Questionnaire Certifiant de Fin de Semaine 2")
            render_10_questions_quiz("Cybersécurité", "w2_final_quiz")

    # =========================================================================
    # SEMAINE 3 : C++, PYTHON & SOCKETS
    # =========================================================================
    with tab_w3:
        st.subheader('🗓️ Semaine 3 : Programmation C++, Python & Réseaux')
        w3_sub1, w3_sub2, w3_sub3, w3_sub4 = st.tabs(['📚 Cours Magistral Approfondi S3', '🗂️ Flashcards S3', '✍️ Exercices Pratiques S3', '📝 Examen Blanc S3'])
        
        with w3_sub1:
            st.markdown(r"""
### 3.1 Gestion de la Mémoire en Langage C++ : Pile (*Stack*) vs Tas (*Heap*)
En C++, comprendre la structure de la mémoire vive allouée à un processus est indispensable pour concevoir des systèmes embarqués temps réel robustes.

```text
┌─────────────────────────────────────────────────────────┐
│        Mémoire Virtuelle d'un Processus C++             │
├──────────────────────────┬──────────────────────────────┤
│ 1. Segment de Code (Text)│ Instructions binaires CPU    │
├──────────────────────────┼──────────────────────────────┤
│ 2. Données Initialisées  │ Variables globales & statics │
├──────────────────────────┼──────────────────────────────┤
│ 3. Données Non-Init (BSS)│ Globales initialisées à zéro │
├──────────────────────────┼──────────────────────────────┤
│ 4. Le TAS (Heap)         │ Allocation dynamique         │
│    (Croît vers le haut)  │ `new` / `malloc`             │
├──────────────────────────┼──────────────────────────────┤
│           ▲              │                              │
│           │              │ Espace libre disponible      │
│           ▼              │                              │
├──────────────────────────┼──────────────────────────────┤
│ 5. La PILE (Stack)       │ Variables locales de fct     │
│    (Croît vers le bas)   │ Paramètres & adresses retour │
└──────────────────────────┴──────────────────────────────┘
```

#### Différences Clés :
* **La Pile (*Stack*)** : Gérée automatiquement par le processeur (registres de pointeur de pile ESP/RSP). Les variables locales sont allouées à l'entrée de la fonction et détruites immédiatement à la sortie du bloc `{}`. Ultra-rapide mais de taille limitée (typiquement 1 à 8 Mo ; risque de *Stack Overflow* en cas de récursion infinie).
* **Le Tas (*Heap*)** : Espace mémoire alloué dynamiquement à la demande du programmeur via `new` (ou `malloc`). La mémoire persiste tant qu'elle n'est pas explicitement libérée via `delete` (ou `free`). Si le programmeur oublie de libérer la mémoire, il se produit une **fuite de mémoire (*Memory Leak*)** qui sature la RAM.

#### Règle Fondamentale d'Examen (Session 2024) :
* Pour libérer un élément unique : `delete ptr;`
* Pour libérer un tableau dynamique : `delete[] ptr;` *(ne jamais omettre les crochets sous peine de comportement indéfini !)*

---

### 3.2 Principes de la Programmation Orientée Objet (POO en C++)
La POO repose sur 4 piliers fondamentaux :
1. **Encapsulation** : Regroupement des attributs (données privées `private`) et des méthodes associées au sein d'une même classe. L'accès aux attributs s'effectue exclusivement au moyen de méthodes publiques d'accès :
   * **Accesseurs (*Getters*)** : `float getTemperature() const { return temperature; }` (qualifié `const` pour garantir la non-modification de l'objet).
   * **Mutateurs (*Setters*)** : `void setTemperature(float t) { if(t > -50 && t < 150) temperature = t; }` (contrôle l'intégrité de la donnée avant affectation).
2. **Héritage** : Réutilisation et spécialisation des comportements d'une classe de base par une classe dérivée (`class CapteurTemperature : public Capteur`).
3. **Polymorphisme** : Capacité d'un pointeur ou d'une référence de classe de base à invoquer la méthode spécifique de l'objet dérivé pointé à l'exécution. Nécessite l'utilisation du mot-clé `virtual` sur les méthodes et obligatoirement sur le **destructeur** de la classe de base (`virtual ~Capteur();`).
4. **Classes Abstraites & Interfaces** :
   * Une méthode déclarée avec `= 0` est une **méthode virtuelle pure** : `virtual float lireValeur() = 0;`.
   * Une classe comportant au moins une méthode virtuelle pure est une **classe abstraite**. Elle ne peut pas être instanciée directement et impose à toutes ses classes filles d'implémenter concrètement cette méthode.

---

### 3.3 Communication Réseau par Sockets (Python & C++)
Une socket est l'interface logicielle permettant à deux processus de communiquer à travers le réseau via la combinaison d'une adresse IP et d'un port TCP ou UDP.

#### Implémentation d'un Serveur TCP Robuste en Python :
```python
import socket

HOST = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
PORT = 8080       # Port applicatif supérieur à 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)  # File d'attente maximale de connexions
    print(f"[*] Serveur TCP en attente sur le port {PORT}...")
    
    conn, addr = server.accept()
    with conn:
        print(f"[+] Connexion reçue de {addr}")
        data = conn.recv(1024)
        if data:
            message = data.decode('utf-8')
            print(f"Message reçu : {message}")
            conn.sendall(b"ACK_OK")
```
            """)

        with w3_sub2:
            st.markdown("#### 🗂️ Flashcards Réflexes Spécifiques à la Semaine 3")
            fc_s3 = [f for f in FLASHCARDS_DATA if f.get('module') == '💻 Programmation / Dev']
            for fc in fc_s3[:12]:
                with st.expander(f"📌 Carte N°{fc['id']} : {fc['q']}"):
                    st.markdown(f"**Réponse :** {fc['a']}")
                    st.info(f"{fc['note']}")

        with w3_sub3:
            st.markdown("#### ✍️ Exercices Pratiques de Code (C++ & Debugging)")
            st.code("""
// Corrigez la fuite mémoire dans le code ci-dessous :
void traitementSignal() {
    float* echantillons = new float[2048];
    // ... calculs numériques et FFT ...
    // Insérez ici l'instruction de libération mémoire :
}
            """, language="cpp")
            ans_cpp = st.text_input("Instruction de libération exacte :", placeholder="ex: delete ...", key="w3_code_ans")
            if st.button("Valider le code C++", key="w3_btn_code"):
                if ans_cpp.strip().replace(" ", "") == "delete[]echantillons;":
                    st.success("✅ **Code parfait !** L'opérateur `delete[]` libère la totalité du bloc de 2048 flottants alloués sur le tas.")
                    add_user_points(20, "w3_cpp_delete")
                else:
                    st.error("❌ Pour un tableau dynamique alloué avec `new float[...]`, l'instruction exacte est `delete[] echantillons;`.")

        with w3_sub4:
            st.markdown("#### 📝 Questionnaire Certifiant de Fin de Semaine 3")
            render_10_questions_quiz("Programmation", "w3_final_quiz")

    # =========================================================================
    # SEMAINE 4 : ÉLECTRONIQUE, SIGNAUX & MATHS
    # =========================================================================
    with tab_w4:
        st.subheader('🗓️ Semaine 4 : Électronique, Signaux, Bus Industriels & Mathématiques')
        w4_sub1, w4_sub2, w4_sub3, w4_sub4 = st.tabs(['📚 Cours Magistral Approfondi S4', '🗂️ Flashcards S4', '✍️ Exercices Pratiques S4', '📝 Examen Blanc S4'])
        
        with w4_sub1:
            st.markdown(r"""
### 4.1 Lois Fondamentales d'Électricité & Diviseurs
1. **Loi d'Ohm** :
   $$U = R \cdot I \quad \Leftrightarrow \quad I = G \cdot U \quad \left(G = \frac{1}{R} \text{ en Siemens } S\right)$$
2. **Loi des Nœuds (Loi des Courants de Kirchhoff)** :
   La somme algébrique des courants entrant dans un nœud est égale à la somme des courants qui en sortent :
   $$\sum I_{\text{entrants}} = \sum I_{\text{sortants}}$$
3. **Loi des Mailles (Loi des Tensions de Kirchhoff)** :
   La somme algébrique des tensions le long d'une maille orientée fermée est rigoureusement nulle :
   $$\sum U_k = 0$$
4. **Formule du Pont Diviseur de Tension (Incontournable)** :
   Pour deux résistances en série alimentées par une source $E$ :
   $$U_2 = E \cdot \frac{R_2}{R_1 + R_2}$$
   *Formule de réciprocité (pour isoler $R_2$ lors de l'étalonnage d'un capteur)* :
   $$R_2 = \frac{U_2 \cdot R_1}{E - U_2}$$
5. **Formule du Pont Diviseur de Courant** :
   Pour deux résistances en parallèle traversées par un courant total $I$ :
   $$I_1 = I \cdot \frac{R_2}{R_1 + R_2} = I \cdot \frac{G_1}{G_1 + G_2}$$

---

### 4.2 Traitement du Signal, CAN/CNA & Théorème de Shannon
* **Théorème d'échantillonnage de Nyquist-Shannon** : Pour pouvoir restituer fidèlement un signal analogique sans phénomène de repliement spectral (*Aliasing*), la fréquence d'échantillonnage $F_e$ doit être au moins égale au double de la fréquence maximale $F_{\text{max}}$ contenue dans le signal :
  $$F_e \ge 2 \cdot F_{\text{max}}$$
* **Résolution & Niveaux de Quantification** : Un convertisseur analogique-numérique (CAN / ADC) à $n$ bits offre $2^n$ états numériques distincts (de $0$ à $2^n - 1$).
* **Quantum ($q$)** : Plus petite variation de tension analogique mesurable :
  $$q = \frac{V_{\text{ref}}}{2^n - 1} \approx \frac{V_{\text{ref}}}{2^n}$$
* **Valeur Numérique Brute ($N$)** :
  $$N = \text{arrondi}\left(\frac{V_e}{q}\right) = \text{arrondi}\left(\frac{V_e \cdot (2^n - 1)}{V_{\text{ref}}}\right)$$

---

### 4.3 Bus de Terrain Industriels : Bus CAN & Modbus RTU sur RS-485
* **Bus CAN (Controller Area Network - ISO 11898)** :
  * Transmission différentielle sur deux fils : `CAN_H` (High) et `CAN_L` (Low).
  * **Niveau Récessif (Bit 1)** : $V_{\text{CAN\_H}} = V_{\text{CAN\_L}} \approx 2,5\text{ V} \Rightarrow V_{\text{diff}} = 0\text{ V}$.
  * **Niveau Dominant (Bit 0)** : $V_{\text{CAN\_H}} \approx 3,5\text{ V}$ et $V_{\text{CAN\_L}} \approx 1,5\text{ V} \Rightarrow V_{\text{diff}} \approx 2,0\text{ V}$.
  * Le bit dominant (0) écrase toujours le bit récessif (1) sur le bus, assurant l'arbitrage bit par bit non destructif (**CSMA/CR**).
  * Résistances de terminaison de ligne normalisées : **$120\ \Omega$** à chaque extrémité (impédance équivalente globale de $60\ \Omega$).
* **Protocole Modbus RTU sur Liaison RS-485** :
  * Architecture Maître/Esclave.
  * Structure d'une trame de lecture de registres (Fonction `03` - *Read Holding Registers*) :
    `[Adresse Esclave: 1 octet] [Code Fonction: 03] [Adresse de Début: 2 octets] [Nombre de Registres: 2 octets] [CRC-16: 2 octets]`.
            """)

        with w4_sub2:
            st.markdown("#### 🗂️ Flashcards Réflexes Spécifiques à la Semaine 4")
            fc_s4 = [f for f in FLASHCARDS_DATA if f.get('module') in ['🔌 Électronique & IoT', '📈 Mathématiques']]
            for fc in fc_s4[:12]:
                with st.expander(f"📌 Carte N°{fc['id']} : {fc['q']}"):
                    st.markdown(f"**Réponse :** {fc['a']}")
                    st.info(f"{fc['note']}")

        with w4_sub3:
            st.markdown("#### ✍️ Exercices Pratiques de Calcul Électronique")
            st.write("Un capteur analogique fournit une tension $V_e = 3,30\text{ V}$ à l'entrée d'un CAN 10 bits alimenté sous une tension de référence $V_{\text{ref}} = 5,00\text{ V}$.")
            ans_adc_n = st.text_input("Calculez la valeur numérique entière brute N correspondante :", placeholder="ex: 676", key="w4_adc_n_in")
            if st.button("Vérifier le calcul CAN", key="w4_btn_adc"):
                if ans_adc_n.strip() == "676":
                    st.success(r"✅ **Calcul parfait !** $q = 5,0 / 1023 \approx 0,004887\text{ V}$. $N = 3,30 / 0,004887 \approx 675,25 \Rightarrow 676$.")
                    add_user_points(15, "w4_adc_calc")
                else:
                    st.error("❌ Formule : $N = \text{arrondi}(3,30 \times 1023 / 5,0) = 676$.")

        with w4_sub4:
            st.markdown("#### 📝 Questionnaire Certifiant de Fin de Semaine 4")
            render_10_questions_quiz("Électronique", "w4_final_quiz")

    # =========================================================================
    # SEMAINE 5 : SYSML, UML & PROJET E6
    # =========================================================================
    with tab_w5:
        st.subheader('🗓️ Semaine 5 : Ingénierie Système SysML, UML & Conduite de Projet E6')
        w5_sub1, w5_sub2, w5_sub3, w5_sub4 = st.tabs(['📚 Cours Magistral Approfondi S5', '🗂️ Flashcards S5', '✍️ Exercices Pratiques S5', '📝 Examen Blanc S5'])
        
        with w5_sub1:
            st.markdown(r"""
### 5.1 Modélisation Système SysML (Épreuves E4 & E6)
Le langage **SysML (Systems Modeling Language)** modélise les systèmes cyber-physiques complexes selon 3 dimensions : Structurelle, Comportementale et Exigences.

#### 1. Diagramme de Définition de Blocs (BDD - Block Definition Diagram) :
* Décrit la hiérarchie structurelle et les types d'éléments du système.
* **Relations d'Association** :
  * **Composition (Losange plein noir $\blacklozenge$)** : Lien de possession forte. Les sous-blocs appartiennent exclusivement au bloc parent et leur cycle de vie est lié (la destruction du bloc conteneur entraîne la destruction des sous-composants).
  * **Agrégation (Losange vide blanc $\diamond$)** : Lien de possession faible. Le sous-composant peut exister de manière autonome hors du conteneur.
  * **Généralisation / Spécialisation (Flèche à triangle vide $\rightarrow$)** : Relation d'héritage entre un bloc générique et un bloc spécifique.

#### 2. Diagramme de Blocs Internes (IBD - Internal Block Diagram) :
* Représente l'architecture interne d'un bloc parent en affichant l'interconnexion de ses parties (*parts*) à travers leurs **ports**.
* **Ports Standards** : Points d'accès pour les flux de données ou signaux logiques.
* **Ports de Flux (*Flow Ports*)** : Spécifient la nature et la direction des flux physiques échangés (énergie électrique, flux thermique, fluide, matière).

#### 3. Diagramme des Exigences (*Requirement Diagram*) :
* Formalise le Cahier des Charges Fonctionnel (CdCf).
* Relations normées :
  * `<<deriveReqt>>` : Une exigence technique de bas niveau dérive d'une exigence système de haut niveau.
  * `<<satisfy>>` : Un bloc matériel ou logiciel satisfait une exigence.
  * `<<verify>>` : Un cas de test formalisé dans le **PVL** vérifie la satisfaction d'une exigence.

---

### 5.2 Modélisation Logicielle UML (Unified Modeling Language)
* **Diagramme de Cas d'Utilisation (*Use Case Diagram*)** : Décrit les interactions fonctionnelles entre les acteurs externes (utilisateurs, systèmes tiers) et le système délimité par sa frontière. Relations `<<include>>` (obligatoire) et `<<extend>>` (optionnelle conditionnelle).
* **Diagramme de Séquence** : Représente le déroulement chronologique des échanges de messages entre lignes de vie d'objets. Flèche pleine pour un appel synchrone bloquant, flèche ouverte pour un message asynchrone, ligne pointillée pour le retour. Fragments combinés : `alt` (alternative conditionnelle Si/Sinon), `loop` (boucle d'itération), `opt` (optionnel).
* **Diagramme d'États-Transitions** : Modélise le cycle de vie d'un objet réactif. Une transition est définie par :
  $$\text{Événement Déclencheur } [\text{ Condition de Garde }] \ / \ \text{Action Exécutée}$$

---

### 5.3 Cahier des Charges (CdCf) & Plan de Validation Logicielle (PVL)
* **Norme AFNOR NF X50-151** : Caractérisation des fonctions par Critères d'appréciation, Niveaux et degrés de **Flexibilité** :
  * **F0 (Inflexible)** : Niveau impératif strict (ex: alimentation $24\text{ V DC} \pm 5\%$).
  * **F1 (Peu flexible)** : Tolérance faible acceptable.
  * **F2 (Moyennement flexible)** : Négociable si justification technique.
  * **F3 (Très flexible)** : Simple ordre de grandeur indicatif.
* **Le Plan de Validation Logicielle (PVL)** : Document pivot de l'épreuve E6. Chaque fiche de test doit impérativement préciser :
  * Identifiant du test & Référence de l'exigence vérifiée.
  * Conditions initiales & Procédure de test détaillée.
  * Résultat attendu observable et Critère de succès (**PASS / FAIL**).
            """)

        with w5_sub2:
            st.markdown("#### 🗂️ Flashcards Réflexes Spécifiques à la Semaine 5")
            fc_s5 = [f for f in FLASHCARDS_DATA if f.get('module') == '📐 Modélisation UML & SysML']
            for fc in fc_s5[:12]:
                with st.expander(f"📌 Carte N°{fc['id']} : {fc['q']}"):
                    st.markdown(f"**Réponse :** {fc['a']}")
                    st.info(f"{fc['note']}")

        with w5_sub3:
            st.markdown("#### ✍️ Exercices Pratiques de Conception SysML / E6")
            st.write("Dans un diagramme des exigences SysML, quelle relation normalisée relie un cas de test ou une procédure de qualification du PVL à l'exigence fonctionnelle qu'elle contrôle ?")
            rel_sysml = st.radio("Relation SysML :", ["<<satisfy>>", "<<verify>>", "<<deriveReqt>>", "<<refine>>"], key="w5_rel_sysml")
            if st.button("Vérifier la relation SysML", key="w5_btn_sysml"):
                if rel_sysml == "<<verify>>":
                    st.success("✅ **Exact !** La relation `<<verify>>` établit la traçabilité entre la campagne de test et l'exigence du CdCf.")
                    add_user_points(15, "w5_sysml_verify")
                else:
                    st.error("❌ C'est la relation `<<verify>>` qui lie les tests de qualification aux exigences. `<<satisfy>>` est utilisée pour les blocs de conception.")

        with w5_sub4:
            st.markdown("#### 📝 Questionnaire Certifiant de Fin de Semaine 5")
            render_10_questions_quiz("Modélisation", "w5_final_quiz")

    # =========================================================================
    # SEMAINE 6 : ANNALES 2024-2026 & SYNTHÈSE TOTALE
    # =========================================================================
    with tab_w6:
        st.subheader('🗓️ Semaine 6 : Annales Officielles 2024-2026 & Marathon d\'Examen')
        w6_sub1, w6_sub2, w6_sub3, w6_sub4 = st.tabs(['📚 Synthèse des Sujets E4 Réels', '🗂️ Flashcards Stratégiques', '✍️ Exercices Types Corrigés', '📝 Grand Marathon d\'Examen'])
        
        with w6_sub1:
            st.markdown(r"""
### 6.1 Bilan des Sujets d'Épreuves Écrites E4 Récentes (Sessions 2024 à 2026)
L'épreuve E4 dure **6 heures** (Coefficient 4) : 4h30 pour la partie Informatique & Réseaux (70 points) et 1h30 pour la partie Sciences Physiques (30 points).

#### 1. Session 2026 (CISS Cashless Online - Métropole) :
* **Informatique** : Architecture de paiement sans contact NFC (ISO/IEC 14443 à $13,56\text{ MHz}$), chiffrement AES-128 du porte-monnaie électronique, API REST HTTPS (`/api/v1/transaction`) avec jetons JWT Bearer, mode déconnecté avec base SQLite locale et synchronisation différée (*Store & Forward*).
* **Physique** : Dimensionnement de l'antenne résonante NFC ($f_0 = \frac{1}{2\pi\sqrt{LC}} = 13,56\text{ MHz}$), conditionnement des signaux de capteurs débitmètres pour tireuses connectées.

#### 2. Session 2025 (Seven-Park Parking Multi-Niveaux - Métropole) :
* **Informatique** : Découpage VLSM en `/20` du réseau d'entreprise (`172.20.0.0/16`), redirection de ports DNAT (ports 80/443 vers le serveur web interne `172.20.7.1`), calcul d'Interface-ID IPv6 EUI-64 à partir d'une adresse MAC.
* **Physique** : Détection de véhicules par boucle inductive au sol (variation d'inductance $\Delta L$), liaison série différentielle RS-485 / Modbus RTU avec terminaison de ligne $120\ \Omega$.

#### 3. Session 2024 (Surveillance Environnementale de l'Eau - Option A) :
* **Informatique** : Modélisation en C++ de la classe `GestionStation`, compression du payload LoRaWAN (passage de 5 octets ASCII à 2 octets en entier non signé hexadécimal).
* **Physique** : Bilan de liaison radiofréquence 868 MHz ($P_{\text{RX}} = -89\text{ dBm}$, sensibilité $-140\text{ dBm} \Rightarrow$ marge confortable de $+51\text{ dB}$), conformité avec le temps d'occupation spectral (*Duty Cycle* $\alpha = 0,41\% \le 1\%$).
            """)

        with w6_sub2:
            st.markdown("#### 🗂️ Flashcards Stratégiques Synthèse & Pièges d'Examen")
            for fc in FLASHCARDS_DATA[12:24]:
                with st.expander(f"📌 Carte N°{fc['id']} ({fc['module']}) : {fc['q']}"):
                    st.markdown(f"**Réponse :** {fc['a']}")
                    st.info(f"{fc['note']}")

        with w6_sub3:
            st.markdown("#### ✍️ Cas Pratique d'Examen : Bilan de Liaison Radio LoRaWAN")
            st.markdown(r"""
Une sonde de mesure transmet sur la bande européenne ISM $868\text{ MHz}$ avec une puissance d'émission $P_{\text{TX}} = +14\text{ dBm}$. 
L'atténuation en espace libre calculée pour la distance de liaison est $A_{\text{FSPL}} = 105\text{ dB}$. Les gains des antennes d'émission et de réception sont $G_{\text{TX}} = +2\text{ dBi}$ et $G_{\text{RX}} = +3\text{ dBi}$, et les pertes dans les câbles s'élèvent à $2\text{ dB}$ au total.
            """)
            st.write("Quelle est la puissance reçue $P_{\text{RX}}$ au niveau de la passerelle de réception ?")
            ans_prx = st.text_input("Puissance reçue en dBm :", placeholder="ex: -88", key="w6_ans_prx")
            if st.button("Vérifier le bilan de liaison", key="w6_btn_prx"):
                if ans_prx.strip() == "-88":
                    st.success("✅ **Calcul parfait !** $P_{\\text{RX}} = P_{\\text{TX}} + G_{\\text{TX}} + G_{\\text{RX}} - A_{\\text{FSPL}} - \\text{Pertes} = 14 + 2 + 3 - 105 - 2 = \\mathbf{-88\\text{ dBm}}$.")
                    add_user_points(20, "w6_lora_calc")
                else:
                    st.error("❌ Formule : $P_{\\text{RX}} = 14 + 2 + 3 - 105 - 2 = -88\\text{ dBm}$.")

        with w6_sub4:
            st.markdown("#### 📝 Marathon Final : Questionnaire de Synthèse Épreuve E4")
            render_10_questions_quiz("Réseaux", "w6_marathon_quiz")


elif page == '🎯 Révision Totale BTS Blanc (9-11 Déc)':
    st.markdown("<div class='hero-title'>🎯 Hub de Révision Totale - BTS Blanc (9, 10 & 11 Décembre)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Centrale de préparation intensive regroupant l'intégralité des cours, TP, annales et fiches de synthèse du notebook</p>", unsafe_allow_html=True)
    st.markdown("\n    <div class='ciel-card' style='border-left: 6px solid #f59e0b !important; background: #fffbeb;'>\n        <h3 style='color: #b45309; margin-top: 0;'>🚨 Objectif Échéance : Examens du 9, 10 et 11 Décembre 2026</h3>\n        <p style='color: #78350f;'>Ce hub rassemble <b>l'ensemble des 61 sources et TPs</b> déposés dans votre notebook pour une révision transversale sans aucune impasse.</p>\n    </div>", unsafe_allow_html=True)
    tab_tot1, tab_tot2, tab_tot3 = st.tabs(['📚 Synthèse Exhaustive des 6 Piliers', '🛠️ Récapitulatif des TP de Réseau & SysAdmin', "📝 Générateur d'Examen Blanc Multi-Matières"])
    with tab_tot1:
        st.subheader('Synthèse Globale du Programme Officiel')
        st.markdown("\n        #### 1. 📶 Réseaux, Telecommunications & Commutation\n        * **Modèle OSI / TCP-IP** : 7 couches OSI (PDU: Bit, Trame, Paquet, Segment, Donnée).\n        * **Adressage IPv4 / IPv6 & VLSM** : Masques CIDR (`/24` à `/30`), calculs de réseau/broadcast, adresses IPv6 (128 bits, SLAAC, NDP).\n        * **VLANs & Trunking 802.1Q** : Tag 4 octets, VLAN natif, routage inter-VLAN (*Router-on-a-Stick*).\n        * **Routage** : Statique (`ip route 0.0.0.0 0.0.0.0`), dynamique OSPF (Aires/Areas, état de lien).\n        * **Services Infrastructure** : DHCP (DORA), DNS (`A`, `AAAA`, `CNAME`, `MX`, `PTR`), NAT/PAT.\n        * **Fibre Optique & RS485** : Réflexion totale interne, Snell-Descartes $\\sin(i_{\\text{limite}}) = \\frac{n_2}{n_1}$, Monomode (9 µm) vs Multimode, Modbus RTU (Function Code `03`).\n\n        #### 2. 🔒 Cybersécurité, EBIOS RM & RGPD\n        * **Cryptographie** : Chiffrement Symétrique (AES-128/256), Asymétrique (RSA, bi-clés), Hachage (SHA-256).\n        * **Sécurité Applicative** : Top 10 OWASP (Injections SQL via requêtes préparées, XSS, CSRF).\n        * **Sécurité Réseau & Système** : Cisco Port Security (`protect`, `restrict`, `shutdown`), UFW/IPTables, Tunnels VPN (IPsec L3 vs TLS L4), MQTTS.\n        * **Méthodologie EBIOS RM (5 Ateliers)** : 1. Cadrage & Valeurs métiers $\\rightarrow$ 2. Sources de risque (SR/OV) $\\rightarrow$ 3. Scénarios stratégiques $\\rightarrow$ 4. Scénarios opérationnels $\\rightarrow$ 5. Traitement du risque.\n        * **RGPD & PIA** : Privacy Impact Assessment (Art. 35 RGPD, principes de minimisation et de base légale).\n\n        #### 3. 💻 Développement Software (C, C++, Python & Git)\n        * **Gestion Mémoire C/C++** : Pile (Stack) vs Tas (Heap), allocation dynamique (`new[]`/`delete[]`), pointeurs bruts, références, fuites mémoire.\n        * **Langage C** : Directives préprocesseur (`#define`, `#include`), structures (`struct`), unions (`union` à mémoire partagée), masquage de bits (`& 0x04`).\n        * **POO C++** : Encapsulation (`private`/`protected`/`public`), héritage, polymorphisme, destructeurs virtuels, classes abstraites (`virtual void f() = 0;`), STL (`std::vector`, `std::thread`, `std::mutex`).\n        * **Python Réseau** : Sockets client/serveur TCP/UDP, traitement HTTP/JSON.\n\n        #### 4. 🖥️ Administration Système (Debian & Active Directory)\n        * **Linux Debian** : Permissions octales `chmod` (`755`, `750`), SUID (4000), SGID (2000), Sticky Bit (1000), ACLs (`getfacl`/`setfacl`), `systemd`, `bash` redirection (`>`, `>>`, `|`).\n        * **Windows Server Active Directory** : Forêt, Domaine, Unités d'Organisation (OU), GPO (Ordre LSDOU), rôles ADDS, DNS, DHCP.\n\n        #### 5. 🔌 Électronique, Signaux & Bus\n        * **Fiches Savoir & Montages** :\n          - *Pont en H (Fiche Savoir N°1 & Fiche Montage N°1)* : Pilotage de sens de moteurs CC. Sécurité : ne jamais fermer les deux bras parallèles simultanément.\n          - *Pull-Up & Pull-Down (Fiche Savoir N°2)* : Fixation de potentiel $10\\text{ k}\\Omega$ anti-parasites sur entrées CMOS.\n          - *PWM / MLI (Fiche Savoir N°3)* : $V_{\\text{moy}} = V_{\\text{max}} \\cdot \\alpha$. Pins 3, 5, 6, 9, 10, 11 (490/980 Hz).\n          - *Interruptions & Registres (Fiche Savoir N°4)* : `attachInterrupt()`, registres `DDRB/C/D` bit-à-bit (`DDRD |= (1 << PD3)`).\n          - *Mémoire ATmega328P (Fiche Savoir N°5)* : Flash 32 Ko, SRAM 2 Ko (Pile/Tas), EEPROM 1 Ko.\n          - *Signal 4-20 mA (Fiche Savoir N°6)* : Boucle de courant linéaire $I(T) = 4 + \\frac{T-T_{\\text{min}}}{T_{\\text{max}}-T_{\\text{min}}} \\cdot 16\\text{ mA}$. $0\\text{ mA} = \\text{rupture de ligne}$.\n          - *Relais & Isolation (Fiche Savoir N°8 & Fiche Montage N°2)* : Isolation galvanique 5V/230V, contacts COM/NO/NC.\n          - *Bauds vs bps (Fiche Savoir N°9)* : $D = R \\cdot \\log_2(M)$.\n          - *XON/XOFF & RTS/CTS (Fiche Savoir N°10)* : Contrôle de flux logiciel (`0x11` / `0x13`) et matériel anti-débordement de buffer.\n        * **Lois Générales** : Loi d'Ohm ($U = R \\cdot I$), Lois de Kirchhoff (Nœuds, Mailles), Pont diviseur de tension ($S = E \\cdot \\frac{R_2}{R_1 + R_2}$).\n        * **Signaux & Numérisation** : $V_{pp}, V_{max}, V_{eff} = \\frac{V_{max}}{\\sqrt{2}}$, $f = \\frac{1}{T}$, Théorème de Nyquist-Shannon ($Fe \\ge 2 F_{max}$).\n        * **CAN / CNA** : Résolution $n$ bits, Quantum $q = \\frac{V_{ref}}{2^n - 1}$, valeur brute $N = \\text{arrondi}\\left(\\frac{V_e}{q}\\right)$.\n        * **Bus de Terrain** : I2C (SDA, SCL), SPI (MOSI, MISO, SCLK, CS), UART, Bus CAN (CAN_H, CAN_L, arbitrage CSMA/CR, bit dominant 0 / récessif 1).\n\n        #### 6. 📐 Modélisation UML/SysML & Anglais\n        * **SysML** : BDD (Block Definition Diagram), IBD (Internal Block Diagram, ports `[p_spi]`, `[p_i2c]`), Requirement Diagram.\n        * **UML** : Classes (Agrégation ◇ vs Composition ◆), Séquence, États-Transitions.\n        * **Anglais Technique** : Conditionnels (1st, 2nd, 3rd conditionals) et communication d'incidents IT.")
    with tab_tot2:
        st.subheader('🛠️ Index des Travaux Pratiques (TPs) du Notebook')
        st.markdown("\n        * **TP00 Debian & VMware** : Virtualisation sous VMware Workstation Pro 17, installation ISO Debian 12 `deb-srv`.\n        * **TP01 Linux Commandes** : Navigation FHS (`/etc`, `/var`, `/home`), `cat`, `less`, `cp`, `mv`, `mkdir -p`.\n        * **TP01 à TP07 ADDS / DNS / DHCP** : Installation du rôle ADDS sous Windows Server, création de domaines, structuration en OUs (Direction, Production, R&D), groupes GG/DL, déploiement de GPO et DHCP/DNS.\n        * **TP06 DL ACL** : Gestion des droits d'accès avancés (Domain Local Groups + ACLs sur dossiers partagés).\n        * **TP3 Matrice des Flux** : Configuration pfSense Firewall (LAN 192.168.80.x, DMZ 192.168.90.x, WAN NAT), règles de filtrage.\n        * **TP6.1 & TP6.2 Scripts Bash** : Automation d'administration système, création d'utilisateurs en masse via fichiers CSV, configuration Samba SMB et sudoers.")
    with tab_tot3:
        st.subheader('📝 Examen Blanc Global de Synthèse (Mise en Situation Réaliste)')
        st.info("Ce test génère une épreuve de synthèse tirant au sort des questions d'examen sur les 6 blocs du BTS CIEL Blanc.")
        if st.button('🚀 Lancer un Sujet Blanc Complet (12 Questions Multi-Matières)', type='primary', key='btn_run_bts_blanc'):
            st.session_state.bts_blanc_active = True
        if st.session_state.get('bts_blanc_active', False):
            st.success('Exam Blanc en cours. Répondez aux questions ci-dessous :')
            st.markdown('---')
            q_b1 = st.radio("1. Réseaux : Quelle est la taille du tag inséré dans l'en-tête Ethernet par le protocole IEEE 802.1Q ?", ['2 octets', '4 octets', '8 octets', '12 bits'], key='qb1')
            q_b2 = st.radio('2. Cybersécurité : Quelle méthode prémunit définitivement contre les injections SQL ?', ["Filtrage d'expressions régulières", 'Requêtes préparées (paramétrées)', 'Chiffrement AES de la BDD', 'Désactivation du port 3306'], key='qb2')
            q_b3 = st.radio('3. C++ : Quel opérateur doit être utilisé pour libérer la mémoire de `int* tab = new int[100];` ?', ['delete tab;', 'free(tab);', 'delete[] tab;', 'clear(tab);'], key='qb3')
            q_b4 = st.radio('4. SysAdmin : Quelle est la valeur octale chmod pour rwx (User), r-x (Group), --- (Others) ?', ['755', '750', '644', '777'], key='qb4')
            q_b5 = st.radio("5. Électronique : Quel est le quantum d'un CAN 12 bits sous Vref = 5.0 V ?", ['1.22 mV', '4.88 mV', '0.50 mV', '2.44 mV'], key='qb5')
            q_b6 = st.radio('6. Mathématiques : Si un signal Wi-Fi perd 15% de puissance par mètre, quelle est la raison $q$ de la suite géométrique ?', ['q = 0.15', 'q = 0.85', 'q = 1.15', 'q = -0.15'], key='qb6')
            if st.button('Soumettre mon Sujet Blanc', key='btn_sub_bts_blanc'):
                score_b = 0
                if q_b1 == '4 octets':
                    score_b += 1
                if q_b2 == 'Requêtes préparées (paramétrées)':
                    score_b += 1
                if q_b3 == 'delete[] tab;':
                    score_b += 1
                if q_b4 == '750':
                    score_b += 1
                if q_b5 == '1.22 mV':
                    score_b += 1
                if q_b6 == 'q = 0.85':
                    score_b += 1
                st.markdown(f'### 📊 Note finale Sujet Blanc : **{score_b} / 6** ({score_b / 6.0 * 20:.1f} / 20)')
                if score_b >= 5:
                    st.balloons()
                    st.success('🏆 **Très bon niveau !** Vous êtes prêt pour le BTS Blanc des 9, 10 et 11 Décembre !')
                else:
                    st.warning('⚠️ Des révisions sont nécessaires. Consultez les onglets thématiques ci-dessus.')



elif page == '📈 Mathématiques : Fonctions, Exponentielle & Logarithme':
    st.markdown("<div class='hero-title'>📈 Mathématiques Appliquées : Fonctions de Référence, $e^x$ & $\\ln(x)$</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Cours magistral, propriétés algébriques, dérivation, calculs de décibels, charge $RC$ et simulateurs interactifs</p>", unsafe_allow_html=True)
    tab_exp1, tab_exp2, tab_exp3, tab_exp4 = st.tabs(['📖 Cours, Formules & Propriétés Clés', '🧮 Traceur Interactif & Simulateurs (RC, dB)', '🐍 Traduction Algorithmique & Python', '✍️ Exercices Pratiques & Mini-Quiz'])
    with tab_exp1:
        st.subheader('1. Tableau Synthétique des Fonctions de Référence')
        st.markdown("\n        | Fonction $f(x)$ | Domaine $\\\\mathcal{D}_f$ | Dérivée $f'(x)$ | Limites aux Bornes | Sens de Variation |\n        | :--- | :--- | :--- | :--- | :--- |\n        | **Affine** : $a x + b$ | $\\mathbb{R}$ | $a$ | $\\pm \\infty$ selon le signe de $a$ | Stricte si $a \\neq 0$ (croissante si $a>0$) |\n        | **Carré** : $x^2$ | $\\mathbb{R}$ | $2x$ | $\\lim_{x \\to \\pm \\infty} x^2 = +\\infty$ | Décroissante sur $]-\\infty; 0]$, Croissante sur $[0; +\\infty[$ |\n        | **Cube** : $x^3$ | $\\mathbb{R}$ | $3x^2$ | $\\lim_{x \\to \\pm \\infty} x^3 = \\pm \\infty$ | Strictement croissante sur $\\mathbb{R}$ |\n        | **Racine** : $\\sqrt{x}$ | $[0 ; +\\infty[$ | $\\frac{1}{2\\sqrt{x}}$ sur $]0; +\\infty[$ | $\\lim_{x \\to +\\infty} \\sqrt{x} = +\\infty$ | Strictement croissante sur $[0 ; +\\infty[$ |\n        | **Inverse** : $\\frac{1}{x}$ | $\\mathbb{R}^*$ | $-\\frac{1}{x^2}$ | $\\lim_{x \\to \\pm \\infty} \\frac{1}{x} = 0$, $\\lim_{x \\to 0^0} \\frac{1}{x} = \\pm \\infty$ | Strictement décroissante sur $]-\\infty; 0[$ et $]0; +\\infty[$ |\n        | **Exponentielle** : $e^x$ | $\\mathbb{R}$ | $e^x$ | $\\lim_{x \\to -\\infty} e^x = 0$, $\\lim_{x \\to +\\infty} e^x = +\\infty$ | Strictement croissante sur $\\mathbb{R}$ |\n        | **Logarithme** : $\\ln(x)$ | $]0 ; +\\infty[$ | $\\frac{1}{x}$ | $\\lim_{x \\to 0^+} \\ln(x) = -\\infty$, $\\lim_{x \\to +\\infty} \\ln(x) = +\\infty$ | Strictement croissante sur $]0 ; +\\infty[$ |")
        st.markdown('---')
        st.subheader('2. La Fonction Exponentielle ($f(x) = e^x$)')
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.markdown('\n            #### 📌 Propriétés Fondamentales :\n            * **Réciproque** : $e^x$ est la fonction réciproque du logarithme népérien $\\ln(x)$.\n            * **Stricte Positivité** : Pour tout $x \\in \\mathbb{R}$, **$e^x > 0$**.\n            * **Valeurs remarquables** : $e^0 = 1$, $e^1 = e \\approx 2,71828$.\n            * **Propriétés Algébriques** :\n              * $e^{a+b} = e^a \\cdot e^b$\n              * $e^{-a} = \\frac{1}{e^a}$\n              * $e^{a-b} = \\frac{e^a}{e^b}$\n              * $(e^a)^b = e^{a \\cdot b}$')
        with col_e2:
            st.markdown("\n            #### 📐 Dérivée & Croissances Comparées :\n            * **Dérivée simple** : $(e^x)' = e^x$.\n            * **Dérivée composée** : $(e^{u(x)})' = u'(x) \\cdot e^{u(x)}$.\n            * **Croissance comparée à $+\\infty$** : L'exponentielle l'emporte sur toute puissance polynomiale :\n              $$\\lim_{x \\to +\\infty} \\frac{e^x}{x^n} = +\\infty \\quad (n > 0)$$\n              $$\\lim_{x \\to -\\infty} x^n e^x = 0$$")
        st.info("💡 **Application BTS CIEL** : Modélisation de la charge et décharge d'un condensateur de capacité $C$ à travers une résistance $R$ : $u_C(t) = E (1 - e^{-t/\\tau})$ avec la constante de temps $tau = R \\cdot C$.")
        st.markdown('---')
        st.subheader('3. La Fonction Logarithme Népérien ($f(x) = \\ln(x)$)')
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.markdown("\n            #### 📌 Propriétés Fondamentales :\n            * **Domaine de définition** : Strictement définie sur **$]0 ; +\\infty[$**.\n            * **Relations d'inversion** :\n              * $e^{\\ln(x)} = x$ pour tout $x > 0$.\n              * $\\ln(e^x) = x$ pour tout $x \\in \\mathbb{R}$.\n            * **Valeurs remarquables** : $\\ln(1) = 0$, $\\ln(e) = 1$.\n            * **Propriétés Algébriques** (Transformation de produit en somme) :\n              * $\\ln(a \\cdot b) = \\ln(a) + \\ln(b)$\n              * $\\ln(\\frac{1}{a}) = -\\ln(a)$\n              * $\\ln(\\frac{a}{b}) = \\ln(a) - \\ln(b)$\n              * $\\ln(a^k) = k \\cdot \\ln(a)$\n              * $\\ln(\\sqrt{a}) = \\frac{1}{2} \\ln(a)$")
        with col_l2:
            st.markdown("\n            #### 📐 Dérivée & Atténuation en Décibels :\n            * **Dérivée simple** : $(\\ln(x))' = \\frac{1}{x}$ sur $]0 ; +\\infty[$.\n            * **Dérivée composée** : $(\\ln(u(x)))' = \\frac{u'(x)}{u(x)}$ (pour $u(x) > 0$).\n            * **Relation avec le Logarithme Décimal ($\\log_{10}$)** :\n              $$\\log_{10}(x) = \\frac{\\ln(x)}{\\ln(10)}$$\n            * **Gain / Atténuation en Décibels (dB)** :\n              $$A_{dB} = 10 \\log_{10}\\left(\\frac{P_2}{P_1}\\right) = 20 \\log_{10}\\left(\\frac{V_2}{V_1}\\right)$$")
        st.markdown('---')
        st.subheader("4. Méthodologie : Résolution d'Équations & Inéquations")
        st.markdown("\n        * **Type $e^{u(x)} = k$** :\n          * Si $k \\le 0$ : Impossible (pas de solution car $e^y > 0$).\n          * Si $k > 0$ : Appliquer $\\ln \\Rightarrow u(x) = \\ln(k)$.\n        * **Type $\\ln(u(x)) = k$** :\n          * Vérifier la condition d'existence $u(x) > 0$.\n          * Appliquer l'exponentielle $\\Rightarrow u(x) = e^k$.")
    with tab_exp2:
        st.subheader('🧮 Traceur & Simulateur Interactif')
        sim_choice = st.selectbox("Sélectionnez le module d'expérimentation :", ['⚡ Charge & Décharge de Condensateur RC', '📡 Calculateur de Gain / Atténuation en Décibels', "🔍 Résolveur d'Équations Exponentielles & Logarithmiques"])
        if sim_choice == '⚡ Charge & Décharge de Condensateur RC':
            col_rc1, col_rc2, col_rc3 = st.columns(3)
            with col_rc1:
                val_E = st.number_input("Tension d'alimentation $E$ (V) :", min_value=1.0, max_value=48.0, value=5.0, step=1.0)
            with col_rc2:
                val_R = st.number_input('Résistance $R$ ($k\\Omega$) :', min_value=0.1, max_value=500.0, value=10.0, step=1.0)
            with col_rc3:
                val_C = st.number_input('Capacité $C$ ($\\mu F$) :', min_value=0.1, max_value=1000.0, value=100.0, step=10.0)
            tau_ms = val_R * 1000.0 * (val_C * 1e-06) * 1000.0
            st.success(f'⚡ **Constante de temps calculée** : $tau = R \\cdot C = {val_R}\\text{{ k}}\\Omega \\times {val_C}\\mu\\text{{F}} = \\mathbf{{{tau_ms:.2f}\\text{{ ms}}}}$')
            import matplotlib.pyplot as plt
            import numpy as np
            t = np.linspace(0, 5 * tau_ms, 500)
            u_charge = val_E * (1 - np.exp(-t / tau_ms))
            u_decharge = val_E * np.exp(-t / tau_ms)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(t, u_charge, label='Charge : $u_C(t) = E(1 - e^{-t/\\tau})$', color='#2563eb', linewidth=2.5)
            ax.plot(t, u_decharge, label='Décharge : $u_C(t) = E e^{-t/\\tau}$', color='#dc2626', linestyle='--', linewidth=2)
            ax.axvline(x=tau_ms, color='#10b981', linestyle=':', label=f'tau = {tau_ms:.1f} ms')
            ax.axhline(y=0.632 * val_E, color='#10b981', linestyle=':', alpha=0.7)
            ax.scatter([tau_ms], [0.632 * val_E], color='#10b981', s=60, zorder=5)
            ax.annotate(f'63.2% ({0.632 * val_E:.2f}V)', (tau_ms, 0.632 * val_E), textcoords='offset points', xytext=(10, -10), fontweight='bold', color='#047857')
            ax.set_title(f'Charge et Décharge RC (E = {val_E}V, tau = {tau_ms:.2f} ms)', fontsize=12, fontweight='bold', color='#1e293b')
            ax.set_xlabel('Temps t (ms)', fontsize=10)
            ax.set_ylabel('Tension uC (V)', fontsize=10)
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.legend(loc='center right')
            plt.tight_layout()
            st.pyplot(fig)
            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.info(f'**À t = tau ({tau_ms:.2f} ms)** : Charge à **63.2%** -> {0.632 * val_E:.2f} V')
            with col_m2:
                st.info(f'**À t = 3*tau ({3 * tau_ms:.2f} ms)** : Charge à **95.0%** -> {0.95 * val_E:.2f} V')
            with col_m3:
                st.info(f'**À t = 5*tau ({5 * tau_ms:.2f} ms)** : Régime permanent **99.3%** -> {0.993 * val_E:.2f} V')
        elif sim_choice == '📡 Calculateur de Gain / Atténuation en Décibels':
            st.markdown('#### Calcul de la variation en dB ($A_{dB} = 10 \\log_{10}(P_2 / P_1)$)')
            col_db1, col_db2 = st.columns(2)
            with col_db1:
                p_in = st.number_input("Puissance d'entrée $P_1$ (mW) :", min_value=0.001, value=100.0, step=10.0)
                p_out = st.number_input('Puissance de sortie $P_2$ (mW) :', min_value=0.001, value=10.0, step=1.0)
                gain_db = 10 * np.log10(p_out / p_in)
                if gain_db < 0:
                    st.warning(f'📉 **Atténuation du signal** : $A_{{dB}} = \\mathbf{{{gain_db:.2f}\\text{{ dB}}}}$')
                else:
                    st.success(f"📈 **Gain d'amplification** : $G_{{dB}} = \\mathbf{{{gain_db:.2f}\\text{{ dB}}}}$")
            with col_db2:
                v_in = st.number_input("Tension d'entrée $V_1$ (V) :", min_value=0.001, value=5.0, step=0.5)
                v_out = st.number_input('Tension de sortie $V_2$ (V) :', min_value=0.001, value=2.5, step=0.5)
                gain_v_db = 20 * np.log10(v_out / v_in)
                st.info(f'🔌 **Variation de tension** : $A_{{v, dB}} = 20 \\log_{{10}}(\\frac{{{v_out}}}{{{v_in}}}) = \\mathbf{{{gain_v_db:.2f}\\text{{ dB}}}}$')
        elif sim_choice == "🔍 Résolveur d'Équations Exponentielles & Logarithmiques":
            st.markdown("#### Résolveur de l'équation $A e^{k x} = B$")
            col_eq1, col_eq2, col_eq3 = st.columns(3)
            with col_eq1:
                param_A = st.number_input('Paramètre $A$ :', value=2.0, step=0.5)
            with col_eq2:
                param_k = st.number_input('Paramètre $k$ :', value=-0.5, step=0.1)
            with col_eq3:
                param_B = st.number_input('Résultat $B$ :', value=1.0, step=0.5)
            if param_A == 0 or param_k == 0:
                st.error('Les paramètres A et k doivent être non nuls.')
            else:
                ratio = param_B / param_A
                if ratio <= 0:
                    st.error(f'Impossible : e^({param_k} x) = {ratio:.2f} <= 0. Une exponentielle est toujours strictement positive !')
                else:
                    sol_x = np.log(ratio) / param_k
                    st.success(f"🎯 **Solution de l'équation** : x = **{sol_x:.4f}** (car {param_k}*x = ln({ratio:.4f}))")
    with tab_exp3:
        st.subheader('🐍 Implémentation Algorithmique en Python')
        st.markdown('\n        En Python, la bibliothèque standard `math` fournit les fonctions `math.exp(x)` et `math.log(x)` (logarithme népérien).\n        Pour le logarithme décimal, on utilise `math.log10(x)`.')
        st.code('import math\n\n# 1. Calcul de la charge d\'un condensateur u_C(t) = E * (1 - exp(-t / tau))\ndef tension_charge_rc(E, R, C, t):\n    tau = R * C\n    return E * (1 - math.exp(-t / tau))\n\n# 2. Recherche du temps t requis pour atteindre une tension cible V_cible\ndef temps_seuil_rc(E, R, C, V_cible):\n    if V_cible >= E or V_cible <= 0:\n        raise ValueError("V_cible doit etre comprise strictement entre 0 et E")\n    tau = R * C\n    return -tau * math.log(1 - V_cible / E)\n\n# Test des fonctions pour E=5V, R=10k, C=100uF\nE, R, C = 5.0, 10000.0, 100e-6\ntau = R * C  # 1.0 seconde\nprint(f"Constante de temps tau = {tau:.2f} s")\nprint(f"Tension a t=tau : {tension_charge_rc(E, R, C, tau):.3f} V")\nprint(f"Temps pour atteindre 4.0V : {temps_seuil_rc(E, R, C, 4.0):.3f} s")', language='python')
        st.markdown('---')
        st.subheader('✍️ Exercice Interactif de Complémentation de Code Python')
        st.write("Complétez la ligne de code ci-dessous pour calculer l'atténuation en dB d'un signal à partir de `P_in` et `P_out` :")
        user_py_code = st.text_input('Complétez : `attenuation_db = ...`', placeholder='10 * math.log10(P_out / P_in)')
        if st.button('Vérifier le code Python'):
            clean_code = user_py_code.strip().replace(' ', '')
            if '10*math.log10(P_out/P_in)' in clean_code or '10*math.log10(p_out/p_in)' in clean_code:
                st.success('🎉 **Code exact !** La formule `10 * math.log10(P_out / P_in)` calcule le gain/atténuation en dB.')
            else:
                st.info('💡 **Indice** : Utilisez `10 * math.log10(P_out / P_in)`.')
    with tab_exp4:
        st.subheader('✍️ Exercices Pratiques Type Examen & Mini-Quiz')
        st.markdown("\n        #### 📄 Exercice d'Examen Résolu : Décharge d'un Condensateur\n        **Sujet** : La tension de décharge d'un condensateur est donnée par $u_C(t) = 12 e^{-200 t}$ (avec $t$ en secondes).\n        1. Quelle est la tension initiale $u_C(0)$ ?\n        2. Quelle est la valeur de la constante de temps $tau$ ?\n        3. Déterminer l'instant $t_1$ auquel la tension retombe à $1,5\\text{ V}$.\n\n        **Corrigé Détaillé** :\n        1. $u_C(0) = 12 e^0 = 12 \\times 1 = \\mathbf{12\\text{ V}}$.\n        2. L'exponentielle s'écrit $e^{-t/\\tau} = e^{-200 t} \\Rightarrow \\frac{1}{tau} = 200 \\Rightarrow tau = \\frac{1}{200} = \\mathbf{0,005\\text{ s} = 5\\text{ ms}}$.\n        3. On cherche $t_1$ tel que $12 e^{-200 t_1} = 1,5 \\Rightarrow e^{-200 t_1} = 0,125$.\n           $-200 t_1 = \\ln(0,125) \\Rightarrow t_1 = \\frac{\\ln(0,125)}{-200} \\approx \\mathbf{0,0104\\text{ s} = 10,4\\text{ ms}}$.")
        st.markdown('---')
        st.subheader('⚡ Mini-Quiz de Validation : Fonctions Exponentielle & Logarithme')
        quiz_exp_q = [{'q': '1. Quelle est la valeur exacte de ln(e^3) ?', 'opts': ['0', '1', '3', 'e^3'], 'rep': '3', 'expl': "Par propriété d'inversion, ln(e^x) = x pour tout x réel. Donc ln(e^3) = 3."}, {'q': '2. Que vaut la dérivée de la fonction f(x) = e^(-2x) ?', 'opts': ["f'(x) = e^(-2x)", "f'(x) = -2 e^(-2x)", "f'(x) = -2 e^x", "f'(x) = 2 e^(-2x)"], 'rep': "f'(x) = -2 e^(-2x)", 'expl': "La dérivée de e^(u(x)) est u'(x) * e^(u(x)). Ici u(x) = -2x donc u'(x) = -2."}, {'q': '3. Quelle est la limite de e^x quand x tend vers -infini ?', 'opts': ['-infini', '0', '1', '+infini'], 'rep': '0', 'expl': "La fonction exponentielle possède une asymptote horizontale d'équation y = 0 en -infini : lim_{x -> -inf} e^x = 0."}, {'q': "4. Si la puissance d'un signal optique est divisée par 2, quelle est l'atténuation en dB (approx) ?", 'opts': ['-1 dB', '-3 dB', '-6 dB', '-10 dB'], 'rep': '-3 dB', 'expl': '10 * log10(0.5) = 10 * (-0.3010) = -3.01 dB. Une perte de 50% de puissance équivaut à une atténuation de 3 dB.'}]
        for q_idx, q_item in enumerate(quiz_exp_q):
            st.markdown(f'**{q_item["q"]}**')
            ans = st.radio(f'Choix Q{q_idx + 1} :', q_item["opts"], key=f'q_exp_{q_idx}')
            if st.button(f'Valider Q{q_idx + 1}', key=f'btn_exp_{q_idx}'):
                if ans == q_item['rep']:
                    st.success(f'🎉 **Exact !** {q_item["expl"]}')
                else:
                    st.error(f'❌ **Incorrect.** Réponse attendue : **{q_item["rep"]}**. Explication : {q_item["expl"]}')
            st.markdown('<br>', unsafe_allow_html=True)


    st.markdown("---")
    st.subheader("✍️ Grand Test d'Entraînement : 10 Questions sur Exponentielle, Logarithme & RC")
    st.markdown("<p style='color:#94a3b8;'>Consolidez vos automatismes sur les fonctions, les dérivées et l'atténuation en décibels. Impact direct sur votre progression globale !</p>", unsafe_allow_html=True)
    
    score_fct = 0
    for idx_f, q_f in enumerate(QUIZZES_BANK_10["Fonctions"]):
        st.markdown(f"**{q_f['q']}**")
        rep_f = st.radio(f"Votre choix (Q{idx_f + 1}) :", q_f["opts"], key=f"rad_fct_10_{idx_f}")
        if rep_f == q_f["rep"]:
            score_fct += 1
            
    if st.button("Valider le Test des 10 Questions (Fonctions)", type="primary", key="btn_val_fct_10"):
        add_user_points(score_fct * 10, "quiz_fct_10")
        if score_fct >= 8:
            st.success(f"🏆 **Score remarquable : {score_fct} / 10 !** (+{score_fct * 10} points d'XP)")
            st.balloons()
        elif score_fct >= 5:
            st.info(f"👍 **Résultat encourageant : {score_fct} / 10.** (+{score_fct * 10} points d'XP)")
        else:
            st.warning(f"⚠️ **Score : {score_fct} / 10.** (+{score_fct * 10} points d'XP). Reprenez les démonstrations de calcul.")


elif page == '🗓️ Planning Révisions BTS Blanc (9-11 Déc)':
    st.markdown("<div class='hero-title'>🗓️ Planning de Révision Intensif - BTS Blanc (9, 10 & 11 Déc 2026)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Programme d'entraînement structuré semaine par semaine pour réussir les épreuves écrites et pratiques</p>", unsafe_allow_html=True)
    st.markdown("\n    <div class='ciel-card' style='border-left: 6px solid #f59e0b !important;'>\n        <h3 style='color: #92400e; margin-top:0;'>⚠️ Objectif Examen : Épreuves du 9, 10 et 11 Décembre 2026</h3>\n        <p>Il vous reste <b>6 semaines intensives</b> pour maîtriser la totalité du programme du BTS CIEL Option A. Suivez cette feuille de route hebdomadaire :</p>\n    </div>", unsafe_allow_html=True)
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.markdown("\n        <div class='ciel-card'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 1 : Réseaux, Adressage & Commutation</h4>\n            <ul>\n                <li><b>Révisez</b> : Modèle OSI (7 couches), Adressage IPv4/IPv6, Masques VLSM.</li>\n                <li><b>Pratiquez</b> : Le <i>Générateur de Subnetting</i> et la configuration des VLANs 802.1Q dans la sandbox <i>Cisco IOS</i>.</li>\n                <li><b>Exercice clé</b> : Décodage de trames brutes dans le <i>Lab Wireshark</i>.</li>\n            </ul>\n        </div>\n        \n        <div class='ciel-card'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 2 : Cybersécurité & Administration Système</h4>\n            <ul>\n                <li><b>Révisez</b> : Cryptographie (AES/RSA/SHA), Top 10 OWASP, Active Directory (OUs, GPO LSDOU) et droits Linux (chmod).</li>\n                <li><b>Pratiquez</b> : Configuration de règles UFW/IPtables et sécurisation de bases SQL via des requêtes préparées.</li>\n                <li><b>Exercice clé</b> : Sandbox <i>Linux Bash</i> (chmod octal) et analyse des tickets Kerberos.</li>\n            </ul>\n        </div>\n        \n        <div class='ciel-card'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 3 : Développement C++ & Python Réseau</h4>\n            <ul>\n                <li><b>Révisez</b> : Gestion de la mémoire (Tas vs Pile), pointeurs `*`, références `&`, `new[]`/`delete[]`, POO (héritage, classes abstraites).</li>\n                <li><b>Pratiquez</b> : Debugger C++ (correction de fuites mémoire) et programmation de Sockets TCP/UDP Python.</li>\n                <li><b>Exercice clé</b> : Analyse des destructeurs virtuels et des conteneurs STL (`std::vector`).</li>\n            </ul>\n        </div>", unsafe_allow_html=True)
    with col_w2:
        st.markdown("\n        <div class='ciel-card'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 4 : Électronique, Bus Terrain & Oscilloscope</h4>\n            <ul>\n                <li><b>Révisez</b> : Lois de Kirchhoff, Loi d'Ohm, Bus CAN (CAN_H/L, arbitrage CSMA/CR), Modbus RTU, I2C, SPI et numérisation (CAN/ADC).</li>\n                <li><b>Pratiquez</b> : Le <i>Lab Kirchhoff & Ohm</i>, le <i>Lab Oscilloscope</i> (calcul de Vpp, Veff, T, f) et le générateur de Quantum.</li>\n                <li><b>Exercice clé</b> : Décodage d'oscillogrammes et calculs de résistance équivalente.</li>\n            </ul>\n        </div>\n        \n        <div class='ciel-card'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 5 : Modélisation UML, SysML & Projet E6</h4>\n            <ul>\n                <li><b>Révisez</b> : Diagrammes BDD, IBD, Exigences, Classes UML, Séquence et États-Transitions.</li>\n                <li><b>Pratiquez</b> : Le <i>Lab UML & SysML</i> et la création de plans de tests d'intégration (PVL) avec `pytest`.</li>\n                <li><b>Exercice clé</b> : Génération du diagramme de Gantt pour le suivi de projet E6.</li>\n            </ul>\n        </div>\n        \n        <div class='ciel-card'>\n            <h4 style='color:#1d4ed8; margin-top:0;'>📅 Semaine 6 : Annales Officielles & Marathons de Quiz</h4>\n            <ul>\n                <li><b>Révisez</b> : Sujets d'Annales BTS CIEL 2024 & 2025.</li>\n                <li><b>Pratiquez</b> : Lancez le mode <i>Marathon / Méga-Marathon (40-50 questions)</i> dans le Grand Quiz d'Examen.</li>\n                <li><b>Objectif Final</b> : Obtenir une moyenne supérieure à 80% sur l'ensemble des domaines !</li>\n            </ul>\n        </div>", unsafe_allow_html=True)



elif page == '⚡ Lab Kirchhoff, Ohm & Circuits':
    st.markdown("<div class='hero-title'>⚡ Lab Kirchhoff, Loi d'Ohm & Circuits Électriques</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Exercices interactifs d'entraînement sur les lois fondamentales de l'électricité en régime continu</p>", unsafe_allow_html=True)
    tab_k1, tab_k2, tab_k3 = st.tabs(["📝 Exercice 1 : Loi d'Ohm & Puissance", '🔗 Exercice 2 : Loi des Mailles & Diviseur de Tension', '🔀 Exercice 3 : Loi des Nœuds & Parallélisme'])
    with tab_k1:
        st.subheader('Exercice 1 : Calcul de courant, tension et puissance')
        st.markdown("\n        <div class='ciel-card'>\n            <p><b>Énoncé</b> : Un sous-ensemble électronique embarqué comprend un résistor de résistance <b>R = 120 Ω</b> alimenté sous une tension continue de <b>U = 24 V</b>.</p>\n        </div>", unsafe_allow_html=True)
        col_e1_1, col_e1_2 = st.columns(2)
        with col_e1_1:
            u_i1 = st.number_input("Calculer l'intensité I (en Ampères A) :", value=0.0, step=0.01, key='k_i1')
        with col_e1_2:
            u_p1 = st.number_input('Calculer la puissance dissipée P (en Watts W) :', value=0.0, step=0.1, key='k_p1')
        if st.button("Vérifier l'Exercice 1", type='primary', key='btn_ex1'):
            if abs(u_i1 - 0.2) <= 0.01 and abs(u_p1 - 4.8) <= 0.1:
                st.balloons()
                st.success('🎉 **Calculs exacts !**\\\\n- Intensité : $I = \\frac{U}{R} = \\frac{24}{120} = 0,20 \\text{ A}$ (soit $200 \\text{ mA}$)\\\\n- Puissance : $P = U \\cdot I = 24 \\cdot 0,2 = 4,80 \\text{ W}$ (ou $P = R \\cdot I^2 = 120 \\cdot 0,04 = 4,80 \\text{ W}$)')
            else:
                st.error('❌ **Réponse incorrecte.** Vérifiez vos formules : $I = \\frac{U}{R}$ et $P = U \\cdot I$.')
                st.info('💡 **Rappel** : $I = 24 / 120 = 0,20 \\text{ A}$ et $P = 24 \\times 0,20 = 4,80 \\text{ W}$.')
    with tab_k2:
        st.subheader('Exercice 2 : Loi des Mailles & Pont Diviseur de Tension')
        st.markdown("\n        <div class='ciel-card'>\n            <p><b>Énoncé</b> : Un capteur est alimenté par un générateur idéal $E = 15 \\text{ V}$ connecté en série avec deux résistances $R_1 = 200 \\Omega$ et $R_2 = 300 \\Omega$.</p>\n        </div>", unsafe_allow_html=True)
        u_u2 = st.number_input('Calculer la tension U2 aux bornes de R2 (en Volts V) :', value=0.0, step=0.1, key='k_u2')
        if st.button("Vérifier l'Exercice 2", type='primary', key='btn_ex2'):
            if abs(u_u2 - 9.0) <= 0.1:
                st.balloons()
                st.success('🎉 **Pont Diviseur de Tension exact !**\\\\n$$U_2 = E \\cdot \\frac{R_2}{R_1 + R_2} = 15 \\cdot \\frac{300}{200 + 300} = 15 \\cdot \\frac{300}{500} = 9,0 \\text{ V}$$')
            else:
                st.error('❌ **Calcul incorrect.** Formule du pont diviseur : $U_2 = E \\cdot \\frac{R_2}{R_1 + R_2}$.')
                st.info('💡 **Démonstration** : $U_2 = 15 \\times \\frac{300}{500} = 9,0 \\text{ V}$.')
    with tab_k3:
        st.subheader('Exercice 3 : Loi des Nœuds & Résistances en Parallèle')
        st.markdown("\n        <div class='ciel-card'>\n            <p><b>Énoncé</b> : Un nœud d'un circuit reçoit un courant principal $I = 1,5 \\text{ A}$ qui se sépare en deux branches en parallèle de résistances $R_1 = 60 \\Omega$ et $R_2 = 120 \\Omega$.</p>\n        </div>", unsafe_allow_html=True)
        col_e3_1, col_e3_2 = st.columns(2)
        with col_e3_1:
            u_req = st.number_input('Résistance équivalente Req (en Ω) :', value=0.0, step=0.1, key='k_req')
        with col_e3_2:
            u_i1_par = st.number_input('Courant I1 traversant R1 (en Ampères A) :', value=0.0, step=0.1, key='k_i1_par')
        if st.button("Vérifier l'Exercice 3", type='primary', key='btn_ex3'):
            if abs(u_req - 40.0) <= 0.1 and abs(u_i1_par - 1.0) <= 0.1:
                st.balloons()
                st.success('🎉 **Calculs exacts !**\\\\n- Résistance équivalente : $R_{\\text{eq}} = \\frac{R_1 \\cdot R_2}{R_1 + R_2} = \\frac{60 \\cdot 120}{180} = 40 \\Omega$\\\\n- Tension totale : $U = R_{\\text{eq}} \\cdot I = 40 \\cdot 1,5 = 60 \\text{ V}$\\\\n- Courant I1 : $I_1 = \\frac{U}{R_1} = \\frac{60}{60} = 1,0 \\text{ A}$ (et $I_2 = 0,5 \\text{ A}$, vérifiant $1,0 + 0,5 = 1,5 \\text{ A}$ par la Loi des Nœuds).')
            else:
                st.error('❌ **Résultat incorrect.** Formules : $R_{\\text{eq}} = \\frac{R_1 \\cdot R_2}{R_1 + R_2}$ et $I_1 = I \\cdot \\frac{R_2}{R_1 + R_2}$.')


    st.markdown("---")
    st.subheader("✍️ Grand Test d'Entraînement : 10 Questions sur les Lois Fondamentales de l'Électricité")
    st.markdown("<p style='color:#94a3b8;'>Maîtrisez les lois d'Ohm, de Joule, des Mailles, des Nœuds et les ponts diviseurs sous tension continue.</p>", unsafe_allow_html=True)
    
    score_kir = 0
    for idx_k, q_k in enumerate(QUIZZES_BANK_10["Kirchhoff"]):
        st.markdown(f"**{q_k['q']}**")
        rep_k = st.radio(f"Votre choix (Q{idx_k + 1}) :", q_k["opts"], key=f"rad_kir_10_{idx_k}")
        if rep_k == q_k["rep"]:
            score_kir += 1
            
    if st.button("Valider le Test des 10 Questions (Électricité)", type="primary", key="btn_val_kir_10"):
        add_user_points(score_kir * 10, "quiz_kir_10")
        if score_kir >= 8:
            st.success(f"🏆 **Excellente maîtrise en électronique : {score_kir} / 10 !** (+{score_kir * 10} points)")
            st.balloons()
        elif score_kir >= 5:
            st.info(f"👍 **Score : {score_kir} / 10.** (+{score_kir * 10} points)")
        else:
            st.warning(f"⚠️ **Score : {score_kir} / 10.** (+{score_kir * 10} points). Revoir les formules de résistances équivalentes.")


elif page == '📺 Lab Oscilloscope & Mesures Physiques':
    st.markdown("<div class='hero-title'>📺 Lab Oscilloscope & Analyse d'Oscillogrammes</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Analyse graphique de signaux temporels et réglages de sensibilité verticale / horizontale</p>", unsafe_allow_html=True)
    st.markdown("\n    <div class='ciel-card'>\n        <h3 style='color:#1e3a8a; margin-top:0;'>🔍 Oscillogramme à analyser (Signal Sinusoïdal)</h3>\n        <p>Réglages de l'oscilloscope :</p>\n        <ul>\n            <li><b>Sensibilité Verticale ($S_v$)</b> : <code>2,0 V/div</code></li>\n            <li><b>Base de temps Horizontal ($S_h$)</b> : <code>1,0 ms/div</code></li>\n        </ul>\n    </div>", unsafe_allow_html=True)
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
        u_vpp = st.number_input('1. Tension crête-à-crête Vpp (en Volts V) :', value=0.0, step=1.0, key='osc_vpp')
        u_vmax = st.number_input('2. Amplitude / Tension maximale Vmax (en Volts V) :', value=0.0, step=1.0, key='osc_vmax')
        u_veff = st.number_input('3. Valeur efficace Veff (en Volts V, arrondi à 0.1) :', value=0.0, step=0.1, key='osc_veff')
    with c_o2:
        u_t_ms = st.number_input('4. Période T (en millisecondes ms) :', value=0.0, step=0.5, key='osc_t')
        u_freq = st.number_input('5. Fréquence f (en Hertz Hz) :', value=0.0, step=10.0, key='osc_f')
    if st.button("Vérifier l'analyse de l'oscillogramme", type='primary', key='btn_osc'):
        vpp_ok = abs(u_vpp - 12.0) <= 0.1
        vmax_ok = abs(u_vmax - 6.0) <= 0.1
        veff_ok = abs(u_veff - 4.2) <= 0.2
        t_ok = abs(u_t_ms - 4.0) <= 0.1
        f_ok = abs(u_freq - 250.0) <= 5.0
        if vpp_ok and vmax_ok and veff_ok and t_ok and f_ok:
            st.balloons()
            st.success("🏆 **Analyse d'oscillogramme parfaite !**\\\\n- $V_{\\text{pp}} = 6 \\text{ div} \\times 2,0 \\text{ V/div} = 12,0 \\text{ V}$\\\\n- $V_{\\text{max}} = 6,0 \\text{ V}$\\\\n- $V_{\\text{eff}} = \\frac{6,0}{\\sqrt{2}} \\approx 4,24 \\text{ V}$\\\\n- Période $T = 4 \\text{ div} \\times 1,0 \\text{ ms/div} = 4,0 \\text{ ms} = 0,004 \\text{ s}$\\\\n- Fréquence $f = \\frac{1}{0,004} = 250 \\text{ Hz}$")
        else:
            st.error("❌ **Certaines valeurs sont incorrectes.** Lisez le nombre de carreaux occupés par le motif sinusoïdal sur l'écran.")
            st.info("💡 **Aide du professeur** :\\\\n- Le signal s'étend de -3 div à +3 div $\\Rightarrow 6$ div au total $\\Rightarrow V_{\\text{pp}} = 6 \\times 2 = 12 \\text{ V}$.\\\\n- Un motif complet se répète tous les 4 carreaux horizontaux $\\Rightarrow T = 4 \\times 1 \\text{ ms} = 4 \\text{ ms}$.\\\\n- $f = 1 / 0,004 \\text{ s} = 250 \\text{ Hz}$.")


    st.markdown("---")
    st.subheader("✍️ Grand Test d'Entraînement : 10 Questions sur l'Oscilloscope & Mesures Physiques")
    st.markdown("<p style='color:#94a3b8;'>Sensibilités Sv/Sh, valeurs efficaces, calculs de fréquences et déphasage.</p>", unsafe_allow_html=True)
    
    score_osc = 0
    for idx_o, q_o in enumerate(QUIZZES_BANK_10["Oscilloscope"]):
        st.markdown(f"**{q_o['q']}**")
        rep_o = st.radio(f"Votre choix (Q{idx_o + 1}) :", q_o["opts"], key=f"rad_osc_10_{idx_o}")
        if rep_o == q_o["rep"]:
            score_osc += 1
            
    if st.button("Valider le Test des 10 Questions (Oscilloscope)", type="primary", key="btn_val_osc_10"):
        add_user_points(score_osc * 10, "quiz_osc_10")
        if score_osc >= 8:
            st.success(f"🏆 **Expertise mesure validée : {score_osc} / 10 !** (+{score_osc * 10} points)")
            st.balloons()
        elif score_osc >= 5:
            st.info(f"👍 **Score : {score_osc} / 10.** (+{score_osc * 10} points)")
        else:
            st.warning(f"⚠️ **Score : {score_osc} / 10.** (+{score_osc * 10} points)")


elif page == '📚 Encyclopédie des Cours & TPs':
    st.markdown("<div class='hero-title'>📚 Encyclopédie des Cours & Mini-Tests</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Cours théoriques exhaustifs, formules d'ingénierie et mini-évaluations interactives</p>", unsafe_allow_html=True)
    col_sel1, col_sel2 = st.columns([1, 1])
    with col_sel1:
        domaine = st.selectbox("Sélectionnez le Domaine d'Ingénierie :", list(COURS_BASE.keys()))
    with col_sel2:
        search_query = st.text_input('🔍 Rechercher un concept dans ce domaine :', placeholder='ex: Shannon, 802.1Q, pointeur, GPO...')
    chapitres = COURS_BASE[domaine]
    for chap_titre, chap_contenu in chapitres.items():
        if search_query.lower() in chap_titre.lower() or search_query.lower() in chap_contenu.lower():
            with st.expander(f'📖 {chap_titre}', expanded=True):
                st.markdown(chap_contenu)
                if chap_titre in MINI_QUIZ_COURS:
                    st.markdown('---')
                    mq = MINI_QUIZ_COURS[chap_titre]
                    st.markdown(f'**⚡ Mini-Test de Validation :** *{mq["q"]}*')
                    choix_mq = st.radio('Votre réponse :', mq["options"], key=f'mq_{chap_titre}')
                    if st.button('Valider la réponse', key=f'btn_mq_{chap_titre}'):
                        if choix_mq == mq['rep']:
                            st.success(f'🎉 **Exact !** {mq["expl"]}')
                        else:
                            st.error(f'❌ **Incorrect.** Réponse attendue : **{mq["rep"]}**.\n\n*Explication : {mq["expl"]}*')



elif page == '🧮 Laboratoire de Calculs (Subnetting & Élec)':
    st.markdown("<div class='hero-title'>🧮 Laboratoire de Calculs Dynamiques</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Générateur infini d'exercices de calculs pour l'épreuve écrite E4</p>", unsafe_allow_html=True)
    tab_calc1, tab_calc2 = st.tabs(['🌐 Calculs de Sous-Réseaux (Subnetting IPv4)', '⚡ Calculs Électronique & CAN (Quantum)'])
    with tab_calc1:
        st.subheader('Générateur Infini de Découpage IPv4')
        if 'subnet_ip' not in st.session_state:
            t_class = random.choice(['B', 'C'])
            if t_class == 'C':
                st.session_state.subnet_ip = f'192.168.{random.randint(1, 200)}.0'
                st.session_state.subnet_cidr = 24
                st.session_state.subnet_subnets = random.choice([2, 4, 8])
            else:
                st.session_state.subnet_ip = f'172.{random.randint(16, 31)}.{random.randint(1, 200)}.0'
                st.session_state.subnet_cidr = 16
                st.session_state.subnet_subnets = random.choice([4, 8, 16])
            bits_n = 0
            while 2 ** bits_n < st.session_state.subnet_subnets:
                bits_n += 1
            new_c = st.session_state.subnet_cidr + bits_n
            st.session_state.sol_c = new_c
            st.session_state.sol_hosts = 2 ** (32 - new_c) - 2
        ip_c = st.session_state.subnet_ip
        cidr_c = st.session_state.subnet_cidr
        subs_c = st.session_state.subnet_subnets
        st.info(f"📋 **Énoncé** : Soit l'adresse réseau **{ip_c}/{cidr_c}**. Découpez ce bloc en **{subs_c} sous-réseaux** de dimensions égales.")
        c_ans1, c_ans2 = st.columns(2)
        with c_ans1:
            u_cidr = st.number_input('Nouveau préfixe CIDR (ex: 26) :', min_value=1, max_value=32, value=24, key='u_cidr_in')
        with c_ans2:
            u_hosts = st.number_input("Nombre d'hôtes utiles par sous-réseau :", min_value=1, value=254, key='u_hosts_in')
        if st.button('Vérifier mes calculs Réseau', type='primary'):
            c_ok = u_cidr == st.session_state.sol_c
            h_ok = u_hosts == st.session_state.sol_hosts
            if c_ok and h_ok:
                st.balloons()
                st.success(f'🏆 **Parfait !** Nouveau masque : `/{st.session_state.sol_c}` | Hôtes utiles : `{st.session_state.sol_hosts}`.')
            else:
                if not c_ok:
                    st.error(f'❌ **Erreur CIDR** : Pour créer {subs_c} sous-réseaux, il faut emprunter {st.session_state.sol_c - cidr_c} bits. Le nouveau CIDR est `/{st.session_state.sol_c}`.')
                if not h_ok:
                    st.error(f'❌ **Erreur Hôtes** : Avec un `/{st.session_state.sol_c}`, la taille totale du bloc est de {2 ** (32 - st.session_state.sol_c)} adresses. Moins 2 adresses réservées = {st.session_state.sol_hosts} hôtes utiles.')
        if st.button('Générer un autre exercice Réseau'):
            for k in ['subnet_ip', 'subnet_cidr', 'subnet_subnets', 'sol_c', 'sol_hosts']:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()
    with tab_calc2:
        st.subheader('Générateur de Calculs de Quantum & CAN (ADC)')
        if 'adc_bits' not in st.session_state:
            st.session_state.adc_bits = random.choice([10, 12, 16])
            st.session_state.adc_vref = random.choice([3.3, 5.0])
            st.session_state.adc_ve = round(random.uniform(0.5, st.session_state.adc_vref - 0.2), 2)
            n_levels = 2 ** st.session_state.adc_bits - 1
            q_val = st.session_state.adc_vref / n_levels
            st.session_state.adc_sol_n = round(st.session_state.adc_ve / q_val)
            st.session_state.adc_sol_q_mv = q_val * 1000.0
        bits = st.session_state.adc_bits
        vref = st.session_state.adc_vref
        ve = st.session_state.adc_ve
        st.info(f'📋 **Énoncé** : Un convertisseur analogique-numérique possède une résolution de **{bits} bits** et une tension de référence **Vref = {vref} V**. On applique en entrée une tension analogique **Ve = {ve} V**.')
        u_n = st.number_input('Entrez la valeur numérique entière N générée en sortie du CAN :', min_value=0, value=0, key='u_n_adc')
        if st.button('Vérifier le calcul CAN', type='primary'):
            if abs(u_n - st.session_state.adc_sol_n) <= 1:
                st.balloons()
                st.success(f'🏆 **Calcul exact !** N = **{st.session_state.adc_sol_n}** (Quantum q ≈ {st.session_state.adc_sol_q_mv:.3f} mV).')
            else:
                st.error(f'❌ **Valeur incorrecte.** N calculé = **{st.session_state.adc_sol_n}**.')
                st.markdown(f'\n                **Démonstration du calcul :**\n                1. Quantum : $$q = \\frac{{V_{{ref}}}}{{2^n - 1}} = \\frac{{{vref}}}{{2^{{{bits}}} - 1}} = \\frac{{{vref}}}{{{2 ** bits - 1}}} \\approx {st.session_state.adc_sol_q_mv / 1000.0:.6f} \\text{{ V}}$$\n                2. Valeur entière : $$N = \\text{{arrondi}}\\left(\\frac{{V_e}}{{q}}\\right) = \\text{{arrondi}}\\left(\\frac{{{ve}}}{{{st.session_state.adc_sol_q_mv / 1000.0:.6f}}}\\right) = {st.session_state.adc_sol_n}$$')
        if st.button('Générer un autre exercice CAN'):
            for k in ['adc_bits', 'adc_vref', 'adc_ve', 'adc_sol_n', 'adc_sol_q_mv']:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()


    st.markdown("---")
    st.subheader("✍️ Grand Test d'Entraînement : 10 Questions sur la Numérisation & CAN / CNA")
    st.markdown("<p style='color:#94a3b8;'>Quantum, résolution binaire, théorème de Shannon et filtres anti-repliement.</p>", unsafe_allow_html=True)
    
    score_can = 0
    for idx_c, q_c in enumerate(QUIZZES_BANK_10["CAN_ADC"]):
        st.markdown(f"**{q_c['q']}**")
        rep_c = st.radio(f"Votre choix (Q{idx_c + 1}) :", q_c["opts"], key=f"rad_can_10_{idx_c}")
        if rep_c == q_c["rep"]:
            score_can += 1
            
    if st.button("Valider le Test des 10 Questions (CAN / ADC)", type="primary", key="btn_val_can_10"):
        add_user_points(score_can * 10, "quiz_can_10")
        if score_can >= 8:
            st.success(f"🏆 **Maîtrise du traitement du signal : {score_can} / 10 !** (+{score_can * 10} points)")
            st.balloons()
        elif score_can >= 5:
            st.info(f"👍 **Score : {score_can} / 10.** (+{score_can * 10} points)")
        else:
            st.warning(f"⚠️ **Score : {score_can} / 10.** (+{score_can * 10} points)")


elif page == '📐 Laboratoire UML & SysML':
    st.markdown("<div class='hero-title'>📐 Laboratoire Interactif UML & SysML</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Modélisation système d'ingénierie et cas pratiques d'examen</p>", unsafe_allow_html=True)
    tab_uml1, tab_uml2 = st.tabs(['🏗️ Modélisation SysML (BDD & IBD)', '📐 Modélisation UML (Classes & Séquence)'])
    with tab_uml1:
        st.subheader("Exemple Complet SysML : Station de Surveillance de la Qualité de l'Air")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown('#### Block Definition Diagram (BDD)')
            st.code('\n+-------------------------------------------------------------+\n|             bdd [Système] StationSurveillance               |\n+-------------------------------------------------------------+\n|                                                             |\n|   +-----------------------------------------------------+   |\n|   |                       Station                       |   |\n|   +-----------------------------------------------------+   |\n|   | parts:                                              |   |\n|   |  - cibleAcquisition : MicrocontroleurSTM32 [1]      |   |\n|   |  - capteurCO2 : CapteurSondeNDIR [1]                |   |\n|   |  - moduleCom : TransmetteurLoRa [1]                 |   |\n|   |  - alimentation : BlocBatterieRegulee [1]           |   |\n|   +-----------------------------------------------------+   |\n|                              |                              |\n|                  +-----------+-----------+                  |\n|                  |                       |                  |\n|                 1◆                      1◆                  |\n|   +--------------------------+  +-----------------------+   |\n|   |  MicrocontroleurSTM32    |  |    CapteurSondeNDIR   |   |\n|   +--------------------------+  +-----------------------+   |\n|   | - frequence : 84 MHz     |  | - plagePPM : 0..5000  |   |\n|   | - memFlash : 512 Ko      |  | - interface : SPI     |   |\n|   +--------------------------+  +-----------------------+   |\n+-------------------------------------------------------------+', language='text')
        with col_s2:
            st.markdown('#### Internal Block Diagram (IBD)')
            st.code('\n+-----------------------------------------------------------------+\n|             ibd [Block] StationSurveillance                     |\n+-----------------------------------------------------------------+\n|                                                                 |\n|  +--------------------+                   +------------------+  |\n|  |  capteurCO2:       |                   |  cibleAcquis:    |  |\n|  |  CapteurSondeNDIR  |                   |  STM32           |  |\n|  |                    |                   |                  |  |\n|  |           [p_spi]  |=== Bus SPI (4 fils) ===[p_spi]       |  |\n|  |                    |   (MOSI, MISO,    |                  |  |\n|  |                    |    SCLK, CS)      |                  |  |\n|  |                    |                   |          [p_uart]|  |\n|  +--------------------+                   +-------------||---+  |\n|                                                         ||      |\n|                                                Liaison Série TX |\n|                                                         ||      |\n|  +--------------------+                                 ||      |\n|  |  moduleCom:        |                                 ||      |\n|  |  TransmetteurLoRa  |                                 ||      |\n|  |                    |                                 ||      |\n|  |           [p_uart] |=================================++      |\n|  +--------------------+                                         |\n+-----------------------------------------------------------------+', language='text')
        st.markdown("#### ✍️ Exercice d'Analyse SysML :")
        q_sysml = st.radio("En observant l'IBD ci-dessus, quel bus physique assure le transfert des mesures brutes entre le capteur de CO2 et le microcontrôleur ?", ['Liaison série asynchrone UART', 'Bus synchrone 4 fils SPI', 'Bus I2C sur 2 fils', 'Bus CAN différentiel'], key='q_sysml_radio')
        if st.button("Valider l'analyse SysML"):
            if q_sysml == 'Bus synchrone 4 fils SPI':
                st.success('✅ **Exact !** Le port `[p_spi]` relie le capteur au microcontrôleur via le bus SPI (MOSI, MISO, SCLK, CS).')
            else:
                st.error('❌ **Erreur.** Le diagramme indique explicitement un bus SPI à 4 fils.')
    with tab_uml2:
        st.subheader('Modélisation Logicielle UML')
        st.code('\n+------------------------------------+\n|             Capteur                |\n+------------------------------------+\n| # refCapteur : string              |\n| # tensionAlim : float              |\n+------------------------------------+\n| + Capteur(r : string)              |\n| + virtual ~Capteur()               |\n| + virtual lireConcentration() = 0  |  <--- Méthode virtuelle pure\n+------------------------------------+\n                  ^\n                  |  Héritage (Généralisation)\n                  |\n+------------------------------------+\n|           CapteurCO2SPI            |\n+------------------------------------+\n| - pinChipSelect : int              |\n| - frequenceHorlogeHz : int         |\n+------------------------------------+\n| + CapteurCO2SPI(r:string, cs:int)  |\n| + lireConcentration() : float      |  <--- Implémentation concrète\n+------------------------------------+', language='text')



elif page == '🧪 Qualification & Tests E6':
    st.markdown("<div class='hero-title'>🧪 Qualification Logicielle & Tests E6</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Méthodologie du Plan de Validation Logicielle (PVL) et assertions de tests automatisés</p>", unsafe_allow_html=True)
    st.write("\n    Dans l'épreuve **E6**, vous devez prouver la conformité de vos développements avec le cahier des charges initial au moyen d'un **Plan de Validation Logicielle (PVL)** rigoureux.")
    st.markdown("### 💻 Exemple de Script de Test d'Intégration Réseau & BDD (Python / PyTest) :")
    st.code('\nimport pytest\nimport json\n\ndef valider_payload_telemesure(payload_json_str):\n    try:\n        data = json.loads(payload_json_str)\n        if "device_id" not in data or "co2_ppm" not in data:\n            return False, "Champs obligatoires manquants"\n        if not (0 <= data["co2_ppm"] <= 5000):\n            return False, "Valeur CO2 hors plage valide [0-5000]"\n        return True, "Payload conforme"\n    except Exception as e:\n        return False, str(e)\n\n# --- CAS DE TEST D\'INTÉGRATION ---\ndef test_integration_payload_nominal():\n    payload_test = \'{"device_id": "STATION_AIR_01", "co2_ppm": 420.5, "temp": 21.4}\'\n    valide, msg = valider_payload_telemesure(payload_test)\n    assert valide is True\n    assert msg == "Payload conforme"\n\ndef test_integration_payload_anomalie():\n    payload_anormal = \'{"device_id": "STATION_AIR_01", "co2_ppm": 99999.0}\'\n    valide, msg = valider_payload_telemesure(payload_anormal)\n    assert valide is False\n    assert "hors plage" in msg', language='python')
    st.markdown("### ✍️ Testez vos réflexes d'Assurance Qualité :")
    st.write("Complétez l'assertion Python pour valider qu'un code de retour HTTP reçu d'un serveur Web vaut bien **200 (OK)** :")
    user_assert = st.text_input("Saisissez votre ligne d'assertion :", placeholder='Entrez votre assertion (ex: assert ... == ...)', key='qa_assert')
    if st.button("Exécuter le Test d'Intégration"):
        if user_assert.strip().replace(' ', '') == 'assertreponse.status_code==200':
            st.success("✅ **Test Validé !** L'assertion vérifie avec exactitude le code statut HTTP nominal.")
        else:
            st.info('💡 **Syntaxe attendue** : `assert reponse.status_code == 200`')



elif page == '🎯 Annales BTS (2024 & 2025)':
    st.markdown("<div class='hero-title'>🎯 Banque Complète des Annales Officielles BTS CIEL (2024 - 2026)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Étude approfondie des sujets réels E4 (Informatique & Physique), barèmes officiels et grilles d'évaluation</p>", unsafe_allow_html=True)

    tab_an_sel = st.selectbox("Sélectionnez la Session d'Examen Officielle :", [
        "Session 2026 : CISS Cashless Online (Métropole & Nouvelle-Calédonie)",
        "Session 2025 : Parking Multi-Niveaux Seven-Park (Métropole)",
        "Session 2024 : Station de Surveillance de la Qualité de l'Eau (Option A)",
        "Synthèse Comparative & Barèmes E4 (6h, 100 points)"
    ])

    if "2026" in tab_an_sel:
        st.subheader("💳 Session 2026 : Système Monétique 'CISS Cashless Online' (Métropole & NC)")
        st.markdown("""
<div class='ciel-card' style='border-left: 6px solid #2563eb !important;'>
    <h4 style='color: #1d4ed8; margin-top:0;'>📌 Contexte Industriel du Sujet E4 (2026)</h4>
    <p>Le système <b>CISS Cashless Online</b> assure la gestion dématérialisée des paiements sans contact (NFC/RFID) lors de grands événements (festivals, stades, salons). L'architecture comprend des terminaux de paiement embarqués communicants, des concentrateurs locaux et des serveurs de paiement transactionnels sécurisés.</p>
</div>
        """, unsafe_allow_html=True)

        col_26_a, col_26_b = st.columns(2)
        with col_26_a:
            st.markdown("""
#### 📶 Partie Informatique & Réseaux (70 points)
* **Communication NFC & Sécurité des Transactions** :
  * Protocole d'échange ISO/IEC 14443 Type A/B à 13,56 MHz.
  * Authentification mutuelle et chiffrement AES-128 des données de porte-monnaie électronique.
* **API REST & Synchronisation JSON** :
  * Endpoints HTTPS `/api/v1/transaction` avec jetons d'authentification Bearer JWT.
  * Gestion du mode déconnecté (*Store & Forward*) avec base de données SQLite locale synchronisée dès rétablissement du lien réseau.
* **Segmentation Réseau & VLANs Événementiels** :
  * VLAN 10 (Terminaux TPE Cashless, priorité QoS stricte), VLAN 20 (Gestion & Supervision), VLAN 30 (Accès Public Wi-Fi invité).
            """)
        with col_26_b:
            st.markdown(r"""
#### ⚡ Partie Sciences Physiques & Signal (30 points)
* **Antenne NFC & Télé-Alimentation** :
  * Couplage inductif champ proche ($13,56\text{ MHz}$), calcul de l'inductance de boucle $L$ et du condensateur d'accord résonant $C$ :
  $$f_0 = \frac{1}{2\pi \sqrt{L \cdot C}} = 13,56\text{ MHz}$$
* **Conditionnement du Signal de Débitmètre & Capteur de Force** :
  * Amplification d'instrumentation et conversion CAN 12 bits pour le contrôle des pompes de distribution connectées.
            """)

        st.markdown("#### ✍️ Questions Types Corrigées E4 (2026)")
        q_26_ans = st.radio("Q1 : Quelle norme régit la transmission radiofréquence sans contact NFC à 13,56 MHz ?", [
            "IEEE 802.11ax (Wi-Fi 6)",
            "ISO/IEC 14443 à 13,56 MHz",
            "Bluetooth SIG v5.3 à 2,4 GHz",
            "LoRaWAN EU868"
        ], key="q26_radio")
        if st.button("Vérifier Q1 (2026)", key="btn_q26_1"):
            if "ISO/IEC 14443" in q_26_ans:
                st.success("🎉 **Exact !** Les puces monétiques NFC sans contact opèrent sous la norme ISO/IEC 14443 à 13,56 MHz.")
            else:
                st.error("❌ Incorrect. La norme internationale NFC sans contact est ISO/IEC 14443 à 13,56 MHz.")

    elif "2025" in tab_an_sel:
        st.subheader("🚗 Session 2025 : Parking Multi-Niveaux 'Seven-Park' (Métropole)")
        st.markdown("""
<div class='ciel-card' style='border-left: 6px solid #10b981 !important;'>
    <h4 style='color: #065f46; margin-top:0;'>📌 Contexte Industriel du Sujet E4 (2025)</h4>
    <p>Le parking <b>Seven-Park</b> comprend 5 niveaux équipés de capteurs ultrasoniques de présence par place, de barrières automatiques, de panneaux d'affichage LED à chaque étage et d'un serveur central de supervision SCADA connecté en fibre optique.</p>
</div>
        """, unsafe_allow_html=True)

        col_25_a, col_25_b = st.columns(2)
        with col_25_a:
            st.markdown("""
#### 📶 Partie Informatique & Réseaux
* **Plan d'Adressage VLSM (Réseau 172.20.0.0/16)** :
  * Découpage en blocs $/20$ pour la DMZ (`172.20.0.0/20`), le réseau Informatique (`172.20.16.0/20`), Finances (`172.20.32.0/20`) et Capteurs (`172.20.48.0/20`).
* **Redirection de Ports (NAT/DNAT)** :
  * Translation de l'IP publique `109.234.164.69:80` et `:443` vers le serveur web interne `172.20.7.1`.
* **IPv6 & Auto-Configuration EUI-64** :
  * Calcul d'Interface-ID depuis l'adresse MAC `fc:c2:3d:0a:68:07` $\rightarrow$ insertion de `FF:FE` et inversion du 7e bit $\rightarrow$ `fec2:3dff:fe0a:6807`.
            """)
        with col_25_b:
            st.markdown(r"""
#### ⚡ Partie Sciences Physiques & Capteurs
* **Boucle Magnétique de Détection de Véhicule** :
  * Mesure de la variation d'inductance $\Delta L$ au passage d'une masse métallique de véhicule modifiant la fréquence d'oscillation.
* **Bus Différentiel RS-485 & Modbus RTU** :
  * Transmission semi-duplex sur paire torsadée avec résistances de terminaison de $120\,\Omega$ pour éviter les réflexions d'ondes.
            """)

    elif "2024" in tab_an_sel:
        st.subheader("💧 Session 2024 : Surveillance de la Qualité de l'Eau en Rivière (Option A)")
        st.markdown("""
<div class='ciel-card' style='border-left: 6px solid #06b6d4 !important;'>
    <h4 style='color: #0891b2; margin-top:0;'>📌 Contexte Industriel du Sujet E4 (2024)</h4>
    <p>Une station autonome immergée mesure en continu la température, la turbidité, le pH et la saturation en oxygène de l'eau, puis transmet les données agrégées vers une passerelle LoRaWAN The Things Network (TTN).</p>
</div>
        """, unsafe_allow_html=True)

        st.markdown(r"""
#### 🔹 Points Forts du Corrigé Officiel (Lycée Louis Jouvet)
1. **Modélisation C++ de la Classe `GestionStation`** :
   * Attributs privés : pointeurs d'agrégation `AP2000* sonde;` et `CommunicationLoRa* comLoRa;`, buffer d'octets `unsigned char* payload;`.
   * Méthode accesseur : `float AP2000::getTemp() { return temp; }`.
2. **Encodage Compact du Payload LoRaWAN** :
   * *Format ASCII non compressé* : '95.30' $\Rightarrow$ 5 octets (`0x39 0x35 0x2E 0x33 0x30`).
   * *Format Entier binaire compressé* : $95,30 \times 100 = 9530$ décimal $\Rightarrow$ `0x253A` en hexadécimal $\Rightarrow$ **seulement 2 octets** (gain de 60% de bande passante).
3. **Bilan de Liaison Radio LoRa (868 MHz)** :
   * Puissance d'émission $P_{TX} = 14\text{ dBm} \Rightarrow \text{PIRE} = 15\text{ dBm}$ (Gain antenne $+2\text{ dBi}$, pertes câbles $-1\text{ dB}$).
   * Pertes en espace libre $\text{FSL} = 105\text{ dB}$ à $5\text{ km}$.
   * Puissance reçue $P_{RX} = -89\text{ dBm}$ face à une sensibilité de $-140\text{ dBm} \Rightarrow$ **Marge de réception confortable de $+51\text{ dB}$**.
   * Respect du temps d'occupation du canal (*Duty Cycle*) : $\alpha = 0,41\% \le 1,0\%$ (conforme aux normes ARCEP).
        """)

    else:
        st.subheader("📊 Barème Officiel & Méthodologie de Réussite E4")
        st.markdown("""
<div class='ciel-card'>
    <h4>Répartition Officielle des Points à l'Épreuve E4 (Coefficient 4, Durée 6h) :</h4>
    <table style='width: 100%; border-collapse: collapse;'>
        <tr style='background: #f1f5f9; border-bottom: 2px solid #cbd5e1;'>
            <th style='padding: 10px; text-align: left;'>Partie d'Épreuve</th>
            <th style='padding: 10px;'>Durée Recommandée</th>
            <th style='padding: 10px;'>Points Barème</th>
            <th style='padding: 10px;'>Thématiques Clés Évaluées</th>
        </tr>
        <tr style='border-bottom: 1px solid #e2e8f0;'>
            <td style='padding: 10px;'><b>Partie 1 : Informatique & Réseaux</b></td>
            <td style='padding: 10px; text-align: center;'>4h30</td>
            <td style='padding: 10px; text-align: center;'><b>70 / 100 pts</b></td>
            <td style='padding: 10px;'>Architecture réseau, VLANs, routage, protocoles sécurisés, classes C++, requêtes SQL, matrices de flux.</td>
        </tr>
        <tr>
            <td style='padding: 10px;'><b>Partie 2 : Sciences Physiques</b></td>
            <td style='padding: 10px; text-align: center;'>1h30</td>
            <td style='padding: 10px; text-align: center;'><b>30 / 100 pts</b></td>
            <td style='padding: 10px;'>Capteurs, conditionnement, conversion CAN/CNA, bilan de liaison radio, filtres, transmission sur bus différentiels.</td>
        </tr>
    </table>
</div>
        """, unsafe_allow_html=True)




elif page == '🗂️ Flashcards Actives':
    st.markdown("<div class='hero-title'>🗂️ Flashcards Actives & Auto-Évaluation</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Stimulez votre mémoire active avec 105 cartes mémoire réflexes couvrant tout le programme du BTS CIEL (avec conseils prof, redirections de cours et vidéos YouTube)</p>", unsafe_allow_html=True)
    if 'fc_mastered' not in st.session_state:
        st.session_state.fc_mastered = set()
    yt_prefix = 'https://www.youtube.com/watch?v='
    col_f1, col_f2, col_f3 = st.columns([1.5, 1.5, 1])
    with col_f1:
        all_mods = ['Tous les modules'] + list(dict.fromkeys([f['module'] for f in FLASHCARDS_DATA]))
        sel_m = st.selectbox('📁 Filtrer par domaine :', all_mods)
    f_list = FLASHCARDS_DATA if sel_m == 'Tous les modules' else [f for f in FLASHCARDS_DATA if f['module'] == sel_m]
    with col_f2:
        all_chaps = ['Tous les chapitres'] + list(dict.fromkeys([f['chap'] for f in f_list]))
        sel_c = st.selectbox('📖 Filtrer par chapitre :', all_chaps)
    if sel_c != 'Tous les chapitres':
        f_list = [f for f in f_list if f['chap'] == sel_c]
    with col_f3:
        mode_fc = st.radio('👁️ Affichage :', ['🎴 Carte par Carte', '📋 Liste Complète'], horizontal=True)
    st.markdown('---')
    total_filtered = len(f_list)
    mastered_in_filter = len([f for f in f_list if f['id'] in st.session_state.fc_mastered])
    pct_mastered = mastered_in_filter / total_filtered * 100 if total_filtered > 0 else 0
    st.progress(mastered_in_filter / max(1, total_filtered))
    st.caption(f'🏆 **Progression sur la sélection** : {mastered_in_filter} / {total_filtered} cartes maîtrisées ({pct_mastered:.1f}%)')
    if mode_fc == '🎴 Carte par Carte':
        if 'fc_idx' not in st.session_state:
            st.session_state.fc_idx = 0
        if st.session_state.fc_idx >= len(f_list):
            st.session_state.fc_idx = 0
        cur_fc = f_list[st.session_state.fc_idx]
        is_mastered = cur_fc['id'] in st.session_state.fc_mastered
        st.markdown(f'**Domaine :** `{cur_fc["module"]}` | **Chapitre :** *{cur_fc["chap"]}* | **Carte `{st.session_state.fc_idx + 1} / {len(f_list)}`**')
        if is_mastered:
            st.success('✅ Carte enregistrée comme **Maîtrisée**')
        else:
            st.info("⏳ Carte en cours d'apprentissage")
        st.markdown(f"\n        <div class='ciel-card' style='border-left: 6px solid #2563eb !important; background: #f8fafc;'>\n            <h3 style='color: #1e3a8a; margin-top: 0;'>❓ Question :</h3>\n            <p style='font-size: 1.15rem; font-weight: 600; color: #0f172a;'>{cur_fc['q']}</p>\n        </div>\n        ", unsafe_allow_html=True)
        user_fc_ans = st.text_area('✍️ Rédigez votre réponse réflexe avant de vérifier :', key=f'fc_txt_{cur_fc["id"]}')
        rev = st.checkbox('👁️ Afficher la Solution & Conseils Examen', key=f'rev_{cur_fc["id"]}')
        if rev:
            st.markdown('---')
            st.markdown('### ✅ Solution Détaillée & Fiche Réflexe')
            st.markdown(f'**Réponse attendue :**\n{cur_fc["a"]}')
            st.markdown(f'{cur_fc["note"]}')
            st.info(f'**{cur_fc["cours_ref"]}**')
            yt_link = yt_prefix + cur_fc['v_id']
            st.markdown(f'#### 📹 Leçon Vidéo Recommandée : *{cur_fc["v_title"]}*')
            st.link_button('▶️ Regarder la leçon sur YouTube', yt_link, type='primary')
        st.markdown('<br>', unsafe_allow_html=True)
        bcol1, bcol2, bcol3, bcol4 = st.columns(4)
        with bcol1:
            if st.button('⬅️ Précédente', use_container_width=True):
                st.session_state.fc_idx = (st.session_state.fc_idx - 1) % len(f_list)
                st.rerun()
        with bcol2:
            if st.button('✅ Maîtrisée', use_container_width=True):
                st.session_state.fc_mastered.add(cur_fc['id'])
                st.success('Carte ajoutée aux acquis !')
                st.rerun()
        with bcol3:
            if st.button('❌ À Revoir', use_container_width=True):
                st.session_state.fc_mastered.discard(cur_fc['id'])
                st.warning('Carte conservée dans la liste de révision.')
                st.rerun()
        with bcol4:
            if st.button('➡️ Suivante', use_container_width=True):
                st.session_state.fc_idx = (st.session_state.fc_idx + 1) % len(f_list)
                st.rerun()
    else:
        st.markdown(f'### 📋 Liste des {len(f_list)} Flashcards sélectionnées')
        for fc in f_list:
            m_status = '✅' if fc['id'] in st.session_state.fc_mastered else '⏳'
            with st.expander(f'{m_status} Carte N°{fc["id"]} : {fc["q"]}'):
                st.markdown(f'**Module :** `{fc["module"]}` | **Chapitre :** *{fc["chap"]}*')
                st.markdown(f'**Réponse :** {fc["a"]}')
                st.markdown(f'{fc["note"]}')
                st.info(f'**{fc["cours_ref"]}**')
                yt_link = yt_prefix + fc['v_id']
                st.link_button(f'▶️ Vidéo : {fc["v_title"]}', yt_link)



elif page == '🔍 Lab Décodeur Wireshark':
    st.markdown("<div class='hero-title'>🔍 Lab Décodeur Wireshark</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Apprenez à décoder les octets hexadécimaux bruts d'une capture réseau</p>", unsafe_allow_html=True)
    st.markdown("\n    <div class='terminal-header'>\n        <span class='terminal-dot dot-red'></span>\n        <span class='terminal-dot dot-yellow'></span>\n        <span class='terminal-dot dot-green'></span>\n        &nbsp; capture_reseau_brute_ipv4.hex (20 Octets En-tête IP)\n    </div>\n    <div class='terminal-body'>\n    Octet n° : 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19<br>\n    Données  : <b>45 00 00 3C 1C 2D 40 00 40 06 A8 B2 C0 A8 0A 05 C0 A8 0A 01</b>\n    </div>", unsafe_allow_html=True)
    st.markdown('### Décryptage des champs du paquet :')
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        ans_ver = st.selectbox("Version IP (Premier nibble '4') :", ['IPv4 (4)', 'IPv6 (6)'])
        ans_ihl = st.number_input("Longueur de l'en-tête (IHL) en mots de 32 bits (Deuxième nibble '5') :", min_value=0, max_value=15, value=0)
        ans_ttl = st.number_input("TTL décimal (Octet 8 : hex '40') :", min_value=0, max_value=255, value=0)
    with col_w2:
        ans_proto = st.selectbox("Protocole encapsulé (Octet 9 : hex '06') :", ['ICMP (1)', 'TCP (6)', 'UDP (17)'])
        ans_src = st.text_input("IP Source décodée (Octets 12-15 : 'C0 A8 0A 05') :", placeholder='Format: X.X.X.X')
        ans_dst = st.text_input("IP Destination décodée (Octets 16-19 : 'C0 A8 0A 01') :", placeholder='Format: X.X.X.X')
    if st.button("Valider l'analyse de trame", type='primary'):
        ok = ans_ver == 'IPv4 (4)' and ans_ihl == 5 and (ans_ttl == 64) and (ans_proto == 'TCP (6)') and (ans_src.strip() == '192.168.10.5') and (ans_dst.strip() == '192.168.10.1')
        if ok:
            st.balloons()
            st.success("🏆 **Décodage parfait ! Vous maîtrisez l'anatomie de l'en-tête IPv4.**")
        else:
            st.error('❌ **Certains champs sont incorrects.**')
            st.info('💡 **Aide** : C0 = 192, A8 = 168, 0A = 10, 05 = 5 $\\rightarrow$ `192.168.10.5` | TTL 0x40 = 64 en décimal.')



elif page == '💻 Sandboxes & Terminaux Pratiques':
    render_extended_lab()


elif page == "📝 Grand Quiz d'Examen":
    st.markdown("<div class='hero-title'>📝 Simulateur de Questionnaires Personnalisés & Marathons</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Configurez votre session de révision : du quiz standard de 10 questions au méga-marathon de 40 questions !</p>", unsafe_allow_html=True)
    st.markdown("<div class='ciel-card'>", unsafe_allow_html=True)
    col_cfg1, col_cfg2, col_cfg3 = st.columns([1.5, 1.5, 1])
    with col_cfg1:
        quiz_type = st.selectbox('Format du questionnaire :', ['Standard (10 questions)', 'Moyen (20 questions)', 'Marathon (30 questions)', 'Méga-Marathon (40 questions)', 'Intégral (Toutes les questions)'])
    with col_cfg2:
        selected_mod_filter = st.selectbox('Filtrer par domaine technique :', ['Tous les domaines', '📶 Réseaux & Télécoms', '🔒 Cybersécurité', '💻 Programmation / Dev', '🖥️ Administration Système', '🔌 Électronique & IoT', '📐 Modélisation UML & SysML'])
    with col_cfg3:
        st.markdown("<div style='padding-top:24px;'></div>", unsafe_allow_html=True)
        if st.button('🚀 Générer le Questionnaire', use_container_width=True, type='primary') or 'active_quiz' not in st.session_state:
            count_map = {'Standard (10 questions)': 10, 'Moyen (20 questions)': 20, 'Marathon (30 questions)': 30, 'Méga-Marathon (40 questions)': 40, 'Intégral (Toutes les questions)': len(GRAND_QUIZ_DATA)}
            limit = count_map.get(quiz_type, 10)
            pool = GRAND_QUIZ_DATA
            if selected_mod_filter != 'Tous les domaines':
                pool = [q for q in GRAND_QUIZ_DATA if q['mod'] == selected_mod_filter]
            sample_size = min(limit, len(pool))
            if sample_size > 0:
                st.session_state.active_quiz = random.sample(pool, sample_size)
            else:
                st.session_state.active_quiz = []
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    if not st.session_state.get('active_quiz', []):
        st.warning('Aucune question ne correspond à vos critères de filtrage. Veuillez sélectionner un autre domaine ou générer à nouveau.')
    else:
        active_q = st.session_state.active_quiz
        st.info(f"📋 **Questionnaire actif** : {len(active_q)} questions générées (Domaine : *{selected_mod_filter}*). Répondez ci-dessous puis cliquez sur 'Soumettre mon questionnaire'.")
        scores = {}
        for idx, q_item in enumerate(active_q):
            st.markdown(f'### Q{idx + 1} : {q_item["q"]}')
            st.markdown(f'**Domaine :** `{q_item["mod"]}` | **Chapitre :** *{q_item["chap"]}*')
            key_ans = f'active_q_ans_{idx}'
            user_sel = st.radio('Sélectionnez votre réponse :', q_item['options'], key=key_ans, disabled=st.session_state.quiz_submitted)
            scores[idx] = (user_sel, q_item['rep'], q_item['expl'], q_item['mod'], q_item['chap'])
            st.markdown("<hr style='border: 1px dashed #e2e8f0; margin: 15px 0;'/>", unsafe_allow_html=True)
        if not st.session_state.quiz_submitted:
            if st.button('📥 Soumettre mon questionnaire', use_container_width=True, type='primary'):
                st.session_state.quiz_submitted = True
                st.rerun()
        if st.session_state.quiz_submitted:
            total_correct = 0
            wrong_answers = []
            details_stats = {'Réseaux': 0, 'Cybersécurité': 0, 'Prog': 0, 'SysAdmin': 0, 'Elec': 0, 'UML': 0}
            for idx, (user_sel, rep, expl, m_ref, c_ref) in scores.items():
                k_mod = 'Réseaux'
                if 'Cyber' in m_ref:
                    k_mod = 'Cybersécurité'
                elif 'Prog' in m_ref:
                    k_mod = 'Prog'
                elif 'SysAdmin' in m_ref:
                    k_mod = 'SysAdmin'
                elif 'Élec' in m_ref:
                    k_mod = 'Elec'
                elif 'Modélisation' in m_ref:
                    k_mod = 'UML'
                if user_sel == rep:
                    total_correct += 1
                    details_stats[k_mod] += 1
                else:
                    wrong_answers.append({'num': idx + 1, 'mod': m_ref, 'chap': c_ref, 'user_sel': user_sel, 'rep': rep, 'expl': expl})
            save_score(total_correct, len(active_q), details_stats)
            st.markdown('## 📊 Votre Bilan du Questionnaire')
            pct = total_correct / len(active_q)
            st.progress(pct)
            st.markdown(f"<div style='font-size: 1.5rem; font-weight: 700; color: #1e3a8a;'>Votre score final : {total_correct} / {len(active_q)} ({pct * 100:.1f}%)</div>", unsafe_allow_html=True)
            if pct >= 0.8:
                st.success("🏆 **Niveau d'Excellence atteint !** Vos connaissances techniques sont extrêmement solides. Prêt pour l'examen final !")
            elif pct >= 0.5:
                st.info('👍 **Bon niveau global !** La plupart des concepts sont acquis. Revoyez vos erreurs pour viser la perfection.')
            else:
                st.warning('⚠️ **Niveau fragile.** Prenez le temps de bien relire vos fiches de cours ci-dessous pour combler vos lacunes.')
            if wrong_answers:
                st.markdown('---')
                st.markdown('### 🔄 Pont de Correction Automatique')
                st.write('Le système a identifié des erreurs. Voici les explications et les fiches de cours correspondantes pour vous corriger :')
                for w in wrong_answers:
                    st.error(f'**Question {w["num"]} ({w["mod"]} - {w["chap"]})**')
                    st.write(f'Votre choix : *{w["user_sel"]}* | Bonne réponse : **{w["rep"]}**')
                    st.info(f"💡 *Explication de l'expert : {w['expl']}*")
                    try:
                        c_txt = COURS_BASE[w['mod']][w['chap']]
                        with st.expander(f'📖 Relire la fiche de cours : {w["chap"]}', expanded=True):
                            st.markdown(c_txt)
                    except:
                        pass
            if st.button('🔄 Lancer un nouveau Questionnaire', use_container_width=True):
                st.session_state.quiz_submitted = False
                st.session_state.active_quiz = []
                st.rerun()



elif page == '📈 Analyse des Scores':
    render_page_analyse_scores()


elif page == '📋 Planning de Projet E6 (Gantt)':
    st.markdown("<div class='hero-title'>📋 Planning de Projet E6 & Diagramme de Gantt</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Gérez vos jalons de projet et générez votre planning pour votre soutenance finale</p>", unsafe_allow_html=True)
    PROJ_FILE = 'e6_tasks_v7.json'
    if os.path.exists(PROJ_FILE):
        try:
            with open(PROJ_FILE, 'r') as f:
                t_data = json.load(f)
        except:
            t_data = []
    else:
        td = datetime.now().date()
        t_data = [{'nom': '1. Cahier des charges & CdCf', 'debut': (td - timedelta(days=25)).strftime('%Y-%m-%d'), 'fin': (td - timedelta(days=15)).strftime('%Y-%m-%d'), 'avancement': 100, 'resp': 'Équipe'}, {'nom': '2. Modélisation SysML & UML', 'debut': (td - timedelta(days=15)).strftime('%Y-%m-%d'), 'fin': (td - timedelta(days=5)).strftime('%Y-%m-%d'), 'avancement': 100, 'resp': 'Étudiant A'}, {'nom': '3. Développement C++ & Pilotes SPI', 'debut': (td - timedelta(days=5)).strftime('%Y-%m-%d'), 'fin': (td + timedelta(days=10)).strftime('%Y-%m-%d'), 'avancement': 60, 'resp': 'Étudiant A'}, {'nom': '4. Passerelle Python & Base de Données', 'debut': td.strftime('%Y-%m-%d'), 'fin': (td + timedelta(days=15)).strftime('%Y-%m-%d'), 'avancement': 30, 'resp': 'Étudiant B'}, {'nom': '5. Sécurisation TLS & Durcissement Linux', 'debut': (td + timedelta(days=10)).strftime('%Y-%m-%d'), 'fin': (td + timedelta(days=22)).strftime('%Y-%m-%d'), 'avancement': 0, 'resp': 'Étudiant B'}, {'nom': '6. Plan de Validation Logicielle (PVL)', 'debut': (td + timedelta(days=20)).strftime('%Y-%m-%d'), 'fin': (td + timedelta(days=30)).strftime('%Y-%m-%d'), 'avancement': 0, 'resp': 'Équipe'}]
        with open(PROJ_FILE, 'w') as f:
            json.dump(t_data, f)
    c_g1, c_g2 = st.columns([1, 2])
    with c_g1:
        st.subheader('Ajouter une tâche de projet :')
        with st.form('f_t'):
            t_nom = st.text_input('Nom de la tâche :', "7. Dossier d'examen et soutenance")
            t_deb = st.date_input('Date de début :', datetime.now().date())
            t_fin = st.date_input('Date de fin :', datetime.now().date() + timedelta(days=12))
            t_pct = st.slider('Avancement (%) :', 0, 100, 0)
            t_r = st.text_input('Responsable :', 'Mon Nom')
            if st.form_submit_button('Ajouter au planning'):
                t_data.append({'nom': t_nom, 'debut': t_deb.strftime('%Y-%m-%d'), 'fin': t_fin.strftime('%Y-%m-%d'), 'avancement': t_pct, 'resp': t_r})
                with open(PROJ_FILE, 'w') as f:
                    json.dump(t_data, f)
                st.rerun()
    with c_g2:
        st.subheader('Planning de Gantt Dynamique')
        if t_data:
            fig, ax = plt.subplots(figsize=(9, 4.5))
            y_pos = []
            y_labels = []
            for i, tk in enumerate(reversed(t_data)):
                s_d = datetime.strptime(tk['debut'], '%Y-%m-%d')
                e_d = datetime.strptime(tk['fin'], '%Y-%m-%d')
                dur = (e_d - s_d).days
                pct_v = tk['avancement']
                ax.barh(i, dur, left=s_d, color='#e2e8f0', edgecolor='#94a3b8', height=0.5)
                bar_c = '#10b981' if pct_v == 100 else '#3b82f6'
                ax.barh(i, dur * (pct_v / 100.0), left=s_d, color=bar_c, height=0.5)
                y_pos.append(i)
                y_labels.append(f'{tk["nom"]}\\n({tk["resp"]} - {pct_v}%)')
            ax.set_yticks(y_pos)
            ax.set_yticklabels(y_labels, fontsize=8)
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
            plt.title('Planning de Gantt du Projet E6', fontsize=12, fontweight='bold', color='#1e3a8a')
            plt.grid(axis='x', linestyle='--', alpha=0.5)
            plt.tight_layout()
            g_path = '/workspace/scratch/gantt_chart_v7.png'
            plt.savefig(g_path, dpi=150)
            plt.close()
            st.image(g_path)



elif page == '📄 Datasheets & Fiches Techniques (Composants)':
    st.markdown("<div class='hero-title'>📄 Datasheets & Fiches Techniques de Composants (en Anglais)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Guide d'analyse et de décodage des fiches constructeurs pour l'épreuve écrite E4 et les travaux pratiques E5/E6</p>", unsafe_allow_html=True)
    tab_ds1, tab_ds2, tab_ds3, tab_ds4, tab_ds5 = st.tabs(['⚙️ Microcontrôleurs 8/32 bits', '🔌 Bus & Transceivers (MCP2515/MAX485)', '⚡ Drivers Moteurs & Puissance', '🌡️ Capteurs Industriels (4-20mA/MAX6675)', '✍️ Quiz Datasheets & Anglais Technique'])
    with tab_ds1:
        st.subheader('1. Microcontrôleurs 8 bits & 32 bits (ATmega328P, ESP32, STM32)')
        st.markdown('\n        #### 🔹 ATmega328P (Microchip / Atmel 8-bit AVR)\n        * **Features** : High Performance 8-bit AVR RISC Architecture, 32 KB Flash, 2 KB SRAM, 1 KB EEPROM, 16 MHz Clock Speed.\n        * **Key Registers for Timers & PWM** :\n          - `TCCR1A` / `TCCR1B` (*Timer/Counter1 Control Register*) : Configures Waveform Generation Mode (Fast PWM, Phase Correct) and Clock Prescaler ($1, 8, 64, 256, 1024$).\n          - `OCR1A` / `OCR1B` (*Output Compare Register*) : Holds the 16-bit value compared with the counter value to adjust the PWM duty cycle.\n        * **USART Control Registers** :\n          - `UBRR0H` / `UBRR0L` (*USART Baud Rate Register*) :\n            $$\\text{UBRR0} = \\frac{F_{\\text{OSC}}}{16 \\times \\text{Baud}} - 1$$\n            *Example for 9600 Baud @ 16 MHz* : $\\text{UBRR0} = \\frac{16000000}{16 \\times 9600} - 1 = 103,16 \\Rightarrow \\mathbf{103} \\quad (0x0067)$.\n\n        #### 🔹 ESP32 (Espressif Systems 32-bit Dual-Core Xtensa LX6)\n        * **Features** : Tensilica LX6 @ 240 MHz, 520 KB SRAM, Integrated 2.4 GHz Wi-Fi 802.11 b/g/n & Bluetooth 4.2 / BLE.\n        * **Low Power Modes** : Active Mode, Modem-sleep, Light-sleep, **Deep-sleep** (RTC Memory active, current consumption down to $10~\\mu\\text{A}$).\n        * **Peripherals** : 12-bit SAR ADC (up to 18 channels), Capacitive Touch, DAC, I2C, SPI, UART, PWM (LEDC controller).\n\n        #### 🔹 STM32F4 (STMicroelectronics ARM Cortex-M4 32-bit)\n        * **Core** : 32-bit ARM Cortex-M4 with FPU (Floating Point Unit) @ 84 MHz / 180 MHz, DSP instructions.\n        * **HAL Architecture** : Hardware Abstraction Layer (`HAL_GPIO_WritePin()`, `HAL_UART_Transmit()`, `HAL_ADC_Start()`).\n        ')
        st.info("💡 **Conseil Examen E4** : Quand un extrait de datasheet en anglais est fourni dans le sujet, repérez immédiatement le tableau **'Absolute Maximum Ratings'** (tensions/courants limites) et le chapitre **'Register Description'** pour identifier le rôle de chaque bit.")
    with tab_ds2:
        st.subheader('2. Contrôleurs de Bus & Transceivers (MCP2515, MAX485, SN75176)')
        st.markdown('\n        #### 🔹 MCP2515 (Microchip Standalone CAN Controller with SPI)\n        * **Role** : Implements CAN Specification V2.0B at up to 1 Mb/s over an SPI interface.\n        * **SPI Commands** :\n          - `RESET` (`0xC0`) : Resets internal registers to default state.\n          - `READ` (`0x03`) : Reads data from the register at selected address.\n          - `WRITE` (`0x02`) : Writes data to selected register.\n          - `BIT MODIFY` (`0x05`) : Modifies specific bits in control registers (`CANCTRL`, `BFPCTRL`).\n        * **Acceptance Filters & Masks** :\n          - `RXF0` to `RXF5` (*Filter Registers*) : Define the exact 11-bit or 29-bit CAN IDs accepted by the node.\n          - `RXM0`, `RXM1` (*Mask Registers*) : Bits set to `1` mean "check filter bit", bits set to `0` mean "don\'t care".\n\n        #### 🔹 MAX485 / SN75176 (RS-485 Transceiver)\n        * **Features** : Low-power transceiver for RS-485 and RS-422 communication, Half-Duplex, differential transmission lines `A` and `B`.\n        * **Control Pins** :\n          - `RO` (*Receiver Output*) : Connected to MCU Rx.\n          - `RE` (*Receiver Enable*) : Active Low ($\\overline{\\text{RE}}$). Set `0` to enable receiver.\n          - `DE` (*Driver Enable*) : Active High. Set `1` to enable transmitter.\n          - `DI` (*Driver Input*) : Connected to MCU Tx.\n        * **Common Wiring Tip** : Connect `RE` and `DE` together to a single MCU GPIO pin (`DIR`). Set `DIR = 1` for Transmission (Tx) and `DIR = 0` for Reception (Rx).\n        ')
    with tab_ds3:
        st.subheader('3. Drivers de Moteurs & Electronique de Puissance (BTS7960, L298N)')
        st.markdown('\n        #### 🔹 BTS7960 (Infineon High Current PN Half Bridge - 43A)\n        * **Application** : High power DC motor drive up to 43A continuous under 6V to 28V.\n        * **Pin Functionality** :\n          - `R_IS` / `L_IS` (*Current Sense Output*) : Provides a current proportional to motor load for overload detection.\n          - `R_EN` / `L_EN` (*Enable Inputs*) : Logic High enables right/left half bridge.\n          - `RPWM` / `LPWM` (*PWM Control Inputs*) : Speed control input up to 25 kHz.\n        * **Protection Features** : Over-temperature shutdown, Short-circuit protection, Under-voltage lockout.\n\n        #### 🔹 L298N (STMicroelectronics Dual Full-Bridge Driver)\n        * **Features** : Integrated dual H-bridge driver up to 46V and 2A per channel.\n        * **Flyback Diodes Requirement** : Inductive loads (motors, relays) require 8 external fast-recovery freewheeling diodes to absorb back-EMF spikes ($e = -L \\frac{di}{dt}$).\n        ')
    with tab_ds4:
        st.subheader('4. Capteurs Industriels (DHT22, BME280, MAX6675, Boucles 4-20mA)')
        st.markdown('\n        #### 🔹 MAX6675 (Thermocouple K-Type to Digital Converter)\n        * **Interface** : SPI Read-Only (3-wire: `SO`, `CS`, `SCK`).\n        * **Resolution** : 12-bit ADC with 0.25°C resolution over 0°C to +1024°C range.\n        * **Open Thermocouple Detection** : Bit D2 goes HIGH when the thermocouple wire is broken.\n\n        #### 🔹 Boucle de Courant Industrielle 4-20 mA\n        * **Datasheet Specification** : Output current $I_{\\text{out}}$ varies linearly from $4\\text{ mA}$ (minimum scale) to $20\\text{ mA}$ (maximum scale).\n        * **Conversion Formula** :\n          $$I = 4 + \\frac{T - T_{\\text{min}}}{T_{\\text{max}} - T_{\\text{min}}} \\times 16 \\quad [\\text{mA}]$$\n        ')
    with tab_ds5:
        st.subheader('✍️ Quiz Datasheets & Anglais Technique Composants')
        q1 = st.radio('1. What is the value of UBRR0 for 9600 Baud under a 16 MHz clock on an ATmega328P?', ['103', '207', '51', '128'], key='ds_q1')
        q2 = st.radio('2. On a MAX485 transceiver, what pin state enables Transmit mode?', ['DE = 1, RE = 1', 'DE = 0, RE = 0', 'DE = 1, RE = 0', 'DE = 0, RE = 1'], key='ds_q2')
        if st.button('Check Datasheets Quiz', type='primary', key='btn_ds_quiz'):
            score = 0
            if q1 == '103':
                score += 1
            if q2 == 'DE = 1, RE = 1' or q2 == 'DE = 1, RE = 0':
                score += 1
            st.success(f'Score : **{score} / 2**')



elif page == '🔍 Captures de Trames & Analyses Wireshark PCAP':
    st.markdown("<div class='hero-title'>🔍 Captures de Trames & Analyses Wireshark PCAP Commentées</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Décryptage pas-à-pas de paquets réseaux réels, captures de trames industrielles et simulateur d'analyse d'examen</p>", unsafe_allow_html=True)
    tab_pc1, tab_pc2, tab_pc3, tab_pc4, tab_pc5 = st.tabs(['🌐 TCP/IP & Handshake 3-Way', '⚙️ Services Réseaux (DHCP & DNS)', '🏭 Bus Industriels (Modbus & CAN)', '🔒 Sessions TLS 1.3 & SSH', "✍️ Simulateur d'Analyse Hex"])
    with tab_pc1:
        st.subheader('1. Établissement de Connexion TCP (Handshake 3-Way) & Fermeture')
        st.markdown('\n        #### 🔹 Trame #1 : Client $\\rightarrow$ Serveur (SYN)\n        ```text\n        Frame 1: 66 bytes on wire\n        Ethernet II, Src: 00:0c:29:1f:8a:12, Dst: 00:50:56:a1:02:bb\n        Internet Protocol Version 4, Src: 192.168.10.15, Dst: 192.168.10.254\n        Transmission Control Protocol, Src Port: 49152, Dst Port: 80, Seq: 0, Flags: 0x002 (SYN)\n            Source Port: 49152\n            Destination Port: 80\n            Sequence Number: 0 (relative sequence number)\n            Header Length: 32 bytes\n            Flags: 0x002 (SYN)\n            Window: 64240\n            MSS: 1460 bytes\n        ```\n        * **Analyse** : Le client (`192.168.10.15`) envoie un paquet TCP avec le bit **SYN** activé (`Flags: 0x002`) sur le port HTTP 80 du serveur (`192.168.10.254`). Son numéro de séquence initial relatif est `Seq = 0`. Le MSS (*Maximum Segment Size*) négocié est de `1460 octets`.\n\n        #### 🔹 Trame #2 : Serveur $\\rightarrow$ Client (SYN-ACK)\n        ```text\n        Frame 2: 66 bytes on wire\n        Transmission Control Protocol, Src Port: 80, Dst Port: 49152, Seq: 0, Ack: 1, Flags: 0x012 (SYN, ACK)\n            Sequence Number: 0\n            Acknowledgment Number: 1 (relative ack)\n            Flags: 0x012 (SYN, ACK)\n        ```\n        * **Analyse** : Le serveur répond avec les bits **SYN** et **ACK** (`Flags: 0x012`). Il valide le paquet SYN reçu en renvoyant `Ack = 1` ($0 + 1$).\n\n        #### 🔹 Trame #3 : Client $\\rightarrow$ Serveur (ACK)\n        ```text\n        Frame 3: 54 bytes on wire\n        Transmission Control Protocol, Src Port: 49152, Dst Port: 80, Seq: 1, Ack: 1, Flags: 0x010 (ACK)\n        ```\n        * **Analyse** : La connexion TCP est **ESTABLISHED**. Les données applicatives HTTP peuvent maintenant transiter.\n        ')
    with tab_pc2:
        st.subheader('2. Services Infrastructure : DHCP DORA & DNS')
        st.markdown('\n        #### 🔹 Processus DHCP DORA (Dynamic Host Configuration Protocol)\n        ```text\n        1. DHCP Discover : Src IP 0.0.0.0 -> Dst IP 255.255.255.255 (UDP 67->68) [Option 53 = 1]\n        2. DHCP Offer    : Src IP 192.168.1.254 -> Dst IP 192.168.1.50 (UDP 68->67) [Option 53 = 2, Offered IP = 192.168.1.50]\n        3. DHCP Request  : Src IP 0.0.0.0 -> Dst IP 255.255.255.255 (UDP 67->68) [Option 53 = 3, Requested IP = 192.168.1.50]\n        4. DHCP ACK      : Src IP 192.168.1.254 -> Dst IP 192.168.1.50 (UDP 68->67) [Option 53 = 5, Lease Time = 86400s]\n        ```\n        * **Options DHCP Clés à Connaître pour E5/E4** :\n          - **Option 53** : DHCP Message Type (1=Discover, 2=Offer, 3=Request, 5=ACK, 6=NAK).\n          - **Option 1** : Subnet Mask (ex: `255.255.255.0`).\n          - **Option 3** : Router / Default Gateway (ex: `192.168.1.254`).\n          - **Option 6** : DNS Servers (ex: `192.168.1.10`).\n          - **Option 15** : Domain Name (ex: `ciel.local`).\n\n        #### 🔹 Requête DNS (Domain Name System)\n        ```text\n        Domain Name System (query)\n            Transaction ID: 0x2a1b\n            Flags: 0x0100 Standard query\n            Questions: 1\n                srv-web.ciel.local: type A, class IN\n        ```\n        ')
    with tab_pc3:
        st.subheader('3. Bus Industriels : Modbus RTU sur RS-485 & Trames Bus CAN')
        st.markdown("\n        #### 🔹 Trame Modbus RTU (Lecture de Registres - Function Code 03)\n        ```text\n        Trame Hexadécimale de Requête : [ 01 ] [ 03 ] [ 00 6B ] [ 00 03 ] [ 76 87 ]\n        - 01    : Adresse Esclave (Slave ID = 1)\n        - 03    : Code Fonction (03 = Read Holding Registers)\n        - 00 6B : Adresse du Premier Registre (107 en décimal)\n        - 00 03 : Nombre de Registres à Lire (3 registres = 6 octets)\n        - 76 87 : Contrôle d'erreur CRC-16 (Cyclic Redundancy Check)\n\n        Trame Hexadécimale de Réponse : [ 01 ] [ 03 ] [ 06 ] [ 02 2B ] [ 00 00 ] [ 01 00 ] [ C5 A1 ]\n        - 01    : Adresse Esclave\n        - 03    : Code Fonction\n        - 06    : Nombre d'Octets de Données Renvoyés (6 octets)\n        - 02 2B : Valeur Registre 107 (555 en décimal -> Température 55.5°C)\n        - 00 00 : Valeur Registre 108 (0)\n        - 01 00 : Valeur Registre 109 (256)\n        - C5 A1 : CRC-16 de validation\n        ```\n\n        #### 🔹 Trame Bus CAN 2.0A (Standard 11-bit ID)\n        ```text\n        Controller Area Network (CAN)\n            [SOF] Start of Frame : 0 (bit dominant)\n            Arbitration Field : Identifier = 0x3A4 (11 bits) [RTR = 0 Data Frame]\n            Control Field : DLC = 4 (Data Length Code = 4 octets)\n            Data Field : 12 34 56 78\n            CRC Field : 15 bits CRC + Delimiter\n            ACK Field : Slot (1 bit écrasé par le récepteur)\n        ```\n        ")
    with tab_pc4:
        st.subheader('4. Tunnels Sécurisés : TLS 1.3 / HTTPS & SSH')
        st.markdown('\n        #### 🔹 Handshake TLS 1.3 (Transport Layer Security)\n        ```text\n        1. Client Hello :\n           - Supported Versions : TLS 1.3, TLS 1.2\n           - Key Share : Offre de clé publique Diffie-Hellman (ECDHE_RSA)\n           - Extension SNI (Server Name Indication) : srv-app.ciel.fr\n        2. Server Hello :\n           - Version sélectionnée : TLS 1.3\n           - Cipher Suite : TLS_AES_256_GCM_SHA384\n           - Certificate : Certificat X.509 du serveur transmis\n           - Finished : Validation chiffrée\n        3. Application Data : Trafic HTTPS 100% chiffré.\n        ```\n        ')
    with tab_pc5:
        st.subheader("✍️ Simulateur d'Analyse de Trame Hexadécimale")
        st.markdown('**Trame à Analyser** : `00 0c 29 1f 8a 12 00 50 56 a1 02 bb 08 00 45 00`')
        q_p1 = st.radio('Quel est le protocole de Couche 3 indiqué par `EtherType = 0x0800` ?', ['IPv6', 'IPv4', 'ARP', 'VLAN 802.1Q'], key='pcap_q1')
        if st.button('Valider Analyse Hex', type='primary', key='btn_pcap'):
            if q_p1 == 'IPv4':
                st.success('🎉 **Exact !** EtherType `0x0800` désigne le protocole IPv4 (`0x0806` pour ARP, `0x86DD` pour IPv6, `0x8100` pour VLAN 802.1Q).')
            else:
                st.error("❌ Incorrect. `0x0800` est l'EtherType d'IPv4.")



elif page == '📁 Modèles de Livrables & PVL Épreuve E6':
    st.markdown("<div class='hero-title'>📁 Modèles de Livrables & PVL (Épreuve E6 - Projet de Fin d'Études)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Gabarits officiels, cahier des charges AFNOR, matrice de traçabilité des exigences, et scripts de tests d'intégration Pytest</p>", unsafe_allow_html=True)
    tab_e6_1, tab_e6_2, tab_e6_3, tab_e6_4, tab_e6_5 = st.tabs(['📋 Cahier des Charges AFNOR (CdCf)', '📐 Matrice de Traçabilité ReqIF', '🧪 Plan de Validation (PVL & Pytest)', '📜 Dossier de Recette (FAT/SAT)', '✍️ Auto-Évaluation Livrables E6'])
    with tab_e6_1:
        st.subheader('1. Structure Normée du Cahier des Charges Fonctionnel (CdCf - Norme NF X50-151)')
        st.markdown("\n        #### 🔹 1. Présentation Générale du Projet\n        * **Intitulé du Projet** : Système de Surveillance Industrielle et Passerelle Multi-Protocoles IoT.\n        * **Demandeur / Client** : Direction des Systèmes d'Information (DSI).\n        * **Objectif Métier** : Remonter en temps réel les mesures de température et de pression d'un parc de machines via le réseau Modbus RTU vers un serveur Cloud sécurisé en MQTTS.\n\n        #### 🔹 2. Analyse Fonctionnelle du Besoin (Diagramme Pieuvre / APTE)\n        * **Fonctions Principales (FP)** :\n          - **FP1** : Acquérir les données physiques de la chaîne de production via le bus RS-485 Modbus.\n          - **FP2** : Transmettre de manière chiffrée (MQTTS / TLS 1.3) les télémesures vers le Broker central.\n        * **Fonctions de Contrainte (FC)** :\n          - **FC1** : Respecter les contraintes d'alimentation électrique industrielle ($24\\text{V DC} \\pm 10\\%$).\n          - **FC2** : Assurer une autonomie minimale sur batterie de secours de $2\\text{ heures}$ en cas de coupure secteur.\n          - **FC3** : Respecter les réglementations RGPD et la politique de durcissement ANSSI.\n\n        #### 🔹 3. Caractérisation des Exigences Fonctionnelles\n        | Identifiant | Libellé de l'Exigence | Critère d'Appréciation | Niveau d'Exigence | Flexibilité |\n        | :--- | :--- | :--- | :--- | :--- |\n        | **REQ_ACQ_01** | Fréquence de rafraîchissement des mesures | Période d'échantillonnage | $1.0\\text{ seconde} \\pm 50\\text{ ms}$ | **F0 (Inflexible)** |\n        | **REQ_SEC_02** | Chiffrement des données en transit | Version du protocole TLS | TLS 1.3 obligatoire | **F0 (Inflexible)** |\n        | **REQ_NET_03** | Reprise automatique sur perte de lien Wi-Fi | Temps de reconnexion | $< 5.0\\text{ secondes}$ | **F1 (Peu flexible)** |\n        ")
    with tab_e6_2:
        st.subheader('2. Matrice de Traçabilité des Exigences (ReqIF / SysML)')
        st.markdown("\n        #### 🔹 Traçabilité Exigences $\\rightarrow$ Conception $\\rightarrow$ Tests de Qualification\n        La matrice de traçabilité garantit devant le jury E6 que **100% des exigences** énoncées dans le CdCf sont couvertes par un composant d'architecture et validées par un test d'intégration :\n\n        | Exigence CdCf | Bloc SysML / Classe UML | Fiche de Test PVL | Statut Recette |\n        | :--- | :--- | :--- | :--- |\n        | **REQ_ACQ_01** | Bloc `CapteurModbus` / Classe `ModbusMaster` | `TEST_ACQ_01.py` | **PASS (100%)** |\n        | **REQ_SEC_02** | Bloc `PasserelleMQTTS` / Classe `MqttClientTLS` | `TEST_SEC_02.py` | **PASS (100%)** |\n        | **REQ_NET_03** | Bloc `GestionnaireReseau` / Classe `WiFiWatchdog` | `TEST_NET_03.py` | **PASS (100%)** |\n        ")
    with tab_e6_3:
        st.subheader('3. Plan de Validation Logicielle (PVL) avec Scripts Automated Pytest')
        st.markdown('\n        #### 🔹 Code Python de Test d\'Intégration Automated (`test_pvl_passerelle.py`)\n        ```python\n        import pytest\n        import time\n        import socket\n        import json\n\n        # Test d\'intégration de l\'exigence REQ_ACQ_01 (Période d\'échantillonnage < 1s)\n        def test_req_acq_01_sampling_rate():\n            start_time = time.time()\n            # Simulation d\'acquisition de registre Modbus\n            data_sample = {"temp_celsius": 24.5, "pressure_bar": 2.1}\n            elapsed = time.time() - start_time\n            \n            assert elapsed < 1.0, f"Erreur REQ_ACQ_01 : temps d\'acquisition trop long ({elapsed:.3f}s)"\n            assert "temp_celsius" in data_sample\n            assert data_sample["temp_celsius"] > -40.0 and data_sample["temp_celsius"] < 125.0\n\n        # Test d\'intégration de l\'exigence REQ_SEC_02 (Vérification port MQTTS 8883)\n        def test_req_sec_02_mqtts_port_open():\n            host = "192.168.10.254"\n            port = 8883  # Port MQTTS sur TLS\n            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n            sock.settimeout(2.0)\n            \n            result = sock.connect_ex((host, port))\n            sock.close()\n            assert result == 0, f"Erreur REQ_SEC_02 : Le port MQTTS {port} est fermé sur {host}"\n        ```\n\n        * **Lancement du Test PVL** : `pytest -v test_pvl_passerelle.py`\n        ')
    with tab_e6_4:
        st.subheader('4. Dossier de Recette Technique (FAT / SAT & Procès-Verbal)')
        st.markdown('\n        #### 🔹 Procès-Verbal (PV) de Recette Finale\n        * **Date de Qualification** : 15 Juin 2026\n        * **Membres de la Commission** : Chef de Projet DSI, Expert Cybersécurité, Ingénieur Intégrateur.\n        * **Décision de Recette** :\n          - [x] **Prononcée Sans Réserve** : Le système répond entièrement aux spécifications.\n          - [ ] Prononcée Avec Réserves Mineures.\n          - [ ] Refusée pour Non-Conformité Majeure.\n        ')
    with tab_e6_5:
        st.subheader('✍️ Auto-Évaluation Livrables E6')
        q_e6_1 = st.radio("Quel outil de test Python standard est préconisé pour automatiser le PVL de l'épreuve E6 ?", ['unittest / pytest', 'Postman', 'Wireshark', 'OpenSSL'], key='e6_q1')
        if st.button('Valider Quiz E6', type='primary', key='btn_e6_q'):
            if 'pytest' in q_e6_1:
                st.success("🎉 **Exact !** `pytest` permet d'exécuter des assertions automatisées et de générer un rapport de qualification E6.")
            else:
                st.error('❌ Incorrect. `pytest` est le framework de test automatisé recommandé.')



elif page == '🛡️ Guides de Durcissement (Hardening) ANSSI':
    st.markdown("<div class='hero-title'>🛡️ Guides de Durcissement (Hardening) ANSSI & PSSI</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Règles de sécurité fondamentales publiées par l'ANSSI pour le durcissement de Linux Debian, Active Directory et des passerelles IoT</p>", unsafe_allow_html=True)
    tab_an1, tab_an2, tab_an3, tab_an4, tab_an5 = st.tabs(['🖥️ Hardening Linux Debian', '🏢 Durcissement Active Directory (Tiering)', '📶 Sécurisation Wi-Fi & IoT', '📜 PSSI & Directives ANSSI', '✍️ Quiz Hardening & Sécurité'])
    with tab_an1:
        st.subheader('1. Recommandations de Durcissement Linux Debian (Guide ANSSI - Niveau Intermédiaire)')
        st.markdown("\n        #### 🔹 1. Fichier de Configuration de Réseau & Noyau (`/etc/sysctl.d/99-anssi-hardening.conf`)\n        ```ini\n        # Désactiver le transfert d'IP (si le serveur n'est pas un routeur)\n        net.ipv4.ip_forward = 0\n        net.ipv6.conf.all.forwarding = 0\n\n        # Désactiver la réponse aux pings Broadcast (protection contre attaques Smurf)\n        net.ipv4.icmp_echo_ignore_broadcasts = 1\n\n        # Ignorer les fausses erreurs ICMP\n        net.ipv4.icmp_ignore_bogus_error_responses = 1\n\n        # Protection contre les attaques SYN Flood\n        net.ipv4.tcp_syncookies = 1\n\n        # Rejeter les redirections ICMP\n        net.ipv4.conf.all.accept_redirects = 0\n        net.ipv4.conf.default.accept_redirects = 0\n        ```\n        * Appliquer la configuration sysctl : `sysctl -p /etc/sysctl.d/99-anssi-hardening.conf`\n\n        #### 🔹 2. Durcissement du Daemon SSH (`/etc/ssh/sshd_config.d/anssi.conf`)\n        ```text\n        # Interdire la connexion directe du compte root\n        PermitRootLogin no\n\n        # Interdire l'authentification par mot de passe (clés SSH RSA 4096 / Ed25519 obligatoires)\n        PasswordAuthentication no\n        PubkeyAuthentication yes\n\n        # Changer le port standard pour limiter le bruit du scan automatisé\n        Port 2222\n\n        # Déconnexion automatique des sessions inactives (5 minutes)\n        ClientAliveInterval 300\n        ClientAliveCountMax 0\n\n        # Désactiver le transfert X11 et le forwarding\n        X11Forwarding no\n        AllowTcpForwarding no\n        ```\n\n        #### 🔹 3. Outil d'Audit de Conformité ANSSI : Lynis\n        * Installation : `apt update && apt install lynis`\n        * Lancement d'un audit de sécurité complet : `lynis audit system`\n        * *Hardening Index Target* : Viser un score de sécurité supérieur à **75/100**.\n        ")
    with tab_an2:
        st.subheader('2. Durcissement Active Directory : Le Modèle de Tiering à 3 Niveaux')
        st.markdown("\n        #### 🔹 Le Modèle de Partitionnement Administratif (Tiering Model)\n        Pour empêcher une compromission latérale (*Pass-the-Hash* / *Golden Ticket*), l'ANSSI impose une séparation stricte des privilèges :\n\n        ```text\n        [ TIER 0 ] Control Plane (Contrôleurs de Domaine, PKI Racine, Comptes Admin du Domaine)\n             |   (Etanche : Interdiction formelle de se connecter sur un Tier 1 ou Tier 2)\n             v\n        [ TIER 1 ] Server Plane (Serveurs Membres, Serveurs Web, Bases de Données)\n             |   (Étanche : Admin Tier 1 ne peut pas se connecter sur un Tier 2)\n             v\n        [ TIER 2 ] Workstation Plane (Postes de Travail Utilisateurs, Imprimantes)\n        ```\n\n        #### 🔹 Mesures Incontournables de Durcissement ADDS :\n        1. **Renouvellement Périodique du Compte KRBTGT** : Changer deux fois consécutivement le mot de passe du compte `krbtgt` pour invalider tout *Golden Ticket* compromis.\n        2. **Désactivation des Protocoles Vulnérables** :\n           - Désactiver **NTLMv1** au profit de Kerberos et NTLMv2.\n           - Désactiver **LLMNR** (*Link-Local Multicast Name Resolution*) et **NBT-NS** (*NetBIOS Name Service*) sur tous les postes membres via GPO.\n        3. **Déploiement de LAPS** (*Local Administrator Password Solution*) : Garantit que chaque poste de travail possède un mot de passe administrateur local unique, aléatoire et renouvelé tous les 30 jours.\n        ")
    with tab_an3:
        st.subheader("3. Sécurisation des Réseaux Wi-Fi d'Entreprise & Passerelles IoT")
        st.markdown("\n        #### 🔹 Architecture WPA3-Enterprise / 802.1X avec Serveur RADIUS\n        * **Chiffrement** : WPA3-Enterprise avec suite cryptographique GCMP-256 bits.\n        * **Authentification 802.1X** : Protocole **EAP-TLS** obligatoire (authentification mutuelle du poste client et du serveur via certificats X.509 délivrés par la PKI d'entreprise).\n        * **Segmentation IoT** : Isoler impérativement tous les équipements d'IoT industrielle dans un **VLAN dédié** restreint par un pare-feu pfSense (accès au LAN interdit).\n        ")
    with tab_an4:
        st.subheader("4. Synthèse de la Politique de Sécurité du Système d'Information (PSSI)")
        st.markdown("\n        #### 🔹 Les 4 Piliers DICP de la PSSI :\n        1. **Disponibilité (D)** : Garantir la continuité de service (Redondance, RAID, Onduleurs).\n        2. **Intégrité (I)** : Garantir l'absence de modification non autorisée (Hachage SHA-256, signatures).\n        3. **Confidentialité (C)** : Garantir que seules les personnes autorisées ont accès aux données (Chiffrement AES-256, ACLs).\n        4. **Preuve / Traçabilité (P)** : Conserver les journaux d'événements horodatés (Syslog centralisé, SIEM).\n        ")
    with tab_an5:
        st.subheader('✍️ Quiz Hardening & Sécurité Système')
        q_ans_1 = st.radio('Dans le modèle de Tiering ANSSI Active Directory, un administrateur Tier 0 a-t-il le droit de se connecter sur un poste de travail Tier 2 ?', ["Non, c'est strictement interdit (risque d'usurpation de jeton)", "Oui, c'est autorisé pour le dépannage"], key='ans_q1')
        if st.button('Valider Quiz Hardening', type='primary', key='btn_ans'):
            if 'Non' in q_ans_1:
                st.success('🎉 **Exact !** Les administrateurs Tier 0 ne doivent jamais se connecter sur un Tier 1 ou Tier 2 pour éviter le vol de leurs identifiants par une attaque Pass-the-Hash.')
            else:
                st.error("❌ Incorrect. L'isolation stricte des Tiers empêche la compromission du domaine.")



elif page == '🇬🇧 Vocabulaire & Anglais Technique BTS':
    st.markdown("<div class='hero-title'>🇬🇧 Vocabulaire & Anglais Technique BTS CIEL</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Module complet : Lexique bilingue, grammaire technique d'examen (passif, conditionnels, verbe BE), étude de cas d'incident critique et oraux</p>", unsafe_allow_html=True)

    tab_en1, tab_en2, tab_en3, tab_en4, tab_en5 = st.tabs([
        "📖 Lexique Bilingue (100+ Mots)",
        "📝 Grammaire Technique (Passif, Conditionnels, BE)",
        "🚨 Project 3 : Critical Incident",
        "📄 Texts & Technical Articles",
        "🗣️ Oral Presentation Guide"
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
* **Vulnerability / Flaw** : Vulnérabilité / Faille.
* **Tamper-resistant** : Résistant aux altérations matérielles.
* **Ciphertext / Plaintext** : Texte chiffré / Texte clair.
* **Denial of Service (DoS)** : Déni de service.
* **Phishing / Spoofing** : Hameçonnage / Usurpation d'identité.
            """)
        with col_lex2:
            st.markdown("""
#### 💻 Software & Systems
* **Pointer / Reference** : Pointeur / Référence mémoire.
* **Memory Leak** : Fuite de mémoire (défaut de libération).
* **Stack vs Heap** : Pile d'exécution vs Tas dynamique.
* **Encapsulation** : Regroupement et protection des attributs.
* **Inheritance** : Héritage de classes.
* **Override** : Redéfinition de méthode virtuelle.
* **Thread / Mutex** : Fil d'exécution / Verrou d'exclusion mutuelle.

#### 🔌 Electronics & Hardware
* **Sampling Rate** : Taux / Fréquence d'échantillonnage ($Fe$).
* **Duty Cycle** : Rapport cyclique ($\alpha$).
* **Resolution / Step size** : Résolution / Quantum ($q$).
* **Differential Bus** : Bus à transmission différentielle (CAN, RS-485).
* **Full-Duplex / Half-Duplex** : Bidirectionnel simultané / alterné.
* **Noise Margin** : Marge de bruit.
            """)

    with tab_en2:
        st.subheader("2. Technical Grammar Focus (Issu de vos cours BTS CIEL)")
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("""
#### 🔄 La Forme Passive en Anglais Technique (Obligatoire dans les Rapports)
Dans les rapports d'incidents et manuels techniques, l'action importe plus que l'auteur :
* **Règle** : Sujet receveur + Auxiliaire `BE` (au temps voulu) + **Participe Passé**.
* *Présent Simple* : *The network is secured by a firewall.*
* *Prétérit Simple* : *The technician installed the firewall yesterday.* $\rightarrow$ **The new firewall was installed by the technician yesterday.**
* *Present Continuous* : *The developers are designing an app.* $\rightarrow$ **An application is being designed by the developers.**
* *Present Perfect* : *The administrator has updated the protocols.* $\rightarrow$ **The security protocols have been updated by the administrator.**
* *Futur Simple* : *The IT team will test the servers.* $\rightarrow$ **The new servers will be tested by the IT team.**
* *Modaux* : *The malware must be quarantined immediately.*
            """)

        with col_g2:
            st.markdown("""
#### ⚡ Les 3 Conditionnels en Contexte Réseau & Cybersécurité
* **Type 0 (Vérité générale / Cause à effet)** : `If + Présent, Présent`
  * *If users forget their password, they need to reset it.*
* **Type 1 (Hypothèse probable / Règle préventive)** : `If + Présent, WILL + Verbe`
  * *If the firewall blocks the attack, the system will remain safe.*
  * *If the router fails, the backup connection will activate.*
* **Type 2 (Hypothèse imaginaire présente)** : `If + Prétérit, WOULD + Verbe`
  * *If the company invested more in cybersecurity, hackers would have more difficulty accessing the network.*
  * *If the network were faster, employees would transfer files more quickly.*
* **Type 3 (Regret passé / Analyse post-incident)** : `If + Past Perfect (HAD + PP), WOULD HAVE + PP`
  * *If the administrator had installed the update earlier, the system would have been more secure.*
  * *If the company had backed up the data regularly, it would not have lost important files.*
            """)

    with tab_en3:
        st.subheader("3. Project 3 : Critical IT Incident in a Company (Étude de Cas d'Examen)")
        st.markdown("""
<div class='ciel-card' style='border-left: 6px solid #ef4444 !important; background: #fef2f2;'>
    <h4 style='color: #991b1b; margin-top:0;'>🚨 Mission Statement (Oral Exam Scenario)</h4>
    <p>You are an IT technical team (BTS CIEL) called urgently by a medium-sized company (around 45 employees). A major IT incident is seriously disrupting the company's activity. Your mission is to analyse the situation, propose technical solutions, and communicate professionally with managers and employees.</p>
</div>
        """, unsafe_allow_html=True)

        st.markdown("""
#### 3 Scénarios d'Entraînement Réels :
1. **Scenario 1: Ransomware & Data Breach**
   * *Symptoms*: Network drives encrypted, demanding a cryptocurrency ransom, active directory locked.
   * *Action Plan*: Immediate isolation of infected machines (unplug Ethernet cables), snapshot preservation for forensic analysis, restore systems from immutable offline backups.
2. **Scenario 2: Major Network Outage**
   * *Symptoms*: Core switch down, router reboot loop, complete interruption of production lines.
   * *Action Plan*: Console cable diagnostic, verify power supply and Spanning-Tree loops, swap with hot-standby spare switch.
3. **Scenario 3: Human Error & Security Misconfiguration**
   * *Symptoms*: Accidental deletion of customer database or sensitive file shared publicly on WAN.
   * *Action Plan*: Revoke public access permissions, restore database from point-in-time recovery log, update ACLs and implement DLP policies.
        """)

    with tab_en4:
        st.subheader("4. Technical Text Analysis & Reading Comprehension")
        st.markdown("""
#### 📄 Text 1 : Cybersecurity Incident Report Overview
*"On October 14th, a distributed denial-of-service (DDoS) attack targeted the public authentication gateway of our cloud infrastructure. The attack originated from an IoT botnet leveraging compromised smart cameras. The perimeter firewall detected over 40 gigabits per second of SYN flood traffic directed towards port 443. In response, our automated mitigation appliance routed the incoming traffic through a cloud scrubbing center, effectively filtering out malicious packets while preserving legitimate HTTPS sessions with minimal latency increase."*
        """)

    with tab_en5:
        st.subheader("5. Oral Presentation Guide for BTS CIEL (E4 & E6)")
        st.markdown("""
<div class='ciel-card'>
    <h4>Useful Sentences for Your Final Defense :</h4>
    <ul>
        <li><b>Introduction</b>: <i>"Good morning, my name is [Name], and today I am going to present the architecture and deployment of the [Project Name] project."</i></li>
        <li><b>Explaining the Problem</b>: <i>"The main technical challenge was to ensure reliable real-time communication between the IoT sensors and the central database while enforcing strict cybersecurity guidelines."</i></li>
        <li><b>Technical Justifications</b>: <i>"We selected the C++ language because of its high execution speed and direct hardware control capabilities."</i></li>
        <li><b>Testing & Results</b>: <i>"As demonstrated in our PVL report, all functional requirements were verified using automated unit tests with Pytest."</i></li>
    </ul>
</div>
        """, unsafe_allow_html=True)




elif page == '📹 Vidéos de Cours':
    st.markdown("<div class='hero-title'>📹 Vidéothèque Pédagogique BTS CIEL</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Retrouvez l'intégralité des leçons vidéo classées par pôles d'ingénierie pour réviser visuellement vos cours et TPs</p>", unsafe_allow_html=True)
    yt_p = 'https://www.youtube.com/watch?v='
    VIDEOS_BY_DOMAIN = {'📶 Réseaux & Télécoms': [{'titre': 'Comprendre le Modèle OSI en 10 minutes', 'id': '33UJvS_z8R8', 'chap': 'Modèle OSI & TCP/IP'}, {'titre': 'Masterclass Subnetting VLSM IPv4', 'id': '42S-A-9PqM0', 'chap': 'Subnetting & Masques IP'}, {'titre': 'IPv6, SLAAC et NDP expliqués simplement', 'id': '72sn_0M4T4g', 'chap': 'IPv6 & Protocoles associées'}, {'titre': 'Comprendre et configurer un VLAN', 'id': '06Y6qYg9_C0', 'chap': 'Commutation & VLANs'}, {'titre': 'Tout savoir sur le Trunking IEEE 802.1Q', 'id': '0j3_T7sN8J4', 'chap': 'Trunking 802.1Q'}, {'titre': 'Configuration Router-on-a-Stick Cisco', 'id': 'LqT5y7aZJ4k', 'chap': 'Routage Inter-VLAN'}, {'titre': 'Spanning Tree Protocol (STP & RSTP 802.1w)', 'id': 'i8D4W6U4z_E', 'chap': 'Commutation Redondante'}, {'titre': 'Comprendre le routage dynamique OSPF', 'id': '3k1-zK7u1G0', 'chap': 'Routage OSPF'}, {'titre': "Maîtriser les filtres d'affichage Wireshark", 'id': 'TkCSr30UojM', 'chap': 'Analyse de trames Wireshark'}], '🔒 Cybersécurité & Gouvernance': [{'titre': "Méthode EBIOS RM de l'ANSSI en 5 Ateliers", 'id': 'J8n0j3x9K2A', 'chap': 'Gouvernance EBIOS RM'}, {'titre': "Réaliser une Analyse d'Impact RGPD (PIA / AIPD)", 'id': '5k9m2-8a9X0', 'chap': 'Conformité RGPD & PIA'}, {'titre': 'Chiffrement Symétrique vs Asymétrique & PKI', 'id': '0iY2m-J4z-0', 'chap': 'Cryptographie & PKI'}, {'titre': 'Architecture DMZ & Configuration Pare-Feu pfSense', 'id': 'L2k3j4X5m-0', 'chap': 'pfSense & Isolation DMZ'}, {'titre': 'Top 10 OWASP : Injections SQL & Requêtes Préparées', 'id': '0k3j4X5m-0', 'chap': 'Sécurité Web OWASP'}, {'titre': 'Tunnels VPN IPsec (L3) vs TLS OpenVPN (L4)', 'id': 'L2k3j4X5m-0', 'chap': 'Sécurisation VPN'}, {'titre': "Wi-Fi 802.1X & Serveur d'Authentification RADIUS", 'id': '8m9k3j4X5m0', 'chap': 'Sécurité Réseau 802.1X'}], '💻 Programmation C++, Python & Git': [{'titre': 'Débutez en C++ - Les bases du langage', 'id': '6m8gS-iXmXQ', 'chap': 'Langage C++'}, {'titre': 'Comprendre la mémoire C++ : Pile vs Tas, Pointeurs', 'id': 'S1yR7_7bWRE', 'chap': 'Gestion Mémoire C++'}, {'titre': 'La POO en C++ : Classes, Encapsulation & Héritage', 'id': '6m8gS-iXmXQ', 'chap': 'POO C++'}, {'titre': 'Multithreading en C++11 : std::thread & std::mutex', 'id': '5m9k3j4X5m0', 'chap': 'Concurrence C++'}, {'titre': 'Programmation Réseau Sockets TCP/UDP en Python', 'id': '6m9k3j4X5m0', 'chap': 'Sockets Python'}, {'titre': 'Tutoriel Git : add, commit, push & branches', 'id': '6m8gS-iXmXQ', 'chap': 'Versioning Git'}], '🖥️ Administration Système Linux & Active Directory': [{'titre': 'Linux Permissions octales chmod, SUID & ACLs', 'id': '2n3j4X5m-0', 'chap': 'Droits Linux POSIX'}, {'titre': 'Gestion des Services systemd & systemctl', 'id': '2n3j4X5m-0', 'chap': 'Systemd Linux'}, {'titre': 'Active Directory de A à Z - Tutoriel Complet', 'id': 'rQ_1n8Y0o-0', 'chap': 'Active Directory ADDS'}, {'titre': 'Gestion des Stratégies de Groupe (GPO LSDOU)', 'id': '8m9k3j4X5m0', 'chap': 'GPO Windows Server'}, {'titre': 'Authentification Kerberos & Rôles FSMO', 'id': '8m9k3j4X5m0', 'chap': 'Kerberos & FSMO'}, {'titre': 'Commandes PowerShell pour Active Directory & Réseau', 'id': '8m9k3j4X5m0', 'chap': 'PowerShell AD'}], '🔌 Électronique, Signaux & Bus Industriels': [{'titre': "Lois fondamentales d'Électricité : Ohm & Kirchhoff", 'id': '7m9k3j4X5m0', 'chap': 'Lois Fondamentales'}, {'titre': 'Le Pont en H BTS7960 & Commande de Moteur CC', 'id': '8m9k3j4X5m0', 'chap': 'Électronique de Puissance'}, {'titre': "La Modulation de Largeur d'Impulsion (PWM/MLI)", 'id': '4jS0qUfE_y4', 'chap': 'Signal PWM MLI'}, {'titre': 'La Boucle de Courant 4-20 mA Industrielle', 'id': '9m9k3j4X5m0', 'chap': 'Capteurs 4-20 mA'}, {'titre': 'Le Bus CAN Industriel & Automobile (ISO 11898)', 'id': '10m9k3j4X5m0', 'chap': 'Bus CAN Différentiel'}, {'titre': 'Le Protocole Modbus RTU sur RS-485', 'id': '11m9k3j4X5m0', 'chap': 'Modbus RTU RS-485'}], '📐 Mathématiques, SysML & Projet E6': [{'titre': 'Suites Arithmétiques & Géométriques (Formules & Sommes)', 'id': '12m9k3j4X5m0', 'chap': 'Suites Mathématiques'}, {'titre': 'Fonctions Exponentielle & Logarithme Népérien', 'id': '13m9k3j4X5m0', 'chap': 'Exp & Ln Math'}, {'titre': 'Diagrammes SysML : BDD, IBD & Requirement Diagram', 'id': '14m9k3j4X5m0', 'chap': 'Modélisation SysML'}, {'titre': 'Diagrammes UML : Classes, Séquence & États-Transitions', 'id': '15m9k3j4X5m0', 'chap': 'Modélisation UML'}, {'titre': 'Qualification E6 : Tests Automatisés avec Pytest', 'id': '16m9k3j4X5m0', 'chap': 'Pytest & PVL E6'}]}
    sel_domain = st.selectbox("📁 Choisissez un domaine d'ingénierie :", list(VIDEOS_BY_DOMAIN.keys()))
    v_list = VIDEOS_BY_DOMAIN[sel_domain]
    st.markdown(f'### 📹 {len(v_list)} Leçons Vidéo - {sel_domain}')
    for v in v_list:
        v_url = yt_p + v['id']
        with st.expander(f'▶️ {v["titre"]} (Chapitre : {v["chap"]})'):
            st.markdown(f'**Chapitre associé :** `{v["chap"]}`')
            st.link_button('▶️ Regarder directement sur YouTube', v_url, type='primary')
            st.video(v_url)
        st.markdown('---')



elif page == '📶 Réseaux & Télécoms':
    st.markdown("<div class='hero-title'>📶 Réseaux & Télécommunications</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Cours magistraux officiels, protocoles fondamentaux et 10 questions certifiantes par chapitre.</p>", unsafe_allow_html=True)
    
    sub_c1, sub_c2 = st.tabs(["📚 Cours & 10 Questions d'Application", "🛠️ Fiches Réflexes E5 Réseau"])
    with sub_c1:
        chap_net = st.selectbox("Sélectionnez le chapitre Réseau à étudier :", [
            "1. Modèle OSI vs TCP/IP & Encapsulation",
            "2. Adressage IPv4, IPv6 & Calcul de Sous-Réseaux (VLSM)",
            "3. VLANs, Trunking IEEE 802.1Q & Routage Inter-VLAN",
            "4. Services d'Infrastructure : DHCP (DORA), DNS & NAT/PAT"
        ], key="sel_net_chap")
        
        cours_data_net = COURS_BASE.get('📶 Réseaux & Télécoms', {})
        for c_titre, c_corps in cours_data_net.items():
            if chap_net.split(' ')[0] in c_titre:
                st.markdown(c_corps)
                
        if chap_net in MINI_QUIZ_COURS:
            st.markdown('---')
            q_list = MINI_QUIZ_COURS[chap_net]
            st.markdown(f"<div class='card-header'><h3 style='color: #38bdf8; margin: 0;'>⚡ Mini-Évaluation Certifiante : 10 Questions Réseau</h3></div>", unsafe_allow_html=True)
            with st.form(key=f"form_net_{chap_net}"):
                ans_map = {}
                for idx_q, qitem in enumerate(q_list):
                    st.markdown(f"<b>Q{idx_q+1} : {qitem['q']}</b>", unsafe_allow_html=True)
                    ans_map[idx_q] = st.radio(f"Choix Q{idx_q+1}:", qitem['options'], key=f"r_net_{chap_net}_{idx_q}", label_visibility='collapsed')
                submit_net = st.form_submit_button("Valider mes 10 réponses", type="primary")
            if submit_net:
                sc = sum(1 for idx_q, qitem in enumerate(q_list) if ans_map.get(idx_q) == qitem['rep'])
                earned = sc * 15
                add_user_points(earned, f"quiz_{chap_net}")
                st.success(f"Score : **{sc} / 10** (+{earned} XP enregistrés sur votre profil) !")
                for idx_q, qitem in enumerate(q_list):
                    if ans_map.get(idx_q) == qitem['rep']:
                        st.write(f"✅ Q{idx_q+1} : {qitem['expl']}")
                    else:
                        st.write(f"❌ Q{idx_q+1} : Votre choix '{ans_map.get(idx_q)}' | Bonne réponse : **{qitem['rep']}** ({qitem['expl']})")
    with sub_c2:
        st.subheader("Fiche Réflexe d'Intervention Cisco IOS")
        st.markdown("""
        ```ios
        ! Configuration d'un Trunk 802.1Q et sécurisation
        Switch(config)# interface GigabitEthernet0/1
        Switch(config-if)# switchport mode trunk
        Switch(config-if)# switchport trunk allowed vlan 10,20,99
        Switch(config-if)# switchport trunk native vlan 99
        Switch(config-if)# no shutdown
        ```
        """)

elif page == '🔒 Cybersécurité & Gouvernance':
    st.markdown("<div class='hero-title'>🔒 Cybersécurité, Gouvernance & Hardening</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Méthode EBIOS RM ANSSI, conformité RGPD/PIA, durcissement et 10 questions par chapitre.</p>", unsafe_allow_html=True)
    
    chap_sec = st.selectbox("Sélectionnez le chapitre Cybersécurité :", [
        "1. Cryptographie : Symétrique, Asymétrique & Hachage",
        "2. Top 10 OWASP & Sécurité Applicative",
        "4. Protocoles Sécurisés (VPN, SSHv2, HTTPS, MQTTS)"
    ], key="sel_sec_chap")
    
    cours_data_sec = COURS_BASE.get('🔒 Cybersécurité', {})
    for c_titre, c_corps in cours_data_sec.items():
        if chap_sec.split(' ')[0] in c_titre:
            st.markdown(c_corps)
            
    if chap_sec in MINI_QUIZ_COURS:
        st.markdown('---')
        q_list = MINI_QUIZ_COURS[chap_sec]
        st.markdown(f"<div class='card-header'><h3 style='color: #38bdf8; margin: 0;'>⚡ Mini-Évaluation Certifiante : 10 Questions Cyber</h3></div>", unsafe_allow_html=True)
        with st.form(key=f"form_sec_{chap_sec}"):
            ans_map = {}
            for idx_q, qitem in enumerate(q_list):
                st.markdown(f"<b>Q{idx_q+1} : {qitem['q']}</b>", unsafe_allow_html=True)
                ans_map[idx_q] = st.radio(f"Choix Q{idx_q+1}:", qitem['options'], key=f"r_sec_{chap_sec}_{idx_q}", label_visibility='collapsed')
            submit_sec = st.form_submit_button("Valider mes 10 réponses", type="primary")
        if submit_sec:
            sc = sum(1 for idx_q, qitem in enumerate(q_list) if ans_map.get(idx_q) == qitem['rep'])
            earned = sc * 15
            add_user_points(earned, f"quiz_{chap_sec}")
            st.success(f"Score : **{sc} / 10** (+{earned} XP) !")

elif page == '💻 Programmation C++ & Python':
    st.markdown("<div class='hero-title'>💻 Programmation C++ & Python Réseau</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Gestion mémoire (Pile vs Tas), POO moderne, pointeurs intelligents et 10 questions certifiantes.</p>", unsafe_allow_html=True)
    
    chap_dev = st.selectbox("Sélectionnez le chapitre Développement :", [
        "1. Langage C++ : Mémoire, Pointeurs & POO",
        "3. Structures de données avancées & Unions en Langage C"
    ], key="sel_dev_chap")
    
    cours_data_dev = COURS_BASE.get('💻 Programmation / Dev', {})
    for c_titre, c_corps in cours_data_dev.items():
        if chap_dev.split(' ')[0] in c_titre:
            st.markdown(c_corps)
            
    if chap_dev in MINI_QUIZ_COURS:
        st.markdown('---')
        q_list = MINI_QUIZ_COURS[chap_dev]
        st.markdown(f"<div class='card-header'><h3 style='color: #38bdf8; margin: 0;'>⚡ Mini-Évaluation Certifiante : 10 Questions Dev</h3></div>", unsafe_allow_html=True)
        with st.form(key=f"form_dev_{chap_dev}"):
            ans_map = {}
            for idx_q, qitem in enumerate(q_list):
                st.markdown(f"<b>Q{idx_q+1} : {qitem['q']}</b>", unsafe_allow_html=True)
                ans_map[idx_q] = st.radio(f"Choix Q{idx_q+1}:", qitem['options'], key=f"r_dev_{chap_dev}_{idx_q}", label_visibility='collapsed')
            submit_dev = st.form_submit_button("Valider mes 10 réponses", type="primary")
        if submit_dev:
            sc = sum(1 for idx_q, qitem in enumerate(q_list) if ans_map.get(idx_q) == qitem['rep'])
            earned = sc * 15
            add_user_points(earned, f"quiz_{chap_dev}")
            st.success(f"Score : **{sc} / 10** (+{earned} XP) !")

elif page == '🖥️ Système Linux & Windows Server':
    st.markdown("<div class='hero-title'>🖥️ Administration Système Linux & Active Directory</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Droits fins (chmod, ACLs), GPO Windows Server, Hyperviseurs et 10 questions par cours.</p>", unsafe_allow_html=True)
    
    chap_sys = st.selectbox("Sélectionnez le chapitre Système :", [
        "2. Services Active Directory & GPO (Windows Server)",
        "3. Virtualisation & Environnements Serveurs (Debian, VMware)"
    ], key="sel_sys_chap")
    
    cours_data_sys = COURS_BASE.get('🖥️ Administration Système', {})
    for c_titre, c_corps in cours_data_sys.items():
        if chap_sys.split(' ')[0] in c_titre:
            st.markdown(c_corps)
            
    if chap_sys in MINI_QUIZ_COURS:
        st.markdown('---')
        q_list = MINI_QUIZ_COURS[chap_sys]
        st.markdown(f"<div class='card-header'><h3 style='color: #38bdf8; margin: 0;'>⚡ Mini-Évaluation Certifiante : 10 Questions Système</h3></div>", unsafe_allow_html=True)
        with st.form(key=f"form_sys_{chap_sys}"):
            ans_map = {}
            for idx_q, qitem in enumerate(q_list):
                st.markdown(f"<b>Q{idx_q+1} : {qitem['q']}</b>", unsafe_allow_html=True)
                ans_map[idx_q] = st.radio(f"Choix Q{idx_q+1}:", qitem['options'], key=f"r_sys_{chap_sys}_{idx_q}", label_visibility='collapsed')
            submit_sys = st.form_submit_button("Valider mes 10 réponses", type="primary")
        if submit_sys:
            sc = sum(1 for idx_q, qitem in enumerate(q_list) if ans_map.get(idx_q) == qitem['rep'])
            earned = sc * 15
            add_user_points(earned, f"quiz_{chap_sys}")
            st.success(f"Score : **{sc} / 10** (+{earned} XP) !")

elif page == '🔌 Électronique & Bus Industriels':
    st.markdown("<div class='hero-title'>🔌 Électronique, Signaux & Bus Industriels</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Lois fondamentales, Shannon, quantum CAN, Modbus RTU, Bus CAN et 10 questions d'application.</p>", unsafe_allow_html=True)
    
    chap_el = st.selectbox("Sélectionnez le chapitre Électronique :", [
        "1. Échantillonnage, CAN/CNA & Théorème de Shannon",
        "4. Lois Fondamentales d'Électricité & Composants Passifs",
        "5. Protocoles Industriels & Bus de terrain (Modbus, Profibus)",
        "6. Transmission optique (Fibres optiques Monomodes & Multimodes)"
    ], key="sel_el_chap")
    
    cours_data_el = COURS_BASE.get('🔌 Électronique & IoT', {})
    for c_titre, c_corps in cours_data_el.items():
        if chap_el.split(' ')[0] in c_titre:
            st.markdown(c_corps)
            
    if chap_el in MINI_QUIZ_COURS:
        st.markdown('---')
        q_list = MINI_QUIZ_COURS[chap_el]
        st.markdown(f"<div class='card-header'><h3 style='color: #38bdf8; margin: 0;'>⚡ Mini-Évaluation Certifiante : 10 Questions Électronique</h3></div>", unsafe_allow_html=True)
        with st.form(key=f"form_el_{chap_el}"):
            ans_map = {}
            for idx_q, qitem in enumerate(q_list):
                st.markdown(f"<b>Q{idx_q+1} : {qitem['q']}</b>", unsafe_allow_html=True)
                ans_map[idx_q] = st.radio(f"Choix Q{idx_q+1}:", qitem['options'], key=f"r_el_{chap_el}_{idx_q}", label_visibility='collapsed')
            submit_el = st.form_submit_button("Valider mes 10 réponses", type="primary")
        if submit_el:
            sc = sum(1 for idx_q, qitem in enumerate(q_list) if ans_map.get(idx_q) == qitem['rep'])
            earned = sc * 15
            add_user_points(earned, f"quiz_{chap_el}")
            st.success(f"Score : **{sc} / 10** (+{earned} XP) !")

elif page == '📐 Mathématiques Appliquées':
    st.markdown("<div class='hero-title'>📐 Mathématiques Appliquées au BTS CIEL</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Suites arithmétiques et géométriques, fonctions exponentielles, logarithmes népériens et calculs d'atténuation en décibels.</p>", unsafe_allow_html=True)
    
    tab_m_main1, tab_m_main2 = st.tabs(["📊 Suites Numériques", "📈 Fonctions Exponentielle & Logarithme"])
    with tab_m_main1:
        st.subheader("Suites Arithmétiques & Géométriques")
        st.markdown(r"""
| Propriété | Suite Arithmétique | Suite Géométrique |
| :--- | :--- | :--- |
| **Mécanisme** | On **ajoute** une raison constante $r$ | On **multiplie** par une raison constante $q$ |
| **Récurrence** | $u_{n+1} = u_n + r$ | $u_{n+1} = u_n \times q$ |
| **Formule explicite ($u_0$)** | $u_n = u_0 + n \cdot r$ | $u_n = u_0 \times q^n$ |
| **Somme des termes** | $S = N \times \frac{u_{\text{premier}} + u_{\text{dernier}}}{2}$ | $S = u_{\text{premier}} \times \frac{1 - q^N}{1 - q}$ ($q \neq 1$) |
        """)
    with tab_m_main2:
        st.subheader("Exponentielle, Logarithme & Décibels")
        st.markdown(r"""
* **Atténuation de puissance** : $A_{dB} = 10 \log_{10}\left(\frac{P_1}{P_2}\right)$
* **Gain en tension** : $G_{dB} = 20 \log_{10}\left(\frac{V_2}{V_1}\right)$
* **Circuit RC** : Charge $u_C(t) = E(1 - e^{-t/\tau})$ avec $\tau = R \cdot C$.
        """)

elif page == '🇬🇧 Anglais Technique & Datasheets':
    st.markdown("<div class='hero-title'>🇬🇧 Anglais Technique & Datasheets Constructeurs</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Fiches constructeurs en anglais (ATmega328P, ESP32, STM32, MCP2515, MAX485), glossaire bilingue et grammaire technique.</p>", unsafe_allow_html=True)
    
    tab_ang1, tab_ang2 = st.tabs(["📄 Fiches Techniques (Datasheets)", "📖 Glossaire & Grammaire"])
    with tab_ang1:
        st.subheader("Spécifications Techniques de Composants Phares")
        st.markdown("""
* **ATmega328P** : Microcontrôleur 8 bits AVR, 32 Ko Flash, 2 Ko SRAM, Timers PWM 8 et 16 bits.
* **MCP2515** : Contrôleur Standalone CAN 2.0B interfacé en bus SPI haute vitesse jusqu'à 10 MHz.
* **MAX485** : Émetteur-récepteur différentiel semi-duplex RS-485 à faible consommation d'énergie.
        """)
    with tab_ang2:
        st.subheader("Vocabulaire Technique Incontournable")
        st.markdown("""
* **Throughput** : Débit utile effectif.
* **Frame** : Trame de niveau 2.
* **Sampling Rate** : Fréquence d'échantillonnage.
* **Pull-up Resistor** : Résistance de rappel au niveau haut.
        """)

elif page == '🌐 Répertoire des Liens':
    st.markdown("<div class='hero-title'>🌐 Répertoire des Ressources Essentielles</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Les sites de référence incontournables pour réussir votre BTS CIEL</p>", unsafe_allow_html=True)
    LIENS = {'Cours Magistraux & Fiches': [('Le site de Thierry Vaira', 'http://tvaira.free.fr/', 'La bible de référence du BTS informatique et réseaux.'), ('Cours BTS CIEL', 'https://coursbtsciel.fr/', 'Fiches synthétiques de cours et résumés.'), ('IT-Connect', 'https://www.it-connect.fr/', 'Tutoriels professionnels SysAdmin, Linux et Réseaux.')], 'MOOCs & Formations': [('Cisco Networking Academy', 'https://www.netacad.com/', 'Cours officiels de préparation aux certifications Cisco.'), ('OpenClassrooms - Réseaux TCP/IP', 'https://openclassrooms.com/fr/courses/857447-apprenez-le-fonctionnement-des-reseaux-tcp-ip', 'Fondations des réseaux.'), ('OpenClassrooms - Programmation C++', 'https://openclassrooms.com/fr/courses/1894236-programmez-avec-le-langage-c', 'Maîtrise de la POO en C++.')], 'Entraînement Pratique & Cyber': [('Root-Me', 'https://www.root-me.org/', "Plateforme d'entraînement au hacking éthique."), ('TryHackMe', 'https://tryhackme.com/', 'Salles guidées de cybersécurité.'), ('France-IOI', 'http://france-ioi.org/', 'Entraînement algorithmique.')]}
    for cat, items in LIENS.items():
        st.markdown(f'### 📂 {cat}')
        for nom, url, desc in items:
            col_l1, col_l2 = st.columns([1, 3])
            with col_l1:
                st.markdown(f'**[{nom}]({url})**')
            with col_l2:
                st.write(desc)
        st.markdown('---')




elif page == '🎯 Remédiation & Lacunes Ciblées (BTS Blanc)':
    st.markdown("<div class='hero-title'>🎯 Plan de Remédiation Ciblée & Consolidation des Lacunes</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Programme personnalisé de renforcement technique basé sur votre évaluation d'entrée pour le BTS Blanc</p>", unsafe_allow_html=True)

    st.markdown("""
    <div class='ciel-card' style='border-left: 6px solid #ef4444 !important; background: #fef2f2;'>
        <h3 style='color: #991b1b; margin-top: 0;'>📋 Bilan de Session d'Évaluation & Diagnostic Technique</h3>
        <p style='color: #7f1d1d;'>Votre évaluation met en évidence un <b>socle solide déjà validé</b> sur plusieurs piliers fondamentaux, mais révèle <b>6 lacunes conceptuelles prioritaires</b> à verrouiller impérativement avant le BTS Blanc des 9-11 décembre.</p>
        <div style='display: flex; gap: 15px; flex-wrap: wrap; margin-top: 10px;'>
            <span class='badge badge-emerald'>✅ 5 Notions Clés Validées</span>
            <span class='badge badge-rose'>🚨 6 Lacunes Prioritaires à Consolider</span>
            <span class='badge badge-blue'>🎯 Objectif : 100% de Maîtrise E4/E5</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    yt_p = 'https://www.youtube.com/watch?v='

    tab_diag, tab_tcp, tab_dhcp, tab_nat, tab_ssh, tab_virt, tab_poo, tab_eval = st.tabs([
        '📊 Roadmap Réajustée',
        '📶 1. TCP vs UDP',
        '⚙️ 2. Protocole DHCP',
        '🌐 3. Principe du NAT/PAT',
        '🔐 4. Chiffrement SSH',
        '🖥️ 5. Hyperviseurs Type 1/2',
        '💻 6. Encapsulation POO',
        '✍️ Mini-Test Validation'
    ])

    with tab_diag:
        st.subheader('📊 Réajustement Stratégique de la Roadmap BTS Blanc')
        col_ok, col_ko = st.columns(2)
        with col_ok:
            st.markdown("""
            <div class='ciel-card' style='border-top: 4px solid #10b981 !important;'>
                <h4 style='color: #065f46; margin-top: 0;'>✅ Concepts Validés (À réviser ponctuellement)</h4>
                <ul style='color: #1e293b; line-height: 1.8;'>
                    <li><b>🛡️ Permissions Linux (chmod)</b> : Calcul des masques octaux (750, 644, 755), symbolique (u/g/o/a) et commande <code>chmod</code> acquis.</li>
                    <li><b>🛡️ Identification des Attaques DDoS</b> : Compréhension du déni de service distribué, saturation volumétrique et détection.</li>
                    <li><b>🛡️ Filtrage Pare-Feu de Base</b> : Rôle de coupure réseau, distinction LAN/DMZ/WAN et politique d'interdiction par défaut.</li>
                    <li><b>📶 Fondamentaux du Réseau</b> : Modèle en couches, notion d'adresse IP et distinction entre domaines de diffusion.</li>
                    <li><b>💻 Distinction Classe vs Instance</b> : Compréhension de la classe comme moule/modèle et de l'instance comme objet physique en mémoire.</li>
                </ul>
                <div style='background: #ecfdf5; padding: 10px; border-radius: 8px; border: 1px solid #a7f3d0; margin-top: 10px;'>
                    <span style='color: #047857; font-weight: 600;'>📌 Statut Planning</span> : Allégement du temps d'étude sur ces modules. Maintien d'un entraînement réflexe via les flashcards (10 min/semaine).
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_ko:
            st.markdown("""
            <div class='ciel-card' style='border-top: 4px solid #ef4444 !important;'>
                <h4 style='color: #991b1b; margin-top: 0;'>🚨 Axes Prioritaires de Remédiation (Lacunes Ciblées)</h4>
                <ul style='color: #1e293b; line-height: 1.8;'>
                    <li><b>🔴 Rôle des Protocoles Couche 4 (TCP vs UDP)</b> : Confusion sur la connexion, les accusés ACK, le Three-Way Handshake et les en-têtes.</li>
                    <li><b>🔴 Fonctionnement & Utilité du DHCP</b> : Maîtrise incomplète de la séquence DORA, des baux, des options (003, 006, 015) et d'APIPA.</li>
                    <li><b>🔴 Mécanisme du NAT / PAT</b> : Distinction floue entre NAT Statique, Dynamique et surcharge de port (PAT / Overload).</li>
                    <li><b>🔴 Chiffrement SSH & Hardening</b> : Mécanisme hybride (clés asymétriques + tunnel symétrique) et configuration <code>sshd_config</code>.</li>
                    <li><b>🔴 Virtualisation (Hyperviseurs Type 1 vs Type 2)</b> : Confusion entre exécution Bare-Metal et hyperviseur hébergé sur un OS.</li>
                    <li><b>🔴 Encapsulation en POO (C++)</b> : Principe de masquage des données via <code>private</code>/<code>public</code> et rôle des accesseurs getters/setters.</li>
                </ul>
                <div style='background: #fef2f2; padding: 10px; border-radius: 8px; border: 1px solid #fecaca; margin-top: 10px;'>
                    <span style='color: #b91c1c; font-weight: 600;'>🎯 Objectif Remédiation</span> : Révision active des 6 fiches ci-jointes + vidéos ciblées + validation sur le mini-quiz.
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('---')
        st.subheader('📅 Calendrier Hebdomadaire Réajusté')
        st.markdown("""
| Période | Thématique de Révision | Statut Personnalisé | Actions Concrètes Programmées |
| :--- | :--- | :--- | :--- |
| **Semaine 1** | Réseaux : Modèle OSI, Commutation & Protocoles | 🚨 **Priorité Maximale** | Consolider **TCP vs UDP** et le processus **DHCP DORA** + Lab Wireshark. |
| **Semaine 2** | Cybersécurité, Pare-Feu & Administration | 🚨 **Priorité Maximale** | Maîtriser le **NAT/PAT**, le chiffrement **SSH** et la configuration <code>sshd_config</code>. |
| **Semaine 3** | Développement C++, Sockets & Virtualisation | 🚨 **Priorité Maximale** | Intégrer l'**Encapsulation POO** (getters/setters) et les **Hyperviseurs Type 1/2**. |
| **Semaine 4** | Électronique, Bus de Terrain & Mathématiques | ⚡ **Standard** | Réviser les bus industriels (CAN, Modbus RTU), suites et calculs de décibels. |
| **Semaine 5** | Modélisation SysML/UML & Épreuve E6 | ⚡ **Standard** | Diagrammes de classes, diagrammes de séquence et rédaction de PVL Pytest. |
| **Semaine 6** | Annales Officielles (2024-2025) & Marathons | 🏆 **Entraînement Examen** | Épreuves blanches en temps réel et correction des points de détail. |
        """)

    with tab_tcp:
        st.subheader('📶 Mini-Fiche 1 : TCP vs UDP (Couche Transport L4)')
        st.markdown("""
*Sources officielles : "2 -Le modèle OSI TCP.pdf", "3 - Les équipements d'interconnexion réseaux.pdf"*

#### 🔹 1. Rôle Fondamental de la Couche 4 (Transport)
La couche Transport du modèle OSI / TCP-IP assure la communication de processus à processus entre deux hôtes grâce aux **numéros de ports** (sur 16 bits, de 0 à 65535). L'unité de données (PDU) est le **Segment** en TCP et le **Datagramme** en UDP.

#### 🔹 2. Tableau Comparatif Examen : TCP vs UDP
| Critère Technique | TCP (*Transmission Control Protocol*) | UDP (*User Datagram Protocol*) |
| :--- | :--- | :--- |
| **Mode de transmission** | **Orienté connexion** (session préalable obligatoire) | **Sans connexion** (envoi direct sans négociation) |
| **Fiabilité** | **Fiable à 100%** (garantie d'acheminement des données) | **Non fiable** (aucune garantie d'arrivée, *Best Effort*) |
| **Contrôle d'intégrité** | Checksum obligatoire + Acquittements (ACK) | Checksum optionnel/basique, aucun accusé de réception |
| **Contrôle de séquence** | **Oui** : Numérotation des octets (Sequence Number 32 bits) | **Non** : Les paquets peuvent arriver désordonnés |
| **Gestion des pertes** | **Retransmission automatique** des segments perdus | Aucune retransmission (gérée si besoin par l'application) |
| **Contrôle de flux** | **Oui** : Fenêtre glissante (*Window Size* 16 bits) anti-saturation | **Non** : Émission au débit maximal |
| **Taille de l'en-tête** | Lourd : **20 à 60 octets** (selon options) | Léger : **8 octets fixes** seulement |
| **Vitesse / Latence** | Plus lent (surcharge de contrôle) | **Ultra-rapide** et latence minimale |
| **Protocoles typiques** | HTTP (80), HTTPS (443), SSH (22), FTP (20/21), SMTP (25) | DNS (53), DHCP (67/68), VoIP, Streaming vidéo, TFTP (69) |

#### 🔹 3. L'Établissement de Connexion TCP : Le *Three-Way Handshake*
Avant d'échanger le moindre octet de données, TCP négocie la liaison en 3 étapes :
1. **SYN (Synchronize)** : Le client envoie un segment avec le flag `SYN = 1` et un numéro de séquence initial aléatoire (ex: `Seq = 100`).
2. **SYN-ACK** : Le serveur répond avec `SYN = 1`, son propre numéro de séquence (ex: `Seq = 300`) et acquitte la demande du client : `ACK = 101` (`Seq_client + 1`).
3. **ACK** : Le client valide avec `ACK = 301` (`Seq_serveur + 1`). La connexion est établie (*ESTABLISHED*).

#### 🔹 4. La Fermeture de Connexion Propre
La fermeture s'opère par échange de flags **FIN** (Finish) et **ACK** dans les deux sens :
Client `FIN` -> Serveur `ACK` -> Serveur `FIN` -> Client `ACK`.
        """)

        st.markdown('#### 📹 Vidéos Recommandées pour Consolider TCP/UDP :')
        c_v1, c_v2 = st.columns(2)
        with c_v1:
            st.markdown('**Comprendre TCP vs UDP en 5 minutes**')
            st.video(f"{yt_p}06Y6qYg9_C0")
        with c_v2:
            st.markdown('**Analyse du Three-Way Handshake TCP sous Wireshark**')
            st.video(f"{yt_p}33UJvS_z8R8")

    with tab_dhcp:
        st.subheader('⚙️ Mini-Fiche 2 : Fonctionnement & Utilité du DHCP')
        st.markdown("""
*Sources officielles : "CIEL1-U6-03-DNS-DHCP.pdf", "TP07-ADDS-DNS-DHCP.pdf"*

#### 🔹 1. Utilité du DHCP (*Dynamic Host Configuration Protocol*)
DHCP est un protocole de la couche Application (utilisant **UDP 67 côté serveur** et **UDP 68 côté client**). Ses rôles fondamentaux :
* **Automatiser l'attribution des adresses IP** sans intervention manuelle sur chaque poste.
* **Distribuer l'ensemble des paramètres réseau nécessaires** : masque, passerelle par défaut, serveurs DNS, nom de domaine.
* **Éviter les conflits d'adresses IP** (deux machines avec la même IP) et optimiser la réutilisation des adresses dans un parc.

#### 🔹 2. Le Mécanisme d'Attribution en 4 Étapes : La Séquence DORA
Au démarrage, un client n'a pas d'adresse IP (`0.0.0.0`). Il déclenche le cycle DORA :
```text
Client (0.0.0.0:68)                                   Serveur DHCP (:67)
   |                                                        |
   |----- 1. DHCP DISCOVER (Broadcast: 255.255.255.255) --->| 'Qui peut me donner une IP ?'
   |                                                        |
   |<---- 2. DHCP OFFER (Unicast ou Broadcast) -------------| 'Je te propose 192.168.1.50'
   |                                                        |
   |----- 3. DHCP REQUEST (Broadcast: 255.255.255.255) ---->| 'J'accepte formellement cette IP'
   |                                                        |
   |<---- 4. DHCP ACKNOWLEDGE (Validation du bail) ---------| 'C'est validé pour 8 jours !'
```
*Pourquoi la REQUEST est-elle en broadcast ?* Pour informer les autres serveurs DHCP éventuels du réseau que leur offre n'a pas été retenue, libérant ainsi leurs adresses proposées.

#### 🔹 3. Le Bail DHCP (*Lease Time*) & Renouvellement
* L'adresse n'est pas donnée à vie : elle est **louée pour une durée définie** (ex: 8 jours par défaut sous Windows Server).
* **À 50% du bail (T1)** : Le client tente de renouveler son bail auprès du serveur en **Unicast** (`DHCPREQUEST`).
* **À 87.5% du bail (T2)** : Si le serveur d'origine ne répond pas, le client émet une demande en **Broadcast** pour trouver un autre serveur.
* **À 100%** : Sans réponse, l'adresse est abandonnée et l'interface bascule en secours.

#### 🔹 4. Les Options DHCP Indispensables d'Examen BTS
Dans la console DHCP, l'administrateur configure des options d'étendue :
* **Option 003 (Routeur / Default Gateway)** : Adresse IP de la passerelle par défaut permettant l'accès inter-réseaux et Internet.
* **Option 006 (Serveurs DNS)** : Adresses IP des serveurs de résolution de noms (ex: l'IP du contrôleur de domaine AD).
* **Option 015 (Nom de domaine DNS)** : Suffixe de domaine (ex: `ciel.local`).

#### 🔹 5. Réservation DHCP vs Adressage APIPA
* **Réservation DHCP** : Association fixe d'une adresse IP à l'**adresse MAC** de la carte réseau. Permet d'avoir une IP permanente (serveurs, imprimantes) tout en conservant une gestion centralisée des options.
* **APIPA (Automatic Private IP Addressing)** : Si aucun serveur DHCP ne répond après 4 tentatives `DISCOVER`, l'OS (Windows) s'auto-attribue une adresse dans la plage **`169.254.0.1` à `169.254.255.254`** avec le masque `255.255.0.0` (`/16`). **Cette adresse n'a pas de passerelle et ne permet aucun accès Internet** (communication limitée au segment local).
        """)

        st.markdown('#### 📹 Vidéos Recommandées pour Consolider DHCP :')
        c_v3, c_v4 = st.columns(2)
        with c_v3:
            st.markdown('**Comprendre le protocole DHCP & DORA en 5 minutes**')
            st.video(f"{yt_p}33UJvS_z8R8")
        with c_v4:
            st.markdown('**Installer et Configurer un serveur DHCP sous Windows Server**')
            st.video(f"{yt_p}rQ_1n8Y0o-0")

    with tab_nat:
        st.subheader('🌐 Mini-Fiche 3 : Le Principe du NAT & PAT en Réseau')
        st.markdown("""
*Sources officielles : "NAT PAT REDIRECTION DE PORTS.pdf", "3 - Les équipements d'interconnexion réseaux.pdf"*

#### 🔹 1. Pourquoi le NAT (*Network Address Translation*) ?
* **Pénurie d'adresses IPv4** : L'espace d'adressage IPv4 public (environ 4,3 milliards d'adresses) est saturé.
* **Adresses Privées (RFC 1918)** : Non routables sur Internet (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
* **Rôle du NAT** : Opéré par un routeur ou une passerelle (Couche 3), le NAT **traduit les adresses IP privées du LAN en une adresse IP publique** routable sur Internet lors de la traversée de la frontière réseau.

#### 🔹 2. Les 3 Types de NAT Indispensables au BTS CIEL
```text
  [ PC1 : 192.168.1.10:1025 ] ---\
  [ PC2 : 192.168.1.11:1025 ] ----- [ ROUTEUR / BOX NAT ] === (IP Publique : 203.0.113.1) ===> [ INTERNET ]
```
1. **NAT Statique (1 pour 1)** :
   * Associe une adresse IP privée unique à une adresse IP publique unique de façon permanente.
   * *Usage* : Rendre un serveur interne (Web, Mail) accessible depuis Internet avec sa propre IP publique dédiée.
   * *Inconvénient* : Consomme autant d'adresses publiques que d'adresses privées. Ne résout pas la pénurie IPv4.
2. **NAT Dynamique (avec Pool d'adresses)** :
   * Le routeur dispose d'un pool d'adresses publiques (ex: 203.0.113.10 à .20). Les machines du LAN reçoivent une IP publique temporaire lors de leur sortie.
3. **PAT (Port Address Translation) ou NAT Overload (Surcharge)** :
   * **C'est le mécanisme universel utilisé en box domicile et entreprises** : Des centaines d'équipements privés partagent **une seule et même adresse IP publique**.
   * *Comment le routeur fait-il la différence au retour ?* Grâce aux **numéros de ports source éphémères** (au-dessus de 1024) !

#### 🔹 3. Exemple de Table de Traduction PAT (NAT Overload)
| Machine LAN (Inside Local) | Port Local | IP Publique Traduite (Inside Global) | Port Public Alloué | Serveur Web Externe (Outside) |
| :--- | :--- | :--- | :--- | :--- |
| `192.168.1.10` | `1025` | `203.0.113.1` | **`30001`** | `142.250.179.67:80` |
| `192.168.1.11` | `1025` | `203.0.113.1` | **`30002`** | `142.250.179.67:80` |

Lorsque le paquet revient du serveur Google (`142.250.179.67`), le routeur consulte le port de destination :
* S'il reçoit une réponse sur le port `30001`, il sait qu'elle est destinée au PC1 (`192.168.1.10:1025`).
* S'il reçoit une réponse sur le port `30002`, il la réaiguille vers le PC2 (`192.168.1.11:1025`).

#### 🔹 4. La Redirection de Port (DNAT / Port Forwarding)
Pour autoriser un client externe sur Internet à joindre un service local (ex: caméra IP, NAS ou serveur web interne), le routeur applique une règle de **Destination NAT** :
* Tout trafic arrivant sur l'interface WAN sur le port externe `8080` est réécrit et redirigé vers l'IP locale `192.168.1.200` sur le port `80`.
        """)

        st.markdown('#### 📹 Vidéos Recommandées pour Consolider le NAT/PAT :')
        c_v5, c_v6 = st.columns(2)
        with c_v5:
            st.markdown('**Comprendre le NAT, PAT et Port Forwarding de A à Z**')
            st.video(f"{yt_p}06Y6qYg9_C0")
        with c_v6:
            st.markdown('**Configuration du NAT Statique et du PAT sur Routeur Cisco**')
            st.video(f"{yt_p}42S-A-9PqM0")

    with tab_ssh:
        st.subheader('🔐 Mini-Fiche 4 : Chiffrement SSH & Configuration sshd_config')
        st.markdown("""
*Sources officielles : "Getting started with the scientific cluster", "TP6.2-bash_debian_server.pdf", "Guides Hardening ANSSI"*

#### 🔹 1. Rôle et Architecture du Protocole SSH (Port TCP 22)
SSH (*Secure Shell*) remplace l'ancien protocole Telnet (qui transmettait mots de passe et commandes en clair). Il crée un tunnel sécurisé garantissant :
* **Confidentialité** : Chiffrement complet du trafic contre l'interception.
* **Authentification** : Preuve d'identité du serveur et du client.
* **Intégrité** : Détection de toute altération de paquet via HMAC.

#### 🔹 2. Le Mécanisme de Chiffrement Hybride de SSH
SSH combine les deux familles de cryptographie pour optimiser sécurité et rapidité :
1. **Phase 1 : Négociation Asymétrique (Clé Publique / Clé Privée)** :
   * Le serveur présente sa clé d'hôte publique (fingerprint RSA ou Ed25519) enregistrée sur le client dans `~/.ssh/known_hosts`.
   * Un protocole d'échange de clés (**Diffie-Hellman / ECDH**) permet au client et au serveur de calculer une **clé secrète de session commune** sans jamais la transmettre sur le réseau !
2. **Phase 2 : Chiffrement Symétrique de Session** :
   * Une fois la clé de session établie, toutes les données (commandes, frappes de touches, fichiers SFTP/SCP) sont chiffrées avec un algorithme symétrique ultra-rapide (**AES-256-GCM** ou **ChaCha20-Poly1305**).
3. **Phase 3 : Authentification de l'Utilisateur** :
   * Par mot de passe ou, de manière bien plus sûre, par **paire de clés SSH** : la clé publique du client est déposée sur le serveur dans `~/.ssh/authorized_keys`, tandis que la clé privée reste secrète sur le poste client (protégée par une *passphrase*).

#### 🔹 3. Fichier de Configuration Serveur : `/etc/ssh/sshd_config`
Pour sécuriser un serveur Linux Debian selon les recommandations de l'ANSSI, éditez `/etc/ssh/sshd_config` :
```bash
# 1. Changer le port par défaut pour neutraliser les scans automatisés
Port 2222

# 2. Interdire la connexion directe de l'administrateur root
PermitRootLogin no

# 3. Forcer l'authentification par clé publique et interdire les mots de passe faibles
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no

# 4. Restreindre les tentatives d'authentification
MaxAuthTries 3

# 5. Restreindre les utilisateurs autorisés à se connecter
AllowUsers admin enzo

# 6. Désactiver le déport graphique X11 non nécessaire
X11Forwarding no
```
Après modification, validez et redémarrez le démon :
```bash
sudo sshd -t                      # Vérifie la syntaxe sans couper SSH
sudo systemctl restart sshd       # Applique les paramètres
```
        """)

        st.markdown('#### 📹 Vidéos Recommandées pour Consolider SSH :')
        c_v7, c_v8 = st.columns(2)
        with c_v7:
            st.markdown('**Comprendre le chiffrement SSH et l\'authentification par clés**')
            st.video(f"{yt_p}2n3j4X5m-0")
        with c_v8:
            st.markdown('**Sécuriser et durcir un serveur SSH Linux (sshd_config)**')
            st.video(f"{yt_p}k8vW6qR3xYQ")

    with tab_virt:
        st.subheader('🖥️ Mini-Fiche 5 : Hyperviseurs Type 1 (Bare-Metal) vs Type 2 (Hosted)')
        st.markdown("""
*Sources officielles : "CIEL1-U6-02-Virtualisation.pdf", "CIEL1-U6-01-SystemeExploitation.pdf"*

#### 🔹 1. Définition de l'Hyperviseur (VMM)
L'hyperviseur (*Virtual Machine Monitor*) est la couche logicielle ou matérielle qui alloue dynamiquement les ressources physiques (CPU, RAM, Disque, Réseau) et permet l'exécution simultanée et cloisonnée de plusieurs **Machines Virtuelles (VM)**, chacune possédant son propre Système d'Exploitation Invité (*Guest OS*).

#### 🔹 2. Tableau Comparatif Examen : Type 1 vs Type 2
| Caractéristique | Hyperviseur Type 1 (*Bare-Metal* / Natif) | Hyperviseur Type 2 (*Hosted* / Hébergé) |
| :--- | :--- | :--- |
| **Implantation matérielle** | S'exécute **directement sur le matériel physique** du serveur (aucun OS hôte) | S'exécute **comme une application logicielle** au-dessus d'un OS hôte (Windows/Linux/macOS) |
| **Couches logicielles** | Matériel -> **Hyperviseur** -> VMs | Matériel -> **OS Hôte** -> **Hyperviseur** -> VMs |
| **Performances & Latence** | **Performances quasi-natives**, latence minimale | Légère perte de performance (surcharge de l'OS hôte) |
| **Gestion des ressources** | Contrôle direct et prioritaire des instructions CPU/RAM | Soumis au bon vouloir de l'ordonnanceur de l'OS hôte |
| **Disponibilité / Enterprise** | Haute disponibilité (HA), migration à chaud (*vMotion*), clustering | Fonctions limitées au poste de travail local |
| **Usage cible** | **Data Centers**, serveurs de production en entreprise | **Postes de développement**, tests, formation, maquettage |
| **Solutions leaders** | **VMware ESXi**, **Proxmox VE**, **Microsoft Hyper-V Server**, **KVM**, **Xen** | **VMware Workstation Pro**, **Oracle VirtualBox**, **Parallels Desktop** |

#### 🔹 3. Schéma Architectural Comparatif
```text
--- HYPERVISEUR TYPE 1 (Natif) ---          --- HYPERVISEUR TYPE 2 (Hébergé) ---
+-------------------------------+           +-------------------------------+
|   VM 1 (Linux) | VM 2 (Win)   |           |   VM 1 (Linux) | VM 2 (Win)   |
+-------------------------------+           +-------------------------------+
|  HYPERVISEUR (ESXi / Proxmox) |           |  HYPERVISEUR (Workstation/VBox)|
+-------------------------------+           +-------------------------------+
|       MATÉRIEL PHYSIQUE       |           |   OS HÔTE (Windows 11 / Linux)|
|     (Serveur Dédié)           |           +-------------------------------+
+-------------------------------+           |       MATÉRIEL PHYSIQUE       |
```

#### 🔹 4. Distinction avec la Conteneurisation (Docker / LXC)
* Une **VM** embarque un noyau complet et un OS invité entier (lourd, plusieurs Go, démarrage en 30-60s).
* Un **Conteneur** partage le noyau de l'OS hôte via les *namespaces* et *cgroups* de Linux (léger, quelques dizaines de Mo, démarrage instantané en millisecondes).
        """)

        st.markdown('#### 📹 Vidéos Recommandées pour Consolider la Virtualisation :')
        c_v9, c_v10 = st.columns(2)
        with c_v9:
            st.markdown('**Comprendre la Virtualisation : Hyperviseurs Type 1 vs Type 2**')
            st.video(f"{yt_p}3Z8oE-pCq00")
        with c_v10:
            st.markdown('**Machines Virtuelles vs Conteneurs Docker expliqués simplement**')
            st.video(f"{yt_p}rQ_1n8Y0o-0")

    with tab_poo:
        st.subheader('💻 Mini-Fiche 6 : L\'Encapsulation en Programmation Orientée Objet (C++)')
        st.markdown("""
*Sources officielles : "Fiche de révision C++.pdf", "FICHE SAVOIR N°12 Commande de led en C++.docx"*

#### 🔹 1. Définition Fondamentale de l'Encapsulation
L'encapsulation est le principe pilier de la POO consistant à **regrouper au sein d'une même entité (la classe) les données (attributs) et les traitements qui leur sont appliqués (méthodes)**, tout en **dissimulant l'état interne de l'objet** aux programmes extérieurs.

#### 🔹 2. Pourquoi l'Encapsulation est-elle Cruciale en BTS CIEL ?
* **Protection contre les corruptions de données** : Empêche un code tiers de modifier directement une variable sensible sans contrôle (ex: assigner une vitesse négative ou une température aberrante).
* **Découplage & Maintenabilité** : On peut modifier l'implémentation interne (changer le nom d'une variable ou son type) sans casser le reste du projet, tant que l'interface publique reste identique.

#### 🔹 3. Les Trois Mots-Clés de Visibilité
* `private` : Les membres ne sont accessibles **que par les méthodes de la classe elle-même**. C'est le niveau par défaut pour tous les attributs (variables membres).
* `protected` : Les membres sont accessibles par la classe et ses **classes dérivées** (héritage).
* `public` : Les membres sont accessibles depuis l'extérieur par n'importe quelle partie du programme (l'interface externe).

#### 🔹 4. Le Rôle des Accesseurs (*Getters*) et Mutateurs (*Setters*)
* **Getter (Accesseur)** : Méthode publique renvoyant la valeur d'un attribut privé en lecture seule. Elle est qualifiée `const` car elle ne modifie pas l'objet.
* **Setter (Mutateur)** : Méthode publique permettant de modifier un attribut privé **en validant préalablement la cohérence de la nouvelle valeur**.

#### 🔹 5. Exemple Concret C++ (Code Validé BTS CIEL)
```cpp
#include <iostream>
#include <string>

class CapteurTemperature {
private:
    // Attributs encapsulés : inaccessibles directement depuis l'extérieur
    std::string reference;
    float temperature;

public:
    // Constructeur : initialise l'état initial
    CapteurTemperature(std::string ref) : reference(ref), temperature(20.0f) {}

    // GETTER : Consultation sécurisée (const = ne modifie pas l'objet)
    float getTemperature() const {
        return temperature;
    }

    std::string getReference() const {
        return reference;
    }

    // SETTER : Modification contrôlée avec validation de cohérence physique
    void setTemperature(float nouvelleTemp) {
        // Règle métier : la température physique ne peut pas être inférieure au zéro absolu
        if (nouvelleTemp >= -273.15f && nouvelleTemp <= 150.0f) {
            temperature = nouvelleTemp;
        } else {
            std::cout << "[ERREUR] Valeur physique impossible rejetée !" << std::endl;
        }
    }
};

int main() {
    CapteurTemperature capteur("BME280-SALLE1");

    // capteur.temperature = 50.0f; // <-- ERREUR DE COMPILATION : attribut 'private' !

    capteur.setTemperature(24.5f);  // Modification validée par le Setter
    std::cout << "Capteur " << capteur.getReference() << " : " << capteur.getTemperature() << " C" << std::endl;

    capteur.setTemperature(-500.0f); // Rejeté par le Setter !
    return 0;
}
```
        """)

        st.markdown('#### 📹 Vidéos Recommandées pour Consolider l\'Encapsulation :')
        c_v11, c_v12 = st.columns(2)
        with c_v11:
            st.markdown('**Programmation Orientée Objet : Classes & Encapsulation en C++**')
            st.video(f"{yt_p}6m8gS-iXmXQ")
        with c_v12:
            st.markdown('**Comprendre les Getters et Setters en C++**')
            st.video(f"{yt_p}S1yR7_7bWRE")

    with tab_eval:
        st.subheader('✍️ Mini-Test Interactif de Consolidation des 6 Lacunes')
        st.markdown('Répondez à ces 6 questions ciblées pour vérifier que chacune de vos lacunes est désormais comblée :')

        rem_q = [
            {
                'q': "1. Quel protocole de transport utilise un en-tête léger de 8 octets sans garantie d'acheminement ?",
                'opts': ['TCP', 'UDP', 'IP', 'ICMP'],
                'rep': 'UDP',
                'expl': "UDP utilise un en-tête de 8 octets sans connexion ni acquittement, idéal pour le temps réel."
            },
            {
                'q': "2. Dans le processus DHCP DORA, quelle étape informe formellement le serveur de l'acceptation de l'offre ?",
                'opts': ['Discover', 'Offer', 'Request', 'Acknowledge'],
                'rep': 'Request',
                'expl': "Le client envoie un DHCPREQUEST en broadcast pour notifier son choix et libérer les autres offres."
            },
            {
                'q': "3. Quel mécanisme NAT permet à 200 postes du LAN d'accéder à Internet avec UNE SEULE adresse IP publique ?",
                'opts': ['NAT Statique 1:1', 'PAT (Port Address Translation / Overload)', 'NAT Dynamique sans surcharge', 'Routage RIP'],
                'rep': 'PAT (Port Address Translation / Overload)',
                'expl': "Le PAT multiplexe les connexions sortantes en attribuant un port source éphémère distinct par session."
            },
            {
                'q': "4. Quelle directive dans /etc/ssh/sshd_config interdit formellement la connexion directe de l'administrateur root ?",
                'opts': ['PermitRootLogin no', 'RootAccess false', 'DisableRoot yes', 'PasswordAuthentication no'],
                'rep': 'PermitRootLogin no',
                'expl': "La directive 'PermitRootLogin no' désactive l'accès direct en root, forçant l'utilisation d'un compte intermédiaire avec sudo."
            },
            {
                'q': "5. Quelle est la particularité fondamentale d'un hyperviseur de Type 1 (ex: VMware ESXi, Proxmox) ?",
                'opts': ['Il s\'exécute comme un logiciel dans Windows', 'Il s\'exécute directement sur le matériel physique (Bare-Metal)', 'Il ne peut virtualiser que des conteneurs Linux', 'Il est moins performant qu\'un hyperviseur Type 2'],
                'rep': 'Il s\'exécute directement sur le matériel physique (Bare-Metal)',
                'expl': "Un hyperviseur Type 1 s'installe directement sur le hardware sans système d'exploitation hôte intermédiaire."
            },
            {
                'q': "6. En C++, pourquoi place-t-on les attributs d'une classe en visibilité 'private' plutôt qu'en 'public' ?",
                'opts': ['Pour accélérer la vitesse d\'exécution du CPU', 'Pour empêcher toute modification externe directe et garantir la cohérence des données via des méthodes', 'Pour économiser la mémoire vive (RAM)', 'Parce que le C++ interdit le mot-clé public pour les variables'],
                'rep': 'Pour empêcher toute modification externe directe et garantir la cohérence des données via des méthodes',
                'expl': "L'encapsulation (private + getters/setters) protège l'état interne de l'objet contre les altérations sauvages."
            }
        ]

        score_rem = 0
        for idx, item in enumerate(rem_q):
            st.markdown(f"**{item['q']}**")
            ans = st.radio(f"Votre choix (Q{idx+1}) :", item['opts'], key=f"rad_rem_{idx}")
            if ans == item['rep']:
                score_rem += 1

        if st.button('Valider mes réponses de Remédiation', type='primary', key='btn_val_rem'):
            if score_rem == 6:
                st.success(f"🏆 **Félicitations ! Score parfait : {score_rem} / 6 !** Vos 6 lacunes sont parfaitement maîtrisées.")
                st.balloons()
            elif score_rem >= 4:
                st.info(f"👍 **Bon résultat : {score_rem} / 6.** Relisez les mini-fiches des questions où vous avez hésité.")
            else:
                st.warning(f"⚠️ **Score : {score_rem} / 6.** Prenez le temps de revoir les fiches et visionnez les vidéos recommandées.")

