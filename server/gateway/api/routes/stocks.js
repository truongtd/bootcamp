const express = require('express');
const router = express.Router();
const utils = require('../utils/finance_api');
const cors = require('cors');
router.options('/',cors());
router.post('/',async(req,res,next)=>{
    const type = req.body.type;
    let data = null;
    res.setHeader('Access-Control-Allow-Origin',"http://localhost:3000");
    res.setHeader('Access-Control-Allow-Headers',"*");
    res.header('Access-Control-Allow-Credentials', true);
    switch(type){
        case "info":            
            data = await get_quote(req.body.code);                 
            break;
        case "chart":
            data = await get_chart(req.body.code,req.body.range,req.body.region,req.body.interval);
            break;
        default:
            break;
    }
    res.status(200).json(data);
    next();
});
router.get('/charts/:code/:range/:region/:interval',async(req,res,next) =>{
    const code = req.params.code;
    const range = req.params.range;
    const region = req.params.region;
    const interval = req.params.interval;
    const data = await get_chart(code,range,region,interval);
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.status(200).json(data);
} );
async function get_quote(list_code){
    return await utils.get_quote(list_code);
}
async function get_chart(code,range,region,interval){
    return await utils.get_chart(code,range,region,interval);
}
module.exports = router;