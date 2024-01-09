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
						array('#','업무시간분석')
					);
					breadcrumb($array);
					?>
			<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
업무 시간 분석					
					</div>

					<div class="panel-body">
					검색 기능 추가

					

					<table data-toggle="table"   data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						<thead>
							<tr>
								<?php	

								$temp = array(
									"작업자","총작업시간(시간)"

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
									select author, sum(timeSpentSeconds) as cnt from jira_worklog group by author
						";

						$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
						while($info	 = mysqli_fetch_array($res)){
							$total += 1;
							echo "<tr>";
							$num=0;
								$name = $total ;hd_tbody_td($num,$name);$num+=1;
								$name = "<a href='02_jira_detial.php?author=".$info['author']."'>".$info['author']."</a>" ;	hd_tbody_td($num,$name);$num+=1;
								$name = floor($info['cnt']/3600*10)/10 ;	hd_tbody_td($num,$name);$num+=1;
								
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






