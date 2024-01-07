<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');










$sql	 = "select * from jirasync_update order by jirasync_update_idx DESC Limit 1	";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);


$url = "https://mz-dev.atlassian.net/rest/api/latest/search?jql=updated>=".$info['jirasync_update_date']."&fields=key&maxResults=10000";


$ress=cute_jy_curl($username,$password,$url);


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
					
						지라 동기화 내역
					
					</div>

					<div class="panel-body">
					<?php
						echo "총 동기화 할 지라 갯수 : ".$ress['total']."<p>";
					?>
					동기화 시작일자 :  	<?php echo $info['jirasync_update_date']	?><br>
					
					마지막 동기화 일자 : 	<?php echo $info['jirasync_update_datetime']	?>
					<p>	<br>	

					<a href="jira_update_main_step1.php" class="btn btn-success login-btn">지라 동기화</a>



					</div>
				</div>
			</div>



		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






