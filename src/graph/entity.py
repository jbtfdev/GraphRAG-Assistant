import requests
import json


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
    prompt = f"""
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
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model" : "llama3.1:8b",
            "prompt" : prompt,
            "stream" : False,
        }
    )

    data = response.json()
    raw = data.get("response", "")

    parsed = json.loads(raw)

    return parsed
