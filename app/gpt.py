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