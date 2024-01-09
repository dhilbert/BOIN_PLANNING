<?php

header('Content-Type: text/html; charset=UTF-8');

//변수에 한글이 포함될 경우 아래 코드를 추가한다.
putenv("LANG=ko_KR.UTF-8");
setlocale(LC_ALL, 'ko_KR.utf8');


$변수1 = "AAA";
$변수2 = "가나다";
$변수3 = "가 나 다"; //공백이 있을경우 문자열로 묶어줘야 함 


//exec("python3 emailsend.py");
exec("python3 emailsend.py ", $output);





print_r($output);
/*
echo $output[0]. "<br>"; //Success1 good
echo $output[1]. "<br>"; //Success2
echo $output[2]. "<br>"; //AAA
echo $output[3]. "<br>"; //가나다
echo $output[4]. "<br>"; //가 나 다
*/
?>
