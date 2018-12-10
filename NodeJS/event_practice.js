var events=require('events');
var eventEmitter=new events.EventEmitter();

var eventHandler=function(){
    console.log("event occured");
}


var buttonClicked=function(){
    console.log("button click event occured");
}

eventEmitter.on('event',eventHandler);
eventEmitter.emit('event');

eventEmitter.addListener('click', buttonClicked);
eventEmitter.emit('click');