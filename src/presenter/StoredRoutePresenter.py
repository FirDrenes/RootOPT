import json

from src.json_encoder.StoredRouteEncoder import StoredRouteEncoder
from src.model.route import StoredRoute
from src.presenter.geo_point_presenter import GeoPointPresenter
from src.presenter.presenter import Presenter


class StoredRoutePresenter(Presenter):
    @staticmethod
    def convert_repr_to_obj(present):
        return StoredRoute(route_name=present['name'], author_id=present['author_id'], length=present['distance'],
                           destination_points=present['towns'],
                           way_points=GeoPointPresenter.convert_repr_to_obj_array(present['path']))

    @staticmethod
    def convert_obj_to_repr(obj):
        return json.dumps(obj, cls=StoredRouteEncoder)
