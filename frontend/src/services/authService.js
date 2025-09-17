import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

const login = (dni, password) => {
    return axios
        .post(API_URL + 'token/', {
            dni,
            password
        })
        .then(response => {
            if (response.data.access) {
                localStorage.setItem('user', JSON.stringify(response.data));
            }
            return response.data;
        });
};

const logout = () => {
    localStorage.removeItem('user');
};

const getCurrentUser = () => {
    return JSON.parse(localStorage.getItem('user'));
};

const authService = {
    login,
    logout,
    getCurrentUser,
};

export default authService;