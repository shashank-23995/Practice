var MongoClient=require('mongodb').MongoClient;
var url="mongodb://localhost:27017";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    dbObject.collection("customers").find({},{projection:{_id:0,name:1,address:1}}).toArray(function(err,result){
        if(err) throw err;
        console.log(result);
        console.log("printing particular field from result array - "+result[2].address);
        db.close();
    });
})