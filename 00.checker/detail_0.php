<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');




$idx = isset($_GET['idx']) ? $_GET['idx'] : 3;
$url ='uptofifty115.json';

$json_string = file_get_contents($url);
$object = json_decode($json_string, true);


$info =	$object[$idx] ;

function hd_temp_html($val1,$val2)
{
?>


			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading"><?php echo $val1?></div>
					<div class="panel-body">
					<div class="cdml_question" style="width :500px"><div class="question_box" style="width :500px">
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
					hd_temp_html("body_html",$info['body_html']);
					hd_temp_html("list_html",$info['list_html']);
					hd_temp_html("answer_html",$info['answer_html']);
					hd_temp_html("explanation_html",$info['explanation_html']);

					?>
			
		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






