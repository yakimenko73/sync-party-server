from dataclasses import dataclass

from envclasses import envclass


@envclass
@dataclass
class MongoDbCredentials:
    host: str = 'localhost'
    port: int = 27017
    database: str = 'mongodb'
    username: str = 'admin'
    password: str = 'admin'


@envclass
@dataclass
class ServerParams:
    host: str = 'localhost'
    port: int = 8000
    debug: int = 1
    secret_key: str = 'super-duper-secret-key'
