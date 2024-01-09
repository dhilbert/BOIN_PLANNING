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
					

					

					<table data-toggle="table"   data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						<thead>
							<tr>
								<?php	
									$num=0;
									$name="#";hd_thead_th($num,$name);$num+=1;
									$name="학교구분";hd_thead_th($num,$name);$num+=1;
									$name="학년";hd_thead_th($num,$name);$num+=1;
									$name="학기";hd_thead_th($num,$name);$num+=1;
									$name="단원명";hd_thead_th($num,$name);$num+=1;
									$name="차시";hd_thead_th($num,$name);$num+=1;
									$name="차시명";hd_thead_th($num,$name);$num+=1;
									$name="문제";hd_thead_th($num,$name);$num+=1;
									
									
								?>
							


							</tr>
						</thead>
					<tbody>
					<?php 
						$total = 0;
						$total_second =0;
						$total_cnt =0;
						$sql	 = "
									SELECT gu.EDU_GUBN,gu.SCHOOL_YEAR,gu.SEMESTER,gu.UNIT_VALUE,lo.LBNO	,lo.lesson,qt.BODY_HTML,qt.QSNO

									FROM kerisaig.questions AS qt
										JOIN kerisaig.learning_objectives AS lo
									ON qt.LBNO = lo.LBNO	
										JOIN kerisaig.grade_unit AS gu
									ON gu.GUNO = lo.GUNO	
									
								LIMIT 10";

						$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
						while($info	 = mysqli_fetch_array($res)){
							$total += 1;
							echo "<tr>";
								$name = $total ;hd_tbody_td($num,$name);$num+=1;
								$name = $info['EDU_GUBN'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['SCHOOL_YEAR'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['SEMESTER'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = "<a href='detial.php?QSNO=".$info['QSNO']."'>".$info['UNIT_VALUE']."</a>" ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['LBNO'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = $info['lesson'] ;	hd_tbody_td($num,$name);$num+=1;
								$name = "<div class='cdml_question'><div class='question_box'>".$info['BODY_HTML']."</div></div>" ;        
    
	hd_tbody_td($num,$name);$num+=1;

								
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






