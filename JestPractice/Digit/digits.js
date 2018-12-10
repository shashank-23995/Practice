const list_digit=(number)=>{
    if(number==undefined){
        return undefined;
    }else if(isNaN(number)){
        return undefined;
    }
    
    
    var output = [],
    sNumber = number.toString();

for (var i = 0, len = sNumber.length; i < len; i += 1) {
    output.push(+sNumber.charAt(i));
}   
    return output;
}

module.exports={list_digit};