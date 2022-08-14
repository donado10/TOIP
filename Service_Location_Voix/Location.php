<?php

function connection($ID_date,$database_name){
    $servername = "localhost";
    $database = $database_name;
    $username = "root";
    $password = "root";

    // Create connection

    $conn = mysqli_connect($servername, $username, $password, $database);

    // Check connection

    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }


    $sql = "SELECT Hour.Period from Date_Hour inner join Hour on Hour.ID_hour = Date_Hour.ID_hour inner join Date on Date.ID_date = Date_Hour.ID_date where Date.Period = '{$ID_date}'  AND disponibilite = 1";
    $result = $conn->query($sql);

    $date ="";
    if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $date = $date.$row["Period"]." heure ";
    }
    echo $date;
    } else {
    echo "0 resultat";
    }

    mysqli_close($conn);
}



$date = $_REQUEST['date'];
$terrain = $_REQUEST['terrain'];

if ($terrain == "1") {
    $terrain = "GT1_2022";
    return connection($date,$terrain);
}elseif ($terrain == "2") {
    $terrain = "GT2_2022";
    return connection($date,$terrain);
}elseif ($terrain == "3") {
    $terrain = "PT_2022";
    return connection($date,$terrain);
}else {
    echo "Ce terrain n'est pas disponible";
}






?>