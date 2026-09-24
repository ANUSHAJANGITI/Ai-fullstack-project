import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"you are a python teacher.give the definition"
        }
    ]
)
print(response["message"]["content"])