import logging

from bson import ObjectId

from src.db.db_entity_repr.mongo.user_db_presenter import UserDbPresenter
from src.db.repo.BaseMongoRepo import BaseMongoRepo


class UserRepo(BaseMongoRepo):
    __mongo_collection = "users"

    @classmethod
    def find_user_by_id(cls, user_id):
        query = {'_id': ObjectId(user_id)}
        logging.info("find user by query ")
        logging.info(query)
        user_db_repr = cls.find_one(query=query, collection=cls.__mongo_collection)
        logging.info("user found:")
        logging.info(user_db_repr)
        if user_db_repr is not None:
            user = UserDbPresenter.convert_repr_to_obj(user_db_repr)
        else:
            user = None
        return user

    @classmethod
    def find_user_by_username(cls, username):
        query = {'username': username}
        logging.info("find user by query ")
        logging.info(query)
        user_db_repr = cls.find_one(query=query, collection=cls.__mongo_collection)
        logging.info("user found:")
        logging.info(user_db_repr)
        if user_db_repr is not None:
            user = UserDbPresenter.convert_repr_to_obj(user_db_repr)
        else:
            user = None

        return user

    @classmethod
    def create_user(cls, user):
        logging.info("creating user...." + str(user))
        user_db_repr = UserDbPresenter.convert_obj_to_repr(user)
        logging.info(user_db_repr)
        user_id = cls.insert(user_db_repr, cls.__mongo_collection)
        user_db_repr['_id'] = user_id
        inserted_user = UserDbPresenter.convert_repr_to_obj(user_db_repr)
        return inserted_user

    @classmethod
    def delete_user(cls, user_id):
        query = {'_id': ObjectId(user_id)}
        return cls.delete(query, cls.__mongo_collection)
