var net = require('net');

var HOST = '127.0.0.1';
var PORT = 8881;

// Create a server
//Link the listen function
net.createServer(function(sock) {
    
    console.log('CONNECTED: ' + sock.remoteAddress +':'+ sock.remotePort);
    
    // data event handler
    sock.on('data', function(data) {
        
        console.log('DATA ' + sock.remoteAddress + ': ' + data);
        // Write data back to the socket
        // Client will receive it as data
        sock.write('Hi There ' + data );
        
    });
    
    // close event handler
    sock.on('close', function(data) {
        console.log('CLOSED: ' + sock.remoteAddress +' '+ sock.remotePort);
    });
    
}).listen(PORT, HOST);

console.log('Listening on ' + HOST +':'+ PORT);