import React from 'react';
import axios from 'axios';
import ProjectList from './templates/ProjectList';


class Project extends React.Component {
    state = { 'project': [] };

    componentDidMount() {
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

    componentWillUnmount() {
    }

    render() {
        return (
            <div>
                <ProjectList items={this.state.project} />
            </div>
        )
    }
}
export default Project;