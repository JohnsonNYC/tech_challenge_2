import React from 'react';
import {Link} from 'react-router-dom'

const Homepage = (props) => {
    
    return (
        <div>
            <button>
                <Link to='/'>Homepage</Link>
            </button>
            <button>
                <Link to='/songs' >Songs Container</Link>
            </button>
        </div>
    );
}

export default Homepage;