import json

from src.json_encoder.GeoPointEncoder import GeoPointEncoder
from src.model.route import StoredRoute


class StoredRouteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, StoredRoute):
            return {
                "id": str(obj.route_id),
                "name": obj.route_name,
                "authorId": obj.author_id,
                'distance': obj.length,
                'towns': obj.destination_points,
                'path': [GeoPointEncoder().default(way_point) for way_point in obj.way_points]
            }
        return json.JSONEncoder.default(self, obj)
