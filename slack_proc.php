<?php
include_once('lib/session.php');
include_once('lib/dbcon_BOIN_PLANNING.php');



$username = isset($_GET['username']) ? $_GET['username'] : 3;
$maintext = isset($_GET['maintext']) ? $_GET['maintext'] : 3;
if( strlen($username)==0) {
    echo "<script>
            alert('사람이름을 입력하시오');
            history.back();
        </script> ";
}
if( strlen($maintext)==0) {
    echo "<script>
            alert('보낼 메세지를을 입력하시오');
            history.back();
        </script> ";
}



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
            //$ch = curl_init('https://hooks.slack.com/services/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');    // 슬랙 테스트방
            $ch = curl_init('https://hooks.slack.com/services/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');    //정휘영
            
            
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

/*
echo "<script>
alert('슬랙 채널 #jira_site_slackapitest 를 확인 하십시오');
history.back();
</script> ";
*/

?>