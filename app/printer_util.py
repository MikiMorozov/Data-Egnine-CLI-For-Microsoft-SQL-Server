import os

def welcome():
    os.system('cls')
    """Welcome to the Dummy Data Generator 

    This program generates dummy data for your application.
    """
    print("****************************************")
    print("Welcome to the Dummy Data Generator ")
    print("****************************************")
    print("Ready to save some yourself some valuable time?")

def prompt_for_connection_string():
    return input('Please provide the connection string for your database')

def prompt_for_output_directory():
    return input("Please provide the output directory for the generated data")

def input(connection_string, output_directory):
    print("----------------------------------------")
    print(f"Connection String: {connection_string}")
    print(f"Output Directory: {output_directory}")
    print("----------------------------------------")

def print_tables(Data_Manager):
    print('Tables:')
    for i, table in enumerate(Data_Manager.tables, start=1):
        print(f'{i}. {table.name}')

def print_relationships(Data_Manager):
    print('Table relationships:')
    for table_name, foreign_keys in Data_Manager.relationships.items():
        for foreign_key in foreign_keys:
            print(f"{table_name} -> {foreign_key.target_fullname}")

def print_table_order(Data_Manager):
    print('Table order for data generation:')
    for i, table_name in enumerate(Data_Manager.table_order, start=1):
        print(f"{i}. {table_name}")

def print_help():
    print('Help:')
    print("The following options are available:")
    print("-pt: see all tables in the database")
    print("-ptr: see tables and their FK relationships")
    print("-pto: see table order for data generation")
    print("-start: starts Data Engine")
    print("-w: writes data to .txt in output directory")
    print("-a: aborts the program")

def print_error():
    print('Please specify a valid command. Use -h or --help for help.')

def print_abort_message():
    print('Aborting...')