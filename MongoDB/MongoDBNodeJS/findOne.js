var MongoClient=require('mongodb');
var url="mongodb://localhost:27017";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    dbObject.collection("customers").findOne({name:"shashank"},function(err,result){
        if(err) throw err;
        console.log(result._id);
        console.log(result.name);
        console.log(result.address);
        console.log(result);
        db.close();
    });
});