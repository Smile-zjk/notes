#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin/:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
# 监控的目录
DIR=/var/www/html/
# 日期变量
DATE=`date +%F_%H:%M`
# 临时文件
TMP_A=/tmp/a.txt
TMP_B=/tmp/b.txt
TMP_C=/tmp/c.txt
# 日志文件
LOG=/tmp/cache/modified.txt
# 遍历指定目录下的文件大小及路径并重定向到日志文件
find $DIR -print0 | xargs -0 du -sb  > $TMP_B
# 比较目录变化，并将变化的文件写入日志
DIFF=$(diff $TMP_A $TMP_B)
if [[ -z $DIFF ]];
 then
   echo "Nothing change" >> $LOG
 else
   echo "Here is the change" >> $LOG
   echo "" >> $LOG
   echo "$DIFF" |awk '{print $3}'|sort -k2n |uniq |sed '/^$/d' |tee $TMP_C >> $LOG
   if [ -s $TMP_C ];
     then
       echo "" >> $LOG
       echo "It modified at $DATE" >> $LOG
   fi
fi
echo "====================================" >> $LOG
#清理临时文件
rm -rf $TMP_B $TMP_C
