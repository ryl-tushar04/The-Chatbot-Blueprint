from groq import Groq
from config.config import GROQ_API_KEY

groq_client = Groq(api_key=GROQ_API_KEY)

def generate_response(prompt, provider="openai"):

   if provider == "groq":
        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content

   return "Model provider not supported."