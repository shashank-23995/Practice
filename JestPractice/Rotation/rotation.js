const rotate=(numbers,k)=>{
    //list=numbers;
    if(k==1){
        numbers.reverse();
        return numbers;
    } else if(k>numbers.length){
        return numbers;
    }
    console.log('k='+k);
        var temp=[];
        for(let i=0,j=k;i<k;i++){
             temp[i]=numbers.pop();
           // console.log(numbers+"--->"+i+"--->"+temp);
            //numbers.shift(temp);
           // console.log("in for loop"+numbers);
        }
        for(let i=0;i<k;i++){
            numbers.unshift(temp[i]);
        }
        //numbers.splice(0,0,temp);
        
        //numbers.unshift(temp)
       // console.log("outside loop"+numbers);
    return numbers;   
};

module.exports={rotate};