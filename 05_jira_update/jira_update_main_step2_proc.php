<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');




$sql	 = "select * from jira_update_info order by jui_idx DESC LIMIT 1;";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));


$jira_update_info_info	 = mysqli_fetch_array($res);
$username = 'yoonhd@mz.co.kr';
$password = 'K80gueIJUonHEGUJHQ4y44E6';

$url = "https://mz-dev.atlassian.net/rest/api/latest/search?jql=updated>=".$jira_update_info_info['jui_updatedate']."%20and%20reporter%20in%20(".$jira_id.")%20and%20timespent>0&maxResults=20000&fields=id,key";


$curl = curl_init();
curl_setopt($curl, CURLOPT_USERPWD, "$username:$password");
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);

//$result = curl_exec($curl);
$ress=json_decode(curl_exec($curl),true);



for($i = 0 ; $i <count($ress['issues']); $i++){
	
	include('jira_update_main_step2_ft.php');



}


$jira_update_sql	= "
update jira_work_log set 
work_kind =  SUBSTRING_INDEX(SUBSTRING_INDEX(work_comment, '[', -1), ']', 1)
where work_kind is null
AND LEFT(work_comment,1)='[';";

$jira_update_res	=  mysqli_query($real_sock,$jira_update_sql) or die(mysqli_error($real_sock));

$now = date("Y-m-d H:i:s");


$sql	= "
	insert jira_update_info set 
		jui_updatedate = '".$now."',
		jui_reg_date	 = '".$now."',
		admin_idx = '".$admin_idx."'
";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));


$sql	= "
	update jira_work_log set 

	MZNO_components = '네이처리퍼블릭'
		where MZNO_components = '' or MZNO_components is null
";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));



echo "<script>
alert('업데이트 완료.');
parent.location.replace('/BOIN_PLANNING/jira_update/jira_update_main.php');
</script> ";



?>