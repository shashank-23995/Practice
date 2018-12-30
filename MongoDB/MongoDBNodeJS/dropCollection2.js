var MongoClient=require('mongodb').MongoClient;
var url="mongodb://localhost:27017";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    dbObject.dropCollection("employee",function(err,result){
        if(err) throw err;
        if(result)
            console.log("collection is deleted");
        console.log(result);
        db.close();
    });
});