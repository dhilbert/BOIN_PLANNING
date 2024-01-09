<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');











?>
			<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">			
					<?php
					$array = array(
						array('#','전체 카드')
					);
					breadcrumb($array);
					?>
			<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
					전체 카드
					
					</div>

					<div class="panel-body">
					검색 기능 추가

					

					<table data-toggle="table"   data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						<thead>
							<tr>
								<?php	

								$temp = array(
									"키","라벨","우선순위","담당자","상태","만든사람","보고자","프로젝트","잔여시간",
									"지금까지 진행한 시간","작업이름","기한","시작일","마지막확인한일자"

								);
									$num=0;
									$name="#";hd_thead_th($num,$name);$num+=1;
									for($i = 0 ; $i < count($temp); $i++){
										$name=$temp[$i];hd_thead_th($num,$name);$num+=1;

									}


									
								?>
							


							</tr>
						</thead>
					<tbody>
					<?php 
						$total = 0;
						$total_second =0;
						$total_cnt =0;
						$sql	 = "
									select * from jira_main
						";

						$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
						while($info	 = mysqli_fetch_array($res)){
							$total += 1;
							echo "<tr>";
							$num=0;
								$name = $total ;hd_tbody_td($num,$name);$num+=1;
								$name = "<a href='01_jira_detial.php?jm_idx=".$info['jm_idx']."'>".$info['jira_key']."</a>" ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['labels'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['priority'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['assignee'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['jira_status'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['creator'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['reporter'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['project'] ;	hd_tbody_td($num,$name);$num+=1;
								
								$name = $info['remainingEstimateSeconds'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['timeSpentSeconds'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['summay'] ;	hd_tbody_td($num,$name);$num+=1;

								$name = $info['duedate'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['ustomfield_10015'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['updated'] ;	hd_tbody_td($num,$name);$num+=1;
								
								
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






