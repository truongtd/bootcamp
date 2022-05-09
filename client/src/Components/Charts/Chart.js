import React,{Component} from 'react'
import axios from 'axios';
import { PropaneSharp } from '@mui/icons-material';
import CandleStickChart from './CandleStickChart';
import './Chart.css'
import { timeParse } from "d3-time-format";

class StockChart extends Component{
    constructor(props){
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            info:props.info,
            data: props.data,
            code:props.code,
            comparision:props.comparision,
            range:props.range,
            region:props.region,
            interval:props.interval,
            lang:props.lang
          };
    }

    render(){
        const {data,code,info}=this.state
        if (data == null ||data.length===0) {
			return <div>Loading...</div>
		}
        const newdata=[]
        for(let i=0;i<data.timestamp.length-1;i++){
            let modified_date = new Date(1000*data.timestamp[i] );
            
            newdata.push({
                            date:modified_date,
                            volume:data.indicators.quote[0].volume[i],
                            close:data.indicators.quote[0].close[i],
                            open:data.indicators.quote[0].open[i],
                            high:data.indicators.quote[0].high[i],
                            low:data.indicators.quote[0].low[i],
                            })
        }
		return (  
      <div>
        <div>
          <div className='chart_symbol'>
            <h3>{code}</h3> 
          </div>
            <div className={info.regularMarketChangePercent>0?'price_green':'price_red'}>       
              <h3>{data.meta.regularMarketPrice}</h3>
            </div>
            <div className={info.regularMarketChangePercent>0?'price_green':'price_red'}>       
              <h3>Recommendations: {info.averageAnalystRating}</h3>
            </div>           
          </div>
        <div>
          <CandleStickChart type='svg'  data={newdata} />
        </div>
      </div>
        )
    }
}
export default StockChart
