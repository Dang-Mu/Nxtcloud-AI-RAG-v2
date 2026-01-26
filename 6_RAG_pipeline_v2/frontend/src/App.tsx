import React, { useState } from 'react';
import { UserPage } from './pages/UserPage';
import { AdminPage } from './pages/AdminPage';
import './styles/globals.css';

type PageType = 'user' | 'admin';

function App() {
  const [currentPage, setCurrentPage] = useState<PageType>('user');

  return (
    <div className="app-container">
      <nav className="app-nav">
        <div className="nav-logo">
          <h1>📚 RAG 문서 Q&A</h1>
        </div>
        <div className="nav-buttons">
          <button
            className={`nav-button ${currentPage === 'user' ? 'active' : ''}`}
            onClick={() => setCurrentPage('user')}
          >
            💬 사용자 페이지
          </button>
          <button
            className={`nav-button ${currentPage === 'admin' ? 'active' : ''}`}
            onClick={() => setCurrentPage('admin')}
          >
            👨‍💼 관리자 페이지
          </button>
        </div>
      </nav>

      <main className="app-main">
        {currentPage === 'user' ? <UserPage /> : <AdminPage />}
      </main>

      <footer className="app-footer">
        <p>&copy; 2024 RAG Chatbot v2. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
