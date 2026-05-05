import { useEffect, useState } from "react";
import { getThreads, deleteThread } from "../api/api";

type Props = {
  selectedThread: string | null;
  setThreadId: (id: string) => void;
};

export default function SideBar({ selectedThread, setThreadId }: Props) {
  const [threads, setThreads] = useState<string[]>([]);

  const loadThreads = async () => {
    const res = await getThreads();
    setThreads(res.data.threads);
  };

  useEffect(() => {
    loadThreads();
  }, []);

  const handleDelete = async (threadId: string) => {
    if (!confirm("Delete this chat?")) return;

    await deleteThread(threadId);

    // remove from UI
    setThreads((prev) => prev.filter((t) => t !== threadId));

    // reset selection if deleted
    if (selectedThread === threadId) {
      setThreadId(null);
    }
  };

  return (
    <div className="w-64 bg-gray-100 p-4 h-full flex flex-col">
      <button
        onClick={() => setThreadId(crypto.randomUUID())}
        className="bg-blue-500 text-white p-2 rounded mb-4"
      >
        + New Chat
      </button>

      <div className="flex-1 overflow-y-auto space-y-2">
        {threads.map((t) => (
          <div
            key={t}
            className={`flex justify-between items-center p-2 rounded cursor-pointer ${
              selectedThread === t
                ? "bg-blue-300"
                : "bg-white hover:bg-gray-200"
            }`}
            onClick={() => setThreadId(t)}
          >
            <span>{t.slice(0, 8)}...</span>

            {/* 🗑 Delete Button */}
            <button
              onClick={(e) => {
                e.stopPropagation(); // prevent selecting thread
                handleDelete(t);
              }}
              className="text-red-500 hover:text-red-700"
            >
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}