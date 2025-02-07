from datetime import datetime, date
from book_types.book_type_and_genre import BookTypes
from helpers.generate_id import generate_id

class Book:
    def __init__(self, title, author, editor=None, page_nbr=None, year_published=None, type=None, genre=None, isbn=None):
        if not title.strip() or not author.strip():
            raise ValueError("Title or Author are required")

        if year_published != None and year_published > date.today().year:
            raise ValueError("Publication year cannot be in the future")
        
        if page_nbr != None and page_nbr <= 0:
            raise ValueError("Page number must be positive")
        
        self.id = generate_id(title, author)

        self.title = title
        self.author = author
        self.page_nbr = page_nbr
        self.editor = editor
        self.year_published = year_published

        self.type = type
        self.genre = genre

        self.isbn = isbn
        

    def __repr__(self):
        return f"Book :\nTitle = {self.title}\nAuthor = {self.author}\nEditor = {self.editor}\nPage number = {self.page_nbr}\nYear published = {self.year_published}\nType = {self.type}\nGenre = {self.genre}"
    
class ReadingRecord:
    def __init__(self, book:Book, is_read=False):
        self.id = book.id
        self.is_read = is_read
        self.start_date = None
        self.end_date = None

    def begin_reading(self, start_date):
        self.start_date = start_date

    def finish_reading(self, end_date):
        self.is_read = True
        if end_date != None:
            self.end_date = end_date
        else:
            self.end_date = "Unknown"

    def __repr__(self):
        if self.is_read:
            return f"This book has been read. Beginning : {self.start_date}, end : {self.end_date}."
        elif self.start_date != None:
            return f"This book is currently being read. Beginning : {self.start_date}"
        else:
            return f"This book hasn't been read yet."
        