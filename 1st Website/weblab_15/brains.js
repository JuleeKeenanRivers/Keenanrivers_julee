/**
 * Created by keenanriversj1816 on 4/28/2017.
 */
function shapes() {
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    var g = canvas.createLinearGradient()


    canvas.fillRect(10, 10, 100, 200);

    
}

window.addEventListener("load", shapes, false);