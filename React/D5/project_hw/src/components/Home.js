import React from 'react';
// import Navbar from './components/Navbar';

function Home() {
  function showEnthusiasm() {
    document.getElementById('home-msg').innerText =
      'Hello from React! I love this page!';
    document.getElementById('home-heading').style.backgroundColor = 'lightblue';
  }

  return (
    <div className="card p-4 mb-4">
      
      <h1 id="home-heading">Home</h1>
      <p>This is the Home Page</p>
      <p id="home-msg">Click the button to see my enthusiasm!</p>
      <button className="btn btn-primary" onClick={showEnthusiasm}>
        Show Enthusiasm
      </button>
    </div>
  );
}

export default Home;
