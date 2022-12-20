import json

from src.json_encoder.RouteEncoder import RouteEncoder
from src.model.route import Route
from src.presenter.geo_point_presenter import GeoPointPresenter
from src.presenter.presenter import Presenter


class RoutePresenter(Presenter):
    @staticmethod
    def convert_obj_to_repr(obj):
        return json.dumps(obj, cls=RouteEncoder)

    @staticmethod
    def convert_obj_array_to_repr(obj_arr):
        return json.dumps(obj_arr, cls=RouteEncoder)

    @staticmethod
    def convert_repr_to_obj(present):
        return Route(length=present['distance'], destination_points=present['towns'],
                     way_points=GeoPointPresenter.convert_repr_to_obj_array(present['path']))
