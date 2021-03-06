const factors = require('./PrimeFactors');

describe('finding prime factors of the number', () => {

    test('expected [null] but was []', () => {
        expect(factors.findFactors(1)).toBe(null);
    });

    test('expected [2] but was []', () => {
        expect(factors.findFactors(2)).toEqual(factors.getFactors(2));
    });

    test('expected [3] but was [2]', () => {
        expect(factors.findFactors(3)).toEqual(factors.getFactors(3));
    });

    test('expected [2,2] but was [4]', () => {
        expect(factors.findFactors(4)).toEqual(factors.getFactors(2, 2));
    });

    test('expected [2,2,2] but was [8]', () => {
        expect(factors.findFactors(8)).toEqual(factors.getFactors(2, 2, 2));
    });

    test('expected [3,3] but was [9]', () => {
        expect(factors.findFactors(9)).toEqual(factors.getFactors(3, 3));
    });

    test('expected [3,3,3] but was [27]', () => {
        expect(factors.findFactors(27)).toEqual(factors.getFactors(3, 3, 3));
    });
});