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
    var sql="insert into student values(3,'xyz','xyz@gmail.com')";
    con.query(sql,function(err,result){
    if(err) throw err;
    console.log(result);
    });
});