import os
import asyncio

from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

client = AsyncOpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)


async def main(question) -> ChatCompletion:
  response = await client.chat.completions.create(
    messages=[
      {
        "role": "user",
        "content": question
      }
    ],
    model="gpt-3.5-turbo"
  )
  return response


question = input("What would you like to ask ChatGPT?")
response = asyncio.run(main(question))
print(response)

answer = response.choices[0].message.content
print(answer)
