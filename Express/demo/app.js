const express = require('express')
const app = express()
const port = 3000

  app.get('/about', function (req, res) {
    res.send('about')
  })

  app.get('/random.text', function (req, res) {
    res.send('random.text')
  })



  app.listen(port, () => console.log(`Example app listening on port ${port}!`))