from line import Line
from point import Point

class Cell():

    def __init__(self, left_wall, right_wall, top_wall, bottom_wall, top_left, bottom_right, window):
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.window = window

    def draw(self):
        if(self.left_wall):
            self.window.draw_line(Line(self.top_left, Point(self.top_left.x, self.bottom_right.y)), "black")
        if(self.right_wall):
            self.window.draw_line(Line(self.bottom_right, Point(self.bottom_right.x, self.top_left.y)), "black")
        if(self.top_wall):
            self.window.draw_line(Line(self.top_left, Point(self.bottom_right.x, self.top_left.y)), "black")
        if(self.bottom_wall):
            self.window.draw_line(Line(self.bottom_right, Point(self.top_left.x, self.bottom_right.y)), "black")