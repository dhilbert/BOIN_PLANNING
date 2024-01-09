<?php
if(!$_SESSION['admin_lv']){
	echo "<script>alert('잘못된 접근입니다.');parent.location.replace('/BOIN_PLANNING/');</script> ";
}
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- 메타 데이터 -->
<title>MZ 12F</title>
<meta name="description" content="" />
<meta name="author" content="MZ 12F" />


<link href="/BOIN_PLANNING/css/bootstrap.min.css" rel="stylesheet">

<link href="/BOIN_PLANNING/css/datepicker3.css" rel="stylesheet">
<link href="/BOIN_PLANNING/css/cdml.css" rel="stylesheet">

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@mdi/font@latest/css/materialdesignicons.min.css">



<link rel="stylesheet" type="text/css" href="assets/cdml.css">

<script type="text/x-mathjax-config">

  MathJax.Hub.Config({
  
    tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
  
  });
  
  </script>
  
  <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
</style>



<link href="/BOIN_PLANNING/css/styles.css" rel="stylesheet">


<link href="/BOIN_PLANNING/css/bootstrap-table.css" rel="stylesheet">
<link href="/BOIN_PLANNING/css/bootstrap-table.css" rel="stylesheet">

<script src="/BOIN_PLANNING/js/lumino.glyphs.js"></script>

<script type="text/javascript" src="/BOIN_PLANNING/js/loader.js"></script>

</head>



<?php
function breadcrumb($array){
?>
		<div class="row">
			<ol class="breadcrumb">
				<li><a href="/JB_SYSTEM/home.php"><svg class="glyph stroked home"><use xlink:href="#stroked-home"></use></svg></a></li>
				

				<?php
				for($i = 0 ; $i < count($array)-1 ; $i++ ){
					echo "<li><a href='".$array[$i][0]."'>".$array[$i][1]."</a></li>";
				}
				echo "<li class='active'>".$array[count($array)-1][1]."</a></li>";
				?>
			</ol>
		</div><!--/.row-->
<?php
}

/*

$sql	 = "select * from key_jira  Limit 1	";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);


$username = $info['idss'];
$password =  $info['keyss'];

*/

?>