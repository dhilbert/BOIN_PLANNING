<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');





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

?>










			<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">			
					<?php
					$array = array(
						array('#','직원 관리')
					);
					breadcrumb($array);
					?>
			<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
						<?php

						$request_uri = $_SERVER['REQUEST_URI'];
						$url =  $request_uri;						

						$temp_url = explode("01_KBO.php?",$url);
						
						
						?>
						<table width='100%'>
							<tr>	
							<td>KBO 주간 보고서<td>
							<td><a href="01_KBO_down.php?<?php echo $temp_url[1] ; ?>" class="btn btn-success login-btn" >            엑셀다운로드     </a>   <td>

							</tr>	
						</table>
					</div>

					<div class="panel-body">

					<form name="frm" role="form" method="get" action="01_KBO.php">

				<table width=100%>		
					<tr>	
						<td width=20%>
							<label>업무단계</label>
						</td>
						<td width=20%>
							<label>업무 시기</label>
						</td>
						
					</tr>							
					<tr>
						<td>	
							<div class="form-group">
							<?php








								$sql	 = "select * from jiraapi_status where jira_status_status = 1;";
								$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
								while($info	 = mysqli_fetch_array($res)){

									$temp_checked = "";
									if(in_array($info["jira_status_idx"],$jiraapi_status))	{
										$temp_checked = "checked";

									}

									echo '<div class="checkbox">
										<label>
											<input type="checkbox" value="'.$info["jira_status_idx"].'"  name="jiraapi_status[]" '.$temp_checked.' >'.$info["jira_status_name_print"].'
										</label>
									</div>
									';
								};
							?>
							</div>
					
							</td>							
						<td>														
							
								<?php echo $jiraapi_fixversion_test?>









						</td>							
												
					</tr>
					



				</table>					

<input  type='submit' class="btn btn-success login-btn" type="submit" value="검색">
					
				</form>







					
				
<?php




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









//HF974VPUAVVTG9CFKQGMR5XE




$url = "https://mz-dev.atlassian.net/rest/api/latest/search?jql=";
$jql = "component in ('BAT글로') and fixVersion in".hd_last_text($temp_array)." and status in ".hd_last_text($temp_array1)."";
$jql = urlencode($jql);
$url = $url.$jql."&maxResults=2000&fields=key";



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










?>




<table data-toggle="table"  data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
	<thead>
		<tr>
			<?php	
				$num=0;
				$name="#";hd_thead_th($num,$name);$num+=1;
				$name="지라번호";hd_thead_th($num,$name);$num+=1;
				$name="상태";hd_thead_th($num,$name);$num+=1;
				
				
				$name="	제목			";hd_thead_th($num,$name);$num+=1;
				$name="	우선순위					";hd_thead_th($num,$name);$num+=1;
				$name="	기획담당			";hd_thead_th($num,$name);$num+=1;
				$name="	개발담당			";hd_thead_th($num,$name);$num+=1;
				
				$name=" 계획 시작일				";hd_thead_th($num,$name);$num+=1;
				$name=" 계획 종료일				";hd_thead_th($num,$name);$num+=1;
				
				$name="	실 업무 시작일			";hd_thead_th($num,$name);$num+=1;
				$name=" 실 업무 종료일			";hd_thead_th($num,$name);$num+=1;
				
				$name="	요청자			";hd_thead_th($num,$name);$num+=1;
				$name="	요청 내용(메일내용)			";hd_thead_th($num,$name);$num+=1;
				$name="	작업 내용			";hd_thead_th($num,$name);$num+=1;
				$name="	진척률			";hd_thead_th($num,$name);$num+=1;
				$name="비고				";hd_thead_th($num,$name);$num+=1;				
				
			?>
		


		</tr>
	</thead>
<tbody>
<?php

$total_num = 0;
for($i = 0 ; $i <count($ress['issues']); $i++){



	$total_num+=1;
	$temp_list = $ress['issues'][$i];

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
	


	
	echo "<tr>"	;
		$num=0;
		$name = $total_num ;	hd_tbody_td($num,$name);$num+=1;
		$name = "<a href='https://mz-dev.atlassian.net/browse/".$temp_list['key']."'>".$temp_list['key']."</a>" ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['status']['name'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['summary'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['customfield_12271'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['reporter']['displayName'] ;	hd_tbody_td($num,$name);$num+=1;


		$name = $sub_ress['fields']['assignee']['displayName'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['customfield_12266'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['customfield_12267'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['customfield_12268'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['customfield_12269'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['customfield_12261'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['customfield_12262'] ;	hd_tbody_td($num,$name);$num+=1;

		$name = mb_substr($sub_ress['fields']['description'] ,0,30,'UTF-8');	hd_tbody_td($num,$name);$num+=1;
		



		
		
		$name = $sub_ress['fields']['customfield_12270'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $sub_ress['fields']['environment'] ;	hd_tbody_td($num,$name);$num+=1;

		
		
	echo "</tr>"	;
	
}

?>

</tbody>
</table>
























					</div>
				</div>
			</div>



		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>




<div class="modal fade" id="99_0_mysettiong_main_0" role="dialog">
	<div class="modal-dialog modal-lg">
		<!-- Modal content-->
		<div class="modal-content">
			<div class="modal-header">
				<strong>템플릿 추가</strong>
			</div>
			<div class="modal-body">
				
					<div class="form-group">

					<form name="frm" role="form" method="get" action="99_0_mysettiong_main_proc.php">

						<label>업무 유형</label>							
							<input class='form-control'		name = 'indi_tem_title'	style='background-color:'><p><br>
						<label>업체</label>							
							<select class="form-control" name = 'jira_comp_idx'>
							<?php
								$jiraapi_component_sql	 = "select * from jiraapi_component where jira_comp_status =1;";
								$jiraapi_component_res	=  mysqli_query($real_sock,$jiraapi_component_sql) or die(mysqli_error($real_sock));
								while($jiraapi_component_info	 = mysqli_fetch_array($jiraapi_component_res)){
										echo "<option value = '".$jiraapi_component_info['jira_comp_idx']."'>".$jiraapi_component_info['jira_comp_name']."</option>";
								};
							?>
							</select>
						<label>회사 선택</label>
						<select class="form-control" name = 'company_idx'>
							<?php
								$admin_company_info_sql	 = "select * from admin_company_info;";
								$admin_company_info_res	=  mysqli_query($real_sock,$admin_company_info_sql) or die(mysqli_error($real_sock));
								while($admin_company_info_info	 = mysqli_fetch_array($admin_company_info_res)){
										echo "<option value = '".$admin_company_info_info['company_idx']."'>".$admin_company_info_info['company_name']."</option>";
								};
							?>
							</select>
							<div class="form-group">
									<label>템플릿 입력</label>
									<textarea class="form-control" rows="4" name ='indi_tem_maintext'></textarea>
							</div>








						</div>
						<p><br>
					














				


			</div>
			<div class="modal-footer">
			<input  type='submit' class="btn btn-success login-btn" type="submit" value="템플릿 등록">
				</form>


				 <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
			</div>
		</div>
	</div>
</div>
