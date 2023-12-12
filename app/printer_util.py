import os
import time
from colorama import Fore
from halo import Halo
from commands import commands_dict as commands
import re

HELP_TEXT = """

    The following options are available:

    --help          see help
    -pt             see all tables in the database
    -ptr            see tables and their FK relationships
    -pto            see table order for data generation
    -start          starts engine: saves latest prompt in memory
    -stop           stops engine: clears latest generated data and prompts from memory
    -w              writes data to file when engine is running
    -idb            inserts data into database when engine is running
    -g <number>     generates data when engine is running: specify the number of lines of data data to be generated for each table
    -ap <prompt>    adds prompt to the prompt list when engine is running. Prompts are used to customize the data generation output.
    -q              quits the program

    """

def welcome():
    os.system('cls')
    """Welcome to Data Engine!

    This program generates dummy data for your application.
    """
    print("****************************************")
    print("Welcome to Data Engine!")
    print("v1.0")
    print("****************************************")

def prompt_for_connection_string():
    return input('Please provide the connection string for your database : ')

def print_user_input(connection_string, output_directory):
    print("----------------------------------------")
    print(f"Connection String: {connection_string}")
    print(f"Output Directory: {output_directory}")
    print("----------------------------------------")

def print_tables(Data_Manager):
    print('\nTables:')
    for i, table in enumerate(Data_Manager.tables, start=1):
        print(f'{i}. {table.name}')
    print('\n')

def print_table_relationships(Data_Manager):
    print('\nTable relationships:')
    for table_name, foreign_keys in Data_Manager.relationships.items():
        for foreign_key in foreign_keys:
            print(f"{table_name} -> {foreign_key}")
    print('\n')

def print_table_order(Data_Manager):
    print('\nTable order for data generation:')
    for i, table_name in enumerate(Data_Manager.table_order, start=1):
        print(f"{i}. {table_name}")
    print('\n')

def print_help():
    print(HELP_TEXT)

def print_error():
    print('Please specify a valid command. Use -h or --help for help.')

def print_abort_message():
    print('Aborting...')

def print_generate_default(engine_manager, nr_of_lines):
    start_time = time.time()
    try: 
        with Halo(text='generating data...'):
            engine_manager.generate_default(nr_of_lines)
            print('\n')
            print(Fore.LIGHTBLUE_EX + engine_manager.insert_script)
            print('\n')
            end_time = time.time()
            print(f"Time elapsed: {round(end_time - start_time, 3)} seconds\n")
    except: 
            print("Error")

def print_engine_not_running():
    print('Engine is not running. Please start the engine before executing this command. Use -h or --help for help.')

def print_invalid_command(user_input):
    print(f"Invalid command: \'{user_input}\'. Use -h or --help for help.")

def print_engine_started():
    print(Fore.LIGHTBLUE_EX + 'ENGINE STARTED _ _ _')

def print_engine_stopped():
    print(Fore.LIGHTBLUE_EX + 'ENGINE STOPPED _ _ _')

def handle_not_running_commands(user_input):
    matching_commands = [
        commands['WRITE_DATA'],
        commands['INSERT_INTO_DB'],
        commands['GENERATE'],
        commands['ADD_POMPT']
    ]

    for cmd in matching_commands:
        if cmd == user_input:
            print_engine_not_running()
            return

    # Check if user_input matches the patterns for 'GENERATE' or 'ADD_POMPT'
    generate_match = re.match(commands['GENERATE'], user_input)
    add_prompt_match = re.match(commands['ADD_POMPT'], user_input)

    if generate_match or add_prompt_match:
        print_engine_not_running()
