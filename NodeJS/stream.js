var fs=require('fs');
var data="";
var rstream=fs.createReadStream("demo.txt");
rstream.on('data',function(chunk){
    //console.log(chunk.toString());
    data+=chunk;
});

rstream.on('end',function(){
    console.log(data);
});

rstream.on('err',function(){
    console.log(err);
});
