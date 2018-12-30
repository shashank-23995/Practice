const express=require('express')
const app=express()
const PORT=3000;
const bodyParser=require('body-parser')
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

app.post('/api/users', function(req, res) {
    var user_id = req.body.id;
    var token = req.body.token;
    var geo = req.body.geo;

    res.send(user_id + ' ' + token + ' ' + geo);
});
app.listen(PORT,()=>{console.log('server is running on port :',PORT)})