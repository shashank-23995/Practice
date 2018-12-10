const addition = (a, b) => {
    if (a == undefined || b == undefined) {
        return undefined;
    }

    if (a.length == b.length) {
        for (let i = 0; i < a.length && i < b.length; i++) {
            if (a[i].length != b[i].length) {
                return 0;
            }
        }
    } else {
        return 0;
    }

    var output = [];

    for (let i = 0; i < a.length; i++) {
        output[i] = [];
        for (let j = 0; j < a[i].length; j++) {
            // if(a[i][j]==undefined || b[i][j]==undefined){
            //     output[i][j]=undefined;
            // }else
            output[i][j] = a[i][j] + b[i][j];
        }
    }

    return output;
}

const subtraction = (a, b) => {
    if (a == undefined || b == undefined) {
        return undefined;
    }

    if (a.length == b.length) {
        for (let i = 0; i < a.length && i < b.length; i++) {
            if (a[i].length != b[i].length) {
                return 0;
            }
        }
    } else {
        return 0;
    }

    var output = [];

    for (let i = 0; i < a.length; i++) {
        output[i] = [];
        for (let j = 0; j < a[i].length; j++) {
            // if(a[i][j]==undefined || b[i][j]==undefined){
            //     output[i][j]=undefined;
            // }else
            output[i][j] = a[i][j] - b[i][j];
        }
    }

    return output;
}

const multiplication = (a, b) => {
    if (a == undefined || b == undefined) {
        return undefined;
    }

    console.log('rows = ' + a.length);
    console.log('columns = ' + b[0].length);
    if (a.length != b[0].length) {
        return 0;
    }

    var output = [];
    for (let i = 0; i < a.length; i++) {
        output[i] = [];
        for (let j = 0; j < b[0].length; j++) {
            for (let k = 0; k < b[0].length; k++) {
                output[i][j] = output[i][j] + a[i][k] * b[k][j];
            }
            console.log('value =' + output[i][j]);
        }
    }
    return output;
}
module.exports = { addition, subtraction, multiplication };