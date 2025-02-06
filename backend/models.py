from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector
from configs import config
import uuid

DATABASE_URL = config.DB_URL
print(f"Connecting to database: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class Video(Base):
    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    title_embedding = Column(Vector(768), nullable=False)
    description = Column(Text, nullable=True)
    description_embedding = Column(Vector(768), nullable=False)
    audio_transcript = Column(Text, nullable=False)
    audio_embedding = Column(Vector(768), nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("✅ Database schema created successfully!")
