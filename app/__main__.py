import printer_util
import command_exe
from setup_handler import check_env_connection_string, check_api_key
import command_exe

def main():

    printer_util.welcome()

    if (not check_env_connection_string() or not check_api_key()):
        return

    while command_exe.program_running[0] == True:

        user_input = command_exe.set_terminal()

        if command_exe.command_valid(user_input) and command_exe.engine_check(user_input):
                command_exe.execute_command(user_input)
        elif not command_exe.engine_check(user_input):
                command_exe.engine_command_handler()
        else: 
            printer_util.print_invalid_command(user_input)

if __name__ == "__main__":
    main()
