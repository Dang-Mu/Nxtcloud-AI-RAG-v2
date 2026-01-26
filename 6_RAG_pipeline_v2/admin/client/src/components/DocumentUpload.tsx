import { useState } from 'react';
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
    } catch {
      setMessage({ text: '❌ 업로드 실패', type: 'error' });
      setProgress(0);
      setTimeout(() => setMessage(null), 3000);
    }
  };

  return (
    <div className="document-upload">
      <h3>문서 업로드</h3>
      <form onSubmit={handleSubmit} className="upload-form">
        <div
          className={`file-drop-zone ${file ? 'has-file' : ''}`}
          onClick={() => document.getElementById('file-input')?.click()}
        >
          <input
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
            disabled={isLoading}
            id="file-input"
            hidden
          />
          <span className="drop-zone-icon">{file ? '✅' : '📄'}</span>
          <span className="drop-zone-text">
            {file ? file.name : 'PDF 파일을 선택하세요'}
          </span>
          {!file && <span className="drop-zone-hint">최대 용량 20MB</span>}
        </div>

        {progress > 0 && (
          <div className="upload-progress-container">
            <div className="progress-label">
              <span>업로드 중...</span>
              <span>{progress}%</span>
            </div>
            <div className="progress-bar-modern">
              <div className="progress-fill" style={{ width: `${progress}%` }}></div>
            </div>
          </div>
        )}

        <button type="submit" disabled={isLoading || !file} className="btn-upload">
          {isLoading ? '업로드 중...' : '데이터 베이스에 추가하기'}
        </button>

        {message && (
          <div className={`upload-message ${message.type}`}>
            {message.text}
          </div>
        )}
      </form>
    </div>
  );
};
