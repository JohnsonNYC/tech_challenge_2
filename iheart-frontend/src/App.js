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

  const handleClick = (e) => {

    let attr = e.target.innerText.toLowerCase();

    let sortedSongs = songs.sort(function (a, b) {
      return ('' + a[attr]).localeCompare(b[attr]);
    })

    setSongs(sortedSongs) // Why does my sort not work?
  }

  return (
    <div className="App">
      <Navbar />
      <Switch>
        <Route path='/songs' render={(routerProps) => <SongContainer {...routerProps} songs={songs} handleClick={handleClick} />} />
        <Route exact path='/' component={Homepage} />
      </Switch>
    </div>
  );
}

export default App;
