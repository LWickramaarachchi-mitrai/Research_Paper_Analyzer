
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const uploadFile = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`${BASE_URL}/upload`, formData);
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