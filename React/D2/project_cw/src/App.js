import React from 'react'
function App(){
  const name="Jishnu"
  const age=20
  const isStudent=true
  const favoriteHobbies = ["Reading", "Hiking", "Coding"]
  const hobbyList=[]
  const headingColor = "lightblue"
  for(let i=0;i<favoriteHobbies.length;i++){
    hobbyList.push(<li key={i}>{favoriteHobbies[i]}</li>)
  }
  function showbutton(){
    document.getElementById('message').innerHTML='Hello from React! I love my hobbies! ';
    document.getElementById('heading').style.backgroundColor = headingColor;

  }


  return(
    <div className='container mt-5'>
      <div className='card '>
          <div className='card-body'>
            <h1 className='card-title' id='heading'>Personal Information</h1>
            <p>Name : {name}</p>
            <p>Age: {age}</p>
            <p>Student : {isStudent.toString()}</p>
          </div>
      </div>
      <div className='row'>
        <div className='col-md-6'>
          <h4>Hobby List (Using for Loop) </h4>
          <ul>{hobbyList}</ul>
        </div>
        <div className='col-md-6'>
          <h4>Hobby List (Using map() method)</h4>
          {favoriteHobbies.map((item, index) => (
            <li key={index}>{item}</li>
            )
            )
            }
        </div>
      </div>
      <button className='btn btn-primary' onClick={showbutton}>Show Enthusiasm</button>
      <br></br>
      <p id='message'>Click the button to see my enthusiasm!</p>
    </div>
    
  
  )
}
export default App