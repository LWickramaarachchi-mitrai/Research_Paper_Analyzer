import { useState } from "react";
import { uploadFile } from "../api/api";

type Props = {
  setUploaded: (val: boolean) => void;
  setFile: (file: File | null) => void;
};

export default function Upload({ setUploaded, setFile }: Props) {
  const [file, setLocalFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  const handleUpload = async () => {
    if (!file) return alert("Upload a PDF");

    try {
      setLoading(true);

      await uploadFile(file, (event) => {
        const percent = Math.round(
          (event.loaded! * 100) / (event.total || 1)
        );
        setProgress(percent);
      });

      setFile(file);
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
        onChange={(e) => setLocalFile(e.target.files?.[0] || null)}
        disabled={loading}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="bg-blue-500 text-white px-4 py-2 rounded mt-2"
      >
        {loading ? "Uploading..." : "Upload"}
      </button>

      {loading && (
        <div className="mt-3">
          <div className="w-full bg-gray-200 h-3 rounded">
            <div
              className="bg-blue-500 h-3 rounded"
              style={{ width: `${progress}%` }}
            />
          </div>
          <p>{progress}%</p>
        </div>
      )}
    </div>
  );
}