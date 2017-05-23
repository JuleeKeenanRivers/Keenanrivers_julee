/**
 * Created by keenanriversj1816 on 5/23/2017.
 */
{var g = canvas.createLinearGradient(10, 10, 100, 200);
g.addColorStop(0, "blue");
g.addColorStop(.3, "green");
g.addColorStop(1, "red");
canvas.fillStyle = g;
canvas.fillRect(10, 10, 100, 200);
}