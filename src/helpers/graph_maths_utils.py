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

def diagonal_lines_for_bar(x1, x2, y1, y2, step):
    diagonal_list = []
    diag_x1 = x1
    diag_x2 = x1 + step
    while diag_x2 < x2:
        diagonal = Line(Point(diag_x1, y2), Point(diag_x2, y1))
        diagonal_list.append(diagonal)
        diag_x2 += step
        diag_x1 += step
    if diag_x1 < x2:
        last_diagonal = Line(Point(diag_x1, y2), Point(x2, y1))
        diagonal_list.append(last_diagonal)
    return diagonal_list

def fake_progress_bar(x1, x2, y1, y2, step):
    lines_list = []
    curr_x = x1 + step
    while curr_x < x2:
        new_line = Line(Point(curr_x, y2), Point(curr_x, y1))
        lines_list.append(new_line)
        curr_x += step
    return lines_list

    

    