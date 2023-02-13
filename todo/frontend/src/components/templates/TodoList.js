import React from 'react'


const TodoItem = ({ item, deleteTodo }) => {
    return (
        <tr>
            <td>
                {item.task}
            </td>
            <td>
                {item.status}
            </td>
            <td>
                {item.deadline}
            </td>
            <td><button type='button' onClick={()=>deleteTodo(item.id)}>Delete</button></td>
        </tr>
    )
}

const TodoList = ({ items, deleteTodo, createTodo }) => {

    let handleSubmit = () => {
        console.log("Submit");
        let task = document.querySelector("#todo_task").value;
        createTodo(task);
        // event.preventDefault();
    }

    return (
        <div>

<table>
            <thead>
                <tr>
                    <th>
                        task
                    </th>
                    <th>
                        status
                    </th>
                    <th>
                        deadline
                    </th>
                </tr>
            </thead>
            <tbody>
                {items.map((data) => <TodoItem key={data.task} item={data} deleteTodo={(id)=>deleteTodo(data.id)} />)}
            </tbody>
        </table>
<form onSubmit={(event)=> handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">name</label>
                    <input type="text" id="todo_task" className="form-control" name="name" />
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        </div>

    )
}
export default TodoList;
