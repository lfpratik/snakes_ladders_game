import unittest

from snake_ladders.snakes_ladders_board import SnakesLaddersBoard
from snake_ladders.player import Player


# default board size
_MAX_WIN_VAL = 100

# default turns
_PRO_MODE = False
_TURN_VAL = 10

# snake takes you down from 'key' to 'value'
_SNAKES = {
    14: 7,
    29: 10,
    36: 2,
    39: 5,
    50: 47,
    56: 36,
    59: 21,
    73: 53,
    78: 65,
    90: 13,
    95: 66,
    97: 84
}

# ladder takes you up from 'key' to 'value'
_LADDERS = {
    3: 22,
    15: 27,
    18: 24,
    24: 38,
    25: 35,
    34: 48,
    42: 60,
    44: 63,
    51: 72,
    54: 68,
    64: 76,
    67: 75,
    77: 96,
    80: 99,
    88: 92
}


class TestSnakesLaddersBoard(unittest.TestCase):

    def setUp(self):
        self.game = SnakesLaddersBoard()

    def test_snakes_ladders_board_static_data(self):
        self.assertEqual(self.game.player_lst, [])
        self.assertEqual(self.game._MAX_WIN_VAL, _MAX_WIN_VAL)
        self.assertEqual(self.game._PRO_MODE, _PRO_MODE)
        self.assertEqual(self.game._TURN_VAL, _TURN_VAL)
        self.assertEqual(self.game._SNAKES, _SNAKES)
        self.assertEqual(self.game._LADDERS, _LADDERS)

    def test_set_profile(self):
        self.assertFalse(self.game._PRO_MODE)
        self.game.set_profile(pro_mode=True)
        self.assertTrue(self.game._PRO_MODE)

    def test_get_player(self):
        self.assertEqual(len(self.game.player_lst), 0)
        self.game._get_players(4)
        self.assertEqual(len(self.game.player_lst), 4)

    def test_check_snake_bite(self):
        self.assertFalse(self.game._check_snake_bite(7))
        self.assertTrue(self.game._check_snake_bite(14))

    def test_check_ladder_jump(self):
        self.assertFalse(self.game._check_ladder_jump(8))
        self.assertTrue(self.game._check_ladder_jump(51))

    def test_check_win(self):
        self.assertFalse(self.game._check_win(90))
        self.assertTrue(self.game._check_win(100))

    def test_next_step(self):
        for (player_pos, dice_value, result) in [(1, 3, 4),
                                                 (8, 6, 7),
                                                 (8, 7, 27)]:
            player = Player(1)
            player.update_position(player_pos)
            self.assertEqual(self.game._next_step(player, dice_value), result)
