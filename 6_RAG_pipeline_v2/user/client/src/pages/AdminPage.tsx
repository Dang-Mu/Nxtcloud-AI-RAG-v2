import React, { useState, useEffect } from 'react';
import { Document, DocumentUploadRequest } from '../types';
import { DocumentUpload } from '../components/DocumentUpload';
import { DocumentList } from '../components/DocumentList';
import { apiClient } from '../services/api';
import '../styles/AdminPage.css';

export const AdminPage: React.FC = () => {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    loadDocuments();
  }, []);

  const loadDocuments = async () => {
    try {
      setIsLoading(true);
      const docs = await apiClient.getAdminDocuments();
      setDocuments(docs);
    } catch (error) {
      console.error('Failed to load documents:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleUpload = async (data: DocumentUploadRequest) => {
    try {
      setIsLoading(true);
      const response = await apiClient.uploadDocument(data);
      if (response.status === 'success') {
        await loadDocuments();
      } else {
        throw new Error(response.message);
      }
    } catch (error) {
      console.error('Upload error:', error);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async (docId: number) => {
    try {
      setIsLoading(true);
      const response = await apiClient.deleteDocument(docId);
      if (response.status === 'success') {
        await loadDocuments();
      } else {
        throw new Error(response.message);
      }
    } catch (error) {
      console.error('Delete error:', error);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="admin-page">
      <header className="admin-header">
        <h1>📚 문서 관리</h1>
      </header>

      <div className="admin-content">
        <DocumentUpload onUpload={handleUpload} isLoading={isLoading} />
        <DocumentList
          documents={documents}
          onDelete={handleDelete}
          onEdit={() => {}}
          isLoading={isLoading}
        />
      </div>
    </div>
  );
};
