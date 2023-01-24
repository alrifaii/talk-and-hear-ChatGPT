import os
import stem.process
import re
import requests
import json
from datetime import datetime
import time
from stem.control import Controller
def Toron():
    global tor_process
    SOCKS_PORT = 9050
    TOR_PATH = os.path.normpath("C:\\Users\\Mohamad\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe")
    tor_process = stem.process.launch_tor_with_config(
    config = {
        'SocksPort': str(SOCKS_PORT),
      },
    init_msg_handler = lambda line: print(line) if re.search('Bootstrapped', line) else False,
    tor_cmd = TOR_PATH
    )
def whatisip():
    PROXIES = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
    }
    response = requests.get("http://ip-api.com/json/", proxies=PROXIES)
    result = json.loads(response.content)
    print('TOR IP [%s]: %s %s'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))  
while True:
    Toron()
    whatisip()
    time.sleep(10)
    break
