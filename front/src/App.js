import React from "react"
import { Route, Routes } from 'react-router-dom';
import GetAllUsers from './components/users'
import GetAllcustomers from "./components/customers";
import GetAllCompanis from "./components/airlines_companis";
import GetAllCountries from "./components/countries";
import GetAllFlights from "./components/flights";
import GetAlAdimns from "./components/administators";
import Login from "./login";
import Navbar from "./components/navbar";
import 'bootstrap/dist/css/bootstrap.css'
import Register from "./Register";
import UpdatUser from "./components/update_user";
import AddFlight from "./components/addflight";
import UpdatFlight from "./components/updateflight";
import BuyTicket from "./buyticket";









function App() {
  return (

   
    <main className="App">
      <Navbar/>
      <Routes>
       <Route path="/users" element={<GetAllUsers/>}/>
       <Route path="/getallcustumers" element={<GetAllcustomers/>}/>
       <Route path="/getallcompanis" element={<GetAllCompanis/>}/>
       <Route path="/getalladmins" element={ <GetAlAdimns/>}/>
       <Route path="/getallcountry" element={ <GetAllCountries/>}/>
       <Route path="/getallflights" element={ <GetAllFlights/>}/>
       <Route path="/login" element={ <Login/>}/>
       <Route path="/register" element={ <Register/>}/>
       <Route path="/update/:id" element={ <UpdatUser/>}/>
       <Route path="/addflight" element={ <AddFlight/>}/>
       <Route path="/updateflight/:id" element={ <UpdatFlight/>}/>
       <Route path="/buyticket" element={ <BuyTicket/>}/>
       </Routes>  
    </main>
  );
}

export default App;
