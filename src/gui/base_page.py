import tkinter as tk
from tkinter import ttk

class BasePage(ttk.Frame):
    def __init__(self, parent, page_manager):
        super().__init__(parent, style='Page.TFrame')
        self.page_manager = page_manager