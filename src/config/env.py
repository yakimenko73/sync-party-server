from envclasses import load_env

from config.model import MongoDbCredentials, ServerParams

MONGODB_CREDS_ENV_PREFIX = 'MONGODB'
SERVER_PARAMS_ENV_PREFIX = 'DJANGO'


def get_mongodb_credentials() -> MongoDbCredentials:
    instance = MongoDbCredentials()
    load_env(instance, MONGODB_CREDS_ENV_PREFIX)

    return instance


def get_server_params() -> ServerParams:
    instance = ServerParams()
    load_env(instance, SERVER_PARAMS_ENV_PREFIX)

    return instance
