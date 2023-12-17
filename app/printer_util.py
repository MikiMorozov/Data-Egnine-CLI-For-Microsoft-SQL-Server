import os
import time
from colorama import Fore
from halo import Halo
from models import MODELS
from help import HELP_TEXT

def welcome():
    os.system('cls')
    print("***********************************************")
    print("*  Welcome to Data Engine CLI for SQL Server  *")
    print("*  v1.0                                       *")
    print("***********************************************")
def print_tables(db_manager):
    try:
        print('\nTables:')
        for i, table_name in enumerate(db_manager.tables, start = 1):
            print(f"{i}. {table_name}")
        print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def print_table_relationships(db_manager):
    try:
        print('\nTable relationships:')
        for table_name, foreign_keys in db_manager.relationships.items():
            for foreign_key in foreign_keys:
                print(f"{table_name} -> {foreign_key}")
        print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def print_table_order(db_manager):
    try:
        print('\nTable order for data generation:')
        for i, table_name in enumerate(db_manager.table_order, start=1):
            print(f"[{i}] {table_name}")
        print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_help():
    try:
        print(HELP_TEXT)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_error():
    print('Please specify a valid command. Use -h or --help for help.')

def print_invalid_command(user_input):
    print(f"Invalid command: \'{user_input}\'. Use --help for help.")

def print_engine_started():
    try:
        print(Fore.LIGHTBLUE_EX + 'ENGINE STARTED _ _ _')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_engine_stopped():
    try:
        print(Fore.LIGHTBLUE_EX + 'ENGINE STOPPED _ _ _')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_req_added(requirement):
    print(f"Requirement added: \"{requirement}\". Use -pr to see all requirements.")

def print_reqs(data_engine):
    try:
        if len(data_engine.requirement_list) == 0:
            print('No requirements added.')
            return
        print('\nRequirements:\n')
        for i, req in enumerate(data_engine.requirement_list, start=1):
            print(f"[{i}] {req}")
        print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_req_deleted():
    print(f"Requirement deleted.")

def print_table_deleted():
    print(f"Table deleted from prompt. Use -sp to see the prompt.")

def see_tables_added(data_engine):
    try:
        if len(data_engine.table_dict) == 0:
            print('No tables added.')
            return
        else:
            print('\nTables added to prompt:\n')
            for table_name, table_index in data_engine.table_dict.items():
                print(f"[{table_index+1}] {table_name}")
            print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_db_prompt(data_engine):
    try:
        print('\n')
        print(f"{data_engine.prompt}")
        print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_tables_prompt(data_engine):
    try:
        print('\n')
        print(f"{data_engine.set_prompt()}")
        print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_tables_cleared():
    print('Tables cleared. -pp to see prompt.')

def print_models():
    try:
        print('\nModels:\n')
        for i, model in enumerate(MODELS, start=1):
            print(f"[{i}] {model}")
        print('\n')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_get_model(data_engine):
    try:
        print(f"Current model: {data_engine.model}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_tables_cleared():
    print('Tables cleared. -pp to see prompt.')