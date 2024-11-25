from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.widget = Tk()
        self.widget.title("Boot.dev Maze Solver")
        self.widget.geometry(f"{width}x{height}")
        self.widget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.widget, width=width, height=height)
        self.canvas.pack(fill='both', expand=True)
        self.running = False

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
