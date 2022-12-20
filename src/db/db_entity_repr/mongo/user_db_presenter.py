from bson import ObjectId

from src.model.user import User
from src.presenter.presenter import Presenter


class UserDbPresenter(Presenter):
    @staticmethod
    def convert_obj_to_repr(obj):
        db_repr = {
            "username": obj.username,
            "password": obj.password
        }
        if obj.user_id is not None:
            db_repr['_id'] = ObjectId(obj.user_id)
        return db_repr

    @staticmethod
    def convert_repr_to_obj(present):
        return User(user_id=str(present['_id']), username=present['username'], password=present['password'])
