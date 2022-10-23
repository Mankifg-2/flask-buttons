
            function yLight(){

                var yb = document.getElementById("yb");

                if (yb.src = "./Buttons/Yellow_Bulb_Off.png"){

                    console.log("1");
                    yb.src  = "./Buttons/Yellow_Bulb_On.png";
                    
                    console.log(yb.src);

                    /*
                    document.getElementById("yb").style.height = "100%"
                    document.getElementById("yb").style.width = "100%"
                    */

                } else {

                    console.log("2");

                    yb.src  = "./Buttons/Yellow_Bulb_Off.png";

                }
               

            }