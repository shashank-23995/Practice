const factors = require('./PrimeFactors');

describe('testing prime factors of the number',() => {
    test('expected null but received []',() => {
        expect(factors.findFactor(1)).toBe(null);
    });

    test('expected [2] but received []',() => {
        expect(factors.findFactor(2)).toEqual(factors.getFactors(2));
    });

    test('expected [2] but received []',() => {
        expect(factors.findFactor(2)).toEqual(factors.getFactors(2));
    });

    test('expected [3] but received [2]',() => {
        expect(factors.findFactor(3)).toEqual(factors.getFactors(3));
    });

    test('expected [2, 2] but received [4]',() => {
        expect(factors.findFactor(4)).toEqual(factors.getFactors(2, 2));
    });

    test('expected [2, 2, 2] but received [2, 4]',() => {
        expect(factors.findFactor(8)).toEqual(factors.getFactors(2, 2, 2));
    });

    test('expected [3, 3] but received [9]',() => {
        expect(factors.findFactor(9)).toEqual(factors.getFactors(3, 3));
    });

    test('expected [3, 3, 3] but received [3, 3, 9]',() => {
        expect(factors.findFactor(27)).toEqual(factors.getFactors(3, 3, 3));
    });
});
