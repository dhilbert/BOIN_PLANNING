<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');




$jirasync_update_date = isset($_GET['jirasync_update_date']) ? $_GET['jirasync_update_date'] : 3;

$sql	 = "select * from jirasync_update order by jirasync_update_idx DESC Limit 1	";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);



$up_sql	 = "

	update jirasync_update set 
		jirasync_update_date = '".$jirasync_update_date."' 
	where jirasync_update_idx = '".$info['jirasync_update_idx']."'";
$up_res	=  mysqli_query($real_sock,$up_sql) or die(mysqli_error($real_sock));



echo "<script>
        alert('일자 수정 완료');
        parent.location.replace('/BOIN_PLANNING/05_jira_update/jira_update_main_date.php');
    </script>";












?>

<!--


-->