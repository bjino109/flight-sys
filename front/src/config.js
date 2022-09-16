import axios from "axios";

export default axios.create({
    baseURL:'https://flight-back.herokuapp.com/'
})