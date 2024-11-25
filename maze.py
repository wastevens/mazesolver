from cell import Cell
from point import Point
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []

    def create(self):
        for x in range(self.num_rows):
            self.cells.append([None for i in range(self.num_cols)])
            for y in range(self.num_rows):
                top_left = Point((x * self.cell_size_x) + self.x1, (y * self.cell_size_y) + self.y1)
                bottom_right = Point(((x+1) * self.cell_size_x) + self.x1, ((y+1) * self.cell_size_y) + self.y1)
                self.cells[x][y] = Cell(True, True, True, True, top_left, bottom_right, self.win)
                self.draw_cell(x, y)

    def open_enterance(self):
        self.cells[0][0].left_wall = False
        self.draw_cell(0, 0)

    def open_exit(self):
        self.cells[self.num_rows-1][self.num_cols-1].right_wall = False
        self.draw_cell(self.num_rows-1, self.num_cols-1)

    def draw_cell(self, i, j):
        self.cells[i][j].draw()
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)


