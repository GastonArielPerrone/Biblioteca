import React from 'react';

const PrestamosList = ({ prestamos }) => {
    return (
        <div className="card bg-dark text-white">
            <div className="card-header"><h3>Préstamos Activos</h3></div>
            <div className="card-body">
                <table className="table table-dark table-striped table-hover">
                    <thead>
                        <tr>
                            <th>Libro</th>
                            <th>Usuario</th>
                            <th>Fecha de Préstamo</th>
                            <th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        {prestamos.map(prestamo => (
                            <tr key={prestamo.id_prestamo}>
                                <td>{prestamo.id_libro.titulo_libro}</td>
                                <td>{prestamo.id_usuario.nombre_usuario}</td>
                                <td>{new Date(prestamo.fecha_prestamo).toLocaleDateString()}</td>
                                <td><span className="badge bg-warning text-dark">{prestamo.estado}</span></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default PrestamosList;