import { useEffect, useState } from "react";
import { chatWithPaper, getChatHistory, ChatMessage } from "../api/api";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

type Props = {
  threadId: string | null;
};

export default function Chat({ threadId }: Props) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  // Load history
  useEffect(() => {
    if (!threadId) return;

    const load = async () => {
      try {
        const res = await getChatHistory(threadId);
        setMessages(res.data.messages);
      } catch (err) {
        console.error(err);
      }
    };

    load();
  }, [threadId]);

  const sendMessage = async () => {
    if (!input || !threadId) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    try {
      const res = await chatWithPaper(input, threadId);

      setMessages([
        ...newMessages,
        { role: "assistant", content: res.response }
      ]);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (!threadId) {
    return <div className="p-4">Select or create a chat</div>;
  }

  return (
    <div className="flex flex-col h-[400px] p-4 border rounded-xl">
      <div className="flex-1 overflow-y-auto space-y-2 mb-2">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`p-2 rounded ${
              msg.role === "user"
                ? "bg-blue-100 text-right"
                : "bg-gray-200 text-left"
            }`}
          >
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
    {msg.content}
  </ReactMarkdown>
          </div>
        ))}

        {loading && (
          <div className="text-sm text-gray-500">Thinking...</div>
        )}
      </div>

      <div className="flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border p-2 rounded"
          placeholder="Ask something..."
        />
        <button
          onClick={sendMessage}
          className="bg-purple-500 text-white px-4 py-2 rounded"
        >
          Send
        </button>
      </div>
    </div>
  );
}