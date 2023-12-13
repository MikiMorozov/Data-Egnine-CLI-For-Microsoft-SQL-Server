
        else:
            user_input = input(Fore.LIGHTBLUE_EX + '>>> ' + Style.RESET_ALL).strip().lower()
        commands.execute_command(user_input, db_manager, data_engine, engine_running)
        if user_input == commands.commands_dict['QUIT']:
            break

if __name__ == "__main__":
    main()