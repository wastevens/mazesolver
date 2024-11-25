from cell import Cell
from point import Point
import time
import random

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
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.seed = (0 if seed == None else seed)
        random.seed(self.seed)

    def create(self):
        for x in range(self.num_cols):
            self.cells.append([None for i in range(self.num_rows)])
            for y in range(self.num_rows):
                top_left = Point((x * self.cell_size_x) + self.x1, (y * self.cell_size_y) + self.y1)
                bottom_right = Point(((x+1) * self.cell_size_x) + self.x1, ((y+1) * self.cell_size_y) + self.y1)
                self.cells[x][y] = Cell(True, True, True, True, top_left, bottom_right, self.win)
                self.draw_cell(x, y)

    def open_enterance(self):
        self.cells[0][0].left_wall = False
        self.draw_cell(0, 0)

    def open_exit(self):
        self.cells[self.num_cols-1][self.num_rows-1].right_wall = False
        self.draw_cell(self.num_cols-1, self.num_rows-1)

    def break_walls(self):
        pass

    def break_walls_r(self, i, j):
        pos = (i, j)
        print(f"pos: {pos}")
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if(i > 0):
                if not self.cells[i-1][j].visited:
                    to_visit.append((i-1, j))
            if(i < self.num_cols -1):
                if not self.cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            if(j > 0):
                if not self.cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if(j < self.num_rows -1):
                if not self.cells[i][j+1].visited:
                    to_visit.append((i, j+1))
            
            if(len(to_visit) == 0):
                return
            print(f"to_visit: {to_visit}")
            target = random.choice(to_visit)
            print(f"target: {target}")
            self.break_wall(pos, target)
            self.break_walls_r(target[0], target[1])

    def break_wall(self, pos, target):
        print(f"break wall between {pos} and {target}")
        if(pos[0] - target[0] == 0):
            #same col
            if(pos[1] - target[1] > 0):
                print(f"target up")
                self.cells[pos[0]][pos[1]].top_wall = False
                self.cells[target[0]][target[1]].bottom_wall = False
            elif(pos[1] - target[1] < 0):
                print(f"target down")
                self.cells[pos[0]][pos[1]].bottom_wall = False
                self.cells[target[0]][target[1]].top_wall = False
            else:
                raise Exception(f"position {pos} and target {target} cannot be equal")
            self.draw_cell(pos[0], pos[1])
            self.draw_cell(target[0], target[1])
            return
        
        if(pos[0] - target[0] > 0):
            print(f"target left")
            self.cells[pos[0]][pos[1]].left_wall = False
            self.cells[target[0]][target[1]].right_wall = False
        elif(pos[0] - target[0] < 0):
            print(f"target right")
            self.cells[pos[0]][pos[1]].right_wall = False
            self.cells[target[0]][target[1]].left_wall = False
        else:
            raise Exception(f"position {pos} and target {target} cannot be equal")
        self.draw_cell(pos[0], pos[1])
        self.draw_cell(target[0], target[1])
            
            

            

        

    def draw_cell(self, i, j):
        print(f"draw cell[{i}][{j}] {self.cells[i][j]}")
        self.cells[i][j].draw()
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)


