import "./App.css";
import image from "./images/mohanlal.jpeg"
function App() {
  let greeting = "Hello World";
  return (
  <div>
  <h1 className="greetingStyle">{greeting}</h1>
  <img src={image} alt="mohanlal"/>
  </div>
  );
}
export default App;