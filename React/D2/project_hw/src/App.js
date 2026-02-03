function App() {
  const favoriteFoods = ["Pizza", "Burger", "Pasta"];
  function showLove(food) {
    document.getElementById("message").innerText ="I love " + food + "!";
  }

  return (
    <div style={{ padding: "25px" }}>
      <h2>My Favorite Foods</h2>
      <ul>
        {favoriteFoods.map((food, index) => (
          <li key={index}>
            {food}{" "}
            <button onClick={() => showLove(food)}>Love</button>
          </li>
          )
        )
        }
      </ul>
      
      <p id="message">Select a food that you love!</p>
    </div>
  );
}

export default App;
