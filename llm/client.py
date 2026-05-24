import ollama

MODEL = "qwen2.5:3b"

def call_llm(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a strict QA system. Follow instructions exactly."},
            {"role": "user", "content": prompt}
        ],
        format="json",
        options={
            "temperature": 0,
            "top_p": 0.1,
            "num_predict": 800
        }
    )
    return response["message"]["content"]