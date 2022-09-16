import React ,{useState} from 'react'
import config from '../config'

function UpdatFlight() {
    const [data,setdata] = useState({
    id:"",
    company_name: "",
    Origen: "",
    Destination: "",
    Remaining_Tickets : "",
 
 })


 function submit(e){
        e.preventDefault();
        config.put('updateflight/'+ data.id, {
        id:data.id,  
        company_name:data.company_name,
        origin:data.Origen,
        Destination: data.Destination,
        Remaining_Tickets:data.Remaining_Tickets
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
        <input onChange={(e)=>handele(e)} id="id" value={data.id}   placeholder="id" type="number" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="company_name" value={data.company_name}   placeholder="company" type="number" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="Origen" value={data.Origen}  placeholder="origen" type="number" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="Destination" value={data.Destination}     placeholder="destination" type="number" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="Remaining_Tickets" value={data.Remaining_Tickets}   placeholder="Remaining_Tickets" type="number" ></input><br></br>
        <button>Update</button>
      </form>
        

    </div>
  )
}
export default  UpdatFlight