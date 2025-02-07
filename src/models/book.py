from datetime import datetime, date
from book_types.book_type_and_genre import BookTypes

class Book:
    def __init__(self, title:str, author:str, editor:str, page_nbr:int, year_published:int, type, genre):
        if not title.strip():
            raise ValueError("Title cannot be empty")

        if year_published > date.today().year:
            raise ValueError("Publication year cannot be in the future")
        
        if page_nbr <= 0:
            raise ValueError("Page number must be positive")
        
        self.title = title
        self.author = author
        self.page_nbr = page_nbr
        self.editor = editor
        self.year_published = year_published

        self.type = type
        self.genre = genre


    def __repr__(self):
        return f"Book :\nTitle = {self.title}\nAuthor = {self.author}\nEditor = {self.editor}\nPage number = {self.page_nbr}\nYear published = {self.year_published}\nType = {self.type}\nGenre = {self.genre} "
    
class ReadingRecord:
    def __init__(self, book:Book, is_read=False):
        self.book = book
        self.is_read = is_read
        self.start_date = None
        self.end_date = None

    def __repr__(self):
        if self.is_read:
            return f"This book has been read. Beginning : {self.start_date}, end : {self.end_date}."
        elif self.start_date != None:
            return f"This book is currently being read. Beginning : {self.start_date}"
        else:
            return f"This book hasn't been read yet."
        
    def as_dict(self):
        return {"is_read": self.is_read, "start_date": self.start_date, "end_date": self.end_date}