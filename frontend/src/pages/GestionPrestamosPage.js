import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PrestamosList from '../components/PrestamosList';
import PrestamoForm from '../components/PrestamoForm';

const GestionPrestamosPage = () => {
    const [prestamos, setPrestamos] = useState([]);

    const fetchPrestamos = () => {
        axios.get('http://127.0.0.1:8000/api/prestamos/')
            .then(response => {
                setPrestamos(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the prestamos!', error);
            });
    }

    useEffect(() => {
        fetchPrestamos();
    }, []);

    const handlePrestamoAdded = (newPrestamo) => {
        fetchPrestamos();
    };

    return (
        <div className="container mt-4">
            <div className="row">
                <div className="col-md-4">
                    <PrestamoForm onPrestamoAdded={handlePrestamoAdded} />
                </div>
                <div className="col-md-8">
                    <PrestamosList prestamos={prestamos} />
                </div>
            </div>
        </div>
    );
}

export default GestionPrestamosPage;