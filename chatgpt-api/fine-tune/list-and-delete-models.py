import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)
client.models.delete('ft:gpt-3.5-turbo-0613:personal::8UXexX8R')

# models = client.models.list()
# print(models)
