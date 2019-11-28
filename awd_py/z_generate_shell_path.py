# -*- coding: utf-8 -*-
ip_list = []
for i in range(17,20):
    # ip池，自行调整
	ip_list.append("10.188.14.{0}".format(str(i)))

url = []    
for ip in ip_list:
	# 位置0为ip，位置1为method，位置2为passwd，自行修改
	url.append("http://{0}:80/index.php,{1},{2}\n".format(str(ip),'post','hb'))
with open('shell_path.txt','w') as f:
	for line in url:
		f.write(line)
