import React from 'react';
import { UserPage } from './pages/UserPage';
import './styles/globals.css';

function App() {
  return (
    <div className="app-container">
      <nav className="app-nav">
        <div className="nav-logo">
          <h1>📚 RAG 사용자 서비스</h1>
        </div>
      </nav>

      <main className="app-main">
        <UserPage />
      </main>

      <footer className="app-footer">
        <p>&copy; 2024 RAG Chatbot v2 - User. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
