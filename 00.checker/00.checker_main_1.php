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
						array('#','문항체커')
					);
					breadcrumb($array);
					?>
			<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
						문항 체커
					
					</div>

					<div class="panel-body">
					<?php

						$url ='uptofifty115.json';

						$json_string = file_get_contents($url);
						$object = json_decode($json_string, true);


					
					
					?>

					

					<table data-toggle="table"   data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						<thead>
							<tr>
								<?php	
									$num=0;
									$name="#";hd_thead_th($num,$name);$num+=1;
									$name="body_html";hd_thead_th($num,$name);$num+=1;
									$name="list_html";hd_thead_th($num,$name);$num+=1;
									$name="answer_html";hd_thead_th($num,$name);$num+=1;
									$name="explanation_html";hd_thead_th($num,$name);$num+=1;
									
									
								?>
							


							</tr>
						</thead>
						<tbody>
							<?php 

								
								$total = 0;
								for($i = 0 ; $i < count($object) ; $i++){
									$temp_list =	$object[$i] ;
									$total+=1;
									echo "<tr>";
										$name = $total ;hd_tbody_td($num,$name);$num+=1;
										$name = "<a href='detail_0.php?idx=".$i."'>".$temp_list['body_html']."</a>" ;	hd_tbody_td($num,$name);$num+=1;
										$name = $temp_list['list_html'] ;	hd_tbody_td($num,$name);$num+=1;
										$name = $temp_list['answer_html'] ;	hd_tbody_td($num,$name);$num+=1;
										$name = $temp_list['explanation_html'] ;	hd_tbody_td($num,$name);$num+=1;

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






