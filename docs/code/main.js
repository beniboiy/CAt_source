/*
    What follows is an original production of code by Caribbean AUTOtech (established as of August 2016) - a subsidiary of GMC.
    Founding members include (in alphabetical order) Yohan Francis, Kevin Nguyen, and Ben Robinson.
    Unauthorised copying, plagarising, or any use of the following not intended for by all of the founding members unanimously is strictly forbidden.

    ©CAt.GMC (2016)
*/

window.addEventListener("load", startup);
var feed = document.getElementById('feed');

function startup()
{
    // Initialising a pop up to display some information. A cookie is also created to prevent this occurring between reloads of the homepage
    var opened = document.cookie;

    if(opened.substr(0,12) !== "visited=true"){
        var popUp = document.createElement("div");
        popUp.style.width = "50%";
        popUp.style.height = "50%";
        popUp.style.margin = "auto";
        popUp.style.padding = "1%";
        popUp.style.position = "absolute";
        popUp.style.backgroundColor = "rgba(250,250,250, 0.1)";
        popUp.innerHTML = "This is a page by CAt.<br/><br/>Please enjoy and subscribe for news<br/>";
        popUp.style.textAlign = "center";
        popUp.style.fontSize = "3em";
        popUp.style.color = "black";
        popUp.style.top = "40%";
        popUp.style.left = "25%";
        popUp.style.zIndex = "10";

        // Preventing the popUp everytime
        document.cookie = "visited=true";

        var button = document.createElement("button");
        button.innerHTML = "Okay, let's go!";
        button.style.fontSize = "0.33em";
        button.style.padding = "2.5px";
        button.style.color = "black";
        button.style.border = "1px solid black";
        button.style.borderRadius = "7.5px";
        button.style.backgroundColor = "white";
        button.style.marginTop = "10%";
        button.addEventListener('mousedown', darken);
        button.addEventListener('mouseup', lighten);
        button.addEventListener('click', hide);

        function darken()
        {
            this.style.backgroundColor = "rgba(255, 75, 75, 1)";
        };

        function lighten()
        {
            this.style.backgroundColor = "white";
        };

        function hide()
        {
            var timer = setInterval(smooth, 30);
            var opacityNumber = Number(popUp.style.backgroundColor.substring(20, popUp.style.backgroundColor.length -1));

            function smooth()
            {
                if(opacityNumber <= 0.1){
                    popUp.style.display = "none";
                    clearInterval(timer);
                } else {
                    opacityNumber -= 0.05;
                    popUp.style.opacity = opacityNumber;
                };
            };
        };

        popUp.appendChild(button);

        document.body.appendChild(popUp);

        shiftUp();

        function shiftUp()
        {
        var shifter = setInterval(move, 30);
        var opacityNumber = 0.1;

        function move()
        {
            var topNumber = Number(popUp.style.top.substr(0,2));

            if(topNumber === 15)
            {
            clearInterval(shifter);
            } else {
                topNumber -= 0.085;
                opacityNumber += 0.0325;
                popUp.style.top = topNumber + "%";
                popUp.style.backgroundColor = "rgba(250,250,250," + opacityNumber + ")";
            };
        };
        };
    };

    var footer = document.getElementById('footer');
    footer.addEventListener('scroll', shuffle);
    
    // Update the feed every ~1min
    var updateFeed = setInterval(60000, updateIt);
};

function jumpTo(tabID)
{
    var tabSelected = tabID + ".php";
    console.log(tabSelected);
    this.location.href = tabSelected;
};

function shuffle(e)
{
  console.log(e.currentTarget.scrollLeft);
};


function updateIt()
{   
    var updateCall = new XMLHttpRequest();
    
    updateCall.onreadystatechange = callPosts;
    updateCall.open('GET', 'code/feed.php');
    updateCall.send();
    
    function callPosts()
    {
        if (updateCall.readyState === XMLHttpRequest.DONE) {
            if (updateCall.status === 200) {
                console.log(updateCall.responseText);
            } else {
                alert('There was a problem with the request.');
            }
        }
    }
}
