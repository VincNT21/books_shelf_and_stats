import tkinter as tk
from tkinter import ttk
from gui.annual_review import create_annual_review
from config import file_path_in_images
from gui.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        ttk.Label(self, text= "Welcome to home page !", background="white").pack(pady= 10)

        image_file = file_path_in_images("home_page_image.png")
        self.book_shelf_image = tk.PhotoImage(file= image_file)
        ttk.Label(self, image= self.book_shelf_image, text= "bg_image", padding= 5, compound= "image", borderwidth=0, background="white").pack()
        
        ttk.Button(self, 
                   text= "Show my library",
                   command=lambda: self.page_manager.show_page("book_library")
                   ).pack(pady= 5)
        ttk.Button(self, 
                   text= "Annual review !", 
                   command=lambda: create_annual_review("2024")
                   ).pack(pady= 5)
        ttk.Button(self,
                   text = "Add new books",
                   command=lambda: self.page_manager.show_page("add_book")
                   ).pack(pady= 5)
