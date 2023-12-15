# #!/usr/bin/env python
import printer_util
import command_exe
from colorama import Fore, Style
from setup_handler import check_env, check_api_key
import command_exe
import command_registry

def main():

    printer_util.welcome()

    if (check_env() == False or check_api_key() == False):
        return
    
    while command_exe.program_running:
        if command_exe.engine_running[0] == False:
            user_input = input('> ').strip().lower()
        else:
            user_input = input(Fore.LIGHTBLUE_EX + '>>> ' + Style.RESET_ALL).strip().lower()

        if command_exe.command_valid(user_input):
            if user_input in command_registry.engine_commands.values() and command_exe.engine_running[0] == False:
               command_exe.engine_command_handler(user_input, command_exe.engine_running)
            elif (user_input in command_registry.non_engine_commands.values() and command_exe.engine_running[0] == True) or (user_input in command_exe.command_registry.non_engine_commands.values()):
                command_function = command_exe.command_functions.get(user_input)
                if command_exe.has_param(command_function):
                    command_function()
                else:
                    command_function(user_input)

if __name__ == "__main__":
    main()