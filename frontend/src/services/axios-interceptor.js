import axios from 'axios';
import authService from './authService';

const setupAxiosInterceptors = () => {
    axios.interceptors.request.use(
        config => {
            const user = authService.getCurrentUser();
            if (user && user.access) {
                config.headers['Authorization'] = 'Bearer ' + user.access;
            }
            return config;
        },
        error => {
            return Promise.reject(error);
        }
    );
};

export default setupAxiosInterceptors;
