// src/App.jsx
import { useState } from "react";
import Upload from "../components/Upload";
import Analyze from "../components/Analyze";
import Chat from "../components/Chat";

export default function MainApp() {
  const [uploaded, setUploaded] = useState(false);
  const [file, setFile] = useState(null);

  return (
    <div className="max-w-5xl mx-auto p-6 space-y-4">
      <h1 className="text-3xl font-bold"> Research Assistant</h1>

      <Upload
        setUploaded={setUploaded}
        setFile={setFile}   
      />

      
      {uploaded && file && <Analyze file={file} />}

      
      {uploaded && <Chat enabled={true} />}
    </div>
  );
}