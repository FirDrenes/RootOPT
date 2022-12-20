import json
import logging

from src.json_encoder.GeoPointEncoder import GeoPointEncoder
from src.model.route import Route


class RouteEncoder(json.JSONEncoder):
    def default(self, obj):
        logging.info("try encode object " + str(obj))

        if isinstance(obj, Route):
            logging.info("object os Route")
            return {
                'distance': obj.length,
                'towns': obj.destination_points,
                'path': [GeoPointEncoder().default(way_point) for way_point in obj.way_points]
            }
        return json.JSONEncoder.default(self, obj)
