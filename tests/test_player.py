import unittest

from snake_ladders.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player(1)

    def test_get_name(self):
        self.assertEqual(self.player.get_name(), f'player1')

    def test_get_position(self):
        self.assertEqual(self.player.get_pos(), 1)

    def test_get_player_num(self):
        self.assertEqual(self.player.get_player_num(), 1)

    def test_update_position(self):
        old_pos = self.player.get_pos()
        self.player.update_position(7)
        new_pos = self.player.get_pos()
        self.assertNotEqual(old_pos, new_pos)
        self.assertEqual(new_pos, 7)
