const factor=require('./PrimeFactors');

describe('testing prime factors of a number',()=>{
    test('expected null but was []',()=>{
        expect(factor.findFactors(1)).toBe(null);
    });

    test('expected [2] but was []',()=>{
        expect(factor.findFactors(2)).toEqual(factor.getFactors(2));
    });

    test('expected [3] but was [2]',()=>{
        expect(factor.findFactors(3)).toEqual(factor.getFactors(3));
    });

    test('expected [2,2] but was [4]',()=>{
        expect(factor.findFactors(4)).toEqual(factor.getFactors(2,2));
    });

    test('expected [2,2,2] but was [8]',()=>{
        expect(factor.findFactors(8)).toEqual(factor.getFactors(2,2,2));
    });

    test('expected [3,3] but was [9]',()=>{
        expect(factor.findFactors(9)).toEqual(factor.getFactors(3,3));
    });

    test('expected [3,3,3] but was [3,3,9]',()=>{
        expect(factor.findFactors(27)).toEqual(factor.getFactors(3,3,3));
    });
});