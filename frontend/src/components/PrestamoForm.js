import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PrestamoForm = ({ onPrestamoAdded }) => {
    const [libros, setLibros] = useState([]);
    const [usuarios, setUsuarios] = useState([]);
    const [selectedLibro, setSelectedLibro] = useState('');
    const [selectedUsuario, setSelectedUsuario] = useState('');

    useEffect(() => {
        // Fetch libros
        axios.get('http://127.0.0.1:8000/api/libros/')
            .then(response => {
                setLibros(response.data);
                if (response.data.length > 0) {
                    setSelectedLibro(response.data[0].id_libro);
                }
            })
            .catch(error => console.error('Error fetching libros:', error));

        // Fetch usuarios
        axios.get('http://127.0.0.1:8000/api/usuarios/')
            .then(response => {
                setUsuarios(response.data);
                if (response.data.length > 0) {
                    setSelectedUsuario(response.data[0].id_usuario);
                }
            })
            .catch(error => console.error('Error fetching usuarios:', error));
    }, []);

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post('http://127.0.0.1:8000/api/prestamos/', {
            id_libro: selectedLibro,
            id_usuario: selectedUsuario
        })
        .then(response => {
            alert('¡Préstamo agregado con éxito!');
            onPrestamoAdded(response.data);
        })
        .catch(error => {
            console.error('Error adding prestamo:', error.response.data);
            alert('Hubo un error al agregar el préstamo.');
        });
    };

    return (
        <div className="card bg-dark text-white mb-4">
            <div className="card-header"><h3>Registrar Nuevo Préstamo</h3></div>
            <div className="card-body">
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="libroSelect" className="form-label">Libro</label>
                        <select id="libroSelect" className="form-select" value={selectedLibro} onChange={e => setSelectedLibro(e.target.value)}>
                            {libros.map(libro => (
                                <option key={libro.id_libro} value={libro.id_libro}>
                                    {libro.titulo_libro}
                                </option>
                            ))}
                        </select>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="usuarioSelect" className="form-label">Usuario</label>
                        <select id="usuarioSelect" className="form-select" value={selectedUsuario} onChange={e => setSelectedUsuario(e.target.value)}>
                            {usuarios.map(usuario => (
                                <option key={usuario.id_usuario} value={usuario.id_usuario}>
                                    {usuario.nombre_usuario}
                                </option>
                            ))}
                        </select>
                    </div>
                    <button type="submit" className="btn btn-primary">Guardar Préstamo</button>
                </form>
            </div>
        </div>
    );
}

export default PrestamoForm;