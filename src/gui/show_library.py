import tkinter as tk
import json

from tkinter import ttk

from managers.library import BookLibrary

class LibraryDisplay(ttk.Frame):
    def __init__(self, parent, page_manager):
        super().__init__(parent)
        self.page_manager = page_manager
        ttk.Button(self, 
                  text= "Back to home page",
                  command=lambda: self.page_manager.show_page("home")
                  ).grid(row=2)
        
        self.tree = self.create_tree_widget()



    def create_tree_widget(self):
        # Create a container frame for the treeview + scrollbars
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        # Initialize the treeview
        columns = ("title", "author", "editor", "pages", "year", "main_genre", "sub_genre")
        # Apply styles to disable resizing
        style = ttk.Style()
        style.configure("Treeview.Heading", handlepad=0)

        tree = ttk.Treeview(container, columns= columns, show="headings", style="Treeview")
        tree.update_idletasks()
    
        # Define headings
        tree.heading("title", text= "Title")
        tree.heading("author", text= "Author")
        tree.heading("editor", text= "Editor")
        tree.heading("pages", text= "Pages")
        tree.heading("year", text= "Year")
        tree.heading("main_genre", text= "Main genre")
        tree.heading("sub_genre", text= "Sub genre")

    
        # Populate the treeview
        book_library = BookLibrary().library
        for book in book_library:
            tree.insert("", "end", book["id"], values= (
                book["title"], book["author"], book["editor"], 
                book["page_nbr"], book["year_published"],
                book["main_genre"], book["sub_genre"]))
            

        # Adjust column widths
        self.adjust_column_widths(tree, columns)

        # Add the treeview to the container and configure its grid
        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # Add scrollbars
        scrollbar_v = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        scrollbar_h = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=scrollbar_v.set)
        tree.configure(xscrollcommand=scrollbar_h.set)
        scrollbar_v.grid(row=0, column=1, sticky=tk.NS)
        scrollbar_h.grid(row=1, column=0, sticky=tk.EW)

        # Configure the container to expand properly within the parent frame
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        

    def adjust_column_widths(self, tree, columns, padding=5):
        for col in columns:
            max_width = len(col)
            for item in tree.get_children():
                cell_value = tree.item(item, "values")[columns.index(col)]
                max_width = max(max_width, len(str(cell_value)))
            tree.column(col, width=(max_width + padding) * 7, stretch=tk.NO)





