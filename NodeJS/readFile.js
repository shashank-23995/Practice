var fs=require('fs');
var readLine=require('readline');
var myInterface=readLine.createInterface(
    {
        input:fs.createReadStream("demo.txt")
    }
);
var line_count=0
myInterface.on('line',function(line){
    line_count++;
    console.log("line number "+line_count+": "+line);
})