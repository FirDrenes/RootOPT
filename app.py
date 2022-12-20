from config.config import ApplicationConfig
from src.Server import Server

import logging

from src.controller.auth_controller import auth_controller
from src.controller.route_controller import route_controller
from src.controller.user_controller import user_controller


def create_app():
    server = Server.get_instance()
    server.initialize(__name__)
    server.configure(ApplicationConfig)

    # register controllers
    server.register_blueprint(auth_controller.bp)
    server.register_blueprint(route_controller.bp)
    server.register_blueprint(user_controller.bp)

    server.init_session()

    return server


logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO)

if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', '5000')



