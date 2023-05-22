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
    print("Enter your level.")
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

# 스도쿠 알고리즘
# 1. 무작위로 스도쿠 정답보드 solution_board를 만든다.
# 2. solution_board를 복제하여 puzzle_board를 하나 만든다.
# 3. 사용자에게 난이도를 선택하게 하여 빈칸의 개수 no_of_holes를 정한다.
# 4. puzzle_board에 no_of_holes만큼 무작위로 선택하여 0으로 채운다.
# 5. puzzle_board를 실행창에 정한 형식대로 보여준다. 실행창에는 빈칸을 (0이 아닌) 점으로 표시한다.
# 6. 다음 절차를 no_of_holes가 0이 될 때까지 반복한다.
#    (a) 숫자를 채울 빈칸의 가로줄번호 i, 세로줄번호 j를 차례로 입력받는다.
#    (b) (i, j) 위치에 있는 숫자가 0이 아니면 빈칸이 아니므로 재입력받는다.
#    (c) 빈칸이면, 숫자(1,2,3,4) n을 입력받는다.
#    (d) n이 solution_board[i][j]와 같으면, puzzle_board[i][j]에 그 숫자를 채우고, 갱신한 puzzle_board를 보여준다.
#    (e) 이 숫자가 solution_board[i][j]와 다르면, 줄 번호부터 모두 다시 재입력 받는다.

def sudoku_4x4():
    solution_board = create_solution_board_4x4()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
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
    end = time.time()
    print("It took you", round(end - start, 2), "seconds to complete the game.")
    print("Well done! Come again.")

# time.process_time() 대신 time.time()을 사용한 이유: 
# 프로세스 시간은 CPU 사용 시간만을 고려하기 때문에 실제 경과 시간과는 차이가 있을 수 있다.