from flask import Flask
import pymongo

from GameObjects.MapObjects.Void import Void
from GameObjects.Player import Player
from GameObjects.World import World
from GameObjects.WorldObject import WorldObject
from Position import Position
from Renderer import Renderer

app = Flask(__name__)

worlds = []


@app.route('/')
def hello_world():
    return 'Hello World!'


def start():
    new_world = generate_world(10, 10)
    renderer_result = Renderer().render_by_symbols(new_world)
    print(renderer_result)
    app.run()


def generate_world(width, height):
    world = World(width, height)
    for i in range(0, height):
        newColumn = []
        for j in range(0, width):
            position = Position(i, j, 0)
            newColumn.append([WorldObject(position, "void", "#", False, "void", Void(position))])
        world.mapObjects.append(newColumn)
    worlds.append(world)
    return world


if __name__ == '__main__':
    start()
