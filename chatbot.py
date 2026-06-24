import ollama

def generate_answer(question, context):

    prompt = f"""
Answer ONLY from the provided context.

If the answer is not available in the context, say:
"I could not find that information in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]