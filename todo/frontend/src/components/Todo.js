import React from 'react';
import axios from 'axios';
import TodoList from './templates/TodoList';


class Todo extends React.Component {
    state = { 'todo': [] };

    loadTodo = () => {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                console.log(response.data);
                this.setState({ 'todo': response.data.results });
                console.log(this.state.todo);
            }).catch(error => console.log(error));
    }

    deleteTodo = (id) => {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        console.log("deletebok");
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers})
        .then(response => {
            this.loadTodo();
        }).catch(error => console.log(error))
    }

    createTodo(name) {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        const data = {
            task: name,
            status: 1,
            deadline: '1990-01-02',
            user: 'http://127.0.0.1:8000/api/users/1/',
            project: 'http://127.0.0.1:8000/api/project/3/'
        }
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers})
        .then(response => {
            this.loadTodo();
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.loadTodo();
    }

    componentWillUnmount() {
    }

    render() {
        return (
            <div>
                <TodoList items={this.state.todo} deleteTodo={this.deleteTodo} createTodo={this.createTodo} />
            </div>
        )
    }
}
export default Todo;