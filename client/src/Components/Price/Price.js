import React, { Component } from 'react'
import {Card} from 'react-bootstrap';
import './Price.css'
import { get_quote } from '../../Utils/finance_api';
class Price extends Component {
  constructor(props){
    super(props)
    this.state={
      name:props.name,
      code:props.code,
      price:0,
      change:0
    }
  }
  async componentDidMount(){
    const {code}=this.state
    const res=await get_quote(code)
    this.setState({
      price:res.quoteResponse.result[0].regularMarketPrice,
      change:res.quoteResponse.result[0].regularMarketChange
    })
    console.log(res)
  }
  render(){
  const {name,price,change}=this.state
  return (
  <div className='Price'>
    <div >
            {name}
    </div>
    <div className={parseFloat(price)>0?'Price_Up':'Price_Down'} >
        {price}
    </div>
    <div className={parseFloat(change)>=0?'Price_Up':'Price_Down'} >
        {change}
    </div>
  </div>
  )
  }
}
export default Price
