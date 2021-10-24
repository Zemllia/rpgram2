from GameObjects.InventoryObject import InventoryObject
from GameObjects.MapObjects.Rock import Rock
from Position import Position


class InventoryRock(InventoryObject):
    map_object_class = Rock
    name = "Coin"
    # -1 if inf or count
    max_stack = -1
    weight = 0
    description = "No one knows who made this coins, but everyone uses them for pay"

    items_count = 1

    def instantiate_to_map_object(self):
        return self.map_object_class(Position(0, 0, 0))
