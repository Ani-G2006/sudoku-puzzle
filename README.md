# Sudoku Game (Command Line)

A command-line Sudoku game written in Python. Every run generates a new random puzzle. You can play it by entering numbers cell by cell, or simply view a puzzle together with its solution.

## Features

- Random 9x9 Sudoku grid generated on every run
- Puzzle with 23 pre-filled clues (empty cells shown as `.`)
- Play mode: enter row, column and number to fill a cell
- Instant feedback ("Correct!" or "Wrong choice") and the updated grid after each correct entry
- Option to continue or stop and view the full answer at any time
- Option to show a puzzle and its solution directly
- Input validation for non-numeric input, out-of-range rows/columns and already-filled cells
- Neat grid output with separators for the 3x3 boxes

## Project Structure

```
sudoku-game/
├── sudoku_cal.py    # main file: menu and program loop
├── sudoku_fun.py    # game functions: puzzle generation, play mode, solution display
└── README.md
```

- `sudoku_cal.py` - shows the main menu and calls the functions.
- `sudoku_fun.py` - contains `sudoku_puz()` (play the game) and `sudoku_prob_sol()` (show question and answer).

## Requirements

- Python 3.10 or newer (the `match` statement is used)
- NumPy

Install NumPy:

```bash
pip install numpy
```

## How to Run

```bash
python sudoku_cal.py
```

## Menu Options

```
1 for start the game
2 for get a puzzle & it's solution
3 for stop the game
```

| Option | What it does |
|--------|--------------|
| 1 | Starts a new puzzle and lets you fill in the empty cells |
| 2 | Prints a new puzzle followed by its solution |
| 3 | Exits the program |

## How to Play (Option 1)

1. A puzzle is printed with `.` marking the empty cells.
2. Enter the **row number** (1-9) and **column number** (1-9) of the cell you want to fill.
3. Enter the number you think belongs there.
4. If it is correct, the cell is filled and the updated grid is shown. If not, you get "Wrong choice".
5. After each attempt, choose:
   - `1` to continue
   - `2` to stop and view the answer
6. The game ends with "You solved it!" once all empty cells are filled correctly.

## How the Puzzle Is Generated

1. A valid base grid is built using the formula `(i * 3 + i // 3 + j) % 9 + 1`.
2. A random number from 1 to 9 shifts every digit, so each run gives a different grid.
3. Only the cells at the fixed clue positions are kept to form the puzzle.

## Notes

- The clue positions are fixed, so a puzzle may not always have a unique solution. The game checks your entry against the generated answer grid.
- Both files must be in the same folder, since `sudoku_cal.py` imports from `sudoku_fun.py`.

## Future Improvements

- Difficulty levels (easy, medium, hard)
- Random clue positions for more variety
- Guarantee a unique solution for every puzzle
- Timer and hint option
- Remove repeated grid-printing code by using one helper function

## Author

B.Tech CSE student, VIT Bhopal
