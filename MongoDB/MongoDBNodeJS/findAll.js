var MongoClinet=require('mongodb').MongoClient;
url="mongodb://localhost:27017";
MongoClinet.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    dbObject.collection("customers").find({}).toArray(function(err,result){
        if(err) throw err;
        console.log(result);
        db.close();
    });
});