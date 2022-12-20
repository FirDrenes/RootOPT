import logging

from flask import g

from src.exception.exception import NotFoundException
from src.presenter.user_presenter import UserPresenter


class UserService:
    @classmethod
    def get_user_info(cls):
        logging.info("get user info")
        user = g.user
        logging.info("user info " + str(user))
        if user is None:
            raise NotFoundException
        user_repr = UserPresenter.convert_obj_to_repr(user)
        return user_repr
