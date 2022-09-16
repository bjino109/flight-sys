import React ,{useState} from 'react'
import config from '../config'

function UpdatUser() {
    const [data,setdata] = useState({
    id:"",
    user_name  : "",
    password : "",
    email : "",
    role_id  : ""
 
 })


 function submit(){
        config.put('/update/'+ data.id, {
        id:data.id,  
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
        <h1>Update</h1>
      <form onSubmit={(e) => submit(e)}>
        <input onChange={(e)=>handele(e)} id="id" value={data.id}   placeholder="id" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="user_name" value={data.user_name}   placeholder="User_Name" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="password" value={data.password}  placeholder="Password" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="email" value={data.email}     placeholder="Email" type="text" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="role_id" value={data.role_id}   placeholder="role_id" type="int" ></input><br></br>
        <button>Update</button>
      </form>
        

    </div>
  )
}
export default  UpdatUser