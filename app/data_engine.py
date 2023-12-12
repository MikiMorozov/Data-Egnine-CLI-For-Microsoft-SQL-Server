import gpt
from database_manager import Database_Manager
from datetime import datetime

class Data_Engine:
    # properties
    db_manager: Database_Manager
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
        
        model = 'gpt-4-1106-preview'
        user_prompt = f"Generate 1 SQL Server INSERT statement with {nr_of_lines} lines of dummy data for each individual table. Take into consideration the FK constraints if there are any. Output everything in 1 code snippet. Don't add comments to the code snippet."
        gpt_response = gpt.get_response(prompt, model, user_prompt)
        begin_idx = gpt_response.find("INSERT INTO")
        end_idx = gpt_response.rfind(";") + 1
        self.insert_script = gpt_response[begin_idx:end_idx]

    def write_to_file(self):
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        file = open(f"{self.db_manager.output_directory}\\data_engine_insert_script_{self.db_manager.db_name}_{timestamp}.sql", "w")
        file.write(self.insert_script)
        file.close()
