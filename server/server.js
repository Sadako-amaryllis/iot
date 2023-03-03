const express = require('express')
const app = express()

let name = "a"
app.use(express.json());

app.get('/name', function (req, res) {
  res.send(name)
})
app.post('/', function (req,res) {
    name = req.body
    res.send(res)
})

app.listen(4000,()=>console.log('port 4000'))