import tkinter as tk
import json

from tkinter import ttk

from gui.graphics import Grid, Window, Cell
from config import json_path
from helpers.logging_utils import log_error
from helpers.months_dicts import months_colors, month_to_index



def create_annual_review(year):
    window = Window(600, 800, "Annual review")
    root = window.get_root()
    monthly_statistics = load_statistics_file(year, "monthly")
    annual_statistics = load_statistics_file(year, "annual")

    # Title top of window
    title_label = ttk.Label(root, text= f"Reading stats of {year}", font= ("Arial", 20), padding= 5)
    title_label.grid(row = 0, column= 0, columnspan= 2)

    # Canvas for Books By Month grid
    books_canvas = tk.Canvas(root, width=450, height=300, bg="white")
    books_canvas.grid(row= 1, column= 0)
    book__title = books_canvas.create_text((225, 35), text= "Books By Month", font=("Arial", 16))
    books_grid = Grid(20, 50, 6, 10, 40, 40, books_canvas)

    # Canvas for Months captions
    caption_canvas = tk.Canvas(root, width=150, height=300, bg="white")
    caption_canvas.grid(row=1, column=1)
    caption_grid = Grid(40, 50, 12, 1, 20, 20, caption_canvas)

    # Canvas for Pages By Month graph
    pages_canvas = tk.Canvas(root, width=600, height=420, bg="white")
    pages_canvas.grid(row= 2, column=0, columnspan= 2)

    # Filling the captions with months names
    month_text_ids = {}
    i = 0
    for month in months_colors:
        text_id = caption_canvas.create_text(65, (60 + (i * 20)), text= month, anchor="w")
        month_text_ids[month] = text_id
        i += 1  

    # Coloring the Books By Month and caption
    row_index = 0
    column_index = 0
    i = - 1
    for month in monthly_statistics:
        month_count = monthly_statistics[month]["count"]
        i += 1
        if month_count == 0:
            caption_canvas.create_text(45, (60 + (i * 20)), text= month_count, anchor="w")
            continue
        month_color = months_colors[month]
        month_index = month_to_index[month]
        month_text_id = month_text_ids[month]
        caption_canvas.itemconfig(month_text_id, fill="red", font=("TkDefaultFont", 10, "bold"))
        caption_canvas.create_text(20, (60 + (i * 20)), text= month_count, anchor="w")
        caption_grid._cells[0][month_index].color_cells(month_color, window)
        for r in range(0, month_count):
            books_grid._cells[column_index][row_index].color_cells(month_color, window)
            column_index += 1
            if column_index == 10:
                column_index = 0
                row_index += 1
            if row_index == 6:
                raise ValueError("Too many books read !! (max 60)")
        caption_canvas.itemconfig(month_text_id, fill="black", font=("TkDefaultFont", 10, "normal"))
    
    # Creating and coloring the bar graph:
    pages_title = pages_canvas.create_text((300, 30), text= "Pages By Month", font=("Arial", 16))
    max_pages = annual_statistics["max_pages_read"]
    counter = 1
    for month in monthly_statistics:
        month_color = months_colors[month]
        month_nbr_pages = monthly_statistics[month]["pages"]
        bar_size = (500 * month_nbr_pages) / max_pages
        bar_pos_y = 20 + (30 * counter)
        month_caption = pages_canvas.create_text(20, 35 + (30 * counter), text= month[0:3], anchor="w")
        month_bar = Grid(50, bar_pos_y, 1, 1, bar_size, 30, pages_canvas, state= "hidden")
        month_bar._cells[0][0].color_bars(month_color, window, width= 10, step= 5)
        month_pages_caption = pages_canvas.create_text(bar_size + 60, bar_pos_y + 15, text=str(month_nbr_pages), anchor="w")
        counter += 1

    # Running it !
    window.run()

def load_statistics_file(year, type):
    filename = f"{type}_statistics_{year}.json"
    filepath = json_path(filename)
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except OSError as e:
        log_error(f"Error: Failed to read from {filepath}. Reason: {e}")


if __name__ == "__main__":
    create_annual_review()