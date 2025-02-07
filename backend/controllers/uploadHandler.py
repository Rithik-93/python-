import os
from fastapi import UploadFile
from sqlalchemy.orm import Session
from helper import extract_audio
from deepgram_client import speech_to_text
from embedding import generateEmbedding
from insert import insert_video
from singleton import get_db
from models import Video

def uploadController(title: str, description: str, file: UploadFile, uploadDir: str) -> Video:
    """Handles video uploads, extracts audio, generates embeddings, and inserts into DB."""

    print('main2---------------')
    try:
        video_dir = os.path.join(uploadDir, "videos")
        audio_dir = os.path.join(uploadDir, "audios")
        os.makedirs(video_dir, exist_ok=True)
        os.makedirs(audio_dir, exist_ok=True)

        video_file_path = os.path.join(video_dir, f"upload_{file.filename}")
        with open(video_file_path, "wb") as buffer:
            content = file.file.read()
            buffer.write(content)
        
        print(f"✅ Video uploaded: {file.filename} ({len(content)} bytes)")

        audio_file_path = os.path.join(audio_dir, "upload.mp3")
        print('main3---------------')
        print(video_file_path, audio_file_path)
        extract_audio(video_file_path, audio_file_path)
        print('main4---------------')
        print(f"🎵 Audio extracted: {audio_file_path}")
        tempAudio = './harvard.wav'

        audio_transcript: str = speech_to_text(tempAudio)
        # if not audio_transcript:
        #     raise ValueError("Failed to generate audio transcript")

        print('main7---------------')
        print(audio_transcript)
        audio_embedding = generateEmbedding(audio_transcript)
        print(audio_embedding)
        title_embedding = generateEmbedding(title)
        description_embedding = generateEmbedding(description)
        print("🔢 Embeddings generated successfully")

        db = next(get_db())

        print('inserting')
        video = insert_video(db, title, title_embedding, description, description_embedding, audio_transcript, audio_embedding)
        print('inserting----------')
        print(f"Video inserted into DB: {video.id}")

        return video

    except Exception as e:
        print(f"❌ Error in uploadController: {str(e)}")
        return None
