import { useState } from "react";
import { uploadFile } from "../api/api";

export default function Upload({ setUploaded, setFile }) {
  const [localFile, setLocalFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  const handleUpload = async () => {
    if (!localFile) return alert("Upload a PDF");

    try {
      setLoading(true);
      setProgress(0);

      await uploadFile(localFile, (event) => {
        const percent = Math.round(
          (event.loaded * 100) / event.total
        );
        setProgress(percent); // 🔥 update progress
      });

      setFile(localFile);
      setUploaded(true);
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 border rounded-xl shadow">
      <h2 className="text-xl font-bold mb-2">Upload Paper</h2>

      <input
        type="file"
        onChange={(e) => setLocalFile(e.target.files[0])}
        disabled={loading}
        className="mb-3"
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className={`px-4 py-2 rounded text-white ${
          loading ? "bg-gray-400" : "bg-blue-500"
        }`}
      >
        {loading ? "Uploading..." : "Upload"}
      </button>

      {/* 🔥 Progress Bar */}
      {loading && (
        <div className="mt-4">
          <div className="w-full bg-gray-200 rounded-full h-3">
            <div
              className="bg-blue-500 h-3 rounded-full transition-all duration-300"
              style={{ width: `${progress}%` }}
            />
          </div>
          <p className="text-sm mt-1 text-gray-600">
            {progress}%
          </p>
        </div>
      )}
    </div>
  );
}