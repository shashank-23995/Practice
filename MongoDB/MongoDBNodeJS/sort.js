var MongoClient=require('mongodb').MongoClient;
var url="mongodb://localhost:27017";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    // ascending = 1, descending = -1
    dbObject.collection("customers").find().sort({name:1}).toArray(function(err,result){
        if(err) throw err;
        console.log(result);
        db.close();
    });
});