const digit=require('./digits');

describe('Returning digits from number',()=>{
    test('if number is undefined, return undefined',()=>{
        expect(digit.list_digit(undefined)).toEqual(undefined);
    });

    test('if input not number return undefined',()=>{
        expect(digit.list_digit("stirng")).toEqual(undefined);
    });

    test('if number is 0 return 0',()=>{
        expect(digit.list_digit(0)).toEqual([0]);
    });

    test('if number is 123 return [1,2,3]',()=>{
        expect(digit.list_digit(123)).toEqual([1,2,3]);
    });
});