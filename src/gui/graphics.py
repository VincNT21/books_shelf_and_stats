from tkinter import Tk, Canvas

class Window:
    def __init__(self, width, height, title):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f"{width}x{height}")

    def get_root(self):
        return self.__root  

    def run(self):
        self.__root.mainloop()


class WhiteCanvas:
    def __init__(self, window, width, height):
        self.__canvas = Canvas(window, width= width, height= height, bg="white")
        self.__canvas.pack()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__canvas.update_idletasks()
        self.__canvas.update()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

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

