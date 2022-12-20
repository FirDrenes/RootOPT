from abc import ABC, abstractmethod


class DBConnectionService(ABC):
    """ Abstract class to manage database connection """

    @classmethod
    @abstractmethod
    def get_db_connection(cls):
        pass

    @classmethod
    @abstractmethod
    def open_db_connection(cls):
        pass

    @classmethod
    @abstractmethod
    def close_db_connection(cls):
        pass

