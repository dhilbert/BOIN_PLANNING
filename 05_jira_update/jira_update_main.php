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
				




$url = 'https://boinplanning.atlassian.net/rest/api/latest/search?fields=key&maxResults=10000';
$url_resss = cute_hh_curl($username,$password,$url);
$url_ress = $url_resss['issues'];

for($jira_i = 0 ; $jira_i <count($url_ress); $jira_i++ ){
	
	
	$keysss = $url_ress[$jira_i]['key'];
	$url = $url_ress[$jira_i]['self'];
	$checks = explode("-",$keysss);
	$check = $checks[0];

	if($check=='EF2024'){}
	else{
		include('jira_ft.php');
	}

}



?>