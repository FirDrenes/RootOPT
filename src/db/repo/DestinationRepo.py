import logging

from src.db.repo.BasePostgresRepo import BasePostgresRepo
from src.model.geo_point import DestinationPoint


class DestinationRepo(BasePostgresRepo):
    @classmethod
    def get_destination_points(cls):
        query = 'SELECT * FROM destination_points'
        query_results = cls.execute_query(query)
        logging.info("destination points:")
        logging.info(query_results)

        destination_points = []
        for row in query_results:
            point_id = row['point_id']
            point_name = row['point_name']
            latitude = row['latitude']
            longitude = row['longitude']
            destination_point = DestinationPoint(point_name, latitude, longitude)
            logging.info(destination_point)
            destination_points.append(destination_point)

        logging.info(destination_points)

        return destination_points
