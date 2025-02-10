from gui.primitives import Line, Point

def diagonal_lines(x1, x2, y1, y2):
    diagonal_list = []
    cell_width = x2 - x1
    cell_height = y2 - y1
    for i in range(1, 4):
        left_top_line = Line(Point(x1, y1 + ((cell_height / 4) * i)), Point(x1 + ((cell_width / 4) * i), y1))
        diagonal_list.append(left_top_line)
    middle_line = Line(Point(x1, y2), Point(x2, y1))
    diagonal_list.append(middle_line)
    for i in range(1, 4):
        bottom_right_line = Line(Point(x1 + ((cell_width / 4) * i), y2), Point(x2, y1 + ((cell_height / 4) * i)))
        diagonal_list.append(bottom_right_line)
    return diagonal_list
    
    