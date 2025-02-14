import tkinter as tk
from tkinter import ttk

from gui.home_page import HomePage
from gui.add_book_page import AddBookPage
from gui.show_library_page import LibraryDisplay
from gui.edit_book_page import EditPage



class PageManager:
    def __init__(self, root, app_context):
        
        self.root = root
        self.current_frame = None
        self.app_context = app_context

        self.style = ttk.Style()
        
        self.style.theme_use("default")

        self.style.configure('Page.TFrame', background="white")

        # define a layout for Custom Label Frame (since it's missing)
        self.style.layout(
            'Custom.TLabelFrame',
            [('LabelFrame.border', {'sticky': 'nswe', 'children': [
                ('LabelFrame.padding', {'sticky': 'nswe', 'children': [
                    ('LabelFrame.label', {'sticky': 'w'}),
                    ('LabelFrame.frame', {'sticky': 'nswe'})
                ]})
            ]})]
        )


        # Configure this layout
        self.style.configure(
            'Custom.TLabelFrame',  
            background="white",  
            relief="groove",
            borderwidth=2
        )
        self.style.configure(
            'Custom.TLabelFrame.Label', 
            background="white",      
        )

        # define a layout for Custom Radio Buttons (since it's missing)
        self.style.layout(
            "Custom.TRadiobutton",
            [
                ("Radiobutton.padding", {"children": [
                    ("Radiobutton.indicator", {"side": "left"}),  
                    ("Radiobutton.label", {"side": "right"}),  
                ]})
            ]
        )

        self.style.configure(
            "Custom.TRadiobutton",
            background="white",         # Background of the radio button
            foreground="black",         # Text color
            padding=5                   # Padding around the content
        )

        # Define a layout and custom style for Check Button
        self.style.layout(
            "Custom.TCheckbutton", [
            ("Checkbutton.padding", {
                "children": [
                    ("Checkbutton.indicator", {"side": "left"}),
                    ("Checkbutton.label", {"side": "left"})
                ],
                "sticky": "nswe",
            })
        ]
        )
        self.style.configure(
            "Custom.TCheckbutton",
            background="white"
        )
        self.style.map("Custom.TCheckbutton", background=[('active', 'white')])

        self.home_page = HomePage(self.root, self)
        self.add_book_page = AddBookPage(self.root, self)
        self.library_page = LibraryDisplay(self.root, self)
        self.edit_page = EditPage(self.root, self)


    def show_page(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
            
        if page_name == "home":
            self.add_book_page.reset_form()
            self.current_frame = self.home_page
        elif page_name == "add_book":
            self.current_frame = self.add_book_page
        elif page_name == "book_library":
            self.current_frame = self.library_page
        elif page_name == "edit_book":
            self.current_frame = self.edit_page

        self.current_frame.pack(fill= "both", expand=True)