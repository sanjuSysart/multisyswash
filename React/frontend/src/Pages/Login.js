import React, { Fragment, useState } from 'react';
import axios from 'axios';
import { Button } from 'reactstrap'


function Login() {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
  
    const submitData = async (e) =>{
      const data = { email, password }
      console.log('data', data)
      const res = await fetch('http://127.0.0.1:8000/api/token/',{
        method: 'POST',
        headers: {
          'Content-Type' : 'application/json'
        },
        body: JSON.stringify(data)
      })
      const datas = await res.json()
      localStorage.setItem('token', datas?.access)
      console.log('response', datas)
      e.preventDefault()
    }    
  
    return (
     <Fragment>
        <div>
        <form>
          Email<br/>
          <input type="email" name="email" id="email" onChange={(e) => setEmail(e.target.value)}></input><br/>
          Password<br/>
          <input type="password" name="password" id="password" onChange={(e) => setPassword(e.target.value)}></input><br/><br/>
          <Button onClick={(e) => submitData(e)}>LOGIN</Button>
        </form>
        
      </div>
      <div>

      </div>
     </Fragment>
    );
}

export default Login;
