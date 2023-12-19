import tiktoken

def get_tokens(input, data_engine) -> int:
        """Returns the number of tokens in a text string."""
        encoding = tiktoken.get_encoding(data_engine.model)
        amount_of_tokens = len(encoding.encode(input))
        return amount_of_tokens