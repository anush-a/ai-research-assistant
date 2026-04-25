import axios from "axios";
import { useState } from "react";

function Upload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setStatus("❌ Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setStatus("Uploading...");
      await axios.post("http://127.0.0.1:5000/upload", formData);
      setStatus("✅ File uploaded successfully");
    } catch (error) {
      setStatus("❌ Upload failed");
      console.error(error);
    }
  };

  return (
  <div className="upload-box">
    <h3>Upload PDF</h3>

    <input
      type="file"
      accept=".pdf"
      onChange={(e) => setFile(e.target.files[0])}
    />

    <button onClick={handleUpload}>Upload</button>

    <p>{status}</p>
  </div>
);
}

export default Upload;