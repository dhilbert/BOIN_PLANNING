<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');




$jira_comp_idx = isset($_GET['jira_comp_idx']) ? $_GET['jira_comp_idx'] : 3;
$jira_comp_status = isset($_GET['jira_comp_status']) ? $_GET['jira_comp_status'] : 3;

$temp = $jira_comp_status+1;
$want = $temp%2;
$up_sql	 = "

	update jiraapi_component set 
        jira_comp_status = '".$want."' 
	where jira_comp_idx = '".$jira_comp_idx."'";
$up_res	=  mysqli_query($real_sock,$up_sql) or die(mysqli_error($real_sock));



echo "<script>
        alert('수정 완료');
        parent.location.replace('/BOIN_PLANNING/02_weekreport/01_setting.php');
    </script>";








/*

$sql	 = "select * from jirasync_update order by jirasync_update_idx DESC Limit 1	";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);






*/








?>

<!--


-->