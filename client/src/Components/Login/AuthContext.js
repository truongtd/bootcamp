import React, { useContext, useState,useEffect } from 'react'
import {auth} from './firebase'

const AuthContext= React.createContext();
export function useAuth(){
    return useContext(AuthContext)
}
export  function AuthProvider({children}) {
    const [currentUser,setCurrentUser]=useState()
    const [loading,setLoading]=useState(true)
    function signup(email,password){
        console.log(auth)
        const res=auth.createUserWithEmailAndPassword(email,password)
        return res
    }
    function login(email,password){
        const res=auth.signInWithEmailAndPassword(email,password)
        return res
    }
    function getCurrentUser(){
        return currentUser;
    }
    const value={
        currentUser,
        login,
        signup,
        getCurrentUser
    }
    useEffect(()=>{
    const unsubcriber=    auth.onAuthStateChanged(user=> {
        setLoading(false);
        setCurrentUser(user);
        })
    return unsubcriber
    },[]);
    return (
    <AuthContext.Provider value={value}>
        {!loading&&children}
    </AuthContext.Provider>
  )
}
