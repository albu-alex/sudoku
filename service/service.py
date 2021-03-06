

class Service:
    def __init__(self, sudoku_board):
        self._sudokuBoard = sudoku_board
        self._sudokuBoard.place_numbers()

    def place_new_value(self, row_in_string, column_in_string, value_in_string):
        row = int(row_in_string)
        column = int(column_in_string)
        value = int(value_in_string)
        return self._sudokuBoard.player_input(row, column, value)

    def get_board(self):
        return self._sudokuBoard.get_board()

    def display_board(self):
        self._sudokuBoard.display_board()

    def is_game_over(self):
        board = self.get_board()
        for row in range(len(board)):
            for column in range(len(board)):
                if self._sudokuBoard.is_square_empty(row, column):
                    return False
        return True
