from pymongo import MongoClient


class ApplicationConfig:
    SECRET_KEY = 'dev'

    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USER_SIGNER = True
    SESSION_MONGODB = MongoClient('localhost', 27017)
    SESSION_MONGODB_DB = 'root_opt_sessions'
