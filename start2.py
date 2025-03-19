import ollama


response = ollama.list()

# print(response)


res = ollama.chat(
    model="test:01",
    messages = [
        {"role": "user", "content": "what is your name?"},
    ]
)

# print(res['message']['content'])


