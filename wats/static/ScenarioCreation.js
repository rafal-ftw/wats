function setPossibleSteps(e) {

    var select = document.getElementById(e.target.id);
    var step_container = select.parentElement;
    var current_chosen_option = document.getElementById(e.target.id).value;

    switch (current_chosen_option) {
        case 'go_to_url':

            removeSettings(step_container);
            
            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings'

            var val_input = document.createElement('input');
            val_input.placeholder = 'https://poprawnyadres.com/';

            var emptydiv = document.createElement('div');
            emptydiv.id = 'empty';
            var emptydiv1 = document.createElement('div');
            emptydiv1.id = 'empty';
            
            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint';
            hint.innerHTML = 'BUTTON';
            hint.setAttribute('hover-data', 'Pozwala na przedostanie się na zdefiniowany URL');


            step_container.append(settings);
            settings.append(val_input);
            settings.append(emptydiv);
            settings.append(emptydiv1);
            settings.append(hint);
            break;

        case 'refresh':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = 'ilość (np. 5)';

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Pozwala na odświeżenie strony zdefiniowaną ilość razy');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        case 'back':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = 'ilość (np. 5)';

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Pozwala na cofnięcie do poprzedniej strony zdefiniowaną ilość razy');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        case 'forward':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = 'ilość (np. 5)';

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Pozwala na przejście do następnej strony zdefiniowaną ilość razy');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;    

        case 'wait':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = 'ilość w sekundach (np. 60 - minuta czekania)';

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Pozwala na oczekiwanie danej ilości sekund');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        case 'take_screenshot':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = 'nazwa-zrzutu-ekranu';

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Pozwala na zrobienie zrzutu ekranu okna przeglądarki');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        // element interactions

        case 'click_element':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.placeholder = "XPATH, np. '//*[@value='login']'";

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'pozwala na wysłanie tekstu do elementu (zlokalizowanego za pomocą wartości XPATH)');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;
        
        case 'send_keys_to_element':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = "XPATH, np. '//*[@value='login']'";
            var keys_to_send = document.createElement('input');
            keys_to_send.placeholder = 'wartość tekstowa do wyslania';

            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'pozwala na wysłanie tekstu do elementu (zlokalizowanego za pomocą wartości XPATH)');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(keys_to_send);
            settings.append(hint);
            break;

        case 'clear_element':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.defaultValue = "XPATH, np. '//*[@value='login']'";
            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Czyści element (np. input) z tekstu)');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        case 'choose_from_list':
            removeSettings(step_container);

            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var locator = document.createElement('input');
            locator.placeholder = "XPATH, np. '//*[@value='login']'";
            
            var type = document.createElement('input');
            type.placeholder = "index/value/text";

            var values = document.createElement('input');
            values.placeholder = "wartosci,dzielone,przecinkiem";


            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'pozwala na wybór jednego lub więcej elementów z listy');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(locator);
            settings.append(type);
            settings.append(values);
            settings.append(hint);
            break;

        case 'click_enter':
            removeSettings(step_container)
            
            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings_clickenter';
            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'naciska przycisk enter (przydatne przy submitach)');
            hint.innerHTML = 'BUTTON';
            step_container.append(settings);
            settings.append(hint);
            break;

            // asserts
        case 'assert_title_has':
            removeSettings(step_container)
            
            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.placeholder = "np. WATS | Scenario Creator";
            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Potwierdza, czy tytuł strony to zawiera podany ciag znakow');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        case 'assert_title_is':
            removeSettings(step_container)
            
            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.placeholder = "np. WATS | Scenario Creator";
            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Potwierdza, czy tytuł strony to podany ciag znakow');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;
        case 'assert_element_exist':
            removeSettings(step_container)
            
            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var val_input = document.createElement('input');
            val_input.placeholder = "XPATH";
            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'Potwierdza, czy na stronie znajduje się element którego XPATH zdefiniowaliśmy');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(val_input);
            settings.append(hint);
            break;

        case 'assert_element_contains_string':
            removeSettings(step_container)
            
            var settings = document.createElement('div');
            settings.id = 'settings';
            settings.className = 'scenario-creation-step-settings';

            var locator = document.createElement('input');
            locator.placeholder = "XPATH";

            var val_input = document.createElement('input');
            val_input.placeholder = "jakas wartosc";
            
            var hint = document.createElement('div');
            hint.id = e.target.id + '-hint';
            hint.className = 'hint'
            hint.setAttribute('hover-data', 'otwierdza najpierw czy element którego XPATH zdefiniowaliśmy istnieje, a potem czy zawiera podaną wartość tekstową');
            hint.innerHTML = 'BUTTON';

            step_container.append(settings);
            settings.append(locator);
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