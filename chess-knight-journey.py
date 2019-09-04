# 08/15/2019 ATOM
import sys
"""Finds path for moving kNight piece on empty chess board by visiting each square once"""
#
def init():
    """Initialization"""
    global rows, cols, num_squares, move_range, board, path_square_cnt, move_seq, moves, board_matrix, comb_cnt
    # cols = ('a', 'b', 'c', 'd', 'e')
    # rows = (1, 2, 3, 4, 5)
    # for a smaller 5-by-5 board size uncomment the two lines above and comment the two lines below
    cols = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    rows = (1, 2, 3, 4, 5, 6, 7, 8)
    # maximum of 8 moves possible from the center c3-c6-f6-f3 quadrant squares only
    moves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
    num_squares = len(rows) * len(cols)
    move_range = range(0,len(rows))
    board = [a+str(n) for a in cols for n in rows]
    board_matrix = [[0 for x in range(len(rows))] for y in range(len(cols))]  # keeps track of visited squares on a given path
    move_seq = list()                                                         # sequential move list of a given path
    comb_cnt = 0                                                              # possible full path combinations count
#
def prompt_for_start_square():
    """Prompts for start square"""
    start_square = ''
    while start_square == '':
        start_square = input("Enter starting square on the board (i.e. c3, e2, b5, etc.), or X/x to exit: ")
        if start_square.upper() == 'X':
            break
        if start_square not in board:
            start_square = ''
            print("Invalid square entered. Should be in (" + board[0] + " ... " + board[-1] + ") range. Try again.")
        else:
            print("You have chosen to start from square", start_square)
    return start_square
#
def print_out():
    """Prints output"""
    # print move sequence
    print(comb_cnt,"-->",move_seq)
    print()
    # print as a grid
    for y in range(len(rows), 0, -1):
        # print row numbers in reverse order
        sys.stdout.write(str(rows[y-1]) + '  ')
        for x in range(len(cols)):
            sys.stdout.write("{0:>2s}".format(str(board_matrix[x][y-1])) + ' ')
        sys.stdout.write('\n')
    sys.stdout.write('\n   ')
    # print 1-char column labels
    for x in range(len(cols)):
        sys.stdout.write("{0:>2s}".format(cols[x]) + ' ')
    sys.stdout.write('\n\n')
#
def moveknight(board_matrix, square, path_square_cnt):
    """Main knight movement function"""
    global comb_cnt
    move_seq.append(square)
    c, r = square[0], int(square[1])
    x, y = cols.index(c), rows.index(r)
    # mark the square as visited with the current path square count
    board_matrix[x][y] = path_square_cnt
    if path_square_cnt == num_squares:
        comb_cnt += 1
        print_out()
        # path complete - unmark the last square as visited
        board_matrix[x][y] = 0
        move_seq.pop()
        return
    c, r = cols.index(c), rows.index(r)
    for dc, dr in moves:
        nextc, nextr = (c + dc), (r + dr)
        # determine next square on the path
        if nextc in move_range and nextr in move_range:
            next_square = cols[nextc] + str(rows[nextr])
            if board_matrix[nextc][nextr] == 0:
                # recursion keeps tack of each path
                moveknight(board_matrix, next_square, path_square_cnt + 1)
    # unmark the last square as visited
    board_matrix[x][y] = 0
    move_seq.pop()
#
def main():
    """Entry point of the program"""
    init()
    square = prompt_for_start_square()
    if square.upper() == 'X':
        return
    path_square_cnt = 1
    moveknight(board_matrix, square, path_square_cnt)
    print("Total number of path combinations from " + square + ":", comb_cnt)
#
if __name__ == '__main__':
    main()
