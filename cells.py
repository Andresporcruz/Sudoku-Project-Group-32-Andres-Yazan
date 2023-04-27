import pygame
from game_constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched = None

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self):  # draws numbers on the board
        font = pygame.font.Font(None, 40)
        if self.value == 0:  # if it was removed, print empty string instead of 0
            surf = font.render("", 0, NUMBER_COLOR)
        else:
            surf = font.render(str(self.value), 0, NUMBER_COLOR)  # uses black for number color
        rect = surf.get_rect(center=((SQUARE_SIZE / 3) // 2 + (SQUARE_SIZE / 3) * self.col,  # puts number in the center
                                     (SQUARE_SIZE / 3) // 2 + (SQUARE_SIZE / 3) * self.row))
        self.screen.blit(surf, rect)  # prints board numbers in center of each cell

    def sketch_draw(self):  # sketches guess into board
        font = pygame.font.Font(None, 42)
        if self.value == 0:  # if it was removed, print empty string instead of 0
            surf = font.render("", 0, NUMBER_COLOR)
        else:
            surf = font.render(str(self.value), 0, SKETCH_COLOR)  # uses gray for sketch color
        rect = surf.get_rect(
            center=((SQUARE_SIZE / 3) // 3.5 + (SQUARE_SIZE / 3) * self.col,  # puts sketch in the top left
                    (SQUARE_SIZE / 3) // 3.5 + (SQUARE_SIZE / 3) * self.row))
        self.screen.blit(surf, rect)

    def highlight(self):
        pygame.draw.rect(self.screen, HIGHLIGHT_COLOR,
                         pygame.Rect(self.col * SQUARE_SIZE / 3 + 1, self.row * SQUARE_SIZE / 3 + 2, SQUARE_SIZE / 3,
                                     SQUARE_SIZE / 3), SMALL_LINE_WIDTH + 1)
