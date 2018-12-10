var url=require('url');
var address="http://localhost:8080/default.htm?year=2017&month=february";
var q=url.parse(address,true);
console.log(q.host);
console.log(q.pathname);
console.log(q.search);
var str=url.resolve("/url.js","abc");
console.log(str);
console.log(q.protocol);
console.log(q.auth);
console.log(q.port);
const myURLs = [
    new URL('https://www.example.com'),
    new URL('https://test.example.org')
  ];
  console.log(JSON.stringify(myURLs));
  