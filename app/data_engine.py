import gpt
import database
import commands

class Engine_Manager:
    # properties
    db_manager: database.Database_Manager
    insert_script: str

    # constructor
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # setters
    def set_db_manager(self, db_manager):
        if db_manager is None : raise TypeError("db_manager cannot be None")
        self.db_manager = db_manager

    def generate_default(self, nr_of_lines):
        prompt = ''

        for string in self.db_manager.table_props:
            prompt += string
            prompt += "\n"
        
        model = 'gpt-3.5-turbo-1106'
        user_prompt = f"This my database. I need dummy data. Generate 1 SQL Server insert statement per table with {nr_of_lines} lines of dummy data. Take into consideration the FK constraints if there are any."
        self.insert_script = gpt.get_response(prompt, model, user_prompt)

    def write_to_file(self):
        file = open(f"{self.db_manager.output_directory}\\insert_script.sql", "w")
        file.write(self.insert_script)
        file.close()
