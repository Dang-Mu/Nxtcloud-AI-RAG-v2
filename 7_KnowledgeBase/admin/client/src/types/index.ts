export interface KnowledgeBase {
  readonly name: string;
  readonly kb_id: string;
  readonly ds_id: string;
  readonly bucket: string;
  readonly prefix: string;
}

export interface KBRegistrationRequest {
  name: string;
  kb_id: string;
  ds_id: string;
  bucket: string;
  prefix?: string;
}

export interface KBUploadRequest {
  kb_id: string;
  ds_id: string;
  bucket: string;
  file: File;
}

export interface KBUploadResponse {
  job_id: string;
  kb_id: string;
  ds_id: string;
}

export interface IngestStatusResponse {
  status: 'STARTING' | 'IN_PROGRESS' | 'COMPLETE' | 'FAILED' | 'ERROR';
}

export type ApiStatus = 'success' | 'error';

export interface ApiResponse<T = unknown> {
  status: ApiStatus;
  data?: T;
  message?: string;
}

export type MessageType = 'user' | 'assistant';

export interface Source {
  content: string;
  page: number;
  document_id?: number;
  document_title?: string;
}

export interface Message {
  id: string;
  type: MessageType;
  content: string;
  timestamp: Date;
  sources?: Source[];
}

export interface Session {
  readonly id: string;
  readonly created_at: Date;
  readonly last_activity: Date;
}

export interface ChatRequest {
  query: string;
  session_id: string;
}

export interface ChatResponse {
  response: string;
  sources: Source[];
}

export type DocumentStatus = 'pending' | 'processed' | 'error';

export interface Document {
  readonly id: number;
  readonly title: string;
  readonly s3_key: string;
  readonly chunk_count: number;
  readonly created_at?: string;
  readonly status?: DocumentStatus;
  readonly queryable_topics?: string[];
  readonly example_questions?: string[];
}

export interface DocumentUploadRequest {
  file: File;
  title: string;
  description?: string;
  category?: string;
  queryable_topics?: string[];
  example_questions?: string[];
}

export interface DocumentUploadResponse {
  status: 'success' | 'error';
  document_id?: number;
  message: string;
}
