#! /usr/bin/env

import os, requests

directory = os.listdir('/data/feedback')

for file in directory:
  dict = {}
  with open('/data/feedback/' + file, 'r') as f:
    dict['title'] = f.readline()
    dict['name'] = f.readline()
    dict['date'] = f.readline()
    dict['feedback'] = f.readline()
  try:
    response = requests.post('http://<external-IP>/feedback/', data=dict)
    response.ok
  except:
    print('Failed with error code: {}'.format(response.status_code))
