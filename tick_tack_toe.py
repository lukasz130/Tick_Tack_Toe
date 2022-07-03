board = [
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

board = [list(row) for row in board]

#      |     |      0
#      |     |      1
# _____|_____|______2
#      |     |      3
#      |     |      4
# _____|_____|______5
#      |     |      6
#      |     |      7
#      |     |      8
# 0123456789ABCDEFGH

position_set = []
number_of_row_ones = 0
number_of_row_twos = 0
number_of_row_threes = 0
number_of_column_ones = 0
number_of_column_twos = 0
number_of_column_threes = 0

def choose_sign():
    while True:
        player_input = input('Choose (N)oughs or (C)rosses: ')
        if player_input == 'N':
            player_sign = '0'
            ai_sign = 'X'
            print('Noughts chosen "0"')
            return player_sign, ai_sign
        elif player_input == 'C':
            player_sign = 'X'
            ai_sign = '0'
            print('Crosses chosen "X"')
            return player_sign, ai_sign
        else:
            print('Only (N)ouths or (C)rosses can be chosen. Try again!')


def draw_board():
    for row in board:
        for item in row:
            print(item, end='')
        print()


def get_position():
    while True:
        position_x, position_y = input('Choose position X and Y').split()
        position_x = int(position_x)
        position_y = int(position_y)
        if (position_x, position_y) not in position_set:
            if position_x <= 3 and position_y <= 3 and position_x > 0 and position_y > 0:
                position_set.append((position_x, position_y))
                return position_x, position_y
            print('Wrong positions, choose between 1 and 3.')
        else:
            print('This position was chosen earlier. Choose free position.')


def draw_sign(position_x, position_y, sign):
    position_x_dict = {1: 1, 2: 4, 3: 7}
    position_y_dict = {1: 2, 2: 8, 3: 14}
    board[position_x_dict[position_x]][position_y_dict[position_y]] = sign


def check_win_case(position_x, position_y):
    global number_of_row_ones, \
        number_of_row_twos, \
        number_of_row_threes, \
        number_of_column_ones, \
        number_of_column_twos, \
        number_of_column_threes

    if len(position_set) >= 3:
        if position_x == 1:
            number_of_row_ones += 1
        elif position_x == 2:
            number_of_row_twos += 1
        elif position_x == 3:
            number_of_row_threes += 1

        if position_y == 1:
            number_of_column_ones += 1
        elif position_x == 2:
            number_of_column_twos += 1
        elif position_x == 3:
            number_of_column_threes += 1



        if max(number_of_row_ones, number_of_row_twos, number_of_row_threes,
               number_of_column_ones, number_of_column_twos, number_of_column_threes) == 3:
            return True

        #TODO Complete win statement. Add diagonal win cases
        #TODO Check how to write win statement. How to apply sign (win or loose).

    return False


def main():
    player_sign, ai_sign = choose_sign()
    draw_board()
    position_x, position_y = get_position()
    draw_sign(position_x, position_y, player_sign)
    draw_board()
    position_x, position_y = get_position()
    draw_sign(position_x, position_y, player_sign)
    draw_board()


if __name__ == '__main__':
    main()
    # draw_board()


