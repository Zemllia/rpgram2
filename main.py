import json
import time
from threading import Thread

from flask import Flask, request

import Config
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


@app.route('/get_legend')
def get_legend():
    answer = {"status": "success", "message": world_manager.world_legend}
    return answer


@app.route('/auth_player', methods=['POST'])
def spawn_player():
    request_data = json.loads(request.data)
    world_id = request_data.get("world_id")
    world = world_manager.get_world_by_id(int(world_id))
    player_name = request_data.get("name")
    password = request_data.get("password")
    player_auth_result = player_manager.create_or_load_player(player_name, password, world)
    if player_auth_result.get("status") == "success":
        player = player_auth_result.get("player")
        return {"status": "success", "message": {"player_id": player.player_id}}
    else:
        error_message = player_auth_result.get("error")
        return {"status": "error", "message": error_message}


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
    print(request.args)
    player = player_manager.get_player_by_id(int(cur_player_id))
    world = world_manager.get_world_by_id(int(0))
    result = player.move(world, move_side)
    return {"status": "success", "message": result}


def start():
    world_manager.generate_main_world(10, 10)
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)


def auto_save():
    print("i'm alive")
    time.sleep(30)


if __name__ == '__main__':
    start()
