<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');



$temp_end_date = date("Y-m-d");
$temp_start_date = date("Y-m-d", strtotime("-7 Day"));




$jira_comp_idx = isset($_GET['jira_comp_idx']) ? $_GET['jira_comp_idx'] : 'BAT글로';
$start_date = isset($_GET['start_date']) ? $_GET['start_date'] : $temp_start_date;
$end_date = isset($_GET['end_date']) ? $_GET['end_date'] : $temp_end_date ;




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
						
					<table width='100%'>
							<tr>
								<td align='left'>			공수 측정</td>
								<td align='right'>
									<form name="frm" role="form" method="get" action="02_loreal_down.php">

																			

										<input type = 'hidden' name = 'jira_comp_idx' value = '<?php echo $jira_comp_idx ?>'>
										<input type = 'hidden' name = 'start_date' value = '<?php echo $start_date ?>'>
										<input type = 'hidden' name = 'end_date' value = '<?php echo $end_date ?>'>


										<input  type='submit' class="btn btn-success login-btn" type="submit" value="엑셀 다운로드">					
				</form>
								</td>
							</tr>

				</table>
						
						</div>

					</div>

					<div class="panel-body">
					<form name="frm" role="form" method="get" action="02_loreal.php">


					<div class="form-group">
						<label>업체 선택</label>
							<select multiple class="form-control" name = 'jira_comp_idx'>
								
							<?php 
								$sql	 = "select * from jiraapi_component where jira_comp_status = 1";
								$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
								while($info	 = mysqli_fetch_array($res)){

									if($jira_comp_idx==$info['jira_comp_name'])	{$temp='selected';}
									else {$temp='';}	

									echo "<option value='".$info['jira_comp_name']."' ".$temp.">".$info['jira_comp_name']."</option>";


								};
					
							?>	

					
							
							
						</select>
					</div>



					<label>시작 시간</label>
								<div class="form-group has-success">
									<input type = 'date' class="form-control" name='start_date' value = '<?php echo $start_date?>'>
								</div>
					<label>마지막 시간</label>								
								<div class="form-group has-success">
									<input type = 'date' class="form-control" name='end_date' value = '<?php echo $end_date?>'>
								</div>
					<input  type='submit' class="btn btn-success login-btn" type="submit" value="검색">					
				</form>


				<h2> 작업자별 공수</h2>



				<table data-toggle="table"  data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
	<thead>
		<tr>
			<?php	
				$num=0;
				$name="#";hd_thead_th($num,$name);$num+=1;
				$name="작업자명";hd_thead_th($num,$name);$num+=1;
				$name="초";hd_thead_th($num,$name);$num+=1;
				$name="공수";hd_thead_th($num,$name);$num+=1;
				$name="갯수";hd_thead_th($num,$name);$num+=1;
				
			?>
		


		</tr>
	</thead>
<tbody>
<?php 

$total = 0;
$total_second =0;
$total_cnt =0;
$sql	 = "

SELECT a.jw_dix,a.jmi_work_name,SUM(a.timeSpentSeconds) as totalsecond,(SUM(a.timeSpentSeconds/3600)/8)/20.8 as totalgong,count(a.jw_dix) as cnt


		
from  jirasync_work as a
	JOIN jirasync_main_info as b
ON a.jmi_inx = b.jmi_inx
	WHERE b.components LIKE '%".$jira_comp_idx ."%'
	AND a.check_date BETWEEN '".$start_date."' AND '".$end_date."'
GROUP BY a.jmi_work_name 
";



$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
	$total += 1;
	$total_second +=$info['totalsecond'];
	$total_cnt +=$info['cnt'];
	echo "<tr>";
		$name = $total ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['jmi_work_name'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['totalsecond'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = round($info['totalgong'],2) ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['cnt'] ;	hd_tbody_td($num,$name);$num+=1;
	echo "</tr>";
}
$total += 1;
echo "<tr>";
		$name = $total ;	hd_tbody_td($num,$name);$num+=1;
		$name = '합계' ;	hd_tbody_td($num,$name);$num+=1;
		$name = $total_second ;	hd_tbody_td($num,$name);$num+=1;
		$name = round((($total_second/3600)/8)/20.8,2) ;	hd_tbody_td($num,$name);$num+=1;
		$name = $total_cnt ;	hd_tbody_td($num,$name);$num+=1;
echo "</tr>";


?>

</tbody>
</table>


<h2> 작업별</h2>


<table data-toggle="table"  data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
	<thead>
		<tr>
			<?php	
				$num=0;
				$name="#";hd_thead_th($num,$name);$num+=1;
				$name="작업자명";hd_thead_th($num,$name);$num+=1;
				$name="초";hd_thead_th($num,$name);$num+=1;
				$name="작업일자";hd_thead_th($num,$name);$num+=1;
				$name="작업명";hd_thead_th($num,$name);$num+=1;
				$name="브랜드";hd_thead_th($num,$name);$num+=1;
				
				$name="코멘트";hd_thead_th($num,$name);$num+=1;
				
				
			?>
		


		</tr>
	</thead>
<tbody>
<?php 

$total = 0;
$sql	 = "

SELECT 

	
	a.jmi_work_name,
	a.timeSpentSeconds,
	b.jmi_summary,
	b.components,
	
	a.comment	,a.jmi_key,a.check_date


		
from  jirasync_work as a
	JOIN jirasync_main_info as b
ON a.jmi_inx = b.jmi_inx
	WHERE b.components LIKE '%".$jira_comp_idx ."%'
	AND a.check_date BETWEEN '".$start_date."' AND '".$end_date."'

";

$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
	$total += 1;
	echo "<tr>";
		$name = $total ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['jmi_work_name'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['timeSpentSeconds'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['check_date'] ;	hd_tbody_td($num,$name);$num+=1;
		
		$name = $info['jmi_summary'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['components'] ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['comment'] ;	hd_tbody_td($num,$name);$num+=1;
		
	echo "</tr>";
}


?>

</tbody>
</table>







<!--

$name = "<a href='https://mz-dev.atlassian.net/browse/".$info['jmi_key']."'>".$info['jmi_summary']."</a>";	hd_tbody_td($num,$name);$num+=1;



-->

















					</div>
				</div>
			</div>



		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


/*
고객명 : 고객명
메일 제목 : 
비고 : summary
개발 운선 순위 : 작업타입
진척률 : 개수
우선 순위 : 메일 제목


*/

	/*
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

	*/	
	

	?>
