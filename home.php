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
					<div class="panel-heading">회원 가입 승인</div>
					<div class="panel-body">
<?php 



	

?>
<!--
								<button type="submit" class="btn btn-primary">google Drive api test(공사중)</button>
-->
<p>
										  
<table  border = 1 width='100%'>
	<thead>
		<tr>
			<th data-field="s_99" data-sortable="true" >No </th>
			
			<th data-field="s_0" data-sortable="true" >아이디</th>
			<th data-field="s_1" data-sortable="true" > 이름</th>
			<th data-field="s_2" data-sortable="true" > 회사</th>
			<th data-field="s_3" data-sortable="true" > 부서</th>
			<th data-field="s_4" data-sortable="true" > 관리자레벨</th>
			<th data-field="s_5" data-sortable="true" >요청시간</th>
			<th data-field="s_6" data-sortable="true" > 승인</th>
			
		</tr>
		</tr>
	</thead>
	<tbody>
		
<?php

	$sql = "select a.admin_id,a.admin_name,a.lasted_login,b.company_name,c.division_name,a.admin_idx
				
	from admin_member as a 
		join admin_company_info as b
	on a.company_idx = b.company_idx
		join admin_division_info as c
	on a.division_idx = c.division_idx		
	
	where a.admin_state = 0
	
	
	;";
	$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
	$count_n = 0;
	while($info	 = mysqli_fetch_array($res)){
		$count_n += 1;
		echo "
			<tr>
				
				<td data-field='s_99' data-sortable='true'>".$count_n."</td>
				<td data-field='s_0' data-sortable='true'>".$info['admin_id']."</td>
				<td data-field='s_1' data-sortable='true'>".$info['admin_name']."</td>
				<td data-field='s_2' data-sortable='true'>".$info['company_name']."</td>
				<td data-field='s_3' data-sortable='true'>".$info['division_name']."</td>
				<td data-field='s_4' data-sortable='true'>
				<form name='frm'  method='get' action='agree_proc.php'>
				<select class='form-control' name = 'admin_lv'>
					<option value = '1'>일반</option>
					<option value = '25'>팀장</option>
					<option value = '50'>부서장</option>					
					
				</select>
				
				</td>
				<td data-field='s_5' data-sortable='true'>".$info['lasted_login']."</td>
				
				<td data-field='s_6' data-sortable='true'>
				<input type='hidden' name = 'admin_idx' value='".$info['admin_idx']."'>
				<input  type='submit' class='btn btn-success login-btn' type='submit' value='승인'>
				
				</form></td>
				
				
			</tr>								
		";

	};











/*
		$count_n = 0;	
		$sql	 = "
					select b.admin_name, a.adminmember_idx, a.updateDate, a.DEAL_YMD, a.serviceKey
					from admin_apidata as a
						Join admin_member as b 
					on b.idx = a.adminmember_idx
					ORDER BY a.idx desc	
				;";
		$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
		
		*/
?>


	</tbody>
</table>





					</div>
				</div>
			</div>
			
		</div><!--/.row-->
		





								
	</div>	<!--/.main-->
<?php include_once('contents_footer.php');?>