def read_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        log_lines = file.readlines()
    return log_lines