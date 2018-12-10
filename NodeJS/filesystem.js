var fs=require('fs');
fs.readFile("demo.txt",function(err,data){
    console.log(data.toString());
});
fs.readdir('./',function(err,data){
    console.log(data);
});

fs.stat("/home/synerzip/Desktop/Practice/NodeJS/demo.txt",function(err,stat){
    console.log(stat);
});