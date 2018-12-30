var MongoClient=require('mongodb').MongoClient;
var url="mongodb://localhost:27017/";
MongoClient.connect(url,{useNewUrlParser:true},function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    var myobj=[
        {name:"abc", address:"pune"},
        {name:"pqr", address:"mumbai"},
        {name:"xyz", address:"nagpur"}
    ];
    dbObject.collection("customers").insertMany(myobj,function(err,result){
        if(err) throw err;
        console.log("multiple documents inserted");
        console.log(result);
        console.log("number of documents inserted - "+result.insertedCount);
        console.log(result.insertedIds);
        db.close();
    });
});