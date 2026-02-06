import React from 'react';

function Contact() {
  function showEnthusiasm() {
    document.getElementById('contact-msg').innerText =
      'Hello from React! I love this page!';
    document.getElementById('contact-heading').style.backgroundColor = 'lightblue';
  }

  return (
    <div className="card p-4 mb-4">
      <h1 id="contact-heading">Contact</h1>
      <p>This is the Contact Page</p>
      <p id="contact-msg">Click the button to see my enthusiasm!</p>
      <button className="btn btn-primary" onClick={showEnthusiasm}>
        Show Enthusiasm
      </button>
    </div>
  );
}

export default Contact;
