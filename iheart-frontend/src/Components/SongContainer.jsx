import React from 'react';
import SongItem from './SongItem'

const SongContainer = (props) => {
    const { songs } = props

    const handleClick = () => {
        console.log('Here')
    }

    return (
        <div className='song-container'>
            <table>
                <thead>
                    <tr>
                        <td onClick={handleClick}>Title</td>
                        <td>Artist</td>
                        <td>Genre</td>
                        <td>Year</td>
                    </tr>
                </thead>
                <tbody>
                    {songs.map((song) => {
                        return <SongItem key={song.id} song={song} />
                    })}
                </tbody>
            </table>
        </div>
    );
}

export default SongContainer;