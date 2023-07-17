"""
basic testing to make sure the environment variable works and i can get a simple return
"""
import openai
import os

openai.api_key = os.environ.get('ChatGPT')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a tagline for an ice cream shop."
)

# the naked response returns a json
# print(response)

print(response.choices[0].text)  # if you just want the text you can just call that
