function sendToExecution() {

    var elements = Array.from(document.getElementsByClassName('scenario-list-item'));


    for (const c in elements) {
        console.log(elements[c].childNodes[1])
        
        console.log(elements[c].childNodes[3].getAttribute('data'))

        // python maybe?
    }
}