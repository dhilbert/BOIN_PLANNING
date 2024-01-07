<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');



$temp_end_date = date("Y-m-d");
$temp_start_date = date("Y-m-d", strtotime("-7 Day"));







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
						업체 관리
						
						</div>

					</div>

					<div class="panel-body">
					<form name="frm" role="form" method="get" action="02_loreal.php">


					<div class="form-group">
					




				<table data-toggle="table"  data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
	<thead>
		<tr>
			<?php	
				$num=0;
				$name="#";hd_thead_th($num,$name);$num+=1;
				$name="업체명";hd_thead_th($num,$name);$num+=1;
				$name="노출여부";hd_thead_th($num,$name);$num+=1;
				$name="상태변경";hd_thead_th($num,$name);$num+=1;
				
			?>
		


		</tr>
	</thead>
<tbody>
<?php 

$total = 0;
$total_second =0;
$total_cnt =0;
$sql	 = "

SELECT * from jiraapi_component order by jira_comp_status DESC

";

$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
	$total += 1;
	echo "<tr>";
		$name = $total ;	hd_tbody_td($num,$name);$num+=1;
		$name = $info['jira_comp_name'] ;	hd_tbody_td($num,$name);$num+=1;
		$array_temp = array('<font color="red">비노출</font>','노출');
		


		$name = $array_temp[$info['jira_comp_status']] ;	hd_tbody_td($num,$name);$num+=1;
		$array_temp_1 = array('노출시키기','<font color="red">비노출노출시키기</font>');
		$name = "<a href ='01_setting_proc.php?jira_comp_idx=".$info['jira_comp_idx']."&jira_comp_status=".$info['jira_comp_status']."'>".$array_temp_1[$info['jira_comp_status']]."</a>";
		;	hd_tbody_td($num,$name);$num+=1;

	echo "</tr>";
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
