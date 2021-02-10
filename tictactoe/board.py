class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class X(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "X"


class O(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "O"


class Board:
    def __init__(self):
        self._board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, val):
        self._board[val.x][val.y] = str(val)

    def __str__(self):
        board_str = ""
        for line in self._board:
            board_str += "|" + "|".join(line) + "|\n"
        return board_str

    def valid_board(self, val):
        value = self._board[val.x][val.y]
        if value == "X" or value == "O":
            return False
        return True
