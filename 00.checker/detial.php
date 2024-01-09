<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');




$QSNO = isset($_GET['QSNO']) ? $_GET['QSNO'] : 3;

$sql	 = "select * from kerisaig.questions where QSNO =".$QSNO;
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);





function hd_temp_html($val1,$val2)
{
?>


			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading"><?php echo $val1?></div>
					<div class="panel-body">
					<div class="cdml_question"><div class="question_box">
						<?php 
							echo $val2;
						?>
					</div></div>
					</div>
					</div>
					</div>					
			

<?php
}

?>			

			<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">			
					<?php
					$array = array(
						array('#','상세')
					);
					?>
					<div class="row">
						<?php
					breadcrumb($array);
					hd_temp_html("ANSWER_HTML",$info['ANSWER_HTML']);
					hd_temp_html("BODY_EXT",$info['BODY_EXT']);
					hd_temp_html("BODY_HTML",$info['BODY_HTML']);
					hd_temp_html("LIST_HTML",$info['LIST_HTML']);

					?>
			


		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






