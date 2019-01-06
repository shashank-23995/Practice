const findFactors=(number)=>{
    let pf=[];
    if(number==1){
        return null;
    }
    let fact=2;
    if(number>1){
        while(number>=fact){
            if(number%fact==0){
                number=number/fact;
                pf.push(fact);
            } else {
                fact++;
            }
        }        
    }
   
    return pf;
}

const getFactors=(...number)=>{
    let nf=[];
    for(let n of number)
        nf.push(n);
    return nf;
}

module.exports={findFactors,getFactors};