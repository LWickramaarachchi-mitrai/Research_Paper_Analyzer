// src/components/Chat.jsx
import { useState } from "react";
import { chatWithPaper } from "../api/api";
import { v4 as uuidv4 } from "uuid";

export default function Chat({ enabled }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [threadId] = useState(uuidv4());

  const sendMessage = async () => {
    if (!input) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);

    try {
      const res = await chatWithPaper(input, threadId);

      setMessages([
        ...newMessages,
        { role: "assistant", content: res.data.response },
      ]);
    } catch (err) {
      console.error(err);
    }

    setInput("");
  };

  return (
    <div className="p-4 border rounded-xl shadow mt-4 flex flex-col h-[400px]">
      <h2 className="text-xl font-bold mb-2">Chat with Paper</h2>

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
            {msg.content}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border p-2 rounded"
          placeholder="Ask about the paper..."
          disabled={!enabled}
        />

        <button
          onClick={sendMessage}
          className="bg-purple-500 text-white px-4 py-2 rounded"
          disabled={!enabled}
        >
          Send
        </button>
      </div>
    </div>
  );
}