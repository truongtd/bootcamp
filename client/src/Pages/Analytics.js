import React, { Component } from 'react'
import StockChart from '../Components/Charts/Chart'
import { get_chart,get_quote } from '../Utils/finance_api'
import axios from 'axios'
class Analytics extends Component {
  constructor(props){
    super(props)
    this.state={
      list_symbol:props.list_symbol,
      range:props.range,
      region:props.region,
      interval:props.interval,
      lang:props.lang,
      isLoading:true
    }
  }
 async  componentDidMount() {   
    const { list_symbol,range,region,interval,lang } = this.state;
    const list_code=list_symbol.map(item=>item.code)
    const meta= await get_quote(list_code.toString())
    for(const item of list_symbol){
      item.info= meta.quoteResponse.result.find(e =>e.symbol==item.code)
      const res =await get_chart(item.code,range,region,interval,lang)
      item.chart=res.chart.result[0]
    }
    this.setState({
      isLoading:false,
    })
    // console.log(list_code)
    // var config = {
    //   method: 'get',
    //   url: `https://yfapi.net/v8/finance/chart/${list_code.toString()}?range=${range}&region=${region}&interval=${interval}&lang=${lang}`,
    //   headers: { 
    //     'X-API-KEY': 'Ys3q6S4PELdCQDivIw915FLjNAxT0p81IK1BZIs6'
    //   }
    // };
    
    // axios(config)
    // .then(response => {
    //   console.log(JSON.stringify(response.data));
    //   this.setState({
    //     data: response.data.chart.result[0],
    //     isLoaded: true
    //   });
    // })
    // .catch(function (error) {
    //   console.log(error);
    // });
  }
  render(){
  const {list_symbol,range,region,lang,interval,isLoading}=this.state;
  if(isLoading){
    return <div>Loading...</div>
  }else{
  return (
    <div>
      {
        list_symbol.map(item => <div><StockChart info={item.info} data={item.chart} code={item.code} range={range} region={region} interval={interval} lang={lang}/></div>)
      }
      {/* <div><StockChart code="AAPL" range="12mo" region="US" interval="1d" lang="en"/></div>
      <div><StockChart code="GRAB" range="12mo" region="US" interval="1d" lang="en"/></div> */}
    </div>
  )}
    }
}

export default Analytics