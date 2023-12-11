import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

events = client.fine_tuning.jobs.list_events(fine_tuning_job_id='ftjob-VFiBg1GJlCUX29enPvfOdZX6', limit=10)

for event in events:
  print(event, "\n")