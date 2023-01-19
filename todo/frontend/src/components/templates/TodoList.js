import React from 'react'


const TodoItem = ({ item }) => {
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
        </tr>
    )
}

const TodoList = ({ items }) => {
    return (
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
                {items.map((data) => <TodoItem key={data.task} item={data} />)}
            </tbody>
        </table>
    )
}
export default TodoList;
