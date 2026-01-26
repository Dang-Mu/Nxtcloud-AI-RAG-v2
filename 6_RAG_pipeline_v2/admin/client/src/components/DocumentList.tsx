import { useState } from 'react';
import { Document } from '../types';
import '../styles/DocumentList.css';

interface DocumentListProps {
  documents: Document[];
  onDelete: (docId: number) => Promise<void>;
  isLoading: boolean;
}

export const DocumentList: React.FC<DocumentListProps> = ({
  documents,
  onDelete,
  isLoading
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [deleteConfirm, setDeleteConfirm] = useState<number | null>(null);
  const [message, setMessage] = useState<{ text: string; type: 'success' | 'error' } | null>(null);

  const filteredDocs = documents.filter((doc) => {
    const matchesSearch = doc.title.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesSearch;
  });

  const handleDeleteClick = (docId: number) => {
    setDeleteConfirm(docId);
  };

  const handleConfirmDelete = async (docId: number) => {
    try {
      await onDelete(docId);
      setMessage({ text: '삭제되었습니다', type: 'success' });
      setDeleteConfirm(null);
      setTimeout(() => setMessage(null), 2000);
    } catch {
      setMessage({ text: '삭제 실패', type: 'error' });
      setTimeout(() => setMessage(null), 2000);
    }
  };

  const handleCancelDelete = () => {
    setDeleteConfirm(null);
  };

  return (
    <div className="document-list">
      <div className="list-header">
        <h3>등록된 문서 목록</h3>
        <div className="search-container">
          <span className="search-icon">🔍</span>
          <input
            type="text"
            placeholder="문서 제목으로 검색..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      {filteredDocs.length === 0 ? (
        <div className="empty-state">
          <span className="empty-state-icon">📂</span>
          <p className="empty-state-text">검색 결과가 없거나 등록된 문서가 없습니다.</p>
        </div>
      ) : (
        <div className="table-container">
          <table className="modern-table">
            <thead>
              <tr>
                <th>문서 정보</th>
                <th>청크</th>
                <th>상태</th>
                <th>등록일</th>
                <th>관리</th>
              </tr>
            </thead>
            <tbody>
              {filteredDocs.map((doc) => (
                <tr key={doc.id}>
                  <td>
                    <div className="doc-info">
                      <span className="doc-name">{doc.title}</span>
                      <span className="doc-meta">ID: {doc.id}</span>
                    </div>
                  </td>
                  <td>
                    <span className="chunk-badge">{doc.chunk_count} chunks</span>
                  </td>
                  <td>
                    <span className="status-badge status-ready">준비됨</span>
                  </td>
                  <td>
                    {doc.created_at
                      ? new Date(doc.created_at).toLocaleDateString('ko-KR')
                      : '-'}
                  </td>
                  <td>
                    <div className="action-buttons">
                      <button
                        className="btn-icon btn-delete"
                        onClick={() => handleDeleteClick(doc.id)}
                        disabled={isLoading}
                        title="삭제"
                      >
                        🗑️
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {message && (
        <div className={`notification ${message.type}`}>
          {message.text}
        </div>
      )}

      {deleteConfirm !== null && (
        <div className="modal-overlay">
          <div className="modal-card">
            <div className="modal-header">
              <h4>문서 삭제</h4>
              <button onClick={handleCancelDelete} className="close-btn">&times;</button>
            </div>
            <div className="modal-body">
              <p>이 문서를 삭제하시겠습니까? 삭제 후에는 복구할 수 없습니다.</p>
            </div>
            <div className="modal-footer">
              <button
                onClick={handleCancelDelete}
                className="btn-secondary"
              >
                취소
              </button>
              <button
                onClick={() => handleConfirmDelete(deleteConfirm)}
                className="btn-danger"
              >
                삭제하기
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
