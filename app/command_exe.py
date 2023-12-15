import inspect
import re
import printer_util
import command_registry
from database_manager import Database_Manager
from data_engine import Data_Engine

engine_running = [False]
program_running = [True]
db_manager = Database_Manager()
data_engine = Data_Engine(db_manager)

def has_param(func):
    signature = inspect.signature(func)
    params = signature.parameters
    if len(params) > 0:
        return True

def write_data(user_input):
    match = re.match(command_registry.engine_commands['WRITE_DATA'], user_input)
    if match:
        output_directory = match.group(1)
        data_engine.write_to_file(output_directory)

def insert_into_db():
    try:
        db_manager.insert_into_db(data_engine.insert_script)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def generate(user_input):
    match = re.match(command_registry.engine_commands['GENERATE'], user_input)
    if match:
        nr_of_lines = int(match.group(1))
        printer_util.print_response_db(data_engine, nr_of_lines)
    else:
        print('Invalid input for -g command')

def generate_tables(user_input):
    match = re.match(command_registry.engine_commands['GENERATE_TABLE'], user_input)
    if match:
        nr_of_lines = int(match.group(1))
        table_index = int(match.group(2))
        printer_util.print_response(data_engine, nr_of_lines, table_index)

def add_requirement(user_input):
    match = re.match(command_registry.engine_commands['ADD_REQUIREMENT'], user_input)
    if match:
        prompt = match.group(1)
        data_engine.add_requirement(prompt)
        printer_util.print_req_added(prompt)

def delete_requirement(user_input):
    match = re.match(command_registry.engine_commands['DELETE_REQUIREMENT'], user_input)
    if match:
        index = int(match.group(1))
        data_engine.delete_requirement(index)
        printer_util.print_req_deleted()

def print_requirements():
    printer_util.print_reqs(data_engine)

def add_table(user_input):
    match = re.match(command_registry.engine_commands['ADD_TABLE'], user_input)
    if match:
        index = int(match.group(1))
        data_engine.add_table(index)

def remove_table(user_input):
    match = re.match(command_registry.engine_commands['REMOVE_TABLE'], user_input)
    if match:
        index = int(match.group(1))
        data_engine.remove_table(index)

def see_tables():
    try:
        printer_util.see_tables_added(data_engine)
    except Exception as e:
        print('Invalid input for -rt command')

def print_prompt():
    if len(data_engine.table_dict) == 0:
        printer_util.print_db_prompt(data_engine)
    else:
        printer_util.print_tables_prompt(data_engine)

def clear_tables():
    data_engine.clear_tables()
    printer_util.print_tables_cleared()

def print_help():
    printer_util.print_help()

def print_tables():
    printer_util.print_tables(db_manager)

def print_table_relationships():
    printer_util.print_table_relationships(db_manager)

def print_table_order():
    printer_util.print_table_order(db_manager)

def start_engine():
    engine_running[0] = True 
    printer_util.print_engine_started()

def stop_engine():
    engine_running[0] = False
    printer_util.print_engine_stopped()
    data_engine.clear()

def quit():
   program_running[0] = False

def print_models():
    try:
        printer_util.print_models()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def set_model(user_input):
    match = re.match(command_registry.non_engine_commands['SET_MODEL'], user_input)
    if match:
        model_index = int(match.group(1))
        data_engine.set_model(model_index)
    else:
        print('Invalid input for --setmodel command')

def print_get_model():
    try:
        printer_util.print_get_model(data_engine)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def command_valid(user_input):

    if user_input not in command_registry.engine_commands.values() and user_input not in command_registry.non_engine_commands.values():
        if not any(re.match(command, user_input) for command in command_registry.engine_commands.values()) and not any(re.match(command, user_input) for command in command_registry.non_engine_commands.values()):
            printer_util.print_invalid_command(user_input)
            return False
    return True

def engine_command_handler(user_input):
    if user_input in command_registry.engine_commands.values() and engine_running[0] == False:
        printer_util.print_engine_not_running()
        return