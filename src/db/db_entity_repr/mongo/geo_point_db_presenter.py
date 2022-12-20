from src.model.geo_point import GeoPoint
from src.presenter.presenter import Presenter


class GeoPointDbPresenter(Presenter):
    @staticmethod
    def convert_obj_to_repr(obj):
        return {
            "latitude": obj.latitude,
            "longitude": obj.longitude
        }

    @staticmethod
    def convert_obj_array_to_repr(obj_arr):
        return list(map(lambda obj: GeoPointDbPresenter.convert_obj_to_repr(obj), obj_arr))

    @staticmethod
    def convert_repr_to_obj(db_repr):
        return GeoPoint(db_repr["latitude"], db_repr["longitude"])

    @staticmethod
    def convert_repr_to_obj_array(db_repr_arr):
        return list(map(lambda obj_repr: GeoPointDbPresenter.convert_repr_to_obj(obj_repr), db_repr_arr))
