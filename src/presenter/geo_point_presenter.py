import json

from src.json_encoder.GeoPointEncoder import GeoPointEncoder
from src.model.geo_point import GeoPoint
from src.presenter.presenter import Presenter


class GeoPointPresenter(Presenter):
    @staticmethod
    def convert_repr_to_obj(present):
        return GeoPoint(latitude=present['latitude'], longitude=present['longitude'])

    @staticmethod
    def convert_repr_to_obj_array(present):
        return list(map(lambda obj_repr: GeoPointPresenter.convert_repr_to_obj(obj_repr), present))

    @staticmethod
    def convert_obj_to_repr(obj):
        return json.dumps(obj, cls=GeoPointEncoder)

    @staticmethod
    def convert_obj_array_to_repr(obj):
        return json.dumps(obj, cls=GeoPointEncoder)
