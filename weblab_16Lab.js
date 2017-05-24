function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0, 0, 600, 600);
    var xPos = e.clientX;
    var yPos = e.clientY;
    var pic = new Image();
    pic.src = "http://www.beaches.com/assets/img/home/rst-btc.jpg";
    canvas.drawImage(pic, xPos, yPos, 100, 100);
}
window.addEventListener("load", mouse, false);