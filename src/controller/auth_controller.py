import functools
import logging

from flask import Blueprint, request, abort, Response, g, session

from src.exception.exception import BlankUsernameException, BlankPasswordException, UserAlreadyExistsException, \
    InvalidUsernameException, InvalidPasswordException
from src.service.AuthService import AuthService


class AuthController:
    def __init__(self):
        self.bp = Blueprint('auth', __name__, url_prefix='/auth/')

        @self.bp.route('/register/', methods=['POST'])
        def __register():
            logging.info('register...' + str(request.form))
            return self.register(request)

        @self.bp.route('/login', methods=['POST'])
        def __login():
            return self.login(request)

        @self.bp.route('/logout', methods=['POST'])
        def __logout():
            logging.info("logout point")
            return self.logout()

        @self.bp.before_app_request
        def load_logged_in_user():
            try:
                AuthService.load_logged_in_user()
            except Exception as e:
                logging.error(str(e))
                abort(500)

    def register(self, req):
        try:
            user_credentials = self.__grab_user_credentials(req)
            logging.info(user_credentials)
            user_repr = AuthService.register(user_credentials['username'], user_credentials['password'])
            logging.info('registered')
            return Response(
                response=user_repr,
                status=200,
                mimetype='application/json'
            )
        except (BlankUsernameException, BlankPasswordException) as e:
            return str(e), 400
        except UserAlreadyExistsException as e:
            return str(e), 409
        except Exception as e:
            return str(e), 500

    def login(self, req):
        try:
            user_credentials = self.__grab_user_credentials(req)
            user_repr = AuthService.login(user_credentials['username'], user_credentials['password'])
            return Response(
                response=user_repr,
                status=200,
                mimetype='application/json'
            )
        except (BlankUsernameException, BlankPasswordException) as e:
            return str(e), 400
        except (InvalidUsernameException, InvalidPasswordException) as e:
            return str(e), 401
        except Exception as e:
            return str(e), 500

    def logout(self):
        try:
            logging.info("logout")
            AuthService.logout()
            return "", 200
        except Exception as e:
            return str(e), 500

    def login_required(self, route):
        @functools.wraps(route)
        def wrapped_view(*args, **kwargs):
            if g.get('user') is None:
                abort(401)
            return route(*args, **kwargs)

        return wrapped_view

    def __grab_user_credentials(self, req):
        try:
            logging.info('grab user credentials')
            if 'username' not in req.json or 'password' not in req.json:
                abort(400)
            logging.info(req.json)
            username = req.json['username']
            password = req.json['password']
            logging.info('form grabbed')
            return {"username": username, "password": password}
        except Exception as e:
            logging.error(str(e))
            raise e


auth_controller = AuthController()