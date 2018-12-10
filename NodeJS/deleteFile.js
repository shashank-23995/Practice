var fs=require('fs');
fs.unlink('demo3.txt',(err)=>{
    if(err){
        //console.log("printing exception="+err);
        throw err;
    }
    console.log("successfully deleted file");
});


// synchronous way
// const fs = require('fs');

// try {
//   fs.unlinkSync('/tmp/hello');
//   console.log('successfully deleted /tmp/hello');
// } catch (err) {
//   // handle the error
//   console.log("file not found");
// }