

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, state= "normal"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, width=2, state= state)

    def draw_diagonal(self, canvas, fill_color="black", width=2):
        line_id = canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width= width)
        canvas.lower(line_id)
        