from sqlalchemy.orm import scoped_session, sessionmaker
from models import engine

# Create a Singleton Session
SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

# Dependency function for database access
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide session to the request
    finally:
        db.close()  # Close after use
