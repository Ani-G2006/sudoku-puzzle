import numpy as np
import random

def sudoku_prob_sol():
    a = random.randint(1, 9)      
    box = np.zeros([9, 9])
    for i in range(9):
        for j in range(9):
            box[i][j] = (i * 3 + i // 3 + j) % 9 + 1
    box = (box + a - 1) % 9 + 1

    clues = [(0, 0), (0, 3), (1, 1), (1, 5), (1, 6), (2, 2), (2, 8),(3, 5), (4, 4), (4, 1), (5, 7), 
             (5, 2), (6, 4), (6, 0),(7, 3), (7, 8), (8, 2), (8, 4), (8, 6),(0,8),(3,6),(2,7),(6,6)]

    puzzle = np.zeros((9, 9), dtype=int)
    for r, c in clues:
        puzzle[r][c] = box[r][c]                                                      # sudoku problem
    print("\nQuestion:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 34)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="  ")
            print(int(puzzle[i][j]) if puzzle[i][j] != 0 else ".", end="  ")
        print()
    
    print("\nAnswer:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 34)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="  ")
            print(int(box[i][j]) , end="  ")
        print()
    print("\n")





def sudoku_puz():
    a = random.randint(1, 9)      
    box = np.zeros([9, 9])                               # construct sudoku
    for i in range(9):
        for j in range(9):
            box[i][j] = (i * 3 + i // 3 + j) % 9 + 1
    box = (box + a - 1) % 9 + 1

    clues = [(0, 0), (0, 3), (1, 1), (1, 5), (1, 6), (2, 2), (2, 8),(3, 5), (4, 4), (4, 1), (5, 7), 
             (5, 2), (6, 4), (6, 0),(7, 3), (7, 8), (8, 2), (8, 4), (8, 6),(0,8),(3,6),(2,7),(6,6)]

    puzzle = np.zeros((9, 9), dtype=int)
    for r, c in clues:
        puzzle[r][c] = box[r][c]                                                      # sudoku problem
    print("\nQuestion:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 34)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="  ")
            print(int(puzzle[i][j]) if puzzle[i][j] != 0 else ".", end="  ")
        print()
    print("\n")
    
    filled = 0                                                     # input of  ans
    total_empty = int((puzzle == 0).sum())                                   
    while filled < total_empty:
        try:
            r = int(input('enter row no: ')) - 1
            c = int(input('enter column no: ')) - 1
        except ValueError:
            print("Please enter numbers only")
            continue

        if not (0 <= r < 9 and 0 <= c < 9):
            print("Row and column must be between 1 and 9")
            continue

        if puzzle[r][c] == 0:
            try:
                sol = int(input("Enter a number: "))
            except ValueError:
                print("Please enter numbers only")
                continue
            if box[r][c] == sol:
                puzzle[r][c] = sol
                filled += 1
                print("Correct!\n")
                for i in range(9):
                    if i % 3 == 0 and i != 0:
                        print("-" * 34)
                    for j in range(9):
                        if j % 3 == 0 and j != 0:
                            print("|", end="  ")
                        print(int(puzzle[i][j]) if puzzle[i][j] != 0 else ".", end="  ")
                    print()
                print("\n")
                if filled == total_empty:
                    break
            else:
                print('Wrong choice')
        else:
            print("That cell is already filled") 

        a=0
        while a%10==0:
            try:
                choise=int(input("enter 1 for continue\nenter 2 for stop & view the answer\nEnter any one: "))
            except ValueError:
                print("wrong Choice")
                continue
            match choise:
                case 1:
                    print("Go forward")
                    a=1                      # leave the menu and continue the game
                case 2:
                    print("\nWell Try\n")
                    for i in range(9):
                        if i % 3 == 0 and i != 0:
                            print("-" * 34)
                        for j in range(9):
                            if j % 3 == 0 and j != 0:
                                print("|", end="  ")
                            print(int(box[i][j]) , end="  ")
                        print()
                    print("\n")
                    return                   # stop the game
                case _:
                    print("wrong Choice")

    if filled==total_empty:
        print("\nYour Answer\n")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 34)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end="  ")
                print(int(puzzle[i][j]) if puzzle[i][j] != 0 else ".", end="  ")
            print()
        print("\nYou solved it!")