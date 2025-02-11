import tkinter as tk
from tkinter import ttk
from gui.annual_review import create_annual_review

class HomePage(ttk.Frame):
    def __init__(self, parent, page_manager):
        super().__init__(parent)
        self.page_manager = page_manager
        ttk.Label(self, text= "Welcome to home page !").pack(pady= 10)
        ttk.Button(self, 
                   text= "Annual review !", 
                   command=lambda: create_annual_review("2024")).pack(pady= 5)
        ttk.Button(self,
                   text = "Add new books",
                   command=lambda: self.parent_manager.show_page("add_book") ).pack(pady= 5)
