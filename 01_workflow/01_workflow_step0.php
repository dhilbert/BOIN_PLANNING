<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');





$indi_tem_idx = isset($_GET['indi_tem_idx']) ? $_GET['indi_tem_idx'] : 3;
$mails = isset($_GET['mails']) ? $_GET['mails'] : 3;



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
					gmail 확인 (공사중 테스트 페이지)
					
					</div>

					<div class="panel-body">

					<form name="frm" role="form" method="get" action="01_workflow_step1.php">

					<?php

$url = 'https://gmail.googleapis.com/gmail/v1/users/yoonhd@mz.co.kr/messages/17fac5d07bcbfcad?access_token=ya29.A0ARrdaM8jUXJeTC6U6neCQdxsFRI5dqu2cRtftvQB8_KP1wMg8nWIQVNiymMJu7lhp6gBu7CiWOZFKXAVD5bgY8yI2ICu_QIBc_5ZqbXUoDejwbQWFFHP2KlAl4xvACV7skJsxIDV0SKQP4t-OpiSuHtcUlXH';
$response = file_get_contents($url);
$object = json_decode($response,true);
?>
<div class="form-group">
	<label>지라 제목</label>
	<input class="form-control" placeholder="Placeholder" value='[로레알_아르마니]<?php echo $object['payload']['headers'][38]['value']?>' name='summary'>
</div>
<div class="form-group">
	<label>설명</label>
	<textarea class="form-control" rows="50" name='description'>
<?php
	$admin_company_info_sql	 = "select * from individual_template_main where indi_tem_idx =".$indi_tem_idx ." ;";
	$admin_company_info_res	=  mysqli_query($real_sock,$admin_company_info_sql) or die(mysqli_error($real_sock));
	$admin_company_info_info	 = mysqli_fetch_array($admin_company_info_res);
	echo $admin_company_info_info['indi_tem_maintext'] ;

?>

작업 요청자 : <?php 	echo $object['payload']['headers'][74]['value'];?>
메일 내용
<?php 	echo $object['snippet'];?></textarea>
</div>

<input  type='submit' class="btn btn-success login-btn" type="submit" value="지라 생성하고, 슬랙 보내기">
				</form>










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
