const findFactors=(number)=>{
    let pf=[];
    if(number==1){
        return null;
    }
    if(number>1){
        let fact=2;
        while(number>=fact){
            if(number%fact==0){
                pf.push(fact);
                number=number/fact;
            } else{
                fact++;
            }
        }
    }
    return pf;
}

const getFactors=(...number)=>{
    let nf=[];
    for(let n of number){
        nf.push(n);
    }
    return nf;
}

module.exports={findFactors,getFactors};