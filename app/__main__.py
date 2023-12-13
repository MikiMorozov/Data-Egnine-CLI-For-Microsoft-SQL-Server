# #!/usr/bin/env python
import printer_util
import gpt
from commands import commands_dict as commands
from database_manager import Database_Manager
from halo import Halo
from data_engine import Data_Engine
from colorama import init, Fore, Style
import re

def main():

    printer_util.welcome()

    connection_string = r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Restaurant;Trusted_Connection=yes;"
    output_directory = r"C:\Users\micha\OneDrive\Documents\DataEngineTests"

    db_manager = Database_Manager(connection_string)
    data_engine = Data_Engine(db_manager)

    # for table in db_manager.table_props:
    #     printer_util.print_table(table_prop)

    engine_running = False

    while True:
        if not engine_running:
            user_input = input('> ').strip().lower()
        else:
            user_input = input(Fore.LIGHTBLUE_EX + '>>> ' + Style.RESET_ALL).strip().lower()
        commands.execute_command(user_input, db_manager, data_engine, engine_running)
        if user_input == commands['QUIT']:
            break

if __name__ == "__main__":
    main()