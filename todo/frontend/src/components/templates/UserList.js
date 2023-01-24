import React from 'react'


const UserItem = ({ item }) => {
    return (
        <tr>
            <td>
                {item.username}
            </td>
            <td>
                {item.firstname}
            </td>
            <td>
                {item.lastname}
            </td>
            <td>
                {item.email}
            </td>
        </tr>
    )
}

const UserList = ({ items }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        username
                    </th>
                    <th>
                        firstname
                    </th>
                    <th>
                        lastname
                    </th>
                    <th>
                        email
                    </th>
                </tr>
            </thead>
            <tbody>
                {items.map((data) => <UserItem key={data.email} item={data} />)}
            </tbody>
        </table>
    )
}
export default UserList;
