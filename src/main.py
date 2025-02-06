from models.book import Book, ReadingRecord
from enums.book_enums import BookType, NovelGenre
from datetime import date, datetime

def main():
    book1 = Book("Silo generations", "Hugh Howey", "Le livre de poche", 540, 2017, BookType.NOVEL, NovelGenre.SF)

    print(book1)
    read = ReadingRecord(book1)
    read.is_read = False
    print(read)

main()