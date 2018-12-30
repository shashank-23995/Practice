var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');

var app = express();

var logger=function(req,res,next){
    console.log('logging');
    next();
}

app.get(logger);

//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({urlencoded:false}));

//set static path
app.use(express.static(path.join(__dirname,'public')));

var person = [
    {
        name:'shashank',
        age: 23
    },
    {
        name:'abc',
        age:30
    }

]

app.get('/',function(req,res){
    res.json(person);
})

app.listen(3000,()=>{console.log('server started at port 3000')});