
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
                        You may also use your own knowledge if needed, but prefer the context.

                        Question :{question}
                        Context : {context}
                        """,
            "stream": False,
            "temperature": 0.7,
            "system": """
                        You are advaita BAB aka BAB a very vise research scholar.
                        You are a knowledgeable and helpful research assistant.

                        Your behavior rules:
                        - Use the provided context as the primary source of truth.
                        - You may use your own knowledge only if necessary.
                        - Do not hallucinate or invent facts.
                        - Stay strictly on topic.
                        - Give clear, structured, and accurate answers.
                    """ 
        }
    )

    data = response.json()

    return data.get("response", "")


'''if __name__ == "__main__":
    query = "What is Adam optimizer?"

    chunks = [
        "Adam is an optimization algorithm used for training neural networks.",
        "It combines momentum and adaptive learning rates.",
        "It is widely used because it converges faster."
    ]

    answer = generator_answer(query, chunks)
    print("\n=== ANSWER ===\n")
    print(answer)'''