from openai import openAI

class OpenAIUtils:
    def __init__ (self):
        openAI.api_key = os.environ.get(API_KEY)

    def get_response(
            self, 
            prompt, 
            engine="text-davinci-003", 
            max_tokens=150, 
            temperature=0.9, 
            top_p=1, 
            frequency_penalty=0, 
            presence_penalty=0, 
            stop=["\n"]
            ):
        
            response = openAI.Completion.create(
                engine=engine,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop
            )
            return response