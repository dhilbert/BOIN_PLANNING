<?php
//include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

//include_once('../contents_header.php');
//include_once('../contents_profile.php');
//include_once('../contents_sidebar.php');



function cute_hh_string($value){
	$value = str_replace("'", "\'",$value);
	$value = str_replace('"', '\"',$value);
	$value = " ".$value." ";
	
	return $value;
}
				



$url = 'https://boinplanning.atlassian.net/rest/api/latest/search';
$url = 'https://boinplanning.atlassian.net/rest/api/latest/issue/AIG-3';

$ress = cute_hh_curl($username,$password,$url);
/*
$key = $ress['key'];
$labels = $ress['fields']['labels'][0]; ##라벨
$priority = $ress['fields']['priority']['name']; ##우선순위
$assignee = $ress['fields']['assignee']['displayName']; ## 담당자
$status = $ress['fields']['status']['name']; ##  상태
$creator = $ress['fields']['creator']['displayName']; ##  만든사람
$reporter = $ress['fields']['reporter']['displayName']; ##  보고자
$project =$ress['fields']['project']['name'] ;## 프로젝트
$remainingEstimateSeconds =$ress['fields']['timetracking']['remainingEstimateSeconds'] ;## 잔여시간
$timeSpentSeconds =$ress['fields']['timetracking']['timeSpentSeconds'] ;## 지금까지 진행한 시간
$summay =$ress['fields']['summary'];## 작업 이름
$description=$ress['fields']['description'];## 작업 내용


$duedate=$ress['fields']['duedate'];## 기한
$customfield_10015=$ress['fields']['customfield_10015'];## 시작일
$updated=$ress['fields']['updated'];## 마지막 확인일자

*/
$project =$ress['fields']['project']['name'] ;## 프로젝트
$key = $ress['key'];

$Main_sql	 = "insert jira_main set 
					jira_key = '".cute_hh_string($ress['key'])."',
					labels = '".cute_hh_string($ress['fields']['labels'][0])."',
					priority = '".cute_hh_string($ress['fields']['priority']['name'])."',
					assignee = '".cute_hh_string($ress['fields']['assignee']['displayName'])."',
					jira_status = '".cute_hh_string($ress['fields']['status']['name'])."',
					creator = '".cute_hh_string($ress['fields']['creator']['displayName'])."',
					reporter = '".cute_hh_string($ress['fields']['reporter']['displayName'])."',
					project ='".cute_hh_string($ress['fields']['project']['name'])."',
					remainingEstimateSeconds ='".cute_hh_string($ress['fields']['timetracking']['remainingEstimateSeconds'])."',
					timeSpentSeconds ='".cute_hh_string($ress['fields']['timetracking']['timeSpentSeconds'])."',
					summay ='".cute_hh_string($ress['fields']['summary'])."',
					jira_description='".cute_hh_string($ress['fields']['description'])."',
					duedate='".cute_hh_string($ress['fields']['duedate'])."',
					ustomfield_10015='".cute_hh_string($ress['fields']['customfield_10015'])."',
					updated='".cute_hh_string($ress['fields']['updated'])."';";

$Main_res	=  mysqli_query($real_sock,$Main_sql) or die(mysqli_error($real_sock));

##서브 테스트 작업해야함


$work_sql  = " INSERT INTO jira_worklog(author,comment,timeSpentSeconds,jira_started,project,jira_key)  VALUES ";
##워킹로그
$worklogs = $ress['fields']['worklog']['worklogs']; ##일한거
for($i = 0 ; $i <count($worklogs);$i++){
	$temp = $worklogs[$i];
	$author	=$temp['author']['displayName']; ##작성자
	$comment =$temp['comment'];##작업내용
	$timeSpentSeconds = $temp['timeSpentSeconds'];##작업시간
	$started = $temp['started'];##작용시간
	$work_sql  = $work_sql." ('".$author."','".$comment."','".$timeSpentSeconds."','".$started."','".$project."','".$key."'),";

}
$work_sql =substr($work_sql, 0, -1);
$work_res	=  mysqli_query($real_sock,$work_sql) or die(mysqli_error($real_sock));


$comment_sql  = " INSERT INTO jira_comment(author,comment,jira_created,project,jira_key)  VALUES ";
##댓글 내용
$comments = $ress['fields']['comment']['comments']; ##코멘트
for($i = 0 ; $i <count($comments);$i++){
	$temp = $comments[$i];
	$author	=$temp['author']['displayName'];
	$comment =$temp['body'];
	$created	= $temp['created'];
	##$project
	##$key 
	$comment_sql  = $comment_sql." ('".$author."','".$comment."','".$created."','".$project."','".$key."'),";

}


$comment_sql =substr($comment_sql, 0, -1);
$comment_res	=  mysqli_query($real_sock,$comment_sql) or die(mysqli_error($real_sock));


?>