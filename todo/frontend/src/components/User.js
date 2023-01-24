import React from 'react';
import axios from 'axios';
import UserList from './templates/UserList';


class User extends React.Component {
    state = { 'users': [] };

    componentDidMount() {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                console.log(response.data);
                this.setState({ 'users': response.data.results });
                console.log(this.state.users);
            }).catch(error => console.log(error));
    }

    componentWillUnmount() {
    }

    render() {
        return (
            <div>
                <UserList items={this.state.users} />
            </div>
        )
    }
}
export default User;