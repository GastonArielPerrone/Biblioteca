import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import GestionPrestamosPage from './pages/GestionPrestamosPage';
import RegistroUsuarioPage from './pages/RegistroUsuarioPage';
import RegistroEmpleadoPage from './pages/RegistroEmpleadoPage';
import LoginPage from './pages/LoginPage';
import StockLibrosPage from './pages/StockLibrosPage';
import PrivateRoute from './components/common/PrivateRoute';
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
            {/* Public Routes */}
            <Route path="/login" element={<LoginPage />} />
            <Route path="/registrar-usuario" element={<RegistroUsuarioPage />} />
            <Route path="/registrar-empleado" element={<RegistroEmpleadoPage />} />

            {/* Protected Routes */}
            <Route path="/" element={
              <PrivateRoute>
                <GestionPrestamosPage />
              </PrivateRoute>
            } />
            <Route path="/stock-libros" element={
              <PrivateRoute>
                <StockLibrosPage />
              </PrivateRoute>
            } />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;