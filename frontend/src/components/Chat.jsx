import axios from "axios";
import { useState } from "react";

function Chat() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question) return;

    const updatedMessages = [
      ...messages,
      { type: "user", text: question },
    ];

    setMessages(updatedMessages);
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:5000/ask", {
        question: question,
      });

      setMessages([
        ...updatedMessages,
        { type: "bot", text: res.data.answer },
      ]);
    } catch (error) {
      setMessages([
        ...updatedMessages,
        { type: "bot", text: "❌ Error fetching response" },
      ]);
      console.error(error);
    }

    setQuestion("");
    setLoading(false);
  };

  return (
  <div className="chat-container">
    <h3>Ask Questions</h3>

    <div className="chat-box">
      {messages.map((msg, i) => (
        <div key={i} className={`message ${msg.type}`}>
          <b>{msg.type === "user" ? "You: " : "AI: "}</b>
          {msg.text}
        </div>
      ))}

      {loading && <p className="loading">✨ AI is thinking...</p>}
    </div>

    <div className="input-area">
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
        onKeyDown={(e) => e.key === "Enter" && askQuestion()}
      />
      <button onClick={askQuestion}>Send</button>
    </div>
  </div>
);
}

export default Chat;