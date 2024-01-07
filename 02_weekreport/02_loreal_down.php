<?php

include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');


$jira_comp_idx = isset($_GET['jira_comp_idx']) ? $_GET['jira_comp_idx'] : 'BAT글로';
$start_date = isset($_GET['start_date']) ? $_GET['start_date'] : $temp_start_date;
$end_date = isset($_GET['end_date']) ? $_GET['end_date'] : $temp_end_date ;




$EXCEL_STR = "
<h2> 작업자별</h2>
<table border=1>
<thead>
	<tr>
	<th> #</th>
	<th> 작업자명</th>
	<th> 초</th>
	<th> 공수</th>
	<th> 갯수</th>
	</tr>
</thead>
<tbody>";


$total = 0;
$total_second =0;
$total_cnt =0;
$sql	 = "

SELECT a.jw_dix,a.jmi_work_name,SUM(a.timeSpentSeconds) as totalsecond,(SUM(a.timeSpentSeconds/3600)/8)/20.8 as totalgong,count(a.jw_dix) as cnt


	
from  jirasync_work as a
JOIN jirasync_main_info as b
ON a.jmi_inx = b.jmi_inx
WHERE b.components LIKE '%".$jira_comp_idx ."%'
AND a.check_date BETWEEN '".$start_date."' AND '".$end_date."'
GROUP BY a.jmi_work_name 
";



$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
$total += 1;
$total_second +=$info['totalsecond'];
$total_cnt +=$info['cnt'];
$EXCEL_STR = $EXCEL_STR."
		<tr>
			<td>".$total."</td>
			<td>".$info['jmi_work_name']."</td>
			<td>".$info['totalsecond']."</td>
			<td>".round($info['totalgong'],2)."</td>
			<td>".$info['cnt']."</td>
	
	</tr>";
}
$total += 1;
$EXCEL_STR = $EXCEL_STR."
		<tr>
			<td>".$total."</td>
			<td>합계</td>
			<td>".$total_second."</td>
			<td>".round((($total_second/3600)/8)/20.8,2)."</td>
			<td>".$total_cnt."</td>
	
	</tr></tbody>
	</table border=1>
	<h2> 작업별</h2>
	<table border=1>
	<thead>
		<tr>
			<th>	#	</th>
			<th>	작업자명	</th>
			<th>	초	</th>
			<th>	작업일자	</th>
			<th>	작업명	</th>
			<th>	브랜드	</th>
			<th>	코멘트	</th>
	
		</tr>
	</thead>
	<tbody>
		


		";
	
	




$total = 0;
$sql	 = "

SELECT 


a.jmi_work_name,
a.timeSpentSeconds,
b.jmi_summary,
b.components,

a.comment	,a.jmi_key,a.check_date


	
from  jirasync_work as a
JOIN jirasync_main_info as b
ON a.jmi_inx = b.jmi_inx
WHERE b.components LIKE '%".$jira_comp_idx ."%'
AND a.check_date BETWEEN '".$start_date."' AND '".$end_date."'

";

$res	=  mysqli_query($real_sock,$sql) or die(mysqli_error($real_sock));
while($info	 = mysqli_fetch_array($res)){
$total += 1;
$EXCEL_STR = $EXCEL_STR."<tr>";

	$name = $total ;	$EXCEL_STR = $EXCEL_STR."<td>".$name."</td>";
	$name = $info['jmi_work_name'] ;$EXCEL_STR = $EXCEL_STR."<td>".$name."</td>";
	$name = $info['timeSpentSeconds'] ;	$EXCEL_STR = $EXCEL_STR."<td>".$name."</td>";
	$name = $info['check_date'] ;	$EXCEL_STR = $EXCEL_STR."<td>".$name."</td>";	
	$name = $info['jmi_summary'] ;	$EXCEL_STR = $EXCEL_STR."<td>".$name."</td>";
	$name = $info['components'] ;	$EXCEL_STR = $EXCEL_STR."<td>".$name."</td>";
	$name = $info['comment'] ;	$EXCEL_STR = $EXCEL_STR."<td>".$name."</td></tr>";
}
$EXCEL_STR = $EXCEL_STR."
</tbody>
</table>
";


header( "Content-type: application/vnd.ms-excel" );
header( "Content-type: application/vnd.ms-excel; charset=utf-8");
header( "Content-Disposition: attachment; filename = [MZ]".$jira_comp_idx."_".$start_date."_".$end_date."공수.xls" );
header( "Content-Description: PHP4 Generated Data" );


$EXCEL_STR .= "</tbody></table>";
echo $EXCEL_STR;

echo "<meta content=\"application/vnd.ms-excel; charset=UTF-8\" name=\"Content-type\"> ";


 
?>