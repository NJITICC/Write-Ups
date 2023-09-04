<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    echo file_get_contents('/flag');
}
?>
<form method="POST">
    <button type="submit">Submit</button>
</form>
