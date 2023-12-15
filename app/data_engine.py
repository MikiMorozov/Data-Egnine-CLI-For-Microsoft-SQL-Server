import gpt
from database_manager import Database_Manager
from datetime import datetime
from models import MODELS

class Data_Engine:
    
    # properties

    db_manager: Database_Manager
    insert_script: str
    prompt: str
    requirement_list: list
    model = str
    table_dict: dict

    # constructor
    def __init__(self, db_manager):
        self.set_db_manager(db_manager)
        self.requirement_list = []
        self.model = 'gpt-3.5-turbo-1106' #default model
        self.table_dict = {}
        self.insert_script = ''
        self.set_prompt()

    def set_assistant(self, assistant):
        if assistant is None : raise TypeError("assistant cannot be None")
        self.assistant = 'I am a highly intelligent assistant that can generate SQL Server INSERT statements with dummy data for your tables. I will only give code snippets and leave out comments. I will make sure to take into consideration special characters and escape characters for MS SQL Server syntax.'

    def set_db_manager(self, db_manager):
        try:
            if db_manager is None : raise TypeError("db_manager cannot be None")
            self.db_manager = db_manager
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def generate(self, nr_of_lines, table_index=None):
        try:
            prompt = ''
            user_prompt = ''
            if table_index is None and len(self.table_dict) == 0:
                prompt = self.set_prompt()
                user_prompt = self.format_user_prompt(nr_of_lines)
            elif table_index is None and len(self.table_dict) != 0:
                prompt = self.set_prompt()
                user_prompt = self.format_user_prompt_tables(nr_of_lines)
            else:
                prompt = self.set_prompt(table_index)
                user_prompt = self.format_user_prompt(nr_of_lines, table_index)

            
            response = gpt.get_response(prompt, self.model, user_prompt, self.assistant)
            self.format_response(response)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

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
        index = int(index)
        try:
            self.requirement_list.pop(index-1)
        except IndexError:
            print('Invalid index')

    def add_requirement(self, prompt):
        try:
            self.requirement_list.append(prompt)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def clear(self):
        self.insert_script = ''
        self.requirement_list = []
        self.table_dict = {}

    def set_prompt(self, table_index=None):
        try:
            if table_index is None:
                prompt = ''

                if len(self.table_dict) == 0:

                    for string in self.db_manager.table_props:
                        prompt += string
                        prompt += "\n"

                    self.prompt = prompt
                    return prompt

                else:
                    for index in self.table_dict.values():
                        prompt += self.db_manager.table_props[index]
                        prompt += "\n"

                    self.prompt = prompt
                    return prompt
            else:
                prompt = self.db_manager.table_props[table_index - 1]
                self.prompt = prompt
                return prompt           
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
     
    def format_user_prompt(self, nr_of_lines, table_index=None):
        try:
            if table_index is None:
                which = 'each individual table'
            else:
                which = 'this table ' + next(iter(self.db_manager.table_order))
            user_prompt = f"Generate 1 SQL Server INSERT statement with {nr_of_lines} lines of dummy data for {which}. Take into consideration the FK constraints if there are any. Output everything in 1 code snippet. Don't add comments to the code snippet. Don't generate IDs if they are auto-generated. \n"
            if len(self.requirement_list) != 0:
                requirements = self.format_requirements()
                user_prompt += requirements
            return user_prompt
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def format_user_prompt_tables(self, nr_of_lines):
        try:
            tables = ''

            for table in self.table_dict.keys():
                tables += table
                tables += ', '

            user_prompt = f"Generate 1 SQL Server INSERT statement with {nr_of_lines} lines of dummy data for these tables: {tables}. Take into consideration the FK constraints if there are any. Output everything in 1 code snippet. Don't add comments to the code snippet. Don't generate IDs if they are auto-generated. \n"
            if len(self.requirement_list) != 0:
                requirements = self.format_requirements()
                user_prompt += requirements
            return user_prompt
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def format_requirements(self):
        try:
            requirements = 'Take into consideration the following requirements: \n'
            for i, string in enumerate(self.requirement_list, start=1):
                requirements += f"{i}. {string}\n"
            return requirements
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def format_response(self, response):
        try:
            begin_idx = response.find("INSERT INTO")
            end_idx = response.rfind(";") + 1
            self.insert_script = response[begin_idx:end_idx]
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def add_table(self, table_index):
        # if table_dict already contains the table, don't add it again. check by table name if the strings match
        table_index = int(table_index)
        try:
            table_name = self.db_manager.table_order[table_index - 1]

            if table_name not in self.table_dict:
                self.table_dict[table_name] = table_index -1
                print(f"Table '{table_name}' added to the list.")
            else:
                print(f"Table '{table_name}' is already in the list.")
        except IndexError:
            print('Invalid index')

    def delete_table(self, table_index):
        table_index = int(table_index)
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

    def set_model(self, index):
        index = int(index)
        try:
            if index is None : raise TypeError("model cannot be None")
            self.model = MODELS[index-1]
            print(f"Model set to '{self.model}'")
        except IndexError:
            print('Invalid index')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")