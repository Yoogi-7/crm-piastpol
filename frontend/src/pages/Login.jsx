// src/pages/Login.jsx
import React from 'react';

const Login = () => {
  const handleSubmit = (e) => {
    e.preventDefault();
    // tutaj w kolejnym kroku zrobimy logowanie przez API
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-sm">
        <h1 className="text-2xl mb-6 font-bold text-center">CRM Piastpol - Logowanie</h1>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block mb-1">Login</label>
            <input type="text" className="w-full border rounded px-3 py-2" />
          </div>
          <div className="mb-6">
            <label className="block mb-1">Hasło</label>
            <input type="password" className="w-full border rounded px-3 py-2" />
          </div>
          <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">Zaloguj</button>
        </form>
      </div>
    </div>
  );
};

export default Login;