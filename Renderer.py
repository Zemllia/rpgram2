class Renderer:

    def render_by_symbols(self, world):
        world_str = ""
        for item in world.mapObjects:
            for item1 in item:
                world_str += item1[len(item1) - 1].sign
            world_str += "\n"
        return world_str

    def render_for_player(self, player, world):
        world_str = ""
        player_pos = player.position
        for i in range(player.fov * -1, player.fov + 1):
            print(world.mapObjects[i])
            for j in range(player.fov * -1, player.fov + 1):
                if (
                        (player_pos.x + i) < 0) or ((player_pos.y + j) < 0
                ) or (
                        (player_pos.x + i) > world.width or (player_pos.y + j) > world.height
                ):
                    world_str += "0  "
                else:
                    world_str += world.mapObjects[player_pos.x + i][player_pos.y + j][
                                     len(world.mapObjects[player_pos.x + i][player_pos.y + j]) - 1].sign
            world_str += "\n"
        return world_str
