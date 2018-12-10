// var fs=require('fs');
// fs.appendFile("demo3.txt","new content",function(err){
//     console.log('saved');
// })

var fs=require('fs');
fs.open("demo3.txt","a",function(err,file_data){
    if(err) throw err;
    fs.appendFile(file_data,"data to append",function(err){
        fs.close(file_data,function(err){
            if(err) throw err;
        });
        if(err) throw err;
    });
});