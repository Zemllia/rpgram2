class Renderer:

    def render_by_symbols(self, world):
        world_str = ""
        for item in world.mapObjects:
            for item1 in item:
                world_str += item1[len(item1) - 1].sign + "  "
            world_str += "\n"
        return world_str
