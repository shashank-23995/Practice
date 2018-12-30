const express=require('express');
const app=express();
const port=3000

app.set('view engine', 'pug');
app.set('views','./views');

app.get('/first_template', function(req, res){
    res.render('first_view');
 });

 app.get('/dynamic', function(req, res){
    res.render('dynamic_view', {
       name: "TutorialsPoint", 
       url:"http://www.tutorialspoint.com"
    });
 });

 app.get('/components',function(req,res){
     res.render('components',{
     user: {name: "Ayush", age: "20"}
     })
 })

 app.listen(3000,()=>{console.log(`server connected to port ${port}`)})