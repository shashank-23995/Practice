var express = require('express');  
var app = express();
const port=3000

// app.get('/user/:id',function(req,res,next){
//     console.log('ID:',req.params.id);
//     next()
// },function(req,res,next){
//     res.send("User Info")
// })

// app.get('user/:id',function(req,res,next){
//     res.send(res.params.id)
// })

app.get('/user/:id',function(req,res,next){
    if(req.params.id==0)
        next('route')
    else
        next()
},function(req,res,next){
    res.send('regular')
})

app.get('/user/:id',function(req,res,next){
    res.send('special')
})
app.listen(port,()=>console.log(`app listening on port ${port}!`))