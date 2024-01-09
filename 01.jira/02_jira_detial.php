<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');




$author = isset($_GET['author']) ? $_GET['author'] : 3;

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



						$sql	 = "select * from jira_worklog where author ='".$author."'";
						$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
						while($info	 = mysqli_fetch_array($res)){
							echo "<p>";
							echo $info['comment']."/".$info['timeSpentSeconds']."/".$info['jira_started']."/".$info['project']."/".$info['jira_key'];
						};







					?>

					</div>
				</div>
		 
	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






