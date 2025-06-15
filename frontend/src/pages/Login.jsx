import React, { useState } from 'react';
import API from '../api/api';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await API.post('token/', { username, password });
      localStorage.setItem('token', response.data.token);
      window.location.href = '/dashboard';
    } catch (err) {
      setError('Błędny login lub hasło');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-sm">
        <h1 className="text-2xl mb-6 font-bold text-center">CRM Piastpol - Logowanie</h1>
        {error && <div className="mb-4 text-red-600">{error}</div>}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block mb-1">Login</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full border rounded px-3 py-2"
            />
          </div>
          <div className="mb-6">
            <label className="block mb-1">Hasło</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full border rounded px-3 py-2"
            />
          </div>
          <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
            Zaloguj
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
