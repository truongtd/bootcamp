const express = require('express');
const router = express.Router();
const utils = require('../utils/finance_api');
router.get('/:code?',async(req,res,next) =>{
    const code = req.body.code;
    const range = req.body.range;
    const region = req.body.region;
    const interval = req.body.interval;
    const data = await get_chart(code,range,region,interval);
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.status(200).json(data);
} );
async function get_chart(code,range,region,interval){
    return await utils.get_chart(code,range,region,interval);
}
module.exports = router;
