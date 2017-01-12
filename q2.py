#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get("http://google.com/https://raw.githubusercontent.com/shadownater/cmput404lab1/master/q2.py")

print response.text
print response.status_code
