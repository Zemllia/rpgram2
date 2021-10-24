from Position import Position


class MapObject:
    position = Position(0, 0, 0)

    possible_actions = []

    count = 1

    def action(self, action, player, world):
        if action not in self.possible_actions:
            return "action_not_supported"
