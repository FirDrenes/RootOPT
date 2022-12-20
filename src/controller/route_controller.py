import logging

from flask import Blueprint, request, Response, abort

from src.exception.exception import NotFoundException
from src.controller.auth_controller import auth_controller
from src.service.RouteService import RouteService


class RouteController:
    def __init__(self):
        self.bp = Blueprint('route', __name__, url_prefix='/route/')

        @self.bp.route('/destinations', methods=['GET'])
        def __get_destinations_list():
            return self.get_destinations_list()

        @self.bp.route('/build', methods=['POST'])
        def __build_route():
            return self.build_route(request)

        @self.bp.route('/save', methods=['POST'])
        def __save_route():
            return self.save_route(request)

        @self.bp.route('/saved/list', methods=['GET'])
        def __get_stored_routes():
            # todo: return ids and names instead of whole routes
            return self.get_stored_routes()

        @self.bp.route('/saved/delete/<route_id>', methods=['DELETE'])
        def __delete_route(route_id):
            return self.delete_route(route_id)

        @self.bp.route('/saved/<route_id>', methods=['GET'])
        def __get_stored_route(route_id):
            return self.get_stored_route(route_id)

    def get_destinations_list(self):
        destinations_repr = RouteService.get_available_destinations()
        return Response(
            response=destinations_repr,
            status=200,
            mimetype='application/json'
        )

    def build_route(self, req):
        destinations = req.json['destinations']
        route_repr = RouteService.build_route(destinations)
        return Response(
            response=route_repr,
            status=200,
            mimetype='application/json'
        )

    @auth_controller.login_required
    def save_route(self, req):
        logging.info("saving route..." + str(req.data))
        logging.info(req.json)
        route_repr = req.json['route']
        logging.info(route_repr)
        stored_route_repr = RouteService.save_route(route_repr)
        return Response(
            response=stored_route_repr,
            status=201,
            mimetype='application/json'
        )

    @auth_controller.login_required
    def delete_route(self, route_id):
        delete_result = RouteService.delete_stored_route(route_id)
        response_status = 200 if delete_result else 204
        return Response(
            status=response_status
        )

    @auth_controller.login_required
    def get_stored_routes(self):
        routes_repr = RouteService.get_stored_routes()
        return Response(
            response=routes_repr,
            status=200,
            mimetype="application/json"
        )

    @auth_controller.login_required
    def get_stored_route(self, route_id):
        try:
            route_repr = RouteService.get_stored_route_by_id(route_id)
            return Response(
                response=route_repr,
                status=200,
                mimetype="application/json"
            )
        except NotFoundException:
            abort(404)


route_controller = RouteController()
