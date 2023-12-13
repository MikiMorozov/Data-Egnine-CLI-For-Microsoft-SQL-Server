# #!/usr/bin/env python
import printer_util
from commands import commands_dict as commands
from database_manager import Database_Manager
from data_engine import Data_Engine
from colorama import Fore, Style
import re

def main():

    printer_util.welcome()

    connection_string = r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;"
    output_directory = r"C:\Users\micha\OneDrive\Documents\DataEngineTests"

    db_manager = Database_Manager(connection_string)
    data_engine = Data_Engine(db_manager)

    # for table in db_manager.table_props:
    #     printer_util.print_table(table_prop)

    engine_running = True

    while True:
        if not engine_running:
            user_input = input('> ').strip().lower()
        else:
            user_input = input(Fore.LIGHTBLUE_EX + '>>> ' + Style.RESET_ALL).strip().lower()

        if user_input not in commands.values():
            if not any(re.match(command, user_input) for command in commands.values()):
                printer_util.print_invalid_command(user_input)
        
        if user_input == commands['PRINT_HELP']:
            printer_util.print_help()
        elif user_input == commands['PRINT_TABLES']:
            printer_util.print_tables(db_manager)
        elif user_input == commands['PRINT_TABLE_RELATIONSHIPS']:
            printer_util.print_table_relationships(db_manager)
        elif user_input == commands['PRINT_TABLE_ORDER']:
            printer_util.print_table_order(db_manager)
        elif user_input == commands['START_ENGINE']:
            engine_running = True 
            printer_util.print_engine_started()
        elif user_input == commands['STOP_ENGINE']:
            engine_running = False
            printer_util.print_engine_stopped()
            data_engine.clear()
        elif user_input == commands['QUIT']:
            break

        # engine-dependent commands

        if engine_running:
            if re.match(commands['WRITE_DATA'], user_input):
                match = re.match(commands['WRITE_DATA'], user_input)
                if match:
                    output_directory = match.group(1)

                    data_engine.write_to_file(output_directory)

            elif user_input == commands['INSERT_INTO_DB']:
                db_manager.insert_into_db(connection_string, data_engine.insert_script)

            elif re.match(commands['GENERATE'], user_input):
                    match = re.match(commands['GENERATE'], user_input)
                    if match:
                        nr_of_lines = int(match.group(1))
                        printer_util.print_response(data_engine, nr_of_lines)
                    else:
                        print('Invalid input for -g command')

            elif re.match(commands['GENERATE_TABLE'], user_input):
                    match = re.match(commands['GENERATE_TABLE'], user_input)
                    if match:
                        nr_of_lines = int(match.group(1))
                        table_index = int(match.group(2))
                        printer_util.print_response(data_engine, nr_of_lines, table_index)
                    else:
                        print('Invalid input for -g -t command')

            elif re.match(commands['ADD_REQUIREMENT'], user_input):
                    match = re.match(commands['ADD_REQUIREMENT'], user_input)
                    if match:
                        prompt = match.group(1)
                        data_engine.add_requirement(prompt)
                        printer_util.print_req_added(prompt)
                    else:
                        print('Invalid input for -ap command')
            elif user_input == commands['PRINT_REQUIREMENTS']:
                printer_util.print_reqs(data_engine)

            # delete requirement
            elif re.match(commands['DELETE_REQUIREMENT'], user_input):
                    match = re.match(commands['DELETE_REQUIREMENT'], user_input)
                    if match:
                        index = int(match.group(1))
                        data_engine.delete_requirement(index)
                        printer_util.print_req_deleted()
                    else:
                        print('Invalid input for -dr command')
        else:
            printer_util.handle_not_running_commands(user_input)


if __name__ == "__main__":
    main()