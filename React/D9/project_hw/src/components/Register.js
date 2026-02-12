import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleRegister = async () => {
    try {
      await axios.post(
        "https://worksheet-product.mashupstack.com/register",
        {
          user_name: name,  
          email: email,
          password: password
        }
      );

      alert("Registered successfully");
      navigate("/login");

    } catch (error) {
      console.log(error.response); 
      alert(
        error.response?.data?.message ||
        JSON.stringify(error.response?.data) ||
        "Registration failed"
      );
    }
  };

  return (
    <div>
      <h2>Register</h2>

      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <br/><br/>

      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <br/><br/>

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <br/><br/>

      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;
