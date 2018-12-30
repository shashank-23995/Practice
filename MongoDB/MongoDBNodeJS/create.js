var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/nodePractice";

MongoClient.connect(url,{useNewUrlParser:true}, function(err, db) {
  if (err) throw err;
  console.log("Database created!");
  db.close();
});