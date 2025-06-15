import React, { useEffect, useState, useContext } from 'react';
import API from '../api/api';
import { AuthContext } from '../context/AuthContext';

const Dashboard = () => {
  const { user, logout } = useContext(AuthContext);
  const [profile, setProfile] = useState(null);
  const [deliveries, setDeliveries] = useState([]);

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

    const fetchDeliveries = async () => {
      try {
        const token = localStorage.getItem('access');
        const response = await API.get('deliveries/', {
          headers: { Authorization: `Bearer ${token}` }
        });
        setDeliveries(response.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchProfile();
    fetchDeliveries();
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
        <h2 className="text-xl font-semibold mb-4">Deliveries</h2>
        {deliveries.length > 0 ? (
          <table className="w-full border-collapse">
            <thead>
              <tr className="border-b">
                <th className="text-left p-2">Date</th>
                <th className="text-left p-2">Driver</th>
              </tr>
            </thead>
            <tbody>
              {deliveries.map(delivery => (
                <tr key={delivery.id} className="border-b">
                  <td className="p-2">{delivery.delivery_date}</td>
                  <td className="p-2">{delivery.driver}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>No deliveries found.</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
