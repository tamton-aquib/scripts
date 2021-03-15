#!/usr/bin/env python3
import requests
import base64
import sys

if len(sys.argv) == 0 or '-h' in sys.argv: print('Usage: "python3 imgur_upload.py file_name"')

client_id, client_secret = "", ""     # Get by registering in https://api.imgur.com/oauth2/addclient
filename = sys.argv[1].strip()
name = filename.split('/')[-1]

result = ""

url = "https://api.imgur.com/3/image"
headers = {"Authorization" : f"Client-ID {client_id}"}
encoded = base64.b64encode(open(filename, 'rb').read()).decode()
payload = {
    "key": client_secret,
    "image": encoded,
    "name": name,
    "title": "I Dont know."
}
files=[]

response = requests.post(url, headers=headers, data=payload, files=files).json()

print("Uploading Image...")
for k, v in response['data'].items():
    result += f"{k.ljust(15)} : {v}\n"
print("==========================================")
print(result)
print("==========================================")
