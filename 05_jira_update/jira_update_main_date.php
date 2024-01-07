<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');










$sql	 = "select * from jirasync_update order by jirasync_update_idx DESC Limit 1	";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);
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
					
					<form name="frm" role="form" method="get" action="jira_update_main_date_proc.php">
								
						       
					
					마지막 동기화 일자 :
					<input type="date" id="start"   value="<?php echo $info['jirasync_update_date']	?>" name='jirasync_update_date'   >
					<input  type='submit' class="btn btn-success login-btn" type="submit" value="수정">

							     </form>
					



					<p>	<br>	

					



					</div>
				</div>
			</div>



		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






