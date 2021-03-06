import React from 'react'

const SongItem = (props) => {
    const { song } = props
    return (
        <tr id={song.id} onClick={() => props.history.push(`/songs/${song.id}`)} >
            <td>{song.title}</td>
            <td>{song.artist}</td>
            <td>{song.genre}</td>
            <td>{song.year}</td>
        </tr>
    )
}

export default SongItem;