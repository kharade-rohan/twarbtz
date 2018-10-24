#!/usr/bin/python2.7
import requests
import sys
r = requests.get('https://koinex.in/api/ticker')
r.json()
print(r)