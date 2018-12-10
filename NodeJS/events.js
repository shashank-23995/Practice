var events=require('events');
var eventEmitter=new events.EventEmitter();

var myEventHandler=function(){
    console.log("user defined event");
}

eventEmitter.on('start',myEventHandler);
eventEmitter.emit('start');