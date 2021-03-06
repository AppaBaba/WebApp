var net = require('net');

var HOST = '127.0.0.1';
var PORT = 8881;

var client = new net.Socket();

client.connect(PORT, HOST, function() {

    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
    // Write a message to the socket
    client.write('Appa Baba');

});

// data event handler for the client socket
// data is what the server sent to this socket
client.on('data', function(data) {
    
    console.log('DATA: ' + data);
    // Close the client socket completely
    client.destroy();
    
});

// close event handler for the client socket
client.on('close', function() {
    console.log('Connection closed');
});