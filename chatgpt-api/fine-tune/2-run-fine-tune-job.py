import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.fine_tuning.jobs.create(
  training_file="file-EcCrSIx3Q9qLs69Yx8HDnU3r",
  model="davinci-002"
)

print(response)


