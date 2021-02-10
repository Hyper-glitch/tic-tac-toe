from tictactoe.board import Board


class Game:
    def __init__(self, player_one, player_two):
        self._board = Board()
        self._player_one = player_one
        self._player_two = player_two

    @property
    def player_one(self):
        return self._player_one

    @property
    def player_two(self):
        return self._player_two

    def run(self):
        player_one = self._player_one
        player_two = self._player_two
        flag = 0
        game = self._board
        while True:
            while True:
                if self.check_progress(player=player_one):
                    break
            print(game)
            if self.check_win():
                print(f"The game is over! The winner is {self._player_one.name}")
                break

            if not self.check_draw():
                print("It's draw game bro!")
                break

            while True:
                if self.check_progress(player=player_two):
                    break
            print(game)
            if self.check_win():
                print(f"The game is over! The winner is {self._player_two.name}")
                break

    def validator_move(self, player):
        player = player.move
        if self._board[player.x][player.y] == "X" or \
                self._board[player.x][player.y] == "O":
            return False
        return True

    def check_win(self):

        line1 = self._board.board[0][0] == self._board.board[0][1] == self._board.board[0][2] == "X" or \
                self._board.board[0][0] == self._board.board[0][1] == self._board.board[0][2] == "O"
        line2 = self._board.board[1][0] == self._board.board[1][1] == self._board.board[1][2] == "X" or \
                self._board.board[1][0] == self._board.board[1][1] == self._board.board[1][2] == "O"
        line3 = self._board.board[2][0] == self._board.board[2][1] == self._board.board[2][2] == "X" or \
                self._board.board[2][0] == self._board.board[2][1] == self._board.board[2][2] == "O"
        columns1 = self._board.board[0][0] == self._board.board[1][0] == self._board.board[2][0] == "X" or \
                   self._board.board[0][0] == self._board.board[1][0] == self._board.board[2][0] == "O"
        columns2 = self._board.board[0][1] == self._board.board[1][1] == self._board.board[2][1] == "X" or \
                   self._board.board[0][1] == self._board.board[1][1] == self._board.board[2][1] == "O"
        columns3 = self._board.board[0][2] == self._board.board[1][2] == self._board.board[2][2] == "X" or \
                   self._board.board[0][2] == self._board.board[1][2] == self._board.board[2][2] == "O"
        main_diagonal = self._board.board[0][0] == self._board.board[1][1] == self._board.board[2][2] == "X" or \
                        self._board.board[0][0] == self._board.board[1][1] == self._board.board[2][2] == "O"
        side_diagonal = self._board.board[0][2] == self._board.board[1][1] == self._board.board[2][0] == "X" or \
                        self._board.board[0][2] == self._board.board[1][1] == self._board.board[2][0] == "O"

        win_combinations = [
            line1, line2, line3,
            columns1, columns2, columns3,
            main_diagonal, side_diagonal]

        for win in win_combinations:
            if win:
                return win
        return False

    def check_progress(self, player):
        counter = player.move()
        if self._board.valid_board(val=counter):
            self._board.board = counter
            return True
        return False

    def check_draw(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.board[i][j] == ' ':
                    return True
        return False
