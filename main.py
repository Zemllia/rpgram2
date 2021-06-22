from flask import Flask, request

from GameObjects.Player import Player
from PlayerManager import PlayerManager
from Position import Position
from Renderer import Renderer
from WorldManager import WorldManager

app = Flask(__name__)

renderer = Renderer()
world_manager = WorldManager()
player_manager = PlayerManager()

players = []


@app.route('/get_worlds_info')
def get_worlds_info():
    answer = {"status": "success", "message": []}
    for cur_world in world_manager.worlds:
        answer.get("message").append({"id": cur_world.world_id, "name": cur_world.world_name})
    return answer


@app.route('/spawn_player')
def spawn_player():
    world_id = request.args.get("world_id")
    world = world_manager.get_world_by_id(int(world_id))
    player_name = request.args.get("name")
    player = player_manager.create_or_load_player(player_name, world)
    return {"status": "success", "message": {"player_id": player.player_id}}


@app.route('/render_player')
def render_player():
    cur_player_id = request.args.get("id")
    player = player_manager.get_player_by_id(int(cur_player_id))
    world = world_manager.get_world_by_id(int(0))
    result = renderer.render_for_player(player, world)
    return result


@app.route('/move_player')
def move_player():
    cur_player_id = request.args.get("id")
    move_side = request.args.get("move_side")
    player = player_manager.get_player_by_id(int(cur_player_id))
    world = world_manager.get_world_by_id(int(0))
    player.move(world, move_side)
    return {"status": "success", "message": {"new_position": {"x": player.postition.x, "y": player.postition.y, "z": player.postition.z}}}


def start():
    new_world = world_manager.generate_main_world(10, 10)
    player = Player(-1, "Zemlia", 1, 1, 100, Position(0, 0, 0), 5)
    player.spawn(new_world)
    renderer_result = Renderer().render_by_symbols(new_world)
    print(renderer_result)
    player.move(new_world, "right")
    renderer_result = Renderer().render_by_symbols(new_world)
    print(renderer_result)
    player.move(new_world, "down")
    renderer_result = Renderer().render_by_symbols(new_world)
    print(renderer_result)
    app.run(debug=False)


if __name__ == '__main__':
    start()
