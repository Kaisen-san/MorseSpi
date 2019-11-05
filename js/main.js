const client = new Paho.MQTT.Client('test.mosquitto.org', 8080, 'NodeBR');

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({
    onSuccess: onConnect
});


const $form = document.getElementById('messageForm');

$form.addEventListener('submit', evt => {
    evt.preventDefault();
    const $message = document.getElementById('message');
    sendMessage($message.value.toUpperCase());
    $message.value = '';
});

function onConnect() {
    console.log('onConnect');
    client.subscribe('NodeJS');
}

function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log('onConnectionLost:' + responseObject.errorMessage);
    }
}

function onMessageArrived(message) {
    const payload = message.payloadString;
    console.log(`onMessageArrived: ${payload}`);
}

function sendMessage(msg) {
    const message = new Paho.MQTT.Message(msg);
    message.destinationName = 'NodeJS';
    client.send(message);
}

