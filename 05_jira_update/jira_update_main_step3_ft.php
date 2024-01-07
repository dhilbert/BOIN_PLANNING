<?php

include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

//SELECT work_comment,  SUBSTRING_INDEX(SUBSTRING_INDEX(work_comment, '[', -1), ']', 1) FROM jira_work_log WHERE jql_idx = 6204;


?>