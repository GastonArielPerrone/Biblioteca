import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import GestionPrestamosPage from './pages/GestionPrestamosPage';
import RegistroUsuarioPage from './pages/RegistroUsuarioPage';
import RegistroEmpleadoPage from './pages/RegistroEmpleadoPage';
import LoginPage from './pages/LoginPage';
import authService from './services/authService';
import setupAxiosInterceptors from './services/axios-interceptor';

setupAxiosInterceptors();

function App() {
  const [currentUser, setCurrentUser] = useState(undefined);

  useEffect(() => {
    const user = authService.getCurrentUser();
    if (user) {
      setCurrentUser(user);
    }
  }, []);

  const logOut = () => {
    authService.logout();
    setCurrentUser(undefined);
  };

  return (
    <Router>
      <div className="App">
        <Header currentUser={currentUser} logOut={logOut} />
        <div className="content">
          <Routes>
            <Route path="/" element={<GestionPrestamosPage />} />
            <Route path="/registrar-usuario" element={<RegistroUsuarioPage />} />
            <Route path="/registrar-empleado" element={<RegistroEmpleadoPage />} />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
