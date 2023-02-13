import React from 'react'

const ProjectItem = ({ item, deleteBook}) => {
    return (
        <tr>
            <td>
                <a href="#not_enough_time">{item.name}</a>
            </td>
            <td><button type='button' onClick={()=>deleteBook(item.id)}>Delete</button></td>
        </tr>
    )
}


const ProjectList = ({ items, deleteBook, createBook }) => {

    let handleSubmit = () => {
        console.log("Submit");
        let name = document.querySelector("#project_name").value;
        createBook(name);
        // event.preventDefault();
    }

    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>
                            name
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {items.map((data) => <ProjectItem key={data.name} item={data} deleteBook={(id)=>deleteBook(data.id)} />)}
                </tbody>
            </table>

            <form onSubmit={(event)=> handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">name</label>
                    <input type="text" id="project_name" className="form-control" name="name" />
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>

        </div>


    )
}
export default ProjectList;
