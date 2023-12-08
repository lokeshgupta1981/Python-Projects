import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

question = input("Ask me anything: ")

stream = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": question}],
  stream=True,
)

for chunk in stream:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
