const express=require('express')
const app=express()
const port=3000


app.get('/users/:userId/books/:bookId', function (req, res) {
    var user=req.params.userId
    var books=req.params.bookId
    res.send(req.params)
    //res.send("user="+user+"<br>"+"book="+books)
  })
app.listen(port)