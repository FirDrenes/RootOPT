import logging

from src.db.db_entity_repr.mongo.stored_route_db_presenter import StoredRouteDbPresenter
from src.db.repo.BaseMongoRepo import BaseMongoRepo

from bson.objectid import ObjectId


class StoredRouteRepo(BaseMongoRepo):
    __mongo_collection = "storedRoutes"

    @classmethod
    def create_route(cls, route):
        logging.info("insert to storedRoutes")
        db_repr = StoredRouteDbPresenter.convert_obj_to_repr(route)
        inserted_id = cls.insert(db_repr, cls.__mongo_collection)
        route.route_id = inserted_id
        return route

    @classmethod
    def delete_route(cls, route_id):
        logging.info("delete route by id")
        query = {"_id" : ObjectId(route_id)}
        deleted_count = cls.delete(query, cls.__mongo_collection)
        return deleted_count

    @classmethod
    def find_all_routes_by_user_id(cls, user_id):
        logging.info("find all by user id " + str(user_id))
        query = {"author_id": ObjectId(user_id)}
        fields_filter = {"_id": 1, "route_name": 1}
        find_result = cls.find_all(cls.__mongo_collection, query=query, fields_filter=fields_filter)
        logging.info(find_result)
        return find_result

    @classmethod
    def find_route_by_id(cls, route_id):
        query = {"_id": ObjectId(route_id)}
        route_db_repr = cls.find_one(query=query, collection=cls.__mongo_collection)
        if route_db_repr is not None:
            route = StoredRouteDbPresenter.convert_repr_to_obj(route_db_repr)
        else:
            route = None
        return route



