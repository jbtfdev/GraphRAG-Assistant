from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def groq_answer(question, context):

    question  = question
    context = "\n".join(context)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": """
                            You are a knowledgeable and helpful research assistant.

                            - Explain mechanism
                            - Include supporting evidence
                            - Summarize relationships
                            - Elaborate if context supports it

                            Your behavior rules:
                            - Use the provided context as the primary source of truth.
                            - You may use your own knowledge only if necessary.
                            - Do not hallucinate or invent facts.
                            - Stay strictly on topic.
                            - Give clear, structured, and accurate answers.
                            - Answer ONLY using the provided context.
                            - Do NOT use outside knowledge.
                            - Do NOT infer beyond explicitly stated information.
                            If the context partially supports the answer:
                            - Answer using available evidence directly.
                            - Mention limitations only briefly if critically necessary.
                            - Do not repeatedly discuss what the context lacks.
                            - Do NOT speculate or supplement with general knowledge.
                            - Be factual and concise.

                            Do not repeatedly mention missing or insufficient context.
                            Focus on answering the question directly using available evidence.
                            Be factual, structured, and thorough.
                            Provide detailed explanations when supported by context.
                            Do not omit relevant supporting details.
                        """
            },
            {
                "role": "user",
                "content": f"""
                        Question: {question}

                        Context:
                        {context}
                        """
            }
        ]
    )

    return response.choices[0].message.content
