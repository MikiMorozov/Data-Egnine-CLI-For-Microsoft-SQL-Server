import tiktoken

def get_tokens_system_prompt(system_prompt, data_engine):
        encoding = tiktoken.encoding_for_model(data_engine.model)
        print(f'Token count: {len(encoding.encode(system_prompt))}')

def get_total_tokens(data_engine, nr_of_lines, response):
        encoding = tiktoken.encoding_for_model(data_engine.model)
        token_count_system_prompt = len(encoding.encode(data_engine.get_system_prompt()))
        token_count_user_prompt = len(encoding.encode(data_engine.format_user_prompt(nr_of_lines)))
        token_count_assistant = len(encoding.encode(data_engine.assistant))
        token_count_response = len(encoding.encode(response))
        print (f"Token count system prompt: {token_count_system_prompt}")
        print (f"Token count user prompt: {token_count_user_prompt}")
        print (f"Token count assistant: {token_count_assistant}")
        print (f"Token count response: {token_count_response}")
        print (f"Total token count: {token_count_system_prompt + token_count_user_prompt + token_count_assistant + token_count_response}\n")