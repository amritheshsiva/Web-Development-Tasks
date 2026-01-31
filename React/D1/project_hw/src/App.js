import React from "react";
import image from "./images/profile.webp";

function App() {
  const name = "John ";
  const description = "React beginner exploring web development.";

  const cardStyle = {
    border: "1px solid #e0e0e0",
    padding: "16px",
    backgroundColor: "#ffffff",
    width: "260px",
    borderRadius: "6px",
    textAlign: "center"
  };
  const profstyle = {
    width: "100%",
    borderRadius: "4px",
    marginBottom: "10px"
  };
  const extimg = {
    width: "80px",
    marginBottom: "10px"
  };

  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div style={cardStyle}>
        <img src={image} alt="Profile" style={profstyle} />
        <img src="https://imgs.search.brave.com/d9ZeiFZ63fTVc9LUdaoLLFmATOdyspaVG3FosB4785w/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jbGlw/YXJ0LWxpYnJhcnku/Y29tLzIwMjQvYmF0/bWFuLWxvZ28taW1h/Z2VzL2JhdG1hbi1s/b2dvLWltYWdlcy0x/LnBuZw"
        alt="External"style={extimg}/>

        <h5>{name}</h5>
        <p style={{ fontSize: "14px", color: "#555" }}>{description}</p></div></div>
        );
      }

export default App;
