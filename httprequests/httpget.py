# sample program to learn http request and response
# -*- coding: utf-8 -*-

import requests

# r = requests.get('http://github.com/timeline.json')

payload = {'key1':'value1', 'key2':'value2'}
r = requests.get("http://httpbin.org/get", params=payload)

print r.text.encode("utf-8")
# print r.status_code

