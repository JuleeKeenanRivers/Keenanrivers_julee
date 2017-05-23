/**
 * Created by keenanriversj1816 on 5/23/2017.
 */
/**
 * Created by keenanriversj1816 on 4/28/2017.
 */
function shapes() {
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.strokeStyle= "yellow";
    canvas.fillStyle = "purple";
    canvas.beginPath();
    canvas.moveTo(50, 50);
    canvas.lineTo(20, 250);
    canvas.lineTo(300, 200);
    canvas.closePath();
    canvas.stroke();
    canvas.fill();

}


window.addEventListener("load", shapes, false);


}
					