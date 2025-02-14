import tkinter as tk
import json

from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo, WARNING

from gui.base_page import BasePage
from gui.edit_book_data_box import EditBox

class LibraryDisplay(BasePage):
    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)
        ttk.Button(self, 
                  text= "Back to home page",
                  command=lambda: self.page_manager.show_page("home")
                  ).grid(row=2)
        
        # create the right-click pop-up menu
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Edit this book", command=self.edit_book)
        self.menu.add_command(label="Delete this book", command=self.delete_book)

        self.tree = self.create_tree_widget()
        self.tree.bind("<Button-3>", self.treeview_right_click)

    def sort_column(self, tree, col, reverse, display_names):
         # Retrieve column index
        col_index = list(tree["columns"]).index(col)

        # Fetch all rows with their values and item IDs
        items = [(tree.set(item, col), item) for item in tree.get_children("")]

        # Attempt to sort numerically, else default to lexicographical sorting
        try:
            items.sort(key=lambda x: float(x[0]), reverse=reverse)
        except ValueError:
            items.sort(key=lambda x: x[0], reverse=reverse)

        # Reorder rows in the Treeview
        for index, (_, item) in enumerate(items):
            tree.move(item, "", index)

        # Toggle the sorting order for next click
        tree.heading(col, text=display_names[col], command=lambda: self.sort_column(tree, col, not reverse, display_names))

    def treeview_right_click(self, event):
        self.selected_item_id = self.tree.identify_row(event.y)
        column_id = self.tree.identify_column(event.x)
        
        if self.selected_item_id:
            self.tree.selection_set(self.selected_item_id)
            column_display_name = self.tree.heading(column_id)["text"]
            self.selected_field = self.name_to_column_id.get(column_display_name)
            self.menu.post(event.x_root, event.y_root)

    def refresh_display(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.populate_tree(self.tree)

    def populate_tree(self, tree):
        book_library = self.page_manager.app_context.books_library.library
        for book in book_library:
            tree.insert("", "end", book["id"], values= (
                book["title"], book["author"], book["editor"], 
                book["page_nbr"], book["year_published"],
                book["main_genre"], book["sub_genre"]))
        pers_library = self.page_manager.app_context.personal_library.library
        for book in pers_library:
            book_id = book["id"]
            old_values = tree.item(book_id)["values"]
            new_values = list(old_values) + [book["is_read"], book["start_date"], book["end_date"], book["reading_time"]]
            tree.item(book_id, values=tuple(new_values))

    def create_tree_widget(self):
        # Create a container frame for the treeview + scrollbars
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        # Initialize the treeview columns
        columns = ("title", "author", "editor", "page_nbr", "year_published", "main_genre", "sub_genre", "is_read", "start_date", "end_date", "reading_time")
        display_names = {
            "title": "Title",
            "author": "Author",
            "editor": "Editor",
            "page_nbr": "Pages",
            "year_published": "Year",
            "main_genre": "Main Genre",
            "sub_genre": "Sub Genre",
            "is_read": "Book Read?",
            "start_date": "Start Date",
            "end_date": "End Date",
            "reading_time": "Reading Duration"
        }

        # Create a reverse mapping for display names to column IDs
        self.name_to_column_id = {v: k for k, v in display_names.items()}

        # Apply styles to disable resizing
        style = ttk.Style()
        style.configure("Treeview.Heading", handlepad=0)

        tree = ttk.Treeview(container, columns= columns, show="headings", style="Treeview")
        tree.update_idletasks()
    
        # Define headings with sorting function
        for col, display_name in display_names.items():
            tree.heading(
                col,
                text=display_name,
                command=lambda c=col: self.sort_column(tree, c, False, display_names)
            )
        
    
        # Populate the treeview
        self.populate_tree(tree)
            

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

        return tree
        

    def adjust_column_widths(self, tree, columns, padding=5):
        for col in columns:
            max_width = len(col)
            for item in tree.get_children():
                cell_value = tree.item(item, "values")[columns.index(col)]
                max_width = max(max_width, len(str(cell_value)))
            tree.column(col, width=(max_width + padding) * 7, stretch=tk.NO)

    def edit_book(self):
        selected_item = self.tree.selection()
        if selected_item:
            book_id = selected_item[0]
            print(f"Editing book with ID: {book_id}")
            self.open_edit_window(book_id)
        else:
            print("No item selected for editing!")


    def open_edit_window(self, book_id):
        self.page_manager.app_context.book_selected_id = book_id
        self.page_manager.app_context.book_selected_field = self.selected_field
        self.page_manager.app_context.get_book_data()
        EditBox(self, self.page_manager)

    def delete_book(self):
        selected_book = self.tree.selection()
        if selected_book:
            book_id = selected_book[0]
            answer = askyesno(
                title="Delete confirmation",
                message=f"Are you sure to PERMANENTLY DELETE this book ??",
                icon=WARNING
            )
            if answer:
                self.page_manager.app_context.library_manager.remove_book(book_id)
                self.refresh_display()


        """
        self.page_manager.edit_page.refresh_data()
        self.page_manager.show_page("edit_book")
        """





