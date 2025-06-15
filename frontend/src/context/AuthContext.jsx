import React, { createContext, useState, useEffect } from 'react';
import API from '../api/api';
import jwt_decode from 'jwt-decode';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    const access = localStorage.getItem('access');
    return access ? jwt_decode(access) : null;
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(false);
  }, []);

  const login = async (username, password) => {
    const response = await API.post('token/', { username, password });
    localStorage.setItem('access', response.data.access);
    localStorage.setItem('refresh', response.data.refresh);
    setUser(jwt_decode(response.data.access));
  };

  const logout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    setUser(null);
  };

  const contextData = {
    user,
    login,
    logout,
  };

  return (
    <AuthContext.Provider value={contextData}>
      {loading ? <div>Loading...</div> : children}
    </AuthContext.Provider>
  );
};
