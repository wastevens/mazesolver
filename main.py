from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(True, False, True, True, Point(20, 20), Point(40, 40), win)
    cell2 = Cell(False, True, True, True, Point(40, 20), Point(60, 40), win)
    cell3 = Cell(True, False, True, True, Point(20, 40), Point(40, 60), win)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell1.draw_move(cell2, True)
    cell1.draw_move(cell3)
    
    win.wait_for_close()

    

main()