import React, { useState } from 'react';
import { Document } from '../types';
import '../styles/DocumentList.css';

interface DocumentListProps {
  documents: Document[];
  onDelete: (docId: number) => Promise<void>;
  onEdit: (doc: Document) => void;
  isLoading: boolean;
}

export const DocumentList: React.FC<DocumentListProps> = ({
  documents,
  onDelete,
  onEdit,
  isLoading
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCategory, setFilterCategory] = useState<string>('');
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
    } catch (error) {
      console.error('Delete error:', error);
      setMessage({ text: '삭제 실패', type: 'error' });
      setTimeout(() => setMessage(null), 2000);
    }
  };

  const handleCancelDelete = () => {
    setDeleteConfirm(null);
  };

  return (
    <div className="document-list">
      <h3>📋 등록된 문서</h3>

      {filteredDocs.length === 0 ? (
        <div className="empty-state">
          <div className="empty-icon">📂</div>
          <p>등록된 문서가 없습니다</p>
          <p className="empty-hint">새 문서를 업로드해주세요</p>
        </div>
      ) : (
        <>
          <div className="filter-bar">
             <input
               type="text"
               placeholder="문서 검색..."
               value={searchTerm}
               onChange={(e) => setSearchTerm(e.target.value)}
               className="search-input"
             />
           </div>
         <div className="table-wrapper">
           <table className="documents-table">
             <thead>
               <tr>
                 <th>#</th>
                 <th>파일명</th>
                 <th>청크 개수</th>
                 <th>업로드일</th>
                 <th>작업</th>
               </tr>
             </thead>
             <tbody>
               {filteredDocs.map((doc, idx) => (
                 <tr key={doc.id}>
                   <td>{idx + 1}</td>
                   <td>
                     <div className="doc-title">
                       <p className="title">{doc.title}</p>
                     </div>
                   </td>
                   <td>
                     <span className="category-badge">{doc.chunk_count}</span>
                   </td>
                   <td>
                     {doc.created_at
                       ? new Date(doc.created_at).toLocaleDateString('ko-KR')
                       : '-'}
                   </td>
                   <td>
                     <div className="actions">
                       <button
                         onClick={() => handleDeleteClick(doc.id)}
                         disabled={isLoading}
                         className="delete-btn"
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
        </>
      )}

      {message && (
        <div className={`message ${message.type}`}>
          {message.text}
        </div>
      )}

      {deleteConfirm !== null && (
        <div className="modal-overlay">
          <div className="modal-dialog">
            <h4>삭제 확인</h4>
            <p>정말 삭제하시겠습니까?</p>
            <div className="modal-actions">
              <button
                onClick={() => handleConfirmDelete(deleteConfirm)}
                className="confirm-btn"
              >
                삭제
              </button>
              <button
                onClick={handleCancelDelete}
                className="cancel-btn"
              >
                취소
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
