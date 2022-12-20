from os import environ

import psycopg2
from psycopg2.extras import DictCursor

from src.db.db_connector.DBConnectionService import DBConnectionService


class PostgresConnectionService(DBConnectionService):
    """ Class to manage postgres connection """
    __connection = None

    @classmethod
    def get_db_connection(cls):
        if cls.__connection is None:
            cls.open_db_connection()
        return cls.__connection

    @classmethod
    def open_db_connection(cls):
        if cls.__connection is not None:
            cls.close_db_connection()
        cls.__connection = psycopg2.connect(user=environ['PGUSER'],
                                            password=environ['PGPASSWORD'],
                                            host='127.0.0.1',
                                            port='5432',
                                            database='RootOPT',
                                            cursor_factory=DictCursor)
        return cls.__connection

    @classmethod
    def close_db_connection(cls):
        if cls.__connection is not None:
            cls.close_db_connection()