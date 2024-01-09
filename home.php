<?php
include_once('lib/session.php');
include_once('lib/dbcon_BOIN_PLANNING.php');
include_once('contents_header.php');
include_once('contents_profile.php');
include_once('contents_sidebar.php');






?>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', '갯수'],

		  <?php 
				$sql	 = "SELECT 
								a.jira_status,COUNT(*) as cnt
							FROM jira_main AS a 
							GROUP BY a.jira_status";
				$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
				while($info	 = mysqli_fetch_array($res)){
					echo "['".$info['jira_status']."',     ".$info['cnt']."],";


				};
		 
		 
		 ?>
         
        ]);

        var options = {
          title: '전체 프로젝트'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>




	
	<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">	
	
		<div class="row">
			<ol class="breadcrumb">
				<li><a href="/BOIN_PLANNING/home.php"><svg class="glyph stroked home"><use xlink:href="#stroked-home"></use></svg></a> home				
				</li>

			</ol>
		</div>

		<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">나의 프로젝트 진행상황</div>
					<div class="panel-body">
공사중, 지금은 전체, 나중엔 로그인 한 유저 위주로
<p>※ 완료 기준은 jira_status = ' 완료됨 ' OR  ' close '
<div id="piechart" style="width: 900px; height: 500px;"></div>

<table data-toggle="table"   data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						<thead>
							<tr>
								<?php	
									$num=0;
									$name="#";hd_thead_th($num,$name);$num+=1;
									$name="프로젝트명";hd_thead_th($num,$name);$num+=1;
									$name="진행률";hd_thead_th($num,$name);$num+=1;
									
									$name="잔여없무";hd_thead_th($num,$name);$num+=1;
									$name="전체 work";hd_thead_th($num,$name);$num+=1;									
								?>
							


							</tr>
						</thead>
						<tbody>
							<?php  
							        $total =0;
									$sql	 = "
									SELECT a.project, (
										SELECT COUNT(*) FROM jira_main AS b WHERE b.project = a.project	
										) AS total , (
										SELECT COUNT(*) FROM jira_main AS c WHERE c.project = a.project	AND (c.jira_status = ' 완료됨 ' OR c.jira_status = ' close ')
										) AS cnt_close
										
										FROM jira_main AS a 
									GROUP BY a.project	";
			
									$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
									while($info	 = mysqli_fetch_array($res)){
										$total += 1;
										echo "<tr>";
											$name = $total ;hd_tbody_td($num,$name);$num+=1;
											$name = $info['project'] ;	hd_tbody_td($num,$name);$num+=1;
											$temp = floor($info['cnt_close']/$info['total']*1000)/10;
											$name = $temp."%" ;	hd_tbody_td($num,$name);$num+=1;
											
											$name = $info['cnt_close'] ;	hd_tbody_td($num,$name);$num+=1;
											$name = $info['total'] ;	hd_tbody_td($num,$name);$num+=1;											
											
				
											
			
											
										echo "</tr>";
									}
								
			
									?>
							
							
					
						</tbody>
						</table>







					</div>
				</div>
			</div>
			
		</div><!--/.row-->
		



		<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">작업자별</div>
					<div class="panel-body">


					<table data-toggle="table"   data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						<thead>
							<tr>
								<?php	
									$num=0;
									$name="#";hd_thead_th($num,$name);$num+=1;
									$name="작업자/팀";hd_thead_th($num,$name);$num+=1;
									$name="프로젝트명";hd_thead_th($num,$name);$num+=1;
									$name="진행률";hd_thead_th($num,$name);$num+=1;
									
									$name="잔여없무";hd_thead_th($num,$name);$num+=1;
									$name="전체 work";hd_thead_th($num,$name);$num+=1;									
								?>
							


							</tr>
						</thead>
						<tbody>
							<?php  
							        $total =0;
									$sql	 = "
									SELECT a.assignee,a.project, (
										SELECT COUNT(*) FROM jira_main AS b WHERE b.project = a.project	and b.assignee = a.assignee
										) AS total , (
										SELECT COUNT(*) FROM jira_main AS c WHERE c.project = a.project	and c.assignee = a.assignee AND (c.jira_status = ' 완료됨 ' OR c.jira_status = ' close ')
										) AS cnt_close
										
										FROM jira_main AS a 
									GROUP BY a.assignee,a.project	";
			
									$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
									while($info	 = mysqli_fetch_array($res)){
										$total += 1;
										echo "<tr>";
											$name = $total ;hd_tbody_td($num,$name);$num+=1;
											$name = $info['assignee'] ;	hd_tbody_td($num,$name);$num+=1;
											$name = $info['project'] ;	hd_tbody_td($num,$name);$num+=1;
											$temp = floor($info['cnt_close']/$info['total']*1000)/10;
											$name = $temp."%" ;	hd_tbody_td($num,$name);$num+=1;
											
											$name = $info['cnt_close'] ;	hd_tbody_td($num,$name);$num+=1;
											$name = $info['total'] ;	hd_tbody_td($num,$name);$num+=1;											
											
				
											
			
											
										echo "</tr>";
									}
								
			
									?>
							
							
					
						</tbody>
						</table>









					</div>
				</div>
			</div>
			
		</div><!--/.row-->
		





								
	</div>	<!--/.main-->
<?php include_once('contents_footer.php');?>