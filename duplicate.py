import os
import openai
openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)