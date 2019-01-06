import React, {Component} from 'react';

class Demo extends Component{

    Fun1 = () =>{
        return <h2>this is function 1</h2>;
    }

    Fun2 = () => {
        return <h2>this is function 2</h2>;
    }

    render(){
        return(
            <div>
                {this.Fun1()}
                {this.Fun2()}
            </div>
        );
    }
}

export default Demo;