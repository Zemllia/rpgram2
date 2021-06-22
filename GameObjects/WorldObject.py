from GameObjects.MapObject import MapObject


class WorldObject(MapObject):
    name = "Void"
    sign = "#"
    is_walkable = False
    object_type = "player"
    controller = None

    def __init__(self, position, name, sign, is_walkable, object_type, controller):
        self.position = position
        self.name = name
        self.sign = sign
        self.is_walkable = is_walkable
        self.object_type = object_type
        self.controller = controller
