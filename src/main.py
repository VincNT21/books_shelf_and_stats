import tkinter as tk
from gui.page_manager import PageManager

from gui.helpers.window_utils import center_window, set_window_icon

if __name__ == "__main__":
    root = tk.Tk()
    width = 1024
    height = 768
    root.title("Book Shelf and Stats")
    
    # to remove/replace before shipping
    center_window(root, width, height)
    set_window_icon(root, "bookshelf_icon.png")

    app = PageManager(root)
    app.show_page("home")
    root.mainloop()