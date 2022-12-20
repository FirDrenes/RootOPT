import datetime


class Route:
    def __init__(self, length=0, destination_points=[], way_points=[]):
        self.destination_points = destination_points
        self.way_points = way_points
        self.length = length

    def __str__(self):
        return f"Route: \n" \
               f"length: {self.length}\n" \
               f"destination_points: {self.destination_points}"


class StoredRoute(Route):
    def __init__(self, route_name, author_id, length=0, destination_points=[], way_points=[], route_id=None, created_at=None):
        self.route_id = route_id
        self.route_name = route_name
        self.author_id = author_id
        self.created_at = created_at if created_at is not None else datetime.datetime.utcnow()
        super().__init__(length, destination_points, way_points)

    def __str__(self):
        return f"Route:\n" \
               f"name: {self.route_name}\n" \
               f"author_id: {self.author_id}\n" \
               f"created_at: {self.created_at}\n" \
               f"length: {self.length}\n" \
               f"destination_points: {self.destination_points}"

