import logging

from src.db.db_connector.MongoConnectionService import MongoConnectionService


class BaseMongoRepo:

    @staticmethod
    def insert(obj, collection: str):
        db = MongoConnectionService.get_db_connection()
        insertion_result = db[collection].insert_one(obj)
        MongoConnectionService.close_db_connection()
        return insertion_result.inserted_id

    @staticmethod
    def insert_many(objs, collection):
        db = MongoConnectionService.get_db_connection()
        insertion_result = db[collection].insert_many(objs)
        MongoConnectionService.close_db_connection()

    @staticmethod
    def delete(query, collection):
        db = MongoConnectionService.get_db_connection()
        delete_result = db[collection].delete_one(query)
        MongoConnectionService.close_db_connection()
        return delete_result.deleted_count

    @staticmethod
    def find_one(collection, query={}, fields_filter={}):
        db = MongoConnectionService.get_db_connection()
        query_result = db[collection].find_one(query, fields_filter)
        MongoConnectionService.close_db_connection()
        logging.info(query_result)
        return query_result

    @staticmethod
    def find_all(collection, query={}, fields_filter={}):
        db = MongoConnectionService.get_db_connection()
        cursor = db[collection].find(query, fields_filter)
        query_result = [res for res in cursor]
        MongoConnectionService.close_db_connection()
        return query_result


