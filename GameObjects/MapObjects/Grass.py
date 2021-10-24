from GameObjects.MapObject import MapObject
from Position import Position


class Grass(MapObject):

    position = Position(0, 0, 0)

    def __init__(self, position):
        self.position = position
