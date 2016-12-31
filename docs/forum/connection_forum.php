<?php
$db_server = 'localhost';
$db_user = 'root';  // LATER: should change it so there is a specific user for read/write functions who cannot grant access
// - and maybe limit write functionality
$db_pass = 'cat-pwd';
$db_name = 'forum';
$connection = new mysqli($db_server, $db_user, $db_pass, $db_name);

// CHECK CONNECTION
if ($connection->connect_error) {
    die('Database connection failed: ');
};
