from tictactoe.game import Game
from tictactoe.player import HumanPlayer, RoboticPlayer
from tictactoe.board import X, O
import random


def choice():
    while True:
        choice_value = int(input("Enter your choice "))
        if choice_value == -1:
            return -1
        try:
            if choice_value < 1 or choice_value > 5:
                raise Exception("Allowing range is between 1 to 4, for exist -1")
        except Exception:
            print("Allowing range is between 1 to 4, for exist -1")
        else:
            return choice_value


def define_symbol_class():
    symbol_random = random.choice([X, O])
    if symbol_random == X:
        return X, O
    return O, X


def main():
    player_first = ""
    player_second = ""
    print("Menu".center(32, ' '))
    print("1. Check rules of the game" + "\n" + "2. Human VS Human" + "\n" +
          "3. Human VS Robot" + "\n" + "4. Robot VS Robot" + "\n" +
          "5. To exist the game push the '5' ")
    while True:
        your_choice = choice()
        if your_choice == 1:
            with open("rules_of_the_game.txt", "r", encoding='utf-8') as f:
                rules_of_the_game = f.read()
                print(rules_of_the_game)
                return main()
        elif your_choice == 2:
            player_first, player_second = main_human()
        elif your_choice == 3:
            player_first, player_second = main_robot_human()
        elif your_choice == 4:
            player_first, player_second = main_robots()
        elif your_choice == 5:
            return 0
        game = Game(player_one=player_first, player_two=player_second)
        game.run()


def main_human():
    class_symbol_first, class_symbol_second = define_symbol_class()
    player_first = HumanPlayer(name=input("Enter the first player name "), symbol_class=class_symbol_first)
    player_second = HumanPlayer(name=input("Enter the second player name "), symbol_class=class_symbol_second)
    print(f"The first player {player_first.name} is gaming with {class_symbol_first.__name__}")
    print(f"The second player {player_second.name} is gaming with {class_symbol_second.__name__}")
    return player_first, player_second


def main_robots():
    class_symbol_first, class_symbol_second = define_symbol_class()
    player_first = RoboticPlayer(symbol_class=class_symbol_first)
    player_second = RoboticPlayer(symbol_class=class_symbol_second)
    print(f"The first player {player_first.name} is gaming with {class_symbol_first.__name__}")
    print(f"The second player {player_second.name} is gaming with {class_symbol_second.__name__}")
    return player_first, player_second


def main_robot_human():
    class_symbol_first, class_symbol_second = define_symbol_class()
    player_first = HumanPlayer(name=input("Enter the first player name "), symbol_class=class_symbol_first)
    player_second = RoboticPlayer(name=random.choice(["R2D2", "Robot", "Robocop"]), symbol_class=class_symbol_second)
    return player_first, player_second


if __name__ == '__main__':
    main()
