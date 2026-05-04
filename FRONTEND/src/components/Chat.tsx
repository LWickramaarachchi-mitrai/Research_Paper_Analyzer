import { useState } from "react";
import { chatWithPaper } from "../api/api";
import { v4 as uuidv4 } from "uuid";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function Chat({ enabled }: { enabled: boolean }) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [threadId] = useState(uuidv4());
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    try {
      const res = await chatWithPaper(input, threadId);

      setMessages([
        ...newMessages,
        { role: "assistant", content: res.response },
      ]);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 border rounded-xl shadow mt-4 h-[400px] flex flex-col">
      <div className="flex-1 overflow-y-auto space-y-2">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`p-2 rounded ${
              m.role === "user"
                ? "bg-blue-100 text-right"
                : "bg-gray-200"
            }`}
          >
            {m.content}
          </div>
        ))}

        {loading && <p className="text-sm">Thinking...</p>}
      </div>

      <div className="flex gap-2 mt-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={!enabled}
          className="flex-1 border p-2 rounded"
        />
        <button
          onClick={sendMessage}
          disabled={!enabled || loading}
          className="bg-purple-500 text-white px-4 py-2 rounded"
        >
          Send
        </button>
      </div>
    </div>
  );
}