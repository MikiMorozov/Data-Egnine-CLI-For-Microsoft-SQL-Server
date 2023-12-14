import commands


engine_commands = {
    'WRITE_DATA': (r'-w\s+(.+)$', commands.write_data),
    'INSERT_INTO_DB': ('-idb', commands.insert_into_db),
    'GENERATE': (r'-g\s+(\d+)$', commands.generate),
    'GENERATE_TABLES': (r'-g\s+(\d+)\s+-t\s+(\d+)$', commands.generate_tables),
    'ADD_REQUIREMENT': (r'-ar\s+(.+)$', commands.add_requirement),
    'DELETE_REQUIREMENT': (r'-dr\s+(\d+)$', commands.delete_requirement),
    'PRINT_REQUIREMENTS': ('-pr', commands.print_requirements),
    'ADD_TABLE': (r'-at\s+(\d+)$', commands.add_table),
    'REMOVE_TABLE': (r'-rt\s+(\d+)$', commands.remove_table),
    'SEE_TABLES': ('-st', commands.see_tables),
    'PRINT PROMPT': ('-pp', commands.print_prompt),
    'CLEAR_TABLES': ('-ct', commands.clear_tables),
    }

non_engine_commands = { 
    'PRINT_HELP': ('--help', commands.print_help),
    'PRINT_TABLES': ('-pt', commands.print_tables),
    'PRINT_TABLE_RELATIONSHIPS': ('-ptr', commands.print_table_relationships),
    'PRINT_TABLE_ORDER': ('-pto', commands.print_table_order),
    'START_ENGINE': ('--start', commands.tart_engine), 
    'STOP_ENGINE': ('--stop', commands.stop_engine),
    'QUIT': ('-q', commands.quit),
    'MODELS': ('--models', commands.print_models), 
    'SET_MODEL': (r'--setmodel\s+(\d+)$', commands.set_model),
    'GET_MODEL': ('--getmodel', commands.print_get_model),
    }