commands_dict = {
    'PRINT_HELP': '--help',
    'PRINT_TABLES': '-pt',
    'PRINT_TABLE_RELATIONSHIPS': '-ptr',
    'PRINT_TABLE_ORDER': '-pto',
    'START_ENGINE': '--start',
    'STOP_ENGINE': '--stop',
    'WRITE_DATA': r'-w\s+(.+)$',
    'QUIT': '-q',
    'INSERT_INTO_DB': '-idb',
    'GENERATE': r'-g\s+(\d+)$',
    'ADD_REQUIREMENT': r'-ar\s+(.+)$',
    'DELETE_REQUIREMENT': r'-dr\s+(\d+)$',
    'PRINT_REQUIREMENTS': '-pr'
    }
