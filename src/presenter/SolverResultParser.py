from src.model.route import Route
from src.model.geo_point import GeoPoint


class SolverResultParser:
    @staticmethod
    def parse(result):
        return Route(length=result['distance'], destination_points=result['towns'],
              way_points=SolverResultParser.__convert_path(result['path']))

    @staticmethod
    def __convert_path(path):
        return list(map(lambda node: SolverResultParser.__convert_path_node(node), path))

    @staticmethod
    def __convert_path_node(node):
        return GeoPoint(node[0], node[1])