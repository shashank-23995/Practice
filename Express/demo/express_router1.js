const express=require('express')
const app=express()
const port=3000
var birds = require('./birds')

app.use('/birds',birds)

app.listen(port,()=>console.log(`app listening on port ${port}!`))