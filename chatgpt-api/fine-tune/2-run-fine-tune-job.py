import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.fine_tuning.jobs.create(
  training_file="file-6hY4l0aEXWQoHpYhvr0kX36o",
  model="davinci-002"
)

print(response)


