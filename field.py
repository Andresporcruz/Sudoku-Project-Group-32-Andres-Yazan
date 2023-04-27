import pygame, sys
from game_constants import *
from sudoku_generator import SudokuGenerator
from cells import Cell

#Initializing pygame module

pygame.init()

#Setting the caption of the game window
pygame.display.set_caption("Sudoku")

#Creating a font object with size 40
font = pygame.font.Font(None, 40)

#Class definition for the Sudoku board
class Board:
    solutionBoard = None
    userBoard = None
    blankBoard = None

    def __init__(self, width, height, screen, difficulty):
        # Creating empty lists for empty cells, sketched numbers, and changed numbers
        self.empty = []
        self.sketchedNums = []
        self.changedNums = []
        self.width = width
        self.height = height
        self.screen = screen
        self.diff = difficulty

        # Initializing the Sudoku board based on difficulty level
        if self.diff == 'easy':
            self.sudoku = SudokuGenerator(9, 30)
        elif self.diff == 'medium':
            self.sudoku = SudokuGenerator(9, 40)
        elif self.diff == 'hard':
            self.sudoku = SudokuGenerator(9, 50)

        # Filling in the Sudoku board with values and getting the board
        self.sudoku.fill_values()
        self.sudoku.get_board()

        # Setting the solution board to the printed version of the board
        self.solutionBoard = self.sudoku.print_board()

        # Removing cells from the board to create the user board
        self.sudoku.remove_cells()
        self.userBoard = self.sudoku.get_board()

    # Drawing the Sudoku board on the game window
    def draw(self):
        # Filling the background color of the screen
        self.screen.fill(BG_COLOR)

        # Drawing the horizontal lines of the board
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen,
                             LINE_COLOR,
                             (0, i * SQUARE_SIZE),
                             (WINDOW_WIDTH, i * SQUARE_SIZE),
                             LINE_WIDTH)

        # Drawing the vertical lines of the board
        for i in range(1, BOARD_COLS):
            pygame.draw.line(self.screen,
                             LINE_COLOR,
                             (i * SQUARE_SIZE, 0),
                             (SQUARE_SIZE * i, 600),
                             LINE_WIDTH)

        # Drawing the small lines of the board
        for i in range(1, SMALL_BOARD_ROWS):
            pygame.draw.line(self.screen,
                             LINE_COLOR,
                             (0, i * (SQUARE_SIZE / 3)),
                             (WINDOW_WIDTH, i * (SQUARE_SIZE / 3)),
                             SMALL_LINE_WIDTH)

            pygame.draw.line(self.screen,
                             LINE_COLOR,
                             (i * (SQUARE_SIZE / 3), 0),
                             ((SQUARE_SIZE / 3) * i, 600),
                             SMALL_LINE_WIDTH)

        # Finding empty cells and drawing them on the board
        for i in range(9):
            for j in range(9):
                if self.userBoard[i][j] == 0:
                    emptyCell = [i, j]
                    self.empty.append(emptyCell)
                cell = Cell(self.userBoard[i][j], i, j, self.screen)
                cell.draw()

        # Sketching numbers into the board
        for num in self.sketchedNums:
            num.sketch_draw()  # using cell class method to sketch the number

    # Selecting a cell on the board
    def select(self, row, col):
        # Checking if the click is on the board
        if row != None and col != None and row <= 8 and col <= 8:
            return True
        else:
            return False
    #Clear the value of a sketched number in a cell
    def clear(self, cell):
        if cell in self.sketchedNums:
            cell.value = 0
    #Sketch a number in a cell and add it to the list of sketched numbers and changed numbers
    def sketch(self, row, col, value):
        sketch = Cell(value, row, col, self.screen)
        self.sketchedNums.append(sketch)
        self.changedNums.append(sketch)
    #Place a number in a cell if the cell is empty
    def place_number(self, row, col, value):
        if self.sudoku.board[row][col] == 0:
            self.sudoku.board[row][col] == value
        else:
            return None
    #Reset all sketched numbers to their original value of 0
    def reset_to_original(self):
        for i in self.sketchedNums:
            i.value = 0
    #Check if the board is full
    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.board[i][j] == 0:
                    return False
                else:
                    continue
        return True
    #Update the board
    def update_board(self):
        pass
    #Find the empty cells
    def find_empty(self):
        pass
    def check_board(self): #checks if the values match in the userBoard & solutionBoard
        for i in range(9):
            for j in range(9):
                if self.userBoard[i][j] != self.solutionBoard[i][j]:
                    return False
        return True
