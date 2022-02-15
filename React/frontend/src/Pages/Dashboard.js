import axios from 'axios';
import React, { useEffect, useState } from 'react';

function Dashboard() {
  
  
  useEffect(() =>{
    async function getAPI (){
      const token =  localStorage.getItem('token')
      console.log('token',token)
      const res = await fetch('http://127.0.0.1:8000/user/hello/',{
        method: 'GET',
        headers: {
          'Content-Type' : 'application/json',
          'Authorization': `Bearer ${token}`
        },
      })
      const datas = await res.json()
      console.log('response', datas)
    }
    getAPI()
    
  }, [])
  return <div>HELLOOO</div>;
}

export default Dashboard;
