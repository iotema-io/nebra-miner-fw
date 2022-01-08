import requests
import time
import os
import sys

try:
    req_url = os.environ['REQ_URL']
    miner_name = os.environ['BALENA_DEVICE_NAME_AT_INIT']
except KeyError:
    print('ENV variables not set')
    sys.exit(1)

while True:
    try:
        r = requests.get(req_url, params={'time': time.time() , 'miner_name': miner_name}, timeout=10)
    except requests.exceptions.Timeout:
        print('Timeout')
    except:
        print('Error connecting to server')
        sys.exit(1)
    if r.status_code == 200:   
        print("ACK: " + r.text)
    time.sleep(60)