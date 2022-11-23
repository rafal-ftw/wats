function setPossibleSteps(e) {

    var select = document.getElementById(e.target.id);
    var step_container = select.parentElement;
    var current_chosen_option = document.getElementById(e.target.id).value;

    switch (current_chosen_option) {
        case 'go_to_url':

            removeSettings(step_container);
            var settings = document.createElement('div');
            settings.id = 'settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = 'https://poprawnyadres.com/';

            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint';
            hint.innerHTML = 'sprawdź podpowiedź!';
            hint.setAttribute('hover-data', 'Pozwala na przedostanie się na zdefiniowany URL');

            step_container.className = 'scenario-creation-step-changed';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        case 'refresh':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = 'ilość (np. 5)';

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Pozwala na odświeżenie strony zdefiniowaną ilość razy');
            hint.innerHTML = 'sprawdz mnie!';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;


    }

}

function removeSettings(parent) {
    var child_elems = parent.children;

    if (child_elems.length > 1){
        if (child_elems[1].id == 'settings'){
        parent.removeChild(child_elems[1])}
        }
     else {
        console.log('no tag with id settings')
    }

}
