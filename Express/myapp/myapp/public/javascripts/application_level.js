const express = require('express')
const app = express()
const port = 3000

app.use(function (req, res, next) {
  console.log('Time:', Date.now())
  next()
})

app.use('/user/:id', function (req, res, next) {
  console.log('Request Type:', req.method)
  next()
})

// app.get('/user/:id', function (req, res, next) {
//   res.send('USER')
// })

app.use('/user/:id', function (req, res, next) {
  console.log('Request URL:', req.originalUrl)
  next()
}, function (req, res, next) {
  console.log('Request Type:', req.method)
  next()
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))