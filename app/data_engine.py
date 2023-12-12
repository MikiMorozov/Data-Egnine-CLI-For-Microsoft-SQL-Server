import gpt
from database_manager import Database_Manager
from datetime import datetime

class Data_Engine:
    # properties

    db_manager: Database_Manager
    insert_script: str
    requirement_list: []
    model = 'gpt-4-1106-preview'

    # constructor
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.requirement_list = []

    # setters
    def set_db_manager(self, db_manager):
        if db_manager is None : raise TypeError("db_manager cannot be None")
        self.db_manager = db_manager

    def generate(self, nr_of_lines):
        
        prompt = self.format_prompt()
        user_prompt = self.format_user_prompt(nr_of_lines)
        model = 'gpt-4-1106-preview'
        
        response = gpt.get_response(prompt, model, user_prompt)
        self.format_response(response)

    def write_to_file(self):
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        file = open(f"{self.db_manager.output_directory}\\data_engine_insert_script_{self.db_manager.db_name}_{timestamp}.sql", "w")
        file.write(self.insert_script)
        file.close()

    def insert_into_db(self):
        # TODO: implement this
        self.db_manager.insert_into_db(self.insert_script) 

    def add_prompt(self, prompt):
        self.requirement_list = []
        self.requirement_list.append(prompt)

    def clear(self):
        self.insert_script = ''
        self.requirement_list = []

    def format_prompt(self):
        prompt = ''

        for string in self.requirement_list:
            prompt += string
            prompt += "\n"

        return prompt
    
    def format_user_prompt(self, nr_of_lines):
        if len(self.requirement_list) == 0:
            prompt = f"Generate 1 SQL Server INSERT statement with {nr_of_lines} lines of dummy data for each individual table. Take into consideration the FK constraints if there are any. Output everything in 1 code snippet. Don't add comments to the code snippet. Don't generate IDs if they are auto-generated. \n"
        else:
            prompt + self.format_requirments()
    
    def format_requirments(self):
        requirements = 'Take into consideration the following requirements: \n'
        for i, string in self.requirement_list:
            requirements += f"{i}. {string}\n"
        return requirements
    
    def format_response(self, response):
        begin_idx = response.find("INSERT INTO")
        end_idx = response.rfind(";") + 1
        self.insert_script = response[begin_idx:end_idx]
