<?php
function CheckID($choix){
    if ($choix == "1"){
        return 1;
    }
    elseif ($choix == "2") {
        return 2;
    }
    elseif ($choix == "3") {
        return 3;
    }
    else {
        return 0;
    }
}



$terrain = $_REQUEST['terrainID'];

$terrain =  CheckID($terrain);
echo $terrain;

return $terrain;

?>