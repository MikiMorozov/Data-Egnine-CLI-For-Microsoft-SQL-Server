import os
import time
from colorama import Fore
from halo import Halo

HELP_TEXT = """

    The following options are available:

    --help          see help
    -pt             see all tables in the database
    -ptr            see tables and their FK relationships
    -pto            see table order for data generation
    -start -d       starts default generation of data
    -start -c       starts custom generation of data
    -w              writes data to file
    -idb            inserts data into database
    -a              aborts the program
    
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
    return input('Please provide the connection string for your database')

def prompt_for_output_directory():
    return input("Please provide the output directory for the generated data")

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

def prompt_number_of_lines():
    try:
        return int(input('How many lines of data do you want to generate for each insert statement? : '))
    except:
        print('Please enter a valid number')
        prompt_number_of_lines()

def print_generate_default(engine_manager):
    nr_of_lines = prompt_number_of_lines()
    start_time = time.time()
    try: 
        with Halo(text='generating data', spinner='dots'):
            engine_manager.generate_default(nr_of_lines)
            print('\n')
            print(Fore.LIGHTBLUE_EX + engine_manager.insert_script)
            print('\n')
            end_time = time.time()
            print(f"Time elapsed: {round(end_time - start_time, 3)} seconds\n")
    except: 
            print("Error")
def write_prompt(engine_manager, database_manager):
    return input('Try again [1] Abort[2] : ')
