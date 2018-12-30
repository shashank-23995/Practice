const express=require('express')
const app=express()
port=3000

app.get("/", function (req, res) {
  throw new Error("BROKEN"); // Express will catch this on its own.
});
app.listen(port,()=>console.log(`app listening on port ${port}!`))