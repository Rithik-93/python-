from fastapi import UploadFile, Depends
from helper import extract_audio
from deepgram_client import speech_to_text
from embedding import generateEmbedding
from sqlalchemy.orm import Session
from singleton import get_db
from insert import insert_video
from models import Video
import os

def uploadController(title: str, description: str, file: UploadFile, uploadDir: str) -> Video:
    os.makedirs(uploadDir, exist_ok=True)

    video_file_path = os.path.join(uploadDir,"/videos",f"upload_{file.fileName}")

    with open(video_file_path, "wb") as buffer:
        content = file.file.read()
        print(f"Uploaded file size: {len(content)} bytes")
        buffer.write(content)

    audio_file_path = os.path.join(uploadDir,"audios",f"upload_{file.fileName}")
    extract_audio( video_file_path, audio_file_path )

    audio_transcript = speech_to_text(audio_file_path)

    audio_embedding = generateEmbedding(audio_transcript)
    title_embedding = generateEmbedding(title)
    description_embedding = generateEmbedding(description)
    db: Session = Depends(get_db)
    video = insert_video(db, title, title_embedding, description, description_embedding, audio_transcript, audio_embedding)

    return video
