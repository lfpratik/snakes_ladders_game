import random


# Dice class

class Dice:

    _DICE_FACE = 6

    def _roll_normal_dice(self):
        dice_value = random.randint(1, self._DICE_FACE)
        print(f'Its a {dice_value}')
        return dice_value

    @staticmethod
    def _roll_crooked_dice():
        dice_value = random.choice([2, 4, 6])
        print(f'Its a {dice_value}')
        return dice_value

    def get_dice_value(self, crooked=False):
        if crooked:
            return self._roll_crooked_dice()
        return self._roll_normal_dice()
