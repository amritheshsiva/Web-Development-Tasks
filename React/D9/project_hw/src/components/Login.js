import { useState } from "react";
import axios from "axios";
import { useDispatch } from "react-redux";
import { loginSuccess } from "../store/authSlice";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await axios.post(
        "https://worksheet-product.mashupstack.com/login",
        { email, password }
      );

      dispatch(loginSuccess({
        email,
        token: res.data.token
      }));

      navigate("/products");
    } catch {
      alert("Login failed");
    }
  };

  return (
    <div>
      <h2>Login</h2>

      <input
        placeholder="Email"
        onChange={e=>setEmail(e.target.value)}
      />
      <br/><br/>

      <input
        type="password"
        placeholder="Password"
        onChange={e=>setPassword(e.target.value)}
      />
      <br/><br/>

      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;
