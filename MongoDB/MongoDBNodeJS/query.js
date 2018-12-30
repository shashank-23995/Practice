var MongoClient=require('mongodb').MongoClient;
var url="mongodb://localhost:27017";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    var query={name:"mahesh",address:"pune"};
    dbObject.collection("customers").find(query).toArray(function(err,result){
        if(err) throw err;
        console.log(result);
        console.log("printing particular record from result array - "+result[0].name,result[0].address);
        db.close();
    });
});