import React, { useState } from 'react'
import Button from '@mui/material/Button';
import './Login.css'
import Popup from '../Popup/Popup';
import LoginForm from './LoginForm';
import Signup from './Signup';
import {AuthProvider,useAuth} from './AuthContext'
function Login(props) {
   const [openPopup,setOpenPopup]=useState(false);
   const {isSignup} =props;
   const [isLogin,setLogin]=useState(false)
   console.log(isLogin)
  if(isSignup==='true'){
  return (
    <AuthProvider>
    <div>    
     <Button variant="contained" onClick={()=>{setOpenPopup(true);}} >
           Signup
    </Button>
    <Popup
      openPopup={openPopup}
      setOpenPopup={setOpenPopup}
      setLogin={setLogin}
      title="Sign Up"
      >      
    <Signup  setOpenPopup={setOpenPopup} /> 
    </Popup>
    </div>
    </AuthProvider>
  )
  }else{
    return (
      <AuthProvider>
    <div>
    <Button variant="contained" onClick={()=>{setOpenPopup(true);}} >
           Login
    </Button>
    <Popup
      openPopup={openPopup}
      setOpenPopup={setOpenPopup}
      title="Login"
      setLogin={setLogin}
      >      
      <LoginForm setOpenPopup={setOpenPopup}/>
    </Popup>
    </div>
    </AuthProvider>
    )
  }
}

export default Login