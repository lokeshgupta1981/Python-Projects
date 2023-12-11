import os
import json
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

input_jsonl_file = 'input_data.jsonl'
'''
input_json_file = 'input_data.json'


with open(input_json_file, 'r') as json_file:
  data = json.load(json_file)

# Write to a JSONL file
with open(input_jsonl_file, 'w') as jsonl_file:
  for entry in data:
    jsonl_file.write(json.dumps(entry) + '\n')

print("Conversion to JSONL complete.")
'''

file = client.files.create(
  file=open(input_jsonl_file, "rb"),
  purpose="fine-tune"
)

print("File has been uploaded to OpenAI with id ", file.id)

ft_job = client.fine_tuning.jobs.create(
  training_file=file.id,
  model="gpt-3.5-turbo"
)

print("Fine Tune Job has been created with id ", ft_job.id)

events = client.fine_tuning.jobs.list_events(fine_tuning_job_id=ft_job.id, limit=10)

print(events)
