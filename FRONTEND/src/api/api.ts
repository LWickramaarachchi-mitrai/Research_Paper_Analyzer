import axios, { AxiosProgressEvent } from "axios";

const BASE_URL = "http://127.0.0.1:8000";

// ---- Types ----

export type ResearchPaper = {
  title: string;
  authors: string[];
  abstract: string;
  problem_statement: string;
  methodology: string;
  results: string;
  conclusion: string;
};

export type UploadResponse = {
  message: string;
};

export type ChatResponse = {
  response: string;
};

// ---- API ----

// Upload
export const uploadFile = async (
  file: File,
  onUploadProgress?: (event: AxiosProgressEvent) => void
): Promise<UploadResponse> => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${BASE_URL}/upload`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
    onUploadProgress,
  });

  return res.data;
};

// Analyze
export const analyzePaper = async (
  file: File
): Promise<ResearchPaper> => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${BASE_URL}/analyze`, formData);
  return res.data;
};

// Chat
export const chatWithPaper = async (
  message: string,
  thread_id: string
): Promise<ChatResponse> => {
  const res = await axios.post(`${BASE_URL}/chat`, {
    message,
    thread_id,
  });

  return res.data;
};