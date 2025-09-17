import React from 'react';
import { Navigate } from 'react-router-dom';
import authService from '../../services/authService';

const PrivateRoute = ({ children }) => {
    const currentUser = authService.getCurrentUser();

    if (!currentUser) {
        // Not logged in, redirect to login page
        return <Navigate to="/login" replace />;
    }

    return children;
};

export default PrivateRoute;