const express=require('express')
const app=express()
const router=express.Router()
const port=3000

router.use(function(req,res,next){
    console.log('time',Date.now())
    next()
})

router.use('/user/:id',function(req,res,next){
    console.log('request url',req.originalUrl)
    next()
},function(req,res,next){
    console.log('request type',req.method)   
})

router.use('/user/:id',function(req,res,next){
    if(req.params.id==0)
        next('route')
    else
        next()
},function(req,res,next){
    res.render('regular')
})

router.use('user/:id',function(req,res,next){
    console.log(req.params.id)
    res.render('special')
})

app.listen(port,()=>console.log(`app listening on port ${port}!`))