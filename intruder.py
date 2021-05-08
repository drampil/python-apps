#!/bin/python3


import requests
from requests.exceptions import SSLError

url = input("Enter Attacking IP Address: ")

print()
headers = {"User-Agent": "AWS Trust and Safety"}
scheme = ["https://", "http://"]

try:
    h = requests.head(f"{scheme[0]}{url}/xmlrpc.php", headers=headers)
except SSLError:
    print("Endpoint does not support TLS, falling back to plaintext...")
    h = requests.head(f"{scheme[1]}{url}/xmlrpc.php", headers=headers)
print()
if h.status_code == 405:
    print(f"{url} is vulnerable to XMLRPC amplification")
elif h.status_code == 403:
    print(f"{url} is protected against XMLRPC amplification")
else:
    print("ERROR: Something is wrong.")
