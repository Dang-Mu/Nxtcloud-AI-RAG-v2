import React, { useState, useEffect } from 'react';
import { Message, Document } from '../types';
import { ChatInterface } from '../components/ChatInterface';
import { apiClient } from '../services/api';
import '../styles/UserPage.css';

export const UserPage: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [documents, setDocuments] = useState<Document[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId] = useState(`user_${Date.now()}`);

  useEffect(() => {
    loadDocuments();
  }, []);

   const loadDocuments = async () => {
     try {
       const docs = await apiClient.getDocuments();
       setDocuments(Array.isArray(docs) ? docs : []);
     } catch (error) {
       console.error('Failed to load documents:', error);
       setDocuments([]);
     }
   };

  const handleSendMessage = async (query: string) => {
    const userMessage: Message = {
      id: `msg_${Date.now()}_user`,
      type: 'user',
      content: query,
      timestamp: new Date()
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await apiClient.chat({
        query,
        session_id: sessionId
      });

      const assistantMessage: Message = {
        id: `msg_${Date.now()}_assistant`,
        type: 'assistant',
        content: response.response,
        timestamp: new Date(),
        sources: response.sources
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Chat error:', error);
      const errorMessage: Message = {
        id: `msg_${Date.now()}_error`,
        type: 'assistant',
        content: '죄송합니다. 질문 처리 중 오류가 발생했습니다.',
        timestamp: new Date()
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearHistory = async () => {
    try {
      await apiClient.clearChatHistory(sessionId);
      setMessages([]);
    } catch (error) {
      console.error('Clear history error:', error);
    }
  };

  return (
    <div className="user-page">
      <aside className="app-sidebar">
        <div className="sidebar-header">
          <h2>📚 문서 목록</h2>
        </div>
        {documents.length === 0 ? (
          <div className="no-docs">
            <p>등록된 문서가 없습니다</p>
          </div>
        ) : (
          <div className="documents-list">
            {documents.map((doc) => (
              <div key={doc.id} className="document-item">
                <div className="doc-icon">📄</div>
                <div className="doc-info">
                  <h4>{doc.title}</h4>
                  <span className="doc-meta">
                    {doc.chunk_count} chunks • {new Date(doc.created_at).toLocaleDateString('ko-KR')}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </aside>

      <main className="chat-layout">
        <header className="chat-header">
          <div className="header-content">
            <h1>RAG Chat Assistant</h1>
            <span className="status-badge">Online</span>
          </div>
          <p className="subtitle">문서 기반 질의응답 시스템</p>
        </header>

        <div className="chat-container-wrapper">
          <ChatInterface
            messages={messages}
            isLoading={isLoading}
            onSendMessage={handleSendMessage}
            onClearHistory={handleClearHistory}
          />
        </div>
      </main>
    </div>
  );
};
