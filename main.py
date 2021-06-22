from flask import Flask, request

from GameObjects.Player import Player
from Position import Position
from Renderer import Renderer
from WorldManager import WorldManager

app = Flask(__name__)

renderer = Renderer()
world_manager = WorldManager()

players = []


@app.route('/render_map')
def render_map():
    print(request.args)
    return 'Hello World!'


def start():
    new_world = world_manager.generate_world(10, 10)
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
