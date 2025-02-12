import tkinter as tk
from tkinter import ttk

from gui.base_page import BasePage

class AddBookPage(BasePage):
    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)
        
        ttk.Button(self, 
                  text= "Back to home page",
                  command=lambda: self.page_manager.show_page("home")
                  ).pack(side= "bottom", pady= 10)
        
