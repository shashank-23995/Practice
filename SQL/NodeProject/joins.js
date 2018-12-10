var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "synerzip",
  database: "practiceDB"
});

con.connect(function(err){
    if(err) throw err;
    console.log('connected');
    var normal_join="";
});