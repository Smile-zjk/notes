## README

1_eval.php 1_system.php 为两个基础的一句话木马
eval.py system.py 为对应的利用脚本
init.sh monitor.sh 为监控脚本，需要用`chmod +x init.sh monitor.sh`加执行权限，创建对应目录，先运行init.sh，需要查看改动时运行monitor.sh
shell1.php shell2.php 为两个不死马，第一个是该权限的，第二个是修改时间的，没有太大区别
raw_door.py为原始木马的利用
z_generate_shell_path.py 生成shell路径
z_upload_shell.py  批量上传木马
upd.py 单独把上传木马功能摘了出来，方便自己临时改
eval_list.py 上次比赛用的脚本，批量获取flag