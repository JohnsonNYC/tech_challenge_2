// import './App.css';
import React, {useState,useEffect} from 'react';
import {Route,Switch} from 'react-router-dom'

//COMPONENTS
import Homepage from './Components/Homepage'
import SongContainer from './Components/SongContainer'


function App() {
  const [songs, setSongs] = useState([{'johnson':'OldTimeRoad'}])

  // useEffect(()=>{
  //   fetch(//enter URL HERE)
  //     .then(resp => resp.json)
  //     .then(songs => setSongs(songs))
  // })

  return (
    <div className="App">
      <Switch>
        <Route path='/songs' render={(routerProps) => <SongContainer {...routerProps} songs={songs}/>}/>
        <Route exact path='/' component={Homepage}/>
      </Switch>
    </div>
  );
}

export default App;
