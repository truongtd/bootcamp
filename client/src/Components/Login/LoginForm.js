import React,{useRef,useState} from 'react'
import {Form,Button,Card, Alert} from 'react-bootstrap';
import { useAuth } from './AuthContext';
function LoginForm(props) {
  const {setOpenPopup}=props;
  const [error,setError]=useState();
  const {login} =useAuth();
  const {setLogin}=props
  const handleClose = () => {
    setOpenPopup(false);
  };
  const emailRef=useRef();
  const passwordRef=useRef();
  async function handleSubmit(e){
    e.preventDefault();
   
    try{
    setError('')    
    const res=await login(emailRef.current.value,passwordRef.current.value)
    console.log('create successful')
    setLogin(true)
    setOpenPopup(false);
    }catch(err){
        console.log(err)
        setError('Login Failed')
    }
}
  return (
    <div>
        <Card>
            <Card.Body>              
                {error && <Alert variant='danger'>{error}</Alert>}
                <Form onSubmit={handleSubmit}>
                    <Form.Group id="email">
                        <Form.Label>Email</Form.Label>
                        <Form.Control type="email" ref={emailRef} required/>
                    </Form.Group>
                    <Form.Group id="password">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" ref={passwordRef} required/>
                    </Form.Group>                    
                    <Button type='submit' className='w-100' size="sm">Sign In</Button>
                    <Button type='Button' size="sm" className='w-100' onClick={handleClose}>Cancel</Button>
                </Form>
            </Card.Body>
            
        </Card>  
    </div>    
  )
}

export default LoginForm