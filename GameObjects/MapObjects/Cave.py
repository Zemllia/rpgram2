from GameObjects.MapObject import MapObject
from Position import Position


class Cave(MapObject):

    position = Position(0, 0, 0)

    possible_actions = [
        "enter"
    ]

    main_world = None
    cave_world = None
    cave_spawn_point = Position(0, 0, 0)

    def action(self, action, player, world):
        if action not in self.possible_actions:
            return "action_not_supported"
        if action == "enter":
            player.remove_from_current_world()
            player.spawn_in_current_position(self.cave_world, self.cave_spawn_point)

    def __init__(self, position, main_world, cave_world, cave_spawn_point):
        self.position = position
        self.main_world = main_world
        self.cave_world = cave_world
        self.cave_spawn_point = cave_spawn_point
