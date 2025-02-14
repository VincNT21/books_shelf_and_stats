import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

from gui.base_page import BasePage

class EditPage(BasePage):
    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        # Configure the grid:
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=3)

        self.check_vars = {}

        ttk.Button(self, 
                  text= "Back to home page",
                  command=lambda: self.page_manager.show_page("home")
                  ).grid(row=8, column=5)
        ttk.Label(self, text= "Edit a book", background="white").grid(row=0, columnspan=6)

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
        

        def toogle_entry(check_var, entry_widget):
            if check_var.get():
                entry_widget.config(state="normal")
            else:
                entry_widget.config(state="disabled")
        
        
        ttk.Label(self, text="Title =", background="white").grid(row=1, column=1)
        title_entry = ttk.Entry(self, textvariable=self.title, state="disabled")
        title_entry.grid(row=1, column=2)
        title_check = tk.BooleanVar()
        self.check_vars["title"] = title_check
        ttk.Checkbutton(self, variable=title_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(title_check, title_entry)).grid(row=1, column=0)

        ttk.Label(self, text="Author =", background="white").grid(row=2, column=1)
        author_entry = ttk.Entry(self, textvariable=self.author, state="disabled")
        author_entry.grid(row=2, column=2)
        author_check = tk.BooleanVar()
        self.check_vars["author"] = author_check
        ttk.Checkbutton(self, variable=author_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(author_check, author_entry)).grid(row=2, column=0)

        ttk.Label(self, text="Editor =", background="white").grid(row=3, column=1)
        editor_entry = ttk.Entry(self, textvariable=self.editor, state="disabled")
        editor_entry.grid(row=3, column=2)
        editor_check = tk.BooleanVar()
        self.check_vars["editor"] = editor_check
        ttk.Checkbutton(self, variable=editor_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(editor_check, editor_entry)).grid(row=3, column=0)


        ttk.Label(self, text="ISBN =", background="white").grid(row=4, column=1)
        isbn_entry = ttk.Entry(self, textvariable=self.isbn, state="disabled")
        isbn_entry.grid(row=4, column=2)
        isbn_check = tk.BooleanVar()
        self.check_vars["isbn"] = isbn_check
        ttk.Checkbutton(self, variable=isbn_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(isbn_check, isbn_entry)).grid(row=4, column=0)
        

        ttk.Label(self, text="Pages number =", background="white").grid(row=1, column=4)
        page_nbr_entry = ttk.Entry(self, textvariable=self.page_nbr, state="disabled")
        page_nbr_entry.grid(row=1, column=5)
        page_nbr_check = tk.BooleanVar()
        self.check_vars["page_nbr"] = page_nbr_check
        ttk.Checkbutton(self, variable=page_nbr_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(page_nbr_check, page_nbr_entry)).grid(row=1, column=3)
        

        ttk.Label(self, text="Year published =", background="white").grid(row=2, column=4)
        year_entry = ttk.Entry(self, textvariable=self.year_published, state="disabled")
        year_entry.grid(row=2, column=5)
        year_check = tk.BooleanVar()
        self.check_vars["year_published"] = year_check
        ttk.Checkbutton(self, variable=year_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(year_check, year_entry)).grid(row=2, column=3)
        

        ttk.Label(self, text="Main genre =", background="white", font=("Arial", 10)).grid(row=3, column=4)
        main_genre_entry = ttk.Entry(self, textvariable=self.main_genre, state="disabled")
        main_genre_entry.grid(row=3, column=5)
        main_genre_check = tk.BooleanVar()
        self.check_vars["main_genre"] = main_genre_check
        ttk.Checkbutton(self, variable=main_genre_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(main_genre_check, main_genre_entry)).grid(row=3, column=3)
        

        ttk.Label(self, text="Sub genre =", background="white").grid(row=4, column=4)
        sub_genre_entry = ttk.Entry(self, textvariable=self.sub_genre, state="disabled")
        sub_genre_entry.grid(row=4, column=5)
        sub_genre_check = tk.BooleanVar()
        self.check_vars["sub-genre"] = sub_genre_check
        ttk.Checkbutton(self, variable=sub_genre_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(sub_genre_check, sub_genre_entry)).grid(row=4, column=3)

        def toogle_start_date_entry_state():
            if self.selected.get() == "not":
                self.is_read.set(False)
            if self.selected.get() == "began":
                self.is_read.set(False)
            if self.selected.get() == "read":
                self.is_read.set(True)

        
        lf = ttk.LabelFrame(self, text="Reading status :", labelanchor="nw", style="Custom.TLabelFrame")
        lf.grid(row=5, column=2, columnspan=2)
        self.selected = tk.StringVar()
        self.first_selected = None
        ttk.Radiobutton(lf, text="Book not read", value="not", variable=self.selected, command=toogle_start_date_entry_state, style="Custom.TRadiobutton", state="disabled").pack(side= 'left', ipadx=5)
        ttk.Radiobutton(lf, text="Book began", value="began", variable=self.selected, command=toogle_start_date_entry_state, style="Custom.TRadiobutton", state="disabled").pack(side= 'left', ipadx=5)
        ttk.Radiobutton(lf, text="Book read", value="read", variable=self.selected, command=toogle_start_date_entry_state, style="Custom.TRadiobutton", state="disabled").pack(side= 'left', ipadx=5)

        def set_labelframe_state(frame, enable):
            state = "normal" if enable else "disabled"
            for child in frame.winfo_children():
                child.configure(state=state) 

        toogle_check = tk.BooleanVar()

        ttk.Checkbutton(self, variable= toogle_check, style="Custom.TCheckbutton", command=lambda: set_labelframe_state(lf, toogle_check.get())).grid(row=5, column=1)

        ttk.Label(self, text="Dates must be in format : YYYY-mm-dd !", background="white").grid(row=6, columnspan=6)

        ttk.Label(self, text="Start date =", background="white").grid(row=7, column=1)
        start_entry = ttk.Entry(self, textvariable=self.start_date, state="disabled")
        start_entry.grid(row=7, column=2)
        start_entry_check = tk.BooleanVar()
        self.check_vars["start_date"] = start_entry_check
        ttk.Checkbutton(self, variable=start_entry_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(start_entry_check, start_entry)).grid(row=7, column=0)


        ttk.Label(self, text="End date =", background="white").grid(row=7, column=4)
        end_entry = ttk.Entry(self, textvariable=self.end_date, state="disabled")
        end_entry.grid(row=7, column=5)
        end_entry_check = tk.BooleanVar()
        self.check_vars["end_date"] = end_entry_check
        
        ttk.Checkbutton(self, variable=end_entry_check, style="Custom.TCheckbutton", command=lambda: toogle_entry(end_entry_check, end_entry)).grid(row=7, column=3)

        ttk.Button(self, text="Edit the book", command=self.edit_a_book).grid(row=8, column=0)
        
    def edit_a_book(self):
        # Convert dates entries to None if not provided: 
        start_date = None if self.start_date.get() == "" else self.start_date.get()
        end_date = None if self.end_date.get() == "" else self.end_date.get()

        for field in self.check_vars:
            if self.check_vars[field].get() == 1:
                print(f"Field {field} has been modified")

        # self.page_manager.app_context.library_manager.edit_a_book()

        

    def refresh_data(self):
        book_data = self.page_manager.app_context.get_book_data()
        
        self.title.set(book_data.get("title", ""))
        self.author.set(book_data.get("author", ""))
        self.editor.set(book_data.get("editor", ""))
        self.page_nbr.set(book_data.get("page_nbr", 0))
        self.year_published.set(book_data.get(("year_published", 0)))
        self.main_genre.set(book_data.get("main_genre", ""))
        self.isbn.set(book_data.get("isbn", ""))
        self.is_read.set(book_data.get("is_read", False))
        self.start_date.set(book_data.get("start_date", ""))
        self.end_date.set(book_data.get("end_date", ""))
        if self.is_read:
            self.selected.set("read")
        else:
            if self.start_date != "" and self.start_date:
                self.selected.set("began")
            else:
                self.selected.set("not")
        self.first_selected = self.selected.get()



