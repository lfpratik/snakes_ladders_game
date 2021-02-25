import unittest

from snake_ladders.dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()
        self.roll_values = [1, 2, 3, 4, 5, 6]

    def test_dice_face(self):
        self.assertEqual(self.dice._DICE_FACE, 6)

    def test_roll_crooked_dice(self):
        self.assertIn(self.dice._roll_crooked_dice(), self.roll_values)

    def test_roll_normal_dice(self):
        self.assertIn(self.dice._roll_normal_dice(), self.roll_values)

    def test_get_crooked_dice_value(self):
        crooked_dice_value = self.dice.get_dice_value(crooked=True)
        self.assertIn(crooked_dice_value, self.roll_values)

    def test_get_normal_dice_value(self):
        normal_dice_value = self.dice.get_dice_value(crooked=False)
        self.assertIn(normal_dice_value, self.roll_values)
