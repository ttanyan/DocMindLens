import axios from 'axios';

const baseURL = import.meta.env.VITE_MINERU_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL,
  timeout: 300000,
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

export const parseFile = async (files, options) => {
  const formData = new FormData();
  files.forEach(file => formData.append('files', file));
  
  Object.entries(options).forEach(([key, value]) => {
    if (value !== undefined && value !== null) {
      formData.append(key, value);
    }
  });
  
  return api.post('/file_parse', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const submitTask = async (files, options) => {
  const formData = new FormData();
  files.forEach(file => formData.append('files', file));
  
  Object.entries(options).forEach(([key, value]) => {
    if (value !== undefined && value !== null) {
      formData.append(key, value);
    }
  });
  
  return api.post('/tasks', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const getTaskStatus = async (taskId) => {
  return api.get(`/tasks/${taskId}`);
};

export const getTaskResult = async (taskId) => {
  return api.get(`/tasks/${taskId}/result`, {
    responseType: 'blob',
  });
};

export const healthCheck = async () => {
  return api.get('/health');
};

export default api;