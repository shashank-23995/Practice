const matrix = require('./matrix');

describe('Testing matrix addition', () => {

    test('if any matrix is undefined, output = undefined', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4]];
        var c, d;
        expect(matrix.addition(c, d)).toEqual(undefined);
    });

    test('if number of rows and columns of matrix are not equal, output = 0', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4], [5, 6]];
        var c, d;
        expect(matrix.addition(a, b)).toEqual(0);
    });

    test('addition = answer', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4]];
        var c, d;
        expect(matrix.addition(a, b)).toEqual([[2, 4], [6, 8]]);
    });

    // test('if any matrix is undefined output = undefined',()=>{
    //     var a=[[1,undefined],[3,4]];
    //     var b=[[1,2],[3,4]];
    //     var c,d;
    //     expect(matrix.addition(a,b)).toEqual([[2,undefined], [6,8]]);
    // });
});

describe('Testing matrix subtraction', () => {

    test('if any matrix is undefined, output = undefined', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4]];
        var c, d;
        expect(matrix.subtraction(c, d)).toEqual(undefined);
    });

    test('if number of rows and columns of matrix are not equal, , output = 0', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4], [5, 6]];
        var c, d;
        expect(matrix.subtraction(a, b)).toEqual(0);
    });

    test('subtraction = answer', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4]];
        var c, d;
        expect(matrix.subtraction(a, b)).toEqual([[0, 0], [0, 0]]);
    });
});

describe('Testing matrix multiplication', () => {
    test('if any matrix is undefined, output = undefined', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4]];
        var c, d;
        expect(matrix.multiplication(c, d)).toEqual(undefined);
    });

    test('if number of rows and columns of matrix are not equal, output = 0', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2, 3], [3, 4, 5]];
        var c, d;
        expect(matrix.multiplication(a, b)).toEqual(0);
    });

    test('multiplication = answer', () => {
        var a = [[1, 2], [3, 4]];
        var b = [[1, 2], [3, 4]];
        var c, d;
        expect(matrix.multiplication(a, b)).toEqual([[7, 10], [15, 22]]);
    });
});