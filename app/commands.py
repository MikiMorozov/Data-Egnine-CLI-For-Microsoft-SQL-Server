import re
import printer_util

commands_dict = {
    'PRINT_HELP': '--help',
    'PRINT_TABLES': '-pt',
    'PRINT_TABLE_RELATIONSHIPS': '-ptr',
    'PRINT_TABLE_ORDER': '-pto',
    'START_ENGINE': '--start',
    'STOP_ENGINE': '--stop',
    'WRITE_DATA': r'-w\s+(.+)$',
    'QUIT': '-q',
    'INSERT_INTO_DB': '-idb',
    'GENERATE': r'-g\s+(\d+)$',
    'GENERATE_TABLE': r'-g\s+(\d+)\s+-t\s+(\d+)$',
    'ADD_REQUIREMENT': r'-ar\s+(.+)$',
    'DELETE_REQUIREMENT': r'-dr\s+(\d+)$',
    'PRINT_REQUIREMENTS': '-pr',
    'ADD_TABLE': r'-at\s+(\d+)$',
    'REMOVE_TABLE': r'-rt\s+(\d+)$',
    'SEE_TABLES': '-st',
    'PRINT PROMPT': '-pp',
    'CLEAR_TABLES': '-ct'
    }


def execute_command(user_input, db_manager, data_engine, engine_running):



    if user_input not in commands_dict.values():
            if not any(re.match(command, user_input) for command in commands_dict.values()):
                printer_util.print_invalid_command(user_input)
    
    # print commands

    if user_input == commands_dict['PRINT_HELP']:
        printer_util.print_help()
    elif user_input == commands_dict['PRINT_TABLES']:
        printer_util.print_tables(db_manager)
    elif user_input == commands_dict['PRINT_TABLE_RELATIONSHIPS']:
        printer_util.print_table_relationships(db_manager)
    elif user_input == commands_dict['PRINT_TABLE_ORDER']:
        printer_util.print_table_order(db_manager)


    elif user_input == commands_dict['START_ENGINE']:
        engine_running[0] = True 
        printer_util.print_engine_started()
    elif user_input == commands_dict['STOP_ENGINE']:
        engine_running[0] = False
        printer_util.print_engine_stopped()
        data_engine.clear()

        # engine-dependent commands

    if engine_running[0] == True:
        if re.match(commands_dict['WRITE_DATA'], user_input):
            match = re.match(commands_dict['WRITE_DATA'], user_input)
            if match:
                output_directory = match.group(1)

                data_engine.write_to_file(output_directory)
        elif user_input == commands_dict['INSERT_INTO_DB']:
            try:
                db_manager.insert_into_db(data_engine.insert_script)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif re.match(commands_dict['GENERATE'], user_input):
                match = re.match(commands_dict['GENERATE'], user_input)
                if match:
                    nr_of_lines = int(match.group(1))
                    printer_util.print_response_db(data_engine, nr_of_lines)
                else:
                    print('Invalid input for -g command')
        elif re.match(commands_dict['GENERATE_TABLE'], user_input):
                match = re.match(commands_dict['GENERATE_TABLE'], user_input)
                if match:
                    nr_of_lines = int(match.group(1))
                    table_index = int(match.group(2))
                    printer_util.print_response(data_engine, nr_of_lines, table_index)
                else:
                    print('Invalid input for -g command')
        elif re.match(commands_dict['ADD_REQUIREMENT'], user_input):
                match = re.match(commands_dict['ADD_REQUIREMENT'], user_input)
                if match:
                    prompt = match.group(1)
                    data_engine.add_requirement(prompt)
                    printer_util.print_req_added(prompt)
                else:
                    print('Invalid input for -ap command')
        elif user_input == commands_dict['PRINT_REQUIREMENTS']:
            printer_util.print_reqs(data_engine)
        elif re.match(commands_dict['DELETE_REQUIREMENT'], user_input):
                match = re.match(commands_dict['DELETE_REQUIREMENT'], user_input)
                if match:
                    index = int(match.group(1))
                    data_engine.delete_requirement(index)
                    printer_util.print_req_deleted()
                else:
                    print('Invalid input for -dr command')
        elif re.match(commands_dict['ADD_TABLE'], user_input):
                match = re.match(commands_dict['ADD_TABLE'], user_input)
                if match:
                    index = int(match.group(1))
                    data_engine.add_table(index)
                else:
                    print('Invalid input for -at command')
        elif re.match(commands_dict['REMOVE_TABLE'], user_input):
                match = re.match(commands_dict['REMOVE_TABLE'], user_input)
                if match:
                    index = int(match.group(1))
                    data_engine.remove_table(index)
                else:
                    print('Invalid input for -rt command')
        elif user_input == commands_dict['SEE_TABLES']:
                try:
                    printer_util.see_tables_added(data_engine)
                except Exception as e:
                    print('Invalid input for -rt command')
        elif user_input == commands_dict['PRINT PROMPT']:
            if len(data_engine.table_dict) == 0:
                printer_util.print_db_prompt(data_engine)
            else:
                printer_util.print_tables_prompt(data_engine)
        elif user_input == commands_dict['CLEAR_TABLES']:
            data_engine.clear_tables()
            printer_util.print_tables_cleared()
    else:
        printer_util.print_engine_not_running()

    