var lyState = "Off";
var lbState = "Off";
var lgState = "Off";


function yLight(){
    document.getElementById("lSound").play();
    var yb = document.getElementById("yb");
    if (lyState == "Off"){
        console.log("1");
        yb.src  = "./Buttons/Yellow_Bulb_On.png";
        lyState = "On";
    } else if(lyState == "On"){
        console.log("2");
        yb.src  = "./Buttons/Yellow_Bulb_Off.png";
        lyState = "Off";
    }
}

function bLight(){

    document.getElementById("lSound").play();

    var bb = document.getElementById("bb");

    if (lbState == "Off"){

        console.log("1");
        bb.src  = "./Buttons/Blue_Bulb_On.png";
        lbState = "On";

    } else if(lbState == "On"){
        console.log("2");
        bb.src  = "./Buttons/Blue_Bulb_Off.png";
        lbState = "Off";
    }
}

function gLight(){
    document.getElementById("lSound").play();
    var gb = document.getElementById("gb");
    if (lgState == "Off"){
        console.log("1");
        gb.src  = "./Buttons/Green_Bulb_On.png";   
        console.log(gb.src);
        lgState = "On";

    } else if(lgState == "On"){
        
        console.log("2");
        gb.src  = "./Buttons/Green_Bulb_Off.png";
        lgState = "Off";

    }
}