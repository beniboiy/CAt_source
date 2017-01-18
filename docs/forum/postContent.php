<?php
if($_SERVER["REQUEST_METHOD"] === "POST")
{
    if($_POST["user"] === "CAt_post_write")
    {
        $db_server = 'localhost';
        $db_user = _POST["user"];
        $db_pass = 'cat-pwd-post';
        $db_name = 'CAt_content';
        $connection = new mysqli($db_server, $db_user, $db_pass, $db_name);
    
        date_default_timezone_set('Australia/Melbourne');
        $date = (string)date('Y-m-d');
        
        $query = "INSERT INTO posts(content, author, pub_date) VALUES ("._POST["content"].", "."CAt Team Tester".', '.$date.")";
    
        if ($connection->connect_error) {
            die('Database connection failed: ');
        };
    
        $response = $connection->query($query);
    
        echo "Posted Successfully";
    }
}

?>