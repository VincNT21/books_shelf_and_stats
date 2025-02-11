import tkinter as tk
from tkinter import ttk

from gui.home_page import HomePage
from gui.add_book_page import AddBookPage

class PageManager:
    def __init__(self, root):
        self.root = root
        self.current_frame = None

        self.home_page = HomePage(self.root, self)
        self.add_book_page = AddBookPage(self.root, self)


    def show_page(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        
        if page_name == "home":
            self.current_frame = self.home_page
        elif page_name == "add_book":
            self.current_frame = self.add_book_page


        self.current_frame.pack(fill= "both", expand=True)