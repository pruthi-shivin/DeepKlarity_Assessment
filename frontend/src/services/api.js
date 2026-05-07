import axios from "axios";

const API = axios.create({
  baseURL: "https://deepklarity-assessment.onrender.com",
});

export default API;