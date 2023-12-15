from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def get_response(prompt, model, user_prompt, assistant):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "assistant", "content": assistant},
                {"role": "user", "content": user_prompt},
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return None  # You can return a default value or raise the exception again if needed



















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