import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def add_message(messages, role, content):
    messages.append({"role": role, "content": content})

# no. of episodes.
N = 5 

for i in range(N):
    input_file = open(f"chunks/chunk{i}.txt")
    chunks = input_file.readlines()
    ofile = open(f"summaries/{i}-opinions.txt", "w")

    messages = []
    add_message(messages, "system", "answer very very concisely.")
    add_message(messages, "user", "ما هي الآراء المذكورة في هذه الحلقة")
    summary = []

    for chunk in chunks:
        add_message(messages, "user", chunk)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        # print(response)
        
        content = response.choices[0].message.content.encode().decode()
        print(content)
        summary.append(content)
        ofile.write(content)
        ofile.write('\n')
        messages.pop()

    ofile.close()
