<?php
// Just testing how to select only latest 10 elements for feed to display
$test_posts = ["post1 - info info info", "post2 - info info info", "post3 - info info info", "post4 - info info info", "post5 - info info info", "post6 - info info info", "post7 - info info info", "post8 - info info info", "post9 - info info info", "post10 - info info info"];

    /*for($i = 0; $i < sizeof($test_posts); $i++)
    {
        if($i >= sizeof($test_posts) - 5)
        {
            echo $test_posts[$i]."\n";    
        };
    };*/

$first_run = true;              // First run flag
$copy_array = null;             // Copy array exists as a reference to check whether the original has updated
if(sizeof($test_posts>10)){     // If the array is longer than 10, chop it. Later we can change this so that we check whether
    $ten_array=array_slice($test_posts,0,10);       //the text fits on the feed
}
else{
    $ten_array=$test_posts;     // if less than 10 just use the originl
}

if($first_run) {                // if this is the first run
    $i = 0;
    $first_run = false;         // no longer first run after this is done so invert flag
    $copy_array = $ten_array;       // make a copy for comparison later on
    while ($i <= 10) {              // echo this into feed
        $first_run = false;
        echo "<p>" . $ten_array[$i] . "</p>";   // Changed it to be wrapped in HTML paragraph tags so it should stay within the feed block
                                                // (will change html/css so it's certain)
        $i++;                       // for loop
    }
}
else{
    if($ten_array!=$copy_array){
        echo "The array has been changed, now we update new info.";
        // todo - as functionality allows, if the feed has changed, echo the new stuff on. logic to be decided
    }
}


require_once 'connection.php';


/* NOTES:

For feed to work eventually:
- need to have current info of array of children nodes (post summaries)
  then compare the 10 latest from the database and either remove or leave 
	-- can use MySQL database's id number as identifier for comparison (easier than checking content)
	-- need DOMNode class from PHP for checking children number (and probably content - although ^id could be added if we made the children a class of objects)

- need a way to actually authenticate to an admin/reserved page to allow write access to database

*/
?>

