from sudoku_fun import sudoku_prob_sol,sudoku_puz

a=1
while a>0:
    print('\n')
    try:
        choise=int(input("1 for start the game\n2 for get a puzzle & it's solution\n3 for stop the game\nEnter any one:  "))
    except ValueError:
        print("Invalid choice")
        continue

    match choise:
        case 1:
            sudoku_puz()
        case 2:
            sudoku_prob_sol()
        case 3:
            print("Good Bye")
            break
        case _:
            print("Invalid choice")