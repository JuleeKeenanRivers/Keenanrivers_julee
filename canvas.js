function text() 
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    
    canvas.shadowOffsetX = 4;
    canvas.shadowOffsetY = 4;
    canvas.shadowBlur = 6;
    canvas.shadowColor = "rgba(0, 0, 225, .5)";
    
    
    canvas.font = "bold 36px Tahoma";
    canvas.textAlign = "start";
    canvas.fillText("robinette", 300, 100);
    
}
window.addEventListener("load", text, false);