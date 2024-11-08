from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API = os.getenv('GEMINI_API')
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}