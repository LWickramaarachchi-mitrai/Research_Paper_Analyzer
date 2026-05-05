import { useState } from "react";
import Upload from "../components/Upload";
import Analyze from "../components/Analyze";
import Chat from "../components/Chat";
import SideBar from "../components/SideBar";

export default function MainApp() {
  const [uploaded, setUploaded] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [threadId, setThreadId] = useState<string | null>(null);

  // ✅ create new thread
  const handleNewThread = () => {
    const id = crypto.randomUUID();
    setThreadId(id);
  };

  return (
    <div className="flex h-screen">
      
      <SideBar
        selectedThread={threadId}
        onSelectThread={setThreadId}
        onNewThread={handleNewThread}
      />

      <div className="flex-1 max-w-4xl mx-auto p-6 space-y-4 overflow-y-auto">
        <h1 className="text-3xl font-bold">📄 Research Assistant</h1>

        <Upload setUploaded={setUploaded} setFile={setFile} />

        {uploaded && (
          <>
            <Analyze file={file} />
            <Chat threadId={threadId} />
          </>
        )}
      </div>
    </div>
  );
}