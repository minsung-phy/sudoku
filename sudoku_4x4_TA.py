import random
import time

def initialize_board_4x4(): 
    row0 = [1,2,3,4]
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1],row0[0],row0[3],row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

def create_solution_board_4x4():
    board = initialize_board_4x4()
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
    print("Time Limit | Beginner: 30s, Intermediate: 40s , Advanced: 50s")
    level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10
    
def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
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

def sudoku_4x4_TA():
    solution_board = create_solution_board_4x4()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    if no_of_holes == 6:
        time_limits = 30
    elif no_of_holes == 8:
        time_limits = 40
    else:
        time_limits = 50
    show_board(puzzle_board)
    start = time.time()
    while no_of_holes > 0:
        i = get_integer("Row#(1,2,3,4): ",1,4) - 1
        j = get_integer("Column#(1,2,3,4): ",1,4) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1,2,3,4): ",1,4)
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