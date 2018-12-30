var MongoClient=require('mongodb').MongoClient;
var url="mongodb://localhost:27017";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    var query={address:'Mountain 21'};
    dbObject.collection("customers").deleteOne(query,function(err,result){
        if(err) throw err;
        console.log("1 document is deleted");
        console.log(result);
        db.close();
    });
});