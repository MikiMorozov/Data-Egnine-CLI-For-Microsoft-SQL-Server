import os

def check_env_connection_string():
    try:
        if os.path.exists('.env'):
            print('.env file detected.')
            with open('.env', 'r') as f:
                # Check if .env file contains connection string
                connection_string = ''
                for line in f:
                    if 'CONNECTION_STRING=' in line:
                        connection_string = line.split('=')[1].strip()
                        if connection_string == '':
                            print('Connection string value is empty. Please add a connection string to the .env file.')
                            return False
                        else:
                            print('Connection string found in .env file.')
                            return True

                # If the loop completes without finding the connection string
                # Add 'CONNECTION_STRING=' string to .env file
                print('Connection string not found in .env file. Adding placeholder. Please replace it with your actual Connection string.')
                with open('.env', 'a') as env_file:
                    env_file.write('\nCONNECTION_STRING=your_connection_string_here\n')
                return False
        else:
            os.makedirs('.env')
            print('Scanned for .env file, but none was found.')
            print('Created .env file')
            print('Connection string not found in .env file. Adding placeholder. Please replace it with your actual Connection string.')
            with open('.env', 'a') as env_file:
                env_file.write('\nCONNECTION_STRING=your_connection_string_here\n')
            return False
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return False
def check_api_key():
    try:
        api_key = ''
        with open('.env', 'r') as f:
            # Check if .env file contains connection string
            for line in f:
                if 'OPENAI_API_KEY=' in line:
                    api_key = line.split('=')[1].strip()
                    if api_key == '':
                        print('Open AI API key value is empty. Please add an API key to the .env file.')
                    else:
                        print('API key found in .env file.')
                        return True
                    break
            else:  # This else block is executed if the loop completes without hitting a break
                # Add 'OPENAI_API_KEY=' string to .env file
                print('API key not found in .env file. Adding placeholder. Please replace it with your actual API key.')
                with open('.env', 'a') as env_file:
                    env_file.write('\nOPENAI_API_KEY=your_api_key_here\n')
                return False
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return False