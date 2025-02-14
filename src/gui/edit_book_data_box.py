import tkinter as tk
from tkinter import ttk

class EditBox:
    def __init__(self, parent, page_manager):
        self.parent = parent
        self.page_manager = page_manager
        self.field_to_edit = self.page_manager.app_context.book_selected_field
        self.book_selected_id = self.page_manager.app_context.book_selected_id
        self.old_value = self.page_manager.app_context.book_selected_data[self.field_to_edit]
        if isinstance(self.old_value, int):
            self.new_value = tk.IntVar()
        elif isinstance(self.old_value, bool):
            self.new_value = tk.BooleanVar()
        else:
            self.new_value = tk.StringVar()
        self.new_value.set(self.old_value)

        def dismiss():
            box.grab_release()
            box.destroy()

        def valid_editing():
            success = self.page_manager.app_context.library_manager.edit_a_book(
                book_id = self.book_selected_id,
                field_to_edit = self.field_to_edit,
                new_value = self.new_value.get()
            )
            if success:
                self.parent.refresh_display()
                dismiss()
            else:
                print(f"Cannot edit {self.field_to_edit} in book ID {self.book_selected_id}")

        box = tk.Toplevel(self.parent)

        
        ttk.Label(box, text=f"Editing {self.field_to_edit}").grid(row=0, columnspan=2, padx=5, pady=5)
        ttk.Entry(box, textvariable=self.new_value).grid(row=1, columnspan=2, padx=5, pady=5)
        ttk.Button(box, text="Cancel", command=dismiss).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(box, text="Valid editing", command=valid_editing).grid(row=2, column=0, padx=5, pady=5)


        box.protocol("WM_DELETE_WINDOW", dismiss)
        box.transient(self.parent)
        box.wait_visibility()
        box.grab_set()
        box.wait_window()


        
