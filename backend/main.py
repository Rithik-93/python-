import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from controllers.uploadHandler import uploadController
from configs import config

app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-video/")
def upload_video(file: UploadFile = File(...), title: str = Form(...), descriptipn: str = Form(...)):
    uploads_dir = config.UPLOADS_DIR
    print('main1---------------')
    video = uploadController(title, descriptipn, file, uploads_dir)
    print('main9---------------')
    print(video)
    return {"filename": file.filename, "message": "Video uploaded successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
