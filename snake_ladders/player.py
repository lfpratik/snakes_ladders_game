# Player class

class Player:

    def __init__(self, player_num, player_name=None):
        self._pos = 1
        self._num = player_num
        self._name = f'player{player_num}'
        if player_name:
            self._name = player_name

    def get_pos(self):
        return self._pos

    def get_name(self):
        return self._name

    def get_player_num(self):
        return self._num

    def update_position(self, position):
        self._pos = position
