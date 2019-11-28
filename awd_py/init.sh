#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin/:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
# 监控的目录
DIR=/var/www/html/
# 临时文件
TMP_A=/tmp/a.txt
# 遍历指定目录下的文件大小及路径并重定向到日志文件
find $DIR -print0 | xargs -0 du -sb  > $TMP_A
