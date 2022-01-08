import os


def parse_env_file_from_command_line(arg_name: str):
    path_to_env_file = os.environ.get(arg_name)
    if path_to_env_file and os.path.isfile(path_to_env_file):
        with open(path_to_env_file, 'r') as f:
            for line in f.readlines():
                key, value = line.split("=")
                os.environ[key] = value
