import { useState } from "react";

export default function VideoUpload() {
  const [video, setVideo] = useState<File | null>(null);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleVideoChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      setVideo(event.target.files[0]);
    }
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (!video || !title) {
      alert("Please provide a title and video.");
      return;
    }

    const formData = new FormData();
    formData.append("file", video);
    formData.append("title", title);
    formData.append("descriptipn", description);

    try {
      const response = await fetch("http://localhost:8000/upload-video", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      alert(data.message);
    } catch (error) {
      console.error("Upload failed", error);
      alert("Failed to upload video.");
    }
  };

  return (
    <div className="max-w-lg mx-auto p-6 bg-white shadow-md rounded-lg">
      <h2 className="text-xl font-semibold mb-4">Upload Video</h2>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
        <input
          type="text"
          placeholder="Video Title"
          className="border p-2 rounded"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <textarea
          placeholder="Video Description"
          className="border p-2 rounded"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <input type="file" accept="video/*" onChange={handleVideoChange} required />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
          Upload
        </button>
      </form>
    </div>
  );
}
