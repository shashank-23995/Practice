var MongoClient=require('mongodb').MongoClient;
var url="mongodb://localhost:27017/";
MongoClient.connect(url,{ useNewUrlParser: true },function(err,db){
    if(err) throw err;
    var dbObject=db.db("nodePractice");
    var myobj={name:"Company Inc", addresss:"Highway 37"};
    dbObject.collection("customers").insertOne(myobj,function(err,result){
        if(err) throw err;
        console.log("1 document inserted");
        console.log("result"+result);
        db.close();
    });
});