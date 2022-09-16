import React ,{useState} from "react";
import config from "../config";
import {Link} from "react-router-dom"



function GetAllUsers(){

const [users,setUsers] = useState([])
const [search,setSearch] =  useState("")
const [user,setUser] = useState({})
 


const getUsers = ()=>{
    config.get('users')
    .then((response) =>{
        console.log(response)
        
        setUsers(response.data)
    })
}

const userDelete = (id,)=> {
    // e.preventDefault();
    config.delete(`user/${id}`)
    .then((response) =>{
        console.log('deleted',response)
        
    })
} 

function setsearchUser(e){
   config.get("user/"+ search)
  .then(function (response){
        console.log(response.data)
        setUser(response.data)
        

    }).catch(function (error){

    })
}



    return(
        <>
        
        <div>
            <div>   
                <div >
                    <button  type="button" class="btn btn-outline-primary" onClick={getUsers} >Get All Users</button>
                    <br></br>
                    <br></br>
                    <button class="btn btn-outline-info" onClick={e => setsearchUser(e)}>Search User </button>
                    <input type="text" class="btn btn-light" placeholder="user name" onChange={e => setSearch(e.target.value)}></input> 
                </div>
                
                <table class="table table-sm">
                { <thead>
                  <tr>
                  <th  >id</th>
                  <th >username</th>
                  <th >password</th>
                  <th >Email</th>
                  <th  >role</th>
                  <th></th>
                  <th></th>
                 </tr>
                 </thead> }
                 <td>{user.id}</td>   
                 <td>{user.username}</td>
                 <td>{user.password}</td>
                 <td>{user.email}</td>
                 <td>{user.role_name}</td>
                 

                 {   
         users.map((value)=>{
                
                return(
                    
     <tbody >
    <th scope="row" >{value.id}</th>
    <td >{value.username}</td>
    <td>{value.password}</td> 
    <td>{value.email}</td>
    <td>{value.role_name}</td>
    <td><Link to={`/update/${value.id}`}><button className="btn btn-info btn-sm">edit</button></Link></td>
    <td> <button  className="btn btn-danger btn-sm"  onClick={(e)=> userDelete(value.id,e)}>delete</button></td>
    
    </tbody>

        
                )
        })
        }

             </table>
            </div>
            </div>
        
        </>

        
    )
    
}




export default GetAllUsers