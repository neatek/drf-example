import React from 'react';
import axios from 'axios';
import ProjectList from './templates/ProjectList';


class Project extends React.Component {
    state = { 'project': [] };

    loadProjects = () => {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        axios.get('http://127.0.0.1:8000/api/project/', {headers})
            .then(response => {
                console.log(response.data);
                this.setState({ 'project': response.data.results });
                console.log(this.state.project);
            }).catch(error => console.log(error));
    }

    loadProjectsByName = (name) => {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        axios.get('http://127.0.0.1:8000/api/project/?search='+name, {headers})
            .then(response => {
                console.log(response.data);
                this.setState({ 'project': response.data.results });
                console.log(this.state.project);
            }).catch(error => console.log(error));
    }

    deleteBook = (id) => {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        console.log("deletebok");
        axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers})
        .then(response => {
            this.loadProjects();
        }).catch(error => console.log(error))
    }

    createBook(name) {
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token')
        };
        const data = {name: name}
        axios.post(`http://127.0.0.1:8000/api/project/`, data, {headers})
        .then(response => {
            this.loadProjects();
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.loadProjects();
    }

    componentWillUnmount() {
    }

    handleSubmit = (event) => {
        console.log("Submit");
        let project_name = document.querySelector("#project_name_search").value;
        console.log("search", project_name);
        this.loadProjectsByName(project_name);
        event.preventDefault();
    }

    render() {
        return (
            <div>
                <ProjectList items={this.state.project} deleteBook={this.deleteBook} createBook={this.createBook} />

                <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">search_by_name</label>
                    <input type="text" id="project_name_search" className="form-control" name="name" />
                </div>
                <input type="submit" className="btn btn-primary" value="Search" />
            </form>
            </div>
        )
    }
}
export default Project;