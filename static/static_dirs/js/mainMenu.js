/**
 * Created by bogdanmursa on 25/01/15.
 */
var code = '';

function doFirst(){
    var mypic = document.getElementById('logo');
    mypic.addEventListener("dragstart", startDrag, false);
    leftbox = document.getElementById('leftBox');
    window.addEventListener('dragenter', function(e){ e.preventDefault() }, false);
    window.addEventListener('dragover', function(e){ e.preventDefault() }, false);
    window.addEventListener('drop', dropped, false);
}

function startDrag(e){
    code = document.getElementById('rightBox').innerHTML;
}

function dropped(e){
    e.preventDefault();
    leftbox.innerHTML = code;
    document.getElementById('rightBox').innerHTML = '';
}

function restoreDefaults(){
    code = document.getElementById('leftBox').innerHTML;
    document.getElementById('rightBox').innerHTML = code;
    document.getElementById('leftBox').innerHTML = '';
}
window.addEventListener('load', doFirst, false);