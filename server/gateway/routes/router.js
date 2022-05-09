const express = require('express');
const router = express.Router();
const stockService = require('./stockService');
router.use((req, res, next) => {
    console.log("Called: ", req.path);
    next();
});
router.use(stockService);
module.exports = router;