import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import axios from 'axios';
import TodoPage from './pages/Todo';
import ProjectPage from './pages/Projects';
import NotFound404 from './templates/Notfound';
import Users from './pages/Users';
import LoginPage from './pages/Login';

const MyRoutes = () => {
  return (
    <Routes>
      <Route path='/' element={<LoginPage />} />
      <Route path='/users' element={<Users />} />
      <Route path='/todo' element={<TodoPage />} />
      <Route path='/project' element={<ProjectPage />} />
      <Route path='/login' element={<LoginPage />} />
      <Route path="*" element={<NotFound404 />} />
    </Routes>
  );
}
export default MyRoutes;