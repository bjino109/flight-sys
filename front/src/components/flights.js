import React ,{useState} from "react";
import config from "../config";
import {Link} from "react-router-dom"

function GetAllFlights(){

const [flights,setFlights] = useState([])
const [search,setSearch] =  useState("")
const [flight,setFlight] = useState({})
 

const getFlights = ()=>{
    config.get("/flights")
    .then((response) =>{
        console.log(response)
        setFlights(response.data)
    })
} 

const flightDelete = (id,e)=> {
    e.preventDefault();
    config.delete(`/flight/${id}`)
    .then((response) =>{
        console.log('deleted',response)
        
    })
} 



function setsearchflight(e){
    config.get("flight/"+ search)
   .then(function (response){
         console.log(response.data)
         setFlight(response.data)
         
 
     }).catch(function (error){
 
     })
 }

 
function setsearchflightbyorgin(e){
    config.get("flightsbyorigin/"+ search)
   .then(function (response){
         console.log(response.data)
         setFlight(response.data)
         
 
     }).catch(function (error){
 
     })
 }
  
function setsearchflightbydes(e){
    config.get("flightsbydes/"+ search)
   .then(function (response){
         console.log(response.data)
         setFlight(response.data)
         
 
     }).catch(function (error){
 
     })
 }
 
    return(
        <>
        <div>
            <div>
            <div style={{padding:"30px"}}>
                    <button type="button" class="btn btn-outline-primary"  onClick={getFlights} >Get All Flights</button>
                    <br/>
                    <br/>
                    <td><Link to="/addflight"><button className="btn btn-info btn-sm">Add flight</button></Link></td>
                    <br/>
                    < br/>
                    <button class="btn btn-outline-info" onClick={e => setsearchflight(e)}>Search Flight by id </button>
                    <input type="text" class="btn btn-light" placeholder="ID...." onChange={e => setSearch(e.target.value)}></input> 
                    <br/>
                    <br/>
                    <button class="btn btn-outline-info" onClick={e => setsearchflightbyorgin(e)}>Search Flight by Origen id </button>
                    <input type="text" class="btn btn-light" placeholder="ID...." onChange={e => setSearch(e.target.value)}></input> 
                    <br/>
                    <br/>
                    <button class="btn btn-outline-info" onClick={e => setsearchflightbydes(e)}>Search Flight by Destination id </button>
                    <input type="text" class="btn btn-light" placeholder="ID...." onChange={e => setSearch(e.target.value)}></input>  
                </div>
                <br></br>
            </div>

            <table class="table table-sm" >
                {   <thead>
                    <tr>
                        <th>id</th>
                        <th>company_name</th>
                        <th>Origen</th>
                        <th>Destination</th>
                        <th>departure_time</th>
                        <th>landing_time</th>
                        <th>Remaining_Tickets</th>
                        <th></th>
                        <th></th>
                    </tr>
                    </thead>
                }
                <td>{flight.id}</td>
                <td>{flight.company_name}</td>
                <td>{flight.Origen}</td>
                <td>{flight.Destination}</td>
                <td>{flight.departure_time}</td>
                <td>{flight.landing_time}</td>
                <td>{flight.Remaining_Tickets}</td>
                {   
                    flights.map((value )=>{
                        return(
        <tbody key={value.id}>
            <th scope="row">{value.id}</th>
            <td>{value.company_name}</td>
            <td>{value.Origen}</td>
            <td>{value.Destination}</td>
            <td>{value.departure_time}</td>
            <td>{value.landing_time}</td>
            <td>{value.Remaining_Tickets}</td>
            <td><Link to={`/updateflight/${value.id}`}><button className="btn btn-info btn-sm">edit</button></Link></td>
            <td><Link to={`/buyticket`}><button className="btn btn-info btn-sm">buy ticket</button></Link></td>
            <td><button className="btn btn-danger btn-sm" onClick={(e)=> flightDelete(value.id ,e)}>delete</button></td>
        </tbody>
        
                        )
                })
                }
         </table>
            </div>
        
        </>
    )
}


export default GetAllFlights