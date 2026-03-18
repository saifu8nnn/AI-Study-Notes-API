from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def generate_summary(content: str):
    client = Groq(api_key=API_KEY)
    
    # Groq uses the chat.completions.create method
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # Groq model ID
        messages=[
            {
                "role": "user", 
                "content": f"Create a one line summary of this note: {content}"
            }
        ]
    )
    
    # Access the text using this path
    return response.choices[0].message.content