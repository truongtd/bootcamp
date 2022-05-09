import React from 'react'
import StockInfo from '../Components/Stocks/StocksInfo'
function Dashboard() {
  return (
    <div><StockInfo list_code='QCOM,GRAB,NDAQ,AAPL,MSFT,GOOG,AMZN,TSLA,NVDA,JNJ,FB,TSM,UNH,PG,PFE'></StockInfo></div>
  )
}

export default Dashboard