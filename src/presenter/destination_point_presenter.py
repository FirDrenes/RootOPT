import json

from src.json_encoder.DestinationPointEncoder import DestinationPointEncoder
from src.model.geo_point import DestinationPoint
from src.presenter.presenter import Presenter


class DestinationPointPresenter(Presenter):
    @staticmethod
    def convert_obj_to_repr(obj):
        return json.dumps(obj, cls=DestinationPointEncoder)

    @staticmethod
    def convert_obj_array_to_repr(obj_arr):
        return json.dumps(obj_arr, cls=DestinationPointEncoder)

    @staticmethod
    def convert_repr_to_obj(present):
        return DestinationPoint(present['name'], present['latitude'], present['longitude'])

    @staticmethod
    def convert_repr_to_obj_array(present):
        return list(map(lambda obj_repr: DestinationPointPresenter.convert_repr_to_obj(obj_repr), present))
