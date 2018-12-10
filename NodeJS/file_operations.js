var fs=require('fs');
fs.open("/home/synerzip/Desktop/Practice/NodeJS/demo.txt","r",function(err,file_data){
    if(err) throw err;
    
    console.log("printing file data -"+file_data);
    fs.close(file_data,function(err){
        if(err) throw err;
    });
});