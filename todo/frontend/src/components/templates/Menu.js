import React from 'react'
import { Link } from 'react-router-dom';
import Utils from '../utils/utils';
import { useNavigate } from "react-router-dom";

const Menu = () => {
    const navigate = useNavigate();

    let logout = () => {
        localStorage.removeItem('token');
        navigate("/login", { replace: true });
    }

    return (
        <nav>
            <li><Link to='/'>Index</Link></li>
            <li><Link to='/users'>Users</Link></li>
            <li><Link to='/todo'>Todo</Link></li>
            <li><Link to='/project'>Projects</Link></li>
            <li>{Utils.is_authenticated() ? <button onClick={()=> logout()}>Logout</button> :<Link to='/login'>Login</Link>}</li>
        </nav>
    )
}
export default Menu;