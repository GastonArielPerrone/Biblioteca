import React, { useState } from 'react';
import axios from 'axios';

const EmpleadoForm = () => {
    const initialFormData = {
        nombre_empleado: '',
        dni: '',
        password: '',
        telefono: '',
        cargo: ''
    };

    const [formData, setFormData] = useState(initialFormData);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/api/empleados/registrar/', formData)
            .then(response => {
                alert('¡Empleado registrado con éxito!');
                setFormData(initialFormData); // Reset form
            })
            .catch(error => {
                console.error('Error registrando empleado:', error.response.data);
                const errors = error.response.data;
                let errorMessage = "Hubo un error al registrar el empleado:";
                for (const key in errors) {
                    errorMessage += `\n- ${key}: ${errors[key].join(' ')}`;
                }
                alert(errorMessage);
            });
    };

    return (
        <div className="card bg-dark text-white">
            <div className="card-header"><h3>Registrar Nuevo Empleado</h3></div>
            <div className="card-body">
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label">Nombre Completo</label>
                        <input type="text" className="form-control" name="nombre_empleado" value={formData.nombre_empleado} onChange={handleChange} required />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">DNI</label>
                        <input type="text" className="form-control" name="dni" value={formData.dni} onChange={handleChange} required />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Contraseña</label>
                        <input type="password" class="form-control" name="password" value={formData.password} onChange={handleChange} required />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Teléfono</label>
                        <input type="text" className="form-control" name="telefono" value={formData.telefono} onChange={handleChange} />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Cargo</label>
                        <input type="text" className="form-control" name="cargo" value={formData.cargo} onChange={handleChange} />
                    </div>
                    <button type="submit" className="btn btn-success">Registrar Empleado</button>
                </form>
            </div>
        </div>
    );
};

export default EmpleadoForm;
