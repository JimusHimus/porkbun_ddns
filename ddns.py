#!/usr/bin/python3

import os
import requests

api_key = 'pk1_*****...'
secret_key = 'sk1_*****...'

json = {
    'secretapikey': secret_key,
    'apikey': api_key
}

# getting computer ip
external_ip = requests.post('https://porkbun.com/api/json/v3/ping', json=json).json()['yourIp']

# saving ip in case it is the same don't do unnecessary actions
filename = 'ip.txt'
mode = 'r+' if os.path.exists(filename) else 'w+'
with open(filename, mode) as f:
    saved_ip = f.readline()
    if saved_ip == external_ip:
        # ip has not changed
        quit()
    f.seek(0)
    f.truncate()
    f.write(external_ip)

json['type'] = 'A'
json['ttl'] = '600'
json['content'] = external_ip

# get your ID's with requests.post('https://porkbun.com/api/json/v3/dns/retrieve/<YOUR_DOMAIN>', json={"secretapikey":secret_key, "apikey":api_key}).json()
#  and write them down as 'id': 'name'
records = {
    '145000001': '',
    '145000002': '*'
}

for record_id, record_name in records.items():
    json['name'] = record_name
    requests.post(f'https://porkbun.com/api/json/v3/dns/edit/<YOUR_DOMAIN>/{record_id}', json=json)
