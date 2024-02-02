<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');



$project = isset($_GET['project']) ? $_GET['project'] : 3;








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
					
					<?php 
echo $project 

?> 진행 률 : 

<?php 
		$total =0 ;
		$temp_array = array();
		$temp_array['BackLog']=0;
		$temp_array['열기']=0;
		$temp_array['in progess']=0;
		$temp_array['comfirm']=0;
		$temp_array['close']=0;
		$temp_array['issue']=0;
		$sql	 = "
		SELECT 
			 jm.jira_status , COUNT(*) AS cnt 
		FROM jira_main AS jm
			WHERE jm.project =' ".trim($project)." '
		GROUP BY jm.jira_status ";

		$res	=  mysqli_query($real_sock,$sql) ;
		while($info	 = mysqli_fetch_array($res)){
			$total +=$info['cnt'];
			$temp_array[trim($info['jira_status'])] = $info['cnt'];

		}
		$temp = floor($temp_array['close']/$total*1000)/10;
		echo $temp."%";
?>

					
					</div>




    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
       google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable([
        ['Genre', 'BackLog', '열기', 'in progess', 'comfirm','close', 'issue', { role: 'annotation' } ],
        ['<?php echo $project ?> 진행 상황', <?php
		
			echo $temp_array['BackLog'].",";
			echo $temp_array['열기'].",";
			echo $temp_array['in progess'].",";
			echo $temp_array['comfirm'].",";
			echo $temp_array['close'].",";
			echo $temp_array['issue'];
		
			?>, '']
      ]);
	  var view = new google.visualization.DataView(data);
      view.setColumns([0,1,2,3,4,5,6
		,
                       { calc: "stringify",
                         sourceColumn: 6,
						 
                         type: "string",
                         role: "annotation" }
                       ]);

      var options = {
        
        legend: { position: 'top', maxLines: 6 },
        bar: { groupWidth: '50%' },
        isStacked: true
      };
	  var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
      chart.draw(view, options);
      }
    </script>
  
  <div id="barchart_values" style="width: 100%; height: 20%;"></div>

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
							$name = "<a href='/BOIN_PLANNING/01.jira/project_main.php?project=".$info['project']."'>".$info['project']."</a>" ;	hd_tbody_td($num,$name);$num+=1;
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



		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






