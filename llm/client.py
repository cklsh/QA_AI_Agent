import ollama

MODEL = "qwen2.5:3b"

def call_llm(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a strict QA system. Follow instructions exactly."},
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0.2
        }
    )
    return response["message"]["content"]