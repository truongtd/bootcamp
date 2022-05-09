import React,{Component} from 'react'
import Login from './Login'
import { useAuth } from './AuthContext';
class Authentication extends Component {
    constructor(props){
        super(props)
        this.state={
            isAuthenticated:false,
            userProfile:''
        }
    }
componentDidUpdate()
{
    console.log('Update')
}
render(){
        return (
            <div>
                <div className='Login' >
                    <Login isSignup='true'></Login>   
                </div>
                <div className='Login'> 
                    <Login isSignup='false'></Login>
                </div>   
            </div>
        )
    }
}
export default Authentication
