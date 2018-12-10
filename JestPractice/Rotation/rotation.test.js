const f=require('./rotation');
describe('Rotation of list by k elements',()=>{
    test('rotation of list if k=1',()=>{
        let a=[1,2,3,4,5,6];
        expect(f.rotate(a,1)).toEqual([6,5,4,3,2,1]);
    });

    test('rotation of list if k > length of list ',()=>{
        let a=[1,2,3,4,5,6];
        expect(f.rotate(a,7)).toEqual([1,2,3,4,5,6]);
    });

    test('rotation of list if k=3 ',()=>{
        let a=[1,2,3,4,5,6];
        expect(f.rotate(a,3)).toEqual([4,5,6,1,2,3]);
    });
});