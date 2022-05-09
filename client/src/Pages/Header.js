import React from 'react'
import Authentication from '../Components/Login/Authentication'
import Price from '../Components/Price/Price'
function Header(){
  return (    
    <div>
      <div>
        <Price name="OIL" code='CL=F'></Price>
      </div>
      <div>
        <Price name="GOLD" code='XAUUSD=X'></Price>
      </div>
      <div>
        <Price name="BITCOIN" code='BTC-USD'></Price>
      </div>
      <div>
        <Price name="USD/JPY" code='JPY=X'></Price>
      </div>
      {/* <div>
        <Price name="OIL" price="104" change="-0.41"></Price>
      </div> */}
      <div>        
        <Authentication/>
      </div>
    </div>    
  )
}

export default Header