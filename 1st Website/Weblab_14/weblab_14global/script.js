/**
 * Created by keenanriversj1816 on 4/26/2017.
 */
function validate(){
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");


    if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
        alert("This is not a valid email address!");

    else
        alert("Success!");
}

function validate(){
    var y = document.forms.input.password.value;

    if( y < 6)
        alert("This is not a valid password!");

    else
        alert("Success!");
}

function validate(){
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");
    var y = document.forms.input.password.value;
    
    if(atPos , 1 || dotPos < atPos + 2 || dotPos + 2 > x.length || y < 6)
        alert("This is not a valid email address or password!");
    
    else
        alert("Success!");
        
    
    
    
}
    