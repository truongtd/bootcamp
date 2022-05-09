import React,{useRef, useState} from 'react'
import {Form,Button,Card} from 'react-bootstrap';
import { useAuth } from './AuthContext';
export default function Signup(props) {
    const {setOpenPopup}=props;
    const emailRef=useRef();
    const passwordRef=useRef();
    const passwordConfirmRef=useRef();
    const {signup,currentUser} =useAuth();
    console.log(currentUser);
    const [error,setError]=useState();
    const {loading,setLoading}=useState(false);
  
    const handleClose = () => {
        setOpenPopup(false);
    };
    async function handleSubmit(e){
        e.preventDefault();
        if(passwordRef.current.value!=passwordConfirmRef.current.value){
            return setError(`Password doesn't match`);
        }
        try{
        setError('')    
        await signup(emailRef.current.value,passwordRef.current.value)
        console.log('create successful')
        setOpenPopup(false);
        }catch(err){
            console.log(err)
            setError('Failed to create an account')
        }
    }
  return (
    <div>
        <Card>
            <Card.Body>
                <Form onSubmit={handleSubmit}>
                    <Form.Group id="email">
                        <Form.Label>Email</Form.Label>
                        <Form.Control type="email" ref={emailRef} required/>
                    </Form.Group>
                    <Form.Group id="password">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" ref={passwordRef} required/>
                    </Form.Group>
                    <Form.Group id="passwordConfirm">
                        <Form.Label>Password Confirm</Form.Label>
                        <Form.Control type="password" ref={passwordConfirmRef} required/>
                    </Form.Group>
                    <Button type='submit' className='w-100'>Sign Up</Button>
                </Form>
            </Card.Body>
            
        </Card>
    </div>
  )
}
