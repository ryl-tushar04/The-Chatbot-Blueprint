from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100