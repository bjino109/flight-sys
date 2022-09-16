import React ,{useState} from "react";
import config from "../config";

function GetAllCompanis(){

const [companis,setCompanis] = useState([])

const getCompanis= ()=>{
    config.get("/companis")
    .then((response) =>{
        console.log(response)
        
        setCompanis(response.data)
    })
} 

const companyDelete = (id,e)=> {
    e.preventDefault();
    config.delete(`company/${id}`)
    .then((response) =>{
        console.log('deleted',response)
        
    })
} 
    return(
        <>
        <div>
            <div>
            <div style={{margin : '20px 40%'}}>
                <button type="button" class="btn btn-outline-primary"  onClick={getCompanis} >Get All Airlines Companis</button>
                </div>
                <br></br>
            </div>

            <table class="table table-sm">
                {
                    <tr>
                        <th>id</th>
                        <th>Company_Name</th>
                        <th>user_id</th>
                        <th>contry_id</th>
                        <th></th>
                    </tr>
                }


            
                {   
                    companis.map((value)=>{
                        return(
                            
                                
      

        <tbody>
            <th scope="row">{value.id}</th>
            <td>{value.Company_Name}</td>
            <td>{value.user_id}</td>
            <td>{value.contry_id}</td>
            <td><button  className="btn btn-danger btn-sm" onClick={(e)=> companyDelete(value.id ,e)}>delete</button></td>
        </tbody>
        
                        )
                })
                }
                </table>
            </div>
        
        </>
    )
}


export default GetAllCompanis