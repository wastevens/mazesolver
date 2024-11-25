from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(20,20,5,5,30,30,win,0)

    maze.create()
    maze.animate()
    
    maze.open_enterance()
    maze.open_exit()
    
    maze.break_walls()

    maze.solve()

    win.wait_for_close()

    

main()