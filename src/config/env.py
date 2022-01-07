import os

from django.conf import settings


def parse_env_file_from_command_line():
    path_to_env_file = os.environ.get(settings.ENV_FILE_ARG)
    if os.path.isfile(path_to_env_file):
        with open(path_to_env_file, 'r') as f:
            for line in f.readlines():
                key, value = line.split("=")
                os.environ[key] = value
