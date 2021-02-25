import sys

from snake_ladders.snakes_ladders_board import SnakesLaddersBoard


if __name__ == '__main__':
    pro_mode = False
    if len(sys.argv) > 1 and 'pro' in sys.argv[1]:
        pro_mode = True

    game = SnakesLaddersBoard()
    game.set_profile(profile_mode=pro_mode)
    game.start()
