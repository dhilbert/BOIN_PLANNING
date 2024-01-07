<?php
include_once('lib/session.php');
include_once('lib/dbcon_BOIN_PLANNING.php');
include_once('contents_header.php');
include_once('contents_profile.php');
include_once('contents_sidebar.php');






?>





	
	<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">	
	
		<div class="row">
			<ol class="breadcrumb">
				<li><a href="/BOIN_PLANNING/home.php"><svg class="glyph stroked home"><use xlink:href="#stroked-home"></use></svg></a> home				
				</li>

			</ol>
		</div>

	<div class="row">
			<div class="col-md-6">
				<div class="panel panel-primary">
					<div class="panel-heading">슬랙 테스트</div>
					<div class="panel-body">
					<div class="form-group">


					<form name="frm" role="form" method="get" action="slack_proc.php">
									<label>사용자 이름</label>
									<input class="form-control" placeholder="이름넣기" name='username'>
								</div>
								<div class="form-group">
									<label>내용</label>
									<textarea class="form-control" rows="4" name='maintext'>동해 물과 백두산이 마르고 닮도록, 
					하느님이보우아사


									</textarea>
								</div>
								<button type="submit" class="btn btn-primary">slack 보내기</button>
								
							</div>
						</form>
<?php 



	


?>



					</div>
				</div>
			</div>
			
		</div><!--/.row-->
		





								
	</div>	<!--/.main-->
<?php include_once('contents_footer.php');?>