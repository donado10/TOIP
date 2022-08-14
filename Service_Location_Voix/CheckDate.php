<?php

function FormatDate($str){
    $re = '/(.*?)(\d{2})(\d{4})$/m';

    preg_match_all($re, $str, $matches, PREG_SET_ORDER, 0);

    if (strlen($matches[0][1]) == 1){

        $Jour = "0".$matches[0][1];
        $Mois = $matches[0][2];
        $Annee = $matches[0][3];
    }
    elseif(strlen($matches[0][1])) {

        $Jour = $matches[0][1];
        $Mois = $matches[0][2];
        $Annee = $matches[0][3];
    }

    $date = $Annee."-".$Mois."-".$Jour;

    return $date;
}

function CheckTime($date){
    $re = '/(.*?)(\d{2})(\d{4})$/m';

    preg_match_all($re, $date, $matches, PREG_SET_ORDER, 0);

    $month = date('m');
    $day = date('d');
    if ($matches[0][2] < $month) {
        return 0;
    } elseif($matches[0][2] == $month && $matches[0][1] < $day) {
        return 0;
    }
    else {
        return 1;
    }
    
    
}

function connection($date){
    $servername = "localhost";
    $database = "GT1_2022";
    $username = "root";
    $password = "root";

    // Create connection

    $conn = mysqli_connect($servername, $username, $password, $database);

    // Check connection

    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }


    $sql = "SELECT Period from Date where Period = '{$date}'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        return 1;
    } else {
        return 0;
    }
}



$date = $_REQUEST['date'];

$CheckingDateNow = CheckTime($date);

$date = FormatDate($date);


if (connection($date) == 1 && $CheckingDateNow == 1) {
    echo $date;
} elseif (connection($date) == 1 && $CheckingDateNow == 0) {
    echo 0;
}else {
    echo 0;
}


?>