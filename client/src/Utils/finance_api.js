import axios from "axios";

export  async function get_quote(list_code){    
        var config = {
            method: 'post',
            data:{
              type:"info",
              code:list_code
            },                    
            url: `http://localhost:5000/stocks`,            
          };          
          const res= await axios(config)
          return res.data;
         
    } 
export async function get_chart(code,range,region,interval,lang){
    var config = {
        method: 'post',
        data:{
          type:'chart',
          code:code,
          range:range,
          region:region,
          interval:interval,
          lang:lang
        },
        url: `http://localhost:5000/stocks`,        
      };      
      const res= await axios(config)
      return res.data;
}
