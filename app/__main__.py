# #!/usr/bin/env python
import printer_util
import gpt
import commands
from database_manager import Database_Manager
from halo import Halo
from data_engine import Data_Engine
from colorama import Fore

def main():

    printer_util.welcome()

    connection_string = r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Restaurant;Trusted_Connection=yes;"
    output_directory = r"C:\Users\micha\OneDrive\Documents\DataEngineTests"

    db_manager = Database_Manager(connection_string, output_directory)
    data_engine = Data_Engine(db_manager)

    # for table in db_manager.table_props:
    #     printer_util.print_table(table_prop)

    while True:
        user_input = input('> ')
        if user_input == commands.PRINT_HELP:
            printer_util.print_help()
        elif user_input == commands.PRINT_TABLES:
            printer_util.print_tables(db_manager)
        elif user_input == commands.PRINT_TABLE_RELATIONSHIPS:
            printer_util.print_table_relationships(db_manager)
        elif user_input == commands.PRINT_TABLE_ORDER:
            printer_util.print_table_order(db_manager)
        elif user_input == commands.GENERATE_DEFAULT:
            printer_util.print_generate_default(data_engine)
            while user_input is not 4:
                user_input = printer_util.write_prompt()
                if user_input == '1':
                    data_engine.write_to_file()
                elif user_input == '2':
                    printer_util.print_generate_default(data_engine)
                    printer_util.write_prompt(data_engine)
                elif user_input == '3':
                    db_manager.insert_into_db()
                elif user_input == '4':
                    print('Aborted')
        elif user_input == commands.GENERATE_CUSTOM:
            printer_util.print_generate_custom(data_engine)
        elif user_input == commands.WRITE_DATA:
            gpt.write_data(db_manager)
        elif user_input == commands.ABORT:
            break

if __name__ == "__main__":
    main()