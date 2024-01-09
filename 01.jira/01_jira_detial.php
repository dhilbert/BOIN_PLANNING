<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');




$jm_idx = isset($_GET['jm_idx']) ? $_GET['jm_idx'] : 3;

$sql	 = "select * from jira_main where jm_idx =".$jm_idx;
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);

function hd_jhh($value1,$value2){
	echo $value1." : ".$value2;
	echo "<br>";

}

?>			

			<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">			
					<?php
					$array = array(
						array('#','상세')
					);
					breadcrumb($array);
					?>
		
					<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
내용					
					</div>

					<div class="panel-body">
					<?php 

$temp = array(
	"키","라벨","우선순위","담당자","상태","만든사람","보고자","프로젝트","잔여시간",
	"지금까지 진행한 시간","작업이름","작업내용","기한","시작일","마지막확인한일자"

);

$num = 0;
								$name = $info['jira_key'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['labels'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['priority'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['assignee'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['jira_status'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['creator'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['reporter'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['project'] ;	hd_jhh($temp[$num],$name);$num+=1;
								
								$name = $info['remainingEstimateSeconds'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['timeSpentSeconds'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['summay'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['jira_description'] ;	hd_jhh($temp[$num],$name);$num+=1;

								$name = $info['duedate'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['ustomfield_10015'] ;	hd_jhh($temp[$num],$name);$num+=1;
								$name = $info['updated'] ;	hd_jhh($temp[$num],$name);$num+=1;










					?>

					</div>
				</div>
		 
				<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
댓글내용					</div>

					<div class="panel-body">
  
	<?php 
	
	
		$comment_sql	 = "select * from jira_comment where jira_key ='".trim($info['jira_key'])."'";
		$comment_res	=  mysqli_query($real_sock,$comment_sql) or die(mysqli_error($real_sock));
		while($comment_info	 = mysqli_fetch_array($comment_res)){
			echo "<p>---<p>";
			echo $comment_info['author']."(".$comment_info['jira_created'].")";
			echo "<br>";
			echo $comment_info['comment'];
			


		};
	
	
	
	?>

		 
			</div>
				</div>
			</div>


			</div>		<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
작업 시간					</div>

					<div class="panel-body">
  
	<?php 
	
	
		$comment_sql	 = "select * from jira_worklog where jira_key ='".trim($info['jira_key'])."'";
		$comment_res	=  mysqli_query($real_sock,$comment_sql) or die(mysqli_error($real_sock));
		while($comment_info	 = mysqli_fetch_array($comment_res)){
			echo "<p>---<p>";
			echo $comment_info['author']."(".$comment_info['jira_started'].")";
			echo "<br>";
			echo $comment_info['comment'].":".$comment_info['timeSpentSeconds'];
			


		};
	
	
	
	?>

		 
			</div>
				</div>
			</div>


			</div>

		 

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






