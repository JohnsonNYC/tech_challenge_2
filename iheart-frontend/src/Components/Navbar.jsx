import React from 'react';
import { Link } from 'react-router-dom'

const Navbar = () => {
    return (
        <div className='navbar'>
            <Link className='link' to='/'>Homepage</Link>
            <Link className='link' to='/songs' >Songs</Link>
        </div>
    );
}

export default Navbar;