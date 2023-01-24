import React from 'react'
import { Link } from 'react-router-dom';

const Menu = () => {
    return (
        <nav>
            <li><Link to='/'>Index</Link></li>
            <li><Link to='/users'>Users</Link></li>
            <li><Link to='/todo'>Todo</Link></li>
            <li><Link to='/project'>Projects</Link></li>
        </nav>
    )
}
export default Menu;