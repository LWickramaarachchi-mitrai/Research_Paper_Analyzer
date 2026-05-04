import { useState } from "react";
import { analyzePaper, ResearchPaper } from "../api/api";

type Props = {
  file: File | null;
};

export default function Analyze({ file }: Props) {
  const [result, setResult] = useState<ResearchPaper | null>(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!file) return alert("Upload first");

    try {
      setLoading(true);
      const res = await analyzePaper(file);
      setResult(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 border rounded-xl shadow mt-4">
      <button
        onClick={handleAnalyze}
        className="bg-green-500 text-white px-4 py-2 rounded"
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div className="mt-4 space-y-2">
          <h2 className="text-xl font-bold">{result.title}</h2>
          <p><b>Authors:</b> {result.authors.join(", ")}</p>
          <p><b>Abstract:</b> {result.abstract}</p>
          <p><b>Problem:</b> {result.problem_statement}</p>
          <p><b>Methodology:</b> {result.methodology}</p>
          <p><b>Results:</b> {result.results}</p>
          <p><b>Conclusion:</b> {result.conclusion}</p>
        </div>
      )}
    </div>
  );
}