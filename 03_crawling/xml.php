<?php

include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');
include "PHPExcel-1.8/Classes/PHPExcel.php";



$company_list = array(array(0,"메가존"));
$sql	 = "select * from crawling_company;";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));

while($info	 = mysqli_fetch_array($res)){
  $temp_list = array($info['crawling_company_idx'],$info['crawling_company_name']	);
  array_push($company_list,$temp_list);
};


function hd_checking_company($company_list,$name){
  $want_num = 99;
  for($i=0 ; $i <count($company_list);$i++){
    if($company_list[$i][1]==$name){
      $want_num = $company_list[$i][0];
      break ;
    }
  }

  return $want_num;
}





$now_time =  date("Y-m-d H:i:s");
$crawling_flie_idx = isset($_GET['crawling_flie_idx']) ? $_GET['crawling_flie_idx'] : 3;

$sql	 = "select crawling_flie_name,crawling_work from crawling_file where crawling_flie_idx ='".$crawling_flie_idx."';";
$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
$info	 = mysqli_fetch_array($res);
$crawling_work = $info['crawling_work'];
//echo $info['crawling_flie_name'];

$objPHPExcel = new PHPExcel();
// 엑셀 데이터를 담을 배열을 선언한다.
$allData = array();
// 파일의 저장형식이 utf-8일 경우 한글파일 이름은 깨지므로 euc-kr로 변환해준다.

$file_name = "xlsx/".$info['crawling_flie_name'];
$filename = iconv("UTF-8", "EUC-KR",$file_name );



try {

        // 업로드한 PHP 파일을 읽어온다.

	$objPHPExcel = PHPExcel_IOFactory::load($filename);

	$sheetsCount = $objPHPExcel -> getSheetCount();



	// 시트Sheet별로 읽기

	for($i = 0; $i < $sheetsCount; $i++) {



          $objPHPExcel -> setActiveSheetIndex($i);

          $sheet = $objPHPExcel -> getActiveSheet();

          $highestRow = $sheet -> getHighestRow();   			           // 마지막 행
          

          $highestColumn = $sheet -> getHighestColumn();	// 마지막 컬럼



          // 한줄읽기

          for($row = 2; $row <= $highestRow; $row++) {



            // $rowData가 한줄의 데이터를 셀별로 배열처리 된다.

            $rowData = $sheet -> rangeToArray("A" . $row . ":" . $highestColumn . $row, NULL, TRUE, FALSE);
            


            // $rowData에 들어가는 값은 계속 초기화 되기때문에 값을 담을 새로운 배열을 선안하고 담는다.
            
            $allData[$row] = $rowData[0];

          }

	}

} catch(exception $e) {

	echo $e;

}



echo "<pre>";


echo "<br>";



//

$start_sql="INSERT INTO crawling(crawling_company_inx, 
crawling_sku,
crawling_price,
crawling_dis,
crawling_name,
crawling_status,
crawling_work,
crawling_reg_date)  VALUES";
$rrsql = $start_sql;

print_r($allData[3]);

for($i=2 ; $i <count($allData)+2;$i++){
  $temp_list = $allData[$i];
        
  
      $rrsql = $rrsql." (
        '".hd_checking_company($company_list,trim($temp_list[0]))."',
        '".$temp_list[2]."',
        '".$temp_list[3]."',
        '".$temp_list[4]."',
        '".$temp_list[1]."',
        '1',
        '".$crawling_work."',
        
        now()),";
        
      
      
}





$rrsql = substr($rrsql, 0, -1);

$res	=  mysqli_query($real_sock,$rrsql) or die(mysqli_error($real_sock));



echo "<script>
	alert('파일 업로드 성공');
	parent.location.replace('/BOIN_PLANNING/03_crawling/01_crawling_settiong.php');
</script> ";



?>
