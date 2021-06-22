import random

from GameObjects.MapObjects.Grass import Grass
from GameObjects.MapObjects.Tree import Tree
from GameObjects.MapObjects.Void import Void
from GameObjects.World import World
from GameObjects.WorldObject import WorldObject
from Position import Position


class WorldManager:
    worlds = []

    tree_spawn_chance = 20

    def generate_main_world(self, width, height):
        world = World(0, width, height, True, "Main")
        for i in range(0, height):
            newColumn = []
            for j in range(0, width):
                position = Position(i, j, 0)
                newColumn.append([WorldObject(position, "grass", "\"  ", True, "grass", Grass(position), world)])
            world.mapObjects.append(newColumn)

        for i in range(0, height):
            for j in range(0, width):
                position = Position(i, j, 1)
                if random.randint(0, 100) < self.tree_spawn_chance:
                    world.mapObjects[i][j].append(WorldObject(position, "tree", "🌲 ", False, "tree", Tree(position), world))
        self.worlds.append(world)
        return world

    def get_world_by_id(self, world_id):
        for item in self.worlds:
            if item.world_id == world_id:
                return item
        return None
