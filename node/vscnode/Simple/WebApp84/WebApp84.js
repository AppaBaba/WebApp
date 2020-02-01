
var http = require('http'); // include http module
var url = require('url');   // include url module
 
// create a server
http.createServer(OnReq).listen(8084); //WebApp84 listens on port 8084
// print message to console
console.log('WebApp84 running at http://127.0.0.1:8084/');

function OnReq(req, res){
    var pn = url.parse(req.url).pathname;
    console.log('pathname ' + pn);
    displayPage(res, pn);
}

function displayPage(res, pn){
    // http header with OK message(200)
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(PageMap['/']); 
    res.write('Appa says Hi There!'); //response to the client
    res.end(); //end response
}

var PageMap = {
  '/' : '<h1>AppaBaba Home Page</h1>',
  '/me' : '<h1>It me again AppaBaba</h1>'
}