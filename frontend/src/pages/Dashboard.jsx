import React, { useEffect, useState, useContext } from 'react';
import API from '../api/api';
import { AuthContext } from '../context/AuthContext';

const Dashboard = () => {
  const { user, logout } = useContext(AuthContext);
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem('access');
        const response = await API.get('users/profile/', {
          headers: { Authorization: `Bearer ${token}` }
        });
        setProfile(response.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchProfile();
  }, []);

  if (!profile) {
    return <div className="p-8">Loading...</div>;
  }

  const client = profile.client_info || {};

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-2xl font-bold">CRM Piastpol — Client Dashboard</h1>
        <button onClick={logout} className="bg-red-600 text-white px-4 py-2 rounded">Log out</button>
      </div>

      <div className="bg-white p-6 rounded shadow mb-6">
        <h2 className="text-xl font-semibold mb-4">Client Info</h2>
        {profile.role === 'client' ? (
          <>
            <p><strong>Name:</strong> {client.name}</p>
            <p><strong>NIP:</strong> {client.nip}</p>
            <p><strong>Email:</strong> {client.email}</p>
            <p><strong>Phone:</strong> {client.phone}</p>
          </>
        ) : (
          <p>This is not a client account.</p>
        )}
      </div>

      <div className="bg-white p-6 rounded shadow">
        <h2 className="text-xl font-semibold mb-4">Delivery Info (mock data)</h2>
        <p>Full bottles: 12</p>
        <p>Dispensers: 4</p>
        <p>Last delivery: 2025-06-14</p>
      </div>
    </div>
  );
};

export default Dashboard;
