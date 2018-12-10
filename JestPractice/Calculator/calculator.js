const add=(a,b)=>{
    if(b==undefined){
        return a;
    }
    return a+b;
};
const sub=(a,b)=>{return a-b};
const mult=(a,b)=>{return a*b};
const div=(a,b)=>{return a/b};
const checkInput=(a)=>{return a};

function randocall(fn) {
    return fn(Math.floor(Math.random()*6+1));
}

module.exports={add, sub, mult, div, checkInput, randocall};