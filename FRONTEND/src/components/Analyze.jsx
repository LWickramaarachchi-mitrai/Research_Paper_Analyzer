
import { useState } from "react";
import { analyzePaper } from "../api/api";

export default function Analyze({ file }) {
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    try {
      const res = await analyzePaper(file);
      setResult(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="p-4 border rounded-xl shadow mt-4">
      <h2 className="text-xl font-bold mb-2">Analyze Paper</h2>

      <button
        onClick={handleAnalyze}
        className="bg-green-500 text-white px-4 py-2 rounded mb-4"
      >
        Analyze
      </button>

      {result && (
        <div className="space-y-3">
          <h3 className="text-2xl font-bold">{result.title}</h3>

          <p><b>Authors:</b> {result.authors.join(", ")}</p>
          <p><b>Abstract:</b> {result.abstract}</p>
          <p><b>Methodology:</b> {result.methodology}</p>
          <p><b>Results:</b> {result.results}</p>
          <p><b>Conclusion:</b> {result.conclusion}</p>
        </div>
      )}
    </div>
  );
}