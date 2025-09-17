import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StockLibrosPage = () => {
    const [libros, setLibros] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/libros/')
            .then(response => {
                setLibros(response.data);
            })
            .catch(error => {
                console.error('Error fetching libros:', error);
                if (error.response && error.response.status === 401) {
                    setError('Acceso no autorizado. Por favor, inicie sesión.');
                } else {
                    setError('Hubo un error al cargar el stock de libros.');
                }
            });
    }, []);

    if (error) {
        return <div className="alert alert-danger">{error}</div>;
    }

    return (
        <div className="container mt-4">
            <div className="card bg-dark text-white">
                <div className="card-header"><h3>Stock de Libros</h3></div>
                <div className="card-body">
                    <table className="table table-dark table-striped table-hover">
                        <thead>
                            <tr>
                                <th>Título</th>
                                <th>Autor</th>
                                <th>Editorial</th>
                                <th>Categoría</th>
                                <th className="text-center">Cantidad</th>
                            </tr>
                        </thead>
                        <tbody>
                            {libros.map(libro => (
                                <tr key={libro.id_libro}>
                                    <td>{libro.titulo_libro}</td>
                                    <td>{libro.id_autor.nombre_autor}</td>
                                    <td>{libro.id_editorial.nombre_editorial}</td>
                                    <td>{libro.id_categoria.nombre_categoria}</td>
                                    <td className="text-center">{libro.cantidad}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}

export default StockLibrosPage;