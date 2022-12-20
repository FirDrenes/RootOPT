from bson import ObjectId

from src.db.db_entity_repr.mongo.geo_point_db_presenter import GeoPointDbPresenter
from src.model.route import StoredRoute
from src.presenter.presenter import Presenter


class StoredRouteDbPresenter(Presenter):
    @staticmethod
    def convert_obj_to_repr(obj):
        db_repr = {
            "route_name": obj.route_name,
            "author_id": ObjectId(obj.author_id),
            "created_at": obj.created_at,
            "length": obj.length,
            "destination_points": obj.destination_points,
            "way_points": GeoPointDbPresenter.convert_obj_array_to_repr(obj.way_points)
        }
        if obj.route_id is not None:
            db_repr['_id'] = ObjectId(obj.route_id)
        return db_repr

    @staticmethod
    def convert_repr_to_obj(db_repr):
        return StoredRoute(route_id=str(db_repr["_id"]), route_name=db_repr["route_name"], length=db_repr["length"],
                           author_id=str(db_repr["author_id"]), created_at=db_repr["created_at"],
                           destination_points=db_repr["destination_points"],
                           way_points=GeoPointDbPresenter.convert_repr_to_obj_array(db_repr["way_points"]))

    @staticmethod
    def convert_repr_to_obj_array(db_repr):
        return list(map(lambda route_repr: StoredRouteDbPresenter.convert_repr_to_obj(db_repr), db_repr))
