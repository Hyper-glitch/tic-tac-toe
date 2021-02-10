from abc import ABC, abstractmethod
import random
import time


class Player(ABC):
    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class
        self.list_of_moves = []

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(Player):
    def __init__(self, name, symbol_class):
        super().__init__(name, symbol_class)

    @property
    def name(self):
        return self._name

    @property
    def symbol_class(self):
        return self._symbol_class

    def move(self):
        symbol = self._symbol_class.__name__

        flag = True
        while flag:
            loc = input(f"{self.name} Where to put {symbol}? ")
            loc_x = int(loc.split(",")[0])
            loc_y = int(loc.split(",")[1])
            move = (loc_x, loc_y)
            if HumanPlayer.valid_move(move) and move not in self.list_of_moves:
                flag = False
        self.list_of_moves.append(move)
        return self._symbol_class(loc_x, loc_y)

    @staticmethod
    def valid_move(x):
        if (x[0] >= 0) and (x[0] <= 2) and (x[1] >= 0) and (x[1] <= 2):
            return True
        else:
            print("The specified values must be in the range (0, 2)")
        return False

    def __str__(self):
        return f"Human{self._name} playing {self._symbol_class.__name__}"


class RoboticPlayer(Player):
    def __init__(self, name, symbol_class):
        super().__init__(name, symbol_class)

    @property
    def name(self):
        return self._name

    def move(self):
        symbol = self._symbol_class.__name__
        flag = True
        time.sleep(3)
        print(f"Robot {self.name} is thinking to move")
        while flag:
            loc_x = random.randint(0, 2)
            loc_y = random.randint(0, 2)
            move = (loc_x, loc_y)
            if HumanPlayer.valid_move(move) and move not in self.list_of_moves:
                flag = False
        self.list_of_moves.append(move)
        return self._symbol_class(loc_x, loc_y)
