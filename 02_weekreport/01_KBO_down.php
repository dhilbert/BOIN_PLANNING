<?php

include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');


$jiraapi_fixversion_test = '';
$temp_nu = 0;
$sql	 = "select * from jiraapi_fixversion where jira_fix_status = 1;";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
	$temp_nu +=	$info["jira_fix_idx"];
}

$temp_arry=array($temp_nu/3);


$jiraapi_status = isset($_GET['jiraapi_status']) ? $_GET['jiraapi_status'] : array(1,2,3,4,5);
$jiraapi_fixversion = isset($_GET['jiraapi_fixversion']) ? $_GET['jiraapi_fixversion'] : $temp_arry;
$searchtext = isset($_GET['searchtext']) ? $_GET['searchtext'] : Null;












$sql	 = "select * from jiraapi_fixversion where jira_fix_status = 1;";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
	$temp_nu +=	$info["jira_fix_idx"];

	$temp_checked = "";
	if(in_array($info["jira_fix_idx"],$jiraapi_fixversion))	{
		$temp_checked = "checked";

	}




	$jiraapi_fixversion_test =$jiraapi_fixversion_test.'<div class="checkbox" >
		<label>
			<input type="checkbox" value="'.$info["jira_fix_idx"].'" name="jiraapi_fixversion[]"  '.$temp_checked.' >'.$info["jira_fix_name"].'
		</label>
	</div>
	';
};




function hd_last_text($jiraapi_status){
	$want_text_1 = "('";
	for($i = 0 ; $i < count($jiraapi_status) ; $i++){
		$want_text_1 =$want_text_1.$jiraapi_status[$i]."','";
	}
	$want_text_1 = substr($want_text_1, 0, -2);
	$want_text_1 = $want_text_1.")";
	return $want_text_1;
}

$temp_array = array();
$sql	 = "select * from jiraapi_fixversion where jira_fix_idx in ". hd_last_text($jiraapi_fixversion).";";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
	array_push($temp_array,$info['jira_fix_name']);
}



$temp_array1 = array();
$sql	 = "select * from jiraapi_status where jira_status_idx in ". hd_last_text($jiraapi_status).";";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
	array_push($temp_array1,$info['jira_status_name']);
}


















$EXCEL_STR = "
<table border='1'>
		<thead>
			<tr>
				
				<th>#</th>
				<th>지라번호</th>
				<th>상태</th>			
				
				<th>	제목			</th>
				<th>	우선순위		</th>
				<th>	기획담당		</th>
				<th>	개발담당		</th>
				
				<th> 계획 시작일			</th>
				<th> 계획 종료일			</th>				
				<th>	실 업무 시작일		</th>
				<th> 실 업무 종료일			</th>				
				<th>	요청자				</th>
				<th>	요청 내용(메일내용)			</th>
				<th>	작업 내용				</th>
				<th>	진척률				</th>
				<th>비고			</th>
				

				</tr>

		</thead>
		<tbody>
";





$url = "https://mz-dev.atlassian.net/rest/api/latest/search?jql=";

$jql = "component in ('BAT글로') and fixVersion in".hd_last_text($temp_array)." and status in ".hd_last_text($temp_array1)."";
$jql = "component in ('BAT글로') and fixVersion in".hd_last_text($temp_array)." and status in ".hd_last_text($temp_array1)."";

$jql = urlencode($jql);
$url = $url.$jql."&maxResults=2000&fields=key,ORDER%20BY%20key%20DESC";


$username = 'yoonhd@mz.co.kr';

$password = 'MCmZeIlRDEyrPdpySeeEF57D';

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
$result = curl_exec($curl);












$total_num = 0;
for($i = 0 ; $i <count($ress['issues']); $i++){
	$total_num+=1;
	$temp_list = $ress['issues'][$i];
	$username = 'yoonhd@mz.co.kr';
	$password = 'MCmZeIlRDEyrPdpySeeEF57D';
	$sub_url = $temp_list['self'];
	
	$sub_curl = curl_init();
	curl_setopt($sub_curl, CURLOPT_USERPWD,"$username:$password");
	curl_setopt($sub_curl, CURLOPT_URL, $sub_url);
	curl_setopt($sub_curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($sub_curl, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($sub_curl, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($sub_curl, CURLOPT_SSL_VERIFYHOST, 0);
	curl_setopt($sub_curl,CURLOPT_RETURNTRANSFER,1);
	
	//$result = curl_exec($curl);
	$sub_ress=json_decode(curl_exec($sub_curl),true);
	


	
	$EXCEL_STR=$EXCEL_STR."<tr>
		
		<td>".$total_num."</td>
		<td><a href='https://mz-dev.atlassian.net/browse/".$temp_list['key']."'>".$temp_list['key']."</a>"."</td>
		<td>".$sub_ress['fields']['status']['name']."</td>
		<td>".$sub_ress['fields']['summary']."</td>
		<td>".$sub_ress['fields']['customfield_12271']."</td>
		<td>".$sub_ress['fields']['reporter']['displayName']."</td>
		<td>".$sub_ress['fields']['assignee']['displayName']."</td>
		<td>".$sub_ress['fields']['customfield_12266']."</td>
		<td>".$sub_ress['fields']['customfield_12267']."</td>
		<td>".$sub_ress['fields']['customfield_12268']."</td>
		<td>".$sub_ress['fields']['customfield_12269']."</td>
		<td>".$sub_ress['fields']['customfield_12261']."</td>
		<td>".$sub_ress['fields']['customfield_12262']."</td>
		<td>".$sub_ress['fields']['description']."</td>
		<td>".$sub_ress['fields']['customfield_12270']."</td>
		<td>".$sub_ress['fields']['environment']."</td>

		
		
	</tr>"	;


}
$today = date("Y-m-d H:i:s");

















header( "Content-type: application/vnd.ms-excel" );
header( "Content-type: application/vnd.ms-excel; charset=utf-8");
header( "Content-Disposition: attachment; filename = [KBO]운영현황_".$today.".xls" );
header( "Content-Description: PHP4 Generated Data" );


$EXCEL_STR .= "</tbody></table>";
echo $EXCEL_STR;

echo "<meta content=\"application/vnd.ms-excel; charset=UTF-8\" name=\"Content-type\"> ";




 
?>