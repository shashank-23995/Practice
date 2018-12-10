const calculator=require('./calculator');

// afterEach(()=>{
//     console.log("executing afterEach() method");
// });


describe('Testing add() method',()=>{
    
    test('adds 1+2 to equal 3',()=>{
        expect(calculator.add(1,2)).toBe(3);
    });

    test('adds 2 + undefined to equal 2',()=>{
        expect(calculator.add(2,undefined)).toBe(2);
    })

});

describe('Testing sub() method',()=>{

    test('subtracts 2-1 to equal',()=>{
        expect(calculator.sub(2,1)).toBe(1);
    });
});

describe('Testing if number is in given range',()=>{
    expect.extend({
        toBeWithinRange(received,floor,ceiling){
            const pass=received>=floor && received<=ceiling;
            if(pass){
                return {
                    message: () =>
                      `expected ${received} not to be within range ${floor} - ${ceiling}`,
                    pass: true,
                  };
            } else{
                return {
                    message: () =>
                    `expected ${received} to be within range ${floor} - ${ceiling}`,
                    pass: false,
                };
            }
        },
    });

    test('numeric ranges',()=>{
        expect(100).toBeWithinRange(90,110);
    });
});

describe('checking parameter for null/undefined',()=>{
    
    test('testing input',()=>{
        expect(calculator.checkInput(2)).toEqual(expect.anything());
    });

    test.skip('validating random number',()=>{
        const mock=jest.fn();
        calculator.randocall(mock);
        expect(mock).toBeCalledWith(expect.any(34));
    });
});

describe('comparing arrays',()=>{

    test('comparing string arrays',()=>{
        const expected_array=['a','b','c'];
        expect(['a','b','c']).toEqual(expect.arrayContaining(expected_array));
    });

    test('comparing string arrays to be not equal',()=>{
        const expected_array=['a','b','c'];
        expect(['a','b','d']).toEqual(expect.not.arrayContaining(expected_array));
    });

    test.skip('doAsync calls both callbacks', () => {
        expect.assertions(2);

        function callback1(data) {
          expect(data).toBeTruthy();
        }
        function callback2(data) {
          expect(data).toBeTruthy();
        }
        doAsync(callback1, callback2);
    });

});

describe('string matching',()=>{
    test('matching strings for equality',()=>{
        expect('hello world').toEqual(expect.stringMatching('hello world'));
    });

    test('matching strings for non equality',()=>{
        expect('hello world').toEqual(expect.not.stringMatching('hi'));
    });
});