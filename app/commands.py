import re
import printer_util
import command_registry

db_manager = None
data_engine = None
engine_running = [False]

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

def see_tables(user_input):
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
    pass

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

def execute_command(user_input, db_manager, data_engine, engine_running):

    if user_input not in engine_commands.values() and user_input not in non_engine_commands.values():
            if not any(re.match(command, user_input) for command in engine_commands.values()) and not any(re.match(command, user_input) for command in non_engine_commands.values()):
                printer_util.print_invalid_command(user_input)

    # # ENGINE COMMANDS
                    
    # if user_input in engine_commands.values() and engine_running[0] == False:
    #     printer_util.print_engine_not_running()
    # elif user_input in engine_commands.values() and engine_running[0] == True or any(re.match(command, user_input) for command in engine_commands.values()) and engine_running[0] == True:
    #     if re.match(engine_commands['WRITE_DATA'], user_input):
    #         match = re.match(engine_commands['WRITE_DATA'], user_input)
    #         if match:
    #             output_directory = match.group(1)

    #             data_engine.write_to_file(output_directory)
    #     elif user_input == engine_commands['INSERT_INTO_DB']:
    #         try:
    #             db_manager.insert_into_db(data_engine.insert_script)
    #         except Exception as e:
    #             print(f"An unexpected error occurred: {e}")
    #     elif re.match(engine_commands['GENERATE'], user_input):
    #             match = re.match(engine_commands['GENERATE'], user_input)
    #             if match:
    #                 nr_of_lines = int(match.group(1))
    #                 printer_util.print_response_db(data_engine, nr_of_lines)
    #             else:
    #                 print('Invalid input for -g command')
    #     elif re.match(engine_commands['GENERATE_TABLE'], user_input):
    #             match = re.match(engine_commands['GENERATE_TABLE'], user_input)
    #             if match:
    #                 nr_of_lines = int(match.group(1))
    #                 table_index = int(match.group(2))
    #                 printer_util.print_response(data_engine, nr_of_lines, table_index)
    #             else:
    #                 print('Invalid input for -g command')
    #     elif re.match(engine_commands['ADD_REQUIREMENT'], user_input):
    #             match = re.match(engine_commands['ADD_REQUIREMENT'], user_input)
    #             if match:
    #                 prompt = match.group(1)
    #                 data_engine.add_requirement(prompt)
    #                 printer_util.print_req_added(prompt)
    #             else:
    #                 print('Invalid input for -ap command')
    #     elif user_input == engine_commands['PRINT_REQUIREMENTS']:
    #         printer_util.print_reqs(data_engine)
    #     elif re.match(engine_commands['DELETE_REQUIREMENT'], user_input):
    #             match = re.match(engine_commands['DELETE_REQUIREMENT'], user_input)
    #             if match:
    #                 index = int(match.group(1))
    #                 data_engine.delete_requirement(index)
    #                 printer_util.print_req_deleted()
    #             else:
    #                 print('Invalid input for -dr command')
    #     elif re.match(engine_commands['ADD_TABLE'], user_input):
    #             match = re.match(engine_commands['ADD_TABLE'], user_input)
    #             if match:
    #                 index = int(match.group(1))
    #                 data_engine.add_table(index)
    #             else:
    #                 print('Invalid input for -at command')
    #     elif re.match(engine_commands['REMOVE_TABLE'], user_input):
    #             match = re.match(engine_commands['REMOVE_TABLE'], user_input)
    #             if match:
    #                 index = int(match.group(1))
    #                 data_engine.remove_table(index)
    #             else:
    #                 print('Invalid input for -rt command')
    #     elif user_input == engine_commands['SEE_TABLES']:
    #             try:
    #                 printer_util.see_tables_added(data_engine)
    #             except Exception as e:
    #                 print('Invalid input for -rt command')
    #     elif user_input == engine_commands['PRINT PROMPT']:
    #         if len(data_engine.table_dict) == 0:
    #             printer_util.print_db_prompt(data_engine)
    #         else:
    #             printer_util.print_tables_prompt(data_engine)
    #     elif user_input == engine_commands['CLEAR_TABLES']:
    #         data_engine.clear_tables()
    #         printer_util.print_tables_cleared()

    # # NON-ENGINE COMMANDS
    
    # elif user_input in non_engine_commands.values() or any(re.match(command, user_input) for command in non_engine_commands.values()):
    #     if user_input == non_engine_commands['MODELS']:
    #         try:
    #             printer_util.print_models()
    #         except Exception as e:
    #             print(f"An unexpected error occurred: {e}")
    #     elif re.match(non_engine_commands['SET_MODEL'], user_input):
    #         match = re.match(non_engine_commands['SET_MODEL'], user_input)
    #         if match:
    #             model_index = int(match.group(1))
    #             data_engine.set_model(model_index)
    #         else:
    #             print('Invalid input for --setmodel command')
    #     elif user_input == non_engine_commands['GET_MODEL']:
    #         try:
    #             printer_util.print_get_model(data_engine)
    #         except Exception as e:
    #             print(f"An unexpected error occurred: {e}")
    #     elif user_input == non_engine_commands['PRINT_HELP']:
    #         printer_util.print_help()
    #     elif user_input == non_engine_commands['PRINT_TABLES']:
    #         printer_util.print_tables(db_manager)
    #     elif user_input == non_engine_commands['PRINT_TABLE_RELATIONSHIPS']:
    #         printer_util.print_table_relationships(db_manager)
    #     elif user_input == non_engine_commands['PRINT_TABLE_ORDER']:
    #         printer_util.print_table_order(db_manager)
    #     elif user_input == non_engine_commands['START_ENGINE']:
    #         engine_running[0] = True 
    #         printer_util.print_engine_started()
    #     elif user_input == non_engine_commands['STOP_ENGINE']:
    #         engine_running[0] = False
    #         printer_util.print_engine_stopped()
    #         data_engine.clear()