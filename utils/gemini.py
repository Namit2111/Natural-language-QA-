from config.config import GEMINI_API
import google.generativeai as genai

genai.configure(api_key=GEMINI_API)

model = genai.GenerativeModel("gemini-1.5-flash")

def chat(query):
    response = model.generate_content(query)
    return response.text