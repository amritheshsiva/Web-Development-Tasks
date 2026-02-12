import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { setUser } from "../../store/authSlice";
import Navbar from "../Navbar";

function Login() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    const dispatch = useDispatch();
    const navigate = useNavigate();

    function attemptLogin() {

        setErrorMessage(""); 

        axios.post("https://demo-blog.mashupstack.com/api/login", {
            email,
            password
        })
        .then(response => {

            const token = response.data.token;

            // Save token in localStorage
            localStorage.setItem("token", token);

            // Save user in Redux store
            dispatch(setUser({
                email: email,
                token: token
            }));

            // Redirect to ListPost page
            navigate("/listpost");   // ✅ fixed path
        })
        .catch(() => {
            setErrorMessage("Invalid login credentials");
        });
    }

    return (
        <div>
            <Navbar />

            <div className="container">
                <h1>Login</h1>

                {errorMessage && (
                    <div style={{ color: "red" }}>
                        {errorMessage}
                    </div>
                )}

                <div>
                    <input
                        type="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>

                <div>
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>

                <button onClick={attemptLogin}>Login</button>
            </div>
        </div>
    );
}

export default Login;
