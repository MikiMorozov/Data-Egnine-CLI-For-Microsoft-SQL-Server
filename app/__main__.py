# #!/usr/bin/env python
import printer_util
import app.command_exe as command_exe
from database_manager import Database_Manager
from data_engine import Data_Engine
from colorama import Fore, Style
from setup_handler import check_env, check_api_key
import command_exe

def main():

    printer_util.welcome()

    if (check_env() == False or check_api_key() == False):
        return
    
    engine_running = [False]

    while True:
        if engine_running[0] == False:
            user_input = input('> ').strip().lower()
        else:
            user_input = input(Fore.LIGHTBLUE_EX + '>>> ' + Style.RESET_ALL).strip().lower()

if __name__ == "__main__":
    main()