import tkinter as tk
from tkinter import ttk
from gui.graphics import Grid, Window


def create_annual_review(year):
    window = Window(600, 800, "Annual review")
    root = window.get_root()


    title_label = ttk.Label(root, text= f"Reading stats of {year}", font= ("Arial", 20))
    title_label.grid(row = 0, column= 0, columnspan= 2)

    books_canvas = tk.Canvas(root, width=450, height=300, bg="white")
    books_canvas.grid(row= 1, column= 0)
    grid_title = books_canvas.create_text((150, 40), text= "Books By Month", font=("Arial", 16))
    empty_grid = Grid(20, 50, 6, 10, 40, 40, books_canvas)
    legend_canvas = tk.Canvas(root, width=150, height=300, bg="white")
    legend_canvas.grid(row=1, column=1)
    
    pages_canvas = tk.Canvas(root, width=600, height=400, bg="white")
    pages_canvas.grid(row= 2, column=0, columnspan= 2)

    window.run()

if __name__ == "__main__":
    create_annual_review()
    
