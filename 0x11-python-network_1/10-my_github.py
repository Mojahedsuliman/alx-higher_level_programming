#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""

import sys
import requests

username = sys.argv[1]
password = sys.argv[2]
url = f"https://api.github.com/users/{username}"
response = requests.get(url, auth=(username, password))
if response.status_code == 404:
    print("None")
else:
    print(response.json().get('id'))
