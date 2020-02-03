var page = require('./page');

function PageDisp(res, pn){
  if(page.PageMap[pn]){
    // http header with OK message(200)
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(page.PageMap[pn]); 
    res.write('Appa says Hi There!'); //response to the client
    res.end(); //end response
  }else {
    res.writeHead(404, {'Content-Type': 'text/html'});
    res.write('404 Page Not Found');
    res.end();
  }
}

exports.PageDisp = PageDisp;