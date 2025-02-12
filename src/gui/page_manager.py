import tkinter as tk
from tkinter import ttk

from gui.home_page import HomePage
from gui.add_book_page import AddBookPage
from gui.show_library import LibraryDisplay



class PageManager:
    def __init__(self, root):
        self.root = root
        self.current_frame = None

        self.style = ttk.Style()
        self.style.configure('Page.TFrame', background="white")

        self.home_page = HomePage(self.root, self)
        self.add_book_page = AddBookPage(self.root, self)
        self.library_page = LibraryDisplay(self.root, self)


    def show_page(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        
        if page_name == "home":
            self.current_frame = self.home_page
        elif page_name == "add_book":
            self.current_frame = self.add_book_page
        elif page_name == "book_library":
            self.current_frame = self.library_page


        self.current_frame.pack(fill= "both", expand=True)