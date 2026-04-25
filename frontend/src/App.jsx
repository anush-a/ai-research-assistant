import Upload from "./components/Upload";
import Chat from "./components/Chat";
import "./app.css";

function App() {
  return (
    <div className="app">
      <h1>📄 AI Research Assistant</h1>
      <Upload />
      <Chat />
    </div>
  );
}

export default App;