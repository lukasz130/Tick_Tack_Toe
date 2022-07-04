import os


# TODO: Add AI Algorithm
class TickTackToe:

    def __init__(self):
        self.board = [
            '     |     |      ',
            '     |     |      ',
            '_____|_____|______',
            '     |     |      ',
            '     |     |      ',
            '_____|_____|______',
            '     |     |      ',
            '     |     |      ',
            '     |     |      '
        ]
        self.board = [list(row) for row in self.board]

        # Table of sings on specific positions
        self.board_signs = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.row = None
        self.column = None

        self.player_sign = None
        self.ai_sign = None

    def choose_sign(self):
        os.system('clear')
        print('Tick-Tack-Toe Game:')
        print('-------------------')
        while True:
            player_input = input('Choose (N)oughs or (C)rosses: ')
            if player_input == 'N':
                self.player_sign = '0'
                self.ai_sign = 'X'
                print('Noughts chosen "0"')
                return
            elif player_input == 'C':
                self.player_sign = 'X'
                self.ai_sign = '0'
                print('Crosses chosen "X"')
                return
            else:
                print('Only (N)ougths or (C)rosses can be chosen. Try again!')

    def draw_board(self):
        os.system('clear')
        for row in self.board:
            for item in row:
                print(item, end='')
            print()

    def draw_sign(self, sign):
        # TODO: Implement clear console for OSes different than Linux.
        os.system('clear')
        position_x_dict = {0: 1, 1: 4, 2: 7}
        position_y_dict = {0: 2, 1: 8, 2: 14}
        self.board[position_x_dict[self.row]][position_y_dict[self.column]] = sign
        self.draw_board()

    def player_set_sign(self):
        while True:
            row, column = input('Choose row and column').split()
            self.row = int(row) - 1
            self.column = int(column) - 1
            if self.row < 0 or self.column < 0 or self.row > 2 or self.column > 2:
                print('Wrong positions, choose between 1 and 3.')
                continue

            if self.board_signs[self.row][self.column] is None:
                self.board_signs[self.row][self.column] = self.player_sign
                break
            else:
                print('This position was chosen earlier. Choose free position.')

        self.draw_sign(self.player_sign)

    def ai_set_sign(self):
        self.row, self.column = self._find_best_move()
        self.board_signs[self.row][self.column] = self.ai_sign
        self.draw_sign(self.ai_sign)

    def check_end_of_game_case(self, sign):
        result_text = 'You win!' if sign == self.player_sign else 'You Loose!'
        for row in self.board_signs:
            if all(map(lambda x: x == sign, row)):
                print(result_text)
                return True

        # TODO: Refactor without transposing matrix (nested lists)
        rows = len(self.board_signs)
        columns = len(self.board_signs[0])
        board_signs_transpose = []
        for j in range(columns):
            row = []
            for i in range(rows):
                row.append(self.board_signs[i][j])
            board_signs_transpose.append(row)
        for row in board_signs_transpose:
            if all(map(lambda x: x == sign, row)):
                print(result_text)
                return True

        if self.board_signs[1][1] == sign:
            if self.board_signs[0][0] == sign and self.board_signs[2][2] == sign or \
                    self.board_signs[0][2] == sign and self.board_signs[2][0] == sign:
                print(result_text)
                return True

        if not self.is_move_left():
            print('There is a draw!')
            return True

        return False

    def is_move_left(self):
        for row in self.board_signs:
            for item in row:
                if item is None:
                    return True
        return False

    def calculate_cost(self):
        for row in self.board_signs:
            if all(map(lambda x: x == self.ai_sign, row)):
                return 10
            elif all(map(lambda x: x == self.player_sign, row)):
                return -10

        for col in range(3):
            if self.board_signs[0][col] == self.board_signs[1][col] and \
                    self.board_signs[1][col] == self.board_signs[2][col]:
                if self.board_signs[0][col] == self.ai_sign:
                    return 10
                elif self.board_signs[0][col] == self.player_sign:
                    return -10

        if self.board_signs[0][0] == self.board_signs[1][1] and self.board_signs[1][1] == self.board_signs[2][2] or \
                self.board_signs[2][0] == self.board_signs[1][1] and self.board_signs[1][1] == self.board_signs[0][2]:
            if self.board_signs[1][1] == self.ai_sign:
                return 10
            elif self.board_signs[1][1] == self.player_sign:
                return -10

        return 0

    def minimax(self, depth, is_max):
        # board = self.board
        score = self.calculate_cost()
        if score == 10 or score == -10:
            return score
        if not self.is_move_left():
            return 0
        if is_max:
            best = -1000
            for row in range(len(self.board_signs)):
                for column in range(len(self.board_signs[0])):
                    if self.board_signs[row][column] is None:
                        self.board_signs[row][column] = self.ai_sign
                        best = max(best, self.minimax(depth + 1, not is_max))
                        self.board_signs[row][column] = None
            return best
        else:
            best = 1000
            for row in range(len(self.board_signs)):
                for column in range(len(self.board_signs[0])):
                    if self.board_signs[row][column] is None:
                        self.board_signs[row][column] = self.player_sign
                        best = min(best, self.minimax(depth + 1, not is_max))
                        self.board_signs[row][column] = None
            return best

    def _find_best_move(self):
        best_val = -1000
        best_move = (-1, -1)
        for row in range(len(self.board_signs)):
            for column in range(len(self.board_signs[0])):
                if self.board_signs[row][column] is None:
                    self.board_signs[row][column] = self.ai_sign
                    move_val = self.minimax(0, False)
                    self.board_signs[row][column] = None
                    if move_val > best_val:
                        best_move = (row, column)
                        best_val = move_val
        # print(f'The value of the best move is : {best_val}')
        print(f'The best move is: {best_move}')
        return best_move


def main():
    tick_tack_toe = TickTackToe()
    tick_tack_toe.choose_sign()
    tick_tack_toe.draw_board()

    result = False
    player_flag = 'player'
    while not result:
        if player_flag == 'player':
            tick_tack_toe.player_set_sign()
            result = tick_tack_toe.check_end_of_game_case(tick_tack_toe.player_sign)
            player_flag = 'ai'
        else:
            # tick_tack_toe.find_best_move()
            tick_tack_toe.ai_set_sign()
            result = tick_tack_toe.check_end_of_game_case(tick_tack_toe.ai_sign)
            player_flag = 'player'


if __name__ == '__main__':
    main()
