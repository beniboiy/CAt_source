<!DOCTYPE html>
<html>
<head>
    <title>Caribbean AUTOtech</title>
    <meta name="author" content="GMC">
    <meta name="description" content="Japanese Imports and Related Services">
    <meta name="keywords" content="Japanese, Cars, JDM, Parts">
    <meta name="google-site-verification" content="PEVdqzX66gqmd4D1vVJKXlF0uOKEoNQ2UMzz1f9zhWM" />
    <meta name="viewport" content="width=device-width, height=device-height, intial-scale=1">
    <link rel="icon" href="images/CAt_ico.ico">
    <link rel="stylesheet" href="code/stylesheet.css">

    <!-- For iOS web application -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <link rel="apple-touch-statup-image" href="images/index_wallpaper.png">
    <link rel="apple-touch-icon" href="images/CAt_ico.ico">

    <!-- For Android web application -->
    <meta name ="mobile-web-app-capable" content="yes">
    <link rel="shortcut icon" sizes="196x196" href="images/CAt_ico.ico" />
</head>
<body>
    <div id="titlebody">
        <div class="banner" id="header">Caribbean &nbsp;&nbsp;&nbsp;<span>AUTO</span>tech</div>
            <table>
                <tr id="menubar">
                    <td class="menubar" id="homeTab" onclick="jumpTo('index')">Home</td>
                    <td class="menubar" id="auctionsTab" onclick="jumpTo('auctions')">Auctions</td>
                    <td class="menubar" id="diyTab" onclick="jumpTo('diy')">DIY</td>
                    <td class="menubar" id="forumTab" style="color: white; border-left: 2px solid white; border-right: 2px solid white;">Forum</td>
                    <td class="menubar" id="merchTab" onclick="jumpTo('merch')">Merchandise</td>
                    <td class="menubar" id="aboutTab" onclick="jumpTo('about')">About Us</td>
                </tr>
            </table>
    </div>
    <div id="mainbody">
        <div class="container" id="mainContent">
            <form action="code/postContent.php" method="post">
                <fieldset>
                    <legend>Post Something!</legend>
                    <input style= "color:black;" type="text" name="user" autofocus placeholder="Your username goes here">
                    <br/>
                    <textarea style="width: 50%; height: 50%; resize: none; color:black;" placeholder="Your thoughts go here" name="content"></textarea>
                    <br/>
                    <input style="color:black;" type="submit" value="Post">
                </fieldset>
            </form>
        </div>
        <div class="container" id="feed">We'll add a feed here. Eventually.</div>
        <div class="banner" id="footer">
            Caribbean AUTOtech is purely a hobby, founded by three guys with no technical experience or qualifications. Everything here is just our oppinion and is most likely wrong. <br/>GMC has no affiliation with General Motors Co. or any of its subsidiaries - again, this is a reference to a private joke between founders. Enjoy.
        </div>
    </div>

    <script src="code/main.js"></script>
</body>
</html>
