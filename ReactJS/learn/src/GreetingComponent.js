import React, {Component} from 'react'

class GreetingComponent extends Component{
    UserGreeting =props =>{
        return <h2>Welcome back</h2>;
    }

    GuestGreeting = props => {
        return <h2>Sign Up please</h2>;
    }

    Greeting = props => {
        const isLoggedIn=props.isLoggedIn;
        if(isLoggedIn){
            return <this.UserGreeting />
        } else{
            return <this.GuestGreeting />
        }
    }
}

export default GreetingComponent;