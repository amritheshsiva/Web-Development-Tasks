import React from 'react';

function About() {
  function showEnthusiasm() {
    document.getElementById('about-msg').innerText =
      'Hello from React! I love this page!';
    document.getElementById('about-heading').style.backgroundColor = 'lightblue';
  }

  return (
    <div className="card p-4 mb-4">
      <h1 id="about-heading">About</h1>
      <p>This is the About Page</p>
      <p id="about-msg">Click the button to see my enthusiasm!</p>
      <button className="btn btn-primary" onClick={showEnthusiasm}>
        Show Enthusiasm
      </button>
    </div>
  );
}

export default About;
