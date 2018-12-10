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
    var sql="create table college(cno int primary key,cname varchar(30),sno int references student(sno))";
     con.query(sql,function(err,result){
        if(err) throw err;
        console.log('table created');
     });
});