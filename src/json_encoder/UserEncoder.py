import json

from src.model.user import User


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'user_id': obj.user_id,
                'username': obj.username,
                'password': obj.password
            }
        return json.JSONEncoder.default(self, obj)
