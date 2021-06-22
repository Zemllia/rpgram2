from flask import Flask
from Renderer import Renderer
from WorldManager import WorldManager

app = Flask(__name__)

world_manager = WorldManager()

players = []


@app.route('/')
def hello_world():
    return 'Hello World!'


def start():
    new_world = world_manager.generate_world(10, 10)
    renderer_result = Renderer().render_by_symbols(new_world)
    print(renderer_result)
    app.run()


if __name__ == '__main__':
    start()
