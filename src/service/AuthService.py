from flask import session, g
from werkzeug.security import generate_password_hash, check_password_hash

from src.exception.exception import *
from src.db.repo.UserRepo import UserRepo
from src.model.user import User
import logging

from src.presenter.user_presenter import UserPresenter


class AuthService:
    """ Class to manage authentication process """

    @classmethod
    def register(cls, username, password):
        logging.info("register in service... " + username + " " + password)
        cls.__check_blank_fields(username, password)
        if cls.__does_user_exist(username):
            raise UserAlreadyExistsException
        hashed_password = generate_password_hash(password)
        logging.info("hashed password")
        user = User(username, hashed_password)
        logging.info("user object instantiated")
        created_user = UserRepo.create_user(user)
        logging.info("user created")
        created_user.password = ""
        user_repr = UserPresenter.convert_obj_to_repr(created_user)
        return user_repr

    @staticmethod
    def __does_user_exist(username):
        user = UserRepo.find_user_by_username(username)
        if not user:
            return False
        return True

    @staticmethod
    def __check_blank_fields(username, password):
        if not username:
            raise BlankUsernameException
        if not password:
            raise BlankPasswordException

    @classmethod
    def login(cls, username, password):
        cls.__check_blank_fields(username, password)
        user = UserRepo.find_user_by_username(username)
        if not user:
            raise InvalidUsernameException
        elif not check_password_hash(user.password, password):
            raise InvalidPasswordException
        user.password = ""
        user_repr = UserPresenter.convert_obj_to_repr(user)
        session.clear()
        session['user_id'] = user.user_id
        logging.info('user id = ' + str(session.get('user_id')))
        return user_repr

    @classmethod
    def logout(cls):
        logging.info("logout...")
        session['user_id'] = None
        session.clear()
        logging.info(str(session.get('user_id')))

    @classmethod
    def load_logged_in_user(cls):
        try:
            logging.info("load logged in user")
            user_id = session.get('user_id')
            logging.info('user id = ' + str(user_id))
            if user_id is None:
                logging.info('user_id is None')
                g.user = None
            else:
                logging.info('user_id ' + user_id)
                g.user = UserRepo.find_user_by_id(user_id)
                g.user.password = ""
        except Exception as e:
            logging.error(e)



