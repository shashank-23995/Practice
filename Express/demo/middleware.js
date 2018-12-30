const express = require('express')
const app = express()
const port = 3000

var myLogger = function (req, res, next) {
    console.log('LOGGED')
    next()
  }

  app.use(myLogger)

  var requestTime = function (req, res, next) {
    req.requestTime = Date.now()
    next()
  }
  
  app.use(requestTime)

app.get('/', function (req, res) {
    var responseText = 'Hello World!<br>'
    responseText += '<small>Requested at: ' + req.requestTime + '</small>'
    res.send(responseText)
  })

  app.listen(port, () => console.log(`Example app listening on port ${port}!`))