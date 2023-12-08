import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

question = input("Ask me anything: ")

response = client.chat.completions.create(
  messages=[
    {
      "role": "user",
      "content": question
    }
  ],
  model="gpt-3.5-turbo",
  temperature=0,
  max_tokens=1024,
  n=1,
  stop=None
)

print(response)

answer = response.choices[0].message.content
print(answer)
