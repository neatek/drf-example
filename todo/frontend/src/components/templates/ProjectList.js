import React from 'react'


const ProjectItem = ({ item }) => {
    return (
        <tr>
            <td>
                <a href="#not_enough_time">{item.name}</a>
            </td>
        </tr>
    )
}

const ProjectList = ({ items }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        name
                    </th>
                </tr>
            </thead>
            <tbody>
                {items.map((data) => <ProjectItem key={data.name} item={data} />)}
            </tbody>
        </table>
    )
}
export default ProjectList;
