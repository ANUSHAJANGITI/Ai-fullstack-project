import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"what is an ai defination,3 types of ai in bullaet oints"
        }
    ]
)
print(response["message"]["content"])