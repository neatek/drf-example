import React from 'react'
import axios from 'axios';
import { useState } from 'react';
import { useNavigate } from "react-router-dom";
import Utils from '../utils/utils';


function LoginPage() {
    const [User, setUser] = useState({ login: '', password: '' });
    const navigate = useNavigate();

    let handleSubmit = (e) => {
        console.log(e.target);
        get_token(User.login, User.password);
        e.preventDefault();
    }

    let get_token = function (username, password) {
        console.log('get_token');
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
          username: username,
          password: password
        })
          .then(response => {
            console.log(response.data);
            localStorage.setItem('token', response.data.token);
            navigate("/users", { replace: true });
          }).catch(error => alert('Неверный логин или пароль'))
    }

    let checkLogin = function() {
        if(Utils.is_authenticated()) {
            navigate("/users", { replace: true });
        }
    }

    if(Utils.is_authenticated()) {
        navigate("/users", { replace: true });
    }

    return (
        <form onLoad={checkLogin} onSubmit={handleSubmit}>
            <input type="text" name="login" placeholder="login"
                value={User.login} onChange={e => { setUser({...User, login: e.target.value}) }} />
            <input type="password" name="password" placeholder="password"
                value={User.password} onChange={e => { setUser({...User, password: e.target.value}) }} />
            <input type="submit" value="Login" />
        </form>
    );

}
export default LoginPage;