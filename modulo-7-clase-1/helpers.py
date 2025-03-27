import geopy.distance


class Distance:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def km(self):
        return geopy.distance.geodesic(
            (
                (self.source.__dict__())["latitude"],
                (self.source.__dict__()["longitude"]),
            ),
            (
                (self.destination.__dict__())["latitude"],
                (self.destination.__dict__()["longitude"]),
            ),
        ).km

    def nautical(self):
        return geopy.distance.geodesic(
            (
                (self.source.__dict__())["latitude"],
                (self.source.__dict__()["longitude"]),
            ),
            (
                (self.destination.__dict__())["latitude"],
                (self.destination.__dict__()["longitude"]),
            ),
        ).nautical


if __name__ == "__main__":
    from geo_location import Position

    source = Position(1, 2, 3)
    destination = Position(4, 5, 6)
    distance = Distance(source, destination)
    print(distance.km())
    print(distance.nautical())
