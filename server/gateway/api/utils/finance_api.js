const axios = require("axios");
const API_KEY = '6DC6Dzskh45TbSpdwZQpHUkYQV2eu4I4RFDdAyy3';
module.exports = {
    async  get_quote(list_code){    
        const config = {
            method: 'get',
            url: `https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols=${list_code}`,
            headers: { 
                'X-API-KEY': API_KEY
            }
        };          
        const res = await axios(config);
        return res.data;                 
    },
    async  get_chart(code,range,region,interval,lang){
        const config = {
            method: 'get',
            url: `https://yfapi.net/v8/finance/chart/${code}?range=${range}&region=${region}&interval=${interval}&lang=${lang}`,
            headers: { 
                'X-API-KEY':API_KEY
            }
        };      
        const res = await axios(config);
        return res.data;
    }
};

// export async function get_quote(list_code){    
//     const config = {
//         method: 'get',
//         url: `https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols=${list_code}`,
//         headers: { 
//             'X-API-KEY': 'Ys3q6S4PELdCQDivIw915FLjNAxT0p81IK1BZIs6'
//         }
//     };          
//     const res = await axios(config);
//     return res.data;
         
// } 
// export async function get_chart(code,range,region,interval,lang){
//     const config = {
//         method: 'get',
//         url: `https://yfapi.net/v8/finance/chart/${code}?range=${range}&region=${region}&interval=${interval}&lang=${lang}`,
//         headers: { 
//             'X-API-KEY': 'Ys3q6S4PELdCQDivIw915FLjNAxT0p81IK1BZIs6'
//         }
//     };      
//     const res = await axios(config);
//     return res.data;


