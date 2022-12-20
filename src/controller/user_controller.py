from flask import Blueprint, Response, abort

from src.controller.auth_controller import auth_controller
from src.exception.exception import NotFoundException
from src.service.UserService import UserService


class UserController:
    def __init__(self):
        self.bp = Blueprint('user', __name__, url_prefix='/user/')

        @auth_controller.login_required
        @self.bp.route("/me")
        def __get_user_info():
            return self.get_user_info()

    def get_user_info(self):
        try:
            info = UserService.get_user_info()
            return Response(
                response=info,
                status=200,
                mimetype="application/json"
            )
        except NotFoundException:
            abort(401)


user_controller = UserController()
