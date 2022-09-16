import React ,{useState} from 'react'

import config from './config'
function Register() {
    const url = "/register"
    const [data,setdata] = useState({
    user_name  : "",
    password : "",
    email : "",
    role_id  : ""
 
 })


 function submit(e){
    e.preventDefault();
    config.post(url, {
        user_name:data.user_name,
        password:data.password,
        email: data.email,
        role_id:data.role_id
    })
    .then(res=>{
        console.log(res.data)
    })
    
 }

 function handele(e){
    
    const newdata = {...data}
    newdata[e.target.id]= e.target.value
    setdata(newdata)
    console.log(newdata)
 }


  return (
    <div>
        <h1>Register </h1>
      <form onSubmit={(e) => submit(e)}>
        <input onChange={(e)=>handele(e)} id="user_name" value={data.user_name}   placeholder="User_Name" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="password" value={data.password}  placeholder="Password" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="email" value={data.email}     placeholder="Email" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="role_id" value={data.role_id}   placeholder="role_id" type="int" ></input><br></br>
        <button>submit</button>
      </form>
        

    </div>
  )
}

export default Register