import React, { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);
  const[name,setName]=useState('');


  useEffect(() => {
    console.log(`Count changed to ${count} and the name is set as ${name}`);
    // Do something here after the count state value changes
  }, [name]);

  return (
    <div>
      <p>Count: {count}</p>
      
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <input type='text' value={name} onChange={(e)=>setName(e.target.value)}></input>
    </div>
  );
}
export default App;