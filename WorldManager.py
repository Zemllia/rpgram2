from GameObjects.MapObjects.Void import Void
from GameObjects.World import World
from GameObjects.WorldObject import WorldObject
from Position import Position


class WorldManager:
    worlds = []

    def generate_main_world(self, width, height):
        world = World(0, width, height, True, "Main")
        for i in range(0, height):
            newColumn = []
            for j in range(0, width):
                position = Position(i, j, 0)
                newColumn.append([WorldObject(position, "void", "#", False, "void", Void(position), world)])
            world.mapObjects.append(newColumn)
        self.worlds.append(world)
        return world

    def get_world_by_id(self, world_id):
        for item in self.worlds:
            if item.world_id == world_id:
                return item
        return None
