import React ,{useState} from "react";
import '../app.css';
import config from "../config";

function GetAlAdimns(){

const [admin,setAdmins] = useState([])

const getAdmin = ()=>{
    config.get("/admins")
    .then((response) =>{
        console.log(response)
        
        setAdmins(response.data)
    })
}

const adminDelete = (id,e)=> {
    e.preventDefault();
    config.delete(`admin/${id}`)
    .then((response) =>{
        console.log('deleted',response)
        
    })
} 


    return(
        <>
        <div>
            <div>
            <div style={{margin : '20px 40%'}}>
                    <button type="button" class="btn btn-outline-primary"  onClick={getAdmin} >Get All Adimnistators</button>
                    
                </div>
                <br>
                </br>
          
            </div>
                {   
                    admin.map((value)=>{
                        
                        return(
                            <table class="table">
                                
      
        <tbody key={value.id}>
            <th scope="row">{value.id}</th>
            <td>{value.First_Name}</td>
            <td>{value.Last_Name}</td>
            <td>{value.user_id}</td>
            <td><button className="btn btn-danger btn-sm" onClick={(e)=> adminDelete(value.id ,e)}>delete</button></td>

        </tbody>
        </table>
                        )
                })
                }

            </div>
        
        </>
    )
}


export default GetAlAdimns