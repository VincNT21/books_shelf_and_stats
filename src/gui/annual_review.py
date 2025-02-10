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
    yearly_statistics = load_statistics_file(year)

    # Title top of window
    title_label = ttk.Label(root, text= f"Reading stats of {year}", font= ("Arial", 20), padding= 5)
    title_label.grid(row = 0, column= 0, columnspan= 2)

    # Canvas for Books By Month grid
    books_canvas = tk.Canvas(root, width=450, height=300, bg="white")
    books_canvas.grid(row= 1, column= 0)
    grid_title = books_canvas.create_text((150, 40), text= "Books By Month", font=("Arial", 16))
    books_grid = Grid(20, 50, 6, 10, 40, 40, books_canvas)

    # Canvas for Months captions
    caption_canvas = tk.Canvas(root, width=150, height=300, bg="white")
    caption_canvas.grid(row=1, column=1)
    caption_grid = Grid(20, 50, 12, 1, 20, 20, caption_canvas)

    # Filling the captions with months names
    month_text_ids = {}
    i = 0
    for month in months_colors:
        text_id = caption_canvas.create_text(45, (60 + (i * 20)), text= month, anchor="w")
        month_text_ids[month] = text_id
        i += 1  

    # Coloring the Books By Month and caption
    row_index = 0
    column_index = 0
    for month in yearly_statistics:
        month_count = yearly_statistics[month]["count"]
        if month_count == 0:
            continue
        month_color = months_colors[month]
        month_index = month_to_index[month]
        month_text_id = month_text_ids[month]
        caption_canvas.itemconfig(month_text_id, fill="red", font=("TkDefaultFont", 10, "bold"))
        caption_grid._cells[0][month_index].color(month_color, window)
        for r in range(0, month_count):
            books_grid._cells[column_index][row_index].color(month_color, window)
            column_index += 1
            if column_index == 10:
                column_index = 0
                row_index += 1
            if row_index == 6:
                raise ValueError("Too many books read !! (max 60)")
        caption_canvas.itemconfig(month_text_id, fill="black", font=("TkDefaultFont", 10, "normal"))
    
            
    # Canvas for Pages By Month graph
    pages_canvas = tk.Canvas(root, width=600, height=400, bg="white")
    pages_canvas.grid(row= 2, column=0, columnspan= 2)
    
    # Running it !
    window.run()


def load_statistics_file(year):
    filename = f"statistics_{year}.json"
    filepath = json_path(filename)
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except OSError as e:
        log_error(f"Error: Failed to read from {filepath}. Reason: {e}")


if __name__ == "__main__":
    create_annual_review()