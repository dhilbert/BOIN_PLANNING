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
						array('#','주간보고')
					);
					breadcrumb($array);
					?>
			<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
주간 보고
					</div>

					<div class="panel-body">
					검색 기능 추가

					

					<table data-toggle="table"   data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						<thead>
							<tr>
								<?php	

								$temp = array(
									"주차","기간"

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
						$temp = array("1주차",'2주차');
						$temp1 = array("1/1~1/7","1/8~1/14");
						for($i =0 ; $i < count($temp);$i++){
							$total += 1;
							echo "<tr>";
								$num=0;
								$name = $total ;hd_tbody_td($num,$name);$num+=1;
								$name = $temp[$i] ;hd_tbody_td($num,$name);$num+=1;
								$name = $temp1[$i] ;hd_tbody_td($num,$name);$num+=1;
								
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






