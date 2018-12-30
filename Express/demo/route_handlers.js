const express=require('express')
const app=express()
const port=3000

app.get('/',function(re,res){
    res.send("Hello")
})

app.get('/example/a', function (req, res) {
    res.send('Hello from A!')
  })

app.get('/example/b',function(req,res,next){
    console.log("the response will be sent by the next function...")
    next()
},function(req,res){
    res.send("Hello from b")
})

var cb0=function(req,res,next){
    console.log("cb0")
    next();
}

var cb1=function(req,res,next){
    console.log("cb1")
    next();
}

var cb2=function(req,res){
    console.log("cb2")
    res.send("Hello from c")
}

app.get('/example/c',[cb0, cb1, cb2])
app.listen(port,()=>console.log(`app listening on port ${port}!`))