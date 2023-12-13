import gpt
from database_manager import Database_Manager
from datetime import datetime

class Data_Engine:
    
    # properties

    db_manager: Database_Manager
    insert_script: str
    requirement_list: list
    model = str

    # constructor
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.requirement_list = list
        self.model = 'gpt-4'
        self.insert_script = """INSERT INTO contact_info (phone, email, address) 
VALUES 
('1234567890', 'email1@example.com', 'Address 1'),
('2345678901', 'email2@example.com', 'Address 2'),
('3456789012', 'email3@example.com', 'Address 3'),
('4567890123', 'email4@example.com', 'Address 4'),
('5678901234', 'email5@example.com', 'Address 5');

INSERT INTO organizer (name, contact_info_id) 
VALUES 
('Organizer 1', 1),
('Organizer 2', 2),
('Organizer 3', 3),
('Organizer 4', 4),
('Organizer 5', 5);

INSERT INTO description (name, description, duration, location, activity_status) 
VALUES 
('Description 1', 'Description 1 Details', 60, 'Location 1', 1),
('Description 2', 'Description 2 Details', 90, 'Location 2', 1),
('Description 3', 'Description 3 Details', 120, 'Location 3', 1),
('Description 4', 'Description 4 Details', 75, 'Location 4', 1),
('Description 5', 'Description 5 Details', 45, 'Location 5', 1);

INSERT INTO customer (name, contact_info_id, activity_status) 
VALUES 
('Customer 1', 1, 1),
('Customer 2', 2, 1),
('Customer 3', 3, 1),
('Customer 4', 4, 1),
('Customer 5', 5, 1);

INSERT INTO price_info (adult_price, child_price, discount, adult_age) 
VALUES 
(100, 50, 10, 18),
(120, 60, 15, 20),
(150, 75, 20, 22),
(90, 45, 10, 16),
(110, 55, 12, 19);

INSERT INTO member (name, birthday, customer_id, activity_status) 
VALUES 
('Member 1', '2000-01-01', 1, 1),
('Member 2', '2001-02-02', 2, 1),
('Member 3', '2002-03-03', 3, 1),
('Member 4', '2003-04-04', 4, 1),
('Member 5', '2004-05-05', 5, 1);

INSERT INTO activity (fixture, nr_of_places, price_info_id, description_id, organizer_id) 
VALUES 
('2022-08-15 10:00:00', 50, 1, 1, 1),
('2022-08-16 11:00:00', 40, 2, 2, 2),
('2022-08-17 12:00:00', 30, 3, 3, 3),
('2022-08-18 13:00:00', 45, 4, 4, 4),
('2022-08-19 14:00:00', 55, 5, 5, 5);

INSERT INTO registration (activity_id, customer_id, total_price) 
VALUES 
(1, 1, 100),
(2, 2, 120),
(3, 3, 150),
(4, 4, 90),
(5, 5, 110);

INSERT INTO registration_details (registration_id, member_id, subtotal_price) 
VALUES 
(1, 1, 50),
(2, 2, 60),
(3, 3, 75),
(4, 4, 45),
(5, 5, 55);"""


    # setters
    def set_db_manager(self, db_manager):
        if db_manager is None : raise TypeError("db_manager cannot be None")
        self.db_manager = db_manager

    def generate_db(self, nr_of_lines):
        
        prompt = self.format_prompt()
        user_prompt = self.format_user_prompt(nr_of_lines)
        
        response = gpt.get_response(prompt, self.model, user_prompt)
        self.format_response(response)

    def generate_table(table_index):
        pass

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


    def insert_into_db(self):
        self.db_manager.insert_into_db(self.insert_script) 

    def add_requirement(self, prompt):
        self.requirement_list.append(prompt)

    def clear(self):
        self.insert_script = ''
        self.requirement_list = []

    def format_prompt(self):
        prompt = ''

        for string in self.db_manager.table_props:
            prompt += string
            prompt += "\n"

        return prompt
    
    def format_user_prompt(self, nr_of_lines):
        prompt = f"Generate 1 SQL Server INSERT statement with {nr_of_lines} lines of dummy data for each individual table. Take into consideration the FK constraints if there are any. Output everything in 1 code snippet. Don't add comments to the code snippet. Don't generate IDs if they are auto-generated. \n"
        if len(self.requirement_list) != 0:
            requirements = self.format_requirments()
            prompt += requirements
        return prompt

    
    def format_requirments(self):
        requirements = 'Take into consideration the following requirements: \n'
        for i, string in enumerate(self.requirement_list, start=1):
            requirements += f"{i}. {string}\n"
        return requirements
    
    def format_response(self, response):
        begin_idx = response.find("INSERT INTO")
        end_idx = response.rfind(";") + 1
        self.insert_script = response[begin_idx:end_idx]

    def delete_requirement(self, index):
        try:
            self.requirement_list.pop(index-1)
        except IndexError:
            print('Invalid index')
