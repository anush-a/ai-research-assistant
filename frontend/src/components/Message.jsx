function Message({ type, text }) {
  return (
    <div className={`message ${type}`}>
      <b>{type === "user" ? "You: " : "AI: "}</b>
      {text}
    </div>
  );
}

export default Message;