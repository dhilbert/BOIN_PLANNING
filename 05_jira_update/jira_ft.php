<?php






$ress = cute_es_curl($username,$password,$url);

$key = $ress['key']? $ress['key'] : null;
if(isset($ress['fields']['labels'][0])){
	$labels = $ress['fields']['labels'][0]; ##라벨 ㅁㅁㅁ
}else{
$labels ="라벨등록안함.";
}

$priority = $ress['fields']['priority']['name']?$ress['fields']['priority']['name']: "우선순위지정안함"; ##우선순위
if(isset($ress['fields']['assignee']['displayName'])){
	
	$assignee = $ress['fields']['assignee']['displayName']; ## 담당자 ㅁㅁㅁ
}
else{
	$assignee =  "담당자지정않함.";

}


$status = $ress['fields']['status']['name']; ##  상태
$creator = $ress['fields']['creator']['displayName']; ##  만든사람
$reporter = $ress['fields']['reporter']['displayName']; ##  보고자
$project =$ress['fields']['project']['name'] ;## 프로젝트

if(isset($ress['fields']['timetracking']['remainingEstimateSeconds'])){
	$remainingEstimateSeconds =$ress['fields']['timetracking']['remainingEstimateSeconds'];## 잔여시간 ㅁㅁㅁ
}
else{
	$remainingEstimateSeconds =0;

}

if(isset($ress['fields']['timetracking']['timeSpentSeconds'])){
	$timeSpentSeconds =$ress['fields']['timetracking']['timeSpentSeconds'];## 지금까지 진행한 시간 ㅁㅁㅁ
}
else{
	$timeSpentSeconds =0;

}

$summay =$ress['fields']['summary'];## 작업 이름
$description=$ress['fields']['description'];## 작업 내용


$duedate=$ress['fields']['duedate'];## 기한
$customfield_10015=$ress['fields']['customfield_10015'];## 시작일
$updated=$ress['fields']['updated'];## 마지막 확인일자


$project =$ress['fields']['project']['name'] ;## 프로젝트
$key = $ress['key'];

$Main_sql	 = "insert jira_main set 
					jira_key = '".cute_es_string($key)."',
					labels = '".cute_es_string($labels)."',
					priority = '".cute_es_string($priority)."',
					assignee = '".cute_es_string($assignee)."',
					jira_status = '".cute_es_string($status)."',
					creator = '".cute_es_string($creator)."',
					reporter = '".cute_es_string($reporter)."',
					project ='".cute_es_string($project)."',
					remainingEstimateSeconds ='".cute_es_string($remainingEstimateSeconds)."',
					timeSpentSeconds ='".cute_es_string($timeSpentSeconds)."',
					summay ='".cute_es_string($summay)."',
					jira_description='".cute_es_string($description)."',
					duedate='".cute_es_string($duedate)."',
					ustomfield_10015='".cute_es_string($customfield_10015)."',
					updated='".cute_es_string($updated)."';";

$Main_res	=  mysqli_query($real_sock,$Main_sql) or die(mysqli_error($real_sock));

##서브 테스트 작업해야함


$work_sql  = " INSERT INTO jira_worklog(author,comment,timeSpentSeconds,jira_started,project,jira_key)  VALUES ";
##워킹로그
$worklogs = $ress['fields']['worklog']['worklogs']; ##일한거

for($i = 0 ; $i <count($worklogs);$i++){
	$temp = $worklogs[$i];
	$author	=$temp['author']['displayName']; ##작성자
	if(isset($temp['comment'])){	
		$comment =cute_es_string($temp['comment']);##작업내용
	}
	else{
		$comment ="작업내용 입력안함";

	}
	$timeSpentSeconds = $temp['timeSpentSeconds'];##작업시간
	$started = $temp['started'];##작용시간
	$work_sql  = $work_sql." ('".$author."','".$comment."','".$timeSpentSeconds."','".$started."','".$project."','".$key."'),";

}
if(count($worklogs)==0){}
else{
	$work_sql =substr($work_sql, 0, -1);
	
	$work_res	=  mysqli_query($real_sock,$work_sql) or die(mysqli_error($real_sock));
}

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

if(count($comments)==0){

}
else{
	$comment_sql =substr($comment_sql, 0, -1);
	$comment_res	=  mysqli_query($real_sock,$comment_sql) or die(mysqli_error($real_sock));

}
?>