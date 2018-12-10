const findFactors=(number)=>{
    let pf=[];
    if (number==1) {

        pf.push(null);
    }
    var fact=2;
    if(number > 1) {
        while(number>=fact){
            if (number%fact==0) {
                pf.push(fact);
                number=number/fact;
            } else {
                fact++;
            }
        }
    }
    return pf;
}

const getFactors=(...number)=>{
    let nf=[];
    for (const i of number) {
        nf.push(i);
    }
    return nf;
}
module.exports={findFactors,getFactors};