import React ,{useState} from 'react'

import config from "../config";

function AddFlight() {
    const url = "/addflights"
    const [data,setdata] = useState({
  company_name: "",
  Origen: "",
  Destination: "", 
  Remaining_Tickets : "",
 
 })


 function submit(){
    config.post(url, {
        company_name:data.company_name,
        origin:data.Origen,
        Destination: data.Destination ,
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
        <h1>Add Flight</h1>
      <form onSubmit={(e) => submit(e)}>
        <input onChange={(e)=>handele(e)} id="company_name" value={data.company_name}   placeholder="Company Name" type="int" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="Origen" value={data.Origen}  placeholder="Origin Country" type="int" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="Destination" value={data.Destination}   placeholder="Destination Country" type="int" ></input><br></br>
        <input onChange={(e)=>handele(e)} id="Remaining_Tickets" value={data.Remaining_Tickets}   placeholder="Remaining_Tickets" type="int" ></input><br></br>
        <button>submit</button>
      </form>
        

    </div>
  )
}

export default AddFlight