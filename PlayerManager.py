from GameObjects.Player import Player
from Position import Position


class PlayerManager:
    players = []

    # todo Подгрузка игрока, если существует
    def create_or_load_player(self, name, world):
        max_id = -1
        for item in self.players:
            if item.player_id > max_id:
                max_id = item.player_id
        player = Player(max_id + 1, name, 1, 1, 100, Position(0, 0, 0), 5)
        player.spawn(world)
        self.players.append(player)
        return player

    def get_player_by_id(self, player_id):
        for item in self.players:
            if item.player_id == int(player_id):
                return item
        return None

    def get_player_by_name(self, name):
        for item in self.players:
            if item.nickname == name:
                return item
        return None
