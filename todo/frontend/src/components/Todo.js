import React from 'react';
import axios from 'axios';
import TodoList from './templates/TodoList';


class Todo extends React.Component {
    state = { 'todo': [] };

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                console.log(response.data);
                this.setState({ 'todo': response.data.results });
                console.log(this.state.todo);
            }).catch(error => console.log(error));
    }

    componentWillUnmount() {
    }

    render() {
        return (
            <div>
                <TodoList items={this.state.todo} />
            </div>
        )
    }
}
export default Todo;