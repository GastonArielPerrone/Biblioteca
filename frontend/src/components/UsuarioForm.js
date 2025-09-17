import React, { useState } from 'react';
import axios from 'axios';

const UsuarioForm = () => {
    const initialFormData = {
        nombre_usuario: '',
        dni: '',
        telefono: '',
        calle: '',
        numero_calle: '',
        casa: false,
        edificio: false,
        piso: '',
        departamento_numero_casa: ''
    };

    const [formData, setFormData] = useState(initialFormData);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === 'checkbox' ? checked : value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/api/usuarios/', formData)
            .then(response => {
                alert('Usuario registrado con éxito!');
                setFormData(initialFormData); // Reset form
            })
            .catch(error => {
                console.error('Error registrando usuario:', error.response.data);
                // Construct a user-friendly error message
                const errors = error.response.data;
                let errorMessage = "Hubo un error al registrar el usuario:";
                for (const key in errors) {
                    errorMessage += `\n- ${key}: ${errors[key].join(' ')}`;
                }
                alert(errorMessage);
            });
    };

    return (
        <div className="card bg-dark text-white">
            <div className="card-header"><h3>Registrar Nuevo Usuario</h3></div>
            <div className="card-body">
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label">Nombre de Usuario</label>
                        <input type="text" className="form-control" name="nombre_usuario" value={formData.nombre_usuario} onChange={handleChange} required />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">DNI</label>
                        <input type="text" className="form-control" name="dni" value={formData.dni} onChange={handleChange} required />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Teléfono</label>
                        <input type="text" className="form-control" name="telefono" value={formData.telefono} onChange={handleChange} />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Calle</label>
                        <input type="text" className="form-control" name="calle" value={formData.calle} onChange={handleChange} />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Número</label>
                        <input type="number" className="form-control" name="numero_calle" value={formData.numero_calle} onChange={handleChange} />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Piso</label>
                        <input type="text" className="form-control" name="piso" value={formData.piso} onChange={handleChange} />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Departamento/Casa</label>
                        <input type="text" className="form-control" name="departamento_numero_casa" value={formData.departamento_numero_casa} onChange={handleChange} />
                    </div>
                    <div className="form-check mb-3">
                        <input className="form-check-input" type="checkbox" name="casa" checked={formData.casa} onChange={handleChange} />
                        <label className="form-check-label">Casa</label>
                    </div>
                    <div className="form-check mb-3">
                        <input className="form-check-input" type="checkbox" name="edificio" checked={formData.edificio} onChange={handleChange} />
                        <label className="form-check-label">Edificio</label>
                    </div>
                    <button type="submit" className="btn btn-success">Registrar Usuario</button>
                </form>
            </div>
        </div>
    );
};

export default UsuarioForm;
