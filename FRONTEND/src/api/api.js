
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const uploadFile = (file, onUploadProgress) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post("http://127.0.0.1:8000/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
    onUploadProgress, 
  });
};

export const analyzePaper = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`${BASE_URL}/analyze`, formData);
};

export const chatWithPaper = (message, thread_id) => {
  return axios.post(`${BASE_URL}/chat`, {
    message,
    thread_id,
  });
};