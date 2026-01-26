import React, { useState, useEffect } from 'react';
import { Document } from '../types';
import '../styles/GuidelineForm.css';

interface GuidelineFormProps {
  document: Document | null;
  isOpen: boolean;
  onSave: (docId: number, guidelines: any) => Promise<void>;
  onClose: () => void;
  isLoading: boolean;
}

export const GuidelineForm: React.FC<GuidelineFormProps> = ({
  document,
  isOpen,
  onSave,
  onClose,
  isLoading
}) => {
  const [topics, setTopics] = useState<string[]>([]);
  const [examples, setExamples] = useState<string[]>([]);
  const [newTopic, setNewTopic] = useState('');
  const [newExample, setNewExample] = useState('');

  useEffect(() => {
    if (document) {
      setTopics(document.queryable_topics);
      setExamples(document.example_questions);
    }
  }, [document, isOpen]);

  const handleAddTopic = () => {
    if (newTopic.trim() && !topics.includes(newTopic.trim())) {
      setTopics([...topics, newTopic.trim()]);
      setNewTopic('');
    }
  };

  const handleRemoveTopic = (idx: number) => {
    setTopics(topics.filter((_, i) => i !== idx));
  };

  const handleAddExample = () => {
    if (newExample.trim() && !examples.includes(newExample.trim())) {
      setExamples([...examples, newExample.trim()]);
      setNewExample('');
    }
  };

  const handleRemoveExample = (idx: number) => {
    setExamples(examples.filter((_, i) => i !== idx));
  };

  const handleSave = async () => {
    if (!document) return;
    try {
      await onSave(document.id, {
        queryable_topics: topics,
        example_questions: examples
      });
      onClose();
    } catch (error) {
      console.error('Save error:', error);
      alert('저장 실패');
    }
  };

  if (!isOpen || !document) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content guideline-form">
        <h2>가이드라인 편집</h2>
        <p className="doc-title">📄 {document.title}</p>

        <div className="form-section">
          <h3>질문 가능 주제</h3>
          <div className="tag-input">
            <input
              type="text"
              value={newTopic}
              onChange={(e) => setNewTopic(e.target.value)}
              placeholder="주제 입력"
              onKeyPress={(e) => {
                if (e.key === 'Enter') {
                  e.preventDefault();
                  handleAddTopic();
                }
              }}
              disabled={isLoading}
            />
            <button
              type="button"
              onClick={handleAddTopic}
              disabled={isLoading}
              className="add-button"
            >
              +
            </button>
          </div>
          <div className="tags">
            {topics.map((topic, idx) => (
              <span key={idx} className="tag">
                {topic}
                <button
                  type="button"
                  onClick={() => handleRemoveTopic(idx)}
                  disabled={isLoading}
                  className="remove-tag"
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        </div>

        <div className="form-section">
          <h3>예시 질문</h3>
          <div className="tag-input">
            <input
              type="text"
              value={newExample}
              onChange={(e) => setNewExample(e.target.value)}
              placeholder="예시 질문 입력"
              onKeyPress={(e) => {
                if (e.key === 'Enter') {
                  e.preventDefault();
                  handleAddExample();
                }
              }}
              disabled={isLoading}
            />
            <button
              type="button"
              onClick={handleAddExample}
              disabled={isLoading}
              className="add-button"
            >
              +
            </button>
          </div>
          <div className="tags">
            {examples.map((example, idx) => (
              <span key={idx} className="tag">
                {example}
                <button
                  type="button"
                  onClick={() => handleRemoveExample(idx)}
                  disabled={isLoading}
                  className="remove-tag"
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        </div>

        <div className="modal-actions">
          <button
            onClick={onClose}
            disabled={isLoading}
            className="modal-button cancel"
          >
            취소
          </button>
          <button
            onClick={handleSave}
            disabled={isLoading}
            className="modal-button confirm"
          >
            {isLoading ? '저장 중...' : '저장'}
          </button>
        </div>
      </div>
    </div>
  );
};
