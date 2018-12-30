const express=require('express')
const bodyParser=require('body-parser')
const app=express()
const PORT=3000

app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json())

app.get('/index.html',function(req,res){
    res.sendFile("/"+"index.html")
})

app.post('/user', function(req,res){
    response={
        first_name:req.body.first_name,
        last_name:req.body.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
});

var server = app.listen(PORT, function(){
    var host = server.address().address;
    var port = server.address().port;
    console.log("Example app listening at http://%s:%s", host, port);
});