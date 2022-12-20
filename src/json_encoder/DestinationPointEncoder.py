import json
import logging

from src.model.geo_point import DestinationPoint


class DestinationPointEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DestinationPoint):
            logging.info(obj)
            return {
                'name': obj.name,
                'longitude': str(obj.longitude),
                'latitude': str(obj.latitude)
            }
        return json.JSONEncoder.default(self, obj)
