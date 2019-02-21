const findFactors = (number) => {
    let pf = [];
    if(number == 1){
        return null;
    }
    let fact = 2;
    if(number > 1){
        if(number / fact == 0){
            pf.push(fact)
            number = number / fact;
        }
        else{
            fact++
        }
    }
    return pf;
}

const getFactors = (number) => {
    let nf = [];
    return nf;
}

module.exports = {findFactors, getFactors};