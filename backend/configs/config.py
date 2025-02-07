from dotenv import find_dotenv, load_dotenv
import os

env_path = find_dotenv()
load_dotenv(env_path)

API_KEY = os.getenv('DEEPGRAM_API_KEY')
DB_URL = os.getenv('DATABASE_URL')
GEMINI = os.getenv('GEMINI_API_KEY')
KEY = os.getenv('KEY')
DEEPGRAM = os.getenv('DEEPGRAM_API_KEY')
UPLOADS_DIR = "../uploads"