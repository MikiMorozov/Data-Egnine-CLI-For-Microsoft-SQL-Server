from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def get_response():
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that helps me to generate INSERT scripts with dummy data for tables in an SQL Server Database."},
            {"role": "assistant", "content": "Skip comments, give raw INSERT script."},
            {"role": "user", "content": "Generate an SQL Server insert statement for the fictional table 'users'."},
                ]  
    )
    print(completion.choices[0].message)

















#     def __init__ (self):
#         self.api_key = os.environ.get("OPENAI_API_KEY")

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
        
#             response = OpenAI.completions.create(
#                 engine=engine,
#                 prompt=prompt,
#                 max_tokens=max_tokens,
#                 temperature=temperature,
#                 top_p=top_p,
#                 frequency_penalty=frequency_penalty,
#                 presence_penalty=presence_penalty,
#                 stop=stop,
#             )
#             return response

# OpenAIUtils = OpenAIUtils()

# prompt = "Tell me a joke"

# response = OpenAIUtils.get_response(prompt)

# print(response.choices[0].text)

# client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# completion = client.chat.completions.create(
#   model="text-davinci-002",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)