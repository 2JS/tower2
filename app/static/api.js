function update() {
    get('heater');
    get('extruder');
    get('fiber')
}

function get(device) {
    const req = new Request('/api/' + device, {method:'GET'});
    fetch(req)
        .then(response => {
            if (response.status === 200) {
                return response.json()
            }
        }).then(response => {
            value = response['value']
            if (device == 'heater') {
                heaterinput.value = value;
            } else if (device == 'extruder') {
                extruderinput.value = value;
            } else if (device == 'fiber') {
                fiberinput.value = value;
            }
        }).catch(error => {
            console.error(error);
        })
}

// function getheater() {
//     return 
// }

function set(device) {
    value = document.getElementById(device + '-input').value;
    var formData = new FormData();
    formData.append('value', value);
    const req = new Request('/api/' + device, {method: 'POST', body: formData});
    fetch(req)
        .catch(error => console.error(error))
}

function inc(device, inc=true) {
    // increase value of given device
    input = document.getElementById(device + '-input')
    input.value = parseFloat(input.value) + (inc ? 1 : -1);
    set(device);
}

function stopAll() {
    heaterinput.value = 0;
    set('heater');
    extruderinput.value = 0;
    set('extruder');
    fiberinput.value = 0;
    set('fiber');
}

function authorize(username, auth) {
    var formData = new FormData();
    formData.append('username', username);
    formData.append('authorize', auth)
    const req = new Request('/users', { method: 'POST', body: formData });
    fetch(req)
        .catch(error => console.error(error))
}

document.addEventListener("DOMContentLoaded", () => {
    heaterinput = document.getElementById('heater-input');
    extruderinput = document.getElementById('extruder-input');
    fiberinput = document.getElementById('fiber-input');
    update();
})