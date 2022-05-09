const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.send('Hello world');
});

router.get('/stockService/:name', (req, res) => {
    res.send(req.path + " called");  
});

module.exports = router;