
import requests



def generator_answer(query, chunks):
    question  = query
    context = "\n".join(chunks)

    

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1:8b",  
            "prompt": f"""
                        Use the context below to answer the question.
                        

                        Question :{question}
                        Context : {context}
                        """,
            "stream": False,
            "temperature": 0.7,
            "system": """
                        You are a knowledgeable and helpful research assistant.

                        - explain mechanism
                        - include supporting evidence
                        - summarize relationships
                        - elaborate if context supports it
                        Your behavior rules:
                        - Use the provided context as the primary source of truth.
                        - You may use your own knowledge only if necessary.
                        - Do not hallucinate or invent facts.
                        - Stay strictly on topic.
                        - Give clear, structured, and accurate answers.
                        - Answer ONLY using the provided context.
                        - Do NOT use outside knowledge.
                        - Do NOT infer beyond explicitly stated information.
                        - If the answer is not contained in the context, say:
                        "The provided context does not contain enough information to answer this."
                        - Do NOT speculate or supplement with general knowledge.
                        - Be factual and concise.

                        dont talk about what is in the context and what is not there use the context to answer.
                    """ 
        }
    )

    data = response.json()

    return data.get("response", "")
