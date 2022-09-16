import React ,{useState} from 'react'

import config from './config'
function BuyTicket() {
    const url = "/buyticket"
    const [data,setdata] = useState({
    Flight_id  :"",
    Customer_id  :""
 })


 function submit(e){
    e.preventDefault();
    config.post(url,{
        Flight_id:data.Flight_id,
        Customer_id:data.Customer_id    
    })
    .then(res=>{
        console.log(res.data)

      }).catch(function (error){

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
        <h1>buy ticket</h1>
      <form onSubmit={(e) => submit(e)}>
        <input onChange={(e)=>handele(e)} id="Flight_id" value={data.Flight_id}   placeholder="Flight_id" type="number"  ></input><br></br>
        <input onChange={(e)=>handele(e)} id="Customer_id" value={data.Customer_id}   placeholder="Customer_id" type="number"   ></input><br></br>
        <button>Buy Ticket</button>
      </form>
        

    </div>
  )
}

export default BuyTicket