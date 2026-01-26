import React, { useState } from 'react';
import { DocumentUploadRequest } from '../types';
import '../styles/DocumentUpload.css';

interface DocumentUploadProps {
  onUpload: (data: DocumentUploadRequest) => Promise<void>;
  isLoading: boolean;
}

export const DocumentUpload: React.FC<DocumentUploadProps> = ({
  onUpload,
  isLoading
}) => {
  const [file, setFile] = useState<File | null>(null);
  const [progress, setProgress] = useState(0);
  const [message, setMessage] = useState<{ text: string; type: 'success' | 'error' } | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) {
      setMessage({ text: '파일을 선택해주세요', type: 'error' });
      setTimeout(() => setMessage(null), 3000);
      return;
    }

    try {
      setProgress(50);
      await onUpload({
        file,
        title: file.name,
        description: '',
        category: '',
        queryable_topics: [],
        example_questions: []
      });
      setProgress(100);

      setMessage({ text: '✅ 업로드 성공!', type: 'success' });
      setFile(null);
      setTimeout(() => setProgress(0), 1000);
      setTimeout(() => setMessage(null), 3000);
    } catch (error) {
      console.error('Upload error:', error);
      setMessage({ text: '❌ 업로드 실패', type: 'error' });
      setProgress(0);
      setTimeout(() => setMessage(null), 3000);
    }
  };

  return (
    <div className="document-upload">
      <h3>📤 새 문서 업로드</h3>
      <form onSubmit={handleSubmit} className="upload-form">
        <div className="form-group">
          <label>파일 선택</label>
          <div className="file-input-wrapper">
            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
              disabled={isLoading}
              id="file-input"
              className="file-input"
            />
            <label htmlFor="file-input" className="file-label">
              {file ? `✓ ${file.name}` : '📁 PDF 파일 선택'}
            </label>
          </div>
        </div>

        {progress > 0 && (
          <div className="progress-bar">
            <div className="progress" style={{ width: `${progress}%` }}></div>
          </div>
        )}

        <button type="submit" disabled={isLoading || !file} className="submit-button">
          {isLoading ? '📤 업로드 중...' : '📤 업로드'}
        </button>

        {message && (
          <div className={`message ${message.type}`} style={{ marginTop: '10px' }}>
            {message.text}
          </div>
        )}
      </form>
    </div>
  );
};
