import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import TodoPage from './pages/Todo';
import ProjectPage from './pages/Projects';
import NotFound404 from './templates/Notfound';
import Users from './pages/Users';

const MyRoutes = () => {
  return (
    <Routes>
      <Route exact path='/' element={<Home />} />
      <Route path='/users' element={<Users />}/>
      <Route path='/todo' element={<TodoPage />}/>
      <Route path='/project' element={<ProjectPage />}/>
      <Route path="*" element={<NotFound404 />}/>
    </Routes>
  );
}
export default MyRoutes;