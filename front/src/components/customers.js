import React ,{useState} from "react";
import {Link} from "react-router-dom"

import config from "../config";


function GetAllcustomers(){

const [customers,setCustomers] = useState([])

const getCustomers = ()=>{
    config.get("/customers")
    .then((response) =>{console.log(response)

        setCustomers(response.data)
    })
} 

const customerDelete = (id,e)=> {
    e.preventDefault();
    config.delete(`/customer/${id}`)
    .then((response) =>{
        console.log('deleted',response)
        
    })
} 
    return(
        <>
        <div>
            <div>
            <div style={{margin : '20px 40%'}}>
                    <button  type="button" class="btn btn-outline-primary"  onClick={getCustomers} >Get All Customers</button>
                </div>
                <br>
                </br>
            </div>
            <table class="table table-sm" >
                { <thead>
                    <tr>
                        <th>id</th>
                        <th>first_name</th>
                        <th>last_name</th>
                        <th>address</th>
                        <th>phone_num</th>
                        <th>Credit_Card_No</th>
                        <th>User_id</th>
                        <th></th>
                    </tr>
                </thead>

                }


            
                {   
                    customers.map((value)=>{
                        return(
                            

        <tbody>
            <th scope="row">{value.id}</th>
            <td>{value.first_name}</td>
            <td>{value.last_name}</td>
            <td>{value.address}</td>
            <td>{value.phone_num}</td>
            <td>{value.Credit_Card_No}</td>
            <td>{value.User_id }</td>
            <td><Link to={`/tiketdetail`}><button className="btn btn-info btn-sm">ticket Dtail</button></Link></td>
            <td><button  className="btn btn-danger btn-sm"  onClick={(e)=> customerDelete(value.id ,e)}>delete</button></td>
        </tbody>
        
                        )
                })
                }
            </table>
            </div>
        
        </>
    )
}


export default GetAllcustomers