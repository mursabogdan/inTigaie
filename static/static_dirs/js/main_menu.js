/**
 * Created by bogdanmursa on 25/01/15.
 */

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    var ingredient = ev.target.id;
    ev.dataTransfer.setData("text", ingredient);
    ev.dataTransfer.setDragImage(document.getElementById(ingredient),0,0);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var code = document.getElementById(data).src;
    ev.target.appendChild(document.getElementById(data));

    var img = document.createElement("IMG");
    img.setAttribute("id", data);
    img.setAttribute("class", 'ingredientsPanel');
    img.setAttribute("src", code);
    img.setAttribute("width", "70");
    img.setAttribute("width", "70");
    img.setAttribute("draggable", "false");
    img.setAttribute("ondblclick", "restoreDefaults('"+ data +"')")
    document.getElementById('ingredientsPanel').appendChild(img);
}

function restoreDefaults(id) {
    var code = document.getElementById(id).src;

    var img = document.createElement("IMG");
    img.setAttribute("id", id);
    img.setAttribute("class", 'ingredients');
    img.setAttribute("draggable", "true");
    img.setAttribute("ondragstart", "drag(event)");
    img.setAttribute("src", code);
    img.setAttribute("width", "70");
    img.setAttribute("width", "70");

    var elements = document.getElementById("ingredientsPanel").getElementsByClassName("ingredientsPanel");
    var panel = document.getElementById("ingredientsPanel");
    for(var i=0; i<elements.length; i++) {
        if(elements[i].id == id ){
            panel.removeChild(elements[i]);
        }
    }

    document.getElementById('leftBox').appendChild(img);
}
