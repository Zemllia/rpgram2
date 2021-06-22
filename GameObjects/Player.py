from GameObjects.Creature import Creature
from GameObjects.WorldObject import WorldObject
from Position import Position


class Player(Creature):
    nickname = "Player"
    player_id = 0

    def __init__(self, player_id, nickname, level, xp, hp, position, fov):
        self.nickname = nickname
        self.level = level
        self.xp = xp
        self.position = position
        self.hp = hp
        self.fov = fov
        self.id = player_id

    def move(self, world, side):
        world.mapObjects[self.position.x][self.position.y].pop(self.position.z)
        new_pos = Position(self.position.x, self.position.y, self.position.z)
        if side == "left":
            new_pos.y -= 1
        elif side == "right":
            new_pos.y += 1
        elif side == "up":
            new_pos.x -= 1
        elif side == "down":
            new_pos.x += 1

        if not world.mapObjects[self.position.x][self.position.y][len(world.mapObjects[self.position.x][self.position.y]) - 1].is_walkable:
            return {"is_moved": False, "position": {"x": self.position.x, "y": self.position.y, "z": self.position.z},
                    "cause": "not_walkable"}

        if (new_pos.x < 0) or (new_pos.y < 0) or (new_pos.x > world.width) or (new_pos.y > world.height):
            return {"is_moved": False, "position": {"x": self.position.x, "y": self.position.y, "z": self.position.z},
                    "cause": "end_of_map"}
        self.position = new_pos
        new_world_pos = world.mapObjects[self.position.x][self.position.y]
        new_world_pos.append(WorldObject(self.position, "Player", self.nickname[0], False, "player", self, world))
        self.position.z = len(new_world_pos) - 1
        return {"is_moved": True, "position": {"x": self.position.x, "y": self.position.y, "z": self.position.z}}

    def spawn(self, world):
        new_world_pos = world.mapObjects[self.position.x][self.position.y]
        new_world_pos.append(WorldObject(self.position, "Player", self.nickname[0], False, "player", self, world))
        self.position.z = len(new_world_pos) - 1
