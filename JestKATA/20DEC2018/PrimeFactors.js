
const findFactors=(number)=>{
    let pf=[];
    if(number==1){
        return null;
    }
    pf.push(number);
    return pf;
};

const getFactors=(...number)=>{
    let nf=[];
    for (let n of number) {
        nf.push(n);
    }
    nf.push(number);
    return nf;
}

module.exports={findFactors,getFactors};