// include http module in the file
var http = require('http'); 
 
// create a server
http.createServer(OnReq).listen(8083); //WebApp81 listens on port 8083
// print message to console
console.log('WebApp82 running at http://127.0.0.1:8083/');

function OnReq(req, res){
    // http header with OK message(200)
    res.writeHead(200, {'Content-Type': 'text/html'});  
    res.write('Appa says Hi There!'); //response to the client
    res.end(); //end response
}


