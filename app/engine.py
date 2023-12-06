import gpt
import database
import commands

def generate_default(nr_of_lines, db_manager):
    prompt = ''

    for string in db_manager.table_props:
        prompt += string
        prompt += "\n"
    
    model = 'gpt-3.5-turbo-1106'
    user_prompt = f"This my database. I need dummy data. Generate 1 SQL Server insert statement per table with {nr_of_lines} lines of dummy data. Take into consideration the FK constraints if there are any. End with ';'"
    return gpt.get_response(prompt, model, user_prompt)