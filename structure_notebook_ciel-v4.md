# 📓 Carnet de Bord & Référentiel de Révision Exhaustif (v3.0) — BTS CIEL (Option A & B)

Ce carnet de bord numérique récapitule la totalité des savoirs, compétences, protocoles, architectures et travaux pratiques du **BTS Cybersécurité, Informatique et réseaux, Électronique (CIEL)** pour la préparation des épreuves **E4 (Écrit technique), E5 (TP & Pratique) et E6 (Projet de fin d'études)**.

---

## 📑 Table des Matières du Référentiel

1. [📶 Module 1 : Réseaux, Commutation & Interconnexions](#1-module-1--réseaux-commutation--interconnexions)
2. [🔒 Module 2 : Cybersécurité, SysAdmin & Gouvernance](#2-module-2--cybersécurité-sysadmin--gouvernance)
3. [💻 Module 3 : Programmation Software, Embedded C/C++ & Python](#3-module-3--programmation-software-embedded-cc--python)
4. [🔌 Module 4 : Électronique, Signaux, Mesures & Bus Industriels](#4-module-4--électronique-signaux-mesures--bus-industriels)
5. [📐 Module 5 : Modélisation SysML/UML & Ingénierie de Projet E6](#5-module-5--modélisation-sysmluml--ingénierie-de-projet-e6)
6. [📈 Module 6 : Mathématiques Appliquées & Sciences Physiques](#6-module-6--mathématiques-appliquées--sciences-physiques)
7. [🛠️ Module 7 : Guide Réussite Épreuve E5 (Fiches Réflexes TP)](#7-module-7--guide-réussite-épreuve-e5-fiches-réflexes-tp)
8. [🇬🇧 Module 8 : Anglais Technique & Datasheets Constructeurs](#8-module-8--anglais-technique--datasheets-constructeurs)

---

## 1. 📶 Module 1 : Réseaux, Commutation & Interconnexions

### 1.1 Architectures & Protocoles
* **Modèle OSI (7 Couches)** :
  1. Physique (Bit)
  2. Liaison (Trame MAC 48 bits, Ethernet 802.3)
  3. Réseau (Paquet IP 32/128 bits)
  4. Transport (Segment TCP / Datagramme UDP)
  5. Session
  6. Présentation (TLS/SSL, ASCII, JSON)
  7. Application (HTTP, DNS, DHCP, SSH, MQTT).
* **Modèle TCP/IP (4 Couches)** : Accès Réseau, Internet, Transport, Application.
* **Encapsulation** : En-tête Ethernet + En-tête IP + En-tête TCP/UDP + Données Utilisateur + FCS (CRC-32).

### 1.2 Adressage IPv4, IPv6 & Subnetting VLSM
* **Formules VLSM IPv4** :
  - Nombre d'hôtes utiles : $N_{hôtes} = 2^{(32 - CIDR)} - 2$.
  - Adresse Réseau : IP `AND` Masque.
  - Adresse Broadcast : Adresse Réseau + $(2^{(32 - CIDR)} - 1)$.
* **Table des Masques Usuels** :
  - `/24` = `255.255.255.0` (254 hôtes)
  - `/26` = `255.255.255.192` (62 hôtes)
  - `/28` = `255.255.255.240` (14 hôtes)
  - `/30` = `255.255.255.252` (2 hôtes - Point à Point).
* **IPv6 (128 bits)** : Notation hexadécimale condensée, auto-configuration **SLAAC**, protocole **NDP** (Neighbor Discovery Protocol, ICMPv6 type 135/136).

### 1.3 Commutation & VLANs
* **Trunking IEEE 802.1Q** : Insère une étiquette de **4 octets** (32 bits) dans la trame Ethernet, dont 12 bits pour l'identifiant VLAN (VID, 1 à 4094). VLAN Natif (non étiqueté).
* **Routage Inter-VLAN** : *Router-on-a-Stick* avec sous-interfaces logiques (`g0/0.10`, `g0/0.20`) ou Commutateur de Niveau 3 (L3 Switch / SVI).
* **Spanning Tree Protocol (STP / RSTP 802.1w)** : Évite les boucles de commutation L2. Convergence rapide RSTP.

### 1.4 Services Réseaux d'Infrastructure
* **DHCP (Dynamic Host Configuration Protocol)** : Processus **DORA** (Discover, Offer, Request, Acknowledge) sur UDP 67/68. Agent Relais DHCP (`ip helper-address`).
* **DNS (Domain Name System)** : Enregistrements `A` (IPv4), `AAAA` (IPv6), `CNAME` (Alias), `MX` (Mail), `PTR` (Résolution inverse), `TXT` (SPF/DKIM).
* **NAT / PAT (Network Address Translation)** : NAT statique (1:1), NAT dynamique, PAT avec Surcharge (Overload).

---

## 2. 🔒 Module 2 : Cybersécurité, SysAdmin & Gouvernance

### 2.1 Gouvernance, EBIOS RM & RGPD (PIA/AIPD)
* **Méthodologie EBIOS RM (5 Ateliers ANSSI)** :
  1. Socle de sécurité & Valeurs métiers (Biens supports, critères DICP : Disponibilité, Intégrité, Confidentialité, Preuve).
  2. Sources de risques & Visées stratégiques (SR / OV).
  3. Scénarios stratégiques (Écosystème & Partenaires).
  4. Scénarios opérationnels (Cyber Kill Chain, attaques techniques).
  5. Traitement du risque & PACS (Plan d'Amélioration de la Cybersécurité).
* **PIA / AIPD (RGPD Art. 35)** : Analyse d'Impact sur la Protection des Données obligatoire dès que **2 critères sur 9** de la CNIL sont remplis (biométrie, grande échelle, personnes vulnérables, etc.).

### 2.2 PKI, Certificats X.509 & Active Directory
* **PKI (Public Key Infrastructure)** : Root CA (hors ligne / *offline*), Intermediate CA, extension **SAN** (*Subject Alternative Name*), requêtes `CSR`, révocation CRL/OCSP.
* **Active Directory Domain Services (ADDS)** : Forêt -> Domaine -> Unités d'Organisation (OU).
* **GPO (Group Policy Object)** : Ordre d'application **LSDOU** (Local, Site, Domaine, OU). La GPO la plus spécifique prévaut.
* **Matrice des Ports Active Directory** : DNS 53, Kerberos 88, LDAP 389, LDAPS 636, SMB 445, RPC 135.

### 2.3 Administration Système Linux Debian & Hardening ANSSI
* **Permissions & Droits** : Masque octal `chmod` (`750` = `rwx`/`r-x`/`---`), droits spéciaux **SUID (4000)**, SGID (2000), Sticky Bit (1000).
* **ACLs POSIX** : `getfacl` / `setfacl -m u:alice:rwx fichier`.
* **Hardening ANSSI** : Désactivation du login root SSH, changement de port SSH, paramètres sysctl contre le SYN Flood, audit Lynis.
* **Modèle Active Directory Tiering ANSSI** : Partitionnement en Tier 0 (Contrôleurs de domaine), Tier 1 (Serveurs d'applications), Tier 2 (Postes de travail). Déploiement de LAPS.

---

## 3. 💻 Module 3 : Programmation Software, Embedded C/C++ & Python

### 3.1 Gestion Mémoire C/C++ & Pointeurs
* **Pile (Stack)** : Mémoire rapide automatique à portée restreinte (*scope*).
* **Tas (Heap)** : Mémoire dynamique allouée via `new` / `new[]` et libérée **obligatoirement** via `delete` / `delete[]`.
* **Smart Pointers C++11** : `std::unique_ptr` (propriété exclusive) et `std::shared_ptr` (propriété partagée avec compteur de références).

### 3.2 Langage C : Structures, Unions & Registres
* **`struct`** : Emplacement mémoire contigu pour chaque membre.
* **`union`** : **Espace mémoire partagé** égal à la taille du plus grand membre (décodage d'octets de réception en `float` IEEE-754).
* **Opérations Bit-à-Bit** : Masquage ET (`&`), OU (`|`), Décalages (`<<`, `>>`).

### 3.3 POO C++ & Programmation Concurrente
* **Encapsulation & Abstraction** : Accès `private`, `protected`, `public`.
* **Polymorphisme** : Méthode virtuelle pure (`virtual void f() = 0;`), **Classe de base abstraite**, et **Destructeur virtuel obligatoire** (`virtual ~Mere() {}`).
* **Multithreading C++11** : `std::thread`, exclusion mutuelle `std::mutex`, et verrouillage RAII `std::lock_guard`.

### 3.4 Sockets Python & JSON
* **Sockets TCP** : `socket.socket(AF_INET, SOCK_STREAM)`, `bind()`, `listen()`, `accept()`, `sendall()`, `recv()`.
* **Trame JSON** : `json.dumps()` (sérialisation objet -> string) et `json.loads()` (désérialisation).

---

## 4. 🔌 Module 4 : Électronique, Signaux, Mesures & Bus Industriels

### 4.1 Lois Fondamentales & Énergie
* **Loi d'Ohm** : $U = R \cdot I$ | Conductance : $G = 1/R$ ($I = G \cdot U$).
* **Lois de Kirchhoff** : Loi des Nœuds ($\sum I_{entrants} = \sum I_{sortants}$) et Loi des Mailles ($\sum U = 0$).
* **Pont Diviseur de Tension** : $U_2 = E \cdot R_2 / (R_1 + R_2)$.
* **Puissance & Énergie** : $P = U \cdot I = R \cdot I^2 = U^2 / R$, $E = P \cdot \Delta t$.

### 4.2 Signaux, Oscilloscope & Numérisation (CAN / ADC)
* **Théorème de Nyquist-Shannon** : La fréquence d'échantillonnage $Fe$ doit vérifier $Fe \ge 2 \cdot F_{max}$.
* **Convertisseur Analogique-Numérique (CAN 12 bits)** :
  - Quantum : $q = V_{ref} / (2^n - 1)$. Pour $V_{ref} = 5,0	ext{V}$ sur 12 bits : $q = 5,0 / 4095 pprox 1,22	ext{ mV}$.
  - Valeur brute entière : $N = 	ext{arrondi}(V_e / q)$.
* **Oscilloscope** : $V_{pp} = N_{div} \cdot S_v$, $V_{max} = V_{pp} / 2$, $V_{eff} = V_{max} / \sqrt{2}$, $T = N_{div} \cdot S_h$, $f = 1/T$.

### 4.3 Bus de Terrain & Transmissions
* **Bus CAN (Controller Area Network)** : Différentiel (`CAN_H`, `CAN_L`), terminaisons $120\Omega$, arbitrage non destructif **CSMA/CR** (bit dominant `0` écrase bit récessif `1`).
* **Modbus RTU / RS-485** : Liaison série différentielle A/B, transmission maître-esclaves (adresses 1 à 247), Code Fonction `03` (*Read Holding Registers*), contrôle d'erreur CRC-16.
* **PWM / MLI (Pulse Width Modulation)** : Rapport cyclique $lpha = t_{haut} / T$. Tension moyenne $V_{moy} = lpha \cdot V_{max}$.
* **Boucle de Courant 4-20 mA** : $I(T) = 4 + rac{T - T_{min}}{T_{max} - T_{min}} \cdot 16	ext{ mA}$. Détection de rupture si $I = 0	ext{ mA}$.

---

## 5. 📐 Module 5 : Modélisation SysML/UML & Ingénierie de Projet E6

### 5.1 Diagrammes SysML & UML
* **SysML** : *Block Definition Diagram* (BDD, blocs et valeur), *Internal Block Diagram* (IBD, ports et flux), *Requirement Diagram* (exigences, traçabilité `deriveReqt`, `verify`).
* **UML** : Diagramme de Classes (attributs, méthodes, compositions, agrégations), Diagramme de Séquence (messages synchrones/asynchrones, fragments `alt`/`loop`), Diagramme d'États-Transitions.

### 5.2 Ingénierie de Projet E6 (CdCf & PVL)
* **Cahier des Charges Fonctionnel (CdCf - Norme AFNOR NF X50-151)** : Fonctions Principales (FP), Fonctions de Contrainte (FC), Critères, Niveaux et Flexibilité (**F0** à **F3**).
* **Plan de Validation Logicielle (PVL)** : Recettes de tests d'intégration automatisés avec scripts `pytest` et assertions.
* **Recette FAT / SAT** : Procès-verbal de Recette en usine (*Factory Acceptance Test*) et sur site (*Site Acceptance Test*).

---

## 6. 📈 Module 6 : Mathématiques Appliquées & Sciences Physiques

### 6.1 Suites Arithmétiques & Géométriques
* **Suite Arithmétique** : $u_{n+1} = u_n + r$, $u_n = u_0 + n \cdot r$, Somme $S = N \cdot (u_0 + u_{N-1}) / 2$.
* **Suite Géométrique** : $u_{n+1} = u_n \cdot q$, $u_n = u_0 \cdot q^n$, Somme $S = u_0 \cdot (1 - q^N) / (1 - q)$.
* **Limites & Dérivée** : Étude du sens de variation d'une suite $u_n = f(n)$ via l'étude du signe de la dérivée $f'(x)$ sur $[0 ; +\infty[$.

### 6.2 Fonctions Exponentielle, Logarithme & Décibels
* **Exponentielle ($e^x$)** : $e^x > 0$, $(e^{u(x)})' = u'(x) e^{u(x)}$, modélisation de la charge/décharge de condensateur $u_C(t) = E(1 - e^{-t/	au})$.
* **Logarithme Népérien ($\ln(x)$)** : Dérivée $(\ln(x))' = 1/x$, $(\ln(u(x)))' = u'(x) / u(x)$.
* **Atténuation & Gain en Décibels** : $A_{dB} = 10 \log_{10}(P_2 / P_1) = 20 \log_{10}(V_2 / V_1)$.

---

## 7. 🛠️ Module 7 : Guide Réussite Épreuve E5 (Fiches Réflexes TP)

* **Fiche E5-01 : Cisco IOS** : VLANs, Trunk 802.1Q, Router-on-a-Stick, Port Security (`protect`/`restrict`/`shutdown`), Route par défaut.
* **Fiche E5-02 : Linux Debian** : Configuration IP, utilisateurs/groupes, `chmod` octal, SUID, SGID, Sticky bit, `setfacl`/`getfacl`, scripts Bash.
* **Fiche E5-03 : Active Directory & Services** : PowerShell `New-ADUser`, GPO LSDOU, DNS enregistrements A/PTR, DHCP DORA et options.
* **Fiche E5-04 : pfSense & DMZ** : Règle stricte d'isolation DMZ -> LAN, matrice des ports AD, NAT/PAT Port Forwarding.
* **Fiche E5-05 : Wireshark** : Filtres BPF/Display, analyse TCP 3-way handshake, décodage DNS/DHCP/Modbus/CAN.
* **Fiche E5-06 : Oscilloscope & Bus** : Mesures $V_{pp}, V_{eff}, f$, quantum CAN $q$, trames I2C, SPI, Bus CAN, Modbus RTU.
* **Fiche E5-07 : Check-list Diagnostic E5** : Démarche méthodique par couche OSI (L1 -> L2 -> L3 -> L4/L7).

---

## 8. 🇬🇧 Module 8 : Anglais Technique & Datasheets Constructeurs

* **Datasheets Anglaises** : Lecture de spécifications pour ATmega328P, ESP32, STM32F4, MCP2515, MAX485, BTS7960, L298N, MAX6675, DHT22.
* **Glossaire Bilingue (100+ Mots)** : Termes essentiels d'ingénierie réseaux, cybersécurité, développement et électroniques.
* **Soutenance Orale E4/E6 en Anglais** : Phraséologie type pour présenter l'architecture technique de son projet devant le jury.

---

<p align="center"><b>Référentiel Complet BTS CIEL — Prêt pour les Épreuves Officielle 🎓⚡</b></p>
