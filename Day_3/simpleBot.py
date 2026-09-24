import ollama
question=input("ask the question")
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"give answe in 2 lines only."
        }
    ]
)
print(response["message"]["content"])