import React from "react";
import images from "./images/profile.webp";

function App() {
  console.log("React app started")
  const uname = "Jishnu"
  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="card text-center p-4">
        <h2 style={{ color: "#1568e5", fontWeight: "bold" }}>Welcome to React Learning, {uname}</h2>

        <div className="mt-3">
          <img src={images} alt="Internal" className="img-fluid mb-3" style={{ width: "200px" }}/>
          <img src="https://imgs.search.brave.com/NM8_wHLqdydUirjKv3WAG0emS3yZRQgn8yhxKy5_II0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90b3Bw/bmcuY29tL3VwbG9h/ZHMvcHJldmlldy9y/ZWFjdC1sb2dvLWlj/b24tMTE2MDkzNzQx/MjJkOXZrYnB0cWFw/LnBuZw" alt="External" className="img-fluid" style={{ width: "200px" }} />
        </div>
        
        <p className="text-muted mt-3">This is your first card with images and styles!</p>
      </div>
    </div>
  );
}
export default App;
