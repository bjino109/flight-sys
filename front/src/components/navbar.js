import React from 'react'
import {NavLink} from 'react-router-dom'

function Navbar  () {
  return (
    <div className='navbar'>
      <NavLink  className="link" to="/">Home</NavLink>
      <NavLink  className="link" to="users">Users</NavLink>
      <NavLink  className="link" to="getallcustumers">Costumers</NavLink>
      <NavLink  className="link" to="getallcompanis">Airlines_companis</NavLink>
      <NavLink  className="link" to="getalladmins">Administators</NavLink>
      <NavLink  className="link" to="getallcountry">Countries</NavLink>
      <NavLink  className="link" to="getallflights">Flights</NavLink>
      <NavLink  className="link" to="login">Login</NavLink>
      <NavLink  className="link" to="register">Rgister</NavLink>
    </div>
  )
}

export default Navbar