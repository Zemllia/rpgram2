from pymongo import MongoClient

from GameObjects.Player import Player
from Position import Position


class PlayerManager:
    players = []
    client = MongoClient('127.0.0.1', 27017)
    db = client.rpgram2

    RESTRICTED_SYMBOLS = ["\"", "0", ".", "🌲", "@", "/", "fuck", "suck", "shit", "admin", "rpgram", "buy", "sell",
                          "drugs", "блять", "сука", "уебок", "урод", "продаю", "продам", "отдам", "куплю", "покупаю",
                          "наркотики", "детское", "порно", "цп", " cp ", "child", "porn", " прон ", "скупаю",
                          "нарко", "соли", "специи", "спайс", "спиды", "пудра"]

    # todo Подгрузка игрока, если существует
    def create_or_load_player(self, name, password, world):
        auth_result = self.auth_player(name, password)
        if auth_result.get("status") == "success":
            player = auth_result.get("player")
            player.spawn(world)
            self.players.append(player)
        return auth_result

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

    def auth_player(self, nickname, password):
        users = self.db.users
        check_user = users.find_one({"nickname": str(nickname)})
        if check_user is not None:
            if check_user.get("password") == password:
                player_pos = Position(check_user.get("position").get("x"),
                                      check_user.get("position").get("y"),
                                      check_user.get("position").get("z"))

                loaded_player = Player(check_user.get("id"), nickname,
                                       check_user.get("level"), check_user.get("xp"), check_user.get("hp"), player_pos,
                                       check_user.get("fov"))
                return {"status": "success", "player": loaded_player, "error": None}
            else:
                return {"status": "error", "player": None, "error": "worng_auth_data"}
        for item in self.RESTRICTED_SYMBOLS:
            if item.lower() in str(nickname).lower():
                return {"status": "error", "player": None, "error": "nickname_restricted"}

        all_users = users.find({})

        max_id = -1
        for cur_user in all_users:
            if int(cur_user.get("id")) > max_id:
                max_id = int(cur_user.get("id"))

        new_user = {
            "id": max_id + 1,
            "nickname": nickname,
            "password": password,
            "level": 1,
            "hp": 100,
            "xp": 0,
            "position": {
                "x": 0,
                "y": 0,
                "z": 0
            },
            "fov": 5
        }

        users.insert_one(new_user)

        player_pos = Position(new_user.get("position").get("x"), new_user.get("position").get("y"),
                              new_user.get("position").get("z"))
        new_player = Player(new_user.get("id"), nickname,
                            new_user.get("level"), new_user.get("xp"), new_user.get("hp"), player_pos,
                            new_user.get("fov"))

        return {"status": "success", "player": new_player, "error": None}
