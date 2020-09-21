import React, { useState, useEffect } from 'react';



const SongProfile = (props) => {
    const { URL } = props
    const [song, setSong] = useState({})

    async function fetchSong() {
        const res = await fetch(`${URL}/${props.match.params.id}`);
        res.json()
            .then(song => setSong(song))
    }

    useEffect(() => {
        fetchSong()
    }, [])

    return (
        <div className='song-profile'>
            <h1> {song.title}</h1>
            <h2> {song.artist}</h2>
            <h3> {song.year}</h3>
        </div>
    );
}

export default SongProfile;