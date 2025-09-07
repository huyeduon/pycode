class Book:
    """A class to model a book
    
    """
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.num_pages = 230

    def read_book(self):
        print(f"Reading (a physical book) {self.title} by {self.author}")

    def describe_book(self):
        print(f"{self.title} by {self.author}, genre: {self.genre}")

    def get_num_pages(self):
        print(f"The {self.title} has {self.num_pages} pages")
    
    def update_page_num(self, new_pages):
        self.num_pages = new_pages
        print(f"{self.title} updated number of pages to {self.num_pages}")


class EBook(Book):
    def __init__(self, title, author, genre, filesize, format_):
        super().__init__(title,author, genre)
        self.filesize = filesize # type: ignore
        self.format = format_

    def download_book(self):
        print(f"Downloading {self.title} in {self.format} format ({self.filesize} MB)")


    def read_book(self):
        print(f"Reading {self.title} on an e-reader device...")

    def describe_book(self):
        super().describe_book()
        print(f"File Size: {self.filesize} MB, Format: {self.format}")
    

# book = Book(title="Runner", author="Me", genre="Classic")
# book.read_book()
# ebook = EBook(title="To be or not to be", author="William", genre="fiction" ,format_="ebook", filesize=120)
# print(ebook.download_book())
# ebook.read_book()
