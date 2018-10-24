#!/usr/bin/python2.7
import requests
import sys
import json
tw_url='https://api.sandbox.transferwise.tech/v1/rates?source=EUR&target=INR'
headers={'Authorization' : 'Bearer ce21ac17-c0b4-4ec0-879f-85005c5ed119'}
resp = requests.get(tw_url,headers=headers)
r=resp.json()
#print (resp.content)
print (r)
print (r['target'])
#r.json()
#print(r)
