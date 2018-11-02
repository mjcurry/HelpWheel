const watson = require('watson-developer-cloud');
const express = require('express')
const bodyParser = require('body-parser')

var assistant = new watson.AssistantV1({
    iam_apikey: 'ylk2P4NKwMN5C85d0TREK3CqL-SBLq3WOpbrAx1Sj6k5',
    version: '2018-09-20'
});


const app = express()
app.use(bodyParser.json())

app.post('/', (req, res) => {
    if (req.body.text) {
        assistant.message({
            workspace_id: 'bcedb5d2-7b05-4185-b039-ee3927e3f4bd',
            input: {'text': req.body.text}
        },  function(err, response) {
            if (err)
                console.log('error:', err);
            else
                res.json(response)
        });

    }
    else {res.json({
        "error": "No input text provided"
    })}
})

app.listen(3000, "0.0.0.0", () => {
    console.log("App is running on http://0.0.0.0:3000")
})
