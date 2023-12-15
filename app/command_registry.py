import app.command_exe as command_exe

engine_commands = {
    'WRITE_DATA': (r'-w\s+(.+)$', command_exe.write_data),
    'INSERT_INTO_DB': ('-idb', command_exe.insert_into_db),
    'GENERATE': (r'-g\s+(\d+)$', command_exe.generate),
    'GENERATE_TABLES': (r'-g\s+(\d+)\s+-t\s+(\d+)$', command_exe.generate_tables),
    'ADD_REQUIREMENT': (r'-ar\s+(.+)$', command_exe.add_requirement),
    'DELETE_REQUIREMENT': (r'-dr\s+(\d+)$', command_exe.delete_requirement),
    'PRINT_REQUIREMENTS': ('-pr', command_exe.print_requirements),
    'ADD_TABLE': (r'-at\s+(\d+)$', command_exe.add_table),
    'REMOVE_TABLE': (r'-rt\s+(\d+)$', command_exe.remove_table),
    'SEE_TABLES': ('-st', command_exe.see_tables),
    'PRINT PROMPT': ('-pp', command_exe.print_prompt),
    'CLEAR_TABLES': ('-ct', command_exe.clear_tables),
    }

non_engine_commands = { 
    'PRINT_HELP': ('--help', command_exe.print_help),
    'PRINT_TABLES': ('-pt', command_exe.print_tables),
    'PRINT_TABLE_RELATIONSHIPS': ('-ptr', command_exe.print_table_relationships),
    'PRINT_TABLE_ORDER': ('-pto', command_exe.print_table_order),
    'START_ENGINE': ('--start', command_exe.start_engine), 
    'STOP_ENGINE': ('--stop', command_exe.stop_engine),
    'QUIT': ('-q', command_exe.quit),
    'MODELS': ('--models', command_exe.print_models), 
    'SET_MODEL': (r'--setmodel\s+(\d+)$', command_exe.set_model),
    'GET_MODEL': ('--getmodel', command_exe.print_get_model),
    }