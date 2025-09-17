import React from 'react';
import { Link } from 'react-router-dom';

const Header = ({ currentUser, logOut }) => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container">
                <Link className="navbar-brand" to="/">Biblioteca Comunal 13</Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        {currentUser && (
                            <li className="nav-item">
                                <Link className="nav-link" to="/">Gestión de Préstamos</Link>
                            </li>
                        )}
                        <li className="nav-item">
                            <Link className="nav-link" to="/registrar-usuario">Registrar Usuario</Link>
                        </li>
                    </ul>
                    <ul className="navbar-nav ms-auto">
                        {currentUser ? (
                            <li className="nav-item">
                                <a href="/login" className="nav-link" onClick={logOut}>Logout</a>
                            </li>
                        ) : (
                            <>
                                <li className="nav-item">
                                    <Link className="nav-link" to="/login">Login</Link>
                                </li>
                                <li className="nav-item">
                                    <Link className="nav-link" to="/registrar-empleado">Registrar Empleado</Link>
                                </li>
                            </>
                        )}
                    </ul>
                </div>
            </div>
        </nav>
    );
}

export default Header;