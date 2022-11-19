
var nextId = 0;
let container = document.getElementById('step');
let arr = ["---","idz tu", "idz tam", "volvo"] ;

function addLabel() {
    var d = document.createElement("select");
    d.id = "step" + nextId;
    d.onclick = addLabel;
    for (let i = 0; i < arr.length; i++){
        let opt = document.createElement('option');
        opt.value = arr[i];
        opt.innerHTML = arr[i];
        d.appendChild(opt);
    }
    container.appendChild(d);
    nextId += 1;
}

addLabel();