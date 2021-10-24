class World:

    world_id = 0
    world_name = "Main"

    is_main = True

    width = 500
    height = 500

    mapObjects = []

    def __init__(self, world_id, width, height, is_main, world_name):
        self.world_id = world_id
        self.width = width
        self.height = height
        self.is_main = is_main
        self.world_name = world_name

