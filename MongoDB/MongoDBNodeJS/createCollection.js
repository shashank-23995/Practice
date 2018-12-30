var MongoClient = require('mongodb').MongoClient;
var url="mongodb://localhost:27017/";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    dbObject.createCollection("customers",function(err,result){
        if(err) throw err;
        console.log("collection created");
        db.close();
    });
});