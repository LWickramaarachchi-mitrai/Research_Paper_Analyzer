// src/components/Upload.jsx
import { useState } from "react";
import { uploadFile } from "../api/api";

export default function Upload({ setUploaded, setFile }) {
  const [localFile, setLocalFile] = useState(null);

  const handleUpload = async () => {
    if (!localFile) return alert("Upload a PDF");

    try {
      await uploadFile(localFile);
      setFile(localFile);        // 🔥 send file to parent
      setUploaded(true);
      alert("Uploaded!");
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    }
  };

  return (
    <div className="p-4 border rounded-xl shadow">
      <h2 className="text-xl font-bold mb-2">Upload Paper</h2>

      <input
        type="file"
        onChange={(e) => setLocalFile(e.target.files[0])}
        className="mb-3"
      />

      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Upload
      </button>
    </div>
  );
}