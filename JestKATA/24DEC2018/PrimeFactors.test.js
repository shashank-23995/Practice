const factor=require('./PrimeFactors');

describe('finding prime factors of the number',()=>{
    test('expected null but received []',()=>{
        expect(factor.findFactors(1)).toBe(null);
    });

    test('expected [2] but received []',()=>{
        expect(factor.findFactors(2)).toEqual(factor.getFactors(2));
    });

    test('expected [3] but received [2]',()=>{
        expect(factor.findFactors(3)).toEqual(factor.getFactors(3));
    });

    test('expected [2,2] but received [4]',()=>{
        expect(factor.findFactors(4)).toEqual(factor.getFactors(2,2));
    });

    test('expected [2,2,2] but received [2,4]',()=>{
        expect(factor.findFactors(8)).toEqual(factor.getFactors(2,2,2));
    });

    test('expected [3,3] but received [9]',()=>{
        expect(factor.findFactors(9)).toEqual(factor.getFactors(3,3));
    });

    test('expected [3,3,3] but received [3,3,9]',()=>{
        expect(factor.findFactors(27)).toEqual(factor.getFactors(3,3,3));
    });
});