"""Les 26 exercices de terminal : bonne réponse -> succès + « +N XP » ; 2e validation -> « déjà gagnés » ; XP ajoutés une seule fois.
Usage : python harness_labs.py <app.py> <dossier>"""
import os, re, sys
from streamlit.testing.v1 import AppTest

app, wd = sys.argv[1], sys.argv[2]
os.makedirs(wd, exist_ok=True); os.chdir(wd)
R = []


def check(n, c, d=''):
    R.append((n, bool(c))); print(('OK   ' if c else 'ECHEC') + ' ' + n + (f'  -> {d}' if d else ''), flush=True)


C, LX, CPP = 'sel_cisco_lab', 'sel_lx_lab', 'sel_cpp_lab'
LABS = [  # (clé XP, points, page, (clé ou libellé de liste, option), {clé champ: valeur}, clé bouton)
    ('lab_cisco_vlan_access', 20, 'sandbox', (C, 'Atelier 1 :'), {'lab_c1_1': 'switchport mode access', 'lab_c1_2': 'switchport access vlan 40'}, 'btn_chk_c1'),
    ('lab_cisco_trunk', 25, 'sandbox', (C, 'Atelier 2 :'), {'lab_c2_1': 'switchport mode trunk', 'lab_c2_2': 'switchport trunk native vlan 99', 'lab_c2_3': 'switchport trunk allowed vlan 10,20,40'}, 'btn_chk_c2'),
    ('lab_cisco_subif', 25, 'sandbox', (C, 'Atelier 3 :'), {'lab_c3_1': 'encapsulation dot1Q 20', 'lab_c3_2': 'ip address 192.168.20.254 255.255.255.0'}, 'btn_chk_c3'),
    ('lab_cisco_port_sec', 25, 'sandbox', (C, 'Atelier 4 :'), {'lab_c4_1': 'switchport port-security', 'lab_c4_2': 'switchport port-security maximum 2', 'lab_c4_3': 'switchport port-security mac-address sticky', 'lab_c4_4': 'switchport port-security violation shutdown'}, 'btn_chk_c4'),
    ('lab_cisco_route_def', 15, 'sandbox', (C, 'Atelier 5 :'), {'lab_c5': 'ip route 0.0.0.0 0.0.0.0 203.0.113.1'}, 'btn_chk_c5'),
    ('lab_cisco_dhcp', 20, 'sandbox', (C, 'Atelier 6 :'), {'lab_c6_1': 'ip dhcp excluded-address 192.168.10.1 192.168.10.20', 'lab_c6_2': 'ip dhcp pool POOL_LAN'}, 'btn_chk_c6'),
    ('lab_cisco_pat', 25, 'sandbox', (C, 'Atelier 7 :'), {'lab_c7': 'ip nat inside source list 1 interface GigabitEthernet0/0/1 overload'}, 'btn_chk_c7'),
    ('lab_cisco_rsa', 20, 'sandbox', (C, 'Atelier 8 :'), {'lab_c8': 'crypto key generate rsa modulus 2048'}, 'btn_chk_c8'),
    ('lab_cisco_rstp', 20, 'sandbox', (C, 'Atelier 9 :'), {'lab_c9_1': 'spanning-tree mode rapid-pvst', 'lab_c9_2': 'spanning-tree portfast'}, 'btn_chk_c9'),
    ('lab_cisco_show_mac', 15, 'sandbox', (C, 'Atelier 10 :'), {'lab_c10': 'show mac address-table'}, 'btn_chk_c10'),
    ('lab_lx_chmod', 15, 'sandbox', (LX, 'Atelier 1 :'), {'lab_lx1': 'chmod 750 /srv/deploy.sh'}, 'btn_chk_lx1'),
    ('lab_lx_sgid', 20, 'sandbox', (LX, 'Atelier 2 :'), {'lab_lx2': 'chmod 2770 /var/partage'}, 'btn_chk_lx2'),
    ('lab_lx_acl', 20, 'sandbox', (LX, 'Atelier 3 :'), {'lab_lx3': 'setfacl -m u:bob:rw /etc/app.conf'}, 'btn_chk_lx3'),
    ('lab_lx_useradd', 15, 'sandbox', (LX, 'Atelier 4 :'), {'lab_lx4': 'useradd -m -s /bin/bash technicien'}, 'btn_chk_lx4'),
    ('lab_lx_systemctl', 15, 'sandbox', (LX, 'Atelier 5 :'), {'lab_lx5': 'systemctl reload ssh'}, 'btn_chk_lx5'),
    ('lab_lx_ss', 20, 'sandbox', (LX, 'Atelier 6 :'), {'lab_lx6': 'ss -tulpn'}, 'btn_chk_lx6'),
    ('lab_lx_var', 15, 'sandbox', (LX, 'Atelier 7 :'), {'lab_lx7': '$?'}, 'btn_chk_lx7'),
    ('lab_cpp_leak', 20, 'sandbox', (CPP, 'Exercice 1 :'), {'lab_cpp1': 'delete[] bufferMesures;'}, 'btn_chk_cpp1'),
    ('lab_cpp_pure', 20, 'sandbox', (CPP, 'Exercice 2 :'), {'lab_cpp2': 'virtual float lireValeur() = 0;'}, 'btn_chk_cpp2'),
    ('lab_cpp_smart', 20, 'sandbox', (CPP, 'Exercice 3 :'), {'lab_cpp3': 'std::make_unique<int>(100);'}, 'btn_chk_cpp3'),
    ('lab_cpp_getter', 20, 'sandbox', (CPP, 'Exercice 4 :'), {'lab_cpp4': 'float getPressionBar() const { return pressionBar; }'}, 'btn_chk_cpp4'),
    ('lab_ad_ps', 25, 'sandbox', None, {'lab_ad1': "New-ADOrganizationalUnit -Name 'Ingénieurs' -Path 'DC=ciel,DC=local'", 'lab_ad2': 'gpupdate /force'}, 'btn_chk_ad'),
    ('lab_iot_modbus', 25, 'sandbox', None, {'lab_iot1': 'Adresse esclave', 'lab_iot2': 'Read Holding Registers', 'lab_iot3': '2'}, 'btn_chk_iot'),
    ('lab_ipsec_diag', 25, 'cyber', ("Choisis l'atelier pratique :", 'Atelier A'), {'rad_vpn_p': 'Phase 2', 'rad_vpn_c': 'Désaccord sur la déclaration'}, 'btn_diag_ipsec'),
    ('lab_pfsense_rule', 20, 'cyber', ("Choisis l'atelier pratique :", 'Atelier B'), {'rad_pf_int': 'Interface LAN', 'rad_pf_r': 'Source: LAN net | Dest: 192.168.90.10'}, 'btn_val_pfsense'),
    ('lab_pki_csr', 20, 'cyber', ("Choisis l'atelier pratique :", 'Atelier C'), {'rad_csr1': 'clé publique', 'rad_csr2': 'Révoquer le certificat'}, 'btn_val_pki'),
]


def remplir(at, sel, champs):
    if sel:
        k, opt = sel
        sb = [s for s in at.selectbox if (s.key == k or s.label == k)]
        if not sb:
            raise RuntimeError(f'liste {k} introuvable')
        choix = next(o for o in sb[0].options if opt in o)
        sb[0].set_value(choix).run()
    for k, v in champs.items():
        ti = [t for t in at.text_input if t.key == k]
        if ti:
            ti[0].input(v); continue
        rd = [r for r in at.radio if r.key == k]
        if rd:
            rd[0].set_value(next(o for o in rd[0].options if v in o)); continue
        raise RuntimeError(f'champ {k} introuvable')


def btn(at, k):
    return next(b for b in at.button if b.key == k)


for cle, pts, page, sel, champs, bk in LABS:
    try:
        at = AppTest.from_file(app, default_timeout=120)
        at.session_state['nav_slug'] = page
        at.run()
        remplir(at, sel, champs)
        p0 = at.session_state['_profile'].get('points', 0) if '_profile' in at.session_state else 0
        btn(at, bk).click().run()
        ok = [str(s.value) for s in at.success if 'XP' in str(s.value)]
        p1 = at.session_state['_profile'].get('points', 0)
        check(f'{cle} : réussi, « +{pts} XP » affiché, +{pts} XP ajoutés', ok and f'+{pts} XP' in ok[0] and p1 - p0 == pts and not at.exception,
              (ok[:1], p1 - p0, [str(e.value)[:80] for e in at.exception]))
        remplir(at, None, champs)
        btn(at, bk).click().run()
        ok2 = [str(s.value) for s in at.success if 'XP' in str(s.value)]
        p2 = at.session_state['_profile'].get('points', 0)
        check(f'{cle} : 2e validation -> « déjà gagnés », aucun XP en plus', ok2 and 'déjà gagnés' in ok2[0] and p2 == p1, (ok2[:1], p2 - p1))
    except Exception as e:
        check(f'{cle} : test exécuté', False, f'{type(e).__name__}: {str(e)[:120]}')
print(f"RESUME {sum(1 for r in R if r[1])} réussis / {sum(1 for r in R if not r[1])} échoués")
