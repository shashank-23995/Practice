import React, { Component } from 'react';

class JSXDemo extends Component{

    const name='shashank'
const element=<h1>hello {name}</h1>

function formatName(user) {
    return user.firstName+' '+user.lastName;
}

    function getGreeting(user) {
        if (user) {
            return <h1>Hello, {formatName(user)}!</h1>;
        }
        return <h1>Hello, Stranger.</h1>;
    }
    
    const user = {
        firstName: 'Haper',
        lastName: 'Perez'
    };
    
    const element2 = (
        <h1>
      Hello, {formatName(user)}!
    </h1>
  );
  
  const greeting = (
      <h1>
      {getGreeting(user)}!
    </h1>
  );
}

export default JSXDemo;