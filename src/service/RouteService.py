import json
import logging

from flask import g

from src.exception.exception import NotFoundException
from src.db.repo.DestinationRepo import DestinationRepo
from src.db.repo.StoredRouteRepo import StoredRouteRepo
from src.presenter.RoutesListPresenter import RoutesListPresenter
from src.presenter.SolverResultParser import SolverResultParser
from src.presenter.StoredRoutePresenter import StoredRoutePresenter
from src.presenter.destination_point_presenter import DestinationPointPresenter
from src.presenter.route_presenter import RoutePresenter
from src.solver.tsp_solver.tsp_solver import TSPSolver


class RouteService:
    """ Class to manage routes """

    @classmethod
    def get_available_destinations(cls):
        destination_points = DestinationRepo.get_destination_points()
        destinations_repr = DestinationPointPresenter.convert_obj_array_to_repr(destination_points)
        return destinations_repr

    @classmethod
    def save_route(cls, stored_route_repr):
        logging.info('saving route in service....')
        user_id = g.get('user').user_id
        stored_route_repr['author_id'] = user_id
        stored_route = StoredRoutePresenter.convert_repr_to_obj(stored_route_repr)
        logging.info("try insert to mongo")
        StoredRouteRepo.create_route(stored_route)
        logging.info("inserted")
        return StoredRoutePresenter.convert_obj_to_repr(stored_route)

    @classmethod
    def build_route(cls, destinations):
        destination_points = DestinationPointPresenter.convert_repr_to_obj_array(destinations)
        solver = TSPSolver(towns_dict=destination_points, start_town=destination_points[0].name)
        logging.info("solve...")
        solver_result = solver.get_result()
        logging.info("solver result")
        logging.info(solver_result)
        route = SolverResultParser.parse(solver_result)
        route_repr = RoutePresenter.convert_obj_to_repr(route)
        logging.info("route_repr " + str(route_repr))
        return route_repr

    @classmethod
    def delete_stored_route(cls, route_id):
        deleted_count = StoredRouteRepo.delete_route(route_id)
        return deleted_count > 0

    @classmethod
    def get_stored_routes(cls):
        user = g.get("user")
        logging.info("get stored routes of user " + str(user))
        routes_list = StoredRouteRepo.find_all_routes_by_user_id(user.user_id)
        routes_list_repr = RoutesListPresenter.convert_obj_to_repr(routes_list)
        return routes_list_repr

    @classmethod
    def get_stored_route_by_id(cls, route_id):
        route = StoredRouteRepo.find_route_by_id(route_id)
        if route is None:
            raise NotFoundException
        route_repr = StoredRoutePresenter.convert_obj_to_repr(route)
        return route_repr
