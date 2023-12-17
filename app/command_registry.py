import command_exe as command_exe

engine_commands = {
    r'-w\s+(.+)$': command_exe.write_data,                  # write data to file: -w <path>
    r'\s*-idb\s*': command_exe.insert_into_db,              # insert data into database: -idb
    r'-g\s+(\d+)$': command_exe.generate,                   # generate data for all tables: -g <number>
    r'-g\s+(\d+)\s+-t\s+(\d+)$': command_exe.generate,      # generate data for given table: -g <number> -t <table_index>
    r'-ar\s+(.+)$': command_exe.add_requirement,            # add requirement to requirement list: -ar <requirement_text>
    r'-dr\s+(\d+)$': command_exe.delete_requirement,        # delete requirement: -dr <index>
    r'\s*-pr\s*': command_exe.print_requirements,           # print requirements: -pr
    r'-at\s+(\d+)$': command_exe.add_table,                 # add table to prompt: -at <table_index>
    r'-dt\s+(\d+)$': command_exe.delete_table,              # delete table from prompt: -dt <table_index>
    r'\s*-ptp\s*': command_exe.see_tables,                  # see tables added to prompt: -ptp
    r'\s*-pp\s*': command_exe.print_prompt,                 # print prompt: -pp
    r'\s*-ct\s*': command_exe.clear_tables,                 # clear tables added to prompt: -ct
    r'\s*-cr\s*': command_exe.clear_requirements,           # clear requirements: -cr
    }

non_engine_commands = { 
    r'\s*--help\s*': command_exe.print_help,                # print help: --help
    r'^\-pt$': command_exe.print_tables,                    # print tables: -pt
    r'\s*-ptr\s*': command_exe.print_table_relationships,   # print table relationships: -ptr
    r'\s*-pto\s*': command_exe.print_table_order,           # print table order: -pto
    r'\s*--start\s*': command_exe.start_engine,             # start engine - saves input by user for reusability: --start
    r'\s*--stop\s*': command_exe.stop_engine,               # stop engine - clears everything, fresh start: --stop
    r'\s*-q\s*': command_exe.quit,                          # quit program: -q
    r'\s*--models\s*': command_exe.print_models,            # print all available OpenAI API models: --models
    r'--setmodel\s+(\d+)$': command_exe.set_model,          # set OpenAI API model: --setmodel <model_index>
    r'\s*--getmodel\s*': command_exe.print_get_model,       # get current OpenAI API model: --getmodel
    }