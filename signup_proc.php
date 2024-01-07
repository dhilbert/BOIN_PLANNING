<?php
	
	include_once('lib/dbcon_BOIN_PLANNING.php');
	function hd_check_val($check_val,$text){
		if($check_val==Null) {
						echo "<script>
							alert('".$text."');
							parent.location.replace('/BOIN_PLANNING/');
						</script> ";
		}
	}
	

	$admin_id		= isset($_GET['admin_id'])		? $_GET['admin_id'] : 3;
	$admin_name 	= isset($_GET['admin_name'])	? $_GET['admin_name'] : 3;
	$admin_pw		= isset($_GET['admin_pw'])		? $_GET['admin_pw'] : 3;
	$admin_pw_re	= isset($_GET['admin_pw_re'])	? $_GET['admin_pw_re'] : 3;
	$company_idx 	= isset($_GET['company_idx'])	? $_GET['company_idx'] : 3;
	$division_idx	= isset($_GET['division_idx'])	? $_GET['division_idx'] : 3;

	
	if( strlen($admin_id)>24) {
		echo "<script>
				alert('아이디는 24자리 이하로 설정해야 함. ');
				parent.location.replace('/BOIN_PLANNING/');
			</script> ";
	}
	
	if( strlen($admin_id)<6) {
		echo "<script>
				alert('아이디는 6자리 이상으로 설정해야 함. ');
				parent.location.replace('/BOIN_PLANNING/');
			</script> ";
	}
	if( strlen($admin_pw)<8) {
		echo "<script>
				alert('패스워드는 8자리 이상으로 설정해야 함. ');
				parent.location.replace('/BOIN_PLANNING/');
			</script> ";
	}
	
	if( strlen($admin_pw)>16) {
		echo "<script>
				alert('패스워드는 16자리 이상으로 설정해야 함. ');
				parent.location.replace('/BOIN_PLANNING/');
			</script> ";
	}





	
	$text = "아이디를 입력하지 않았습니다.";
	hd_check_val($admin_id,$text);
	$text = "이름을 입력하지 않았습니다.";
	hd_check_val($admin_name,$text);
	if($admin_pw!=$admin_pw_re) {
		echo "<script>
				alert('패스워드가 일치 하지 않았습니다.');
				parent.location.replace('/BOIN_PLANNING/');
			</script> ";
	}


	$sql	 = "select * from admin_member where admin_id ='".$admin_id."';";
	$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
	$info	 = mysqli_fetch_array($res);
	if($info!=Null) {
		echo "<script>
				alert('이미 등록된 아이디 입니다. ');
				parent.location.replace('/BOIN_PLANNING/');
			</script> ";
	}
	
	$sql	= "
			insert admin_member set 
			admin_id		= '".$admin_id."',
			admin_name		= '".$admin_name."',
			admin_pw		= '".md5($admin_pw)."',
			lasted_login	= now(),
			division_idx	= '".$division_idx."',	
			company_idx	= '".$company_idx."',	
					
			admin_state		=	0
	
	
	
				";
	$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
	
	
	echo "<script>
		alert('회원 가입이 완료 되었습니다. 관리자 승인해야 완료 됩니다. ');
		parent.location.replace('/BOIN_PLANNING/');
	</script> ";
	
	

 

 




	/*
	$company_info_sql	 = "select * from division_info;";
	$company_info_res	=  mysqli_query($real_sock,$company_info_sql) or die(mysqli_error($real_sock));
	while($company_info_info	 = mysqli_fetch_array($company_info_res)){
			echo "<option value = '".$company_info_info['division_idx']."'>".$company_info_info['division_name']."</option>";									
	};

*/

	/*
	$now_time =  date("Y-m-d H:i:s");



	$sql	 = "select * from admin_member where admin_id ='".$admin_id."';";
	$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
	$info	 = mysqli_fetch_array($res);
	if($info==Null) {
		echo "<script>
				alert('아이디가 존재 하지 않습니다.');
				parent.location.replace('/BOIN_PLANNING/');
			</script> ";
	}else {



		if($info['admin_pw']==MD5($admin_pw)){
				


				$_SESSION['admin_idx']	 = $info['admin_idx'];
				$_SESSION['admin_id']	 = $info['admin_id'];
				$_SESSION['admin_name']  = $info['admin_name'];
				$_SESSION['admin_lv']	 = $info['admin_lv'];
				$_SESSION['division_idx']	 = $info['division_idx'];
				$_SESSION['jira_id']	 = $info['jira_id'];
				

				$sql	 = "update admin_member set 
							lasted_login = '".$now_time."'
				
				where admin_id ='".$admin_id."';";
				$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));

				
				
				echo "<script>
					alert('환영합니다.');
					parent.location.replace('/BOIN_PLANNING/home.php');
				</script> ";



		}else {
		
				echo "<script>
				alert('비밀번호를 확인하세요. ');
				parent.location.replace('/BOIN_PLANNING/');
				</script> ";
			
		}

	}






	/*
	if($실투자금 == 0 or null){
	}






	$emp_id			= $_GET[emp_id];
	$emp_password	= $_GET[emp_password];


	/*
	$_SESSION['emp_num'] = $rs['emp_num'];
	$_SESSION['company_num'] = $rs['company_num'];
	$_SESSION['emp_id'] = $rs['emp_id'];
	$_SESSION['gr_num']= $rs['gr_num'];
	$_SESSION['emp_name']= $rs['emp_name'];




	$_SESSION['emp_num'] = 1111;
	$_SESSION['company_num'] = 1111;
	$_SESSION['emp_id'] = 1111;
	$_SESSION['gr_num']= 1111;
	$_SESSION['emp_name']= 1111;


			echo "<script>
			alert('환영합니다.');
			parent.location.replace('/TW_MOMO/home.php');
			</script> ";

















	$order_paper_sql = "select * from com_tkop where com_id ='$com_id' ";
	$res = mysql_query($order_paper_sql, $cset_sock);
	$rs = mysql_fetch_array($res);


	if($rs==Null) {
			echo "<script>
			alert('그럼 아이디 없어');
			parent.location.replace('/PIRATES/');
			</script> ";
	} else {
		if($rs[com_pw]==MD5($com_pw)){

			$com_name = $rs['com_name'];

			$_SESSION['session_com_id'] = $com_id;
			$_SESSION['session_com_level'] = $rs['com_level'];

			$pirates_log_check = 0;
			$pirates_log_sql = "select * from pirates_log where com_id ='$com_id' ";
			$pirates_log_res = mysql_query($pirates_log_sql, $cset_sock);
			while($pirates_log_rs = mysql_fetch_array($pirates_log_res)){
				$pirates_log_check+=1;
			}

			echo "<script>
				alert('".$com_name."님의 ".$pirates_log_check."번째 방문을 환영합니다.1000번째 방문에는 특별한 선물이 있습니다. ');
				parent.location.replace('/PIRATES/main.php');
				</script> ";

			$dates = date("Y-m-d h:i:s");
			$ip = $_SERVER["REMOTE_ADDR"];
			$order_paper_sql = "insert pirates_log set 
				com_id ='".$com_id."',
				log_ip ='".$ip."',
				log_dates ='".$dates."',
				log_type  = 0;";
			$res = mysql_query($order_paper_sql, $cset_sock);

		}	else {
				echo "<script>
				alert('비밀번호 확인해');
				parent.location.replace('/PIRATES/');
				</script> ";
		}
	}

	*/
?>	