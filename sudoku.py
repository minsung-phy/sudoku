import sudoku_4x4
import sudoku_6x6
import sudoku_9x9
import sudoku_4x4_TA
import sudoku_6x6_TA
import sudoku_9x9_TA

def select_mode():
    print("Choose Game Mode!")
    mode = input("Normal=1, TimeAttack=2: ")
    while mode not in ("1","2"):
        mode = input("Normal=1, TimeAttack=2: ")
    if mode == "1":
        return 1
    else:
        return 2

def get_level():
    print("Enter your level.")
    level = input("4x4=1, 6x6=2, 9x9=3: ")
    while level not in ("1","2","3"):
        level = input("4x4=1, 6x6=2, 9x9=3: ")
    if level == "1":
        return 1
    elif level == "2":
        return 2
    else:
        return 3

def sudoku():
    mode = select_mode()
    if mode == 1:
        normal_level = get_level()
        if normal_level == 1:
            sudoku_4x4.sudoku_4x4()
        elif normal_level == 2:
            sudoku_6x6.sudoku_6x6()
        else:
            sudoku_9x9.sudoku_9x9()
    else:
        normal_level = get_level()
        if normal_level == 1:
            sudoku_4x4_TA.sudoku_4x4_TA()
        elif normal_level == 2:
            sudoku_6x6_TA.sudoku_6x6_TA()
        else:
            sudoku_9x9_TA.sudoku_9x9_TA()
            
sudoku()