// const s1 = 'Hello';
// console.log("s1 = ",typeof s1);
// const s2 = new String('Hello');
// console.log("s2 = ",typeof s2);
// console.log(window);
// console.log(navigator.appVersion);

const book1 = {
    title: 'Book One',
    author: 'John Doe',
    year: '2013',
    getSummary: function(){
        return `${this.title} was written by ${this.author} in ${this.year}`;
    }
};

console.log(book1);
console.log(book1.title);
console.log(book1.author);
console.log(book1.year);
console.log(book1.getSummary());

const book2 = {
    title: 'Book Two',
    author: 'Jane Doe',
    year: '2016',
    getSummary: function(){
        return `${this.title} was written by ${this.author} in ${this.year}`;
    }
};

console.log("object keys ",Object.keys(book2));
console.log("object keys ",Object.values(book2));