import random
import time

def initialize_board_6x6(): 
    row0 = [1,2,3,4,5,6]
    random.shuffle(row0)
    row1 = row0[3:6] + row0[0:3]
    row2 = [row0[2]] + row0[0:2] + [row0[5]] + row0[3:5]
    row3 = row2[3:6] + row2[0:3]
    row4 = [row0[1],row0[2],row0[0],row0[4],row0[5],row0[3]]
    row5 = row4[3:6] + row4[0:3]
    return [row0, row1, row2, row3, row4, row5]

def shuffle_ribbons(board):
    top = board[:2]
    mid = board[2:4]
    bottom = board[4:]
    random.shuffle(top)
    random.shuffle(mid)
    random.shuffle(bottom)
    return top + mid + bottom

def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

def create_solution_board_6x6():
    board = initialize_board_6x6()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Hello. This is a time attack sudoku.")
    print("Enter your level.")
    print("Time Limit | Beginner: 60s, Intermediate: 80s , Advanced: 100s")
    level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    if level == "1":
        return 10
    elif level == "2":
        return 15
    else:
        return 20
    
def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,5)
        j = random.randint(0,5)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1  
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

def get_integer(message, i ,j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)

def sudoku_6x6_TA():
    solution_board = create_solution_board_6x6()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    if no_of_holes == 10:
        time_limits = 60
    elif no_of_holes == 15:
        time_limits = 80
    else:
        time_limits = 100
    show_board(puzzle_board)
    start = time.time()
    while no_of_holes > 0:
        i = get_integer("Row#(1,2,3,4,5,6): ",1,6) - 1
        j = get_integer("Column#(1,2,3,4,5,6): ",1,6) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1,2,3,4,5,6)): ",1,6)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n, ": Wrong number! Try again.")
        if time.time() - start > time_limits:
            print("Time is up! Game Over.")
            return
    end = time.time()
    print("It took you", round(end - start, 2), "seconds to complete the game.")
    print("Well done! Come again.")

# time.process_time() 대신 time.time()을 사용한 이유: 
# 프로세스 시간은 CPU 사용 시간만을 고려하기 때문에 실제 경과 시간과는 차이가 있을 수 있다.