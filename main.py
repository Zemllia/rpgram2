from flask import Flask, request

from GameObjects.Player import Player
from Position import Position
from Renderer import Renderer
from WorldManager import WorldManager

app = Flask(__name__)

renderer = Renderer()
world_manager = WorldManager()

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
    player = Player(str(player_name), 1, 1, 100, Position(0, 0, 0))
    player.spawn(world)
    return {"status": "success", "message": "Player successfully created"}


@app.route('/render_player')
def render_map():
    print(request.args.get("id"))
    return 'Hello World!'


def start():
    new_world = world_manager.generate_main_world(10, 10)
    player = Player("Zemlia", 1, 1, 100, Position(0, 0, 0))
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
