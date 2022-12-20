from flask import Flask
from flask_cors import CORS
from flask_session import Session
import os

from src.exception.exception import NotInitializedException


class Server:
    """
    Class representing app server
    """

    __instance = None

    def __init__(self):
        if not Server.__instance:
            print('init')
            self.__app = None
            self.__initialized = False
            self.__configured = False
            self.__server_session = None


    def __check_initialized(func):
        def wrapper(self, *args, **kwargs):
            if not self.__initialized:
                raise NotInitializedException
            func(self, *args, **kwargs)
        return wrapper

    def __check_configured(func):
        def wrapper(self, *args, **kwargs):
            if not self.__configured:
                raise NotInitializedException
            func(self, *args, **kwargs)
        return wrapper

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Server()
        return cls.__instance

    def initialize(self, name):
        self.__app = Flask(name)
        self.__initialized = True
        # CORS(self.__app, resources={r"*": {"origins": "*"}})
        CORS(self.__app, supports_credentials=True)

    @__check_configured
    def init_session(self):
        pass
        # self.__server_session = Session(self.__app)

    @__check_initialized
    def configure(self, configuration=None):
        if not self.__initialized:
            raise Exception('not initialized')
        # todo: replace secret key
        self.__app.config.from_mapping(
            SECRET_KEY='dev'
        )
        if configuration:
            self.__app.config.from_object(configuration)
        try:
            os.makedirs(self.__app.instance_path)
        except OSError:
            pass
        self.__configured = True

        @self.__app.route('/hello')
        def __hello():
            return self.hello()

    @__check_initialized
    def register_db_connector(self, db_connector):
        self.__app.teardown_appcontext(db_connector.close_db)

    @__check_initialized
    def register_blueprint(self, blueprint):
        self.__app.register_blueprint(blueprint)


    @__check_configured
    def run(self, host, port):
        self.__app.run(host, port)

    def hello(self):
        return 'Hello, World!'
