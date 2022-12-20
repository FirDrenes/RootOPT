import json
import logging

from src.model.geo_point import GeoPoint


class GeoPointEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, GeoPoint):
            logging.info(obj)
            return {
                "latitude": str(obj.latitude),
                "longitude": str(obj.longitude)
            }
        return json.JSONEncoder.default(self, obj)
