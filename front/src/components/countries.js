import React ,{useState} from "react";

import config from "../config";


function GetAllCountries(){

const [countries,setCountries] = useState([])

const getCountries = ()=>{
    config.get("/countries")
    .then((response) =>{
        console.log(response)
        
        setCountries(response.data)
    })
} 
const countryDelete = (id,e)=> {
    e.preventDefault();
    config.delete(`country/${id}`)
    .then((response) =>{
        console.log('deleted',response)
        
    })
} 
    return(
        <>
        <div>
            <div>
            <div style={{margin : '20px 40%'}}>
                <button type="button" class="btn btn-outline-primary"   onClick={getCountries} >Get All Countries</button>
                </div>
                <br></br>
                <br></br>
                </div>
        <table class="table table-sm">
            {<thead>
                <tr>
                <th>id</th>
                <th>name</th>
                </tr>
            </thead> }
            {   
             countries.map((value)=>{
                  return(
        <tbody>
            <th >{value.id}</th>
            <td>{value.name}</td>
            <td><button className="btn btn-danger btn-sm"  onClick={(e)=> countryDelete(value.id ,e)}>delete</button></td>
        </tbody>
                        )
                })
                }
        </table>
            </div>
        
        </>
    )
}


export default GetAllCountries