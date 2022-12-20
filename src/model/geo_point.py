class GeoPoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        return f"Point: latitude={self.latitude} longitude={self.longitude}"


class DestinationPoint(GeoPoint):
    def __init__(self, point_name, latitude, longitude):
        self.id = None,
        self.name = point_name
        super().__init__(latitude, longitude)

    def __str__(self):
        return f"DestinationPoint: name={self.name} latitude={str(self.latitude)} longitude={str(self.longitude)}"
