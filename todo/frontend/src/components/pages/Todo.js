import React from 'react'
import Menu from '../templates/Menu';
import Todo from '../Todo';

const TodoPage = () => {
    return (
        <div>
            <Menu />
            <Todo />
            <Menu />
        </div>
    )
}
export default TodoPage;