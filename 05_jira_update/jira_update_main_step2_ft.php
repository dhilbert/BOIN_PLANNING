<?php


		$temps_list = $ress['issues'][$i];



		$del_sql	 = "DELETE FROM jira_work_log where MZNO_key = '".$temps_list['key']."' ;";
		$del_res	=  mysqli_query($real_sock,$del_sql) or die(mysqli_error($real_sock));		
		
		
		
		$jira_ini_sql = "INSERT INTO jira_work_log (MZNO_key,parent_MZNO_key,MZNO_priority,MZNO_labels,MZNO_components,MZNO_reporter,work_comment,work_timeSpentSeconds,work_author,work_updated,MZNO_created,MZ_summary,due_datetime)
		VALUES";
		
	
	
					$sub_url = "https://mz-dev.atlassian.net/rest/api/latest/issue/".$temps_list['key']."?fields=key,priority,labels,components,reporter,worklog,parent,summary,created,customfield_10600";
					

		//echo "<a href = 'https://mz-dev.atlassian.net/browse/".$temps_list['key']."'>".$temps_list['key']."</a><br>	";


		

		$sub_curl = curl_init();
		curl_setopt($sub_curl, CURLOPT_USERPWD, "$username:$password");
		curl_setopt($sub_curl, CURLOPT_URL, $sub_url);
		curl_setopt($sub_curl, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($sub_curl, CURLOPT_FOLLOWLOCATION, 1);
		curl_setopt($sub_curl, CURLOPT_SSL_VERIFYPEER, 0);
		curl_setopt($sub_curl, CURLOPT_SSL_VERIFYHOST, 0);
		curl_setopt($sub_curl,CURLOPT_RETURNTRANSFER,1);
		
		//$result = curl_exec($curl);
		$sub_res=json_decode(curl_exec($sub_curl),true);
		$MZNO_key = $sub_res['key'];
		$MZNO_priority = $sub_res['fields']['priority']['name'];
		$MZNO_labels= isset($sub_res['fields']['labels'][0]) ? $sub_res['fields']['labels'][0] : '라벨없음.';
		 
	
		
		;
		

		$MZNO_reporter = $sub_res['fields']['reporter']['displayName'];
	
		$MZNO_components = isset( $sub_res['fields']['components'][0]['name']) ? $sub_res['fields']['components'][0]['name'] : '네이쳐리퍼블릭';
		$MZNO_worklog_total = $sub_res['fields']['worklog']['total'];
		
		

		
		if($MZNO_worklog_total>0){
		if($MZNO_worklog_total<20){

			for($work_i = 0 ;$work_i<$MZNO_worklog_total;$work_i++){
				$temps =$sub_res['fields']['worklog']['worklogs'][$work_i];
				$work_comment = isset($temps['comment']) ? $temps['comment'] : '댓글없음';
				$work_comment = str_replace('\'' , '\"', $work_comment);
				$work_comment = $work_comment." ";
				
				if(isset($sub_res['fields']['parent']['key'])){
					$parent_MZNO_key = $sub_res['fields']['parent']['key'];
				}
				else
					$parent_MZNO_key = '';{
				}
				
				
				$work_timeSpentSeconds = $temps['timeSpentSeconds'];
				$work_author = $temps['author']['displayName'];
				
				$work_updated = explode("T",$temps['started']);
				$work_updateds =$work_updated[0];
				
				



				$MZ_summary =$temps =$sub_res['fields']['summary'];
				$MZNO_created=$temps =$sub_res['fields']['created'];
				$due_datetime=$temps =$sub_res['fields']['customfield_10600'];


				$jira_ini_sql =$jira_ini_sql."	('".$MZNO_key."','".$parent_MZNO_key."','".$MZNO_priority."','".$MZNO_labels."','".$MZNO_components."','".$MZNO_reporter."',
												
				'".$work_comment."','".$work_timeSpentSeconds."','".$work_author."','".$work_updateds."','".$MZNO_created."','".$MZ_summary."','".$due_datetime."'),";
			}

		}
		else{
			
			$work_url = "https://mz-dev.atlassian.net/rest/api/latest/issue/".$temps_list['key']."/worklog?maxResults=2000";
			
			$work_curl = curl_init();
			curl_setopt($work_curl, CURLOPT_USERPWD, "$username:$password");
			curl_setopt($work_curl, CURLOPT_URL, $work_url);
			curl_setopt($work_curl, CURLOPT_RETURNTRANSFER, 1);
			curl_setopt($work_curl, CURLOPT_FOLLOWLOCATION, 1);
			curl_setopt($work_curl, CURLOPT_SSL_VERIFYPEER, 0);
			curl_setopt($work_curl, CURLOPT_SSL_VERIFYHOST, 0);
			curl_setopt($work_curl,CURLOPT_RETURNTRANSFER,1);

			//$result = curl_exec($curl);
			$work_res=json_decode(curl_exec($work_curl),true);
			for($work_i = 0 ;$work_i<$work_res['total'];$work_i++){
				$temps = $work_res['worklogs'][$work_i];
				$work_comment = isset($temps['comment']) ? $temps['comment'] : '댓글없음';
				$work_comment = str_replace('\'' , '\"', $work_comment);
				$work_timeSpentSeconds = $temps['timeSpentSeconds'];
				$work_author = $temps['author']['displayName'];
				

				
				$MZ_summary =$temps =$sub_res['fields']['summary'];
				$MZNO_created=$temps =$sub_res['fields']['created'];


				if(isset($sub_res['fields']['parent']['key'])){
					$parent_MZNO_key = $sub_res['fields']['parent']['key'];
				}
				else
					$parent_MZNO_key = '';{
				}
				$work_updated = explode("T",$temps['started']);
				$work_updateds =$work_updated[0];
				$due_datetime=$temps =$sub_res['fields']['customfield_10600'];
			
				$jira_ini_sql =$jira_ini_sql."	('".$MZNO_key."','".$parent_MZNO_key."','".$MZNO_priority."','".$MZNO_labels."','".$MZNO_components."','".$MZNO_reporter."',
												'".$work_comment."','".$work_timeSpentSeconds."','".$work_author."','".$work_updateds."','".$MZNO_created."','".$MZ_summary."','".$due_datetime."'),";
				
			}

		}
		$jira_ini_sql = substr($jira_ini_sql , 0, -1);
		$jira_ini_res	=  mysqli_query($real_sock,$jira_ini_sql) or die(mysqli_error($real_sock));

	}


?>