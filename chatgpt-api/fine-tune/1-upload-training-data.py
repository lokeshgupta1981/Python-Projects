import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.files.create(
  file=open("input_data.jsonl", "rb"),
  purpose="fine-tune"
)

print(response)
