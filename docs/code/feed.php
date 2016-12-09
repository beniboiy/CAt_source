<?php
    // Just testing how to select only latest 10 elements for feed to display
    $test_posts = ["post1 - info info info", "post2 - info info info", "post3 - info info info", "post4 - info info info", "post5 - info info info", "post6 - info info info", "post7 - info info info", "post8 - info info info", "post9 - info info info", "post10 - info info info"];
    
    for($i = 0; $i < sizeof($test_posts); $i++)
    {
        if($i >= sizeof($test_posts) - 5)
        {
            echo $test_posts[$i]."\n";    
        };
    };
?>
