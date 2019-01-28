const factors=require('./PrimeFactors');

describe('testing prime factors of the number',()=>{
    
    test('expected null but returned []',()=>{
        expect(factors.findFactors(1)).toBe(null);
    });

    test('expected [2] but returned []',()=>{
        expect(factors.findFactors(2)).toEqual(factors.getFactors(2));
    });

    test('expected [3] but returned [2]',()=>{
        expect(factors.findFactors(3)).toEqual(factors.getFactors(3));
    });

    test('expected [2,2] but returned [4]',()=>{
        expect(factors.findFactors(4)).toEqual(factors.getFactors(2,2));
    });

    test('expected [2,2,2] but returned [2,4]',()=>{
        expect(factors.findFactors(8)).toEqual(factors.getFactors(2,2,2));
    });

    test('expected [3,3] but returned [9]',()=>{
        expect(factors.findFactors(9)).toEqual(factors.getFactors(3,3));
    });

    test('expected [3,3,3] but returned [3,3,9]',()=>{
        expect(factors.findFactors(27)).toEqual(factors.getFactors(3,3,3));
    });
});