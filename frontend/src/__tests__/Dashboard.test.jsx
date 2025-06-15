import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { AuthContext } from '../context/AuthContext';
import Dashboard from '../pages/Dashboard';
import { vi } from 'vitest';
import API from '../api/api';
import '@testing-library/jest-dom';
import { MemoryRouter } from 'react-router-dom';

vi.mock('../api/api', () => ({
  default: {
    get: vi.fn()
  }
}));

describe('Dashboard Page', () => {
  const mockProfile = {
    username: 'clientuser',
    role: 'client',
    client_info: {
      name: 'Test Client',
      nip: '1234567890',
      email: 'client@example.com',
      phone: '123456789'
    }
  };

  const mockDeliveries = [
    { id: 1, delivery_date: '2025-06-14', driver: 'Driver 1' },
    { id: 2, delivery_date: '2025-06-10', driver: 'Driver 2' }
  ];

  beforeEach(() => {
    vi.spyOn(window.localStorage.__proto__, 'getItem').mockImplementation((key) => {
      if (key === 'access') return 'mock_token';
      return null;
    });

    API.get.mockImplementation((url) => {
      if (url.includes('users/profile')) {
        return Promise.resolve({ data: mockProfile });
      }
      if (url.includes('deliveries')) {
        return Promise.resolve({ data: mockDeliveries });
      }
      return Promise.reject(new Error('not found'));
    });
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  test('renders dashboard with client info and deliveries', async () => {
    render(
      <AuthContext.Provider value={{ user: mockProfile, logout: vi.fn() }}>
        <MemoryRouter>
          <Dashboard />
        </MemoryRouter>
      </AuthContext.Provider>
    );

    await waitFor(() => {
      expect(screen.getByText(/Test Client/i)).toBeInTheDocument();
      expect(screen.getByText(/Driver 1/i)).toBeInTheDocument();
      expect(screen.getByText(/Driver 2/i)).toBeInTheDocument();
    });
  });
});
