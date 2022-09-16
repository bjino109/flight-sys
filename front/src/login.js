import React ,{useState} from 'react'
import axios from 'axios'
function Login() {
    const url = "http://127.0.0.1:5000//login"
    const [data,setdata] = useState({
    user_name  : "",
    password : "",

 
 })


 function submit(){
    axios.post(url, {
        user_name:data.user_name,
        password:data.password,
     
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
        <h1>Login</h1>
      <form onSubmit={(e) => submit(e)}>
        <input onChange={(e)=>handele(e)} id="user_name" value={data.user_name}   placeholder="User_Name" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="password" value={data.password}  placeholder="Password" type="text" ></input><br></br>
        <button>submit</button>
      </form>
        

    </div>
  )
}

export default Login