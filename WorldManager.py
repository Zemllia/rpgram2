from GameObjects.MapObjects.Void import Void
from GameObjects.World import World
from GameObjects.WorldObject import WorldObject
from Position import Position


class WorldManager:
    worlds = []

    def generate_world(self, width, height):
        world = World(width, height)
        for i in range(0, height):
            newColumn = []
            for j in range(0, width):
                position = Position(i, j, 0)
                newColumn.append([WorldObject(position, "void", "#", False, "void", Void(position), world)])
            world.mapObjects.append(newColumn)
        self.worlds.append(world)
        return world
