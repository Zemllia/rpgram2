from GameObjects.MapObjects.Coin import Coin
from Position import Position


class InventoryObject:
    map_object_class = Coin
    name = "Coin"
    # -1 if inf or count
    max_stack = -1
    weight = 0
    description = "No one knows who made this coins, but everyone uses them for pay"

    items_count = 1

    def __init__(self, map_object_class, name, max_stack, weight, description):
        self.map_object_class = map_object_class
        self.name = name
        self.max_stack = max_stack
        self.weight = weight
        self.description = description

    def instantiate_to_map_object(self):
        return self.map_object_class(Position(0, 0, 0))
