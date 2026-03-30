import requests
import json


def extract_relations(chunks: str):
    allowed_relations = [
    "Treats",
    "Treated_By"
    "Causes",
    "Associated_with",
    "Located_in",
]

    context = chunks
    prompt = f"""
                Extract relations from the text.

                Return ONLY a JSON array like:
                [
                {{"source": "...", "relation": "...", "target": "..." }}
                ]

                Allowed relations types(only follow these relations):
                {", ".join(allowed_relations)}

                Instructions(should be followed strictly as well as rules):
                - have a correct flow of relations
                - Use ONLY valid medical entities (Drug, Disease).
                - Do NOT use generic words like "patients", "body".
                - Also CAPITALIZE all the relations please just for clarity
                - And please stick to the give relations only
                - Only extract relationships explicitly stated in the text given above.
                - Do NOT infer or assume relationships.
                - Only refer to relations that are medically correct.(double check your asnwer before giving it)

                Rules:
                - Only use given relations
                - only explicit relationships
                - No explanations needed
                - Do not add relations on your own, strictly follow the Relations list given.
                - STRICLY FOllow medically correct terms and relations while giving an response.
                disclaimer : STRICTLY FOLLOW the above rules and instructions , stick to them strictly dont add additonal relations based on your assumption that are not basic  medical practice.
                
                Use correct direction:
                - Drug TREATS Disease
                - Disease does NOT treat Drug
                Always ensure source is the one performing the action.
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

    start = raw.find("[")
    end = raw.rfind("]") + 1

    if start != -1 and end != -1:
        raw = raw[start:end]
    else:
        return [] 

    parsed = json.loads(raw)

    return parsed



d = extract_relations("Type 2 diabetes is commonly treated using metformin.")
print(d)