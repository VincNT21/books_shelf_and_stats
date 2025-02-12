import tkinter as tk
from tkinter import ttk

from config import file_path_in_icons
from helpers.logging_utils import log_error

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

def set_window_icon(window, icon_name):
    file = file_path_in_icons(icon_name)
    try:
        icon = tk.PhotoImage(file= file)
        window.iconphoto(False, icon)
    except Exception as e:
        log_error(f"Could not load icon {file}. Reason: {e}")
