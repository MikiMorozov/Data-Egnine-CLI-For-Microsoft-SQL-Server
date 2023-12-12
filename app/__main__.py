# #!/usr/bin/env python
import printer_util
import gpt
from commands import commands_dict as commands
from database_manager import Database_Manager
from halo import Halo
from data_engine import Data_Engine
from colorama import Fore, Style

def main():

    printer_util.welcome()

    connection_string = r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Restaurant;Trusted_Connection=yes;"
    output_directory = r"C:\Users\micha\OneDrive\Documents\DataEngineTests"

    db_manager = Database_Manager(connection_string, output_directory)
    data_engine = Data_Engine(db_manager)

    # for table in db_manager.table_props:
    #     printer_util.print_table(table_prop)

    engine_running = False

    while True:
        if not engine_running:
            user_input = input('> ').strip().lower()
        else:
            user_input = input(Fore.LIGHTBLUE_EX + '>>> ' + Style.RESET_ALL).strip().lower()

        if user_input not in commands.values():
            printer_util.print_invalid_command(user_input)
        
        if user_input == commands['PRINT_HELP']:
            printer_util.print_help()
        elif user_input == commands['PRINT_TABLES']:
            printer_util.print_tables(db_manager)
        elif user_input == commands['PRINT_TABLE_RELATIONSHIPS']:
            printer_util.print_table_relationships(db_manager)
        elif user_input == commands['PRINT_TABLE_ORDER']:
            printer_util.print_table_order(db_manager)
        elif user_input == commands['GENERATE_DEFAULT']:
            engine_running = True 
            printer_util.print_engine_started()
            printer_util.print_generate_default(data_engine)
        elif user_input == commands['GENERATE_CUSTOM']:
            printer_util.print_generate_custom(data_engine)
        elif user_input == commands['WRITE_DATA'] and engine_running:
            printer_util.prompt_for_output_directory()
            data_engine.write_to_file()
        # elif user_input == commands['WRITE_DATA'] and not engine_running:
        #     printer_util.print_engine_not_running()
        # elif user_input == commands['INSERT_INTO_DB'] and engine_running:
        #     # db_manager.insert_into_db()
        # elif user_input == commands['INSERT_INTO_DB'] and not engine_running:
        #     printer_util.print_engine_not_running()
        elif user_input == commands['STOP']:
            engine_running = False
            printer_util.print_engine_stopped()
            data_engine.insert_script = ''
        elif user_input == commands['ABORT']:
            break


if __name__ == "__main__":
    main()