import time
from tkinter import Tk, Canvas
from helpers.graph_maths_utils import diagonal_lines
from gui.primitives import Point, Line

class Window:
    def __init__(self, width, height, title):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__running = False

    def get_root(self):
        return self.__root  

    def run(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
        print("window closed...")

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def close(self):
        self.__running = False


class Cell:
    def __init__(self, canvas=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._canvas = canvas

    def draw(self, x1, x2, y1, y2):
        if self._canvas is None: # in test case
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        left_wall.draw(self._canvas)
        right_wall.draw(self._canvas)
        top_wall.draw(self._canvas)
        bottom_wall.draw(self._canvas)

    def color(self, color, window):
        diagonal_lines_list = diagonal_lines(self._x1, self._x2, self._y1, self._y2)
        for line in diagonal_lines_list:
            line.draw_diagonal(self._canvas, fill_color= color)
            self._animate(window)
            
    def _animate(self, window):
        window.redraw()
        time.sleep(0.1)



class Grid:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, canvas=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._canvas = canvas
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            cells_col = []
            for j in range(self._num_rows):
                cells_col.append(Cell(self._canvas))
            self._cells.append(cells_col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
            x1 = self._x1 + (self._cell_size_x * i)
            x2 = self._x1 + (self._cell_size_x * (i + 1))
            y1 = self._y1 + (self._cell_size_y * j)
            y2 = self._y1 + (self._cell_size_y * (j + 1))
            self._cells[i][j].draw(x1, x2, y1, y2)

