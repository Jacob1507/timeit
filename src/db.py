from .infrastructure.in_memory_db import config

Database = config.Database

db = config.Database()


def get_db() -> config.Database:
    return db