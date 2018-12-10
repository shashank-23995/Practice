const findFactors=(number)=>{
    pf=[];
    if(number==1){
        return null;
    }
    fact=2;
    if(number>1){
        while(number>=fact){
            if(number%fact==0){
                pf.push(fact);
                number=number/fact;
            }
            else{
                fact++;
            }
        }
    }
    return pf;
}

const getFactors=(...number)=>{
    nf=[];
    for (const n of number) {
        nf.push(n);
    }
    return nf;
}

module.exports={findFactors,getFactors};