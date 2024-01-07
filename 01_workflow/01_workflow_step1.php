<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');


$summary = isset($_GET['summary']) ? $_GET['summary'] : 3;
$summary = str_replace('[' , '*', $summary);
$summary = str_replace(']' , '*', $summary);
$summary = str_replace('(' , '\(', $summary);
$summary = str_replace(')' , '\)', $summary);

$description = isset($_GET['description']) ? $_GET['description'] : 3;
$description = str_replace('"' , '', $description);
$description = str_replace("'" , "", $description);
$description = str_replace("[" , "", $description);
$description = str_replace("]" , "", $description);
$description = str_replace("\r\n", "<br>",  $description);
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
					gmail 확인 (공사중 테스트 페이지)
					
					</div>

					<div class="panel-body">
<?php

$username = 'yoonhd@mz.co.kr';
$password = 'K80gueIJUonHEGUJHQ4y44E6';
$password = 'aqzsIiu6OOqPsJdb6XWM031D';

$url = "https://mz-dev.atlassian.net/rest/api/2/issue/";


$json_data = '{
	
    "fields": {
        "project": {
            "self": "https://mz-dev.atlassian.net/rest/api/2/project/11600",
			"id": "11600",
			"key": "MZNO",
			"name": "DSG-SM/그로스팀 업무관리",
			"projectTypeKey": "software",
			"simplified": false,
			"avatarUrls": {
				"48x48": "https://mz-dev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10409",
				"24x24": "https://mz-dev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10409?size=small",
				"16x16": "https://mz-dev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10409?size=xsmall",
				"32x32": "https://mz-dev.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10409?size=medium"
			} 
        }
        ,"issuetype": { 
            "name": "작업",
            "id": "3" 
        }
        ,"summary": "'.$summary.'"     
        ,"description": "'.$description.'"     
        ,"labels": [ 
            "일반유지보수"
        ]        
        ,  "assignee": {
			"self": "https://mz-dev.atlassian.net/rest/api/2/user?accountId=557058%3Ae044222f-7e8e-4af3-8fe3-12d0f0ba1af4",
			"accountId": "557058:e044222f-7e8e-4af3-8fe3-12d0f0ba1af4",
			"emailAddress": "olive1@mz.co.kr",
			"avatarUrls": {
			  "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:e044222f-7e8e-4af3-8fe3-12d0f0ba1af4/c6565c20-cbbe-4cb3-823c-b84de9ddddba/48",
			  "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:e044222f-7e8e-4af3-8fe3-12d0f0ba1af4/c6565c20-cbbe-4cb3-823c-b84de9ddddba/24",
			  "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:e044222f-7e8e-4af3-8fe3-12d0f0ba1af4/c6565c20-cbbe-4cb3-823c-b84de9ddddba/16",
			  "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:e044222f-7e8e-4af3-8fe3-12d0f0ba1af4/c6565c20-cbbe-4cb3-823c-b84de9ddddba/32"
			},
			"displayName": "안승희",
			"active": true,
			"timeZone": "Asia/Seoul",
			"accountType": "atlassian"
		  },
		  "components": [
			{
			  "self": "https://mz-dev.atlassian.net/rest/api/2/component/19627",
			  "id": "19627",
			  "name": "로레알_아르마니",
			  "description": "아르마니 운영"
			}
		  ],"fixVersions": [
			{
			  "self": "https://mz-dev.atlassian.net/rest/api/2/version/24968",
			  "id": "24968",
			  "description": "2022년 3월 업무",
			  "name": "2022년 3월 업무",
			  "archived": false,
			  "released": false,
			  "releaseDate": "2022-03-31"
			}
		  ],
		  "reporter": {
			"self": "https://mz-dev.atlassian.net/rest/api/2/user?accountId=5f9631478405b10077318f2c",
			"accountId": "5f9631478405b10077318f2c",
			"emailAddress": "yoonhd@mz.co.kr",
			"avatarUrls": {
			  "48x48": "https://secure.gravatar.com/avatar/c4be0d10744ba0dbd0eed19227da335c?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Fdefault-avatar-1.png",
			  "24x24": "https://secure.gravatar.com/avatar/c4be0d10744ba0dbd0eed19227da335c?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Fdefault-avatar-1.png",
			  "16x16": "https://secure.gravatar.com/avatar/c4be0d10744ba0dbd0eed19227da335c?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Fdefault-avatar-1.png",
			  "32x32": "https://secure.gravatar.com/avatar/c4be0d10744ba0dbd0eed19227da335c?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Fdefault-avatar-1.png"
			},
			"displayName": "윤희동",
			"active": true,
			"timeZone": "Asia/Seoul",
			"accountType": "atlassian"
		  }
		
    }
}';

$body = $json_data ;


//$body = json_encode($json_data);



$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_USERPWD, "$username:$password");
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);


$result = curl_exec ($ch);



print_r($result);


$temp = explode('","key":"',$result);
$temp = explode('","self":"',$temp[1]);
$jira_num= $temp[0];




$username = "시스템 알림";
$maintext = "윤희동님이 안승희 님에게 업무를 요청 하였습니다. 

https://mz-dev.atlassian.net/browse/".$jira_num."

[업무 요청 내역]

".$description


;




class Slack {
    
    private $postData;
    
    public function __construct(){
    }
    
    public function setPostData($postData){
        $this->postData = $postData;
    }
    
    public function sendSlack($postData) {
        
        $this->postData = $postData;
        
        if( isset($this->postData) == false || empty($this->postData) == true) {
            // 데이터가 없으면 값을 보내지 않는다.
            return false;
        }
        
        try {
                            
            //$ch = curl_init('https://hooks.slack.com/services/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');
            
            //$ch = curl_init('https://hooks.slack.com/services/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');    //정휘영
            //$ch = curl_init('https://hooks.slack.com/services/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');    // 슬랙 테스트방
			$ch = curl_init('https://hooks.slack.com/services/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');    // 슬랙 테스트방
            
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST,  'POST');
            curl_setopt($ch, CURLOPT_POSTFIELDS,     'payload='.json_encode($this->postData));
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            
            $result = curl_exec($ch);
            curl_close($ch);
            
        } catch(Exception $e) {
            $s = $e->getMessage() . ' (오류코드:' . $e->getCode() . ')';
            //로깅처리
        }
        
        return true;
    }
    


}
$slack = new Slack(); 
$postData = array( 'channel' => '#jira_site_slackapitest', 'username' => $username, 'text' =>  $maintext."
". date("Y-m-d H:i:s") ); 

$slack->sendSlack($postData);








?>














					</div>
				</div>
			</div>



		 
  

	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');

?>




<div class="modal fade" id="99_0_mysettiong_main_0" role="dialog">
	<div class="modal-dialog modal-lg">
		<!-- Modal content-->
		<div class="modal-content">
			<div class="modal-header">
				<strong>템플릿 추가</strong>
			</div>
			<div class="modal-body">
				
					<div class="form-group">

					<form name="frm" role="form" method="get" action="99_0_mysettiong_main_proc.php">

						<label>업무 유형</label>							
							<input class='form-control'		name = 'indi_tem_title'	style='background-color:'><p><br>
						<label>업체</label>							
							<select class="form-control" name = 'jira_comp_idx'>
							<?php
								$jiraapi_component_sql	 = "select * from jiraapi_component where jira_comp_status =1;";
								$jiraapi_component_res	=  mysqli_query($real_sock,$jiraapi_component_sql) or die(mysqli_error($real_sock));
								while($jiraapi_component_info	 = mysqli_fetch_array($jiraapi_component_res)){
										echo "<option value = '".$jiraapi_component_info['jira_comp_idx']."'>".$jiraapi_component_info['jira_comp_name']."</option>";
								};
							?>
							</select>
						<label>회사 선택</label>
						<select class="form-control" name = 'company_idx'>
							<?php
								$admin_company_info_sql	 = "select * from admin_company_info;";
								$admin_company_info_res	=  mysqli_query($real_sock,$admin_company_info_sql) or die(mysqli_error($real_sock));
								while($admin_company_info_info	 = mysqli_fetch_array($admin_company_info_res)){
										echo "<option value = '".$admin_company_info_info['company_idx']."'>".$admin_company_info_info['company_name']."</option>";
								};
							?>
							</select>
							<div class="form-group">
									<label>템플릿 입력</label>
									<textarea class="form-control" rows="4" name ='indi_tem_maintext'></textarea>
							</div>








						</div>
						<p><br>
					














				


			</div>
			<div class="modal-footer">
			<input  type='submit' class="btn btn-success login-btn" type="submit" value="템플릿 등록">
				</form>


				 <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
			</div>
		</div>
	</div>
</div>
