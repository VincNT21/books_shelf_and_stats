import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

from datetime import date

from helpers.date_utils import convert_date_to_str

from gui.base_page import BasePage

class AddBookPage(BasePage):
    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        # Configure the grid:
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=3)

        
        ttk.Button(self, 
                  text= "Back to home page",
                  command=lambda: self.page_manager.show_page("home")
                  ).grid(row=8, column=3)
        
        ttk.Label(self, text= "Add a new book", background="white").grid(row=0, columnspan=4)
        
        self.title = tk.StringVar()
        self.author = tk.StringVar()
        self.editor = tk.StringVar()
        self.page_nbr = tk.IntVar()
        self.year_published = tk.IntVar()
        self.main_genre = tk.StringVar()
        self.sub_genre = tk.StringVar()
        self.isbn = tk.StringVar()
        self.is_read = tk.BooleanVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()

        ttk.Label(self, text="Title =", background="white").grid(row=1, column=0)
        ttk.Entry(self, textvariable=self.title).grid(row=1, column=1)

        ttk.Label(self, text="Author =", background="white").grid(row=2, column=0)
        ttk.Entry(self, textvariable=self.author).grid(row=2, column=1)

        ttk.Label(self, text="Editor =", background="white").grid(row=3, column=0)
        ttk.Entry(self, textvariable=self.editor).grid(row=3, column=1)

        ttk.Label(self, text="ISBN =", background="white").grid(row=4, column=0)
        ttk.Entry(self, textvariable=self.isbn).grid(row=4, column=1)

        ttk.Label(self, text="Pages number =", background="white").grid(row=1, column=2)
        ttk.Entry(self, textvariable=self.page_nbr).grid(row=1, column=3)

        ttk.Label(self, text="Year published =", background="white").grid(row=2, column=2)
        ttk.Entry(self, textvariable=self.year_published).grid(row=2, column=3)

        # Main genre and sub genre Comboboxes :
        self.book_genres = self.page_manager.app_context.library_manager.get_genres_dict()
        
        ttk.Label(self, text="Main genre =", background="white", font=("Arial", 10)).grid(row=3, column=2)
        
        main_genres_cb = ttk.Combobox(self, textvariable=self.main_genre)
        main_genres_cb["values"] = list(self.book_genres.keys())
        main_genres_cb.grid(row=3, column=3)

        def sub_genre_update(event):
            selected_main_genre = self.main_genre.get()
            if selected_main_genre in self.book_genres:
                new_sub_genres = self.book_genres[selected_main_genre]
                sub_genres_cb["values"] = new_sub_genres
                self.sub_genre.set("")
                    

        main_genres_cb.bind("<<ComboboxSelected>>", sub_genre_update)

        ttk.Label(self, text="Sub genre =", background="white").grid(row=4, column=2)

        # I WAAAAS HEEEEERE
        sub_genres_cb = ttk.Combobox(self, textvariable=self.sub_genre)
        sub_genres_cb.grid(row=4, column=3)

        def toogle_start_date_entry_state():
            if self.selected.get() == "not":
                start_entry.configure(state="disabled")
                end_entry.configure(state="disabled")
                self.is_read.set(False)
                self.end_date.set("")
            if self.selected.get() == "began":
                start_entry.configure(state="normal")
                end_entry.configure(state="disabled")
                self.is_read.set(False)
                self.end_date.set("")
            if self.selected.get() == "read":
                start_entry.configure(state="normal")
                end_entry.configure(state="normal")
                self.is_read.set(True)
                today_date = convert_date_to_str(date.today())
                self.end_date.set(today_date)

        lf = ttk.LabelFrame(self, text="Reading status :", labelanchor="nw", style="Custom.TLabelFrame")
        lf.grid(row=5, columnspan=4)
        self.selected = tk.StringVar(value="not")
        ttk.Radiobutton(lf, text="Book not read", value="not", variable=self.selected, command=toogle_start_date_entry_state, style="Custom.TRadiobutton").pack(side= 'left', ipadx=5)
        ttk.Radiobutton(lf, text="Book began", value="began", variable=self.selected, command=toogle_start_date_entry_state, style="Custom.TRadiobutton").pack(side= 'left', ipadx=5)
        ttk.Radiobutton(lf, text="Book read", value="read", variable=self.selected, command=toogle_start_date_entry_state, style="Custom.TRadiobutton").pack(side= 'left', ipadx=5)
        
        ttk.Label(self, text="Dates must be in format : YYYY-mm-dd !", background="white").grid(row=6, columnspan=4)

        ttk.Label(self, text="Start date =", background="white").grid(row=7, column=0)
        start_entry = ttk.Entry(self, textvariable=self.start_date, state="disabled")
        start_entry.grid(row=7, column=1)

        ttk.Label(self, text="End date =", background="white").grid(row=7, column=2)
        end_entry = ttk.Entry(self, textvariable=self.end_date, state="disabled")
        end_entry.grid(row=7, column=3)

        ttk.Button(self, text="Add the book", command=self.click_add).grid(row=8, column=0)

    def add_a_book(self):
        # Convert dates entries to None if not provided: 
        start_date = None if self.start_date.get() == "" else self.start_date.get()
        end_date = None if self.end_date.get() == "" else self.end_date.get()

        if self.page_manager.app_context.library_manager.new_book(
                self.title.get(), self.author.get(), 
                self.editor.get(), self.page_nbr.get(), self.year_published.get(),
                self.main_genre.get(), self.sub_genre.get(), self.isbn.get(),
                self.is_read.get(), start_date, end_date
                ):
            print("Book added!")


    def click_add(self):
        
        # Ask for confirmation with data checks
        answer = askyesno(
            title="Confirmation", 
            message=f"""
Do you want to add this new book ?

Title: {self.title.get()}
Author: {self.author.get()}
Editor: {self.editor.get()}
ISBN: {self.isbn.get()}
Pages number: {self.page_nbr.get()}
Year published: {self.year_published.get()}
Main genre: {self.main_genre.get()}
Sub genre: {self.sub_genre.get()}
Start date: {self.start_date.get()}
End date: {self.end_date.get()}

            """
            )
        
        # If ok, go for new book
        if answer:
            self.add_a_book()
            self.page_manager.show_page("home")

    def reset_form(self):
        self.title.set("")
        self.author.set("")
        self.editor.set("")
        self.page_nbr.set(0)
        self.year_published.set(0)
        self.main_genre.set("")
        self.sub_genre.set("")
        self.isbn.set("")
        self.is_read.set(False)
        self.start_date.set("")
        self.end_date.set("")
            

    



        






