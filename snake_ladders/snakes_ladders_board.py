import random
import sys
import time

from snake_ladders.dice import Dice
from snake_ladders.player import Player

SLEEP_BETWEEN_ACTIONS = 1


# Snakes and Ladder Board class

class SnakesLaddersBoard:
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

    _PLAYER_TURN_TEXT = [
        'Your turn.',
        'Go.',
        'Please proceed.',
        'Lets win this.',
        'Are you ready?',
        ''
    ]

    def __init__(self):
        self.player_lst = []

    @staticmethod
    def welcome():
        msg = """
            Welcome to Snake and Ladder Game.

            Rules:
                1.  Initially both the players are at starting position i.e. 1.
                    Take it in turns to roll the dice.
                    Move forward the number of spaces shown on the dice.
                2.  If you lands at the bottom of a ladder,
                    you can move up to the top of the ladder.
                3.  If you lands on the head of a snake,
                    you must slide down to the bottom of the snake.
                4.  Hit enter to roll the dice.
        """
        print(msg)

    @staticmethod
    def show_bite_state(name, old_pos, current_pos):
        print(f'{name} got a snake bite. '
              f'Going down from {old_pos} to {current_pos}')

    @staticmethod
    def show_jump_state(name, old_pos, current_pos):
        print(f'{name} climbed the ladder '
              f'from {old_pos} to {current_pos}')

    @staticmethod
    def show_moving_state(name, old_pos, current_pos):
        print(f'{name} moving.... '
              f'from {old_pos} to {current_pos} position')

    @staticmethod
    def get_position(position, _from):
        return _from.get(position)

    def set_profile(self, pro_mode=False):
        self._PRO_MODE = pro_mode

    def _get_players(self, no_players):
        player_name = None
        for i in range(0, no_players):
            if self._PRO_MODE:
                player_name = input('Enter player name: ')
            player_instance = Player(player_num=(i + 1),
                                     player_name=player_name)
            self.player_lst.append(player_instance)

    def _check_snake_bite(self, position):
        return position in self._SNAKES

    def _check_ladder_jump(self, position):
        return position in self._LADDERS

    def _check_win(self, current_pos):
        return self._MAX_WIN_VAL == current_pos

    def _next_step(self, player, dice_value):

        time.sleep(SLEEP_BETWEEN_ACTIONS)
        name = player.get_name()
        old_pos = player.get_pos()
        current_pos = player.get_pos() + dice_value

        if self._MAX_WIN_VAL < current_pos:
            print(f'You need {str(self._MAX_WIN_VAL - old_pos)} '
                  f'to win this game. Keep trying.')
            return old_pos
        elif self._check_snake_bite(current_pos):
            new_pos = self.get_position(current_pos, self._SNAKES)
            self.show_moving_state(name, old_pos, current_pos)
            self.show_bite_state(name, current_pos, new_pos)
            return new_pos
        elif self._check_ladder_jump(current_pos):
            new_pos = self.get_position(current_pos, self._LADDERS)
            self.show_moving_state(name, old_pos, current_pos)
            self.show_jump_state(name, current_pos, new_pos)
            return new_pos
        else:
            self.show_moving_state(name, old_pos, current_pos)
            return current_pos

    def show_winners(self):
        print('\n')
        print('*'*79)
        self.player_lst.sort(key=lambda x: x._pos, reverse=True)
        print('Winner is')
        for idx, player in enumerate(self.player_lst, start=1):
            print(f'{idx}: {player.get_name()} current position {player.get_pos()}')
        print('*'*79)
        print('\n')

    def play_demo_mode(self):
        dice = Dice()
        for i in range(1, self._TURN_VAL+1):
            print('\n')
            print('-' * 79)
            print(f'Round: {i}')
            print('-' * 79)
            for player in self.player_lst:
                crooked = (player.get_pos() != 1)
                time.sleep(SLEEP_BETWEEN_ACTIONS)
                print(f'{player.get_name()} : '
                      f'{random.choice(self._PLAYER_TURN_TEXT)} '
                      f'Hit the enter to roll dice: ')
                print("Rolling dice...")
                dice_value = dice.get_dice_value(crooked)
                time.sleep(SLEEP_BETWEEN_ACTIONS)
                pos = self._next_step(player, dice_value)
                player.update_position(pos)
                winner = self._check_win(current_pos=player.get_pos())
                if winner:
                    self.show_winners()
                    sys.exit(1)
        self.show_winners()

    def play_pro_mode(self):
        dice = Dice()
        cnt = 1
        while True:
            print('\n')
            print('-' * 79)
            print(f'Round: {cnt}')
            print('-' * 79)
            for player in self.player_lst:
                time.sleep(SLEEP_BETWEEN_ACTIONS)
                input(f'{player.get_name()} : '
                      f'{random.choice(self._PLAYER_TURN_TEXT)} '
                      f'Hit the enter to roll dice: ')
                print("Rolling dice...")
                dice_value = dice.get_dice_value()
                time.sleep(SLEEP_BETWEEN_ACTIONS)
                pos = self._next_step(player, dice_value)
                player.update_position(pos)
                winner = self._check_win(current_pos=player.get_pos())
                if winner:
                    self.show_winners()
                    sys.exit(1)
            cnt += 1

    def start(self):
        self.welcome()
        time.sleep(SLEEP_BETWEEN_ACTIONS)

        num_players = 1
        if self._PRO_MODE:
            num_players = int(input('Enter number of players: '))

        self._get_players(num_players)
        self.play_pro_mode() if self._PRO_MODE else self.play_demo_mode()
