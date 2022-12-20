import json

from src.json_encoder.UserEncoder import UserEncoder
from src.model.user import User
from src.presenter.presenter import Presenter


class UserPresenter(Presenter):
    @staticmethod
    def convert_obj_to_repr(obj):
        return json.dumps(obj, cls=UserEncoder)

    @staticmethod
    def convert_repr_to_obj(present):
        return User(present['username'], present['password'])