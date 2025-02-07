from models import Video
from sqlalchemy.orm import Session
import uuid

def insert_video(db: Session, title: str, title_embedding: list, description: str, 
                 description_embedding: list, audio_transcript: str, audio_embedding: list):
    
    new_video = Video(
        id=uuid.uuid4(),
        title=title,
        title_embedding=title_embedding,
        description=description,
        description_embedding=description_embedding,
        audio_transcript=audio_transcript,
        audio_embedding=audio_embedding
    )

    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video
