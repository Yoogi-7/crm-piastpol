import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import API from '../api/api';

const DeliveryDetails = () => {
  const { id } = useParams();
  const [delivery, setDelivery] = useState(null);

  useEffect(() => {
    const fetchDelivery = async () => {
      try {
        const token = localStorage.getItem('access');
        const response = await API.get(`deliveries/${id}/`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        setDelivery(response.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchDelivery();
  }, [id]);

  if (!delivery) {
    return <div className="p-8">Loading delivery details...</div>;
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Delivery Details</h1>
      <p><strong>Date:</strong> {delivery.delivery_date}</p>
      <p><strong>Driver:</strong> {delivery.driver}</p>
      <p><strong>Delivery Address:</strong> {delivery.delivery_address}</p>

      <div className="mt-4">
        <h2 className="text-xl font-semibold mb-2">Additional Products:</h2>
        {delivery.additional_products.length > 0 ? (
          <ul className="list-disc pl-5">
            {delivery.additional_products.map(product => (
              <li key={product.id}>
                {product.name} - Quantity: {product.quantity}
              </li>
            ))}
          </ul>
        ) : (
          <p>No additional products.</p>
        )}
      </div>

      <div className="mt-4">
        <Link to="/dashboard" className="bg-blue-600 text-white px-4 py-2 rounded">Back to Dashboard</Link>
      </div>
    </div>
  );
};

export default DeliveryDetails;
