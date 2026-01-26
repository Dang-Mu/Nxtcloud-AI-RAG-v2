import React from 'react';
import '../styles/Modal.css';

interface DocumentDeleteProps {
  isOpen: boolean;
  documentTitle: string;
  onConfirm: () => Promise<void>;
  onCancel: () => void;
  isLoading: boolean;
}

export const DocumentDelete: React.FC<DocumentDeleteProps> = ({
  isOpen,
  documentTitle,
  onConfirm,
  onCancel,
  isLoading
}) => {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>문서 삭제 확인</h2>
        <p>
          <strong>"{documentTitle}"</strong> 문서를 정말 삭제하시겠습니까?
        </p>
        <p className="warning">⚠️ 이 작업은 되돌릴 수 없습니다</p>
        <div className="modal-actions">
          <button
            onClick={onCancel}
            disabled={isLoading}
            className="modal-button cancel"
          >
            취소
          </button>
          <button
            onClick={onConfirm}
            disabled={isLoading}
            className="modal-button confirm"
          >
            {isLoading ? '삭제 중...' : '삭제'}
          </button>
        </div>
      </div>
    </div>
  );
};
