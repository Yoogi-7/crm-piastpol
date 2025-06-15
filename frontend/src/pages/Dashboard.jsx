import React from 'react';

const Dashboard = () => {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">CRM Piastpol — Dashboard klienta</h1>

      <div className="grid grid-cols-3 gap-4 mb-6">
        <div className="bg-white p-6 rounded shadow text-center">
          <h2 className="text-xl font-semibold mb-2">Pełne butle u klienta</h2>
          <p className="text-3xl font-bold text-blue-600">12</p>
        </div>

        <div className="bg-white p-6 rounded shadow text-center">
          <h2 className="text-xl font-semibold mb-2">Dystrybutory</h2>
          <p className="text-3xl font-bold text-blue-600">4</p>
        </div>

        <div className="bg-white p-6 rounded shadow text-center">
          <h2 className="text-xl font-semibold mb-2">Ostatnia dostawa</h2>
          <p className="text-lg text-gray-700">14 czerwca 2025</p>
        </div>
      </div>

      <div className="bg-white p-6 rounded shadow">
        <h2 className="text-xl font-semibold mb-4">Ostatnie dostawy</h2>
        <table className="w-full border-collapse">
          <thead>
            <tr className="border-b">
              <th className="text-left p-2">Data</th>
              <th className="text-left p-2">Pełne butle</th>
              <th className="text-left p-2">Puste butle</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b">
              <td className="p-2">2025-06-14</td>
              <td className="p-2">6</td>
              <td className="p-2">4</td>
            </tr>
            <tr className="border-b">
              <td className="p-2">2025-06-10</td>
              <td className="p-2">8</td>
              <td className="p-2">7</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;
