from managers.library import BookLibrary, PersonalLibrary, LibraryManager

class AppContext:
    def __init__(self):
        self.personal_library = PersonalLibrary()
        self.books_library = BookLibrary()
        self.library_manager = LibraryManager(self.books_library, self.personal_library)
        self.book_selected_id = None
        self.book_selected_field = None
        self.book_selected_data = None
        
    def get_book_data(self):
        self.book_selected_data = self.library_manager.find_book_and_record(self.book_selected_id)