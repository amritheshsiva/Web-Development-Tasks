import image from "./images/profile.webp";

function App() {
  const name = "Jishnu ";
  const description = "React beginner exploring web development.";

  const cardstyle = {
    border: "1px solid #020202",
    padding: "15px",
    backgroundColor: "#f1ecec",
    width: "260px",
    borderRadius: "6px",
    textAlign: "center"
  };
  const profilestyle = {
    width: "100%",
    borderRadius: "4px",
    marginBottom: "10px"
  };
  const extstyle = {
    width: "200px",
    marginBottom: "10px"
  };
  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div style={cardstyle}>
        <img src={image} alt="Profile" style={profilestyle}/>
        <img src="https://imgs.search.brave.com/PQsqioJ6A4jL1H-MpI6PWEckJRnEl76jCkHez4Sh_1U/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zaWdu/YXR1cmUuZnJlZWZp/cmUtbmFtZS5jb20v/aW1nLnBocD9mPTUm/dD1KaXNobnU"
        alt="External"style={extstyle}/>

        <h5>{name}</h5>
        <p style={{fontSize:"14px",color:"#674545" }}>{description}</p>
      </div>
    </div>
    );
  }

export default App;
