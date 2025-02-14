import tkinter as tk
from gui.page_manager import PageManager

from gui.helpers.window_utils import center_window, set_window_icon
from managers.app_context import AppContext

if __name__ == "__main__":
    root = tk.Tk()
    width = 1024
    height = 768
    root.title("Book Shelf and Stats")
    root.configure(bg="white")
    
    center_window(root, width, height)
    set_window_icon(root, "bookshelf_icon.png")

    app_context = AppContext()
    

    app = PageManager(root, app_context)
    app.show_page("home")
    root.mainloop()