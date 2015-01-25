/**
 * Created by bogdanmursa on 25/01/15.
 */

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}

function restoreDefaults(ev){
    code = document.getElementById('leftBox').innerHTML;
    document.getElementById('rightBox').innerHTML = code;
    document.getElementById('leftBox').innerHTML = '';
}
