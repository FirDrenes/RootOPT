import logging

from pymongo import MongoClient

from src.db.db_connector.DBConnectionService import DBConnectionService


class MongoConnectionService(DBConnectionService):
    """ Class to connect MongoDB """

    __connection = None

    @classmethod
    def get_db_connection(cls):
        if cls.__connection is None:
            cls.open_db_connection()
        return cls.__connection['root_opt']

    @classmethod
    def open_db_connection(cls):
        if cls.__connection is not None:
            cls.close_db_connection()
        cls.__connection = MongoClient('localhost', 27017)

    @classmethod
    def close_db_connection(cls):
        if cls.__connection is not None:
            cls.__connection.close()
            cls.__connection = None
