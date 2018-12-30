var MongoClinet=require('mongodb').MongoClient;
var url="mongodb://localhost:27017";
MongoClinet.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    var query={address:/^P/};
    dbObject.collection("customers").find(query).toArray(function(err,result){
        console.log(result);
        db.close();
    });
});