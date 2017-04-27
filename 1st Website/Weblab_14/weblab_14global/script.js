/**
 * Created by keenanriversj1816 on 4/26/2017.
 */
// function validate(){
//     var x = document.forms.input.username.value;
//     var atPos = x.indexOf("@");
//     var dotPos = x.lastIndexOf(".");
//
//
//     if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
//         alert("This is not a valid email address!");
//
//     else
//         alert("Success!");
// }
//
// function validate(y){
//     if( y < 6) {
//         alert("This is not a valid password!");
//         return false;
//     }
//     else
//         return true;
// }

function validate(){
    var x = document.forms.input.username.value;
    var y = document.forms.input.password.value;

    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    //if username and password are not correct
    if((atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length) && y.length < 6)
        alert("This is not a valid email address or password!");
    else {
        if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
            alert("Username is not correct.");
        else if (y < 6)
            alert("Password is not correct.");
        else
            alert("Success!");
    }
}
    