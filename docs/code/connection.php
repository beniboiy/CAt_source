<?php
// Script to be REQUIRED in 'feed.php' for MySQL connections (SECURE)
$db_server = 'localhost';
$db_user = 'root';  // LATER: should change it so there is a specific user for read/write functions who cannot grant access 
                    // - and maybe limit write functionality 
$db_pass = 'cat-pwd';
$db_name = 'CAt_content';
$connection = new mysqli($db_server, $db_user, $db_pass, $db_name);
    
// CHECK CONNECTION
if ($connection->connect_error) {
    die('Database connection failed: ');
};
    
// PREPARED STATEMENTS FOR SAFETY - later implemented

$sql = 'SELECT * FROM posts';
    
$response = $connection->query($sql);
$response_text = $response->fetch_assoc();

if ($response_text !== null)
{
    echo $response_text['content'] . "<br/>" . $response_text['author'] . "<br/>";
} else {
    echo "Error";
}
?>