import React, { useState, useEffect } from 'react';

function App() {
  const [name, setName] = useState('Guest');
  useEffect(() => {
    console.log(`Welcome ${name}`);
  }, [name]);

  return (
    <div>
      <p>Welcome {name}</p>
      <button onClick={() => setName('Alice')}>Login as Alice</button>
    </div>
  );
}
export default App;