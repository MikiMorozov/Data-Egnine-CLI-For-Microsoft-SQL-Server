import gpt
from database_manager import Database_Manager
from datetime import datetime

class Data_Engine:
    
    # properties

    db_manager: Database_Manager
    insert_script: str
    db_prompt: str
    requirement_list: list
    model = str
    table_dict: dict

    # constructor
    def __init__(self, db_manager):
        self.set_db_manager(db_manager)
        self.requirement_list = []
        self.model = 'gpt-3.5-turbo-1106'
        self.table_dict = {}
        self.insert_script = ''
        self.set_prompt()

    def set_db_manager(self, db_manager):
        if db_manager is None : raise TypeError("db_manager cannot be None")
        self.db_manager = db_manager

    def generate(self, nr_of_lines):

        prompt = ''
        user_prompt = ''
        
        if len(self.table_dict) == 0:
            prompt = self.db_prompt
            user_prompt = self.format_user_prompt_db(nr_of_lines)
        else:
            prompt = self.format_prompt_tables()
            user_prompt = self.format_user_prompt_tables(nr_of_lines)
        
        response = gpt.get_response(prompt, self.model, user_prompt)
        self.format_response(response)

    def write_to_file(self, output_directory):
        try:
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

            file_path = f"{output_directory}\\data_engine_insert_script_{self.db_manager.db_name}_{timestamp}.sql"

            with open(file_path, "w") as file:
                file.write(self.insert_script)

            print(f"Data written to: {file_path}")

        except FileNotFoundError as e:
            print(f"Error: The specified directory '{output_directory}' does not exist.")
        except PermissionError as e:
            print(f"Error: Permission denied. Unable to write to '{output_directory}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_requirement(self, index):
        try:
            self.requirement_list.pop(index-1)
        except IndexError:
            print('Invalid index')

    def add_requirement(self, prompt):
        self.requirement_list.append(prompt)

    def clear(self):
        self.insert_script = ''
        self.requirement_list = []
        self.table_dict = {}

    def set_prompt(self):
        prompt = ''

        for string in self.db_manager.table_props:
            prompt += string
            prompt += "\n"

        self.db_prompt = prompt
    
    def format_prompt_tables(self):
        prompt = ''

        for index in self.table_dict.values():
            prompt += self.db_manager.table_props[index]
            prompt += "\n"

        return prompt
    
    def format_user_prompt_db(self, nr_of_lines):
        user_prompt = f"Generate 1 SQL Server INSERT statement with {nr_of_lines} lines of dummy data for each individual table. Take into consideration the FK constraints if there are any. Output everything in 1 code snippet. Don't add comments to the code snippet. Don't generate IDs if they are auto-generated. \n"
        if len(self.requirement_list) != 0:
            requirements = self.format_requirements()
            prompt += requirements
        return user_prompt

    def format_user_prompt_tables(self, nr_of_lines):
        tables = ''

        for table in self.table_dict.keys():
            tables += table
            tables += ', '

        user_prompt = f"Generate 1 SQL Server INSERT statement with {nr_of_lines} lines of dummy data for these tables: {tables}. Take into consideration the FK constraints if there are any. Output everything in 1 code snippet. Don't add comments to the code snippet. Don't generate IDs if they are auto-generated. \n"
        if len(self.requirement_list) != 0:
            requirements = self.format_requirements()
            user_prompt += requirements
        return user_prompt

    def format_requirements(self):
        requirements = 'Take into consideration the following requirements: \n'
        for i, string in enumerate(self.requirement_list, start=1):
            requirements += f"{i}. {string}\n"
        return requirements
    
    def format_response(self, response):
        begin_idx = response.find("INSERT INTO")
        end_idx = response.rfind(";") + 1
        self.insert_script = response[begin_idx:end_idx]

    def add_table(self, table_index):
        # if table_dict already contains the table, don't add it again. check by table name if the strings match
        try:
            table_name = self.db_manager.table_order[table_index - 1]

            if table_name not in self.table_dict:
                self.table_dict[table_name] = table_index -1
                print(f"Table '{table_name}' added to the list.")
            else:
                print(f"Table '{table_name}' is already in the list.")
        except IndexError:
            print('Invalid index')

    def remove_table(self, table_index):
        try:
            table_name = self.db_manager.table_order[table_index - 1]

            if table_name in self.table_dict:
                del self.table_dict[table_name]
                print(f"Table '{table_name}' removed from the list.")
            else:
                print(f"Table '{table_name}' is not in the list.")
        except IndexError:
            print('Invalid index')

    def clear_tables(self):
        self.table_dict = {}
