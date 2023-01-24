import psutil
import time
import requests
import json
from datetime import datetime
def Torkill():
    for proc in psutil.process_iter():
        if proc.name() == 'tor.exe':
            proc.kill()
            print("Tor killed")
while True:
	Torkill()
	time.sleep(5)
	break