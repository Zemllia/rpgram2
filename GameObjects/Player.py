from GameObjects.Creature import Creature
from GameObjects.WorldObject import WorldObject


class Player(Creature):
    nickname = "Player"

    def __init__(self, nickname, level, xp, hp, position):
        self.nickname = nickname
        self.level = level
        self.xp = xp
        self.position = position
        self.hp = hp

    def move(self, world, side):
        world.mapObjects[self.position.x][self.position.y].pop(self.position.z)
        if side == "left":
            self.position.y -= 1
        elif side == "right":
            self.position.y += 1
        elif side == "up":
            self.position.x -= 1
        elif side == "down":
            self.position.x += 1
        new_world_pos = world.mapObjects[self.position.x][self.position.y]
        new_world_pos.append(WorldObject(self.position, "Player", self.nickname[0], True, "player", self))
        self.position.z = len(new_world_pos) - 1

    def spawn(self, world):
        new_world_pos = world.mapObjects[self.position.x][self.position.y]
        new_world_pos.append(WorldObject(self.position, "Player", self.nickname[0], True, "player", self))
        self.position.z = len(new_world_pos) - 1
