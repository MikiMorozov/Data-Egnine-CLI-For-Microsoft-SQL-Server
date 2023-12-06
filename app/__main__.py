# #!/usr/bin/env python
import printer_util
import gpt
import commands
from database import Database_Manager
from halo import Halo
from data_engine import Engine_Manager
from colorama import Fore
import time

def main():

    printer_util.welcome()

    connection_string = r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;"
    output_directory = r"C:\Users\micha\OneDrive\Documents\DataEngineTests"

    db_manager = Database_Manager(connection_string, output_directory)
    engine_manager = Engine_Manager(db_manager)
    printer_util.input(connection_string, output_directory)

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
            start_time = time.time()
            try: 
                with Halo(text='generating data', spinner='dots'):
                    engine_manager.generate_default(5)
                    print('\n')
                    print(Fore.LIGHTBLUE_EX + engine_manager.insert_script)
                    print('\n')
                    end_time = time.time()
                    print(f"Time elapsed: {round(end_time - start_time, 3)} seconds\n")
            except: 
                    print("Error")
            user_input = input('Write data to file / abort [1/2] : ')
            if user_input == '1':
                engine_manager.write_to_file()
            elif user_input == '2':
                print('Aborted')
        elif user_input == commands.WRITE_DATA:
            gpt.write_data(db_manager)
        elif user_input == commands.ABORT:
            break

if __name__ == "__main__":
    main()