import './App.css';
import React, { useState, useEffect } from 'react';
import { Route, Switch } from 'react-router-dom'

//COMPONENTS
import Homepage from './Components/Homepage'
import SongContainer from './Components/SongContainer'
import Navbar from './Components/Navbar'

//API 
const URL = 'http://localhost:5000/song'

function App() {
  const [songs, setSongs] = useState([])

  async function fetchData() {
    const res = await fetch(URL);
    res.json()
      .then(songs => setSongs(songs))
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <div className="App">
      <Navbar />
      <Switch>
        <Route path='/songs' render={(routerProps) => <SongContainer {...routerProps} songs={songs} />} />
        <Route exact path='/' component={Homepage} />
      </Switch>
    </div>
  );
}

export default App;
