from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# class OpenAIUtils:
#     def __init__ (self):
#         openAI.api_key = os.environ.get("API_KEY")

#     def get_response(
#             self, 
#             prompt, 
#             engine="text-davinci-002", 
#             max_tokens=150, 
#             temperature=0.9, 
#             top_p=1, 
#             frequency_penalty=0, 
#             presence_penalty=0, 
#             stop=["\n"]
#             ):
        
#             response = openAI.Completion.create(
#                 engine=engine,
#                 prompt=prompt,
#                 max_tokens=max_tokens,
#                 temperature=temperature,
#                 top_p=top_p,
#                 frequency_penalty=frequency_penalty,
#                 presence_penalty=presence_penalty,
#                 stop=stop
#             )
#             return response

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model="text-davinci-002",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)