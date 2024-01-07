<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
//include_once('../contents_sidebar.php');





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
						지라 동기화
					</div>
					<div class="panel-body">
						<?php
							echo "총 동기화 할 지라 갯수 : ".$ress['total']."<p>";






function cute_jy_string($value){
	$value = str_replace("'", "\'",$value);
	$value = str_replace('"', '\"',$value);
	$value = " ".$value." ";
	/*
	$value = str_replace('"', '\"',$value);
	$value = str_replace('\\DiskStation', 'DiskStation',$value);
	$value = str_replace('\\\\DiskStation', 'DiskStation',$value);
	*/
	return $value;
}
							





function cute_jy_jira_sql($table_text,$col_array){

	
	$col_test = "(";
	$value_text = "(";
	$UPDATE_text = " ";
	
	for($i = 0; $i < count($col_array) ;$i++  ){
		$col_test   = $col_test.$col_array[$i][0].",";
		$value_text = $value_text."'".$col_array[$i][1]."',";
		$UPDATE_text = $UPDATE_text.$col_array[$i][0]." = '".$col_array[$i][1]."',";


	}
	$col_test   =substr($col_test, 0, -1);
	$value_text   =substr($value_text, 0, -1);
	$UPDATE_text   =substr($UPDATE_text, 0, -1);
	
	
	$col_test   =$col_test.")";
	$value_text   =$value_text.")";
	

	$want_text = " INSERT INTO ".$table_text." ".$col_test." VALUES  ".$value_text."  ON DUPLICATE KEY UPDATE ".$UPDATE_text;

	return $want_text;

}


if(!empty($sub_ress['fields']['timetracking']['originalEstimate'])){
	array_push($col_array,array('timetracking',$sub_ress['fields']['timetracking']['originalEstimate']));


}




$table_text = 'jirasync_main_info';
$fixversions_array = array();
for($i = 0 ; $i <count($ress['issues']); $i++){


	$temps_list = $ress['issues'][$i];	
	
	$url = "https://mz-dev.atlassian.net/rest/api/latest/issue/".$temps_list['key']."?fields=key,id,fixVersions,summary,status,priority,reporter,updated,created,lastViewed,labels,components,assignee,timetracking,description,customfield_12261,environment,customfield_12262,customfield_12265,customfield_12270,customfield_12271,customfield_12267,customfield_12266,customfield_10600,customfield_12268,customfield_12269,statuscategorychangedate";


	//?fields=id,key,summary
	$sub_ress=sub_cute_jy_curl($username,$password,$url);

	
	
	$col_array = array(
		array('jmi_inx',$sub_ress['id']),
		array('jmi_key',$sub_ress['key']),
		array('jmi_summary',str_replace("'", "\'",$sub_ress['fields']['summary'])),
		array('status',$sub_ress['fields']['status']['name']),
		array('priority',$sub_ress['fields']['priority']['name']),		
		array('jmi_reporter_id',$sub_ress['fields']['reporter']['accountId']),
		array('jmi_reporter_name',$sub_ress['fields']['reporter']['displayName']),		
		array('updated',$sub_ress['fields']['updated']),
		array('created',$sub_ress['fields']['created']),

		
		array('lastViewed',explode(".",$sub_ress['fields']['lastViewed'])[0])
		);

		$text = 'jmi_labels';	
		$value = isset($sub_ress['fields']['labels'][0]) ? $sub_ress['fields']['labels'][0] : "라벨등록안함.";
		$value =cute_jy_string($value);
		if($value!=Null){array_push($col_array,array($text,$value));	}

		$text = 'components';	
		$value = isset($sub_ress['fields']['components'][0]['name']) ? $sub_ress['fields']['components'][0]['name'] : "연결된 없체없음.";
		$value =cute_jy_string($value);
		if($value!=Null){array_push($col_array,array($text,$value));	}


		
		$text = 'jmi_assignee_id';	
		$value = isset($sub_ress['fields']['assignee']['accountId']) ? $sub_ress['fields']['assignee']['accountId'] : "담당자 지정 안함.";
		$value =cute_jy_string($value);
		if($value!=Null){array_push($col_array,array($text,$value));	}

		$text = 'jmi_assignee_name';	
		$value = isset($sub_ress['fields']['assignee']['displayName']) ? $sub_ress['fields']['assignee']['displayName'] : "담당자 지정 안함.";
		$value =cute_jy_string($value);
		if($value!=Null){array_push($col_array,array($text,$value));	}
	

		$text = 'originalEstimate';	
		$value = isset($sub_ress['fields']['timetracking']['originalEstimate']) ? $sub_ress['fields']['timetracking']['originalEstimate'] : null;
		$value =cute_jy_string($value);	
		if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'originalEstimateSeconds';	
		$value = isset($sub_ress['fields']['timetracking']['originalEstimateSeconds']) ? $sub_ress['fields']['timetracking']['originalEstimateSeconds'] : null;
		$value =cute_jy_string($value);
		if($value!=Null){array_push($col_array,array($text,$value));	}
		
	    $text = 'description';	
	    $value = isset($sub_ress['fields']['description']) ? $sub_ress['fields']['description'] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_12261';	
	    $value = isset($sub_ress['fields']['customfield_12261']) ? $sub_ress['fields']['customfield_12261'] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'environment';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_12262';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_12265';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_12270';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_12271';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_12266';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_12267';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		$text = 'customfield_10600';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		$text = 'customfield_12268';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}
		
		
		$text = 'customfield_12269';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}

		
		$text = 'statuscategorychangedate';	
	    $value = isset($sub_ress['fields'][$text ]) ? $sub_ress['fields'][$text ] : null;
		$value =cute_jy_string($value);
	    if($value!=Null){array_push($col_array,array($text,$value));	}

		$temp_list = array(array($sub_ress['id'],$sub_ress['key']),	$sub_ress['fields']['fixVersions']);
		array_push($fixversions_array,$temp_list);
		$del_jirasync_fixversions_sql ="delete from jirasync_fixversions where jmi_inx =".$sub_ress['id']; //지우기
		$del_jirasync_fixversions_res	=  mysqli_query($real_sock,$del_jirasync_fixversions_sql) or die(mysqli_error($real_sock));

		$del_jirasync_work_sql ="delete from jirasync_work where jmi_inx =".$sub_ress['id']; //지우기
		$del_jirasync_work_res	=  mysqli_query($real_sock,$del_jirasync_work_sql) or die(mysqli_error($real_sock));


		$want_sql = cute_jy_jira_sql($table_text,$col_array);
	
		$sub_res	=  mysqli_query($real_sock,$want_sql) or die(mysqli_error($real_sock));
	
		$work_url = "https://mz-dev.atlassian.net/rest/api/2/issue/".$temps_list['key']."/worklog/?maxResults=10000";
		
		$work_ress=sub_cute_jy_curl($username,$password,$work_url);
		
		
		$work_sql = "INSERT INTO jirasync_work(jmi_inx,jmi_key,jmi_work_name,jmi_work_id,started,created,updated,timeSpent,timeSpentSeconds,comment)	VALUES";


		$tmp_list = $work_ress['worklogs'];

		for($work_i = 0 ;	$work_i <count($tmp_list);	$work_i ++	){
			$comment = isset($tmp_list[$work_i]['comment']) ? $tmp_list[$work_i]['comment']: "코멘트 입력 안함.";			
			$comment =cute_jy_string($comment);


			$temp_sql ="('".$sub_ress['id']."','".$sub_ress['key'].
			"','".$tmp_list[$work_i]['author']['displayName'].
			"','".$tmp_list[$work_i]['author']['accountId'].
			"','".$tmp_list[$work_i]['started'].
			"','".$tmp_list[$work_i]['created'].
			"','".$tmp_list[$work_i]['updated'].
			
			"','".$tmp_list[$work_i]['timeSpent'].
			"','".$tmp_list[$work_i]['timeSpentSeconds'].
			"','".$comment."'),";
			$work_sql = $work_sql.$temp_sql ;
			
			$temp = explode("[",$comment);
		}
		if(count($tmp_list)>0){
			$work_sql =substr($work_sql, 0, -1);
			$work_res	=  mysqli_query($real_sock,$work_sql) or die(mysqli_error($real_sock));
		}
	
	

}


	for($i = 0 ; $i < count($fixversions_array)  ;$i++  ){

		$temp_list_0 = $fixversions_array[$i][0];
		$temp_list_1 = $fixversions_array[$i][1];

		
		for($j = 0 ; $j <count($temp_list_1);$j++){
			$sub_fixversions_sql = "
				
				INSERT INTO jirasync_fixversions(jmi_inx,jmi_key,id,description)
				VALUES ('".$temp_list_0[0]."','".$temp_list_0[1]."','".$temp_list_1[$j]['id']."','".cute_jy_string($temp_list_1[$j]['description'])."');"	;	
			
			$sub_fixversions_res	=  mysqli_query($real_sock,$sub_fixversions_sql) or die(mysqli_error($real_sock));

		}
	}
		
	$sql	= "
	insert jirasync_update set 

		admin_idx = '".$admin_idx."',
		jirasync_update_datetime = now(),
		jirasync_update_date = now()

		
	";
	$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));

	


	$jira_update_sql	= "
	update jirasync_work set comment_kind = SUBSTRING_INDEX(SUBSTRING_INDEX(comment, '[', -1), ']', 1) where comment_kind is null AND LEFT(COMMENT,2)=' [';";
	
	$jira_update_res	=  mysqli_query($real_sock,$jira_update_sql) or die(mysqli_error($real_sock));
	
	$jira_update_sql	= "
	UPDATE jirasync_main_info SET 
	customfield_12268 = SUBSTRING_INDEX(created , 'T', 1)
		WHERE customfield_12268 ='';	";
	$jira_update_res	=  mysqli_query($real_sock,$jira_update_sql) or die(mysqli_error($real_sock));


	
	$jira_update_sql	= '
	UPDATE jirasync_main_info SET 
	customfield_12269 = SUBSTRING_INDEX(statuscategorychangedate , "T", 1)
WHERE STATUS = "닫힘" AND customfield_12269="";';
	$jira_update_res	=  mysqli_query($real_sock,$jira_update_sql) or die(mysqli_error($real_sock));
	







	$sql	 = "select * from jirasync_work where check_date is null 	";
	$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
	while($info	 = mysqli_fetch_array($res)){


		$temp = explode("T",$info['started']);

		$jira_update_sql	= "
		UPDATE 		jirasync_work set 
		check_date = '".$temp[0]."'
		
		WHERE jw_dix = ".$info['jw_dix'];
		$jira_update_res	=  mysqli_query($real_sock,$jira_update_sql) or die(mysqli_error($real_sock));
		



	};
	










	










	echo "<script>
	alert('업데이트 완료.');
	parent.location.replace('/BOIN_PLANNING/05_jira_update/jira_update_main.php');
	</script> ";


	?>


					</div>
				</div>
			</div>



		 





			
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>
<!--
https://mz-dev.atlassian.net/rest/api/latest/search?jql=updated%3E=2022-01-01&&fields=key&maxResults=10000
https://mz-dev.atlassian.net/rest/api/latest/issue/260823

부모 / 자식
작업 시간

-->