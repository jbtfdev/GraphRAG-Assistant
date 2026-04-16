import requests
import json
import os
from groq import Groq
from dotenv import load_dotenv
    
load_dotenv()  

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extract_entities(chunks: str):
    allowed_types = [
    "Disease",
    "Drug",
    "Symptom",
    "Procedure",
    "Anatomy",
    "Biomarker"
]

    context = chunks
    query = f"""
                Extract entities from the text.

                Return ONLY a JSON array like:
                [
                {{"entity": "...", "type": "..."}}
                ]

                Allowed entity types:
                {", ".join(allowed_types)}

                Rules:
                - Only meaningful medical entities
                - Skip generic words
                - If unsure, skip
                - No explanation

                Text:
                {context}
"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Extract medical entities from: {query}"}]
    )
    # response = requests.post(
    #     "http://localhost:11434/api/generate",
    #     json={
    #         "model" : "llama3.1:8b",
    #         "prompt" : prompt,
    #         "stream" : False,
    #     }
    # )

    content = response.choices[0].message.content.strip()
    try:
        parsed = json.loads(content)
        return parsed
    except:
        return []  


