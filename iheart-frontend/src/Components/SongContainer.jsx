import React from 'react';
import SongItem from './SongItem'

const SongContainer = (props) => {
    const { songs, handleClick, reset } = props
    console.log(props)
    return (
        <div className='song-container'>
            <table>
                <thead>
                    <tr>
                        <td onClick={handleClick}>Title</td>
                        <td onClick={handleClick}>Artist</td>
                        <td onClick={handleClick}>Genre</td>
                        <td onClick={handleClick}>Year</td>
                    </tr>
                </thead>
                <tbody>
                    {songs.map((song) => {
                        return <SongItem key={song.id} song={song} {...props} />
                    })}
                </tbody>
            </table>
            <div className='reset'>
                <button onClick={reset}>Reset!</button>
            </div>
        </div>
    );
}

export default SongContainer;