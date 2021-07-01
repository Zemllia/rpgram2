import random

import Config
from GameObjects.MapObjects.Grass import Grass
from GameObjects.MapObjects.Tree import Tree
from GameObjects.World import World
from GameObjects.WorldObject import WorldObject
from Position import Position


class WorldManager:
    worlds = []

    tree_spawn_chance = 20

    world_legend = {
        "version": Config.LEGEND_VERSION,
        "legend": [
            {
                "name": "grass",
                "symbol": "\"",
                "image": str(Config.PROTOCOL) + str(Config.HOST) + ":" + str(Config.PORT) + "/static/images/grass.png",
                "actions": []
            },
            {
                "name": "tree",
                "symbol": "🌲",
                "image": str(Config.PROTOCOL) + str(Config.HOST) + ":" + str(Config.PORT) + "/static/images/tree.png",
                "actions": []
            },
            {
                "name": "void",
                "symbol": "0",
                "image": str(Config.PROTOCOL) + str(Config.HOST) + ":" + str(Config.PORT) + "/static/images/void.png",
                "actions": []
            }
        ]
    }

    def generate_main_world(self, width, height):
        world = World(0, width, height, True, "Main")
        for i in range(0, height):
            newColumn = []
            for j in range(0, width):
                position = Position(i, j, 0)
                grass_legend = self.get_from_legend_by_name("grass")
                newColumn.append([WorldObject(position, grass_legend.get("name"),
                                              grass_legend.get("symbol") + "  ",
                                              True, grass_legend.get("name"),
                                              Grass(position), world)])
            world.mapObjects.append(newColumn)

        for i in range(0, height):
            for j in range(0, width):
                position = Position(i, j, 1)
                if random.randint(0, 100) < self.tree_spawn_chance:
                    tree_legend = self.get_from_legend_by_name("tree")
                    world.mapObjects[i][j].append(WorldObject(position, tree_legend.get("name"),
                                                              tree_legend.get("symbol") + " ", False,
                                                              tree_legend.get("name"), Tree(position),
                                                              world))
        self.worlds.append(world)
        return world

    def get_world_by_id(self, world_id):
        for item in self.worlds:
            if item.world_id == world_id:
                return item
        return None

    def get_from_legend_by_name(self, name):
        for item in self.world_legend.get("legend"):
            if item.get("name") == name:
                return name
        return None

    # def save(self):
    #     for world in self.worlds:
    #
